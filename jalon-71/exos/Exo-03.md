# Exercice 3 : Tonelli sur un domaine infini $\bigstar\bigstar\star\star\star$

## Énoncé

Calculer l'intégrale suivante en justifiant soigneusement l'utilisation du théorème de Tonelli :
$$ I = \int_0^{+\infty} \int_0^{+\infty} y e^{-(1+x)y} \, dx \, dy $$

## Correction

**Justification :**
L'espace d'intégration est $\mathbb{R}_+ \times \mathbb{R}_+$, qui est $\sigma$-fini.
La fonction $f(x, y) = y e^{-(1+x)y}$ est continue et positive sur $\mathbb{R}_+ \times \mathbb{R}_+$.
Par le théorème de Tonelli, on peut intégrer dans n'importe quel ordre, et le résultat sera dans $[0, +\infty]$.

**Calcul :**
Intégrons d'abord par rapport à $x$ en gardant $y$ constant :
$$ I = \int_0^{+\infty} y \left( \int_0^{+\infty} e^{-y} e^{-xy} \, dx \right) dy $$
$$ I = \int_0^{+\infty} y e^{-y} \left[ \frac{e^{-xy}}{-y} \right]_{x=0}^{x=+\infty} dy $$
Pour $y > 0$, $\lim_{x \to +\infty} e^{-xy} = 0$. Donc la valeur entre crochets est $0 - (-\frac{1}{y}) = \frac{1}{y}$.
Pour $y = 0$, $f(x,0) = 0$, l'intégrale est nulle. Comme on intègre en $y$, ce point de mesure nulle (Lebesgue) ne change rien.
On a donc :
$$ I = \int_0^{+\infty} y e^{-y} \times \frac{1}{y} \, dy = \int_0^{+\infty} e^{-y} \, dy $$
$$ I = \left[ -e^{-y} \right]_0^{+\infty} = 0 - (-1) = 1 $$
Ainsi, l'intégrale vaut 1.
