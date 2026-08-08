## Exercice 3 : Distances bornées \quad $\bigstar\bigstar$

**Énoncé :** Soit $(X, d)$ un espace métrique. Montrer que $\delta(x, y) = \frac{d(x, y)}{1 + d(x, y)}$ est une distance sur $X$, et qu'elle est bornée par $1$.

**Correction :**
1. **Séparation et Symétrie :** Évidentes à partir des propriétés de $d$. De plus, $\delta(x,y) < 1$ pour tout $x,y$.
2. **Inégalité triangulaire :** Soit $f(t) = \frac{t}{1+t}$. La dérivée $f'(t) = \frac{1}{(1+t)^2} > 0$, donc $f$ est strictement croissante sur $\mathbb{R}_+$.
On sait que $d(x, z) \le d(x, y) + d(y, z)$. Par croissance de $f$ :
$\delta(x, z) = f(d(x, z)) \le f(d(x, y) + d(y, z)) = \frac{d(x, y) + d(y, z)}{1 + d(x, y) + d(y, z)}$
On sépare la fraction :
$\delta(x, z) \le \frac{d(x, y)}{1 + d(x, y) + d(y, z)} + \frac{d(y, z)}{1 + d(x, y) + d(y, z)}$
En minorant les dénominateurs (en enlevant les termes positifs) :
$\delta(x, z) \le \frac{d(x, y)}{1 + d(x, y)} + \frac{d(y, z)}{1 + d(y, z)} = \delta(x, y) + \delta(y, z)$.
L'application $\delta$ est bien une métrique bornée par $1$ (et topologiquement équivalente à $d$).
