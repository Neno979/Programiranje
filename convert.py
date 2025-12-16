import os
import chardet   # pip install chardet

# ---- CONFIGURATION ----
USB_PATH = r"D:\The_Mandalorian"         # USB drive D:
ANSI_ENCODING = "cp1252"   # Common Windows ANSI encoding
TARGET_EXTENSIONS = (".txt", ".srt")  # Include TXT + SRT

# ---- CHARACTER CONVERSION TABLE ----
CONVERSIONS = {
    "æ": "ć",
    "ð": "đ",
    "è": "č",
    "Æ": "Ć",
    "È": "Č",
}

def modify_text(text):
    for old, new in CONVERSIONS.items():
        text = text.replace(old, new)
    return text

# ---- MAIN PROCESS ----
for root, dirs, files in os.walk(USB_PATH):
    for filename in files:
        if filename.lower().endswith(TARGET_EXTENSIONS):
            full_path = os.path.join(root, filename)

            # Detect encoding
            with open(full_path, "rb") as f:
                raw = f.read()
            enc_guess = chardet.detect(raw)
            encoding = enc_guess["encoding"]

            # Process ANSI-like encodings
            if encoding in ["Windows-1252", "ISO-8859-1", ANSI_ENCODING]:
                try:
                    # Decode using ANSI
                    text = raw.decode(ANSI_ENCODING)

                    # Apply your replacements
                    modified = modify_text(text)

                    # Save in UTF-8
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(modified)

                    print(f"Converted: {full_path}")

                except Exception as e:
                    print(f"Error processing {full_path}: {e}")
