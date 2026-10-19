# Exercice 6 : Exploration de la LFGN : Variables Transformées et Pièges Potentiels
$\bigstar\bigstar\bigstar\star\star$

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes et identiquement distribuées (i.i.d.) suivant une loi de Bernoulli $\mathcal{B}(p)$ avec $p \in (0,1)$. Cela signifie que pour chaque $n$, $P(X_n=1) = p$ et $P(X_n=0) = 1-p$.

On définit une nouvelle suite de variables aléatoires $(Y_n)_{n \ge 1}$ par $Y_n = \frac{X_n}{1+X_n^2}$ pour tout $n \ge 1$.

1.  Montrer que la suite $(Y_n)_{n \ge 1}$ est une suite de variables aléatoires i.i.d.
2.  Calculer l'espérance $\mathbb{E}[Y_1]$.
3.  Énoncer la Loi Forte des Grands Nombres (LFGN) pour une suite de variables aléatoires i.i.d.
4.  En déduire la convergence presque sûre de la moyenne arithmétique $\frac{1}{N}\sum_{n=1}^N Y_n$ et déterminer sa limite.
5.  Considérons maintenant une suite $(Z_n)_{n \ge 1}$ définie par $Z_n = \frac{1}{X_n}$ pour tout $n \ge 1$ (en convenant que $1/0$ est infini). Expliquer pourquoi la LFGN ne peut pas être appliquée directement à la suite $(Z_n)_{n \ge 1}$ pour établir la convergence presque sûre de $\frac{1}{N}\sum_{n=1}^N Z_n$.

---

### Correction

