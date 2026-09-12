import re
import os

# Fix jalon-67/Jalon-67.md (next target is Jalon 68 (...).md not Jalon-68.md)
f = "jalon-67/Jalon-67.md"
with open(f, "r") as file:
    content = file.read()
content = content.replace('next: "[[jalon-68/Jalon-68.md]]"', 'next: "[[jalon-68/Jalon 68 (Lemme de Fatou et définition de l\'intégrale pour les fonctions de signe quelconque).md]]"')
with open(f, "w") as file:
    file.write(content)

# Fix jalon-66/Jalon-66.md
f = "jalon-66/Jalon-66.md"
with open(f, "r") as file:
    content = file.read()
content = content.replace('next: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"', 'next: "[[jalon-67/Jalon-67.md|Jalon 67 (Démonstration du théorème de convergence monotone)]]"')
with open(f, "w") as file:
    file.write(content)

# Fix jalon-68
f = "jalon-68/Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md"
with open(f, "r") as file:
    content = file.read()
content = content.replace('prev: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"', 'prev: "[[jalon-67/Jalon-67.md|Jalon 67 (Démonstration du théorème de convergence monotone)]]"')
content = content.replace('[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]', '[[jalon-67/Jalon-67.md|Jalon 67 (Démonstration du théorème de convergence monotone)]]')
with open(f, "w") as file:
    file.write(content)
