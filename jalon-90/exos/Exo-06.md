# Exercice 6 : Convergence p.s. et lemme de Borel-Cantelli

Niveau : $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires indépendantes suivant la loi de Bernoulli de paramètre $p_n = \frac{1}{n^2}$ pour $n \ge 1$.
Montrer en utilisant le lemme de Borel-Cantelli que $X_n \xrightarrow{\text{p.s.}} 0$.

## Correction

Pour montrer que $X_n \xrightarrow{\text{p.s.}} 0$, on fixe un $\varepsilon > 0$.
Il s'agit de prouver que la probabilité que l'événement $A_n = \{ |X_n - 0| > \varepsilon \}$ se réalise une infinité de fois est nulle.
Comme $X_n \in \{0, 1\}$, si l'on prend $\varepsilon \in ]0, 1[$, l'événement $A_n$ équivaut à $\{X_n = 1\}$.
Évaluons la probabilité de $A_n$ :
$$\mathbb{P}(A_n) = \mathbb{P}(X_n = 1) = p_n = \frac{1}{n^2}$$
Considérons la série de terme général $\mathbb{P}(A_n)$ :
$$\sum_{n=1}^{+\infty} \mathbb{P}(A_n) = \sum_{n=1}^{+\infty} \frac{1}{n^2}$$
Il s'agit d'une série de Riemann convergente (exposant $2 > 1$).
Donc $\sum \mathbb{P}(A_n) < +\infty$.
D'après le premier lemme de Borel-Cantelli, si la série des probabilités converge, alors la probabilité que la limite supérieure des $A_n$ (le fait qu'une infinité de $A_n$ se réalisent) est nulle :
$$\mathbb{P}(\limsup_{n \to \infty} A_n) = 0$$
Cela signifie que presque sûrement, l'événement $\{X_n = 1\}$ ne se produit qu'un nombre fini de fois.
Donc, presque sûrement, il existe un rang $N$ à partir duquel $X_n = 0$.
Ainsi, la suite $(X_n(\omega))$ est stationnaire en $0$ à partir d'un certain rang, presque sûrement.
On en conclut que $X_n \xrightarrow{\text{p.s.}} 0$.
