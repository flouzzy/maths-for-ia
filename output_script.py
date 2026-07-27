import sys

def print_chunks(filename, chunk_size=30000):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We write it out to standard output and redirect it in bash
    sys.stdout.write(content)

print_chunks('/tmp/output.tex')
