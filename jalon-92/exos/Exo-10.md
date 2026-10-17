# Exercice 10

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X_i)_{i \ge 1}$ I.I.D. centrées avec $\mathbb{E}[X_1^4] = K < +\infty$.
On note $S_n = \sum_{i=1}^n X_i$.
On admet que $\mathbb{E}[S_n^4] \le 3 K n^2$.
Soit $\epsilon > 0$. Démontrer, en utilisant l'inégalité de Markov sur $\left(\frac{S_n}{n}\right)^4$ et le lemme de Borel-Cantelli, que $\frac{S_n}{n}$ converge vers 0 presque sûrement.

**Correction :**
1. L'inégalité de Markov pour une variable aléatoire positive s'écrit $\mathbb{P}(Y \ge a) \le \frac{\mathbb{E}[Y]}{a}$.
Prenons $Y = \left(\frac{S_n}{n}\right)^4$ et $a = \epsilon^4$.
$\mathbb{P}\left( \left|\frac{S_n}{n}\right| \ge \epsilon \right) = \mathbb{P}\left( \left(\frac{S_n}{n}\right)^4 \ge \epsilon^4 \right) \le \frac{\mathbb{E}\left[\left(\frac{S_n}{n}\right)^4\right]}{\epsilon^4}$.
2. Injectons l'hypothèse de la borne supérieure :
$\mathbb{E}\left[\left(\frac{S_n}{n}\right)^4\right] = \frac{1}{n^4}\mathbb{E}[S_n^4] \le \frac{3 K n^2}{n^4} = \frac{3 K}{n^2}$.
Par conséquent, $\mathbb{P}\left( \left|\frac{S_n}{n}\right| \ge \epsilon \right) \le \frac{3 K}{\epsilon^4 n^2}$.
3. Formons la série des probabilités de ces événements $A_n = \{ |\frac{S_n}{n}| \ge \epsilon \}$ :
$\sum_{n=1}^\infty \mathbb{P}(A_n) \le \sum_{n=1}^\infty \frac{3 K}{\epsilon^4 n^2} = \frac{3 K}{\epsilon^4} \sum_{n=1}^\infty \frac{1}{n^2}$.
La série de Riemann $\sum_{n \ge 1} \frac{1}{n^2}$ converge. Donc la série $\sum \mathbb{P}(A_n)$ converge.
4. Appliquons le 1er lemme de Borel-Cantelli.
Si $\sum \mathbb{P}(A_n) < \infty$, alors la probabilité que les événements $A_n$ se réalisent une infinité de fois est nulle.
Donc $\mathbb{P}(\limsup A_n) = 0$.
Cela équivaut à dire que presqu'sûrement, on est dans $\liminf A_n^c$.
Donc, avec probabilité 1, à partir d'un certain rang $N$, $|\frac{S_n}{n}| < \epsilon$.
5. Comme cela est vrai pour tout $\epsilon > 0$ pris arbitrairement petit, $\frac{S_n}{n}$ converge presque sûrement vers 0.
