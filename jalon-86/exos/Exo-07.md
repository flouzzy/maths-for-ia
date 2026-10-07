# Exercice 7

## Exercice 7 : Loi d'une transformation affine $\bigstar\bigstar\bigstar\bigstar\star$

Soit $X$ une variable aléatoire de densité de probabilité $f_X$ (par rapport à la mesure de Lebesgue sur $\mathbb{R}$).
Soient $a \neq 0$ et $b$ deux constantes réelles. On définit la nouvelle variable aléatoire $Y = aX + b$.
Déterminer la fonction de densité $f_Y$ de la variable $Y$ en utilisant la fonction de répartition.

### Correction pas à pas

1. **Définition de la fonction de répartition de $Y$**
   La fonction de répartition $F_Y(y)$ est définie par :
   $F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(aX + b \leq y)$.

2. **Séparation des cas selon le signe de $a$**
   - **Cas 1 : $a > 0$**
     L'inégalité $aX + b \leq y$ équivaut à $X \leq \frac{y - b}{a}$.
     Donc, $F_Y(y) = \mathbb{P}\left(X \leq \frac{y - b}{a}\right) = F_X\left(\frac{y - b}{a}\right)$.

   - **Cas 2 : $a < 0$**
     L'inégalité $aX + b \leq y$ équivaut (en divisant par $a < 0$, le sens change) à $X \geq \frac{y - b}{a}$.
     Donc, $F_Y(y) = \mathbb{P}\left(X \geq \frac{y - b}{a}\right) = 1 - \mathbb{P}\left(X < \frac{y - b}{a}\right)$.
     Comme $X$ est une variable continue (elle a une densité), $\mathbb{P}(X = c) = 0$, donc $\mathbb{P}(X < c) = \mathbb{P}(X \leq c) = F_X(c)$.
     Ainsi, $F_Y(y) = 1 - F_X\left(\frac{y - b}{a}\right)$.

3. **Calcul de la densité par dérivation**
   La densité $f_Y$ s'obtient en dérivant la fonction de répartition $F_Y$ par rapport à $y$.
   Rappel : $F_X'(x) = f_X(x)$.
   - **Si $a > 0$ :**
     $$ f_Y(y) = \frac{d}{dy} F_X\left(\frac{y - b}{a}\right) = \frac{1}{a} f_X\left(\frac{y - b}{a}\right) $$
   - **Si $a < 0$ :**
     $$ f_Y(y) = \frac{d}{dy} \left[ 1 - F_X\left(\frac{y - b}{a}\right) \right] = -\frac{1}{a} f_X\left(\frac{y - b}{a}\right) $$

4. **Synthèse de la formule**
   Puisque dans le deuxième cas $a < 0$, le terme $-1/a$ est positif et correspond à $1/|a|$.
   Dans les deux cas, on peut écrire :
   $$ f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y - b}{a}\right) $$
   C'est la formule classique du changement de variable affine pour les densités.
