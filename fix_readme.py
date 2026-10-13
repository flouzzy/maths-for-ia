import re

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Fix existing links that still point to the old deleted file (Jalon 88, 87, 89, 70)
content = content.replace(
    "[[jalon-87/Jalon-87.md|Jalon 87 : Intégration et Espérance mathématique]]",
    "[[jalon-87/Jalon-87.md|Jalon 87 : Intégration et Espérance mathématique]]"
)
content = content.replace(
    "[[jalon-88/Jalon 88 (Indépendance d'événements).md|Jalon 88 : Indépendance d'événements]]",
    "[[jalon-88/Jalon-88.md|Jalon 88 : Indépendance d'événements]]"
)
content = content.replace(
    "[[jalon-89/Jalon 89 (Lemmes de Borel-Cantelli).md|Jalon 89 : Lemmes de Borel-Cantelli]]",
    "[[jalon-89/Jalon 89 (Lemmes de Borel-Cantelli).md|Jalon 89 : Lemmes de Borel-Cantelli]]"
)

# Fix links in other files if they exist
content = content.replace(
    "jalon-87/Jalon-87.md",
    "jalon-87/Jalon-87.md"
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
