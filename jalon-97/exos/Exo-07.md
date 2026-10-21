# Exercice 7 : L'inverse d'un opérateur proche de l'identité
$\bigstar$\bigstar$\bigstar$\bigstar\star$

**Énoncé :**
Soit $E$ un espace de Banach et $T \in \mathcal{L}(E)$ tel que $\|T\| < 1$. Montrer que l'opérateur $I - T$ est inversible (série de Neumann).

**Correction Détaillée :**
1. Considérons la série $S_n = \sum_{k=0}^n T^k$. Montrons qu'elle converge dans $\mathcal{L}(E)$.
2. $\|T^k\| \le \|T\|^k$. Comme $\|T\| < 1$, la série numérique $\sum \|T\|^k$ converge (série géométrique).
3. L'espace $\mathcal{L}(E)$ étant complet (car $E$ est un Banach), la série $\sum T^k$ converge absolument, donc converge vers un opérateur $S$.
4. On vérifie que $(I-T)S = S(I-T) = \sum_{k=0}^\infty T^k - \sum_{k=1}^\infty T^k = T^0 = I$. Ainsi $I-T$ est inversible.
