# Exercice 8 : Matrice de Gram et formes quadratiques

## Énoncé
Soit $E$ un espace préhilbertien réel muni du produit scalaire $\langle \cdot, \cdot \rangle$.
Soit une famille de vecteurs $v_1, \dots, v_n \in E$. La matrice de Gram associée est $G = (g_{ij})$ avec $g_{ij} = \langle v_i, v_j \rangle$.
Montrer que la forme quadratique associée à $G$ (définie sur $\mathbb{R}^n$) est toujours positive.
À quelle condition est-elle définie positive ?

## Correction Détaillée (Zéro Ellipse)

La matrice de Gram $G$ est une matrice de taille $n \times n$. Elle est symétrique car le produit scalaire réel est symétrique ($g_{ij} = \langle v_i, v_j \rangle = \langle v_j, v_i \rangle = g_{ji}$).
Soit $q$ la forme quadratique sur $\mathbb{R}^n$ dont la matrice est $G$.
Pour tout vecteur $X \in \mathbb{R}^n$, où $X = (x_1, \dots, x_n)^T$, on a par définition :
$$ q(X) = X^T G X = \sum_{i=1}^n \sum_{j=1}^n x_i g_{ij} x_j $$
Substituons l'expression de $g_{ij}$ :
$$ q(X) = \sum_{i=1}^n \sum_{j=1}^n x_i \langle v_i, v_j \rangle x_j $$
Par bilinéarité du produit scalaire, nous pouvons entrer les scalaires $x_i$ et $x_j$ à l'intérieur :
$$ q(X) = \sum_{i=1}^n \sum_{j=1}^n \langle x_i v_i, x_j v_j \rangle $$
On peut factoriser la double somme par rapport aux deux variables du produit scalaire :
$$ q(X) = \left\langle \sum_{i=1}^n x_i v_i , \sum_{j=1}^n x_j v_j \right\rangle $$
Posons le vecteur $V = \sum_{i=1}^n x_i v_i \in E$.
La formule devient :
$$ q(X) = \langle V, V \rangle = \|V\|^2 $$
La norme au carré d'un vecteur d'un espace préhilbertien est un nombre réel positif ou nul.
Donc, $\forall X \in \mathbb{R}^n, q(X) \ge 0$. La forme quadratique est positive.

**Condition pour qu'elle soit définie positive :**
La forme $q$ est définie positive si $q(X) = 0 \implies X = 0_{\mathbb{R}^n}$.
Supposons $q(X) = 0$.
Cela signifie que $\|V\|^2 = 0$, et par la séparation de la norme, $V = 0_E$.
On a donc $\sum_{i=1}^n x_i v_i = 0_E$.
- Si la famille $(v_1, \dots, v_n)$ est **libre**, la seule solution de cette combinaison linéaire nulle est d'avoir tous les coefficients nuls : $x_1 = \dots = x_n = 0$. Donc $X = 0_{\mathbb{R}^n}$, ce qui signifie que $q$ est définie positive.
- Si la famille est **liée**, il existe des coefficients $x_i$ non tous nuls tels que $\sum_{i=1}^n x_i v_i = 0_E$. Pour le vecteur $X \neq 0$ correspondant, on aura $q(X) = 0$, donc $q$ ne sera pas définie positive.

Conclusion : La forme quadratique est définie positive si et seulement si la famille $(v_1, \dots, v_n)$ est libre. $\blacksquare$
