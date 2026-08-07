# Exercice 10 : Topologie de l'ordre \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Soit $X$ un ensemble totalement ordonné muni d'une relation d'ordre strict $<$. On définit la base de la topologie de l'ordre par les intervalles ouverts $]a, b[ = \{x \in X \mid a < x < b\}$, les demi-droites ouvertes $]-\infty, a[$ et $]a, +\infty[$. Montrer que l'intersection finie de ces ouverts de base reste un ouvert de base ou est vide.

\textbf{Correction exhaustive :}
Une base de topologie engendre une topologie par réunions quelconques de ses éléments. Pour que ce soit valide, il faut que l'intersection de deux ouverts de base s'écrive comme union d'ouverts de base (ou soit vide). Montrons ici qu'elle est en fait un seul ouvert de base ou vide.
Soient $I_1$ et $I_2$ deux éléments de la base.
Prenons le cas général de deux intervalles ouverts $I_1 = ]a, b[$ et $I_2 = ]c, d[$.
Leur intersection est $\{x \in X \mid (a < x < b) \text{ et } (c < x < d)\}$.
Puisque l'ordre est total, l'ensemble $\{a, c\}$ a un plus grand élément, notons le $\max(a,c)$. De même l'ensemble $\{b, d\}$ a un plus petit élément, notons le $\min(b,d)$.
L'intersection devient $\{x \in X \mid \max(a,c) < x < \min(b,d)\}$.
Si $\max(a,c) < \min(b,d)$, cet ensemble est exactement l'intervalle ouvert $]\max(a,c), \min(b,d)[$, qui est un ouvert de base.
Sinon, l'intersection est vide $\emptyset$.
Ce raisonnement s'étend de la même manière si $I_1$ ou $I_2$ est une demi-droite, en considérant que $-\infty$ est toujours inférieur à n'importe quel élément et $+\infty$ toujours supérieur. L'intersection finie reste donc toujours dans la famille des ouverts de base ou l'ensemble vide, assurant ainsi que l'axiome d'intersection finie de la topologie engendrée sera vérifié.
