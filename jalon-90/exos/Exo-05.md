# Exercice 05

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Convergence en loi (théorème de Slutsky partiel)

Soient $(X_n)$ et $(Y_n)$ deux suites de variables aléatoires.
On suppose que $X_n$ converge en loi vers $X$, et que $Y_n$ converge en probabilité vers la variable certaine $c$ ($c \in \mathbb{R}$).
Montrez que la suite $X_n + Y_n$ converge en loi vers $X + c$.

**Correction exhaustive :**
Pour prouver que $X_n + Y_n \xrightarrow{\mathcal{L}} X + c$, nous allons utiliser la caractérisation par l'espérance des fonctions continues bornées. Soit $f : \mathbb{R} \to \mathbb{R}$ uniformément continue et bornée. Soit $M > 0$ la borne telle que $|f(x)| \le M$ pour tout $x$.
Puisque $f$ est uniformément continue, pour tout $\eta > 0$, il existe $\delta > 0$ tel que pour tous $x, y \in \mathbb{R}$, $|x - y| < \delta \implies |f(x) - f(y)| < \eta$.
Nous voulons montrer que $\lim_{n \to \infty} \mathbb{E}[f(X_n + Y_n)] = \mathbb{E}[f(X + c)]$.
Décomposons la différence :
$$ |\mathbb{E}[f(X_n + Y_n)] - \mathbb{E}[f(X + c)]| \le |\mathbb{E}[f(X_n + Y_n)] - \mathbb{E}[f(X_n + c)]| + |\mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)]| $$
Traitons le second terme : soit $g(x) = f(x + c)$. La fonction $g$ est également continue et bornée. Puisque $X_n \xrightarrow{\mathcal{L}} X$, par définition de la convergence en loi, on a :
$$ \lim_{n \to \infty} \mathbb{E}[g(X_n)] = \mathbb{E}[g(X)] \implies \lim_{n \to \infty} |\mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)]| = 0 $$
Traitons le premier terme : nous majorons $|f(X_n + Y_n) - f(X_n + c)|$.
L'écart dans l'argument est $|(X_n + Y_n) - (X_n + c)| = |Y_n - c|$.
Introduisons l'événement $A_n = \{|Y_n - c| \ge \delta\}$.
$$ \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|] = \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)| \mathbf{1}_{A_n}] + \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)| \mathbf{1}_{A_n^c}] $$
Sur l'événement $A_n$, on majore l'écart par $2M$. Donc l'espérance est majorée par $2M \cdot \mathbb{P}(A_n)$.
Sur l'événement complémentaire $A_n^c$, on a $|Y_n - c| < \delta$. Par uniforme continuité de $f$, $|f(X_n + Y_n) - f(X_n + c)| < \eta$. L'espérance est donc majorée par $\eta$.
Ainsi :
$$ \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|] \le 2M \cdot \mathbb{P}(|Y_n - c| \ge \delta) + \eta $$
Puisque $Y_n \xrightarrow{\mathbb{P}} c$, pour ce $\delta > 0$ fixé, la probabilité $\mathbb{P}(|Y_n - c| \ge \delta)$ tend vers 0 lorsque $n \to \infty$.
La limite de l'écart est donc inférieure ou égale à $\eta$.
Comme $\eta$ a été choisi arbitrairement petit, la limite de ce terme est nulle.
En sommant les deux limites nulles, on obtient la convergence désirée. (Le résultat se généralise pour $f$ continue bornée grâce au théorème de Portmanteau partiel).
