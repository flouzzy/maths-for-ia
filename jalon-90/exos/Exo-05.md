# Exercice 5 : Convergence en loi via la fonction de répartition

Niveau : $\bigstar\bigstar\bigstar\star\star$

Soit $X_n \sim \mathcal{U}([0, \frac{1}{n}])$.
1. Déterminer la fonction de répartition $F_{X_n}(x)$ de $X_n$.
2. En déduire la limite simple de $F_{X_n}(x)$.
3. Conclure sur la convergence en loi de la suite $(X_n)$.

## Correction

**1. Fonction de répartition :**
La densité de $X_n$ est $f_n(t) = n \mathbb{1}_{[0, \frac{1}{n}]}(t)$.
La fonction de répartition est $F_{X_n}(x) = \int_{-\infty}^x f_n(t) dt$.
- Si $x < 0$, $F_{X_n}(x) = 0$.
- Si $0 \le x \le \frac{1}{n}$, $F_{X_n}(x) = \int_0^x n dt = nx$.
- Si $x > \frac{1}{n}$, $F_{X_n}(x) = 1$.

**2. Limite simple de la fonction de répartition :**
Soit $x \in \mathbb{R}$.
- Si $x < 0$, pour tout $n$, $F_{X_n}(x) = 0 \xrightarrow{n \to +\infty} 0$.
- Si $x > 0$, il existe un rang $N$ tel que pour tout $n \ge N$, on a $\frac{1}{n} < x$.
Alors pour tout $n \ge N$, $F_{X_n}(x) = 1$. Donc $\lim_{n \to +\infty} F_{X_n}(x) = 1$.
- Si $x = 0$, $F_{X_n}(0) = 0 \xrightarrow{n \to +\infty} 0$.
Ainsi, la limite simple notée $F(x)$ est la fonction définie par $F(x) = 0$ si $x \le 0$, et $F(x) = 1$ si $x > 0$.

**3. Conclusion sur la convergence en loi :**
On observe que $F(x)$ correspond (presque) à la fonction de répartition d'une variable aléatoire constante égale à 0 (une masse de Dirac en 0), notons la $X = 0$.
La fonction de répartition de $X=0$ est $F_X(x) = 0$ si $x < 0$, et $F_X(x) = 1$ si $x \ge 0$.
Remarquons que $\lim F_{X_n}(0) = 0 \neq F_X(0) = 1$. La limite simple des fonctions de répartition diffère de $F_X$ au point $x=0$.
Cependant, le point $x=0$ est un point de discontinuité de la fonction de répartition limite $F_X$.
Le théorème de Portmanteau stipule que la convergence en loi $X_n \xrightarrow{\mathcal{L}} X$ équivaut à la convergence $\lim_{n \to \infty} F_{X_n}(x) = F_X(x)$ pour tout point $x$ **où $F_X$ est continue**.
Ici, $F_X$ est continue sur $\mathbb{R} \setminus \{0\}$.
Or, on a bien montré que pour $x < 0$, $F_{X_n}(x) \to 0 = F_X(x)$ et pour $x > 0$, $F_{X_n}(x) \to 1 = F_X(x)$.
L'égalité est donc vérifiée en tout point de continuité de $F_X$.
On conclut que $X_n \xrightarrow{\mathcal{L}} 0$.
