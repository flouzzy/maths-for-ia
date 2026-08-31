## Exercice 5 : Somme double de termes positifs \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(a_{i,j})_{i,j \ge 0}$ une suite double de réels positifs. Démontrer, en utilisant la mesure de comptage sur $\mathbb{N}$ et le corollaire du TCM, que $\sum_{i=0}^\infty \sum_{j=0}^\infty a_{i,j} = \sum_{j=0}^\infty \sum_{i=0}^\infty a_{i,j}$.

**Correction Détaillée :**
1. On munit $\mathbb{N}$ de la tribu de l'ensemble de ses parties et de la mesure de comptage $\mu$. L'intégrale par rapport à $\mu$ d'une fonction positive $f$ est $\int_{\mathbb{N}} f d\mu = \sum_{k=0}^\infty f(k)$.
2. Posons la fonction $u_j : \mathbb{N} \to [0, +\infty]$ définie par $u_j(i) = a_{i,j}$.
3. La série $\sum_{j=0}^\infty u_j$ est une série de fonctions mesurables positives sur $\mathbb{N}$.
4. D'après le corollaire du TCM (sommation terme à terme) :
   $\int_{\mathbb{N}} (\sum_{j=0}^\infty u_j(i)) d\mu(i) = \sum_{j=0}^\infty \int_{\mathbb{N}} u_j(i) d\mu(i)$.
5. Explicitons les intégrales comme des sommes :
   Le membre de gauche est $\sum_{i=0}^\infty \left( \sum_{j=0}^\infty a_{i,j} \right)$.
   Le membre de droite est $\sum_{j=0}^\infty \left( \sum_{i=0}^\infty a_{i,j} \right)$.
6. L'égalité est donc démontrée : l'interversion des sommes est toujours licite pour des termes positifs.
