### Exercice 9 : Inégalité de Jensen pour les espérances conditionnelles $\bigstar\bigstar\star\star$

**Énoncé :** Soit $X$ une variable aléatoire dans $L^1(\Omega, \mathcal{A}, P)$ et $\mathcal{B}$ une sous-tribu de $\mathcal{A}$. Soit $\phi$ une fonction convexe telle que $\phi(X) \in L^1$. Montrer que $\phi(\mathbb{E}[X|\mathcal{B}]) \le \mathbb{E}[\phi(X)|\mathcal{B}]$ presque sûrement.

**Correction Détaillée :**
*Analyse :* C'est une application directe de la définition par les droites d'appui de la convexité (sous-gradients), combinée à la monotonie de l'espérance conditionnelle.
*Résolution pas-à-pas :*
1. Toute fonction convexe $\phi$ sur $\mathbb{R}$ peut s'écrire comme l'enveloppe supérieure d'une famille dénombrable de fonctions affines : $\phi(x) = \sup_{n \in \mathbb{N}} (a_n x + b_n)$.
2. Pour tout $n$, $\phi(X) \ge a_n X + b_n$ presque sûrement.
3. Par croissance de l'espérance conditionnelle (qui préserve l'inégalité presque sûrement) :
   $$\mathbb{E}[\phi(X) | \mathcal{B}] \ge \mathbb{E}[a_n X + b_n | \mathcal{B}] = a_n \mathbb{E}[X | \mathcal{B}] + b_n \quad p.s.$$
4. Cette inégalité est vraie $P$-p.s. pour chaque $n$. Une union dénombrable d'ensembles négligeables étant négligeable, elle est vraie $P$-p.s. simultanément pour tous les $n \in \mathbb{N}$.
5. Sur cet événement de probabilité 1, on peut prendre le supremum sur $n$ du membre de droite :
   $$\mathbb{E}[\phi(X) | \mathcal{B}] \ge \sup_{n \in \mathbb{N}} (a_n \mathbb{E}[X | \mathcal{B}] + b_n) = \phi(\mathbb{E}[X | \mathcal{B}])$$
6. Ce qui termine la démonstration.
