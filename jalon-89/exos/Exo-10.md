# Exercice 10 : Distance entre points aléatoires sur un cercle

$\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(P_n)$ une suite de points tirés indépendamment et uniformément sur un cercle de périmètre 1.
Quelle est la probabilité que la distance entre $P_n$ et un point fixe $P_0$ soit inférieure à $1/n$ pour une infinité d'indices $n$ ?

**Correction :**
Soit $d(P_n, P_0)$ la distance sur le cercle (qui correspond à la longueur de l'arc le plus court entre les deux points).
La distance maximale possible sur le cercle de périmètre 1 est $1/2$.
Soit l'événement $A_n = \{ d(P_n, P_0) \le 1/n \}$.
Pour un $n \ge 2$, l'ensemble des points à une distance inférieure à $1/n$ de $P_0$ correspond à un arc de cercle centré en $P_0$ de longueur $2/n$.
Puisque $P_n$ est tiré uniformément, la probabilité que $P_n$ tombe dans cet arc est le rapport de la longueur de l'arc sur le périmètre total :
$$ \mathbb{P}(A_n) = \frac{2/n}{1} = \frac{2}{n} $$
Les tirages des $P_n$ étant indépendants, les événements $A_n$ sont mutuellement indépendants.
Nous étudions la série $\sum_{n=2}^\infty \mathbb{P}(A_n) = \sum_{n=2}^\infty \frac{2}{n} = 2 \sum_{n=2}^\infty \frac{1}{n}$.
Cette série est la série harmonique, qui diverge :
$$ \sum_{n=2}^\infty \mathbb{P}(A_n) = +\infty $$
D'après le second lemme de Borel-Cantelli, l'événement $\limsup A_n$ est presque certain :
$$ \mathbb{P}(\limsup A_n) = 1 $$
Ainsi, avec une probabilité de 1, la distance entre $P_n$ et $P_0$ sera inférieure à $1/n$ pour une infinité d'indices $n$.
