# Exercice 7 : Convergence monotone pour la fonction Gamma d'Euler
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Montrer que $\Gamma(z) = \lim_{n \to \infty} \int_0^n \left(1-\frac{t}{n}\right)^n t^{z-1} dt$ pour $z>0$.

## Correction Détaillée

Pour $t \in [0, n]$, posons $f_n(t) = \left(1-\frac{t}{n}\right)^n t^{z-1} \mathbf{1}_{[0, n]}(t)$.
On sait que pour $t \geq 0$, la suite $n \mapsto \left(1-\frac{t}{n}\right)^n$ est croissante et converge vers $e^{-t}$.
En effet, on peut écrire $\left(1-\frac{t}{n}\right)^n = \exp\left(n \ln\left(1-\frac{t}{n}\right)\right)$. L'étude de la dérivée par rapport à $n$ montre la croissance.
Donc pour $t \in [0, n]$, $f_n(t)$ est croissante et positive.
De plus, $\lim_{n \to \infty} f_n(t) = e^{-t} t^{z-1}$.
D'après le Théorème de Convergence Monotone :
$$\lim_{n \to \infty} \int_0^\infty f_n(t) dt = \int_0^\infty \lim_{n \to \infty} f_n(t) dt = \int_0^\infty e^{-t} t^{z-1} dt = \Gamma(z)$$
Ainsi, $\lim_{n \to \infty} \int_0^n \left(1-\frac{t}{n}\right)^n t^{z-1} dt = \Gamma(z)$.
