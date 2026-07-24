# Exercice 9 : ★★★★★

**Énoncé :**
Distance à un compact

**Correction (Zéro Ellipse) :**
Soit $K$ un compact non vide de $E$, et $x \in E$. Montrer qu'il existe un point $y \in K$ tel que $\|x - y\| = \inf_{z \in K} \|x - z\|$.

Posons $d = \inf_{z \in K} \|x - z\|$.
Par définition de la borne inférieure (infimum), il existe une suite $(z_n)_{n \in \mathbb{N}}$ d'éléments de $K$ telle que la suite des distances $\|x - z_n\|$ converge vers $d$.
Puisque la suite $(z_n)$ prend ses valeurs dans le compact $K$, le théorème de Bolzano-Weierstrass nous garantit l'existence d'une sous-suite extraite $(z_{\phi(n)})_{n \in \mathbb{N}}$ qui converge vers un élément $y \in K$.
Considérons l'application distance $f : z \mapsto \|x - z\|$.
Par l'inégalité triangulaire inversée, $\big| \|x - z_1\| - \|x - z_2\| \big| \le \|z_1 - z_2\|$.
Donc $f$ est 1-lipschitzienne, et par suite, continue sur $E$.
La sous-suite $z_{\phi(n)}$ converge vers $y$. Par continuité de $f$, $f(z_{\phi(n)})$ converge vers $f(y)$.
Donc $\lim_{n \to \infty} \|x - z_{\phi(n)}\| = \|x - y\|$.
Cependant, la suite $(\|x - z_n\|)_n$ converge vers $d$, donc toute sous-suite extraite converge également vers $d$.
En identifiant les limites, on obtient $\|x - y\| = d$.
Le minimum de la distance est donc bien atteint en $y \in K$. $\blacksquare$
