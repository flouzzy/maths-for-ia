---
title: "Exo 06 : La mesure de Lebesgue et la limite discriminatoire"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exo 06 : La mesure de Lebesgue et la limite discriminatoire

## Énoncé formel
Soit $\sigma(t) = \mathbf{1}_{\{t > 0\}}$ la fonction de Heaviside. Soit $\mu$ une mesure finie sur $\mathbb{R}$. Si l'intégrale $\int_{\mathbb{R}} \sigma(wx + b) d\mu(x) = 0$ pour tous $w, b \in \mathbb{R}$, démontrez en utilisant les propriétés des tribus que la mesure de la demi-droite est nulle.

---

## Démonstration et correction pas à pas
Analysons l'expression $\int_{\mathbb{R}} \sigma(wx + b) d\mu(x)$. Par définition de la fonction de Heaviside, $\sigma(wx+b)$ vaut $1$ si $wx+b > 0$ et $0$ sinon.\nAinsi, l'intégrale se réécrit comme la mesure de l'ensemble d'intégration :\n$$\int_{\mathbb{R}} \mathbf{1}_{\{wx + b > 0\}} d\mu(x) = \mu(\{x \in \mathbb{R} \mid wx + b > 0\})$$\n\nPrenons $w = 1$ et $b = -c$. L'ensemble devient $\{x \in \mathbb{R} \mid x - c > 0\} = (c, +\infty)$. \nPar hypothèse, l'intégrale est nulle. Donc $\mu((c, +\infty)) = 0$ pour tout $c \in \mathbb{R}$.\nDe la même manière, prenons $w = -1$ et $b = c$. L'ensemble devient $\{x \in \mathbb{R} \mid -x + c > 0\} = (-\infty, c)$.\nAinsi $\mu((-\infty, c)) = 0$ pour tout $c \in \mathbb{R}$.\n\nPuisque les intervalles de la forme $(a, b]$ peuvent s'écrire comme $(-\infty, b] \cap (a, +\infty)$, et que la tribu borélienne sur $\mathbb{R}$ est engendrée par les demi-droites, le fait que la mesure s'annule sur tous ces ensembles générateurs (stables par intersection finie, c'est-à-dire un $\pi$-système) implique que $\mu$ est la mesure identiquement nulle par le lemme d'unicité des mesures (Théorème de la classe monotone). Cela prouve que l'échelon de Heaviside est une fonction discriminatoire absolue.
