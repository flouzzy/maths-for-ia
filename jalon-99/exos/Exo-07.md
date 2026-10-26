# Exercice 7
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $E$ un espace vectoriel normé et $M$ un sous-espace vectoriel fermé de $E$.
Montrer que pour tout $x_0 \in E \setminus M$, il existe une forme linéaire continue $f \in E^*$ telle que $f(x) = 0$ pour tout $x \in M$, et $f(x_0) = 1$.

**Correction :**
1. **Modélisation du problème avec Hahn-Banach géométrique :**
   L'ensemble $M$ est un sous-espace vectoriel, il est donc trivialement convexe. Par hypothèse, il est fermé.
   L'ensemble $B = \{x_0\}$ est un singleton, il est donc convexe et compact.
   Comme $x_0 \notin M$, les ensembles $M$ et $B$ sont disjoints.
   Les conditions de la deuxième forme géométrique du théorème de Hahn-Banach sont réunies pour la séparation stricte de $M$ et $\{x_0\}$.
2. **Application du théorème :**
   Il existe une forme linéaire $g \in E^*$, un réel $\alpha$ et une constante stricte $\varepsilon > 0$ tels que :
   $\forall x \in M, \quad g(x) \le \alpha - \varepsilon$
   $g(x_0) \ge \alpha + \varepsilon$
3. **Exploitation de la structure de sous-espace vectoriel :**
   L'inégalité sur $M$ affirme que la forme linéaire $g$ est majorée (par $\alpha - \varepsilon$) sur le sous-espace $M$.
   Or, l'image d'un sous-espace vectoriel par une forme linéaire (qui n'y est pas identiquement nulle) est nécessairement la droite réelle tout entière $\mathbb{R}$.
   Si $g$ n'était pas identiquement nulle sur $M$, il existerait un $v \in M$ tel que $g(v) \ne 0$. Alors en considérant la suite de vecteurs $\lambda v$ (qui appartiennent tous à $M$ puisque c'est un sous-espace) avec $\lambda \in \mathbb{R}$, l'image $g(\lambda v) = \lambda g(v)$ décrirait $\mathbb{R}$ en entier, et ne pourrait être majorée par la constante finie $\alpha - \varepsilon$.
   L'unique conclusion possible est que l'image de $M$ par $g$ est réduite à $0$.
   Donc, $\forall x \in M, g(x) = 0$.
4. **Normalisation de la forme linéaire :**
   Puisque $g(x) = 0$ sur $M$, la condition de majoration devient $0 \le \alpha - \varepsilon$, ce qui force $\alpha \ge \varepsilon > 0$.
   La condition sur $x_0$ devient $g(x_0) \ge \alpha + \varepsilon \ge 2\varepsilon > 0$. En particulier, $g(x_0) \ne 0$.
   Nous pouvons donc définir la forme linéaire normalisée $f = \frac{1}{g(x_0)} g$.
   $f$ est continue, car c'est un multiple scalaire d'une forme linéaire continue $g$.
   Pour tout $x \in M$, $f(x) = \frac{1}{g(x_0)} g(x) = 0$.
   Et par construction, $f(x_0) = \frac{g(x_0)}{g(x_0)} = 1$.
   Ceci clôt la démonstration rigoureuse de ce corollaire fondamental (souvent appelé lui-même théorème de Hahn-Banach dans certaines littératures).
