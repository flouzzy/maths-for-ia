# Exercice 9 : Continuité d'une intégrale paramétrée par Fatou
$\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $f : X \times [0, 1] \to \mathbb{R}$ mesurable en la première variable et continue en la seconde.
On suppose que pour tout $t \in [0, 1]$ et tout $x \in X$, $0 \leq f(x, t) \leq g(x)$, où $g$ est une fonction intégrable.
Définissons $F(t) = \int_X f(x, t) d\mu(x)$.
Démontrer que $F$ est continue sur $[0, 1]$ en utilisant uniquement le Lemme de Fatou (classique et inversé), sans utiliser directement le théorème de convergence dominée.

## Correction
Soit $t_0 \in [0, 1]$. Considérons une suite $t_n \to t_0$.
Posons $f_n(x) = f(x, t_n)$.
Par continuité de $f$ en la seconde variable, pour tout $x \in X$, $\lim_{n \to \infty} f_n(x) = f(x, t_0)$.
Donc $\liminf f_n = \limsup f_n = f(\cdot, t_0)$.

**1. Application de Fatou classique (Borne inférieure) :**
Les fonctions $f_n$ sont positives ($f_n \geq 0$).
Par le Lemme de Fatou :
$$\int_X (\liminf f_n) d\mu \leq \liminf \int_X f_n d\mu$$
$$\int_X f(x, t_0) d\mu \leq \liminf_{n \to \infty} F(t_n)$$
Soit $F(t_0) \leq \liminf_{n \to \infty} F(t_n)$.

**2. Application de Fatou inversé (Borne supérieure) :**
Les fonctions $f_n$ sont majorées par $g$, fonction intégrable.
On peut appliquer le résultat de l'exercice 6 (Fatou inversé) :
$$\limsup \int_X f_n d\mu \leq \int_X (\limsup f_n) d\mu$$
$$\limsup_{n \to \infty} F(t_n) \leq \int_X f(x, t_0) d\mu$$
Soit $\limsup_{n \to \infty} F(t_n) \leq F(t_0)$.

**3. Synthèse :**
Par définition générale des limites inf et sup d'une suite réelle, on a toujours :
$$\liminf_{n \to \infty} F(t_n) \leq \limsup_{n \to \infty} F(t_n)$$
En chaînant les inégalités obtenues en 1 et 2, on obtient la sandwicherie :
$$F(t_0) \leq \liminf F(t_n) \leq \limsup F(t_n) \leq F(t_0)$$
La seule possibilité est que toutes ces valeurs soient égales.
Donc $\liminf F(t_n) = \limsup F(t_n) = F(t_0)$.
Cela signifie que la suite $(F(t_n))$ converge et que sa limite est $F(t_0)$.
Comme ceci est vrai pour toute suite $t_n \to t_0$, $F$ est séquentiellement continue (donc continue) en $t_0$.
