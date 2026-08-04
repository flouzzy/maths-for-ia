# Exercice 6 : Différentielle d'une application bilinéaire $\quad \bigstar\bigstar\star\star\star$
## Énoncé
Soit $B : \mathbb{R}^n \times \mathbb{R}^p \to \mathbb{R}^m$ une application bilinéaire.
Démontrer en utilisant la définition par développement limité que sa différentielle en un point $a = (x_0, y_0)$ appliquée à un vecteur $h = (h_x, h_y)$ est :
$$ dB_{(x_0, y_0)}(h_x, h_y) = B(x_0, h_y) + B(h_x, y_0) $$
## Correction Détaillée
Calculons $B(a+h) = B(x_0+h_x, y_0+h_y)$.
Par bilinéarité de $B$ :
$$ B(x_0+h_x, y_0+h_y) = B(x_0, y_0+h_y) + B(h_x, y_0+h_y) $$
$$ B(x_0+h_x, y_0+h_y) = B(x_0, y_0) + B(x_0, h_y) + B(h_x, y_0) + B(h_x, h_y) $$
Analysons les termes :
- $B(x_0, y_0) = B(a)$ (la constante).
- L'application $L : (h_x, h_y) \mapsto B(x_0, h_y) + B(h_x, y_0)$ est linéaire par rapport à $h=(h_x, h_y)$.
- Le terme de reste est $R(h) = B(h_x, h_y)$.
Montrons que $R(h) = o(\|h\|)$.
Puisque $B$ est bilinéaire sur des espaces de dimension finie, elle est continue. Il existe $C > 0$ tel que $\|B(u, v)\| \le C\|u\|\|v\|$.
$\|R(h)\| = \|B(h_x, h_y)\| \le C \|h_x\| \|h_y\|$.
Or $\|h_x\| \le \|h\|$ et $\|h_y\| \le \|h\|$ (où $\|h\| = \max(\|h_x\|, \|h_y\|)$ par exemple).
Donc $\|R(h)\| \le C \|h\|^2$.
Par conséquent, $\frac{\|R(h)\|}{\|h\|} \le C\|h\| \to 0$ quand $h \to 0$.
La différentielle est donc bien l'application linéaire $L$.
$\blacksquare$
