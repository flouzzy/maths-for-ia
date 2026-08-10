# Exercice 1 : Axiomes de base et distance usuelle
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé formel
Soit $X = \mathbb{R}$. Montrer que la fonction $d(x, y) = |x - y|$ définit bien une distance sur $\mathbb{R}$. Que se passe-t-il si on remplace la valeur absolue par la fonction $f(t) = t^2$ (i.e. $d'(x,y) = (x-y)^2$) ?

## Résolution pas à pas
**Étape 1 : Vérification des axiomes pour la valeur absolue**

1. **Séparation :** $d(x,y) = 0 \iff |x-y| = 0 \iff x-y=0 \iff x=y$.
2. **Symétrie :** $d(x,y) = |x-y| = |-(y-x)| = |-1| \cdot |y-x| = |y-x| = d(y,x)$.
3. **Inégalité triangulaire :** Pour $x,y,z \in \mathbb{R}$, on a $d(x,z) = |x-z| = |(x-y) + (y-z)|$. D'après l'inégalité triangulaire classique sur les réels, $|(x-y) + (y-z)| \le |x-y| + |y-z| = d(x,y) + d(y,z)$. Les trois axiomes sont validés.

**Étape 2 : Analyse de la fonction au carré**

Pour $d'(x,y) = (x-y)^2$, vérifions l'inégalité triangulaire. Prenons $x=0$, $y=1$ et $z=2$.
$d'(x,z) = (0-2)^2 = 4$.
$d'(x,y) + d'(y,z) = (0-1)^2 + (1-2)^2 = 1 + 1 = 2$.
On constate que $4 \not\le 2$, l'inégalité triangulaire n'est donc pas respectée. $d'$ n'est pas une distance, confirmant que le passage par un point intermédiaire ($y=1$) pourrait curieusement rendre le trajet total plus 'court' que le trajet direct si $d'$ était une métrique valide, ce qui est absurde. $\blacksquare$
