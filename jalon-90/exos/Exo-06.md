# Exercice 06

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Convergence d'une variable exponentielle rescalée

Soit $(X_n)$ une suite de variables aléatoires indépendantes suivant la loi exponentielle de paramètre $\lambda = n$.
Étudiez les modes de convergence (presque sûre, probabilité, loi) de la suite $(X_n)$.

**Correction exhaustive :**
Déterminons d'abord la fonction de répartition de $X_n$.
Pour tout $t > 0$, $F_n(t) = \mathbb{P}(X_n \le t) = 1 - e^{-nt}$.
Pour $t \le 0$, $F_n(t) = 0$.
Fixons $t > 0$. Lorsque $n \to \infty$, $e^{-nt} \to 0$, donc $F_n(t) \to 1$.
Pour $t < 0$, $F_n(t) = 0 \to 0$.
La limite simple des fonctions de répartition est la fonction $\mathbf{1}_{[0, +\infty[}(t)$, qui correspond à la fonction de répartition de la variable certaine $X = 0$.
Puisque la convergence a lieu en tout point de continuité de la fonction de répartition de la variable constante $0$ (seul le point $t=0$ pose question, mais on ne regarde que les points de continuité), on déduit que :
$$ X_n \xrightarrow{\mathcal{L}} 0 $$
Puisque la limite est une variable certaine (constante), le théorème de convergence affirme que la convergence en loi vers une constante est équivalente à la convergence en probabilité.
Vérifions-le analytiquement : pour tout $\epsilon > 0$,
$$ \mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(X_n > \epsilon) = 1 - F_n(\epsilon) = e^{-n\epsilon} $$
Puisque $\epsilon > 0$, $\lim_{n \to \infty} e^{-n\epsilon} = 0$. Ainsi, $X_n \xrightarrow{\mathbb{P}} 0$.
Étudions la convergence presque sûre via Borel-Cantelli.
Fixons $\epsilon > 0$. Formons la somme des probabilités :
$$ \sum_{n=1}^\infty \mathbb{P}(|X_n| > \epsilon) = \sum_{n=1}^\infty e^{-n\epsilon} $$
Il s'agit d'une série géométrique de raison $q = e^{-\epsilon} \in ]0, 1[$, qui est convergente.
Par le premier lemme de Borel-Cantelli, l'événement $\{|X_n| > \epsilon\}$ ne se réalise qu'un nombre fini de fois avec probabilité 1.
Puisque cela est vrai pour une suite de $\epsilon$ tendant vers $0$, on en déduit que :
$$ X_n \xrightarrow{p.s.} 0 $$
La suite converge donc selon les trois modes principaux vers la variable $0$.
