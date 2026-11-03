# Exercice 8 : Décomposition polaire (Introduction) $\bigstar\bigstar\bigstar\bigstar\star$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$.
On définit un opérateur dit "absolu" lié à $T$ via la construction de l'opérateur auto-adjoint $A = T^* T$.
1. Montrer que $A$ est auto-adjoint et positif (c'est-à-dire $\forall x \in H, \langle Ax, x \rangle \ge 0$).
2. Soit $\lambda \in \mathbb{C}$ une valeur propre de $A$ et $x$ un vecteur propre associé non nul. Montrer que $\lambda$ est un nombre réel positif ou nul.
3. Si $T$ est normal (c'est-à-dire $T^* T = T T^*$), démontrer rigoureusement que $\|Tx\| = \|T^*x\|$ pour tout vecteur $x \in H$.

## Correction
1. Vérifions d'abord que $A$ est auto-adjoint.
En utilisant la propriété d'involution de l'adjoint $(ST)^* = T^*S^*$ (démontrée dans l'exercice 2) :
$$ A^* = (T^* T)^* = T^* (T^*)^* = T^* T = A $$
Donc $A$ est bien un opérateur auto-adjoint.
Montrons qu'il est positif. Soit un vecteur quelconque $x \in H$. Évaluons $\langle Ax, x \rangle$ :
$$ \langle Ax, x \rangle = \langle (T^*T)x, x \rangle $$
Par définition de l'opérateur adjoint $T^*$, on le transfère sur le second membre. Il devient $(T^*)^* = T$ :
$$ = \langle Tx, Tx \rangle = \|Tx\|^2 $$
Comme la norme d'un vecteur dans un espace de Hilbert est toujours un nombre réel positif ou nul, on conclut que :
$$ \langle Ax, x \rangle \ge 0 \quad \forall x \in H $$
L'opérateur $A$ est donc positif.

2. Supposons que $Ax = \lambda x$ avec $x \ne 0_H$.
Calculons le produit scalaire $\langle Ax, x \rangle$ :
$$ \langle Ax, x \rangle = \langle \lambda x, x \rangle = \lambda \langle x, x \rangle = \lambda \|x\|^2 $$
D'autre part, d'après la question 1, nous avons établi que $\langle Ax, x \rangle = \|Tx\|^2$.
Par conséquent, on obtient l'égalité :
$$ \lambda \|x\|^2 = \|Tx\|^2 $$
Puisque $x \ne 0_H$, on sait que sa norme est strictement positive ($\|x\|^2 > 0$). On peut donc diviser par cette quantité :
$$ \lambda = \frac{\|Tx\|^2}{\|x\|^2} $$
Le membre de droite est le quotient de deux nombres réels positifs ou nuls. Il en résulte que $\lambda \in \mathbb{R}$ et $\lambda \ge 0$.

3. Hypothèse : L'opérateur $T$ est normal, donc $T^*T = TT^*$.
Soit $x \in H$. Considérons le carré de la norme de $Tx$ et utilisons la définition de l'adjoint :
$$ \|Tx\|^2 = \langle Tx, Tx \rangle = \langle x, T^*(Tx) \rangle = \langle x, (T^*T)x \rangle $$
Utilisons maintenant la propriété de normalité de l'opérateur pour substituer $T^*T$ par $TT^*$ :
$$ = \langle x, (TT^*)x \rangle = \langle x, T(T^*x) \rangle $$
Appliquons à nouveau la définition de l'adjoint pour déplacer l'opérateur $T$ du second membre vers le premier membre. Son adjoint est $T^*$ :
$$ = \langle T^*x, T^*x \rangle = \|T^*x\|^2 $$
Nous avons ainsi démontré la chaîne d'égalités rigoureuse $\|Tx\|^2 = \|T^*x\|^2$, ce qui implique, par prise de la racine carrée (les normes étant positives), que :
$$ \|Tx\| = \|T^*x\| \quad \forall x \in H $$
