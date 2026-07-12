import re

filepath = "jalon-25/Jalon-25.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("   - Si $y = 0_E$, alors $\langle x, y \n\\rangle = \langle x, 0_E \\rangle = 0$.", "   - Si $y = 0_E$, alors $\\langle x, y \\rangle = \\langle x, 0_E \\rangle = 0$.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("LaTeX fixed 3.")
