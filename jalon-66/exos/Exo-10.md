# Exercice 10 : Lemme de Borel-Cantelli (Partie directe)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'ensembles mesurables dans $(X, \mathcal{A}, \mu)$. Démontrer que si la série des mesures est convergente ($\sum_{n=1}^\infty \mu(A_n) < +\infty$), alors la mesure de la limite supérieure est nulle : $\mu(\limsup A_n) = 0$.

**Démonstration :**
Le lemme de Borel-Cantelli est le socle des lois fortes en probabilités.
La limite supérieure d'une suite d'ensembles est définie par :
$$A = \limsup_{n \to \infty} A_n = \bigcap_{k=1}^\infty \bigcup_{n=k}^\infty A_n$$
Cet ensemble représente les points qui appartiennent à une infinité d'ensembles $A_n$.
Posons la suite d'ensembles $B_k = \bigcup_{n=k}^\infty A_n$.
Par construction, la suite $(B_k)$ est une suite d'ensembles décroissante pour l'inclusion : $B_{k+1} \subseteq B_k$.
En effet, on retire l'ensemble $A_k$ de l'union infinie.
Leur intersection est exactement l'ensemble limite supérieure : $A = \bigcap_{k=1}^\infty B_k$.
Évaluons la mesure de $B_k$. Par sous-additivité dénombrable de la mesure $\mu$, l'union de ces ensembles satisfait :
$$\mu(B_k) = \mu\left(\bigcup_{n=k}^\infty A_n\right) \leq \sum_{n=k}^\infty \mu(A_n)$$
Par hypothèse fondamentale, la série entière des mesures converge, c'est-à-dire que $\sum_{n=1}^\infty \mu(A_n) = S < +\infty$.
Le reste d'une série convergente tend nécessairement vers zéro. Le terme de droite est précisément le reste de cette série à partir du rang $k$.
Ainsi, lorsque $k \to \infty$ :
$$\lim_{k \to \infty} \sum_{n=k}^\infty \mu(A_n) = 0$$
Par conséquent, la limite de $\mu(B_k)$ lorsque $k \to \infty$ est égale à $0$.
Puisque la suite $B_k$ est décroissante et que la mesure de son premier terme $B_1$ est finie (majorée par la somme de la série, qui est finie), nous pouvons appliquer le théorème de continuité monotone décroissante de la mesure.
La mesure de l'intersection est la limite des mesures :
$$\mu(A) = \mu\left(\bigcap_{k=1}^\infty B_k\right) = \lim_{k \to \infty} \mu(B_k) \leq 0$$
Puisque la mesure est positive, $\mu(A) = 0$.
