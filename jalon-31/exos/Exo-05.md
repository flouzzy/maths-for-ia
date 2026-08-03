# Nilpotence et trace (⭐⭐⭐)

## Énoncé
Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension $n$. Soit $u \in \mathcal{L}(E)$.
On suppose que $\mathbb{K}$ est un corps de caractéristique nulle (ex: $\mathbb{R}$ ou $\mathbb{C}$).
1. Si $u$ est nilpotent, montrer que pour tout entier $k \ge 1$, $\text{Tr}(u^k) = 0$.
2. (Réciproque partielle) On suppose que pour tout $k \in \{1, 2, \dots, n\}$, $\text{Tr}(u^k) = 0$. En utilisant les identités de Newton (admises), montrer que $u$ est nilpotent.

## Corrigé Détaillé

### 1. Condition nécessaire
Si $u$ est nilpotent, alors son polynôme caractéristique est $\chi_u(X) = X^n$ (Théorème vu en cours).
Cela signifie que dans la clôture algébrique de $\mathbb{K}$ (ou dans $\mathbb{C}$ si on travaille sur $\mathbb{R}$), toutes les valeurs propres de $u$ sont nulles.
$u$ est trigonalisable dans $\mathbb{C}$, donc il existe une base dans laquelle sa matrice $T$ est triangulaire supérieure avec des zéros sur la diagonale.
Pour tout entier $k \ge 1$, la matrice $T^k$ est également triangulaire supérieure, et ses éléments diagonaux sont les éléments diagonaux de $T$ élevés à la puissance $k$, donc des zéros.
La trace étant invariante par changement de base et égale à la somme des éléments diagonaux de $T^k$, on a $\text{Tr}(u^k) = 0$ pour tout $k \ge 1$.

### 2. Condition suffisante via Newton
Soient $\lambda_1, \lambda_2, \dots, \lambda_n$ les racines complexes (valeurs propres) du polynôme caractéristique de $u$, répétées avec leur multiplicité.
On sait que $\text{Tr}(u^k) = \sum_{i=1}^n \lambda_i^k$.
Par hypothèse, $S_k = \sum_{i=1}^n \lambda_i^k = 0$ pour tout $k \in \{1, \dots, n\}$.
Considérons le polynôme caractéristique factorisé :
$\chi_u(X) = X^n - e_1 X^{n-1} + e_2 X^{n-2} - \dots + (-1)^n e_n$
où les $e_k$ sont les fonctions symétriques élémentaires des racines.
Les identités de Newton relient les sommes de puissances $S_k$ aux $e_k$ par la relation récursive (pour $k \le n$) :
$k e_k = \sum_{i=1}^k (-1)^{i-1} e_{k-i} S_i \quad (\text{avec } e_0 = 1)$
Appliquons ceci itérativement :
- Pour $k=1$ : $1 e_1 = S_1$. Puisque $S_1 = 0$, on a $e_1 = 0$.
- Pour $k=2$ : $2 e_2 = e_1 S_1 - S_2 = 0 \times 0 - 0 = 0$. Comme la caractéristique du corps est nulle, $2 \neq 0$, donc $e_2 = 0$.
- Par récurrence forte, si $e_1 = e_2 = \dots = e_{k-1} = 0$,
  alors $k e_k = S_k - e_1 S_{k-1} + \dots = 0$.
  La division par $k$ (possible en caractéristique nulle) donne $e_k = 0$.
Ainsi, pour tout $k \in \{1, \dots, n\}$, $e_k = 0$.
Le polynôme caractéristique de $u$ est donc simplement :
$\chi_u(X) = X^n$
D'après le théorème de Cayley-Hamilton, $u^n = \chi_u(u) = 0_{\mathcal{L}(E)}$.
L'endomorphisme $u$ est donc nilpotent.
