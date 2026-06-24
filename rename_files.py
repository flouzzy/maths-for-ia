import os
import glob
import re

# Remove specific mojibake
REPLACEMENTS = {
    'Ã©': 'e',
    'Ã¨': 'e',
    'Ãª': 'e',
    'Ã«': 'e',
    'Ã ': 'a',
    'Ã¢': 'a',
    'Ã´': 'o',
    'Ã»': 'u',
    'Ã§': 'c',
    'Ã®': 'i',
    'Ã¯': 'i',
    'Ã': 'e', # fallback for cut-off sequences
    '$-mathbb{R}^n$': 'Rn',
    '$-mathcal{L}^p$': 'Lp',
    '$-mathbb{R}$': 'R',
    '$': '',
    '\\': ''
}

# Sort keys by length descending to match longest sequences first, avoiding partial matches
_sorted_keys = sorted(REPLACEMENTS.keys(), key=len, reverse=True)
_PATTERN = re.compile('|'.join(re.escape(k) for k in _sorted_keys))

def _replacer(match):
    return REPLACEMENTS[match.group(0)]

def clean_filename(filename):
    return _PATTERN.sub(_replacer, filename)

def main():
    files = glob.glob("Jalon *.md") + glob.glob("Jalons *.md")
    for file in files:
        new_name = clean_filename(file)
        if new_name != file:
            print(f"Renaming: '{file}' -> '{new_name}'")
            os.rename(file, new_name)

if __name__ == '__main__':
    main()
