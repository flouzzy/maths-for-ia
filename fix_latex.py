import re

filepath = "jalon-25/Jalon-25.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("angle = \langle", "rangle = \langle")
content = content.replace("angle = 0$.", "rangle = 0$.")
content = content.replace("angle} = 0$.", "rangle} = 0$.")
content = content.replace("\nangle", "\\rangle")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("LaTeX fixed.")
