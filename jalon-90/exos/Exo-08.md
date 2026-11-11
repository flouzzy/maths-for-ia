# Exercice 08

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Convergence $L^p$ et intégrabilité de la limite

Supposons que $X_n \xrightarrow{L^p} X$ pour $p \ge 1$.
Démontrez de façon complète que la fonction limite $X$ appartient nécessairement à $L^p$, en utilisant la stricte inégalité de Minkowski.

**Correction exhaustive :**
Par hypothèse, pour tout $n$, $X_n \in L^p$, c'est-à-dire $\mathbb{E}[|X_n|^p] < \infty$.
La condition $X_n \xrightarrow{L^p} X$ signifie que la quantité $\mathbb{E}[|X_n - X|^p]$ (la puissance $p$-ème de la norme $\|X_n - X\|_p$) tend vers $0$ lorsque $n \to \infty$.
Ceci implique en particulier qu'il existe un rang $N$ à partir duquel cette quantité est finie. Ainsi, $\|X_n - X\|_p < \infty$ pour $n \ge N$.
Considérons la norme dans l'espace $L^p$ définie par $\|Z\|_p = (\mathbb{E}[|Z|^p])^{1/p}$.
La variable aléatoire $X$ peut s'écrire artificiellement comme une somme télescopique :
$$ X = (X - X_N) + X_N $$
Prenons la norme $L^p$ de cette somme. L'inégalité de Minkowski, qui exprime la sous-additivité de la norme, affirme que :
$$ \|X\|_p = \|(X - X_N) + X_N\|_p \le \|X - X_N\|_p + \|X_N\|_p $$
Puisque la norme est symétrique (absolue), $\|X - X_N\|_p = \|X_N - X\|_p$.
Par hypothèse, nous savons que $\|X_N - X\|_p < \infty$ puisque la limite tend vers 0.
De plus, $X_N \in L^p$ garantit que $\|X_N\|_p < \infty$.
La somme de deux nombres réels finis étant finie, nous en déduisons :
$$ \|X\|_p < \infty $$
L'élévation à la puissance $p$ conserve la finitude (puisque $p \ge 1$) :
$$ \mathbb{E}[|X|^p] = (\|X\|_p)^p < \infty $$
Nous avons ainsi démontré que l'espace vectoriel d'arrivée n'a pas été fracturé : la limite de la convergence en norme $L^p$ reste strictement emprisonnée dans la classe des fonctions $L^p$ intégrables.
