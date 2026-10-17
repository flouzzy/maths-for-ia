# Exercice 08

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit à calculer $I = \int_{0}^{+\infty} g(x) e^{-x} dx$ avec $g$ telle que $\int_0^{+\infty} |g(x)| e^{-x} dx < \infty$.
Proposer un estimateur $\hat{I}_n$ construit à partir d'une suite de variables I.I.D. judicieusement choisie et démontrer qu'il converge presque sûrement vers $I$.

**Correction :**
1. L'intégrale à estimer a la forme d'une espérance :
$I = \int_{0}^{+\infty} g(x) e^{-x} dx$.
Remarquons que $f(x) = e^{-x} \mathbf{1}_{[0,+\infty[}(x)$ est la densité de probabilité d'une loi exponentielle de paramètre $\lambda = 1$.
2. Par conséquent, si on prend $X$ une variable aléatoire suivant la loi $\mathcal{E}(1)$, on a par le théorème de transfert :
$\mathbb{E}[g(X)] = \int_{-\infty}^{+\infty} g(x) f(x) dx = \int_{0}^{+\infty} g(x) e^{-x} dx = I$.
3. La condition $\int_0^{+\infty} |g(x)| e^{-x} dx < \infty$ s'écrit $\mathbb{E}[|g(X)|] < +\infty$.
4. On définit l'estimateur empirique suivant : on tire une suite $(X_1, ..., X_n)$ I.I.D. de loi $\mathcal{E}(1)$ et on pose $\hat{I}_n = \frac{1}{n} \sum_{i=1}^n g(X_i)$.
5. Les variables $Y_i = g(X_i)$ sont I.I.D. car composées mesurables de variables I.I.D.
Elles vérifient la condition d'intégrabilité $\mathbb{E}[|Y_1|] < +\infty$.
Par la Loi Forte des Grands Nombres de Kolmogorov, on conclut que :
$\hat{I}_n = \frac{1}{n} \sum_{i=1}^n g(X_i) \xrightarrow{p.s.} \mathbb{E}[g(X_1)] = I$.
