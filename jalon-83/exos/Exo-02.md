---
uuid: jalon-83-exo-02
title: "Exercice 02 - Dérivation des distributions"
---

# Exercice 02 $\bigstar\star\star\star\star$

**Énoncé :**
Soit la fonction "rampe" (ou ReLU en apprentissage profond) définie par $R(x) = \max(0, x)$.
1. Montrer que $R$ est une distribution régulière (localement intégrable).
2. En utilisant la formule des sauts, calculer la dérivée première $R'$ au sens des distributions. Reconnaissez-vous une fonction classique ?
3. Calculer la dérivée seconde $R''$ au sens des distributions.

**Correction pas à pas :**
1. La fonction $R(x)$ est continue sur $\mathbb{R}$ (elle vaut 0 pour $x \le 0$ et $x$ pour $x > 0$). Toute fonction continue sur $\mathbb{R}$ est localement intégrable (l'intégrale de sa valeur absolue sur tout segment fini est finie). Donc $R \in L^1_{loc}(\mathbb{R})$ et définit une distribution.

2. La fonction $R(x)$ est de classe $C^1$ sur $\mathbb{R} \setminus \{0\}$.
Sa dérivée usuelle, définie sur $\mathbb{R}^*$, vaut :
- $\{R'\}(x) = 0$ si $x < 0$.
- $\{R'\}(x) = 1$ si $x > 0$.
La fonction $R$ étant continue en 0 (car $R(0^-) = 0$ et $R(0^+) = 0$), le saut est nul ($\sigma = 0$).
D'après la formule des sauts, $R' = \{R'\} + 0 \delta_0$.
On reconnait la fonction échelon de Heaviside $H(x)$. Donc $R' = H$ au sens des distributions.

3. Calculons $R'' = H'$.
La fonction $H$ est de classe $C^1$ sur $\mathbb{R} \setminus \{0\}$, de dérivée usuelle nulle.
Elle présente un saut en $x = 0$ d'amplitude : $\sigma = H(0^+) - H(0^-) = 1 - 0 = 1$.
D'après la formule des sauts, $R'' = H' = \{H'\} + 1 \delta_0 = 0 + \delta_0 = \delta_0$.
La dérivée seconde de la fonction rampe est exactement la masse de Dirac à l'origine. $\blacksquare$
