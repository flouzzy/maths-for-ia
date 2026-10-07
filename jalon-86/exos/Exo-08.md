# Exercice 8

## Exercice 8 : Variables aléatoires de même loi $\bigstar\bigstar\bigstar\bigstar\star$

Donner un exemple explicite de deux variables aléatoires $X$ et $Y$ définies sur le même espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$, ayant la même loi de probabilité ($\mathbb{P}_X = \mathbb{P}_Y$), mais telles que l'événement $\{ X = Y \}$ a une probabilité nulle.

### Correction pas à pas

1. **Choix de l'espace probabilisé**
   Prenons l'expérience classique d'un lancer de dé ou d'une pièce. Pour avoir des probabilités nulles sur une égalité exacte, il vaut mieux choisir un espace continu.
   Soit $\Omega = [0, 1]$ muni de la tribu borélienne $\mathcal{B}([0, 1])$ et de la mesure de Lebesgue $\mathbb{P}$ (probabilité uniforme sur $[0, 1]$).

2. **Construction des deux variables**
   - Soit $X : \Omega \to \mathbb{R}$ définie par $X(\omega) = \omega$.
     C'est la variable identité. Sa loi est la loi uniforme sur $[0, 1]$, notée $\mathcal{U}([0, 1])$.
   - Soit $Y : \Omega \to \mathbb{R}$ définie par la symétrie : $Y(\omega) = 1 - \omega$.

3. **Vérification de la loi de $Y$**
   Calculons la fonction de répartition de $Y$ pour $y \in [0, 1]$ :
   $F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(1 - \omega \leq y) = \mathbb{P}(\omega \geq 1 - y)$.
   Puisque $\omega$ suit une loi uniforme, la probabilité d'être supérieur à $1-y$ est la longueur de l'intervalle $[1-y, 1]$, qui vaut : $1 - (1 - y) = y$.
   On retrouve $F_Y(y) = y$ sur $[0, 1]$. C'est exactement la fonction de répartition de la loi $\mathcal{U}([0, 1])$.
   Donc $X$ et $Y$ ont la même loi (Loi Uniforme sur $[0, 1]$).

4. **Calcul de la probabilité de l'égalité**
   Étudions l'événement $\{ X = Y \}$.
   $X(\omega) = Y(\omega) \iff \omega = 1 - \omega \iff 2\omega = 1 \iff \omega = \frac{1}{2}$.
   Ainsi, $\{ \omega \in \Omega \mid X(\omega) = Y(\omega) \} = \left\{ \frac{1}{2} \right\}$.
   La probabilité d'obtenir exactement un point précis (un singleton) avec la mesure de Lebesgue sur $[0, 1]$ est nulle :
   $$ \mathbb{P}\left(\left\{ \frac{1}{2} \right\}\right) = 0 $$
   Nous avons bien construit deux variables de même loi mais presque sûrement distinctes.
