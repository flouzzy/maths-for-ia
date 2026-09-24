# Exercice 6 : Non-densité dans $L^\infty$ $\star\star\star\star\mathstrut$

**Énoncé :**
Montrer que $C_c(\mathbb{R})$ n'est pas dense dans $L^\infty(\mathbb{R})$. Quelle est la clôture (adhérence) de $C_c(\mathbb{R})$ dans l'espace $L^\infty(\mathbb{R})$ muni de la norme $\| \cdot \|_\infty$ ?

**Correction détaillée :**
1. **Contre-exemple pour la densité :** Soit la fonction constante $f(x) = 1$ pour tout $x \in \mathbb{R}$. Il est clair que $f \in L^\infty(\mathbb{R})$ et $\|f\|_\infty = 1$.
Soit $\varphi \in C_c(\mathbb{R})$. Par définition, $\varphi$ a un support compact $K \subset [-R, R]$. Donc pour $|x| > R$, $\varphi(x) = 0$.
Évaluons la distance en norme $L^\infty$ entre $f$ et $\varphi$ :
$$ \|f - \varphi\|_\infty = \text{ess sup}_{x \in \mathbb{R}} |1 - \varphi(x)| $$
Pour tout $x > R$, $|1 - \varphi(x)| = |1 - 0| = 1$.
Donc le supremum essentiel est nécessairement au moins $1$, ce qui implique $\|f - \varphi\|_\infty \ge 1$.
Il est impossible de trouver une suite de $C_c(\mathbb{R})$ convergeant vers $f$ avec la norme uniforme : $C_c(\mathbb{R})$ n'est pas dense dans $L^\infty(\mathbb{R})$.
2. **Identification de la clôture :** Soit $\overline{C_c(\mathbb{R})}$ la clôture pour la norme $\|\cdot\|_\infty$. La convergence au sens de $L^\infty$ implique la convergence uniforme.
Une limite uniforme de fonctions continues est continue.
De plus, soit $g$ dans la clôture. Il existe $\varphi_n \in C_c(\mathbb{R})$ telle que $\|g - \varphi_n\|_\infty \to 0$.
Pour $\varepsilon > 0$, soit $N$ tel que $\|g - \varphi_N\|_\infty \le \varepsilon$.
Comme $\varphi_N$ est à support compact, il existe un rayon $R$ tel que $\varphi_N(x) = 0$ pour $|x| > R$.
Ainsi, pour tout $|x| > R$, on a $|g(x)| = |g(x) - \varphi_N(x)| \le \varepsilon$.
Ceci prouve que $\lim_{|x| \to \infty} g(x) = 0$.
L'adhérence est l'espace $C_0(\mathbb{R})$, l'espace des fonctions continues s'annulant à l'infini. $\blacksquare$
