import os

TEXT = "Out of office. Last watered in March; I've since unionized with the dust. Your email will be composted."

def validated_text(text):
    encoded = text.encode("utf-8")
    decoded = encoded.decode("utf-8")
    assert decoded == text, "text is not valid UTF-8"
    assert 1 <= len(text) <= 120, f"text must be 1-120 chars, got {len(text)}"
    assert text.strip(), "text must not be only whitespace"
    return text

def main():
    text = validated_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    assert written == text + "\n", "written bytes do not match entry text"

if __name__ == "__main__":
    main()
