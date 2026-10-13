# Exercice 7 : Borel-Cantelli sans indépendance : une fausse conclusion

$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer par un contre-exemple que si les événements $(A_n)$ ne sont pas indépendants, la divergence de $\sum \mathbb{P}(A_n) = +\infty$ n'implique pas que $\mathbb{P}(\limsup A_n) = 1$.

**Correction :**
Soit un espace de probabilité modélisant le tirage uniforme d'un nombre $U$ dans l'intervalle $[0, 1]$. La loi de $U$ est continue uniforme.
Considérons l'événement $A_n = \{ U \le \frac{1}{n} \}$.
La probabilité de chaque événement est $\mathbb{P}(A_n) = \frac{1}{n}$.
La série $\sum \mathbb{P}(A_n) = \sum \frac{1}{n} = +\infty$ est divergente.
Toutefois, étudions la limite supérieure de ces événements.
$$ \limsup_{n \to \infty} A_n = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k $$
Puisque la suite $(A_n)$ est décroissante (si $U \le 1/(n+1)$, alors $U \le 1/n$, donc $A_{n+1} \subset A_n$), l'union $\bigcup_{k=n}^\infty A_k$ est simplement égale à $A_n$.
Ainsi, $\limsup_{n \to \infty} A_n = \bigcap_{n=1}^\infty A_n$.
L'événement $\bigcap_{n=1}^\infty A_n$ est l'ensemble des $\omega$ tels que pour tout $n \ge 1$, $U(\omega) \le \frac{1}{n}$.
Le seul nombre réel positif ou nul satisfaisant cette condition est $0$.
Donc $\limsup_{n \to \infty} A_n = \{ U = 0 \}$.
Or, pour une variable aléatoire continue, la probabilité d'un point est nulle : $\mathbb{P}(U = 0) = 0$.
Nous avons donc $\mathbb{P}(\limsup A_n) = 0$, et ce malgré la divergence de la série des probabilités.
Cela illustre de manière flagrante que l'hypothèse d'indépendance dans le second lemme de Borel-Cantelli est absolument incontournable.
