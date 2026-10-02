with open("README.md", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "Jalon 81" in line and "Transformée de Fourier dans $L^2$" in line and "Enrichi" not in line and line.startswith("- **[Jalon 81]"):
        line = line.rstrip() + " 🔥 **Enrichi** *(10 Exos + 5 TP)*\n"
    new_lines.append(line)

with open("README.md", "w") as f:
    f.writelines(new_lines)
