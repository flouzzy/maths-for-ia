with open('jalon-11/jalon-11.tex', 'r') as f:
    lines = f.readlines()
print("".join(lines[:30]) + "...\n[Output truncated for brevity]\n..." + "".join(lines[-30:]))
