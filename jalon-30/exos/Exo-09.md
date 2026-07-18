# Exercice 9 : Propriétés topologiques de l'ensemble des matrices diagonalisables (★★★★★)

Montrer que sur le corps $\mathbb{C}$, l'ensemble des matrices diagonalisables de $\mathcal{M}_n(\mathbb{C})$ est dense dans $\mathcal{M}_n(\mathbb{C})$.
*Indication : Utiliser le théorème de trigonalisation et perturber les éléments de la diagonale pour les rendre tous distincts.*

### Solution :

Cet exercice fait le lien crucial entre l'algèbre linéaire structurelle (trigonalisation) et la topologie des espaces de matrices.
Soit $A \in \mathcal{M}_n(\mathbb{C})$.
D'après le théorème de d'Alembert-Gauss, le polynôme caractéristique de $A$, $\chi_A$, est scindé sur $\mathbb{C}$.
Par le théorème de trigonalisation, il existe une matrice de passage $P \in GL_n(\mathbb{C})$ et une matrice triangulaire supérieure $T$ telles que :
$$ A = P T P^{-1} $$
Soient $\lambda_1, \lambda_2, \ldots, \lambda_n$ les coefficients diagonaux de $T$ (qui sont les valeurs propres de $A$).
Si ces coefficients sont tous distincts, la matrice $A$ est déjà diagonalisable et il n'y a rien à faire.
Si certains sont multiples, l'idée est de les "perturber" légèrement pour forcer le polynôme caractéristique à avoir $n$ racines simples, ce qui garantira la diagonalisabilité.

Pour tout entier $k \in \mathbb{N}^*$, on construit une matrice $T_k$ triangulaire supérieure telle que :
- Les éléments strictement au-dessus de la diagonale de $T_k$ sont les mêmes que ceux de $T$.
- Les éléments diagonaux de $T_k$ sont notés $\lambda_{1}^{(k)}, \ldots, \lambda_{n}^{(k)}$, choisis de sorte que :
  1. $\forall i \in \llbracket 1, n \rrbracket, \lim_{k \to +\infty} \lambda_{i}^{(k)} = \lambda_i$
  2. $\forall k \in \mathbb{N}^*, \forall i \neq j, \lambda_{i}^{(k)} \neq \lambda_{j}^{(k)}$

Un tel choix est toujours possible. Par exemple, on peut poser $\lambda_{i}^{(k)} = \lambda_i + \frac{\epsilon_i}{k}$, où les $\epsilon_i \in \mathbb{C}$ sont choisis de manière astucieuse pour éviter toute coïncidence (l'ensemble des coïncidences est un nombre fini de droites dans $\mathbb{C}$, on peut s'y soustraire).

Ainsi, par construction, la matrice $T_k$ possède $n$ valeurs propres distinctes.
Une condition suffisante de diagonalisabilité assure que $T_k$ est diagonalisable.

Posons ensuite $A_k = P T_k P^{-1}$.
Puisque $T_k$ est diagonalisable, $A_k$ est la conjuguée d'une matrice diagonalisable, donc $A_k$ est elle-même diagonalisable.
La suite $(A_k)_{k \in \mathbb{N}^*}$ est donc une suite de matrices diagonalisables.

De plus, par continuité des opérations matricielles (produit et addition), et sachant que $\lim_{k \to +\infty} T_k = T$, on a :
$$ \lim_{k \to +\infty} A_k = \lim_{k \to +\infty} (P T_k P^{-1}) = P \left( \lim_{k \to +\infty} T_k \right) P^{-1} = P T P^{-1} = A $$
Nous avons ainsi construit une suite de matrices diagonalisables convergeant vers notre matrice arbitraire $A$.
L'ensemble des matrices diagonalisables est par conséquent topologiquement dense dans l'espace $\mathcal{M}_n(\mathbb{C})$.

Cette densité est fondamentale : elle permet souvent de démontrer une propriété continue (comme l'identité de Cayley-Hamilton) d'abord sur les matrices diagonalisables (où c'est trivial), puis de l'étendre à toutes les matrices par un argument de continuité (passage à la limite).
