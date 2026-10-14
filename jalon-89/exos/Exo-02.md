# Exercice 2 : Événements indépendants et divergence

$\bigstar\bigstar\star\star\star$

**Énoncé :**
On lance une pièce de monnaie biaisée de telle sorte que la probabilité d'obtenir "Pile" au $n$-ième lancer soit $p_n = \frac{1}{n}$. Les lancers sont indépendants.
Montrer que l'on obtiendra "Pile" une infinité de fois presque sûrement.

**Correction :**
Soit $A_n$ l'événement "Obtenir Pile au $n$-ième lancer".
Les événements $A_n$ sont mutuellement indépendants d'après l'énoncé.
La probabilité de l'événement $A_n$ est $\mathbb{P}(A_n) = \frac{1}{n}$.
Nous étudions la convergence de la série $\sum_{n=1}^\infty \mathbb{P}(A_n) = \sum_{n=1}^\infty \frac{1}{n}$.
Cette série est la série harmonique. Or, la série harmonique diverge vers $+\infty$.
$$ \sum_{n=1}^\infty \mathbb{P}(A_n) = +\infty $$
Étant donné que les événements $A_n$ sont indépendants et que la somme de leurs probabilités diverge, le second lemme de Borel-Cantelli s'applique.
On en conclut que :
$$ \mathbb{P}(\limsup_{n \to \infty} A_n) = 1 $$
Par conséquent, on obtient "Pile" une infinité de fois presque sûrement.
