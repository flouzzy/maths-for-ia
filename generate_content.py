import os
import sys
from google import genai

def is_safe_path(basedir, path):
    abs_base = os.path.abspath(basedir)
    abs_path = os.path.abspath(path)
    return os.path.commonpath([abs_base, abs_path]) == abs_base

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_content.py <prompt_file> <output_file>")
        sys.exit(1)

    base_dir = os.getcwd()
    prompt_file = sys.argv[1]
    output_file = sys.argv[2]

    if not is_safe_path(base_dir, prompt_file) or not is_safe_path(base_dir, output_file):
        print("Error: Path traversal detected.", file=sys.stderr)
        sys.exit(1)

    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt = f.read()

    client = genai.Client()
    response = client.models.generate_content(
        model='gemini-2.5-pro', # Or use flash depending on complexity
        contents=prompt
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(response.text)

if __name__ == '__main__':
    main()
