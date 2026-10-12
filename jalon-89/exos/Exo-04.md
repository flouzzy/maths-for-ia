# Exercice 4 : Série de probabilités non monotones

$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(A_n)$ une suite d'événements indépendants. On sait que $\mathbb{P}(A_n) = \frac{1}{n \ln(n)}$ pour $n \ge 2$.
Déterminer la probabilité que les événements $A_n$ se réalisent une infinité de fois.

**Correction :**
Nous devons déterminer la nature de la série $\sum_{n=2}^\infty \mathbb{P}(A_n) = \sum_{n=2}^\infty \frac{1}{n \ln(n)}$.
La fonction $f(x) = \frac{1}{x \ln(x)}$ est continue, positive et décroissante sur $[2, +\infty[$.
On peut utiliser le critère intégral de Cauchy.
L'intégrale généralisée $\int_2^\infty \frac{1}{x \ln(x)} dx$ se calcule aisément avec le changement de variable $u = \ln(x)$, $du = \frac{dx}{x}$ :
$$ \int_{\ln(2)}^\infty \frac{1}{u} du = \left[ \ln|u| \right]_{\ln(2)}^\infty = +\infty $$
Puisque l'intégrale diverge, la série $\sum \frac{1}{n \ln(n)}$ diverge également.
Les événements $A_n$ étant indépendants, et la somme de leurs probabilités divergeant, le second lemme de Borel-Cantelli nous permet de conclure.
La probabilité que les événements $A_n$ se réalisent une infinité de fois est de 1.
$$ \mathbb{P}(\limsup A_n) = 1 $$
