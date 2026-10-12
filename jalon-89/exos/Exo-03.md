# Exercice 3 : Convergence presque sûre vers 0

$\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(Y_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires telles que $\mathbb{P}(|Y_n| \ge \epsilon) \le e^{-n\epsilon}$ pour tout $\epsilon > 0$.
Montrer que $Y_n$ converge presque sûrement vers 0.

**Correction :**
Rappelons que $Y_n$ converge presque sûrement vers 0 si pour tout $\epsilon > 0$, l'événement $\{|Y_n| \ge \epsilon\}$ ne se produit qu'un nombre fini de fois presque sûrement.
Fixons $\epsilon > 0$.
Posons l'événement $A_n = \{|Y_n| \ge \epsilon\}$.
D'après l'hypothèse de l'énoncé, $\mathbb{P}(A_n) \le e^{-n\epsilon}$.
Étudions la série de ces probabilités :
$$ \sum_{n=0}^\infty \mathbb{P}(A_n) \le \sum_{n=0}^\infty e^{-n\epsilon} $$
La somme à droite est une série géométrique de raison $e^{-\epsilon}$. Comme $\epsilon > 0$, on a $0 < e^{-\epsilon} < 1$, ce qui garantit la convergence de la série.
Ainsi, $\sum_{n=0}^\infty \mathbb{P}(A_n) < +\infty$.
Par le premier lemme de Borel-Cantelli, l'événement $\limsup A_n$ a une probabilité nulle.
C'est-à-dire que, presque sûrement, il n'y a qu'un nombre fini d'indices $n$ pour lesquels $|Y_n| \ge \epsilon$.
Par conséquent, pour presque tout $\omega \in \Omega$, il existe un rang $N$ tel que pour tout $n \ge N$, $|Y_n(\omega)| < \epsilon$.
Ceci étant vrai pour tout $\epsilon > 0$ (en prenant une suite dénombrable $\epsilon_k \to 0$), la suite de variables aléatoires $Y_n$ converge presque sûrement vers 0.
