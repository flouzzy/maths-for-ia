---
title: "Exercice 5 : Inégalité de Hölder généralisée"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 5 : Inégalité de Hölder généralisée

## Énoncé
Soient $p_1, \dots, p_k \in [1, \infty]$ tels que $\sum_{i=1}^k \frac{1}{p_i} = 1$.
Si $f_i \in L^{p_i}(X)$ pour tout $i=1,\dots,k$, montrer que le produit $\prod_{i=1}^k f_i \in L^1(X)$ et que :
$$ \int_X |f_1 \dots f_k| d\mu \le \|f_1\|_{p_1} \dots \|f_k\|_{p_k} $$

## Corrigé
On raisonne par récurrence sur $k$.
Le cas $k=2$ est l'inégalité de Hölder standard.
Supposons le résultat vrai pour $k-1$.
Considérons $f_1, \dots, f_k$. Soit $q$ tel que $\frac{1}{q} = \sum_{i=1}^{k-1} \frac{1}{p_i}$. Alors $\frac{1}{q} + \frac{1}{p_k} = 1$.
Appliquons l'inégalité de Hölder à 2 fonctions : $F = f_1 \dots f_{k-1}$ et $G = f_k$.
$F \in L^q$ et $G \in L^{p_k}$.
$\int |F G| d\mu \le \|F\|_q \|G\|_{p_k}$.
Mais par définition de $q$ et l'hypothèse de récurrence (appliquée aux $k-1$ fonctions avec exposants $p_i/q$ dont la somme des inverses est 1), on a :
$$ \|F\|_q = \left( \int |f_1 \dots f_{k-1}|^q d\mu \right)^{1/q} = \| |f_1|^q \dots |f_{k-1}|^q \|_1^{1/q} $$
En appliquant l'hypothèse de récurrence aux fonctions $|f_i|^q \in L^{p_i/q}$ :
$$ \|F\|_q^q \le \prod_{i=1}^{k-1} \| |f_i|^q \|_{p_i/q} = \prod_{i=1}^{k-1} \left( \int |f_i|^{q \times p_i/q} d\mu \right)^{\frac{q}{p_i}} = \prod_{i=1}^{k-1} \|f_i\|_{p_i}^q $$
En prenant la puissance $1/q$, on trouve $\|F\|_q \le \prod_{i=1}^{k-1} \|f_i\|_{p_i}$.
On remplace dans la première inégalité :
$$ \int |f_1 \dots f_k| d\mu \le \left( \prod_{i=1}^{k-1} \|f_i\|_{p_i} \right) \|f_k\|_{p_k} = \prod_{i=1}^k \|f_i\|_{p_i} $$
Le résultat est démontré.
