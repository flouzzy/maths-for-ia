# Exercice 6 : Application à la loi des grands nombres

$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(Z_n)$ une suite de variables aléatoires indépendantes centrées telles que $\mathbb{E}[Z_n^4] \le K$ pour une constante $K$.
Soit $S_n = \sum_{i=1}^n Z_i$. Montrer en utilisant le lemme de Borel-Cantelli que $\frac{S_n}{n} \xrightarrow{p.s.} 0$.

**Correction :**
L'indépendance et l'espérance nulle impliquent que $\mathbb{E}[Z_i] = 0$.
On calcule $\mathbb{E}[S_n^4] = \mathbb{E}\left[ \left(\sum_{i=1}^n Z_i\right)^4 \right]$.
En développant ce polynôme, les termes de la forme $\mathbb{E}[Z_i Z_j^3]$ ou $\mathbb{E}[Z_i Z_j Z_k^2]$ s'annulent par indépendance et car $\mathbb{E}[Z_i]=0$.
Il reste seulement les termes $\mathbb{E}[Z_i^4]$ (au nombre de $n$) et les termes $\mathbb{E}[Z_i^2 Z_j^2]$ (au nombre de $3n(n-1)$).
D'après l'inégalité de Cauchy-Schwarz, $\mathbb{E}[Z_i^2 Z_j^2] = \mathbb{E}[Z_i^2]\mathbb{E}[Z_j^2] \le \sqrt{\mathbb{E}[Z_i^4]\mathbb{E}[Z_j^4]} \le K$.
Donc $\mathbb{E}[S_n^4] \le nK + 3n(n-1)K \le 3n^2K$.
Appliquons l'inégalité de Markov à $S_n^4$ :
Pour tout $\epsilon > 0$, posons $A_n = \left\{ \left|\frac{S_n}{n}\right| \ge \epsilon \right\} = \{ |S_n| \ge n\epsilon \}$.
$$ \mathbb{P}(A_n) = \mathbb{P}(S_n^4 \ge n^4\epsilon^4) \le \frac{\mathbb{E}[S_n^4]}{n^4\epsilon^4} \le \frac{3n^2K}{n^4\epsilon^4} = \frac{3K}{\epsilon^4 n^2} $$
La série $\sum \mathbb{P}(A_n)$ est donc majorée par $\sum \frac{3K}{\epsilon^4 n^2}$, qui est une série de Riemann convergente.
Par le premier lemme de Borel-Cantelli, l'événement $\{ |\frac{S_n}{n}| \ge \epsilon \}$ ne se réalise qu'un nombre fini de fois presque sûrement.
Ainsi, $\frac{S_n}{n}$ converge presque sûrement vers 0.
