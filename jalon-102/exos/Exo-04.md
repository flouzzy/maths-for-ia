# Exercice 4

## Exercice 4 : Sous-espaces fermés et topologie faible \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $E$ un espace de Banach et $F$ un sous-espace vectoriel de $E$. Montrer que $F$ est fortement fermé si et seulement si $F$ est faiblement fermé.

**Correction :**
*Analyse de l'énoncé :* La topologie faible est moins fine que la topologie forte, donc tout fermé faible est fortement fermé. L'implication inverse utilise le théorème d'Hahn-Banach (forme géométrique).
*Résolution pas-à-pas :*
1. **Étape 1 : Faiblement fermé implique fortement fermé.**
   Puisque la topologie forte a plus d'ouverts (et donc plus de fermés) que la topologie faible, tout ensemble fermé pour la topologie faible l'est aussi pour la topologie forte.
2. **Étape 2 : Fortement fermé implique faiblement fermé.**
   Supposons $F$ fortement fermé et convexe (un sous-espace vectoriel est toujours convexe).
   Soit $x_0 \notin F$. Nous voulons montrer que le complémentaire de $F$ est faiblement ouvert, ou de manière équivalente, qu'il existe un voisinage faible de $x_0$ disjoint de $F$.
   Par le théorème de Hahn-Banach géométrique (seconde forme), séparant le compact $\{x_0\}$ du fermé convexe $F$, il existe une forme linéaire $f \in E^*$ et un réel $\alpha$ tels que :
   $$f(x_0) < \alpha < \inf_{x \in F} f(x)$$
   Comme $F$ est un sous-espace vectoriel, $f(F)$ est un sous-espace vectoriel de $\mathbb{K}$.
   La seule façon pour $f(F)$ d'être minoré par $\alpha$ est que $f(F) = \{0\}$.
   Ainsi, $\inf_{x \in F} f(x) = 0$. Donc $f(x_0) < 0$ et $f_{|F} = 0$.
   Considérons l'ouvert faible $V = \{ y \in E \mid f(y) < 0 \}$.
   On a $x_0 \in V$, et pour tout $x \in F$, $f(x) = 0$, donc $x \notin V$.
   Ainsi, $V \cap F = \emptyset$. Ceci prouve que le complémentaire de $F$ est un voisinage faible pour chacun de ses points, donc il est faiblement ouvert, et $F$ est faiblement fermé.
