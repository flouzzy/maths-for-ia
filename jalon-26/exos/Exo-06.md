---
uuid: "jalon-26-exo-06"
title: "Espace $l^2$ des suites de carré sommable"
difficulty: 4
---

# Exercice 6 : Espace $l^2$ des suites de carré sommable (Difficulté ★★★★☆)

Soit $l^2$ l'ensemble des suites réelles $(u_n)_{n \in \mathbb{N}}$ telles que la série $\sum u_n^2$ converge.
1. Montrer que si $(u_n), (v_n) \in l^2$, alors la série $\sum u_n v_n$ est absolument convergente (utiliser Cauchy-Schwarz sur les sommes partielles).
2. En déduire que $l^2$ est un sous-espace vectoriel de l'espace des suites réelles.
3. Montrer que $\langle u, v \rangle = \sum_{n=0}^\infty u_n v_n$ définit un produit scalaire sur $l^2$.

## Démonstration Rigoureuse à Blanc

1. Soit $(u_n), (v_n) \in l^2$. Considérons la somme partielle $S_N = \sum_{n=0}^N |u_n v_n|$.
   - Les vecteurs $(|u_0|, \ldots, |u_N|)$ et $(|v_0|, \ldots, |v_N|)$ appartiennent à l'espace euclidien $\mathbb{R}^{N+1}$.
   - Appliquons l'inégalité de Cauchy-Schwarz canonique sur ces vecteurs :
     $$ \sum_{n=0}^N |u_n v_n| \le \sqrt{\sum_{n=0}^N u_n^2} \sqrt{\sum_{n=0}^N v_n^2} $$
   - Puisque les séries $\sum u_n^2$ et $\sum v_n^2$ convergent (hypothèse $(u_n), (v_n) \in l^2$), leurs sommes partielles sont majorées par leurs restes infinis :
     $$ \sqrt{\sum_{n=0}^N u_n^2} \le \sqrt{\sum_{n=0}^\infty u_n^2} \quad \text{et} \quad \sqrt{\sum_{n=0}^N v_n^2} \le \sqrt{\sum_{n=0}^\infty v_n^2} $$
   - Ainsi, pour tout $N$, la somme partielle des valeurs absolues est majorée par une constante indépendante de $N$ :
     $$ S_N \le \sqrt{\sum_{n=0}^\infty u_n^2} \sqrt{\sum_{n=0}^\infty v_n^2} = M $$
   - Une série à termes positifs dont les sommes partielles sont majorées est convergente. Donc la série $\sum |u_n v_n|$ converge. La série $\sum u_n v_n$ est donc absolument convergente.

2. Pour montrer que $l^2$ est un sous-espace vectoriel :
   - La suite nulle appartient évidemment à $l^2$ car $\sum 0^2 = 0$.
   - Soit $\lambda \in \mathbb{R}$ et $u, v \in l^2$. Considérons la série $\sum (u_n + \lambda v_n)^2$.
     $$ (u_n + \lambda v_n)^2 = u_n^2 + 2\lambda u_n v_n + \lambda^2 v_n^2 $$
   - Or, la série $\sum u_n^2$ converge (car $u \in l^2$), la série $\sum v_n^2$ converge (car $v \in l^2$), et d'après la question 1, la série $\sum u_n v_n$ converge absolument (donc converge).
   - Par linéarité, la série somme converge : $\sum (u_n + \lambda v_n)^2 < \infty$.
   - Donc $u + \lambda v \in l^2$. $l^2$ est bien un sous-espace vectoriel.

3. Vérifions les axiomes du produit scalaire pour $\langle u, v \rangle = \sum_{n=0}^\infty u_n v_n$.
   - La forme est bien définie car la série converge absolument.
   - **Bilinéarité** : Par linéarité de la somme de séries convergentes, $\sum (\lambda u_n + w_n)v_n = \lambda \sum u_n v_n + \sum w_n v_n$.
   - **Symétrie** : Évidente, car $u_n v_n = v_n u_n$.
   - **Définie positive** : $\langle u, u \rangle = \sum u_n^2 \ge 0$.
   - Si $\sum u_n^2 = 0$, comme c'est une série de termes positifs ou nuls, chaque terme doit être nul. Donc pour tout $n$, $u_n^2 = 0$, soit $u_n = 0$. Donc $u = 0_{l^2}$.
   $\blacksquare$
