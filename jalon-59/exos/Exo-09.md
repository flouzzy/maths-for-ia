# Exercice 9 : Équation différentielle et Théorème de Peano (Esquisse par Arzelà-Ascoli)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $F : \mathbb{R} \to \mathbb{R}$ une fonction continue, bornée par $M > 0$.
Considérons l'équation intégrale de Volterra, associée au problème de Cauchy $y' = F(y)$ avec $y(0) = 0$ :
$$ y(t) = \int_0^t F(y(s)) ds $$
Soit $(y_n)_{n\in\mathbb{N}}$ la suite d'approximations d'Euler polygonalisées de pas $1/n$ définies sur un segment fixe $[0, T]$.
Ces approximations vérifient la propriété de Lipschitz stricte : pour tout $n$, $|y'_n(t)| \le M$ (sauf aux points de cassure, où l'on prend les dérivées à droite et à gauche).

Montrer, par compacité, que cette suite admet une sous-suite convergeant vers une solution locale de l'équation différentielle (Théorème de Peano d'existence, sans unicité).

## Résolution Détaillée

Cet exercice est le sommet applicatif du théorème d'Arzelà-Ascoli dans l'étude des équations différentielles non-linéaires, où Cauchy-Lipschitz ne s'applique pas par manque de lipschitzianité de $F$.

### 1. Propriétés de la suite d'approximations

Considérons l'ensemble $\mathcal{F} = \{y_n \mid n \in \mathbb{N}^*\}$ des fonctions d'Euler sur le segment de temps compact $[0, T]$.
Les approximations polygonales d'Euler sont, par construction formelle, continues et affines par morceaux.
Sur chaque intervalle linéaire, la pente est fixée par la valeur de $F$, qui est bornée par $M$. Ainsi, pour tout $t$ régulier (hors des cassures), $|y'_n(t)| \le M$.
Par le théorème des accroissements finis (ou en intégrant la dérivée de cette fonction continue), il en découle que toutes les approximations $y_n$ sont globalement $M$-Lipschitziennes sur $[0, T]$.

### 2. Équicontinuité et Bornitude ponctuelle

- **Équicontinuité :** Puisque toute fonction de la famille est $M$-Lipschitzienne, la famille est équicontinue sur le segment compact $[0, T]$. (Il suffit de prendre $\delta = \frac{\epsilon}{M}$ universel pour toutes les fonctions $y_n$).
- **Bornitude ponctuelle :** Pour $t \in [0, T]$, la condition initiale impose $y_n(0) = 0$. Donc $|y_n(t)| = |y_n(t) - y_n(0)| \le M|t - 0| \le MT$.
La famille est donc uniformément bornée, ce qui assure la condition ponctuelle exigée.

### 3. Extraction d'une sous-suite convergente

D'après le Théorème d'Arzelà-Ascoli appliqué sur le compact $[0, T]$, la famille $(y_n)$ est relativement compacte pour la norme uniforme. Il existe donc une sous-suite $(y_{\phi(n)})$ qui converge uniformément vers une fonction $y : [0, T] \to \mathbb{R}$ continue.

### 4. Validation de la solution (Passage à la limite sous le signe intégrale)

Il reste à montrer que cette fonction limite $y$ vérifie effectivement l'équation intégrale $y(t) = \int_0^t F(y(s)) ds$.
Par la construction d'Euler (ce qui demande une petite majoration technique souvent omise en licence mais cruciale) :
$$ y_n(t) = \int_0^t F(y_n(s_n)) ds + \epsilon_n(t) $$
Où $s_n$ est l'arrondi du temps sur la grille, et l'erreur d'approximation du schéma $\epsilon_n$ tend uniformément vers $0$.
Dans l'extraction, remplaçons $n$ par $\phi(n)$.
Puisque $y_{\phi(n)}$ converge uniformément vers $y$, et que $F$ est continue (donc uniformément continue sur tout compact contenant les images de $y$), la composition $F(y_{\phi(n)}(s))$ converge uniformément vers $F(y(s))$ sur $[0, T]$.
Par le théorème d'interversion de la limite et de l'intégrale (convergence uniforme sur le segment $[0, t] \subset [0, T]$), on passe à la limite sous le signe intégral :
$$ \lim_{k\to\infty} \int_0^t F(y_{\phi(k)}(s_{\phi(k)})) ds = \int_0^t F(y(s)) ds $$
Ainsi, on obtient $y(t) = \int_0^t F(y(s)) ds$.
Par le théorème fondamental de l'analyse, l'intégrande étant continue, $y$ est de classe $\mathcal{C}^1$ et $y'(t) = F(y(t))$, avec $y(0) = 0$. $\blacksquare$
