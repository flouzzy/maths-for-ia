# Exercice 4 : La Loi Forte des Grands Nombres : Une Démonstration par Troncature et Borel-Cantelli

$\bigstar\bigstar\star\star\star$

**Énoncé :**

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires réelles indépendantes et identiquement distribuées (i.i.d.) définies sur un espace de probabilité $(\Omega, \mathcal{A}, P)$. On suppose que $E[|X_1|] < \infty$. On note $\mu = E[X_1]$. L'objectif de cet exercice est de démontrer la Loi Forte des Grands Nombres (LFGN), c'est-à-dire que la suite des moyennes empiriques $\frac{S_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i$ converge presque sûrement vers $\mu$.

Pour ce faire, nous allons suivre une approche par troncature.

1.  **Troncature des variables :**
    Pour chaque $k \in \mathbb{N}^*$, on définit les variables aléatoires tronquées $Y_k$ et $Z_k$ comme suit :
    $Y_k = X_k \mathbf{1}_{\{|X_k| \le k\}}$ et $Z_k = X_k \mathbf{1}_{\{|X_k| > k\}}$.
    Montrer que $X_k = Y_k + Z_k$ pour tout $k \in \mathbb{N}^*$.

2.  **Convergence de la somme des queues :**
    a.  Montrer que $\sum_{k=1}^\infty P(|X_k| > k) < \infty$.
    b.  En déduire, à l'aide d'un lemme fondamental de la théorie des probabilités, que $P(Z_k \ne 0 \text{ pour une infinité de } k) = 0$.
    c.  Montrer que la série $\sum_{k=1}^\infty Z_k$ converge presque sûrement.
    d.  En déduire que $\frac{1}{n} \sum_{k=1}^n Z_k \xrightarrow{p.s.} 0$ lorsque $n \to \infty$.

3.  **Convergence de l'espérance des variables tronquées :**
    Montrer que $E[Y_k] \xrightarrow{k \to \infty} \mu$.

4.  **Convergence des moyennes des variables tronquées centrées :**
    Soit $Y_k' = Y_k - E[Y_k]$.
    a.  Montrer que $E[(Y_k')^2] = E[Y_k^2] - (E[Y_k])^2$.
    b.  Montrer que $\sum_{k=1}^\infty \frac{E[Y_k^2]}{k^2} < \infty$.
    c.  En déduire que $\sum_{k=1}^\infty \frac{E[(Y_k')^2]}{k^2} < \infty$.
    d.  Soit $S_n' = \sum_{k=1}^n Y_k'$. En utilisant le théorème des trois séries de Kolmogorov et le lemme de Kronecker, montrer que $\frac{S_n'}{n} \xrightarrow{p.s.} 0$ lorsque $n \to \infty$.

5.  **Conclusion :**
    En combinant les résultats précédents, démontrer que $\frac{S_n}{n} \xrightarrow{p.s.} \mu$ lorsque $n \to \infty$.

---

**Correction :**

1.  **Troncature des variables :**
    Pour tout $k \in \mathbb{N}^*$, nous considérons la décomposition de $X_k$ en deux parties mutuellement exclusives selon la valeur absolue de $X_k$.
    Si $|X_k| \le k$, alors $\mathbf{1}_{\{|X_k| \le k\}} = 1$ et $\mathbf{1}_{\{|X_k| > k\}} = 0$. Dans ce cas, $Y_k = X_k$ et $Z_k = 0$. Donc $Y_k + Z_k = X_k + 0 = X_k$.
    Si $|X_k| > k$, alors $\mathbf{1}_{\{|X_k| \le k\}} = 0$ et $\mathbf{1}_{\{|X_k| > k\}} = 1$. Dans ce cas, $Y_k = 0$ et $Z_k = X_k$. Donc $Y_k + Z_k = 0 + X_k = X_k$.
    Dans tous les cas, $X_k = Y_k + Z_k$ pour tout $k \in \mathbb{N}^*$.

2.  **Convergence de la somme des queues :**
    a.  Nous voulons montrer que $\sum_{k=1}^\infty P(|X_k| > k) < \infty$.
        Puisque les variables aléatoires $(X_k)_{k \in \mathbb{N}^*}$ sont identiquement distribuées, $P(|X_k| > k) = P(|X_1| > k)$ pour tout $k \in \mathbb{N}^*$.
        Considérons la somme $\sum_{k=1}^\infty P(|X_1| > k)$.
        Nous savons que pour toute variable aléatoire $X$ avec $E[|X|] < \infty$, l'espérance peut être exprimée par l'intégrale de sa fonction de survie : $E[|X|] = \int_0^\infty P(|X| > t) dt$.
        Puisque $P(|X_1| > t)$ est une fonction décroissante de $t$, nous pouvons majorer la somme par l'intégrale :
        $\sum_{k=1}^\infty P(|X_1| > k) \le \int_0^\infty P(|X_1| > t) dt$.
        En effet, pour tout $k \ge 1$, $P(|X_1| > k) \le \int_{k-1}^k P(|X_1| > t) dt$.
        Donc, $\sum_{k=1}^\infty P(|X_1| > k) \le \sum_{k=1}^\infty \int_{k-1}^k P(|X_1| > t) dt = \int_0^\infty P(|X_1| > t) dt = E[|X_1|]$.
        Par hypothèse, $E[|X_1|] < \infty$.
        Par conséquent, $\sum_{k=1}^\infty P(|X_k| > k) < \infty$.

    b.  Nous avons montré que $\sum_{k=1}^\infty P(|X_k| > k) < \infty$.
        Par définition, $Z_k \ne 0$ si et seulement si $|X_k| > k$.
        Donc, la série des probabilités $\sum_{k=1}^\infty P(Z_k \ne 0)$ est égale à $\sum_{k=1}^\infty P(|X_k| > k)$, qui est finie.
        D'après le premier lemme de Borel-Cantelli, si $\sum_{k=1}^\infty P(A_k) < \infty$, alors $P(\limsup_{k \to \infty} A_k) = 0$.
        En appliquant ce lemme avec $A_k = \{Z_k \ne 0\}$, nous obtenons $P(\limsup_{k \to \infty} \{Z_k \ne 0\}) = 0$.
        Cela signifie que la probabilité que $Z_k \ne 0$ pour une infinité de $k$ est nulle. En d'autres termes, presque sûrement, seuls un nombre fini de variables $Z_k$ sont non nulles.

    c.  Puisque $P(Z_k \ne 0 \text{ pour une infinité de } k) = 0$, cela signifie que pour presque tout $\omega \in \Omega$, il existe un entier $N(\omega)$ (qui dépend de $\omega$) tel que pour tout $k > N(\omega)$, $Z_k(\omega) = 0$.
        Par conséquent, pour presque tout $\omega$, la série $\sum_{k=1}^\infty Z_k(\omega)$ est une somme finie de termes non nuls (les $Z_k(\omega)$ pour $k \le N(\omega)$) suivie d'une infinité de zéros.
        Une somme finie de nombres réels est toujours convergente.
        Donc, la série $\sum_{k=1}^\infty Z_k$ converge presque sûrement.

    d.  Nous avons établi que la série $\sum_{k=1}^\infty Z_k$ converge presque sûrement.
        Soit $S_Z(\omega) = \sum_{k=1}^\infty Z_k(\omega)$ pour $\omega$ dans l'ensemble de probabilité 1 où la série converge. $S_Z(\omega)$ est une valeur finie.
        Un résultat classique de l'analyse des séries (souvent appelé théorème de Cesaro pour les séries convergentes, ou plus généralement une propriété des suites convergentes) stipule que si une série $\sum_{k=1}^\infty a_k$ converge, alors la moyenne de ses termes tend vers 0, c'est-à-dire $\frac{1}{n} \sum_{k=1}^n a_k \xrightarrow{n \to \infty} 0$.
        En appliquant ce résultat à la suite de variables aléatoires $(Z_k(\omega))_{k \in \mathbb{N}^*}$ pour presque tout $\omega$, nous obtenons :
        $\frac{1}{n} \sum_{k=1}^n Z_k(\omega) \xrightarrow{n \to \infty} 0$ pour presque tout $\omega$.
        Par conséquent, $\frac{1}{n} \sum_{k=1}^n Z_k \xrightarrow{p.s.} 0$ lorsque $n \to \infty$.

3.  **Convergence de l'espérance des variables tronquées :**
    Nous voulons montrer que $E[Y_k] \xrightarrow{k \to \infty} \mu$.
    On a $Y_k = X_k \mathbf{1}_{\{|X_k| \le k\}}$.
    Puisque les variables $X_k$ sont identiquement distribuées, $E[Y_k] = E[X_1 \mathbf{1}_{\{|X_1| \le k\}}]$.
    Nous savons que $E[X_1] = \mu$.
    Nous pouvons écrire $E[X_1 \mathbf{1}_{\{|X_1| \le k\}}] = E[X_1] - E[X_1 \mathbf{1}_{\{|X_1| > k\}}]$.
    Donc, $E[Y_k] = \mu - E[X_1 \mathbf{1}_{\{|X_1| > k\}}]$.
    Pour montrer que $E[Y_k] \to \mu$, il suffit de montrer que $E[X_1 \mathbf{1}_{\{|X_1| > k\}}] \to 0$ lorsque $k \to \infty$.
    Considérons la suite de variables aléatoires $U_k = X_1 \mathbf{1}_{\{|X_1| > k\}}$.
    Pour chaque $\omega \in \Omega$, $X_1(\omega)$ est une valeur finie. Donc, pour $k > |X_1(\omega)|$, l'indicatrice $\mathbf{1}_{\{|X_1(\omega)| > k\}}$ est nulle.
    Ainsi, $U_k(\omega) \xrightarrow{k \to \infty} 0$ pour tout $\omega \in \Omega$, ce qui implique une convergence presque sûre vers 0.
    De plus, la suite $(U_k)_{k \in \mathbb{N}^*}$ est dominée par la variable aléatoire $|X_1|$, car $|U_k| = |X_1 \mathbf{1}_{\{|X_1| > k\}}| \le |X_1|$.
    Par hypothèse, $E[|X_1|] < \infty$.
    Nous pouvons donc appliquer le théorème de convergence dominée de Lebesgue :
    $\lim_{k \to \infty} E[X_1 \mathbf{1}_{\{|X_1| > k\}}] = E[\lim_{k \to \infty} X_1 \mathbf{1}_{\{|X_1| > k\}}] = E[0] = 0$.
    Par conséquent, $E[Y_k] \xrightarrow{k \to \infty} \mu$.

4.  **Convergence des moyennes des variables tronquées centrées :**
    Soit $Y_k' = Y_k - E[Y_k]$.
    a.  Nous voulons montrer que $E[(Y_k')^2] = E[Y_k^2] - (E[Y_k])^2$.
        Par définition, $E[(Y_k')^2] = E[(Y_k - E[Y_k])^2]$.
        En développant le carré de la différence : $E[(Y_k - E[Y_k])^2] = E[Y_k^2 - 2 Y_k E[Y_k] + (E[Y_k])^2]$.
        Par linéarité de l'espérance, et en notant que $E[Y_k]$ est une constante par rapport à l'espérance :
        $E[Y_k^2 - 2 Y_k E[Y_k] + (E[Y_k])^2] = E[Y_k^2] - 2 E[Y_k E[Y_k]] + E[(E[Y_k])^2]$.
        Puisque $E[Y_k]$ est une constante, $E[Y_k E[Y_k]] = E[Y_k] E[Y_k] = (E[Y_k])^2$.
        De même, $E[(E[Y_k])^2] = (E[Y_k])^2$.
        En substituant ces expressions, nous obtenons :
        $E[(Y_k')^2] = E[Y_k^2] - 2(E[Y_k])^2 + (E[Y_k])^2 = E[Y_k^2] - (E[Y_k])^2$.
        Ceci est la définition de la variance de $Y_k$, $Var(Y_k)$.

    b.  Nous voulons montrer que $\sum_{k=1}^\infty \frac{E[Y_k^2]}{k^2} < \infty$.
        On a $Y_k = X_k \mathbf{1}_{\{|X_k| \le k\}}$.
        Donc, $Y_k^2 = X_k^2 \mathbf{1}_{\{|X_k| \le k\}}$.
        Puisque les variables $X_k$ sont i.i.d., $E[Y_k^2] = E[X_1^2 \mathbf{1}_{\{|X_1| \le k\}}]$.
        Considérons la somme $\sum_{k=1}^\infty \frac{E[X_1^2 \mathbf{1}_{\{|X_1| \le k\}}]}{k^2}$.
        Les termes de la somme sont positifs, nous pouvons donc intervertir la somme et l'espérance par le théorème de Fubini-Tonelli :
        $\sum_{k=1}^\infty \frac{E[X_1^2 \mathbf{1}_{\{|X_1| \le k\}}]}{k^2} = E\left[\sum_{k=1}^\infty \frac{X_1^2 \mathbf{1}_{\{|X_1| \le k\}}}{k^2}\right]$.
        Analysons la somme interne pour un $\omega$ fixé, en posant $x = X_1(\omega)$ :
        $\sum_{k=1}^\infty \frac{x^2 \mathbf{1}_{\{|x| \le k\}}}{k^2} = x^2 \sum_{k=\max(1, \lceil |x| \rceil)}^\infty \frac{1}{k^2}$.
        Nous savons que pour $N \ge 1$, $\sum_{k=N}^\infty \frac{1}{k^2} \le \frac{1}{N^2} + \int_N^\infty \frac{1}{t^2} dt = \frac{1}{N^2} + \frac{1}{N}$.
        Si $|x| < 1$, alors $\max(1, \lceil |x| \rceil) = 1$. La somme est $x^2 \sum_{k=1}^\infty \frac{1}{k^2} = x^2 \frac{\pi^2}{6}$.
        Si $|x| \ge 1$, alors $\max(1, \lceil |x| \rceil) = \lceil |x| \rceil$. La somme est $x^2 \sum_{k=\lceil |x| \rceil}^\infty \frac{1}{k^2}$.
        En utilisant la majoration $\sum_{k=N}^\infty \frac{1}{k^2} \le \frac{1}{N} + \frac{1}{N^2}$ avec $N = \lceil |x| \rceil$:
        $x^2 \left( \frac{1}{\lceil |x| \rceil} + \frac{1}{\lceil |x| \rceil^2} \right)$.
        Puisque $\lceil |x| \rceil \ge |x|$, nous avons $\frac{1}{\lceil |x| \rceil} \le \frac{1}{|x|}$ et $\frac{1}{\lceil |x| \rceil^2} \le \frac{1}{|x|^2}$.
        Donc, $x^2 \left( \frac{1}{\lceil |x| \rceil} + \frac{1}{\lceil |x| \rceil^2} \right) \le x^2 \left( \frac{1}{|x|} + \frac{1}{|x|^2} \right) = |x| + 1$.
        En combinant les deux cas, la somme interne est majorée par :
        $x^2 \frac{\pi^2}{6} \mathbf{1}_{\{|x| < 1\}} + (|x| + 1) \mathbf{1}_{\{|x| \ge 1\}}$.
        Prenons l'espérance de cette majoration :
        $E\left[X_1^2 \frac{\pi^2}{6} \mathbf{1}_{\{|X_1| < 1\}} + (|X_1| + 1) \mathbf{1}_{\{|X_1| \ge 1\}}\right]$
        $= \frac{\pi^2}{6} E[X_1^2 \mathbf{1}_{\{|X_1| < 1\}}] + E[|X_1| \mathbf{1}_{\{|X_1| \ge 1\}}] + E[\mathbf{1}_{\{|X_1| \ge 1\}}]$.
        Chacun de ces termes est fini :
        $E[X_1^2 \mathbf{1}_{\{|X_1| < 1\}}] \le E[1^2 \mathbf{1}_{\{|X_1| < 1\}}] \le E[1] = 1 < \infty$.
        $E[|X_1| \mathbf{1}_{\{|X_1| \ge 1\}}] \le E[|X_1|] < \infty$ par hypothèse.
        $E[\mathbf{1}_{\{|X_1| \ge 1\}}] = P(|X_1| \ge 1) \le E[|X_1|] < \infty$ par l'inégalité de Markov.
        Puisque l'espérance de la majoration est finie, la somme $\sum_{k=1}^\infty \frac{E[Y_k^2]}{k^2}$ est finie.

    c.  Nous voulons en déduire que $\sum_{k=1}^\infty \frac{E[(Y_k')^2]}{k^2} < \infty$.
        D'après la question 4.a, nous savons que $E[(Y_k')^2] = Var(Y_k) = E[Y_k^2] - (E[Y_k])^2$.
        Puisque la variance est toujours non négative, $(E[Y_k])^2 \ge 0$.
        Par conséquent, $E[(Y_k')^2] \le E[Y_k^2]$.
        En divisant par $k^2$ et en sommant :
        $\sum_{k=1}^\infty \frac{E[(Y_k')^2]}{k^2} \le \sum_{k=1}^\infty \frac{E[Y_k^2]}{k^2}$.
        D'après la question 4.b, nous avons montré que $\sum_{k=1}^\infty \frac{E[Y_k^2]}{k^2} < \infty$.
        Par conséquent, $\sum_{k=1}^\infty \frac{E[(Y_k')^2]}{k^2} < \infty$.

    d.  Nous voulons montrer que $\frac{S_n'}{n} \xrightarrow{p.s.} 0$ lorsque $n \to \infty$, où $S_n' = \sum_{k=1}^n Y_k'$.
        Les variables $Y_k'$ sont indépendantes car les $X_k$ sont indépendantes et la troncature et la centration sont des opérations appliquées individuellement à chaque $X_k$.
        De plus, $E[Y_k'] = E[Y_k - E[Y_k]] = E[Y_k] - E[Y_k] = 0$ pour tout $k \in \mathbb{N}^*$.
        Nous avons montré à la question 4.c que $\sum_{k=1}^\infty \frac{Var(Y_k)}{k^2} = \sum_{k=1}^\infty \frac{E[(Y_k')^2]}{k^2} < \infty$.
        Considérons la série $\sum_{k=1}^\infty \frac{Y_k'}{k}$. Les termes $\frac{Y_k'}{k}$ sont des variables aléatoires indépendantes et centrées (car $E[Y_k'/k] = E[Y_k']/k = 0$).
        La somme de leurs variances est $\sum_{k=1}^\infty Var\left(\frac{Y_k'}{k}\right) = \sum_{k=1}^\infty \frac{Var(Y_k')}{k^2}$.
        Puisque cette somme est finie (d'après 4.c), nous pouvons appliquer le théorème des trois séries de Kolmogorov. Ce théorème stipule que si $(Z_k)$ est une suite de variables aléatoires indépendantes, alors la série $\sum Z_k$ converge presque sûrement si et seulement si trois conditions sont remplies. Dans le cas où les $Z_k$ sont centrées et de variance finie, la convergence de $\sum Var(Z_k)$ est suffisante pour la convergence presque sûre de $\sum Z_k$.
        Ici, les variables $Z_k = \frac{Y_k'}{k}$ sont indépendantes, centrées, et $\sum_{k=1}^\infty Var\left(\frac{Y_k'}{k}\right) < \infty$.
        Par conséquent, la série $\sum_{k=1}^\infty \frac{Y_k'}{k}$ converge presque sûrement.
        Soit $T_n = \sum_{k=1}^n \frac{Y_k'}{k}$. Nous avons $T_n \xrightarrow{p.s.} T$ pour une variable aléatoire $T$ finie.
        Nous appliquons maintenant le lemme de Kronecker. Le lemme de Kronecker stipule que si une série $\sum_{k=1}^\infty a_k$ converge, alors $\frac{1}{n} \sum_{k=1}^n k a_k \xrightarrow{n \to \infty} 0$.
        En posant $a_k = \frac{Y_k'}{k}$, nous avons montré que $\sum_{k=1}^\infty a_k$ converge presque sûrement.
        Donc, pour presque tout $\omega$, la suite $a_k(\omega) = \frac{Y_k'(\omega)}{k}$ satisfait les conditions du lemme de Kronecker.
        Par conséquent, pour presque tout $\omega$:
        $\frac{1}{n} \sum_{k=1}^n k a_k(\omega) = \frac{1}{n} \sum_{k=1}^n k \frac{Y_k'(\omega)}{k} = \frac{1}{n} \sum_{k=1}^n Y_k'(\omega) \xrightarrow{n \to \infty} 0$.
        C'est-à-dire, $\frac{S_n'}{n} \xrightarrow{p.s.} 0$ lorsque $n \to \infty$.

5.  **Conclusion :**
    Nous avons la décomposition $X_k = Y_k + Z_k$ pour tout $k \in \mathbb{N}^*$.
    En sommant sur $k$ de 1 à $n$ et en divisant par $n$, nous obtenons :
    $\frac{S_n}{n} = \frac{1}{n} \sum_{k=1}^n X_k = \frac{1}{n} \sum_{k=1}^n Y_k + \frac{1}{n} \sum_{k=1}^n Z_k$.
    D'après la question 2.d, nous avons démontré que $\frac{1}{n} \sum_{k=1}^n Z_k \xrightarrow{p.s.} 0$.
    Il nous reste à analyser le terme $\frac{1}{n} \sum_{k=1}^n Y_k$.
    Nous pouvons réécrire ce terme en ajoutant et soustrayant l'espérance de $Y_k$:
    $\frac{1}{n} \sum_{k=1}^n Y_k = \frac{1}{n} \sum_{k=1}^n (Y_k - E[Y_k]) + \frac{1}{n} \sum_{k=1}^n E[Y_k]$.
    Le premier terme de cette somme est $\frac{1}{n} \sum_{k=1}^n Y_k' = \frac{S_n'}{n}$.
    D'après la question 4.d, nous avons montré que $\frac{S_n'}{n} \xrightarrow{p.s.} 0$.
    Il nous reste donc à évaluer la limite du second terme, $\frac{1}{n} \sum_{k=1}^n E[Y_k]$.
    D'après la question 3, nous savons que la suite des espérances $E[Y_k]$ converge vers $\mu$ lorsque $k \to \infty$.
    Par le théorème de Cesaro (ou théorème de la moyenne de Cesaro), si une suite de nombres réels $(a_k)_{k \in \mathbb{N}^*}$ converge vers une limite $L$, alors la suite de ses moyennes arithmétiques $\left(\frac{1}{n} \sum_{k=1}^n a_k\right)_{n \in \mathbb{N}^*}$ converge également vers $L$.
    En appliquant ce théorème à la suite $a_k = E[Y_k]$ et $L = \mu$, nous obtenons :
    $\frac{1}{n} \sum_{k=1}^n E[Y_k] \xrightarrow{n \to \infty} \mu$.
    En combinant tous ces résultats de convergence presque sûre :
    $\frac{S_n}{n} = \frac{1}{n} \sum_{k=1}^n (Y_k - E[Y_k]) + \frac{1}{n} \sum_{k=1}^n E[Y_k] + \frac{1}{n} \sum_{k=1}^n Z_k$.
    $\frac{S_n}{n} \xrightarrow{p.s.} 0 + \mu + 0$.
    Par conséquent, $\frac{S_n}{n} \xrightarrow{p.s.} \mu$ lorsque $n \to \infty$.
    Ceci achève la démonstration de la Loi Forte des Grands Nombres.