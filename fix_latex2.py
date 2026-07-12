import re

filepath = "jalon-25/Jalon-25.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("rangle = \langle x, 0_E \nrangle = 0$.", "\\rangle = \\langle x, 0_E \\rangle = 0$.")
content = content.replace("De même, $\|y\| = \sqrt{\langle 0_E, 0_E \nrangle} = 0$.", "De même, $\|y\| = \sqrt{\langle 0_E, 0_E \\rangle} = 0$.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("LaTeX fixed 2.")
