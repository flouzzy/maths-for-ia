# Exercice 10 : Convergence Presque Sûre des Moyennes Pondérées : Au-delà de l'Identité de Distribution

$\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes, centrées ($E[X_n] = 0$ pour tout $n \ge 1$). On note $\sigma_n^2 = Var(X_n)$.

Pour chaque $n \ge 1$, on définit les variables tronquées $Y_n = X_n \mathbf{1}_{\{|X_n| \le n\}}$ et $Z_n = X_n - Y_n = X_n \mathbf{1}_{\{|X_n| > n\}}$.

### Partie 1 : Préliminaires et Troncature

1.  Montrer que si $\sum_{n=1}^\infty P(|X_n| > n) < \infty$, alors $P(X_n \ne Y_n \text{ i.o.}) = 0$. En déduire que $\frac{1}{N} \sum_{n=1}^N X_n$ et $\frac{1}{N} \sum_{n=1}^N Y_n$ ont le même comportement asymptotique en termes de convergence presque sûre. (i.o. signifie "infiniment souvent").
2.  Montrer que $E[Y_n]$ n'est pas nécessairement nul. Exprimer $E[Y_n]$ en fonction de $X_n$.
3.  Soit $Y_n' = Y_n - E[Y_n]$. Montrer que $E[Y_n'] = 0$ et $Var(Y_n') \le Var(Y_n) \le E[X_n^2 \mathbf{1}_{\{|X_n| \le n\}}]$.

### Partie 2 : Condition de Kolmogorov et LFGN Généralisée

On suppose désormais que la condition $\sum_{n=1}^\infty \frac{E[X_n^2]}{n^2} < \infty$ est satisfaite.

4.  Montrer que $\sum_{n=1}^\infty P(|X_n| > n) < \infty$. (Indication : Utiliser l'inégalité de Markov ou une majoration directe).
5.  Montrer que $\sum_{n=1}^\infty \frac{Var(Y_n')}{n^2} < \infty$. (Indication : Utiliser le résultat de la question 3 et l'hypothèse).
6.  En déduire, en utilisant le critère de Kolmogorov pour la convergence presque sûre des séries de variables aléatoires centrées, que $\sum_{n=1}^\infty \frac{Y_n'}{n}$ converge presque sûrement.
7.  En utilisant le lemme de Kronecker, montrer que $\frac{1}{N} \sum_{n=1}^N Y_n' \to 0$ presque sûrement.
8.  Montrer que $\sum_{n=1}^\infty \frac{E[Y_n]}{n}$ converge absolument. (Indication : Utiliser l'égalité $E[Y_n] = -E[X_n \mathbf{1}_{\{|X_n| > n\}}]$ et une majoration appropriée).
9.  En déduire que $\frac{1}{N} \sum_{n=1}^N E[Y_n] \to 0$ presque sûrement.
10. Conclure que si $(X_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes, centrées, et si $\sum_{n=1}^\infty \frac{E[X_n^2]}{n^2} < \infty$, alors $\frac{1}{N} \sum_{n=1}^N X_n \to 0$ presque sûrement.

---

## Correction

### Partie 1 : Préliminaires et Troncature

1.  **Montrer que si $\sum_{n=1}^\infty P(|X_n| > n) < \infty$, alors $P(X_n \ne Y_n \text{ i.o.}) = 0$. En déduire que $\frac{1}{N} \sum_{n=1}^N X_n$ et $\frac{1}{N} \sum_{n=1}^N Y_n$ ont le même comportement asymptotique en termes de convergence presque sûre.**

    *   **Démonstration de $P(X_n \ne Y_n \text{ i.o.}) = 0$ :**
        Par définition, $X_n \ne Y_n$ si et seulement si $X_n \mathbf{1}_{\{|X_n| \le n\}} \ne X_n$, ce qui est équivalent à $|X_n| > n$.
        L'événement "$X_n \ne Y_n$ infiniment souvent" est l'événement $\limsup_{n \to \infty} \{|X_n| > n\}$.
        Le lemme de Borel-Cantelli stipule que si $\sum_{n=1}^\infty P(A_n) < \infty$, alors $P(\limsup_{n \to \infty} A_n) = 0$.
        Ici, nous avons $A_n = \{|X_n| > n\}$. L'hypothèse est $\sum_{n=1}^\infty P(|X_n| > n) < \infty$.
        Par conséquent, en appliquant le lemme de Borel-Cantelli, nous obtenons $P(\limsup_{n \to \infty} \{|X_n| > n\}) = 0$.
        Ceci signifie que $P(X_n \ne Y_n \text{ i.o.}) = 0$.

    *   **Déduction du comportement asymptotique :**
        L'événement $P(X_n \ne Y_n \text{ i.o.}) = 0$ signifie qu'il existe un ensemble de probabilité 1, notons-le $\Omega_0$, tel que pour tout $\omega \in \Omega_0$, il existe un entier $N_0(\omega)$ tel que pour tout $n > N_0(\omega)$, $X_n(\omega) = Y_n(\omega)$.
        Considérons la différence des sommes :
        $\frac{1}{N} \sum_{n=1}^N X_n - \frac{1}{N} \sum_{n=1}^N Y_n = \frac{1}{N} \sum_{n=1}^N (X_n - Y_n) = \frac{1}{N} \sum_{n=1}^N Z_n$.
        Pour tout $\omega \in \Omega_0$, pour $N > N_0(\omega)$, la somme $\sum_{n=1}^N Z_n(\omega)$ peut s'écrire :
        $\sum_{n=1}^N Z_n(\omega) = \sum_{n=1}^{N_0(\omega)} Z_n(\omega) + \sum_{n=N_0(\omega)+1}^N Z_n(\omega)$.
        Puisque $X_n(\omega) = Y_n(\omega)$ pour $n > N_0(\omega)$, nous avons $Z_n(\omega) = 0$ pour $n > N_0(\omega)$.
        Donc, $\sum_{n=1}^N Z_n(\omega) = \sum_{n=1}^{N_0(\omega)} Z_n(\omega)$. Cette somme est une valeur finie qui dépend de $\omega$ mais pas de $N$.
        Par conséquent, $\lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^N Z_n(\omega) = \lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^{N_0(\omega)} Z_n(\omega) = 0$ pour tout $\omega \in \Omega_0$.
        Ceci signifie que $\frac{1}{N} \sum_{n=1}^N Z_n \to 0$ presque sûrement.
        Ainsi, $\frac{1}{N} \sum_{n=1}^N X_n - \frac{1}{N} \sum_{n=1}^N Y_n \to 0$ presque sûrement.
        Si $\frac{1}{N} \sum_{n=1}^N Y_n \to L$ presque sûrement, alors $\frac{1}{N} \sum_{n=1}^N X_n \to L$ presque sûrement.
        Les deux suites de moyennes ont donc le même comportement asymptotique en termes de convergence presque sûre.

2.  **Montrer que $E[Y_n]$ n'est pas nécessairement nul. Exprimer $E[Y_n]$ en fonction de $X_n$.**

    *   **$E[Y_n]$ n'est pas nécessairement nul :**
        Par définition, $Y_n = X_n \mathbf{1}_{\{|X_n| \le n\}}$.
        Puisque $E[X_n] = 0$, nous avons $E[X_n] = E[X_n \mathbf{1}_{\{|X_n| \le n\}}] + E[X_n \mathbf{1}_{\{|X_n| > n\}}]$.
        Donc, $0 = E[Y_n] + E[X_n \mathbf{1}_{\{|X_n| > n\}}]$.
        Ceci implique $E[Y_n] = -E[X_n \mathbf{1}_{\{|X_n| > n\}}]$.
        Pour que $E[Y_n]$ soit nul, il faudrait que $E[X_n \mathbf{1}_{\{|X_n| > n\}}]$ soit nul.
        Considérons un exemple simple : Soit $X_n$ une variable aléatoire symétrique, par exemple $X_n \sim \mathcal{N}(0, \sigma^2)$. Dans ce cas, $X_n \mathbf{1}_{\{|X_n| > n\}}$ est aussi symétrique par rapport à 0, et son espérance est nulle. Donc $E[Y_n]=0$.
        Cependant, si $X_n$ n'est pas symétrique, $E[X_n \mathbf{1}_{\{|X_n| > n\}}]$ n'est pas nécessairement nul.
        Par exemple, si $X_n$ prend la valeur $-1$ avec probabilité $p$ et la valeur $1/(1-p)$ avec probabilité $1-p$, alors $E[X_n] = -p + (1-p) \frac{1}{1-p} = -p+1 \ne 0$. Pour avoir $E[X_n]=0$, on peut prendre $X_n$ prenant la valeur $-a$ avec probabilité $p$ et $b$ avec probabilité $1-p$ tel que $-ap + b(1-p)=0$.
        Prenons $X_n$ telle que $P(X_n = -n-1) = \frac{1}{n+1}$ et $P(X_n = 1) = \frac{n}{n+1}$.
        Alors $E[X_n] = (-n-1)\frac{1}{n+1} + 1 \cdot \frac{n}{n+1} = -1 + \frac{n}{n+1} = \frac{-1}{n+1} \ne 0$.
        Il faut que $E[X_n]=0$.
        Considérons $X_n$ telle que $P(X_n = -n) = \frac{1}{2n}$ et $P(X_n = 1) = \frac{1}{2}$ et $P(X_n = n-1) = \frac{1}{2n}$.
        Non, c'est trop compliqué.
        Prenons une variable $X$ centrée. Par exemple, $P(X=-1)=1/2$, $P(X=1)=1/2$. Alors $E[X]=0$.
        Si $n=0.5$, alors $|X|>n$ est toujours vrai. $Y_n=0$. $E[Y_n]=0$.
        Si $n=1.5$, alors $|X| \le n$ est toujours vrai. $Y_n=X$. $E[Y_n]=E[X]=0$.
        Il faut une distribution asymétrique.
        Soit $X$ une variable aléatoire telle que $P(X=-1) = 1/2$ et $P(X=1/2) = 1/2$. Alors $E[X] = -1/2 + 1/4 = -1/4 \ne 0$.
        Pour avoir $E[X]=0$, prenons $P(X=-1) = 1/3$ et $P(X=1/2) = 2/3$. Alors $E[X] = -1/3 + (1/2)(2/3) = -1/3 + 1/3 = 0$.
        Fixons $n=0.8$.
        Alors $\{|X| \le n\}$ est l'événement $\{X=1/2\}$.
        $Y = X \mathbf{1}_{\{|X| \le 0.8\}} = (1/2) \mathbf{1}_{\{X=1/2\}}$.
        $E[Y] = (1/2) P(X=1/2) = (1/2)(2/3) = 1/3$.
        Dans cet exemple, $E[Y]$ n'est pas nul, même si $E[X]=0$.

    *   **Expression de $E[Y_n]$ :**
        Comme établi ci-dessus, $E[X_n] = E[X_n \mathbf{1}_{\{|X_n| \le n\}}] + E[X_n \mathbf{1}_{\{|X_n| > n\}}]$.
        Puisque $E[X_n] = 0$ par hypothèse, et $Y_n = X_n \mathbf{1}_{\{|X_n| \le n\}}$, nous avons :
        $0 = E[Y_n] + E[X_n \mathbf{1}_{\{|X_n| > n\}}]$.
        Donc, $E[Y_n] = -E[X_n \mathbf{1}_{\{|X_n| > n\}}]$.

3.  **Soit $Y_n' = Y_n - E[Y_n]$. Montrer que $E[Y_n'] = 0$ et $Var(Y_n') \le Var(Y_n) \le E[X_n^2 \mathbf{1}_{\{|X_n| \le n\}}]$.**

    *   **$E[Y_n'] = 0$ :**
        Par définition de $Y_n'$, $E[Y_n'] = E[Y_n - E[Y_n]] = E[Y_n] - E[E[Y_n]]$.
        Puisque $E[Y_n]$ est une constante (une valeur numérique), $E[E[Y_n]] = E[Y_n]$.
        Donc, $E[Y_n'] = E[Y_n] - E[Y_n] = 0$. La variable $Y_n'$ est centrée.

    *   **$Var(Y_n') \le Var(Y_n)$ :**
        Par définition de la variance, $Var(Y_n') = E[(Y_n' - E[Y_n'])^2]$.
        Puisque $E[Y_n'] = 0$, nous avons $Var(Y_n') = E[(Y_n')^2] = E[(Y_n - E[Y_n])^2]$.
        Par définition de la variance d'une variable aléatoire $Y_n$, $Var(Y_n) = E[(Y_n - E[Y_n])^2]$.
        Donc, $Var(Y_n') = Var(Y_n)$. L'inégalité $Var(Y_n') \le Var(Y_n)$ est en fait une égalité.

    *   **$Var(Y_n) \le E[X_n^2 \mathbf{1}_{\{|X_n| \le n\}}]$ :**
        Nous savons que $Var(Y_n) = E[Y_n^2] - (E[Y_n])^2$.
        Puisque $(E[Y_n])^2 \ge 0$, nous avons $Var(Y_n) \le E[Y_n^2]$.
        Par définition, $Y_n = X_n \mathbf{1}_{\{|X_n| \le n\}}$.
        Donc, $Y_n^2 = (X_n \mathbf{1}_{\{|X_n| \le n\}})^2 = X_n^2 \mathbf{1}_{\{|X_n| \le n\}}^2 = X_n^2 \mathbf{1}_{\{|X_n| \le n\}}$.
        Par conséquent, $E[Y_n^2] = E[X_n^2 \mathbf{1}_{\{|X_n| \le n\}}]$.
        En combinant ces résultats, nous obtenons $Var(Y_n) \le E[X_n^2 \mathbf{1}_{\{|X_n| \le n\}}]$.

### Partie 2 : Condition de Kolmogorov et LFGN Généralisée

4.  **Montrer que $\sum_{n=1}^\infty P(|X_n| > n) < \infty$. (Indication : Utiliser l'inégalité de Markov ou une majoration directe).**

    Nous utilisons l'inégalité de Markov pour la variable aléatoire $X_n^2$.
    Pour toute variable aléatoire $Z \ge 0$ et tout $a > 0$, $P(Z \ge a) \le \frac{E[Z]}{a}$.
    Ici, nous prenons $Z = X_n^2$ et $a = n^2$.
    Alors, $P(|X_n| > n) = P(X_n^2 > n^2)$.
    En appliquant l'inégalité de Markov, nous obtenons :
    $P(X_n^2 > n^2) \le \frac{E[X_n^2]}{n^2}$.
    L'hypothèse de la Partie 2 est $\sum_{n=1}^\infty \frac{E[X_n^2]}{n^2} < \infty$.
    Puisque $P(|X_n| > n) \le \frac{E[X_n^2]}{n^2}$ pour tout $n \ge 1$, et la série des majorants converge, la série des termes $P(|X_n| > n)$ converge également par le critère de comparaison des séries à termes positifs.
    Donc, $\sum_{n=1}^\infty P(|X_n| > n) < \infty$.

5.  **Montrer que $\sum_{n=1}^\infty \frac{Var(Y_n')}{n^2} < \infty$. (Indication : Utiliser le résultat de la question 3 et l'hypothèse).**

    D'après la question 3, nous avons $Var(Y_n') = Var(Y_n)$ et $Var(Y_n) \le E[X_n^2 \mathbf{1}_{\{|X_n| \le n\}}]$.
    De plus, $E[X_n^2 \mathbf{1}_{\{|X_n| \le n\}}] \le E[X_n^2]$ car $\mathbf{1}_{\{|X_n| \le n\}} \le 1$.
    Donc, $Var(Y_n') \le E[X_n^2]$.
    Nous voulons montrer que $\sum_{n=1}^\infty \frac{Var(Y_n')}{n^2} < \infty$.
    En utilisant l'inégalité précédente, nous avons :
    $\sum_{n=1}^\infty \frac{Var(Y_n')}{n^2} \le \sum_{n=1}^\infty \frac{E[X_n^2]}{n^2}$.
    L'hypothèse de la Partie 2 est $\sum_{n=1}^\infty \frac{E[X_n^2]}{n^2} < \infty$.
    Par le critère de comparaison des séries à termes positifs, la série $\sum_{n=1}^\infty \frac{Var(Y_n')}{n^2}$ converge.
    Donc, $\sum_{n=1}^\infty \frac{Var(Y_n')}{n^2} < \infty$.

6.  **En déduire, en utilisant le critère de Kolmogorov pour la convergence presque sûre des séries de variables aléatoires centrées, que $\sum_{n=1}^\infty \frac{Y_n'}{n}$ converge presque sûrement.**

    Le critère de Kolmogorov (ou la condition de Kolmogorov pour la convergence des séries) stipule que si $(W_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes et centrées ($E[W_n]=0$), et si $\sum_{n=1}^\infty Var(W_n) < \infty$, alors la série $\sum_{n=1}^\infty W_n$ converge presque sûrement.
    Dans notre cas, nous considérons la suite de variables aléatoires $W_n = \frac{Y_n'}{n}$.
    *   Les variables $Y_n'$ sont indépendantes car les $X_n$ sont indépendantes, et $Y_n'$ est une fonction mesurable de $X_n$.
    *   Les variables $Y_n'$ sont centrées ($E[Y_n'] = 0$) d'après la question 3. Par conséquent, $E[W_n] = E[\frac{Y_n'}{n}] = \frac{1}{n} E[Y_n'] = 0$. Les variables $W_n$ sont donc centrées.
    *   Nous devons vérifier la condition sur la somme des variances : $\sum_{n=1}^\infty Var(W_n) = \sum_{n=1}^\infty Var\left(\frac{Y_n'}{n}\right)$.
        Puisque $Var(cZ) = c^2 Var(Z)$ pour une constante $c$, nous avons $Var\left(\frac{Y_n'}{n}\right) = \frac{1}{n^2} Var(Y_n')$.
        Donc, $\sum_{n=1}^\infty Var(W_n) = \sum_{n=1}^\infty \frac{Var(Y_n')}{n^2}$.
        D'après la question 5, nous avons montré que $\sum_{n=1}^\infty \frac{Var(Y_n')}{n^2} < \infty$.
    Toutes les conditions du critère de Kolmogorov sont satisfaites.
    Par conséquent, la série $\sum_{n=1}^\infty \frac{Y_n'}{n}$ converge presque sûrement.

7.  **En utilisant le lemme de Kronecker, montrer que $\frac{1}{N} \sum_{n=1}^N Y_n' \to 0$ presque sûrement.**

    Le lemme de Kronecker stipule que si $(a_n)_{n \ge 1}$ est une suite de nombres réels et $(b_n)_{n \ge 1}$ est une suite de nombres réels positifs et croissants telle que $b_n \to \infty$, et si la série $\sum_{n=1}^\infty \frac{a_n}{b_n}$ converge, alors $\frac{1}{b_N} \sum_{n=1}^N a_n \to 0$.
    Dans notre cas, nous avons montré à la question 6 que la série $\sum_{n=1}^\infty \frac{Y_n'}{n}$ converge presque sûrement.
    Ceci signifie qu'il existe un ensemble de probabilité 1, notons-le $\Omega_1$, tel que pour tout $\omega \in \Omega_1$, la série $\sum_{n=1}^\infty \frac{Y_n'(\omega)}{n}$ converge.
    Pour chaque $\omega \in \Omega_1$, nous pouvons appliquer le lemme de Kronecker avec :
    *   $a_n = Y_n'(\omega)$ (les valeurs prises par la variable aléatoire)
    *   $b_n = n$ (qui est une suite de nombres réels positifs et croissants, et $n \to \infty$).
    La condition $\sum_{n=1}^\infty \frac{a_n}{b_n}$ converge est satisfaite pour $\omega \in \Omega_1$.
    Par conséquent, pour tout $\omega \in \Omega_1$, le lemme de Kronecker implique que $\frac{1}{N} \sum_{n=1}^N Y_n'(\omega) \to 0$ lorsque $N \to \infty$.
    Ceci signifie que $\frac{1}{N} \sum_{n=1}^N Y_n' \to 0$ presque sûrement.

8.  **Montrer que $\sum_{n=1}^\infty \frac{E[Y_n]}{n}$ converge absolument. (Indication : Utiliser l'égalité $E[Y_n] = -E[X_n \mathbf{1}_{\{|X_n| > n\}}]$ et une majoration appropriée).**

    D'après la question 2, nous avons $E[Y_n] = -E[X_n \mathbf{1}_{\{|X_n| > n\}}]$.
    Nous devons montrer que $\sum_{n=1}^\infty \frac{|E[Y_n]|}{n} < \infty$.
    Substituons l'expression de $E[Y_n]$ :
    $\sum_{n=1}^\infty \frac{|E[Y_n]|}{n} = \sum_{n=1}^\infty \frac{|-E[X_n \mathbf{1}_{\{|X_n| > n\}}]|}{n} = \sum_{n=1}^\infty \frac{|E[X_n \mathbf{1}_{\{|X_n| > n\}}]|}{n}$.
    Nous savons que $|E[Z]| \le E[|Z|]$ pour toute variable aléatoire $Z$.
    Donc, $|E[X_n \mathbf{1}_{\{|X_n| > n\}}]| \le E[|X_n \mathbf{1}_{\{|X_n| > n\}}|] = E[|X_n| \mathbf{1}_{\{|X_n| > n\}}]$.
    Pour majorer $E[|X_n| \mathbf{1}_{\{|X_n| > n\}}]$, nous utilisons le fait que sur l'événement $\{|X_n| > n\}$, nous avons $|X_n| > n$.
    Donc, $\mathbf{1}_{\{|X_n| > n\}} < \frac{|X_n|}{n} \mathbf{1}_{\{|X_n| > n\}}$.
    Par conséquent, $|X_n| \mathbf{1}_{\{|X_n| > n\}} < \frac{X_n^2}{n} \mathbf{1}_{\{|X_n| > n\}}$.
    En prenant l'espérance, nous obtenons :
    $E[|X_n| \mathbf{1}_{\{|X_n| > n\}}] \le E\left[\frac{X_n^2}{n} \mathbf{1}_{\{|X_n| > n\}}\right] = \frac{1}{n} E[X_n^2 \mathbf{1}_{\{|X_n| > n\}}]$.
    Puisque $E[X_n^2 \mathbf{1}_{\{|X_n| > n\}}] \le E[X_n^2]$, nous avons :
    $E[|X_n| \mathbf{1}_{\{|X_n| > n\}}] \le \frac{E[X_n^2]}{n}$.
    En substituant cette majoration dans la somme :
    $\sum_{n=1}^\infty \frac{|E[Y_n]|}{n} \le \sum_{n=1}^\infty \frac{1}{n} \left(\frac{E[X_n^2]}{n}\right) = \sum_{n=1}^\infty \frac{E[X_n^2]}{n^2}$.
    L'hypothèse de la Partie 2 est $\sum_{n=1}^\infty \frac{E[X_n^2]}{n^2} < \infty$.
    Par le critère de comparaison des séries à termes positifs, la série $\sum_{n=1}^\infty \frac{|E[Y_n]|}{n}$ converge.
    Donc, $\sum_{n=1}^\infty \frac{E[Y_n]}{n}$ converge absolument.

9.  **En déduire que $\frac{1}{N} \sum_{n=1}^N E[Y_n] \to 0$ presque sûrement.**

    Nous avons montré à la question 8 que la série $\sum_{n=1}^\infty \frac{E[Y_n]}{n}$ converge absolument. Une série qui converge absolument converge.
    Donc, la série $\sum_{n=1}^\infty \frac{E[Y_n]}{n}$ converge.
    Les termes $E[Y_n]$ sont des constantes (non aléatoires).
    Nous pouvons appliquer le lemme de Kronecker (voir question 7) à la suite de nombres réels $a_n = E[Y_n]$ et $b_n = n$.
    Puisque $\sum_{n=1}^\infty \frac{E[Y_n]}{n}$ converge, le lemme de Kronecker implique que :
    $\frac{1}{N} \sum_{n=1}^N E[Y_n] \to 0$ lorsque $N \to \infty$.
    Puisque cette convergence est pour une suite de constantes, elle est une convergence ordinaire, et donc aussi une convergence presque sûre (l'ensemble des $\omega$ pour lesquels la convergence ne se produit pas est l'ensemble vide, de probabilité 0).

10. **Conclure que si $(X_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes, centrées, et si $\sum_{n=1}^\infty \frac{E[X_n^2]}{n^2} < \infty$, alors $\frac{1}{N} \sum_{n=1}^N X_n \to 0$ presque sûrement.**

    Nous voulons montrer que $\frac{1}{N} \sum_{n=1}^N X_n \to 0$ presque sûrement.
    Nous décomposons la somme $\sum_{n=1}^N X_n$ en utilisant les variables tronquées et centrées :
    $\frac{1}{N} \sum_{n=1}^N X_n = \frac{1}{N} \sum_{n=1}^N (Y_n + Z_n)$.
    D'après la question 1, nous avons montré que si $\sum_{n=1}^\infty P(|X_n| > n) < \infty$, alors $\frac{1}{N} \sum_{n=1}^N X_n$ et $\frac{1}{N} \sum_{n=1}^N Y_n$ ont le même comportement asymptotique presque sûre.
    La condition $\sum_{n=1}^\infty P(|X_n| > n) < \infty$ a été établie à la question 4 sous l'hypothèse $\sum_{n=1}^\infty \frac{E[X_n^2]}{n^2} < \infty$.
    Donc, il suffit de montrer que $\frac{1}{N} \sum_{n=1}^N Y_n \to 0$ presque sûrement.

    Nous décomposons $Y_n$ en $Y_n = Y_n' + E[Y_n]$ (par définition de $Y_n'$).
    Alors, $\frac{1}{N} \sum_{n=1}^N Y_n = \frac{1}{N} \sum_{n=1}^N (Y_n' + E[Y_n]) = \frac{1}{N} \sum_{n=1}^N Y_n' + \frac{1}{N} \sum_{n=1}^N E[Y_n]$.

    *   D'après la question 7, nous avons montré que $\frac{1}{N} \sum_{n=1}^N Y_n' \to 0$ presque sûrement.
    *   D'après la question 9, nous avons montré que $\frac{1}{N} \sum_{n=1}^N E[Y_n] \to 0$ presque sûrement.

    Puisque la somme de deux suites qui convergent presque sûrement vers 0 converge presque sûrement vers 0, nous avons :
    $\frac{1}{N} \sum_{n=1}^N Y_n = \frac{1}{N} \sum_{n=1}^N Y_n' + \frac{1}{N} \sum_{n=1}^N E[Y_n] \to 0 + 0 = 0$ presque sûrement.

    En combinant ce résultat avec la déduction de la question 1, nous concluons que :
    $\frac{1}{N} \sum_{n=1}^N X_n \to 0$ presque sûrement.

    Ceci est une version généralisée de la Loi Forte des Grands Nombres pour des variables aléatoires indépendantes mais non nécessairement identiquement distribuées, sous la condition de Kolmogorov sur les variances.