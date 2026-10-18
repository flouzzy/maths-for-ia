# Exercice 1 : Au-delà de la Variance : La Loi Forte des Grands Nombres par Troncature
$\bigstar\star\star\star\star$

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires réelles indépendantes et identiquement distribuées (i.i.d.) définies sur un espace de probabilité $(\Omega, \mathcal{F}, P)$. Nous supposons que $E[|X_1|] < \infty$. Soit $\mu = E[X_1]$. L'objectif de cet exercice est d'établir la Loi Forte des Grands Nombres (LFGN) pour cette suite, à savoir que $\frac{1}{N} \sum_{n=1}^N X_n \to \mu$ presque sûrement (p.s.) lorsque $N \to \infty$. Cette démonstration ne requiert pas l'existence d'une variance finie.

1.  **Préliminaires sur la Troncature.**
    Pour chaque $n \ge 1$, on définit la variable aléatoire tronquée $Y_n$ par $Y_n = X_n \mathbf{1}_{\{|X_n| \le n\}}$, où $\mathbf{1}_A$ est la fonction indicatrice de l'événement $A$.
    a.  Montrer que $\sum_{n=1}^\infty P(X_n \ne Y_n) < \infty$.
    b.  En déduire que $P(X_n \ne Y_n \text{ infiniment souvent}) = 0$. Que peut-on conclure sur la convergence de $\frac{1}{N} \sum_{n=1}^N X_n$ si l'on suppose que $\frac{1}{N} \sum_{n=1}^N Y_n$ converge presque sûrement ?
    c.  Montrer que $E[Y_n] \to \mu$ lorsque $n \to \infty$.

2.  **Analyse de la Variance des Variables Tronquées.**
    a.  Montrer que $\sum_{n=1}^\infty \frac{E[Y_n^2]}{n^2} < \infty$. (Indication : Utiliser la formule $E[Z] = \int_0^\infty P(Z>t) dt$ pour $Z \ge 0$ et un changement d'ordre de sommation et d'intégration).
    b.  En déduire que $\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} < \infty$.

