### Limite d'une intégrale tronquée \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f \in \mathcal{M}_+$. On définit $f_n(x) = \min(f(x), n)$.
Montrer que pour tout $x$, $f_n(x)$ est une suite croissante, et exprimer la relation entre $\sup_n \int f_n d\mu$ et $\int f d\mu$ (en l'admettant comme cas particulier de Beppo-Levi, ou en le montrant directement).

**Correction Détaillée :**
**Étape 1 : Croissance de la suite.**
Pour tout $x \in X$, $f_n(x) = \min(f(x), n)$.
Évidemment, $\min(f(x), n) \le \min(f(x), n+1)$ car $n < n+1$.
Donc $f_n \le f_{n+1}$. La suite de fonctions est positive et croissante.
De plus, $\lim_{n \to \infty} f_n(x) = f(x)$.

**Étape 2 : Relation d'ordre sur les intégrales.**
Puisque $f_n \le f$, la croissance de l'intégrale assure que pour tout $n$, $\int f_n d\mu \le \int f d\mu$.
En passant au supremum (ou à la limite, puisque la suite est croissante) :
$$\sup_n \int f_n d\mu \le \int f d\mu$$

**Étape 3 : Inégalité inverse.**
L'égalité $\sup_n \int f_n d\mu = \int f d\mu$ est une conséquence directe du théorème de convergence monotone (Beppo-Levi), qui sera formellement prouvé au Jalon suivant.
L'intérêt de cette troncature est que chaque $f_n$ est bornée. Si la mesure de l'espace est finie, les $f_n$ sont dans des espaces plus réguliers (comme $L^\infty$), facilitant certains passages à la limite analytiques.
