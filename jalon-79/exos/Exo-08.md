# Exercice 8 : Équation différentielle et Parseval $\bigstar\bigstar\bigstar\bigstar\star$
**Énoncé :** Soit $y \in \mathcal{C}^2([0, 2\pi])$ une solution $2\pi$-périodique de l'équation différentielle :
$$y''(t) + k^2 y(t) = f(t)$$
où $k$ est un entier non nul, et $f \in L^2([0, 2\pi])$ est $2\pi$-périodique avec $c_k(f) = c_{-k}(f) = 0$.
Exprimer l'énergie $L^2$ de la solution $y$ en fonction des coefficients de Fourier de $f$.

**Correction Détaillée :**
*Étape 1 : Passage dans le domaine de Fourier.*
On décompose $y$ et $f$ en séries de Fourier exponentielles.
$y(t) = \sum c_n(y) e^{int}$, $y''(t) = \sum (-n^2) c_n(y) e^{int}$.
L'équation devient :
$$\sum_{n} (-n^2 c_n(y) + k^2 c_n(y)) e^{int} = \sum_{n} c_n(f) e^{int}$$
Par unicité des coefficients de Fourier, on a pour tout $n \in \mathbb{Z}$ :
$$(k^2 - n^2) c_n(y) = c_n(f)$$

*Étape 2 : Résolution pour $c_n(y)$.*
- Si $n = k$ ou $n = -k$, l'équation donne $0 = c_{\pm k}(f)$. Ceci est cohérent avec l'hypothèse. Les coefficients $c_k(y)$ et $c_{-k}(y)$ sont libres (correspondant à la solution homogène $A \cos(kt) + B \sin(kt)$). Pour trouver l'énergie minimale ou spécifique, supposons que l'on prenne la solution d'énergie minimale (donc $c_k(y) = c_{-k}(y) = 0$).
- Pour $n \neq \pm k$, on a $c_n(y) = \frac{c_n(f)}{k^2 - n^2}$.

*Étape 3 : Énergie par Parseval.*
L'énergie de $y$ (en supposant la solution de norme minimale) est :
$$\|y\|_2^2 = \sum_{n \neq \pm k} |c_n(y)|^2 = \sum_{n \neq \pm k} \frac{|c_n(f)|^2}{(k^2 - n^2)^2}$$
On voit que l'équation différentielle agit comme un filtre qui atténue fortement les hautes fréquences ($n \to \infty$, l'atténuation est en $1/n^4$).
