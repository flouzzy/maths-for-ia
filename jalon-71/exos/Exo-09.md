# Exercice 9 : Contre-exemple de Sierpinski (Mesurabilité) $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Le théorème de Tonelli-Fubini requiert que la fonction $f$ soit mesurable pour la **tribu produit** $\mathcal{F} \otimes \mathcal{G}$.
Est-il possible qu'une fonction soit mesurable séparément en $x$ et en $y$, mais ne soit pas mesurable sur l'espace produit ?
On rappelle l'axiome du continu (hypoyhèse, CH). Sous CH, il existe un bon ordre $\preceq$ sur $[0, 1]$ tel que pour tout $x$, l'ensemble $\{y \in [0, 1] \mid y \preceq x\}$ est dénombrable.
Soit $E = \{ (x, y) \in [0, 1]^2 \mid y \preceq x \}$.
1. Montrer que les sections $E_x$ et $E^y$ sont des boréliens simples.
2. Évaluer les intégrales itérées de $\mathbf{1}_E$.
3. Conclure sur la mesurabilité de $E$ pour la tribu produit de Lebesgue.

## Correction

**1. Sections :**
- La $x$-section de $E$ est $E_x = \{ y \in [0, 1] \mid y \preceq x \}$. Par construction, c'est un ensemble dénombrable.
Tout ensemble dénombrable de réels est un borélien (réunion dénombrable de singletons) de mesure de Lebesgue nulle. Donc $E_x$ est mesurable et $\mu(E_x) = 0$.
- La $y$-section de $E$ est $E^y = \{ x \in [0, 1] \mid y \preceq x \}$. C'est le complémentaire dans $[0, 1]$ de l'ensemble $\{x \in [0, 1] \mid x \prec y\}$. L'ensemble des prédécesseurs stricts est dénombrable, donc de mesure nulle. Son complémentaire $E^y$ a donc pour mesure $1 - 0 = 1$. C'est un borélien.
Ainsi, la fonction indicatrice $\mathbf{1}_E$ est mesurable par rapport à chaque variable fixée.

**2. Intégrales itérées :**
Pour l'intégrale en y, à x fixé :
$\int_0^1 \mathbf{1}_E(x,y) dy = \mu(E_x) = 0$.
L'intégrale itérée est $\int_0^1 \left( \int_0^1 \mathbf{1}_E(x,y) dy \right) dx = \int_0^1 0 \, dx = 0$.

Pour l'intégrale en x, à y fixé :
$\int_0^1 \mathbf{1}_E(x,y) dx = \mu(E^y) = 1$.
L'intégrale itérée est $\int_0^1 \left( \int_0^1 \mathbf{1}_E(x,y) dx \right) dy = \int_0^1 1 \, dy = 1$.

**3. Conclusion :**
Les deux intégrales itérées de cette fonction positive (elle ne prend que les valeurs 0 et 1) sont différentes ($0 \neq 1$).
Puisque le théorème de Tonelli affirme que ces intégrales devraient être égales **si** la fonction était mesurable pour la tribu produit, par contraposée, l'ensemble $E$ (et donc sa fonction indicatrice) **n'est pas** dans la tribu produit $\mathcal{B}([0, 1]) \otimes \mathcal{B}([0, 1])$.
Cet exemple pathologique justifie l'exigence fondamentale de mesurabilité conjointe dans l'énoncé de Fubini.
