## Exercice 9 : Indépendance et Axiomes croisés
$\bigstar\bigstar\bigstar\bigstar\bigstar$

### Énoncé

Soient deux événements indépendants $A$ et $B$ dans $(\Omega, \mathcal{F}, \mathbb{P})$. (Rappel : par définition de l'indépendance, $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$).
1. En utilisant uniquement les axiomes de Kolmogorov et les propriétés ensemblistes (complémentaires, unions disjointes), prouver rigoureusement que $A$ et le complémentaire $B^c$ sont également indépendants.
2. Démontrer que si $A$ est indépendant de lui-même, alors $\mathbb{P}(A) = 0$ ou $\mathbb{P}(A) = 1$. (Les seuls événements indépendants d'eux-mêmes sont les événements presques sûrs ou presques impossibles).


### Correction Détaillée

1. **Indépendance de $A$ et $B^c$ :**
Pour prouver que $A$ et $B^c$ sont indépendants, nous devons démontrer que :
$\mathbb{P}(A \cap B^c) = \mathbb{P}(A)\mathbb{P}(B^c)$.

Décomposons l'événement $A$ en deux parties disjointes selon $B$ :
La partie de $A$ qui est dans $B$, et la partie de $A$ qui n'est pas dans $B$.
$A = (A \cap B) \cup (A \cap B^c)$.
Puisque $(A \cap B)$ et $(A \cap B^c)$ sont disjoints, l'axiome d'additivité finie donne :
$\mathbb{P}(A) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap B^c)$.

Isolons le terme qui nous intéresse :
$\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$.

Par hypothèse, $A$ et $B$ sont indépendants, donc $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$. On substitue :
$\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B)$.

Factorisons par $\mathbb{P}(A)$ :
$\mathbb{P}(A \cap B^c) = \mathbb{P}(A) (1 - \mathbb{P}(B))$.

D'après la propriété du complémentaire (dérivée de l'axiome de la masse totale), $1 - \mathbb{P}(B) = \mathbb{P}(B^c)$. Donc :
$\mathbb{P}(A \cap B^c) = \mathbb{P}(A)\mathbb{P}(B^c)$.
La propriété est démontrée : l'indépendance est préservée par passage au complémentaire.

2. **Événement indépendant de lui-même :**
Par hypothèse, $A$ est indépendant de $A$. La définition de l'indépendance donne :
$\mathbb{P}(A \cap A) = \mathbb{P}(A)\mathbb{P}(A) = \mathbb{P}(A)^2$.

Or, d'un point de vue ensembliste (idempotence de l'intersection), on a trivialement $A \cap A = A$.
Donc la probabilité est aussi :
$\mathbb{P}(A \cap A) = \mathbb{P}(A)$.

En égalisant les deux expressions, on obtient l'équation :
$\mathbb{P}(A)^2 = \mathbb{P}(A)$.
$\mathbb{P}(A)^2 - \mathbb{P}(A) = 0$.
$\mathbb{P}(A) (\mathbb{P}(A) - 1) = 0$.

C'est un polynôme du second degré ayant pour seules racines réelles :
Soit $\mathbb{P}(A) = 0$.
Soit $\mathbb{P}(A) = 1$.
Les événements déterministes (presque sûrs ou presque impossibles) sont les seuls à ne dépendre que d'eux-mêmes en termes d'information probabiliste.
