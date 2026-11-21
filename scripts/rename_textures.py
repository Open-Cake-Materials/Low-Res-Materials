import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_DIR = ROOT / "Original-Photos"
WORDS_FILE = ROOT / "data" / "words.txt"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALREADY_NAMED_RE = re.compile(r"^[a-z]+-[a-z]+$", re.IGNORECASE)


def load_words(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"Brak pliku z bazą słów: {path}")

    words = []
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        word = re.sub(r"[^a-zA-Z]", "", line).strip().lower()
        if word and word not in seen:
            seen.add(word)
            words.append(word)

    if len(words) < 2:
        raise ValueError("Plik ze słowami musi zawierać co najmniej 2 słowa.")
    return words


def generate_unique_name(words: list[str], ext: str, used_stems: set[str]) -> str:
    max_attempts = 10_000
    for _ in range(max_attempts):
        w1, w2 = random.sample(words, 2)
        stem = f"{w1}-{w2}"
        if stem not in used_stems and not (INPUT_DIR / f"{stem}{ext}").exists():
            used_stems.add(stem)
            return f"{stem}{ext}"
    raise RuntimeError("Nie udało się wylosować unikalnej nazwy.")


def main() -> None:
    if not INPUT_DIR.exists():
        print("Brak katalogu 'Original-Photos'.")
        return

    words = load_words(WORDS_FILE)
    files = sorted(
        p for p in INPUT_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in EXTENSIONS
    )

    used_stems = {p.stem.lower() for p in files}

    for file_path in files:
        if ALREADY_NAMED_RE.match(file_path.stem):
            print(f"Pominięto (już nazwane): {file_path.name}")
            continue

        new_name = generate_unique_name(words, file_path.suffix.lower(), used_stems)
        target_path = file_path.with_name(new_name)
        file_path.rename(target_path)
        print(f"Zmieniono nazwę: {file_path.name} -> {new_name}")


if __name__ == "__main__":
    main()
