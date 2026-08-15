---
title: "Exo 08 : Complexité paramétrique de l'approximation"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exo 08 : Complexité paramétrique de l'approximation

## Énoncé formel
Soit $f(x) = x^2$ sur $[0, 1]$. Si on approche $f$ par une combinaison linéaire de $N$ ReLU avec des points de cassure uniformément répartis aux abscisses $x_i = i/N$, quelle est l'erreur maximale d'approximation $\|f - G\|_\infty$ en fonction de $N$ ? Cela quantifie la vitesse de convergence de l'approximation universelle.

---

## Démonstration et correction pas à pas
On cherche à approximer la parabole $x^2$ par une ligne polygonale avec des sommets aux abscisses $x_i = i/N$. Entre deux points de cassure, disons sur le segment $[x_i, x_{i+1}]$, le réseau forme le segment affine sécant connectant les points $(x_i, x_i^2)$ et $(x_{i+1}, x_{i+1}^2)$.\nL'erreur de l'interpolation affine d'une fonction $f$ sur un segment $[a, b]$ atteint son maximum lorsque la dérivée de l'interpolant correspond à la dérivée de $f$, c'est-à-dire au centre de l'intervalle si $f$ est une parabole.\nSur $[x_i, x_{i+1}]$, la longueur de l'intervalle est $\Delta x = 1/N$. \nLa théorie classique de l'interpolation numérique garantit que l'erreur d'interpolation linéaire est majorée par :\n$$ \max_{x \in [a,b]} |f(x) - P_1(x)| \le \frac{1}{8} (b - a)^2 \max_{x \in [a,b]} |f''(x)| $$\nIci, $f(x) = x^2$, donc $f''(x) = 2$ sur tout le domaine.\nEn substituant $b - a = 1/N$, on obtient :\n$$ \|f - G\|_\infty \le \frac{1}{8} \left(\frac{1}{N}\right)^2 \times 2 = \frac{1}{4N^2} $$\nLe maximum exact est même pris au milieu du sous-intervalle $x_m = x_i + \frac{1}{2N}$. On vérifie que la flèche entre la parabole et sa sécante vaut exactement $1 / (4N^2)$. Ainsi, l'erreur chute en $\mathcal{O}(1/N^2)$ pour la classe des fonctions $C^2$ approchées par des réseaux ReLU superficiels.
