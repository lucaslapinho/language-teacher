"""Check documented import invariants locally; does not simulate the ChatGPT service."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import struct
import sys
import unicodedata
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[1]


def validate(archive):
    checks = []
    def check(name, condition, detail=""):
        checks.append({"check": name, "passed": bool(condition), "detail": detail})
    with zipfile.ZipFile(archive) as z:
        files = [i for i in z.infolist() if not i.is_dir()]
        names = [i.filename for i in files]
        check("zip_integrity", z.testzip() is None)
        check("archive_limits", len(z.infolist()) <= 5000 and sum(i.file_size for i in files) <= 512 * 1024**2 and archive.stat().st_size <= 100_000_000 and all(i.file_size <= 100 * 1024**2 for i in files))
        check("safe_unique_paths", all(n == n.strip() and "\\" not in n and not n.startswith("/") and ":" not in n and ".." not in n.split("/") and len(n.split("/")) <= 20 for n in names) and len(names) == len({unicodedata.normalize("NFC", n).casefold() for n in names}))
        manifests = [n for n in names if n.endswith("/plugin.json") or n == "plugin.json"]
        roots = set()
        for n in manifests:
            parent = PurePosixPath(n).parent
            roots.add(str(parent.parent if parent.name in (".codex-plugin", ".agent-plugin", ".claude-plugin") else parent))
        check("single_plugin_root", len(roots) == 1, "Supported manifest roots: " + repr(sorted(roots)))
        if len(roots) != 1:
            return checks
        base = next(iter(roots))
        prefix = "" if base == "." else base + "/"
        check("root_location_and_siblings", (base == "." or len(PurePosixPath(base).parts) == 1) and all(n.startswith(prefix) for n in names))
        root_manifest = prefix + "plugin.json"
        overlay_manifest = prefix + ".codex-plugin/plugin.json"
        check("portable_and_compatibility_manifests", root_manifest in names and overlay_manifest in names)
        if root_manifest not in names or overlay_manifest not in names:
            return checks
        p = json.loads(z.read(root_manifest))
        c = json.loads(z.read(overlay_manifest))
        check("portable_schema", p.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
        check("identity", bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", p.get("name", ""))) and bool(re.fullmatch(r"\d+\.\d+\.\d+", p.get("version", ""))) and 0 < len(p.get("description", "")) <= 1024 and 0 < len(p.get("author", {}).get("name", "")) <= 120)
        ui = p.get("extensions", {}).get("com.openai", {}).get("interface", {})
        check("compatibility_consistency", all(p.get(k) == c.get(k) for k in ("name", "version", "description", "author")) and ui == c.get("interface") and c.get("skills") == "./skills/")
        check("listing_metadata", all(isinstance(ui.get(k), str) and 0 < len(ui[k]) <= limit for k, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000), ("developerName", 80))) and ui.get("category") == "Education & Research" and all("\n" not in ui.get(k, "") for k in ("displayName", "shortDescription", "developerName")))
        prompts = ui.get("defaultPrompt", [])
        check("starter_prompts", len(prompts) <= 3 and len(set(prompts)) == len(prompts) and all(isinstance(t, str) and 0 < len(t) <= 128 and "\n" not in t and "@" not in t for t in prompts))
        skills = [n for n in names if n.startswith(prefix + "skills/") and n.endswith("/SKILL.md")]
        check("three_skills_in_root_skills", len(skills) == 3 and all(len(n[len(prefix):].split("/")) == 3 for n in skills))
        header_ok, links_ok, icon_refs = True, True, True
        for name in skills:
            text = z.read(name).decode("utf-8").replace("\r\n", "\n")
            parts = text.split("---", 2)
            header_ok &= len(parts) == 3 and bool(re.search(r"^name: language-(english|spanish|french)-teacher$", parts[1], re.M)) and bool(re.search(r"^description: .+", parts[1], re.M)) and "TODO" not in text
            folder = PurePosixPath(name).parent
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if "://" not in link:
                    links_ok &= str(folder / link.removeprefix("./")) in names
            yml = z.read(str(folder / "agents/openai.yaml")).decode("utf-8")
            for key in ("icon_small", "icon_large"):
                match = re.search(rf'{key}: "([^"\n]+)"', yml)
                icon_refs &= bool(match) and str(folder / match.group(1).removeprefix("./")) in names
            initial = json.loads(z.read(str(folder / "assets/learning-progress.json")))
            check("empty_template_" + folder.name, initial["record_revision"] == 0 and all(not v["evidence"] and not v["sessions"] for v in initial["languages"].values()))
        check("skill_frontmatter", header_ok)
        check("skill_reference_paths", links_ok)
        check("skill_icons", icon_refs)
        for field in ("logo", "composerIcon"):
            rel = ui.get(field, "")
            valid_path = rel.startswith("./assets/") and ".." not in PurePosixPath(rel).parts and prefix + rel[2:] in names
            check(field + "_path", valid_path)
            if not valid_path:
                continue
            png = z.read(prefix + rel[2:])
            valid_png = png[:8] == b"\x89PNG\r\n\x1a\n" and len(png) <= 5 * 1024**2
            width, height, depth, color, compression, filtering, interlace = struct.unpack(">IIBBBBB", png[16:29])
            check(field + "_format_dimensions", valid_png and width == height and 48 <= width <= 4096, f"PNG {width}x{height}; {len(png)} bytes")
            offset, compressed, crc_ok = 8, b"", True
            while offset < len(png):
                size = struct.unpack(">I", png[offset:offset+4])[0]
                kind = png[offset+4:offset+8]
                content = png[offset+8:offset+8+size]
                crc = struct.unpack(">I", png[offset+8+size:offset+12+size])[0]
                crc_ok &= zlib.crc32(kind + content) & 0xffffffff == crc
                if kind == b"IDAT":
                    compressed += content
                offset += 12 + size
            pixels = zlib.decompress(compressed)
            check(field + "_png_integrity", crc_ok and depth == 8 and color == 6 and interlace == 0 and len(pixels) == height * (1 + width * 4), "RGBA data decoded without modifying the image")
        check("skills_only_package", not any(n.endswith((".mcp.json", "mcp.json", ".app.json", "hooks.json", ".py", ".zip")) or "/qa/" in n for n in names))
    return checks
