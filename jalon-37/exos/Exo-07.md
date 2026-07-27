---
uuid: "jalon-37-exo-7"
title: "Exercice 7 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 7

**Difficulté :** ★★★★☆

**Énoncé :**
Soit $f : [0, 1] \to \mathbb{R}$ la fonction de Thomae, définie par :
$f(x) = \frac{1}{q}$ si $x = \frac{p}{q}$ fraction irréductible avec $q > 0$, et $f(x) = 0$ si $x$ est irrationnel ou nul.
Montrer que $f$ est Riemann-intégrable sur $[0, 1]$ et que son intégrale vaut $0$.

**Correction détaillée :**
1. Soit $\epsilon > 0$. Nous cherchons une subdivision $\sigma$ de $[0, 1]$ telle que $S_+(\sigma, f) < \epsilon$ (car $S_-(\sigma, f)$ est toujours nulle vu que chaque sous-intervalle contient un irrationnel, où $f=0$).
2. Il n'y a qu'un nombre fini de points $x \in [0, 1]$ pour lesquels $f(x) \ge \frac{\epsilon}{2}$. En effet, $f(x) \ge \frac{\epsilon}{2}$ signifie $q \le \frac{2}{\epsilon}$. Comme $0 \le p \le q$, le nombre de couples $(p,q)$ satisfaisant cette condition est fini.
3. Soit $N$ ce nombre fini de points, notons-les $x_1, \dots, x_N$.
4. Construisons une subdivision en isolant ces "grands" points dans de très petits intervalles. Entourons chaque point $x_k$ d'un intervalle $J_k$ de longueur $\frac{\epsilon}{4N}$.
5. La somme des longueurs de ces intervalles $J_k$ est au plus $N \cdot \frac{\epsilon}{4N} = \frac{\epsilon}{4}$.
6. Considérons les sous-intervalles de notre subdivision qui ne contiennent aucun des points $x_k$. Sur ces intervalles, pour tout $x$, on a $f(x) < \frac{\epsilon}{2}$. La contribution à la somme de Darboux supérieure de ces intervalles est donc majorée par $\frac{\epsilon}{2} \times (\text{longueur totale}) \le \frac{\epsilon}{2} \times 1 = \frac{\epsilon}{2}$.
7. La contribution des intervalles $J_k$ (où $f(x) \le 1$) à la somme de Darboux supérieure est majorée par $1 \times (\text{somme des longueurs des } J_k) = 1 \times \frac{\epsilon}{4} = \frac{\epsilon}{4}$.
8. Ainsi, il existe une subdivision $\sigma$ (construite en ajoutant les bornes des $J_k$) pour laquelle $S_+(\sigma, f) \le \frac{\epsilon}{2} + \frac{\epsilon}{4} < \epsilon$.
9. Comme $\epsilon$ est arbitraire, $\inf_{\sigma} S_+(\sigma, f) = 0$.
10. Or $\sup_{\sigma} S_-(\sigma, f) = 0$ (car $f(x)=0$ sur les irrationnels denses).
11. Donc $f$ est Riemann-intégrable et $\int_0^1 f(x) \, dx = 0$. $\blacksquare$
