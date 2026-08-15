---
title: "Exo 09 : Rôle crucial du compact"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exo 09 : Rôle crucial du compact

## Énoncé formel
Expliquer, preuve géométrique à l'appui, pourquoi le théorème de Cybenko ne s'applique pas sur l'espace tout entier $\mathbb{R}^n$, c'est-à-dire qu'un réseau de neurones à taille fixe $N$ (aussi grand soit-il) ne peut pas approximer la fonction $f(x) = x^2$ de façon uniformément proche sur $\mathbb{R}$.

---

## Démonstration et correction pas à pas
Un réseau à une couche cachée de taille $N$ avec des activations sigmoïdales bornées (comme Tanh ou Logistique) génère des fonctions de la forme $G(x) = \sum_{i=1}^N \alpha_i \sigma(w_i x + b_i)$.\nPuisque $\sigma$ est bornée (disons $|\sigma(t)| \le 1$), alors pour tout $x \in \mathbb{R}$, on a la majoration globale absolue :\n$$ |G(x)| \le \sum_{i=1}^N |\alpha_i| |\sigma(w_i x + b_i)| \le \sum_{i=1}^N |\alpha_i| = M $$\nLa fonction du réseau $G(x)$ est donc intrinsèquement bornée par la somme des normes des poids de la couche de sortie, notée $M$. Cette constante $M$ est fixée dès que l'entraînement est achevé (poids gelés).\nEn revanche, la fonction cible $f(x) = x^2$ tend vers $+\infty$ lorsque $|x| \to \infty$. Elle est non bornée sur $\mathbb{R}$.\nL'erreur uniforme sur $\mathbb{R}$ est :\n$$ \|f - G\|_{L^\infty(\mathbb{R})} = \sup_{x \in \mathbb{R}} |x^2 - G(x)| $$\nPour des $x$ suffisamment grands, $x^2 > M + 1$, ce qui garantit $|x^2 - G(x)| \ge (M+1) - M = 1$. L'erreur suprémum est donc toujours infinie, peu importe le nombre fini $N$ de neurones choisis. C'est pourquoi le théorème exige un domaine compact $K$, où toute fonction continue $f$ atteint ses bornes (théorème de Weierstrass) et peut donc coexister avec l'enveloppe bornée du réseau.