3.  **Convergence de la Somme des Variables Tronquées Centrées.**
    Soit $S_N' = \sum_{n=1}^N (Y_n - E[Y_n])$.
    a.  Montrer que pour tout $\epsilon > 0$, $\sum_{k=1}^\infty P\left(\left|\frac{S_{2^k}'}{2^k}\right| > \epsilon\right) < \infty$. (Indication : Utiliser l'inégalité de Chebyshev et le lemme de Borel-Cantelli).
    b.  En déduire que $\frac{S_{2^k}'}{2^k} \to 0$ presque sûrement lorsque $k \to \infty$.
    c.  Pour montrer la convergence pour tout $N$, on peut utiliser l'inégalité de Kolmogorov. Pour $N \in (2^{k-1}, 2^k]$, montrer que
        $$ \max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| \le \frac{1}{2^{k-1}} \max_{2^{k-1} < N \le 2^k} |S_N'| $$
        En utilisant l'inégalité de Kolmogorov pour les sommes $S_N'$, montrer que pour tout $\epsilon > 0$,
        $$ \sum_{k=1}^\infty P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon\right) < \infty $$
        (Rappel : L'inégalité de Kolmogorov stipule que pour des variables indépendantes $Z_i$ avec $E[Z_i]=0$ et $\text{Var}(Z_i) < \infty$, on a $P\left(\max_{1 \le j \le n} \left|\sum_{i=1}^j Z_i\right| > \delta\right) \le \frac{1}{\delta^2} \sum_{i=1}^n \text{Var}(Z_i)$).
    d.  En déduire que $\frac{S_N'}{N} \to 0$ presque sûrement lorsque $N \to \infty$.

4.  **Conclusion.**
    En utilisant les résultats précédents, démontrer que $\frac{1}{N} \sum_{n=1}^N X_n \to \mu$ presque sûrement lorsque $N \to \infty$.

---

### Correction de l'Exercice 1

1.  **Préliminaires sur la Troncature.**
    a.  Nous devons montrer que $\sum_{n=1}^\infty P(X_n \ne Y_n) < \infty$.
        Par définition, $X_n \ne Y_n$ si et seulement si $|X_n| > n$.
        Puisque les variables aléatoires $(X_n)_{n \ge 1}$ sont identiquement distribuées, $P(X_n \ne Y_n) = P(|X_1| > n)$ pour tout $n \ge 1$.
        Nous devons donc montrer que $\sum_{n=1}^\infty P(|X_1| > n) < \infty$.
        Pour toute variable aléatoire $Z \ge 0$, son espérance $E[Z]$ peut être exprimée comme $E[Z] = \sum_{n=0}^\infty P(Z > n)$.
        En appliquant cette formule à la variable aléatoire $|X_1|$, nous avons $E[|X_1|] = \sum_{n=0}^\infty P(|X_1| > n)$.
        Par hypothèse, $E[|X_1|] < \infty$.
        Par conséquent, la somme $\sum_{n=1}^\infty P(|X_1| > n)$ est une partie de la somme convergente $E[|X_1|]$, et donc $\sum_{n=1}^\infty P(X_n \ne Y_n) < \infty$.

    b.  Nous avons montré que $\sum_{n=1}^\infty P(X_n \ne Y_n) < \infty$.
        D'après le premier lemme de Borel-Cantelli, si la somme des probabilités d'une suite d'événements est finie, alors la probabilité que ces événements se produisent infiniment souvent est nulle.
        Ainsi, $P(X_n \ne Y_n \text{ infiniment souvent}) = P(\limsup_{n \to \infty} \{X_n \ne Y_n\}) = 0$.
        Cela signifie que presque sûrement, il n'y a qu'un nombre fini d'indices $n$ pour lesquels $X_n \ne Y_n$.
        Autrement dit, pour presque tout $\omega \in \Omega$, il existe un entier $N_0(\omega)$ tel que pour tout $n > N_0(\omega)$, nous avons $X_n(\omega) = Y_n(\omega)$.
        Considérons la somme $\frac{1}{N} \sum_{n=1}^N X_n(\omega)$. Pour $N > N_0(\omega)$, nous pouvons écrire :
        $$ \frac{1}{N} \sum_{n=1}^N X_n(\omega) = \frac{1}{N} \sum_{n=1}^N Y_n(\omega) + \frac{1}{N} \sum_{n=1}^{N_0(\omega)} (X_n(\omega) - Y_n(\omega)) $$
        Si nous supposons que $\frac{1}{N} \sum_{n=1}^N Y_n \to L$ presque sûrement lorsque $N \to \infty$, alors nous devons analyser le second terme.
        Le terme $\sum_{n=1}^{N_0(\omega)} (X_n(\omega) - Y_n(\omega))$ est une somme finie de variables aléatoires (pour un $\omega$ fixé, $N_0(\omega)$ est fixé). C'est donc une constante finie.
        Lorsque $N \to \infty$, $\frac{1}{N} \sum_{n=1}^{N_0(\omega)} (X_n(\omega) - Y_n(\omega)) \to 0$.
        Par conséquent, si $\frac{1}{N} \sum_{n=1}^N Y_n \to L$ presque sûrement, alors $\frac{1}{N} \sum_{n=1}^N X_n \to L + 0 = L$ presque sûrement.

    c.  Nous devons montrer que $E[Y_n] \to \mu$ lorsque $n \to \infty$.
        Par définition, $E[Y_n] = E[X_n \mathbf{1}_{\{|X_n| \le n\}}]$.
        Puisque les variables $(X_n)_{n \ge 1}$ sont identiquement distribuées, $E[Y_n] = E[X_1 \mathbf{1}_{\{|X_1| \le n\}}]$.
        Considérons la suite de variables aléatoires $Z_n = X_1 \mathbf{1}_{\{|X_1| \le n\}}$.
        Lorsque $n \to \infty$, l'événement $\{|X_1| \le n\}$ tend vers l'événement $\Omega$ (l'ensemble de tous les résultats possibles), car $|X_1|$ est une variable aléatoire finie.
        Donc, $Z_n(\omega) \to X_1(\omega)$ pour presque tout $\omega \in \Omega$.
        De plus, nous avons $|Z_n(\omega)| = |X_1(\omega) \mathbf{1}_{\{|X_1(\omega)| \le n\}}| \le |X_1(\omega)|$.
        Nous avons par hypothèse $E[|X_1|] < \infty$.
        Par le théorème de convergence dominée de Lebesgue, puisque $Z_n \to X_1$ presque sûrement et que $|Z_n| \le |X_1|$ avec $E[|X_1|] < \infty$, nous pouvons intervertir la limite et l'espérance :
        $$ \lim_{n \to \infty} E[Z_n] = E[\lim_{n \to \infty} Z_n] = E[X_1] $$
        Ainsi, $E[Y_n] \to E[X_1] = \mu$ lorsque $n \to \infty$.

2.  **Analyse de la Variance des Variables Tronquées.**
    a.  Nous devons montrer que $\sum_{n=1}^\infty \frac{E[Y_n^2]}{n^2} < \infty$.
        Puisque les variables $X_n$ sont i.i.d., $E[Y_n^2] = E[X_1^2 \mathbf{1}_{\{|X_1| \le n\}}]$.
        Pour une variable aléatoire non négative $Z$, $E[Z] = \int_0^\infty P(Z > t) dt$.
        Appliquons cette formule à $Z = X_1^2 \mathbf{1}_{\{|X_1| \le n\}}$.
        $P(X_1^2 \mathbf{1}_{\{|X_1| \le n\}} > t) = P(X_1^2 > t \text{ et } |X_1| \le n)$.
        Si $t \ge n^2$, alors $P(X_1^2 > t \text{ et } |X_1| \le n) = 0$.
        Si $t < n^2$, alors $P(X_1^2 > t \text{ et } |X_1| \le n) = P(\sqrt{t} < |X_1| \le n)$.
        Donc, $E[Y_n^2] = \int_0^{n^2} P(\sqrt{t} < |X_1| \le n) dt$.
        Effectuons le changement de variable $u = \sqrt{t}$, d'où $t = u^2$ et $dt = 2u du$.
        $E[Y_n^2] = \int_0^n P(u < |X_1| \le n) 2u du = \int_0^n 2u (P(|X_1| > u) - P(|X_1| > n)) du$.
        Ceci peut être réécrit comme $2 \int_0^n u P(|X_1| > u) du - 2 P(|X_1| > n) \int_0^n u du = 2 \int_0^n u P(|X_1| > u) du - n^2 P(|X_1| > n)$.
        Nous devons évaluer la somme $\sum_{n=1}^\infty \frac{E[Y_n^2]}{n^2}$.
        $$ \sum_{n=1}^\infty \frac{E[Y_n^2]}{n^2} = \sum_{n=1}^\infty \frac{1}{n^2} \left( 2 \int_0^n u P(|X_1| > u) du - n^2 P(|X_1| > n) \right) $$
        $$ = 2 \sum_{n=1}^\infty \frac{1}{n^2} \int_0^n u P(|X_1| > u) du - \sum_{n=1}^\infty P(|X_1| > n) $$
        Le second terme, $\sum_{n=1}^\infty P(|X_1| > n)$, est fini et égal à $E[|X_1|]$ (moins $P(|X_1|>0)$ si on commence la somme à $n=0$). Il est donc convergent d'après la partie 1.a.
        Concentrons-nous sur le premier terme : $2 \sum_{n=1}^\infty \frac{1}{n^2} \int_0^n u P(|X_1| > u) du$.
        Nous pouvons intervertir l'ordre de sommation et d'intégration (tous les termes sont positifs) :
        $$ \sum_{n=1}^\infty \frac{1}{n^2} \int_0^n u P(|X_1| > u) du = \int_0^\infty u P(|X_1| > u) \left( \sum_{n=\lceil u \rceil}^\infty \frac{1}{n^2} \right) du $$
        Pour $u \ge 1$, nous avons $\sum_{n=\lceil u \rceil}^\infty \frac{1}{n^2} \le \frac{1}{\lceil u \rceil^2} + \int_{\lceil u \rceil}^\infty \frac{1}{x^2} dx \le \frac{1}{u^2} + \int_u^\infty \frac{1}{x^2} dx = \frac{1}{u^2} + \frac{1}{u}$.
        Pour $u \ge 1$, $\frac{1}{u^2} + \frac{1}{u} \le \frac{2}{u}$.
        Pour $u \in (0, 1]$, $\sum_{n=\lceil u \rceil}^\infty \frac{1}{n^2} = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.
        Donc, l'intégrale devient :
        $$ \int_0^1 u P(|X_1| > u) \frac{\pi^2}{6} du + \int_1^\infty u P(|X_1| > u) \left( \frac{1}{u^2} + \frac{1}{u} \right) du $$
        $$ \le \frac{\pi^2}{6} \int_0^1 u P(|X_1| > u) du + \int_1^\infty \left( \frac{1}{u} + 1 \right) P(|X_1| > u) du $$
        Le premier terme est fini car $P(|X_1|>u) \le 1$.
        Le second terme est $\int_1^\infty \frac{1}{u} P(|X_1| > u) du + \int_1^\infty P(|X_1| > u) du$.
        Nous savons que $\int_1^\infty P(|X_1| > u) du \le E[|X_1|] < \infty$.
        Pour $\int_1^\infty \frac{1}{u} P(|X_1| > u) du$, puisque $P(|X_1| > u) \le E[|X_1|]/u$ (par inégalité de Markov), cela ne garantit pas la convergence.
        Cependant, nous savons que $E[|X_1|] = \int_0^\infty P(|X_1|>u) du$.
        L'expression $2 \int_0^\infty u P(|X_1| > u) \left( \sum_{n=\lceil u \rceil}^\infty \frac{1}{n^2} \right) du$ est majorée par $C \int_0^\infty P(|X_1| > u) du = C E[|X_1|]$ pour une constante $C$ appropriée (par exemple, $C = \max(\frac{\pi^2}{6}, 2)$).
        Plus rigoureusement, $\sum_{n=\lceil u \rceil}^\infty \frac{1}{n^2} \le \frac{C}{u}$ pour $u \ge 1$ et est bornée pour $u \in (0,1]$.
        Donc, $\int_0^\infty u P(|X_1| > u) \left( \sum_{n=\lceil u \rceil}^\infty \frac{1}{n^2} \right) du \le \int_0^1 u P(|X_1| > u) \frac{\pi^2}{6} du + \int_1^\infty u P(|X_1| > u) \frac{2}{u} du$.
        Le premier terme est fini. Le second terme est $2 \int_1^\infty P(|X_1| > u) du \le 2 E[|X_1|] < \infty$.
        Par conséquent, $\sum_{n=1}^\infty \frac{E[Y_n^2]}{n^2} < \infty$.

    b.  Nous devons en déduire que $\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} < \infty$.
        Nous savons que $\text{Var}(Y_n) = E[Y_n^2] - (E[Y_n])^2$.
        D'après la partie 1.c, $E[Y_n] \to \mu$ lorsque $n \to \infty$.
        Puisque la suite $(E[Y_n])_{n \ge 1}$ converge, elle est bornée. Il existe donc une constante $M < \infty$ telle que $|E[Y_n]| \le M$ pour tout $n \ge 1$.
        Par conséquent, $(E[Y_n])^2 \le M^2$ pour tout $n \ge 1$.
        Nous pouvons écrire la somme comme :
        $$ \sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} = \sum_{n=1}^\infty \frac{E[Y_n^2] - (E[Y_n])^2}{n^2} = \sum_{n=1}^\infty \frac{E[Y_n^2]}{n^2} - \sum_{n=1}^\infty \frac{(E[Y_n])^2}{n^2} $$
        Le premier terme, $\sum_{n=1}^\infty \frac{E[Y_n^2]}{n^2}$, est convergent d'après la partie 2.a.
        Le second terme, $\sum_{n=1}^\infty \frac{(E[Y_n])^2}{n^2}$, est également convergent car $(E[Y_n])^2 \le M^2$ et $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} < \infty$.
        Puisque les deux sommes sont convergentes, leur différence est également convergente.
        Donc, $\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} < \infty$.

