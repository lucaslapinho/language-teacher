"""Validate release packages, documentation links, and empty progress templates."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys
import zipfile

from build import LANGUAGES, PROJECT_FILES, ROOT, SHARED
from plugin_checks import validate as validate_plugin


def validate():
    checks = []

    def check(name, passed, detail=""):
        checks.append({"check": name, "passed": bool(passed), "detail": detail})

    dist = ROOT / "dist"
    plugin = dist / "Language-Teacher-Plugin.zip"
    project = dist / "Language-Teacher-Project.zip"
    if not plugin.exists() or not project.exists():
        print("Run python scripts/build.py before validation.", file=sys.stderr)
        return 1
    checks.extend(validate_plugin(plugin))
    instructions = (ROOT / "project/project-instructions.md").read_text(encoding="utf-8")
    count = len(instructions.encode("utf-16-le")) // 2
    check("project_instruction_budget", count <= 7500, f"{count} UTF-16 code units; conservative budget 7500")

    template = json.loads((ROOT / "project/learning-progress.json").read_text(encoding="utf-8"))
    empty = template["record_revision"] == 0 and template["updated_at"] is None and template["active_language"] is None
    for state in template["languages"].values():
        empty &= all(not state[key] for key in (
            "objectives", "practiced_content", "recurrent_errors", "vocabulary",
            "review_items", "evidence", "sessions",
        ))
        empty &= all(s["status"] == "not_assessed" and s["estimated_cefr"] is None and not s["evidence_ids"] for s in state["skills"].values())
        empty &= state["gamification"]["points"] == 0 and not state["gamification"]["enabled"]
    check("public_progress_template_empty", empty)

    consistent = True
    for language in LANGUAGES:
        folder = ROOT / "skills" / f"language-{language}-teacher"
        for name in (*SHARED, f"{language}-teacher.md"):
            consistent &= (ROOT / "project" / name).read_bytes() == (folder / "references" / name).read_bytes()
        for canonical, copy in (
            (ROOT / "project/learning-progress.json", folder / "assets/learning-progress.json"),
            (ROOT / "assets/language-teacher-icon.png", folder / "assets/language-teacher-icon.png"),
        ):
            consistent &= canonical.read_bytes() == copy.read_bytes()
    check("shared_resources_consistent", consistent)

    public_files = [file for file in ROOT.rglob("*") if file.is_file() and not any(
        part in {".git", "dist", "__pycache__", "personal-progress"} for part in file.relative_to(ROOT).parts
    )]
    missing, leaks = [], []
    for file in public_files:
        if file.suffix not in {".md", ".json", ".yaml", ".py"}:
            continue
        text = file.read_text(encoding="utf-8")
        if re.search(r"[A-Za-z]:[/\\]Users[/\\]|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}", text):
            leaks.append(file.relative_to(ROOT).as_posix())
        if file.suffix != ".md":
            continue
        links = re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r'(?:src|href)="([^"]+)"', text)
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (file.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                missing.append(f"{file.relative_to(ROOT).as_posix()}: {link}")
    check("local_document_links", not missing, "; ".join(missing))
    check("no_local_user_paths_or_token_patterns", not leaks, "; ".join(leaks))
    check("readme_images_present", all((ROOT / name).is_file() and (ROOT / name).stat().st_size > 1000 for name in (
        "assets/language-teacher-icon.png", "docs/images/language-teacher-chatgpt.png",
    )))

    with zipfile.ZipFile(project) as package:
        expected = {"Language-Teacher-Project/" + name for name in (*PROJECT_FILES, "LEIA-ME.txt")}
        check("project_zip_integrity_and_contents", package.testzip() is None and set(package.namelist()) == expected)
        check("project_zip_matches_sources", all(package.read("Language-Teacher-Project/" + name) == (ROOT / "project" / name).read_bytes() for name in PROJECT_FILES))
    with zipfile.ZipFile(plugin) as package:
        check("plugin_zip_matches_sources", all(package.read(name) == (ROOT / name.removeprefix("language-teacher/")).read_bytes() for name in package.namelist()))
    sums_ok = True
    lines = (dist / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines()
    sums_ok &= len(lines) == 2
    for line in lines:
        digest, name = line.split("  ", 1)
        sums_ok &= name in {plugin.name, project.name} and hashlib.sha256((dist / name).read_bytes()).hexdigest() == digest
    check("release_checksums", sums_ok)

    report = {"passed": all(item["passed"] for item in checks), "checks": checks}
    (dist / "validation-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    for item in checks:
        if not item["passed"]:
            print(f"FAIL {item['check']}: {item['detail']}")
    print(f"{sum(item['passed'] for item in checks)}/{len(checks)} local checks passed.")
    print("Report: dist/validation-report.json. Server-side import is not simulated.")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(validate())
