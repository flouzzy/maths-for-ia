# Exercice 04 : Application combinée de théorèmes de croissances comparées

## Énoncé
Soit $u_n = \frac{n^2 + \ln n}{e^n}$ pour $n \ge 1$.
Montrer que la série $\sum u_n$ converge en utilisant la règle du $n^2 \cdot u_n$.

## Correction Détaillée
1. **Positivité :**
   Pour $n \ge 1$, $n^2 + \ln n > 0$ et $e^n > 0$. Donc $u_n > 0$.

2. **Règle du $n^\alpha u_n$ avec $\alpha = 2$ :**
   Considérons la limite du produit $n^2 u_n$.
   $$n^2 u_n = n^2 \frac{n^2 + \ln n}{e^n} = \frac{n^4 + n^2 \ln n}{e^n}$$
   Séparons l'expression en deux fractions :
   $$n^2 u_n = \frac{n^4}{e^n} + \frac{n^2 \ln n}{e^n}$$

3. **Évaluation des limites (Croissances comparées) :**
   D'après le théorème des croissances comparées entre fonctions puissances et exponentielles en l'infini, l'exponentielle l'emporte :
   $\lim_{n \to \infty} \frac{n^4}{e^n} = 0$.
   De plus, pour le deuxième terme, $\ln n \le n$ (pour $n$ assez grand), donc $\frac{n^2 \ln n}{e^n} \le \frac{n^3}{e^n}$, qui tend également vers $0$. Ainsi :
   $\lim_{n \to \infty} \frac{n^2 \ln n}{e^n} = 0$.
   Par conséquent,
   $$\lim_{n \to \infty} n^2 u_n = 0 + 0 = 0$$

4. **Conclusion et majoration par Riemann :**
   Comme $\lim_{n \to \infty} n^2 u_n = 0$, cela implique qu'il existe un rang $N$ à partir duquel $n^2 u_n \le 1$.
   Donc pour $n \ge N$, $u_n \le \frac{1}{n^2}$.
   Or, la série $\sum \frac{1}{n^2}$ converge (série de Riemann avec $\alpha = 2 > 1$).
   Par le critère de majoration des séries à termes positifs, la série $\sum u_n$ converge.
