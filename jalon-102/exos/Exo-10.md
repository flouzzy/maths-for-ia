$\bigstar\bigstar\bigstar\bigstar\bigstar$
**Énoncé :** Convergence faible et condition de Cauchy.
Montrer que dans l'espace $\ell^1$, toute suite faiblement convergente est fortement convergente (propriété de Schur). On admettra que si une suite converge faiblement vers 0 dans $\ell^1$, mais pas fortement, on peut construire par extraction une "suite basique" équivalente à la base canonique, conduisant à une contradiction.

**Correction Détaillée :**
Cet exercice demande de prouver un cas remarquable où la topologie faible se comporte comme la forte pour les suites.
Soit $(x_n)$ une suite de $\ell^1$ convergeant faiblement vers 0. Supposons par l'absurde qu'elle ne converge pas fortement vers 0.
Il existe alors $\epsilon > 0$ et une sous-suite (toujours notée $x_n$) telle que $\|x_n\|_1 \ge \epsilon$ pour tout $n$.
En utilisant une technique de "glissement de bosse" (sliding hump argument), on peut extraire une sous-suite $(y_k) = (x_{n_k})$ telle que les supports de $y_k$ (les indices où les coefficients sont non nuls) soient presque disjoints.
Plus précisément, on peut approcher chaque $y_k$ par un vecteur $z_k$ à support fini $S_k$, tel que les $S_k$ soient deux à deux disjoints, et $\|y_k - z_k\|_1 \le \epsilon/4$.
Soit $L \in (\ell^1)^* \cong \ell^\infty$ défini par $L_j = \text{sign}(z_{k, j})$ pour $j \in S_k$, et $0$ ailleurs. $L$ est bien bornée par 1.
Évaluons $L(y_k)$ :
$L(y_k) = L(z_k) + L(y_k - z_k) = \sum_{j \in S_k} |z_{k, j}| + L(y_k - z_k) = \|z_k\|_1 + L(y_k - z_k)$.
On a $\|z_k\|_1 \ge \|y_k\|_1 - \|y_k - z_k\|_1 \ge \epsilon - \epsilon/4 = 3\epsilon/4$.
Et $|L(y_k - z_k)| \le \|L\|_\infty \|y_k - z_k\|_1 \le 1 \cdot \epsilon/4$.
Donc $L(y_k) \ge 3\epsilon/4 - \epsilon/4 = \epsilon/2$.
Mais comme $y_k \rightharpoonup 0$ faiblement, on doit avoir $L(y_k) \to 0$. Contradiction !
La prémisse était fausse, la suite doit donc converger fortement. C'est la propriété de Schur de l'espace $\ell^1$.
