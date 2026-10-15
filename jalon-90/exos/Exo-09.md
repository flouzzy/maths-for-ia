# Exercice 09

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Montrez que si une suite de variables aléatoires converge en probabilité, alors on peut en extraire une sous-suite qui converge presque sûrement.

**Correction :**
Soit $X_n \xrightarrow{\mathbb{P}} X$. Par définition, pour tout $\epsilon > 0$, $\mathbb{P}(|X_n - X| > \epsilon) \to 0$.
Construisons la sous-suite par extraction. Pour chaque entier $k \ge 1$, fixons $\epsilon_k = \frac{1}{2^k}$.
Puisque la probabilité tend vers zéro, il existe un rang $n_k$ (que l'on peut choisir strictement croissant : $n_1 < n_2 < \dots$) tel que :
$$ \mathbb{P}\left(|X_{n_k} - X| > \frac{1}{2^k}\right) < \frac{1}{2^k} $$
Considérons les événements $A_k = \left\{|X_{n_k} - X| > \frac{1}{2^k}\right\}$.
La somme des probabilités est une série géométrique convergente :
$$ \sum_{k=1}^\infty \mathbb{P}(A_k) < \sum_{k=1}^\infty \frac{1}{2^k} = 1 < \infty $$
D'après le premier Lemme de Borel-Cantelli, la probabilité que les $A_k$ se réalisent infiniment souvent est nulle :
$$ \mathbb{P}(\limsup A_k) = 0 $$
Ainsi, presque sûrement, seuls un nombre fini de $A_k$ se réalisent. Cela implique que pour presque tout $\omega \in \Omega$, il existe un entier $K(\omega)$ tel que pour tout $k \ge K(\omega)$ :
$$ |X_{n_k}(\omega) - X(\omega)| \le \frac{1}{2^k} $$
En passant à la limite lorsque $k \to \infty$, l'écart tend vers $0$ presque sûrement.
Donc $X_{n_k} \xrightarrow{p.s.} X$.
