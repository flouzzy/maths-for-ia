# Exercice 7 : Densité et convergence

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $(f_n)_{n\in\mathbb{N}}$ une suite de fonctions réelles, équicontinues sur $[0, 1]$.
On suppose de plus qu'il existe une partie dénombrable dense $D \subset [0, 1]$ telle que pour tout $x \in D$, la suite numérique $(f_n(x))$ converge.
Montrer que la suite $(f_n)$ converge uniformément sur tout l'intervalle $[0, 1]$.

*Indice : Ce résultat est l'étape finale de la démonstration constructive du théorème d'Arzelà-Ascoli.*

## Résolution Détaillée

Pour montrer la convergence uniforme, nous allons montrer que $(f_n)$ est une suite de Cauchy pour la norme uniforme. Comme l'espace des fonctions continues sur un compact à valeurs dans $\mathbb{R}$ est complet (Banach), cela prouvera la convergence uniforme.

Fixons $\epsilon > 0$.

### 1. Utilisation de l'équicontinuité

Puisque la suite $(f_n)$ est équicontinue sur le compact $[0, 1]$, elle est uniformément équicontinue (théorème de Heine généralisé).
Il existe donc $\delta > 0$ tel que :
$$ \forall n \in \mathbb{N}, \forall x, y \in [0, 1], \quad |x - y| < \delta \implies |f_n(x) - f_n(y)| < \frac{\epsilon}{3} $$

### 2. Discrétisation par la partie dense

Le segment $[0, 1]$ est compact. Les boules ouvertes $B(y, \delta)$ pour $y \in [0, 1]$ en forment un recouvrement. De ce recouvrement, on peut extraire un sous-recouvrement fini. Mieux encore, $D$ étant dense dans $[0, 1]$, on peut choisir un sous-ensemble fini $A = \{a_1, a_2, \ldots, a_K\} \subset D$ tel que $[0, 1] \subset \bigcup_{i=1}^K B(a_i, \delta)$.
Concrètement, cela signifie que pour tout $x \in [0, 1]$, il existe $a_i \in A$ tel que $|x - a_i| < \delta$.

### 3. Convergence sur l'ensemble fini

L'ensemble $A \subset D$ est fini (de cardinal $K$). Par hypothèse, pour tout $a_i \in A$, la suite $(f_n(a_i))$ converge.
La convergence d'une suite réelle implique qu'elle est de Cauchy. Donc, pour chaque $a_i$, il existe un rang $N_i$ tel que pour tous $p, q \ge N_i$, $|f_p(a_i) - f_q(a_i)| < \frac{\epsilon}{3}$.
Posons $N = \max(N_1, \ldots, N_K)$. Puisque le maximum porte sur un nombre fini d'éléments, $N$ est bien un entier défini, et pour tous $p, q \ge N$, on a :
$$ \forall i \in \{1, \ldots, K\}, \quad |f_p(a_i) - f_q(a_i)| < \frac{\epsilon}{3} $$

### 4. Recollage : La méthode des trois epsilons

Soit $x \in [0, 1]$ quelconque. Il existe $a_i \in A$ tel que $|x - a_i| < \delta$.
Soient $p, q \ge N$. Évaluons l'écart global par l'inégalité triangulaire :
$$ |f_p(x) - f_q(x)| \le |f_p(x) - f_p(a_i)| + |f_p(a_i) - f_q(a_i)| + |f_q(a_i) - f_q(x)| $$
Détaillons chaque terme :
- Par équicontinuité (car $|x - a_i| < \delta$), $|f_p(x) - f_p(a_i)| < \frac{\epsilon}{3}$.
- Par la condition de Cauchy ponctuelle au point $a_i$ (pour $p, q \ge N$), $|f_p(a_i) - f_q(a_i)| < \frac{\epsilon}{3}$.
- Par équicontinuité pour l'indice $q$, $|f_q(a_i) - f_q(x)| < \frac{\epsilon}{3}$.

En somsommant, nous obtenons pour tout $x \in [0, 1]$ et tous $p, q \ge N$ :
$$ |f_p(x) - f_q(x)| < \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon $$
Le rang $N$ ne dépendant pas de $x$, la propriété :
$$ \forall \epsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, \sup_{x \in [0, 1]} |f_p(x) - f_q(x)| \le \epsilon $$
est démontrée. La suite $(f_n)$ est donc une suite de Cauchy pour la norme uniforme sur $[0, 1]$.
L'espace $\mathcal{C}([0, 1], \mathbb{R})$ muni de $\| \cdot \|_\infty$ étant complet, la suite de Cauchy $(f_n)$ converge uniformément. $\blacksquare$
