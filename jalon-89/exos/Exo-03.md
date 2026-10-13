# Exercice 3

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Le paradoxe du singe savant revisité

Considérons un alphabet de $L$ lettres. Un singe frappe aléatoirement sur un clavier, les frappes étant indépendantes et chaque lettre ayant la probabilité $\frac{1}{L}$.
Soit un mot $M$ fixé de longueur $k$. On note $A_n$ l'événement : "le mot $M$ est tapé entre la frappe $n \cdot k$ et $(n+1) \cdot k - 1$".
Montrer que presque sûrement, le singe tapera le mot $M$ une infinité de fois.

**Correction détaillée :**
1. Un bloc de frappe allant de $n \cdot k$ à $(n+1) \cdot k - 1$ comprend exactement $k$ caractères consécutifs. La probabilité que ces $k$ caractères correspondent exactement aux $k$ caractères du mot $M$ est $p = \left(\frac{1}{L}\right)^k > 0$.
2. Puisque les événements $A_n$ concernent des blocs de caractères disjoints et que les frappes sont indépendantes, les événements $A_n$ sont mutuellement indépendants.
3. On calcule la somme de leurs probabilités : $\sum_{n=1}^{\infty} \mathbb{P}(A_n) = \sum_{n=1}^{\infty} p$.
4. Puisque $p$ est une constante strictement positive, cette série géométrique dont le terme général ne tend pas vers zéro diverge nécessairement vers $+\infty$.
5. D'après le second lemme de Borel-Cantelli, l'indépendance des $A_n$ et la divergence de la série impliquent que $\mathbb{P}(\limsup_{n \to \infty} A_n) = 1$.
6. Le mot $M$ sera donc tapé une infinité de fois avec une probabilité égale à 1.
