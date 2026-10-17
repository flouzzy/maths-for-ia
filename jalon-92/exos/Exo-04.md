# Exercice 4 : Estimation d'une intégrale par méthode de Monte-Carlo \quad $\bigstar\bigstar\bigstar\star\star$

## Énoncé
On souhaite estimer l'intégrale $I = \int_0^{\pi/2} \sin(x) dx$.
1. Exprimer $I$ sous la forme d'une espérance mathématique $\mathbb{E}[f(U)]$ où $U$ suit une loi uniforme sur $[0, \pi/2]$.
2. Proposer un estimateur $\hat{I}_n$ basé sur $n$ tirages i.i.d. et justifier sa convergence presque sûre vers $I$.

## Correction Détaillée
### 1. Expression sous forme d'espérance
La densité d'une variable $U$ suivant une loi uniforme sur $[0, \pi/2]$ est $p(x) = \frac{1}{\pi/2 - 0} = \frac{2}{\pi}$ pour $x \in [0, \pi/2]$ et $0$ sinon.
On peut écrire $I$ en introduisant cette densité :
$$ I = \int_0^{\pi/2} \sin(x) dx = \int_0^{\pi/2} \left( \sin(x) \frac{\pi}{2} \right) \frac{2}{\pi} dx $$
Ainsi, si $f(x) = \frac{\pi}{2} \sin(x)$, alors :
$$ I = \int_0^{\pi/2} f(x) p(x) dx = \mathbb{E}[f(U)] = \mathbb{E}\left[ \frac{\pi}{2} \sin(U) \right] $$

### 2. Estimateur et convergence
On génère une suite $(U_n)_{n \ge 1}$ de variables aléatoires i.i.d. de loi uniforme sur $[0, \pi/2]$.
On pose $X_i = \frac{\pi}{2} \sin(U_i)$. Les $X_i$ sont i.i.d.
L'intégrabilité de $X_1$ est immédiate car $X_1$ est bornée (comprise entre $0$ et $\pi/2$). Donc $\mathbb{E}[|X_1|] < +\infty$.
L'estimateur naturel est la moyenne empirique :
$$ \hat{I}_n = \frac{1}{n} \sum_{i=1}^n X_i = \frac{1}{n} \sum_{i=1}^n \frac{\pi}{2} \sin(U_i) $$
Par la Loi Forte des Grands Nombres de Kolmogorov, puisque $\mathbb{E}[|X_1|] < \infty$, la moyenne empirique converge presque sûrement vers son espérance théorique :
$$ \hat{I}_n \xrightarrow{p.s.} \mathbb{E}[X_1] = I $$
Ainsi, $\hat{I}_n$ est un estimateur fortement convergent de l'intégrale $I$. $\blacksquare$
