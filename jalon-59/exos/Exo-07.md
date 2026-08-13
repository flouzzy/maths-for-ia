### Exercice 7 : Application de l'équicontinuité aux suites de primitives \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions continues sur $[0, 1]$ convergeant simplement vers $f$, avec $\sup_{n, x} |f_n(x)| \le M$. Posons $F_n(x) = \int_0^x f_n(t) dt$. Montrer que $(F_n)$ admet une sous-suite uniformément convergente.

**Correction :**
Étudions la famille $(F_n)$.
1. $F_n(0) = 0$ pour tout $n$, donc la suite de valeurs en $0$ est trivialement bornée.
2. Pour $x \in [0, 1]$, $|F_n(x)| \le \int_0^x |f_n(t)| dt \le Mx \le M$. Les $F_n$ sont donc bornées ponctuellement (et même uniformément).
3. **Équicontinuïté :** Pour $x, y \in [0, 1]$ avec $x > y$,
$$ |F_n(x) - F_n(y)| = \left| \int_y^x f_n(t) dt \right| \le \int_y^x |f_n(t)| dt \le M(x-y) $$
Toutes les fonctions $F_n$ sont $M$-lipschitziennes, donc la famille est uniformément équicontinue.
Par le théorème d'Arzelà-Ascoli, il existe une sous-suite $(F_{n_k})$ qui converge uniformément sur $[0, 1]$.
