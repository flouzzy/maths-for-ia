---
title: "Exo 07 : Approximation trigonométrique par des sigmoïdes"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exo 07 : Approximation trigonométrique par des sigmoïdes

## Énoncé formel
Montrez que si une famille de fonctions $\mathcal{F}$ permet d'approximer uniformément sur $[-\pi, \pi]$ les fonctions $x \mapsto \cos(kx)$ et $x \mapsto \sin(kx)$ pour tout entier $k$, alors par le théorème de Stone-Weierstrass, $\mathcal{F}$ est dense dans $C([-\pi, \pi])$.

---

## Démonstration et correction pas à pas
Le théorème de Stone-Weierstrass stipule qu'une algèbre de fonctions continues sur un compact $K$, qui sépare les points et qui contient les constantes, est dense dans $C(K)$. Si nous regardons le cas périodique, les polynômes trigonométriques $\sum_{k=0}^n a_k \cos(kx) + b_k \sin(kx)$ forment une telle algèbre sur le cercle unitaire (identifié à $[-\pi, \pi]$ avec les bouts recollés).\n\nSi le réseau de neurones $\mathcal{F}$ (qui est déjà un espace vectoriel) est capable d'approximer individuellement la fonction de base $e_k(x) = \cos(kx)$ à une erreur $\epsilon_k$ arbitrairement petite, et la fonction $\sin(kx)$ à une erreur $\epsilon'_k$, alors par linéarité, il peut approximer n'importe quelle somme finie (polynôme trigonométrique) avec une erreur totale limitée par la somme des erreurs, que l'on peut rendre arbitrairement petite.\n\nPuisque tout polynôme trigonométrique peut approcher n'importe quelle fonction continue périodique (Théorème de Fejér) avec une erreur $\delta$, l'inégalité triangulaire garantit que pour toute fonction $f \in C([-\pi, \pi])$, on peut trouver un réseau $G \in \mathcal{F}$ tel que :\n$$\|f - G\|_\infty \le \|f - P\|_\infty + \|P - G\|_\infty < \delta + \epsilon$$\nCela prouve l'universalité d'un approximateur via sa simple capacité à reproduire l'analyse de Fourier.
