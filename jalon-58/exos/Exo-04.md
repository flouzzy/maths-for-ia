---
uuid: "jalon-58-exo-04"
title: "Exercice 04 : Les points de continuité des fonctions limites"
---

## Les points de continuité des fonctions limites \quad $\bigstar\bigstar\bigstar\star\star$

Soit $f: X \to \mathbb{R}$ la limite simple d'une suite de fonctions continues $(f_n)$ sur un espace complet $X$. Montrer que l'ensemble des points de discontinuité de $f$ est maigre (union dénombrable de nulle part denses).

## Correction Détaillée (Zéro Ellipse)


1. Soit $\omega_f(x)$ l'oscillation de $f$ en $x$. $f$ est continue en $x$ si et seulement si $\omega_f(x) = 0$.
2. L'ensemble des points de discontinuité de $f$ est $D = \{x \in X \mid \omega_f(x) > 0\} = \bigcup_{k \geq 1} \{x \in X \mid \omega_f(x) \geq 1/k\}$.
3. Pour un $\epsilon > 0$, l'ensemble $O_\epsilon = \{x \in X \mid \omega_f(x) \geq \epsilon\}$ peut s'écrire en fonction des $f_n$.
4. Considérons $F_{n, m} = \{x \in X \mid |f_n(x) - f_m(x)| \leq \epsilon / 3\}$.
5. Par le théorème d'Osgood (qui repose sur le théorème de Baire), comme $(f_n)$ converge simplement, on peut prouver que les ensembles fermés où l'oscillation de $f$ est grande sont d'intérieur vide.
6. Précisément, $D$ est une union dénombrable de tels ensembles (qui sont fermés ou inclus dans des fermés d'intérieur vide).
7. Ainsi, $D$ est maigre. En d'autres termes, l'ensemble des points de continuité d'une limite simple de fonctions continues est un sous-ensemble dense (intersection dénombrable d'ouverts denses).
