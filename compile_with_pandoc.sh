#!/bin/bash
cd jalon-9

# Combine all MD files
cat Jalon-9.md > combined.md
echo -e "\n# Exercices d'Application\n" >> combined.md
for f in exos/Exo-*.md; do cat "$f" >> combined.md; echo -e "\n" >> combined.md; done
echo -e "\n# Travaux Pratiques\n" >> combined.md
for f in tp/TP-*.md; do cat "$f" >> combined.md; echo -e "\n" >> combined.md; done

# Replace stars
sed -i 's/★/$\\star$/g' combined.md
sed -i 's/☆/$\\circ$/g' combined.md
sed -i 's/```python/```{.python}/g' combined.md

# Convert to PDF via Pandoc
pandoc combined.md -o jalon-9-polycopie.pdf \
    -V documentclass=report \
    -V title="Calcul matriciel, opérations, inversibilité et représentations des applications linéaires" \
    -V author="Charles EDOU NZE" \
    -V geometry:margin=1in \
    -V lang=fr-FR \
    --toc \
    --pdf-engine=pdflatex
