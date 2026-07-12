---
title: "Exercice 5 : Cas d'égalité dans Cauchy-Schwarz"
difficulty: 3
---

## Énoncé
Soit $E$ un espace préhilbertien réel avec son produit scalaire $\langle \cdot, \cdot \rangle$.
L'inégalité de Cauchy-Schwarz stipule que $|\langle x, y \rangle| \le \|x\| \|y\|$.
Démontrer que l'égalité $|\langle x, y \rangle| = \|x\| \|y\|$ se produit si et seulement si les vecteurs $x$ et $y$ sont colinéaires (c'est-à-dire que la famille $(x, y)$ est liée).

## Correction Détaillée
Soient $x, y \in E$. Nous devons prouver une équivalence ($A \iff B$).

**Sens direct ($\implies$) : Supposons que l'égalité est vérifiée.**
Hypothèse : $|\langle x, y \rangle| = \|x\| \|y\|$.
Si $y = 0_E$, la famille $(x, 0_E)$ est liée (car $0 \cdot x + 1 \cdot 0_E = 0_E$ avec des coefficients non tous nuls).
Supposons désormais $y \neq 0_E$. Considérons le polynôme défini dans la preuve classique :
$$P(\lambda) = \|x + \lambda y\|^2 = \|x\|^2 + 2\lambda\langle x, y \rangle + \lambda^2\|y\|^2$$
$P$ est un trinôme du second degré en $\lambda$. Son discriminant $\Delta$ est :
$$\Delta = (2\langle x, y \rangle)^2 - 4\|y\|^2\|x\|^2 = 4(\langle x, y \rangle^2 - \|x\|^2\|y\|^2)$$
Par hypothèse, $\langle x, y \rangle^2 = \|x\|^2\|y\|^2$, donc $\Delta = 0$.
Puisque le discriminant est nul, le trinôme possède une racine double $\lambda_0 = -\frac{2\langle x, y \rangle}{2\|y\|^2} = -\frac{\langle x, y \rangle}{\|y\|^2} \in \mathbb{R}$.
Pour cette valeur $\lambda_0$, le polynôme s'annule :
$P(\lambda_0) = 0 \implies \|x + \lambda_0 y\|^2 = 0$.
Par séparation de la norme, cela implique $x + \lambda_0 y = 0_E$, soit $x = -\lambda_0 y$.
Ainsi, $x$ s'écrit comme un multiple scalaire de $y$. Les vecteurs $x$ et $y$ sont donc colinéaires, et la famille $(x, y)$ est liée.

**Sens réciproque ($\impliedby$) : Supposons que $(x, y)$ est une famille liée.**
Si la famille est liée, l'un des vecteurs s'écrit comme combinaison linéaire de l'autre.
- Cas 1 : $y = 0_E$. L'égalité $|\langle x, 0_E \rangle| = |0| = 0$ et $\|x\|\|0_E\| = \|x\| \cdot 0 = 0$ est trivialement vérifiée.
- Cas 2 : $y \neq 0_E$. Alors il existe $\alpha \in \mathbb{R}$ tel que $x = \alpha y$.
Calculons séparément les deux membres de l'égalité :
Membre de gauche :
$|\langle x, y \rangle| = |\langle \alpha y, y \rangle|$
Par linéarité à gauche :
$|\langle x, y \rangle| = |\alpha \langle y, y \rangle| = |\alpha| \langle y, y \rangle = |\alpha| \|y\|^2$
Membre de droite :
$\|x\| \|y\| = \|\alpha y\| \|y\|$
Par propriété d'homogénéité absolue de la norme :
$\|x\| \|y\| = (|\alpha| \|y\|) \|y\| = |\alpha| \|y\|^2$
Les deux membres sont strictement égaux pour tout scalaire $\alpha$.

**Conclusion :**
On a bien démontré l'équivalence. L'inégalité de Cauchy-Schwarz est une égalité si et seulement si les vecteurs sont colinéaires.
