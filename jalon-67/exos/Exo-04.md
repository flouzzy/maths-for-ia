# Exercice 4 : Fonction Gamma

**Difficulté :** $\bigstar\bigstar\star$

**Énoncé :**
Soit $\Gamma(s) = \int_0^\infty t^{s-1} e^{-t} dt$. En utilisant une suite croissante, montrer que $\Gamma(s)$ est bien définie pour $s>0$.

**Correction :**
Posons $f_n(t) = t^{s-1} e^{-t} \mathbb{I}_{[\frac{1}{n}, n]}(t)$. La suite $f_n$ est croissante pour tout $t>0$ et converge vers $f(t) = t^{s-1} e^{-t}$. Le TCM s'applique : $\int_0^\infty f(t) dt = \lim \int_{1/n}^n t^{s-1} e^{-t} dt$. L'intégrale sur $[\frac{1}{n}, 1]$ est dominée par $t^{s-1}$ dont l'intégrale converge si $s>0$, et sur $[1, n]$ elle est dominée par $e^{-t/2}$, qui converge. $\blacksquare$
