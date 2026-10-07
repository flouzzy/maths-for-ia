# Exercice 7 : Fonction créneau et distribution peigne  \quad $\bigstar\bigstar\bigstar\bigstar\star$


## Énoncé
Soit $f$ la fonction créneau périodique de période $2\pi$, définie sur $]-\pi, \pi]$ par :
$$
f(x) = \begin{cases}
1 & \text{si } 0 < x \le \pi \\
-1 & \text{si } -\pi < x \le 0
\end{cases}
$$
Calculer la dérivée de $f$ au sens des distributions sur $\mathbb{R}$.

## Correction
La fonction $f$ est une fonction constante par morceaux sur $\mathbb{R}$.
Sa dérivée usuelle $\{f'\}$ est nulle partout où elle est définie (c'est-à-dire sur $\mathbb{R} \setminus \{k\pi\}_{k \in \mathbb{Z}}$).
Étudions les sauts de $f$. La fonction présente une discontinuité en chaque point $x_k = k\pi$.
- Pour $k = 0$ : saut entre $-\pi$ et $\pi$. En $0^+$, $f$ vaut 1. En $0^-$, $f$ vaut -1. Saut $\sigma_0 = 1 - (-1) = 2$.
- Pour $k = 1$ (point $\pi$) : en $\pi^+$, on passe dans le créneau $[-1]$ de la période suivante, donc $f(\pi^+) = -1$. En $\pi^-$, $f$ vaut 1. Saut $\sigma_1 = -1 - 1 = -2$.
- Pour $k = 2$ (point $2\pi$) : en $(2\pi)^+$, $f$ vaut 1. En $(2\pi)^-$, $f$ vaut -1. Saut $\sigma_2 = 1 - (-1) = 2$.

De manière générale, le saut au point $k\pi$ vaut :
- $\sigma_k = 2$ si $k$ est pair (les sauts montants).
- $\sigma_k = -2$ si $k$ est impair (les sauts descendants).
On peut écrire $\sigma_k = 2(-1)^k$.

Par la formule des sauts :
$$ f' = \{f'\} + \sum_{k \in \mathbb{Z}} \sigma_k \delta_{k\pi} $$
Puisque $\{f'\} = 0$, on obtient :
$$ f' = \sum_{k \in \mathbb{Z}} 2(-1)^k \delta_{k\pi} $$
La dérivée est une série de masses de Dirac, alternant positivement et négativement aux multiples de $\pi$. C'est une distribution apparentée au peigne de Dirac.
