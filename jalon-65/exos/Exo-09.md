---
uuid: "jalon-65-exo-09"
title: "Exercice 9 : Approximation étagée - Cas concret"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Approximation étagée - Cas concret

## Énoncé

Considérons $f(x) = x^2$ définie sur $E = [0, 2]$. Construire explicitement la suite de fonctions étagées $(s_n)_{n \in \mathbb{N}}$ de la preuve du Théorème d'approximation et expliciter $s_1$.

## Solution Détaillée

La formule est $s_n(x) = \sum_{k=0}^{n2^n-1} \frac{k}{2^n} \mathbb{1}_{A_{n,k}}(x)$ avec $A_{n,k} = f^{-1}([\frac{k}{2^n}, \frac{k+1}{2^n}[)$.
Pour $n=1$, $n2^n - 1 = 1 \times 2^1 - 1 = 1$. La somme va de $k=0$ à $k=1$. Et on ajoute le terme pour $f(x) \ge 1$.
$k=0 : A_{1,0} = f^{-1}([0, \frac{1}{2}[) = [0, \frac{1}{\sqrt{2}}[$.
$k=1 : A_{1,1} = f^{-1}([\frac{1}{2}, 1[) = [\frac{1}{\sqrt{2}}, 1[$.
Pour la partie 'reste' : $B_1 = f^{-1}([1, +\infty]) = [1, 2]$.
Ainsi, $s_1(x) = 0 \cdot \mathbb{1}_{[0, 1/\sqrt{2}[}(x) + \frac{1}{2} \cdot \mathbb{1}_{[1/\sqrt{2}, 1[}(x) + 1 \cdot \mathbb{1}_{[1, 2]}(x)$. $\blacksquare$