1.  **Montrer que la suite $(Y_n)_{n \ge 1}$ est une suite de variables aléatoires i.i.d.**

    Soit $f(x) = \frac{x}{1+x^2}$ la fonction qui transforme $X_n$ en $Y_n$.
    Puisque les variables aléatoires $(X_n)_{n \ge 1}$ sont indépendantes, et que chaque $Y_n$ est une fonction déterministe de $X_n$ (c'est-à-dire $Y_n = f(X_n)$), alors les variables aléatoires $(Y_n)_{n \ge 1}$ sont également indépendantes.
    De plus, puisque les variables aléatoires $(X_n)_{n \ge 1}$ sont identiquement distribuées, et que la fonction $f$ est la même pour toutes les transformations, alors les variables aléatoires $(Y_n)_{n \ge 1}$ sont également identiquement distribuées.
    En effet, pour tout $n$, la loi de $Y_n$ est déterminée par la loi de $X_n$ et la fonction $f$. Comme la loi de $X_n$ est la même pour tout $n$, la loi de $Y_n$ est aussi la même pour tout $n$.
    Par conséquent, la suite $(Y_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes et identiquement distribuées (i.i.d.).

2.  **Calculer l'espérance $\mathbb{E}[Y_1]$.**

    La variable aléatoire $X_1$ suit une loi de Bernoulli $\mathcal{B}(p)$. Elle prend les valeurs $0$ et $1$ avec les probabilités $P(X_1=0) = 1-p$ et $P(X_1=1) = p$.
    Calculons les valeurs que $Y_1$ peut prendre :
    Si $X_1 = 0$, alors $Y_1 = \frac{0}{1+0^2} = \frac{0}{1} = 0$.
    Si $X_1 = 1$, alors $Y_1 = \frac{1}{1+1^2} = \frac{1}{2}$.
    Ainsi, $Y_1$ est une variable aléatoire discrète qui prend la valeur $0$ avec probabilité $P(Y_1=0) = P(X_1=0) = 1-p$, et la valeur $1/2$ avec probabilité $P(Y_1=1/2) = P(X_1=1) = p$.
    L'espérance de $Y_1$ est donnée par :
    $\mathbb{E}[Y_1] = 0 \cdot P(Y_1=0) + \frac{1}{2} \cdot P(Y_1=1/2)$
    $\mathbb{E}[Y_1] = 0 \cdot (1-p) + \frac{1}{2} \cdot p$
    $\mathbb{E}[Y_1] = \frac{p}{2}$.
    L'espérance $\mathbb{E}[Y_1]$ est finie, car $p \in (0,1)$, donc $\frac{p}{2}$ est un nombre réel fini.

3.  **Énoncer la Loi Forte des Grands Nombres (LFGN) pour une suite de variables aléatoires i.i.d.**

    Soit $(V_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes et identiquement distribuées (i.i.d.). Si l'espérance $\mathbb{E}[V_1]$ existe et est finie (c'est-à-dire $\mathbb{E}[|V_1|] < \infty$), alors la moyenne arithmétique des $N$ premières variables converge presque sûrement vers cette espérance lorsque $N$ tend vers l'infini.
    Formellement, si $\mathbb{E}[V_1] = \mu$, alors :
    $$ \frac{1}{N}\sum_{n=1}^N V_n \xrightarrow{p.s.} \mu \quad \text{quand } N \to \infty $$
    où $\xrightarrow{p.s.}$ signifie "converge presque sûrement".

4.  **En déduire la convergence presque sûre de la moyenne arithmétique $\frac{1}{N}\sum_{n=1}^N Y_n$ et déterminer sa limite.**

    Nous avons montré à la question 1 que la suite $(Y_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes et identiquement distribuées (i.i.d.).
    Nous avons calculé à la question 2 que l'espérance $\mathbb{E}[Y_1] = \frac{p}{2}$, qui est une valeur finie.
    Toutes les conditions de la Loi Forte des Grands Nombres sont donc satisfaites pour la suite $(Y_n)_{n \ge 1}$.
    En appliquant la LFGN, nous pouvons conclure que la moyenne arithmétique des $Y_n$ converge presque sûrement vers l'espérance de $Y_1$.
    Par conséquent :
    $$ \frac{1}{N}\sum_{n=1}^N Y_n \xrightarrow{p.s.} \mathbb{E}[Y_1] \quad \text{quand } N \to \infty $$
    $$ \frac{1}{N}\sum_{n=1}^N Y_n \xrightarrow{p.s.} \frac{p}{2} \quad \text{quand } N \to \infty $$
    La limite de la moyenne arithmétique est $\frac{p}{2}$.

5.  **Expliquer pourquoi la LFGN ne peut pas être appliquée directement à la suite $(Z_n)_{n \ge 1}$ pour établir la convergence presque sûre de $\frac{1}{N}\sum_{n=1}^N Z_n$.**

    La suite $(Z_n)_{n \ge 1}$ est définie par $Z_n = \frac{1}{X_n}$.
    Puisque $(X_n)_{n \ge 1}$ sont i.i.d., les variables $(Z_n)_{n \ge 1}$ sont également i.i.d. (par le même raisonnement qu'à la question 1).
    Pour appliquer la Loi Forte des Grands Nombres, la condition essentielle est que l'espérance de $Z_1$ doit exister et être finie, c'est-à-dire $\mathbb{E}[|Z_1|] < \infty$.
    La variable $X_1$ suit une loi de Bernoulli $\mathcal{B}(p)$. Elle prend la valeur $0$ avec probabilité $1-p$ et la valeur $1$ avec probabilité $p$.
    Considérons les valeurs que $Z_1$ peut prendre :
    Si $X_1 = 1$, alors $Z_1 = \frac{1}{1} = 1$.
    Si $X_1 = 0$, alors $Z_1 = \frac{1}{0}$, qui est défini comme infini.
    Puisque $p \in (0,1)$, la probabilité $P(X_1=0) = 1-p$ est strictement positive. Cela signifie que $Z_1$ prend la valeur infinie avec une probabilité non nulle.
    L'espérance de $Z_1$ est donnée par :
    $\mathbb{E}[Z_1] = 1 \cdot P(Z_1=1) + \infty \cdot P(Z_1=\infty)$
    $\mathbb{E}[Z_1] = 1 \cdot p + \infty \cdot (1-p)$.
    Étant donné que $1-p > 0$ (car $p < 1$), le terme $\infty \cdot (1-p)$ est égal à $\infty$.
    Par conséquent, $\mathbb{E}[Z_1] = p + \infty = \infty$.
    L'espérance de $Z_1$ n'est pas finie. La condition fondamentale de la Loi Forte des Grands Nombres n'est donc pas satisfaite.
    En conséquence, la LFGN ne peut pas être appliquée directement à la suite $(Z_n)_{n \ge 1}$ pour établir la convergence presque sûre de $\frac{1}{N}\sum_{n=1}^N Z_n$ vers une limite finie.