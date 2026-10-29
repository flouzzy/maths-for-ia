import re

with open("jalon-99.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    # Just aggressively wrap L^2 in math mode or escape
    if "L^2" in line:
        lines[i] = line.replace("L^2", "$L^2$")
    if "L^p" in line:
        lines[i] = line.replace("L^p", "$L^p$")

with open("jalon-99.tex", "w", encoding="utf-8") as f:
    f.writelines(lines)
