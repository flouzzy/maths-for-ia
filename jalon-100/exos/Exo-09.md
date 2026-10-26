# Exercice 9 : Surjectivité et Application Ouverte (Préliminaire)
$\bigstar\bigstar\bigstar\bigstar\bigstar$
**Énoncé :**
Soient $E$ et $F$ deux espaces de Banach.
Soit $T \in \mathcal{L}(E, F)$ tel que l'image $T(B_E)$ de la boule unité de $E$ a un intérieur non vide dans $F$.
Montrer par un argument de type Baire que $T$ est surjectif (c'est le cœur de la preuve du théorème de l'application ouverte, Jalon 101).

**Correction :**
1. L'hypothèse est que l'intérieur de $\overline{T(B_E)}$ n'est pas vide.
   Or, $T$ est linéaire. L'adhérence $\overline{T(B_E)}$ est convexe et symétrique.
   Par convexité et symétrie, si un tel intérieur est non vide, alors $0$ appartient à l'intérieur de $\overline{T(B_E)}$.
   Il existe donc $r > 0$ tel que la boule $B_F(0, r) \subset \overline{T(B_E)}$.
2. Cela signifie que pour tout $y \in F$ avec $\|y\| < r$, et pour tout $\epsilon > 0$, il existe $x \in B_E$ tel que $\|y - T(x)\| < \epsilon$.
3. Fixons $y \in F$.
   Par homothétie, il existe $x_0 \in E$ avec $\|x_0\| \le \frac{1}{r} \|y\|$ tel que $\|y - T(x_0)\| \le \frac{1}{2} \|y\|$.
   Posons $y_1 = y - T(x_0)$.
   En appliquant itérativement le même raisonnement : il existe $x_n \in E$ tel que $\|x_n\| \le \frac{1}{r} \|y_n\|$ et $\|y_n - T(x_n)\| \le \frac{1}{2} \|y_n\|$, avec $y_{n+1} = y_n - T(x_n)$.
4. La norme des $y_n$ décroît géométriquement ($\|y_n\| \le 2^{-n} \|y\|$).
   Par conséquent, la série de terme général $x_n$ est absolument convergente car $\|x_n\| \le \frac{1}{r} 2^{-n} \|y\|$.
5. $E$ étant un espace de Banach, la série $\sum x_n$ converge vers un élément $X \in E$.
   Par continuité de $T$, $T(X) = \sum T(x_n) = \sum (y_n - y_{n+1}) = y_0 = y$.
6. On a ainsi montré que pour tout $y \in F$, il existe $X \in E$ tel que $T(X) = y$.
   L'application $T$ est donc surjective.