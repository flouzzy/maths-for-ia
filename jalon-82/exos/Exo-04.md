\subsection*{Exercice 4 : Support d'une distribution \quad $\bigstar\bigstar\bigstar\star\star$}

**Énoncé :**
Déterminer le support de la distribution $T = \delta_2 + \delta_5$.

**Correction :**
Le support d'une distribution $T$, noté $\text{supp}(T)$, est le complémentaire du plus grand ouvert $O$ sur lequel $T$ est nulle. Une distribution est nulle sur un ouvert $O$ si et seulement si pour toute fonction test $\phi$ dont le support est inclus dans $O$, $\langle T, \phi \rangle = 0$.
Soit $\phi \in \mathcal{D}(\mathbb{R})$. On a $\langle T, \phi \rangle = \phi(2) + \phi(5)$.
Si le support de $\phi$ ne contient ni $2$ ni $5$, alors $\phi(2) = 0$ et $\phi(5) = 0$, donc $\langle T, \phi \rangle = 0$.
Ainsi, $T$ est nulle sur tout ouvert ne contenant pas $\{2, 5\}$, par exemple $\mathbb{R} \setminus \{2, 5\}$. Le plus grand ouvert sur lequel $T$ est nulle est donc $\mathbb{R} \setminus \{2, 5\}$.
Le support est le complémentaire de cet ouvert, c'est-à-dire le fermé $\{2, 5\}$.
$\text{supp}(T) = \{2, 5\}$.
