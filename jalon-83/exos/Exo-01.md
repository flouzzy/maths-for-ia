---
uuid: jalon-83-exo-01
title: "Exercice 01 - Dérivation des distributions"
---

# Exercice 01 $\bigstar\star\star\star\star$

**Énoncé :**
Soit la fonction $f(x) = |x|$ définie sur $\mathbb{R}$.
1. Tracer mentalement ou sur papier le graphe de $f$. La fonction est-elle dérivable en 0 au sens classique ?
2. Calculer la dérivée première $f'$ au sens des distributions et l'exprimer à l'aide de la fonction signe, notée $\text{sgn}(x)$ (qui vaut 1 si $x > 0$, -1 si $x < 0$, et 0 si $x = 0$).
3. Calculer la dérivée seconde $f''$ au sens des distributions. Exprimer le résultat en fonction de la distribution de Dirac $\delta_0$.

**Correction pas à pas :**
1. Le graphe de $f(x) = |x|$ est en forme de "V". La pente est de -1 pour $x < 0$ et de +1 pour $x > 0$. Au point $x = 0$, la courbe présente un point anguleux. La limite du taux d'accroissement à gauche vaut -1, et à droite vaut +1. Puisqu'elles sont différentes, la fonction $f$ n'est pas dérivable en 0 au sens usuel.

2. En revanche, $f$ est une fonction localement intégrable, elle définit donc une distribution $T_f$.
La fonction $f$ est de classe $C^1$ par morceaux et continue partout. Elle ne présente aucun saut.
On peut appliquer la formule des sauts : la dérivée au sens des distributions coïncide avec la dérivée usuelle là où elle est définie, plus la somme des sauts pondérés par des Diracs.
Ici, comme la fonction est continue, le saut en 0 est nul ($\sigma = 0$).
Donc $f' = \{f'\}$, la dérivée usuelle définie presque partout.
On a bien $f'(x) = 1$ si $x > 0$ et $f'(x) = -1$ si $x < 0$.
Ainsi, $f' = \text{sgn}$ au sens des distributions.

3. Calculons maintenant la dérivée seconde, c'est-à-dire la dérivée de la distribution $T_{\text{sgn}}$.
La fonction $\text{sgn}(x)$ est de classe $C^1$ sur $\mathbb{R} \setminus \{0\}$. Sa dérivée usuelle $\{\text{sgn}'\}$ est nulle partout où elle est définie (car la fonction est constante sur $]-\infty, 0[$ et sur $]0, +\infty[$).
Cependant, la fonction $\text{sgn}$ présente un saut de discontinuité en $x = 0$.
Calculons l'amplitude du saut $\sigma$ :
$$ \sigma = \text{sgn}(0^+) - \text{sgn}(0^-) = 1 - (-1) = 2 $$
En appliquant la formule des sauts pour la dérivée des distributions d'une fonction $C^1$ par morceaux présentant des sauts, on a :
$$ f'' = (\text{sgn})' = \{\text{sgn}'\} + \sigma \delta_0 $$
$$ f'' = 0 + 2 \delta_0 $$
Donc, la dérivée seconde de la valeur absolue au sens des distributions est le double de la masse de Dirac en zéro :
$$ f'' = 2 \delta_0 \quad \blacksquare $$
