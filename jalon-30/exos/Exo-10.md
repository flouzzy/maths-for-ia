# Exercice 10 : Preuve de l'appartenance à $\mathbb{K}[f]$ (★★★★★)

Démontrer la seconde partie du théorème de Dunford : si $f = d + n$ est la décomposition de Dunford, alors $d$ et $n$ sont des polynômes en $f$.
*Indication : Utiliser le lemme des noyaux, les projecteurs spectraux associés aux sous-espaces caractéristiques, et le théorème des restes chinois (ou l'interpolation de Lagrange).*

### Solution :

Cette démonstration est le summum de l'exégèse conceptuelle de ce jalon.
Soit $\chi_f(X) = \prod_{i=1}^k (X - \lambda_i)^{\alpha_i}$ le polynôme caractéristique de $f$, scindé sur $\mathbb{K}$ par hypothèse. (Les $\lambda_i$ sont distincts).
Par le lemme des noyaux, appliqué aux polynômes premiers entre eux deux à deux $P_i(X) = (X - \lambda_i)^{\alpha_i}$, l'espace vectoriel $E$ se décompose en somme directe des sous-espaces caractéristiques :
$$ E = \bigoplus_{i=1}^k \ker((f - \lambda_i \text{Id}_E)^{\alpha_i}) = \bigoplus_{i=1}^k E_i $$

Soit $\pi_i$ la projection vectorielle sur $E_i$ parallèlement à la somme des autres $E_j$.
Le point clé, issu du théorème de Bézout généralisé pour les projecteurs, est que **chaque projecteur spectral $\pi_i$ est un polynôme en $f$**.
En effet, soit $Q_i(X) = \prod_{j \neq i} (X - \lambda_j)^{\alpha_j}$. Les $Q_i$ sont globalement premiers entre eux. Il existe des polynômes $U_i$ tels que $\sum U_i Q_i = 1$.
En évaluant en $f$, on obtient $\text{Id}_E = \sum U_i(f) Q_i(f)$. On démontre que $\pi_i = U_i(f) Q_i(f)$, qui est bien un polynôme en $f$.

Maintenant, construisons l'endomorphisme $d$.
Sur chaque sous-espace caractéristique $E_i$, $d$ doit agir comme l'homothétie de rapport $\lambda_i$ (pour que la différence $f-d$ y soit nilpotente de l'indice approprié).
Donc, $\forall x \in E_i, d(x) = \lambda_i x$.
Puisque tout vecteur $x \in E$ se décompose de manière unique en $x = \sum x_i$ avec $x_i \in E_i$ et $x_i = \pi_i(x)$, on a :
$$ d(x) = \sum_{i=1}^k d(x_i) = \sum_{i=1}^k \lambda_i x_i = \sum_{i=1}^k \lambda_i \pi_i(x) $$
Ainsi, $d = \sum_{i=1}^k \lambda_i \pi_i$.

Comme nous avons établi que chaque projecteur $\pi_i$ est un polynôme en $f$, une combinaison linéaire de ces projecteurs est également un polynôme en $f$.
Donc $d \in \mathbb{K}[f]$.
Il existe $P \in \mathbb{K}[X]$ tel que $d = P(f)$.

La partie nilpotente est définie par $n = f - d$.
Puisque l'identité (représentée par le polynôme $X$) et $d$ (représentée par $P(X)$) sont des polynômes en $f$, leur différence l'est aussi.
Donc $n = (X - P)(f)$, ce qui montre que $n$ est également un polynôme en $f$.

C'est cette appartenance à $\mathbb{K}[f]$ qui force la commutation ($d \circ n = n \circ d$, et la commutation avec tout endomorphisme commutant avec $f$), donnant à la décomposition de Dunford son incroyable puissance de calculabilité. L'ellipse n'a plus sa place ici, l'architecture algébrique est totale.
