# Exercice 5

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Convergence presque sûre vers 0

Soit $(Y_n)_{n \ge 1}$ une suite de variables aléatoires réelles. On suppose que pour tout $\epsilon > 0$, il existe $c > 0$ tel que $\mathbb{P}(|Y_n| > \epsilon) \le \frac{c}{n^{3/2}}$.
Démontrer que la suite $(Y_n)$ converge presque sûrement vers 0.

**Correction détaillée :**
1. Fixons un $\epsilon > 0$ quelconque. Soit l'événement $A_n^\epsilon = \{|Y_n| > \epsilon\}$.
2. L'énoncé donne l'inégalité $\mathbb{P}(A_n^\epsilon) \le \frac{c}{n^{3/2}}$.
3. La série $\sum_{n=1}^{\infty} \frac{1}{n^{3/2}}$ est une série de Riemann convergente car $\frac{3}{2} > 1$.
4. Par comparaison de séries à termes positifs, la série $\sum_{n=1}^{\infty} \mathbb{P}(A_n^\epsilon)$ est donc convergente.
5. En appliquant le premier lemme de Borel-Cantelli à la suite d'événements $(A_n^\epsilon)$, on obtient que $\mathbb{P}(\limsup A_n^\epsilon) = 0$.
6. Cela signifie qu'il existe un ensemble $\Omega_\epsilon$ de probabilité 1 tel que pour tout $\omega \in \Omega_\epsilon$, $|Y_n(\omega)| \le \epsilon$ pour tout $n$ assez grand.
7. Pour prouver la convergence vers 0 pour presque tout $\omega$, prenons une suite de rationnels $\epsilon_k = \frac{1}{k}$ pour $k \in \mathbb{N}^*$.
8. On pose $\tilde{\Omega} = \bigcap_{k=1}^{\infty} \Omega_{1/k}$. Comme intersection dénombrable d'ensembles de probabilité 1, $\mathbb{P}(\tilde{\Omega}) = 1$.
9. Pour tout $\omega \in \tilde{\Omega}$ et pour tout $k \in \mathbb{N}^*$, il existe un entier $N$ tel que pour $n \ge N$, $|Y_n(\omega)| \le \frac{1}{k}$. Ceci est la définition stricte de la convergence de $Y_n(\omega)$ vers 0.
10. La convergence est donc presque sûre.
