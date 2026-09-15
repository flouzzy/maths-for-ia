# Exercice 4 : Calcul de volume par Fubini $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $D = \{ (x, y) \in \mathbb{R}^2 \mid x^2 + y^2 \le 1 \}$.
Calculer l'intégrale double :
$$ V = \iint_D (1 - x^2 - y^2) \, dx \, dy $$
Cette intégrale représente le volume du solide compris entre le plan $z=0$ et le paraboloïde $z = 1 - x^2 - y^2$.

## Correction

La fonction $f(x, y) = 1 - x^2 - y^2$ est continue et positive sur le disque unité fermé $D$ (qui est compact, donc de mesure finie). Le théorème de Tonelli/Fubini s'applique.
Passons en coordonnées polaires pour simplifier le domaine, ce qui est une application de la formule du changement de variables (qui préserve la mesurabilité et l'intégrabilité).
On pose $x = r \cos \theta$ et $y = r \sin \theta$.
Le domaine $D$ est décrit par $0 \le r \le 1$ et $0 \le \theta < 2\pi$.
Le déterminant de la matrice jacobienne est $r$.
L'intégrale devient :
$$ V = \int_0^{2\pi} \int_0^1 (1 - r^2) r \, dr \, d\theta $$
Par le théorème de Tonelli, comme les bornes sont indépendantes, on peut séparer :
$$ V = \left( \int_0^{2\pi} d\theta \right) \times \left( \int_0^1 (r - r^3) \, dr \right) $$
Calculons chaque terme :
$$ \int_0^{2\pi} d\theta = 2\pi $$
$$ \int_0^1 (r - r^3) \, dr = \left[ \frac{r^2}{2} - \frac{r^4}{4} \right]_0^1 = \frac{1}{2} - \frac{1}{4} = \frac{1}{4} $$
Donc :
$$ V = 2\pi \times \frac{1}{4} = \frac{\pi}{2} $$
Le volume du solide est $\frac{\pi}{2}$.
