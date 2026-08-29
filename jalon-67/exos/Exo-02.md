---
title: "Exercice 2 : Intégration terme à terme"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 2 : Intégration terme à terme

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Problème

Calculer l'intégrale de Lebesgue $\int_0^1 \sum_{n=1}^\infty x^n dx$ en justifiant chaque étape.

## Démonstration et Résolution

### Étape 1 : Poser le cadre
Soit l'espace mesuré $([0,1], \mathcal{B}([0,1]), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Considérons la suite de fonctions $u_n : [0,1] \to \mathbb{R}$ définie par $u_n(x) = x^n$ pour tout $n \ge 1$.
Chaque $u_n$ est continue, donc borélienne et par conséquent mesurable. De plus, sur $[0,1]$, on a clairement $u_n(x) \ge 0$.

### Étape 2 : Invoquer le Corollaire du Théorème de Convergence Monotone
Le corollaire du Théorème de Beppo Levi stipule que pour toute suite de fonctions mesurables positives $(u_n)$, l'intégrale de la somme infinie est égale à la somme infinie des intégrales :
$$ \int_{[0,1]} \left( \sum_{n=1}^\infty u_n(x) \right) d\lambda(x) = \sum_{n=1}^\infty \int_{[0,1]} u_n(x) d\lambda(x) $$
Cette interversion est justifiée sans aucune condition de convergence uniforme, grâce à la stricte positivité des termes.

### Étape 3 : Calcul des intégrales individuelles
Pour un entier $n \ge 1$ fixé, l'intégrale de $u_n$ sur le segment $[0,1]$ se calcule par les primitives élémentaires :
$$ \int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1^{n+1}}{n+1} - \frac{0^{n+1}}{n+1} = \frac{1}{n+1} $$

### Étape 4 : Sommation infinie
Il nous reste à évaluer la somme de la série :
$$ \sum_{n=1}^\infty \frac{1}{n+1} $$
En effectuant le changement d'indice $k = n + 1$, la somme devient :
$$ \sum_{k=2}^\infty \frac{1}{k} $$
Il s'agit de la série harmonique amputée de son premier terme ($k=1$). On sait par comparaison série-intégrale que la série harmonique $\sum \frac{1}{k}$ diverge vers $+\infty$.
Par conséquent, la somme est infinie.
Conclusion :
$$ \int_0^1 \left( \sum_{n=1}^\infty x^n \right) dx = +\infty $$
