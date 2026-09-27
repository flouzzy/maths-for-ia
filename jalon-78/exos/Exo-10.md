## Exercice 10 : Théorème d'Isopérimétrie \quad \bigstar\bigstar\bigstar\bigstar\bigstar

Utiliser l'inégalité de Wirtinger pour montrer que parmi toutes les courbes fermées simples $C^1$ de longueur $L$ du plan, le cercle a l'aire maximale $A = L^2/(4\pi)$.

**Correction :**
Soit $\gamma(s) = (x(s), y(s))$ un paramétrage par l'abscisse curviligne $s \in [0, L]$.
$(x'(s))^2 + (y'(s))^2 = 1$. L'aire est $A = \frac{1}{2} \int_0^L (x(s)y'(s) - y(s)x'(s))ds$.
En posant $t = \frac{2\pi s}{L}$, on normalise la période à $2\pi$.
On développe $x, y$ en séries de Fourier trigonométriques. En appliquant Parseval sur l'aire (qui mélange $x, y, x', y'$) et sur la longueur, on retrouve l'inégalité de Wirtinger coefficient par coefficient (les indices $n^2$ apparaissent via la dérivée). L'inégalité $A \le L^2/(4\pi)$ apparaît, avec égalité si et seulement si les coefficients non nuls sont ceux de $n=\pm1$, ce qui correspond à un cercle paramétré.
