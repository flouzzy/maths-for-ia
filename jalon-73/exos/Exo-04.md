# Exercice 4 : Classe d'équivalence de la fonction indicatrice de $\mathbb{Q}$ \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Sur l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, soit $f = 1_{\mathbb{Q}}$ la fonction indicatrice des rationnels.
Déterminer la classe d'équivalence de $f$ dans $L^p(\lambda)$ (pour $1 \le p \le +\infty$).

**Correction :**
La fonction $f$ vaut 1 sur $\mathbb{Q}$ et 0 sur $\mathbb{R} \setminus \mathbb{Q}$.
L'ensemble des rationnels $\mathbb{Q}$ est dénombrable.
Or, la mesure de Lebesgue d'un ensemble dénombrable est nulle : $\lambda(\mathbb{Q}) = 0$.
Par conséquent, l'ensemble sur lequel $f$ est non nulle, $A = \{x \in \mathbb{R} \mid f(x) \neq 0\} = \mathbb{Q}$, est de mesure nulle.
Cela signifie que $f(x) = 0$ pour presque tout $x \in \mathbb{R}$.
Donc $f \sim 0$.
La classe d'équivalence de $f$ dans $L^p(\lambda)$ est la classe de la fonction nulle, c'est-à-dire $[0]$.
