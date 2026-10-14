\subsection*{Exercice 7 : Convergence du produit par Slutsky \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Soit $X_n$ une suite convergeant en loi vers $X$, et $Y_n$ une suite convergeant en probabilité vers une constante $c$.
Montrer rigoureusement le théorème de Slutsky pour le produit : $X_n Y_n \xrightarrow{\mathcal{L}} cX$.

**Correction :**
La preuve générale est technique. Il est possible de l'établir à l'aide des fonctions caractéristiques, mais nous procéderons par une méthode directe avec les fonctions bornées continues uniformément.
Soit $f : \mathbb{R} \to \mathbb{R}$ bornée par $M$ et Lipschitzienne de constante $K$ (la convergence sur ces fonctions suffit pour la convergence en loi, lemme de Portmanteau).
$\mathbb{E}[f(X_n Y_n)] - \mathbb{E}[f(cX)] = (\mathbb{E}[f(X_n Y_n)] - \mathbb{E}[f(c X_n)]) + (\mathbb{E}[f(c X_n)] - \mathbb{E}[f(cX)])$.
Le second terme tend vers 0. En effet, $X_n \xrightarrow{\mathcal{L}} X \implies cX_n \xrightarrow{\mathcal{L}} cX$. Soit $h(x) = f(cx)$, $h$ est continue bornée, donc $\mathbb{E}[h(X_n)] \to \mathbb{E}[h(X)]$.
Il reste le premier terme, noté $E_n$. Soit $\varepsilon > 0$.
$|f(X_n Y_n) - f(c X_n)| \le \min(2M, K |X_n| |Y_n - c|)$.
Fixons un compact $A = [-R, R]$ tel que $\mathbb{P}(|X| > R) < \varepsilon / (8M)$. Par la convergence en loi (Portmanteau sur les ouverts), pour $n$ grand, $\mathbb{P}(|X_n| > R) < \varepsilon / (4M)$.
Découpons l'espace $\Omega$ :
- Sur $\{|X_n| \le R\} \cap \{|Y_n - c| \le \delta\}$, l'écart est $\le K \cdot R \cdot \delta$. En choisissant $\delta = \frac{\varepsilon}{2 K R}$, l'écart est $\le \varepsilon / 2$.
- Sur l'événement contraire, on le majore brutalement par $2M$.
L'espérance du premier terme se majore par :
$\varepsilon/2 + 2M \cdot \left[ \mathbb{P}(|X_n| > R) + \mathbb{P}(|Y_n - c| > \delta) \right]$.
Par hypothèse $Y_n \xrightarrow{\mathbb{P}} c$, donc $\mathbb{P}(|Y_n - c| > \delta) \to 0$.
Pour $n$ grand, cette somme est $\le \varepsilon/2 + 2M (\varepsilon/(4M) + \varepsilon/(4M)) = \varepsilon/2 + \varepsilon = \frac{3\varepsilon}{2}$.
Ainsi, $\lim_{n \to \infty} |\mathbb{E}[f(X_n Y_n)] - \mathbb{E}[f(c X_n)]| = 0$.
D'où $X_n Y_n \xrightarrow{\mathcal{L}} cX$.
