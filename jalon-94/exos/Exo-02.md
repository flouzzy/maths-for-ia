# Exercice 2 : Application directe : Approximation d'une loi de Poisson \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes suivant toutes la loi de Poisson de paramètre $\lambda = 2$.
On pose $S_n = \sum_{i=1}^n X_i$.
1. Quelle est l'espérance et la variance de $S_n$ ?
2. À l'aide du Théorème Central Limite, trouver la limite quand $n \to \infty$ de $\mathbb{P}(S_n \le 2n + \sqrt{2n})$.
3. Expliquer le lien géométrique avec la forme de la cloche.

**Correction :**

1. Les variables $X_i$ sont I.I.D. et suivent une loi de Poisson de paramètre $\lambda = 2$.
L'espérance est $\mathbb{E}[X_1] = \lambda = 2$.
La variance est $\text{Var}(X_1) = \lambda = 2$.
La variable $S_n$ est la somme de $n$ telles variables. Par linéarité de l'espérance et additivité de la variance (indépendance), on a :
$\mathbb{E}[S_n] = 2n$ et $\text{Var}(S_n) = 2n$.
Remarque : On sait que la somme de variables de Poisson indépendantes est une loi de Poisson de paramètre la somme des paramètres. Donc $S_n$ suit exactement une loi $\mathcal{P}(2n)$.

2. Le Théorème Central Limite stipule que la variable centrée et réduite :
$$Z_n = \frac{S_n - \mathbb{E}[S_n]}{\sqrt{\text{Var}(S_n)}} = \frac{S_n - 2n}{\sqrt{2n}}$$
converge en loi vers $\mathcal{N}(0, 1)$.
On cherche $\lim_{n \to \infty} \mathbb{P}(S_n \le 2n + \sqrt{2n})$.
Cela se réécrit :
$$\mathbb{P}\left( S_n - 2n \le \sqrt{2n} \right) = \mathbb{P}\left( \frac{S_n - 2n}{\sqrt{2n}} \le 1 \right) = \mathbb{P}(Z_n \le 1)$$
Par convergence en loi vers $Z \sim \mathcal{N}(0, 1)$, on a :
$$\lim_{n \to \infty} \mathbb{P}(Z_n \le 1) = \Phi(1) \approx 0.8413$$

3. La loi de Poisson $\mathcal{P}(\lambda)$ est asymétrique pour de petits paramètres (biaisée vers $0$). Lorsque le paramètre $\lambda = 2n$ devient grand, le profil de probabilité de cette loi discrète épouse très précisément le profil symétrique de la densité de la loi normale (cloche). Le TCL démontre que l'asymétrie initiale des $(X_i)$ s'estompe avec l'accumulation additive.
