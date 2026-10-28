$\bigstar\bigstar\bigstar\star\star$
**Énoncé :** Exemple de convergence faible non forte dans $\ell^2$.
Soit $\ell^2$ l'espace des suites de carré sommable. On note $(e_n)$ la base hilbertienne canonique.
Montrer que $e_n \rightharpoonup 0$ faiblement, mais que $(e_n)$ ne converge pas fortement.

**Correction Détaillée :**
Considérons l'espace de Hilbert $H = \ell^2$. Le théorème de représentation de Riesz assure que toute forme linéaire continue $L \in H^*$ s'écrit $L(x) = \langle x, y \rangle$ pour un unique $y \in H$.
Soit $y = (y_k) \in \ell^2$. Évaluons la forme linéaire sur la suite $e_n$ :
$L(e_n) = \langle e_n, y \rangle = y_n$.
Comme $y \in \ell^2$, la série $\sum y_k^2$ est convergente. La condition nécessaire de convergence d'une série impose que son terme général tende vers $0$.
Ainsi, $\lim_{n \to \infty} y_n = 0$.
On a donc pour toute $L \in H^*$, $\lim_{n \to \infty} L(e_n) = 0 = L(0)$. La suite $(e_n)$ converge donc faiblement vers $0$.
Cependant, évaluons la distance forte entre deux termes distincts $e_n$ et $e_m$ ($n \neq m$) :
$\|e_n - e_m\|^2 = \langle e_n - e_m, e_n - e_m \rangle = \|e_n\|^2 + \|e_m\|^2 - 2\langle e_n, e_m \rangle = 1 + 1 - 0 = 2$.
Ainsi $\|e_n - e_m\| = \sqrt{2} \neq 0$. La suite $(e_n)$ n'est pas de Cauchy en norme forte, elle ne peut donc pas converger fortement.
