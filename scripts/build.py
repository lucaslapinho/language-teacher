"""Build the two distribution archives using only the Python standard library."""
from pathlib import Path
import hashlib
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("english", "spanish", "french")
SHARED = ("teacher-core.md", "progress-format.md", "references.md")
PROJECT_FILES = (
    "project-instructions.md", "teacher-core.md", "english-teacher.md",
    "spanish-teacher.md", "french-teacher.md", "learning-progress.json",
    "progress-format.md", "references.md",
)


def synchronize():
    """Keep runtime resources identical to their canonical project sources."""
    for language in LANGUAGES:
        folder = ROOT / "skills" / f"language-{language}-teacher"
        for name in (*SHARED, f"{language}-teacher.md"):
            shutil.copyfile(ROOT / "project" / name, folder / "references" / name)
        shutil.copyfile(ROOT / "project/learning-progress.json", folder / "assets/learning-progress.json")
        shutil.copyfile(ROOT / "assets/language-teacher-icon.png", folder / "assets/language-teacher-icon.png")


def archive(path, entries):
    """Use stable paths, timestamps, and permissions for repeatable local builds."""
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for name, content in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            output.writestr(info, content)


def build():
    synchronize()
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    plugin_files = [ROOT / "plugin.json", ROOT / ".codex-plugin/plugin.json", ROOT / "assets/language-teacher-icon.png"]
    for language in LANGUAGES:
        folder = ROOT / "skills" / f"language-{language}-teacher"
        plugin_files.extend(folder / name for name in (
            "SKILL.md", "agents/openai.yaml", "assets/learning-progress.json",
            "assets/language-teacher-icon.png", *(f"references/{name}" for name in SHARED),
            f"references/{language}-teacher.md",
        ))
    archive(dist / "Language-Teacher-Plugin.zip", {
        "language-teacher/" + file.relative_to(ROOT).as_posix(): file.read_bytes()
        for file in plugin_files
    })
    project_entries = {
        "Language-Teacher-Project/" + name: (ROOT / "project" / name).read_bytes()
        for name in PROJECT_FILES
    }
    project_entries["Language-Teacher-Project/LEIA-ME.txt"] = (
        "Language Teacher — projeto ChatGPT\n\n"
        "1. Crie um projeto no ChatGPT.\n"
        "2. Copie project-instructions.md para as instruções do projeto.\n"
        "3. Anexe os outros sete arquivos como fontes do projeto.\n"
        "4. Comece: Quero uma aula de inglês de 15 minutos.\n\n"
        "Este ZIP é para extração e configuração manual de um projeto.\n"
        "Para importar um plugin, baixe Language-Teacher-Plugin.zip.\n"
        "Guia: https://github.com/lucaslapinho/language-teacher/blob/main/docs/installation.md\n"
        "Salve seu progresso pessoal fora do repositório público.\n"
    ).encode("utf-8")
    archive(dist / "Language-Teacher-Project.zip", project_entries)
    archives = [dist / "Language-Teacher-Plugin.zip", dist / "Language-Teacher-Project.zip"]
    sums = "".join(f"{hashlib.sha256(file.read_bytes()).hexdigest()}  {file.name}\n" for file in archives)
    (dist / "SHA256SUMS.txt").write_text(sums, encoding="utf-8", newline="\n")
    for file in archives:
        print(f"Built dist/{file.name}: {file.stat().st_size:,} bytes")
    print("Wrote dist/SHA256SUMS.txt")


if __name__ == "__main__":
    build()
