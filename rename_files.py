import os
import glob

def clean_filename(filename):
    # Remove specific mojibake
    replacements = {
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
        '$-mathbb{R}$': 'R'
    }

    new_name = filename
    for bad, good in replacements.items():
        new_name = new_name.replace(bad, good)

    # Remove any remaining $ or \
    new_name = new_name.replace('$', '')
    new_name = new_name.replace('\\', '')

    return new_name

def main():
    files = glob.glob("Jalon *.md") + glob.glob("Jalons *.md")
    for file in files:
        new_name = clean_filename(file)
        if new_name != file:
            print(f"Renaming: '{file}' -> '{new_name}'")
            os.rename(file, new_name)

if __name__ == '__main__':
    main()
