# Exercice 7 - Jalon 34

**Difficulté :** ★★★★

## Énoncé

Dans l'espace vectoriel $E = \mathbb{R}^2$, on définit pour un vecteur $X=(x_1, x_2)$ la fonction $N_7(X)$ comme suit. Déterminez avec une rigueur absolue si cette application est une norme.

On pose $N_7(X) = |x_1| + 7 |x_2|$.

## Correction avec Zéro Ellipse

Pour vérifier si $N_7$ est une norme, nous devons examiner méticuleusement les trois axiomes. Soit $X = (x_1, x_2) \in \mathbb{R}^2$, $Y = (y_1, y_2) \in \mathbb{R}^2$, et $\lambda \in \mathbb{R}$.

**1. Séparation :**
Supposons $N_7(X) = 0$.
Par définition, $|x_1| + 7 |x_2| = 0$.
Puisque $|x_1| \ge 0$ et $7|x_2| \ge 0$ (car $7 > 0$), la somme de deux réels positifs est nulle si et seulement si chaque terme est nul.
Donc, $|x_1| = 0$ et $7 |x_2| = 0$.
Il s'ensuit que $x_1 = 0$ et $x_2 = 0$.
Ainsi, le vecteur $X$ est le vecteur nul $(0,0)$.
L'axiome de séparation est vérifié.

**2. Homogénéité absolue :**
Calculons $N_7(\lambda X) = N_7(\lambda x_1, \lambda x_2)$.
$N_7(\lambda X) = |\lambda x_1| + 7 |\lambda x_2|$.
Par les propriétés de la valeur absolue sur les réels, $|\lambda x| = |\lambda||x|$.
Donc $N_7(\lambda X) = |\lambda| |x_1| + 7 |\lambda| |x_2|$.
En factorisant par $|\lambda|$, on obtient :
$N_7(\lambda X) = |\lambda| (|x_1| + 7 |x_2|) = |\lambda| N_7(X)$.
L'axiome d'homogénéité est vérifié.

**3. Inégalité triangulaire :**
Considérons le vecteur somme $X+Y = (x_1+y_1, x_2+y_2)$.
Calculons $N_7(X+Y) = |x_1+y_1| + 7 |x_2+y_2|$.
D'après l'inégalité triangulaire de la valeur absolue dans $\mathbb{R}$, on a $|x_1+y_1| \leq |x_1| + |y_1|$ et $|x_2+y_2| \leq |x_2| + |y_2|$.
En insérant ces majorations, puisque $7 > 0$ préserve le sens de l'inégalité :
$N_7(X+Y) \leq (|x_1| + |y_1|) + 7(|x_2| + |y_2|)$
$N_7(X+Y) \leq |x_1| + |y_1| + 7 |x_2| + 7 |y_2|$.
En réarrangeant les termes :
$N_7(X+Y) \leq (|x_1| + 7 |x_2|) + (|y_1| + 7 |y_2|)$
$N_7(X+Y) \leq N_7(X) + N_7(Y)$.
L'axiome de l'inégalité triangulaire est vérifié.

**Conclusion :**
Les trois axiomes étant rigoureusement satisfaits, l'application $N_7$ définit bien une norme sur l'espace vectoriel $\mathbb{R}^2$.
