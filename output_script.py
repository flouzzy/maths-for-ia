def chunk_file(filepath, chunk_size=30000):
    with open(filepath, 'r') as f:
        content = f.read()
    for i in range(0, len(content), chunk_size):
        yield content[i:i + chunk_size]

for i, chunk in enumerate(chunk_file("jalon-1.tex")):
    print(f"Chunk {i+1}:\n{chunk[:100]}...\n")