3.  **Convergence de la Somme des Variables Tronquées Centrées.**
    a.  Nous devons montrer que pour tout $\epsilon > 0$, $\sum_{k=1}^\infty P\left(\left|\frac{S_{2^k}'}{2^k}\right| > \epsilon\right) < \infty$.
        Les variables $Z_n = Y_n - E[Y_n]$ sont indépendantes et centrées ($E[Z_n]=0$).
        $S_{2^k}' = \sum_{n=1}^{2^k} Z_n$.
        En utilisant l'inégalité de Chebyshev pour la variable $\frac{S_{2^k}'}{2^k}$ :
        $$ P\left(\left|\frac{S_{2^k}'}{2^k}\right| > \epsilon\right) \le \frac{E\left[\left(\frac{S_{2^k}'}{2^k}\right)^2\right]}{\epsilon^2} = \frac{\text{Var}(S_{2^k}')}{(2^k)^2 \epsilon^2} $$
        Puisque les $Z_n$ sont indépendantes, $\text{Var}(S_{2^k}') = \sum_{n=1}^{2^k} \text{Var}(Z_n) = \sum_{n=1}^{2^k} \text{Var}(Y_n)$.
        Donc, $P\left(\left|\frac{S_{2^k}'}{2^k}\right| > \epsilon\right) \le \frac{1}{\epsilon^2 (2^k)^2} \sum_{n=1}^{2^k} \text{Var}(Y_n)$.
        Nous devons montrer que $\sum_{k=1}^\infty \frac{1}{\epsilon^2 (2^k)^2} \sum_{n=1}^{2^k} \text{Var}(Y_n) < \infty$.
        En ignorant la constante $\frac{1}{\epsilon^2}$, nous analysons la somme $\sum_{k=1}^\infty \frac{1}{4^k} \sum_{n=1}^{2^k} \text{Var}(Y_n)$.
        Nous pouvons intervertir l'ordre de sommation (tous les termes sont positifs) :
        $$ \sum_{n=1}^\infty \text{Var}(Y_n) \sum_{k: 2^k \ge n}^\infty \frac{1}{4^k} $$
        Pour un $n$ donné, soit $k_0 = \lceil \log_2 n \rceil$ le plus petit entier tel que $2^{k_0} \ge n$.
        Alors $\sum_{k=k_0}^\infty \frac{1}{4^k} = \frac{1}{4^{k_0}} \sum_{j=0}^\infty \left(\frac{1}{4}\right)^j = \frac{1}{4^{k_0}} \frac{1}{1 - 1/4} = \frac{4}{3} \frac{1}{4^{k_0}}$.
        Puisque $2^{k_0} \ge n$, nous avons $4^{k_0} = (2^{k_0})^2 \ge n^2$.
        Donc, $\frac{1}{4^{k_0}} \le \frac{1}{n^2}$.
        Par conséquent, $\sum_{k: 2^k \ge n}^\infty \frac{1}{4^k} \le \frac{4}{3n^2}$.
        En substituant cela dans la somme :
        $$ \sum_{n=1}^\infty \text{Var}(Y_n) \left( \sum_{k: 2^k \ge n}^\infty \frac{1}{4^k} \right) \le \sum_{n=1}^\infty \text{Var}(Y_n) \frac{4}{3n^2} = \frac{4}{3} \sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} $$
        D'après la partie 2.b, nous savons que $\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} < \infty$.
        Ainsi, $\sum_{k=1}^\infty P\left(\left|\frac{S_{2^k}'}{2^k}\right| > \epsilon\right) < \infty$.

    b.  D'après la partie 3.a, nous avons $\sum_{k=1}^\infty P\left(\left|\frac{S_{2^k}'}{2^k}\right| > \epsilon\right) < \infty$ pour tout $\epsilon > 0$.
        En appliquant le premier lemme de Borel-Cantelli, cela implique que $P\left(\left|\frac{S_{2^k}'}{2^k}\right| > \epsilon \text{ infiniment souvent}\right) = 0$.
        Ceci signifie que pour presque tout $\omega \in \Omega$, pour tout $\epsilon > 0$, il existe un entier $K_0(\omega, \epsilon)$ tel que pour tout $k > K_0(\omega, \epsilon)$, nous avons $\left|\frac{S_{2^k}'(\omega)}{2^k}\right| \le \epsilon$.
        Ceci est la définition de la convergence presque sûre vers 0.
        Par conséquent, $\frac{S_{2^k}'}{2^k} \to 0$ presque sûrement lorsque $k \to \infty$.

    c.  Soit $N$ un entier tel que $2^{k-1} < N \le 2^k$.
        Alors $\frac{1}{N} < \frac{1}{2^{k-1}}$.
        Donc, $\left|\frac{S_N'}{N}\right| < \frac{|S_N'|}{2^{k-1}}$.
        En prenant le maximum sur l'intervalle $(2^{k-1}, 2^k]$ :
        $$ \max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| \le \max_{2^{k-1} < N \le 2^k} \frac{|S_N'|}{2^{k-1}} = \frac{1}{2^{k-1}} \max_{2^{k-1} < N \le 2^k} |S_N'| $$
        Ceci établit la première partie de la question.
        Maintenant, nous devons montrer que $\sum_{k=1}^\infty P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon\right) < \infty$.
        En utilisant l'inégalité que nous venons de démontrer :
        $$ P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon\right) \le P\left(\frac{1}{2^{k-1}} \max_{2^{k-1} < N \le 2^k} |S_N'| > \epsilon\right) = P\left(\max_{2^{k-1} < N \le 2^k} |S_N'| > \epsilon 2^{k-1}\right) $$
        Les variables $Z_n = Y_n - E[Y_n]$ sont indépendantes et centrées. Nous pouvons appliquer l'inégalité de Kolmogorov à la somme $S_N' = \sum_{n=1}^N Z_n$.
        L'inégalité de Kolmogorov stipule que pour des variables indépendantes $Z_1, \dots, Z_m$ avec $E[Z_i]=0$ et $\text{Var}(Z_i) < \infty$, on a $P\left(\max_{1 \le j \le m} \left|\sum_{i=1}^j Z_i\right| > \delta\right) \le \frac{1}{\delta^2} \sum_{i=1}^m \text{Var}(Z_i)$.
        Appliquons cette inégalité avec $m = 2^k$ et $\delta = \epsilon 2^{k-1}$.
        Notez que $\max_{2^{k-1} < N \le 2^k} |S_N'| \le \max_{1 \le N \le 2^k} |S_N'|$.
        Donc,
        $$ P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon\right) \le P\left(\max_{1 \le N \le 2^k} |S_N'| > \epsilon 2^{k-1}\right) \le \frac{1}{(\epsilon 2^{k-1})^2} \sum_{n=1}^{2^k} \text{Var}(Y_n) $$
        $$ = \frac{1}{\epsilon^2 4^{k-1}} \sum_{n=1}^{2^k} \text{Var}(Y_n) = \frac{4}{\epsilon^2} \frac{1}{4^k} \sum_{n=1}^{2^k} \text{Var}(Y_n) $$
        Nous devons sommer cette expression sur $k$:
        $$ \sum_{k=1}^\infty P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon\right) \le \sum_{k=1}^\infty \frac{4}{\epsilon^2} \frac{1}{4^k} \sum_{n=1}^{2^k} \text{Var}(Y_n) $$
        La somme $\sum_{k=1}^\infty \frac{1}{4^k} \sum_{n=1}^{2^k} \text{Var}(Y_n)$ a été évaluée dans la partie 3.a et a été montrée convergente vers $\frac{4}{3} \sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2}$.
        Puisque $\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} < \infty$ d'après la partie 2.b, la somme totale est finie.
        Par conséquent, $\sum_{k=1}^\infty P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon\right) < \infty$.

    d.  D'après la partie 3.c, nous avons $\sum_{k=1}^\infty P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon\right) < \infty$ pour tout $\epsilon > 0$.
        En appliquant le premier lemme de Borel-Cantelli, cela implique que $P\left(\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'}{N}\right| > \epsilon \text{ infiniment souvent}\right) = 0$.
        Ceci signifie que pour presque tout $\omega \in \Omega$, pour tout $\epsilon > 0$, il existe un entier $K_1(\omega, \epsilon)$ tel que pour tout $k > K_1(\omega, \epsilon)$, nous avons $\max_{2^{k-1} < N \le 2^k} \left|\frac{S_N'(\omega)}{N}\right| \le \epsilon$.
        Pour tout $N > 2^{K_1(\omega, \epsilon)}$, il existe un $k > K_1(\omega, \epsilon)$ tel que $2^{k-1} < N \le 2^k$. Pour un tel $N$, nous avons $\left|\frac{S_N'(\omega)}{N}\right| \le \epsilon$.
        Ceci est la définition de la convergence presque sûre vers 0 pour la suite $\frac{S_N'}{N}$.
        Par conséquent, $\frac{S_N'}{N} \to 0$ presque sûrement lorsque $N \to \infty$.

4.  **Conclusion.**
    Nous voulons démontrer que $\frac{1}{N} \sum_{n=1}^N X_n \to \mu$ presque sûrement lorsque $N \to \infty$.
    D'après la partie 1.b, nous avons établi que si $\frac{1}{N} \sum_{n=1}^N Y_n \to L$ presque sûrement, alors $\frac{1}{N} \sum_{n=1}^N X_n \to L$ presque sûrement.
    Nous allons maintenant analyser la convergence de $\frac{1}{N} \sum_{n=1}^N Y_n$.
    Nous pouvons décomposer cette somme comme suit :
    $$ \frac{1}{N} \sum_{n=1}^N Y_n = \frac{1}{N} \sum_{n=1}^N (Y_n - E[Y_n]) + \frac{1}{N} \sum_{n=1}^N E[Y_n] $$
    D'après la partie 3.d, nous avons montré que $\frac{1}{N} \sum_{n=1}^N (Y_n - E[Y_n]) = \frac{S_N'}{N} \to 0$ presque sûrement lorsque $N \to \infty$.
    Il nous reste à évaluer la limite du second terme, $\frac{1}{N} \sum_{n=1}^N E[Y_n]$.
    D'après la partie 1.c, nous savons que $E[Y_n] \to \mu$ lorsque $n \to \infty$.
    Le théorème de Cesaro (ou lemme de Toeplitz) stipule que si une suite $(a_n)_{n \ge 1}$ converge vers une limite $L$, alors sa moyenne de Cesaro, $\frac{1}{N} \sum_{n=1}^N a_n$, converge également vers $L$.
    En appliquant ce théorème à la suite $a_n = E[Y_n]$, qui converge vers $\mu$, nous obtenons :
    $$ \lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^N E[Y_n] = \mu $$
    En combinant ces deux résultats, nous avons :
    $$ \frac{1}{N} \sum_{n=1}^N Y_n = \frac{1}{N} \sum_{n=1}^N (Y_n - E[Y_n]) + \frac{1}{N} \sum_{n=1}^N E[Y_n] \to 0 + \mu = \mu \quad \text{presque sûrement} $$
    Enfin, en utilisant la conclusion de la partie 1.b, puisque $\frac{1}{N} \sum_{n=1}^N Y_n \to \mu$ presque sûrement, il s'ensuit que $\frac{1}{N} \sum_{n=1}^N X_n \to \mu$ presque sûrement.
    Ceci achève la démonstration de la Loi Forte des Grands Nombres pour des variables i.i.d. avec une espérance finie.