import sys
from google import genai

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_content.py <prompt_file> <output_file>")
        sys.exit(1)

    prompt_file = sys.argv[1]
    output_file = sys.argv[2]

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
