# Exercice 9 : Hahn-Banach et Dualité $\bigstar\bigstar\bigstar\bigstar\bigstar$
Justifier rigoureusement que si $\bar{S} \neq E$ (où $E$ est un espace de Banach réel et $S$ un sous-espace vectoriel), il existe une forme linéaire continue $L \in E^*$ telle que $L_{|S} = 0$ et $L \neq 0$.

\textbf{Correction détaillée}
Soit $x_0 \in E \setminus \bar{S}$.
Puisque $\bar{S}$ est un sous-espace vectoriel fermé, la distance $d = \inf_{y \in \bar{S}} \|x_0 - y\|$ est strictement positive ($d > 0$).
Considérons le sous-espace $F = \bar{S} \oplus \mathbb{R}x_0$.
Définissons une forme linéaire $f_0 : F \to \mathbb{R}$ par $f_0(y + \lambda x_0) = \lambda d$ pour tout $y \in \bar{S}$ et $\lambda \in \mathbb{R}$.
Vérifions sa continuité sur $F$ :
Pour $\lambda \neq 0$, $\|y + \lambda x_0\| = |\lambda| \| \frac{y}{\lambda} + x_0 \| \ge |\lambda| d$.
Donc $|f_0(y + \lambda x_0)| = |\lambda| d \le \|y + \lambda x_0\|$.
Ainsi, $f_0$ est continue et sa norme sur $F$ est $\le 1$ (en fait exactement 1).
Par le théorème de Hahn-Banach analytique, il existe un prolongement linéaire $L : E \to \mathbb{R}$ tel que $L_{|F} = f_0$ et $\|L\|_{E^*} = \|f_0\|_{F^*} = 1$.
Puisque pour $y \in S$, $L(y) = f_0(y) = 0$, $L$ s'annule sur $S$.
Comme $L(x_0) = f_0(x_0) = d > 0$, $L$ n'est pas la forme nulle.
