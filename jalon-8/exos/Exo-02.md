# Exercice 2 : Application linéaire de dérivation (Difficulté : *)

## Énoncé du problème

Soit $\mathbb{K}$ le corps des nombres réels, $\mathbb{K} = \mathbb{R}$.
On considère l'espace vectoriel $E = \mathbb{R}_2[X]$ des polynômes à coefficients réels de degré au plus 2. Autrement dit, $E = \{ a_0 + a_1 X + a_2 X^2 \mid a_0, a_1, a_2 \in \mathbb{R} \}$.

On définit l'application $D: E \to E$ par $D(P) = P'$, où $P'$ désigne le polynôme dérivé de $P$.

1.  Justifier que $D$ est une application linéaire.
2.  Déterminer le noyau de $D$, noté $\text{Ker}(D)$. En donner une base et sa dimension.
3.  Déterminer l'image de $D$, notée $\text{Im}(D)$. En donner une base et sa dimension.
4.  Vérifier le théorème du rang pour l'application $D$.

## Correction détaillée

### Question 1 : Justifier que $D$ est une application linéaire.

Pour montrer que $D$ est une application linéaire, nous devons vérifier deux propriétés :
1.  Additivité : $D(P+Q) = D(P) + D(Q)$ pour tous $P, Q \in E$.
2.  Homogénéité : $D(\lambda P) = \lambda D(P)$ pour tout $P \in E$ et tout scalaire $\lambda \in \mathbb{R}$.

Soient $P, Q \in E$. Par les propriétés de la dérivation des polynômes :
*   $D(P+Q) = (P+Q)' = P' + Q' = D(P) + D(Q)$.
Soit $\lambda \in \mathbb{R}$. Par les propriétés de la dérivation des polynômes :
*   $D(\lambda P) = (\lambda P)' = \lambda P' = \lambda D(P)$.

Puisque ces deux propriétés sont satisfaites, l'application $D$ est bien une application linéaire de $E$ dans $E$.

### Question 2 : Déterminer le noyau de $D$, $\text{Ker}(D)$. En donner une base et sa dimension.

Par définition, le noyau de $D$ est l'ensemble des polynômes $P \in E$ tels que $D(P) = 0_E$, où $0_E$ est le polynôme nul.
$P \in \text{Ker}(D) \iff D(P) = 0_E \iff P' = 0_E$.

Soit un polynôme $P(X) \in E$, il s'écrit sous la forme $P(X) = a_0 + a_1 X + a_2 X^2$ avec $a_0, a_1, a_2 \in \mathbb{R}$.
La dérivée de $P(X)$ est $P'(X) = a_1 + 2a_2 X$.

Pour que $P'(X)$ soit le polynôme nul, il faut que tous ses coefficients soient nuls.
Ainsi, $P'(X) = 0_E \iff a_1 = 0 \text{ et } 2a_2 = 0$.
Cela implique $a_1 = 0$ et $a_2 = 0$.

Le polynôme $P(X)$ doit donc s'écrire $P(X) = a_0 + 0 \cdot X + 0 \cdot X^2 = a_0$, où $a_0$ est un réel quelconque.
Le noyau de $D$ est donc l'ensemble des polynômes constants :
$\text{Ker}(D) = \{ a_0 \mid a_0 \in \mathbb{R} \} = \mathbb{R}_0[X]$.

Pour trouver une base de $\text{Ker}(D)$, nous pouvons observer que tout polynôme constant $P(X) = a_0$ peut s'écrire $a_0 \cdot 1$. Le polynôme constant $1$ est non nul et engendre $\text{Ker}(D)$.
Une base de $\text{Ker}(D)$ est $(1)$.
La dimension de $\text{Ker}(D)$ est le nombre de vecteurs dans cette base, donc $\dim(\text{Ker}(D)) = 1$.

### Question 3 : Déterminer l'image de $D$, $\text{Im}(D)$. En donner une base et sa dimension.

Par définition, l'image de $D$ est l'ensemble des polynômes $Q \in E$ pour lesquels il existe au moins un polynôme $P \in E$ tel que $D(P) = Q$.
$Q \in \text{Im}(D) \iff \exists P \in E \text{ tel que } P' = Q$.

Soit un polynôme $P(X) = a_0 + a_1 X + a_2 X^2 \in E$.
Son image par $D$ est $D(P) = P'(X) = a_1 + 2a_2 X$.
Tout polynôme dans l'image est donc de la forme $a_1 + 2a_2 X$.
Ces polynômes sont de degré au plus 1. L'ensemble de ces polynômes est l'espace vectoriel $\mathbb{R}_1[X]$.
Tout polynôme de $\mathbb{R}_1[X]$, disons $Q(X) = b_0 + b_1 X$, peut être obtenu comme la dérivée d'un polynôme de $\mathbb{R}_2[X]$. Par exemple, $P(X) = b_0 X + \frac{b_1}{2} X^2$ est dans $\mathbb{R}_2[X]$ et $P'(X) = b_0 + b_1 X = Q(X)$. (Nous pouvons choisir $a_0=0$ et ajuster $a_1, a_2$ pour obtenir n'importe quel $b_0+b_1X$).

Ainsi, $\text{Im}(D) = \{ a_1 + 2a_2 X \mid a_1, a_2 \in \mathbb{R} \} = \mathbb{R}_1[X]$.

Pour trouver une base de $\text{Im}(D)$, nous cherchons un ensemble de polynômes qui engendrent $\mathbb{R}_1[X]$ et sont linéairement indépendants.
Les polynômes $1$ et $X$ forment une base standard de $\mathbb{R}_1[X]$.
*   $1$ est la dérivée de $X$ (qui est dans $\mathbb{R}_2[X]$).
*   $X$ est la dérivée de $\frac{1}{2}X^2$ (qui est dans $\mathbb{R}_2[X]$).
Une base de $\text{Im}(D)$ est $(1, X)$.
La dimension de $\text{Im}(D)$ est le nombre de vecteurs dans cette base, donc $\dim(\text{Im}(D)) = 2$.

### Question 4 : Vérifier le théorème du rang pour l'application $D$.

Le théorème du rang stipule que pour une application linéaire $D: E \to F$, on a la relation :
$\dim(E) = \dim(\text{Ker}(D)) + \dim(\text{Im}(D))$.

Nous avons l'espace de départ $E = \mathbb{R}_2[X]$. Une base canonique de $\mathbb{R}_2[X]$ est $(1, X, X^2)$.
Le nombre d'éléments dans cette base est 3, donc $\dim(E) = 3$.

D'après la question 2, nous avons trouvé $\dim(\text{Ker}(D)) = 1$.
D'après la question 3, nous avons trouvé $\dim(\text{Im}(D)) = 2$.

Calculons la somme de ces dimensions :
$\dim(\text{Ker}(D)) + \dim(\text{Im}(D)) = 1 + 2 = 3$.

Nous observons que $\dim(E) = 3$ et $\dim(\text{Ker}(D)) + \dim(\text{Im}(D)) = 3$.
L'égalité est vérifiée : $\dim(E) = \dim(\text{Ker}(D)) + \dim(\text{Im}(D))$.
Le théorème du rang est bien vérifié pour l'application linéaire $D$.
