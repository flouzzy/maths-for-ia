## Exercice 1 : La tribu grossière et discrète \quad $\bigstar\star\star\star\star$


\textbf{Énoncé :}
Soit $X$ un ensemble. Démontrer que l'intersection de toutes les tribus sur $X$ est la tribu grossière $\{\emptyset, X\}$, et que l'union de toutes les tribus n'est pas nécessairement une tribu, mais que la tribu des parties $\mathcal{P}(X)$ est la plus grande.

\textbf{Correction exhaustive pas-à-pas :}
1. Soit $\mathfrak{F}$ l'ensemble de toutes les tribus sur $X$. Par définition, pour toute tribu $\mathcal{F} \in \mathfrak{F}$, on a $\emptyset \in \mathcal{F}$ et $X \in \mathcal{F}$.
2. Par conséquent, $\{\emptyset, X\} \subset \bigcap_{\mathcal{F} \in \mathfrak{F}} \mathcal{F}$.
3. De plus, $\mathcal{F}_0 = \{\emptyset, X\}$ est elle-même une tribu sur $X$, donc elle appartient à $\mathfrak{F}$. L'intersection est donc contenue dans $\mathcal{F}_0$.
4. Ainsi, $\bigcap_{\mathcal{F} \in \mathfrak{F}} \mathcal{F} = \{\emptyset, X\}$.
5. Pour l'union : soient $\mathcal{F}_1 = \{\emptyset, \{1\}, \{2, 3\}, \{1, 2, 3\}\}$ et $\mathcal{F}_2 = \{\emptyset, \{2\}, \{1, 3\}, \{1, 2, 3\}\}$ sur $X=\{1, 2, 3\}$. $\mathcal{F}_1 \cup \mathcal{F}_2$ contient $\{1\}$ et $\{2\}$, mais pas leur union $\{1, 2\}$. Donc l'union de tribus n'est pas une tribu.
