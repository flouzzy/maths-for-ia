## Limite en norme $L^2$ : Prolongement par densité

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$


Considérons la fonction $f(x) = \frac{\sin(x)}{x}$. On sait que $f \in L^2(\mathbb{R})$ mais $f \notin L^1(\mathbb{R})$.
Soit la suite de fonctions tronquées $f_n(x) = f(x) \mathbb{1}_{[-n, n]}(x)$.
1. Montrer que $f_n \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ pour tout entier $n$.
2. Écrire l'expression de $\hat{f}_n(\xi)$. (On ne demande pas d'évaluer complètement l'intégrale, mais de justifier sa bonne définition).
3. En utilisant l'isométrie de Plancherel, expliquer pourquoi la suite $(\hat{f}_n)$ est une suite de Cauchy dans $L^2(\mathbb{R})$. Qu'en déduit-on pour la définition de $\hat{f}$ ?

### Correction :

1. La fonction $f_n$ est continue par morceaux et à support compact (incluse dans $[-n, n]$). Elle est donc bornée et son intégrale sur un domaine fini est finie.
$$ \int_{\mathbb{R}} |f_n(x)| dx = \int_{-n}^n \left|\frac{\sin(x)}{x}\right| dx \le \int_{-n}^n 1 dx = 2n < \infty $$
Ainsi $f_n \in L^1(\mathbb{R})$.
De même, $|f_n(x)|^2 \le 1$ sur $[-n, n]$, donc l'intégrale du carré est bornée par $2n$. Ainsi $f_n \in L^2(\mathbb{R})$.

2. Puisque $f_n \in L^1(\mathbb{R})$, sa transformée de Fourier classique est bien définie :
$$ \hat{f}_n(\xi) = \int_{-n}^n \frac{\sin(x)}{x} e^{-i\xi x} dx $$
Cette intégrale de Riemann propre est parfaitement définie pour tout $\xi \in \mathbb{R}$.

3. Soient $n > m$. La différence $f_n - f_m$ vaut :
$$ f_n(x) - f_m(x) = f(x) \mathbb{1}_{[-n, n] \setminus [-m, m]}(x) $$
Son énergie temporelle est :
$$ \|f_n - f_m\|_{L^2}^2 = \int_{m \le |x| \le n} \left| \frac{\sin(x)}{x} \right|^2 dx $$
Puisque $f \in L^2(\mathbb{R})$, l'intégrale impropre $\int_{\mathbb{R}} |f(x)|^2 dx$ converge (les "restes" tendent vers 0). Donc, pour tout $\epsilon > 0$, il existe $N$ tel que pour $n, m > N$, $\|f_n - f_m\|_{L^2}^2 < \epsilon$.
La suite $(f_n)$ est donc de Cauchy dans $L^2(\mathbb{R})$.
Par la linéarité et l'isométrie de la transformée de Fourier sur $L^1 \cap L^2$ (Plancherel), on a :
$$ \|\hat{f}_n - \hat{f}_m\|_{L^2} = \sqrt{2\pi} \|f_n - f_m\|_{L^2} $$
Ainsi, la suite $(\hat{f}_n)$ est également une suite de Cauchy dans l'espace $L^2(\mathbb{R})$.
Or, l'espace $L^2(\mathbb{R})$ est un espace de Hilbert, donc complet. Toute suite de Cauchy y converge.
On en déduit qu'il existe une limite unique dans $L^2(\mathbb{R})$ pour la suite $(\hat{f}_n)$. Cette limite est par définition la transformée de Fourier de $f$ dans $L^2$, bien que l'intégrale ne converge pas absolument au sens de Lebesgue.
