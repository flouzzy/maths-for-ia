---
uuid: "jalon-58-exo-06"
title: "Exercice 06 : Séries de Fourier divergentes"
---

## Séries de Fourier divergentes \quad $\bigstar\bigstar\bigstar\bigstar\star$

Montrer que l'ensemble des fonctions continues périodiques dont la série de Fourier diverge en 0 est dense dans l'espace des fonctions continues périodiques.

## Correction Détaillée (Zéro Ellipse)


1. Soit $E = \{f \in \mathcal{C}_{2\pi} \mid f(0) = f(2\pi)\}$ muni de la norme uniforme.
2. La $N$-ième somme partielle de la série de Fourier en 0 est $S_N(f)(0) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) D_N(t) dt$, où $D_N$ est le noyau de Dirichlet.
3. Considérons les formes linéaires continues $T_N : E \to \mathbb{R}$ définies par $T_N(f) = S_N(f)(0)$.
4. La norme de l'opérateur $T_N$ est $\|T_N\| = \frac{1}{2\pi} \int_{-\pi}^{\pi} |D_N(t)| dt$. On sait que cette norme (constante de Lebesgue) tend vers l'infini avec $N$.
5. Par le théorème de Banach-Steinhaus (une conséquence de Baire), comme $\sup_N \|T_N\| = \infty$, il existe un sous-ensemble $G_\delta$ dense de fonctions $f \in E$ telles que $\sup_N |T_N(f)| = \infty$.
6. Ainsi, pour ces fonctions, la suite $(S_N(f)(0))$ n'est pas bornée, donc la série de Fourier diverge en 0.
