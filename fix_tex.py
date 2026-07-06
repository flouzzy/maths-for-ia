import re

tex_file = "jalon-11/jalon-11.tex"
with open(tex_file, "r", encoding="utf-8") as f:
    content = f.read()

# Fix \chapter{...} inside listings
def fix_listings(match):
    code_block = match.group(0)
    # Revert \chapter{...} back to # ...
    fixed_code = re.sub(r'\\chapter\{(.*?)\}', r'# \1', code_block)
    return fixed_code

content = re.sub(r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}', fix_listings, content, flags=re.DOTALL)

with open(tex_file, "w", encoding="utf-8") as f:
    f.write(content)

print("TeX file fixed.")
