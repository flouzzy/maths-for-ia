---
title: "Exercice 10 : Matrice de Gram et indépendance linéaire"
difficulty: 5
---

### Exercice 10 : Inégalité de Minkowski par Cauchy-Schwarz
**Niveau : \star \star \star \star \star**

**Énoncé :**
En n'utilisant strictement que l'inégalité de Cauchy-Schwarz, démontrer l'inégalité triangulaire de Minkowski pour la norme induite par un produit scalaire : $\|x + y\| \le \|x\| + \|y\|$.

**Correction (Zéro Ellipse) :**
Développons le carré de la norme de la somme :
\[ \|x + y\|^2 = \langle x + y, x + y \rangle = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2 \]
Selon l'inégalité de Cauchy-Schwarz :
\[ \langle x, y \rangle \le | \langle x, y \rangle | \le \|x\| \|y\| \]
En substituant cette majoration :
\[ \|x + y\|^2 \le \|x\|^2 + 2\|x\| \|y\| + \|y\|^2 = (\|x\| + \|y\|)^2 \]
Puisque la fonction racine carrée est croissante et préserve l'ordre sur les nombres positifs, nous pouvons en déduire :
\[ \sqrt{\|x + y\|^2} \le \sqrt{(\|x\| + \|y\|)^2} \]
\[ \|x + y\| \le \|x\| + \|y\| \]
La démonstration s'achève avec une rigueur absolue.
