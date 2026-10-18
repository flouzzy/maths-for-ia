# Exercice 5 : L'Écho de la Moyenne : Convergence d'une Statistique Non Linéaire
$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires réelles indépendantes et identiquement distribuées (i.i.d.). On suppose que $\mathbb{E}[X_1] = \mu$ et $\text{Var}(X_1) = \sigma^2$ sont finis.

On définit la moyenne empirique $Y_n$ pour $n \ge 1$ par :
$$ Y_n = \frac{1}{n} \sum_{k=1}^n X_k $$

On s'intéresse à la convergence d'une statistique transformée $Z_n$, définie pour $n \ge 1$ par :
$$ Z_n = \frac{Y_n^2}{1 + Y_n^2} $$

Démontrer que la suite de variables aléatoires $(Z_n)_{n \ge 1}$ converge presque sûrement vers une limite que l'on déterminera.

---

**Correction :**

Nous allons démontrer la convergence presque sûre de la suite $(Z_n)_{n \ge 1}$ en utilisant la Loi Forte des Grands Nombres (LFGN) et le théorème de l'application continue.

1.  **Application de la Loi Forte des Grands Nombres (LFGN) à $Y_n$ :**
    La suite $(X_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes et identiquement distribuées.
    De plus, l'énoncé stipule que l'espérance $\mathbb{E}[X_1] = \mu$ est finie.
    Selon la Loi Forte des Grands Nombres, pour une suite de variables aléatoires i.i.d. ayant une espérance finie, la moyenne empirique converge presque sûrement vers cette espérance.
    Ainsi, nous avons :
    $$ Y_n = \frac{1}{n} \sum_{k=1}^n X_k \xrightarrow{p.s.} \mathbb{E}[X_1] = \mu $$
    Cela signifie qu'il existe un ensemble $\Omega_0 \subset \Omega$ de probabilité 1 (c'est-à-dire $\mathbb{P}(\Omega_0) = 1$) tel que pour tout $\omega \in \Omega_0$, la suite numérique $(Y_n(\omega))_{n \ge 1}$ converge vers $\mu$.

2.  **Définition de la fonction de transformation :**
    Considérons la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par :
    $$ f(x) = \frac{x^2}{1 + x^2} $$
    La variable aléatoire $Z_n$ peut être exprimée comme $Z_n = f(Y_n)$.

3.  **Analyse de la continuité de la fonction $f(x)$ :**
    Pour déterminer si $f(x)$ est continue, nous pouvons examiner sa dérivée ou simplement noter qu'elle est un quotient de polynômes.
    Le dénominateur $1 + x^2$ est toujours strictement positif pour tout $x \in \mathbb{R}$ (en effet, $x^2 \ge 0$, donc $1 + x^2 \ge 1$).
    Le numérateur $x^2$ est un polynôme et donc continu sur $\mathbb{R}$.
    Le dénominateur $1 + x^2$ est un polynôme et donc continu sur $\mathbb{R}$.
    Puisque le dénominateur ne s'annule jamais, la fonction $f(x)$ est continue sur tout $\mathbb{R}$.

4.  **Application du Théorème de l'Application Continue pour la convergence presque sûre :**
    Le Théorème de l'Application Continue (ou Continuous Mapping Theorem) stipule que si une suite de variables aléatoires $(A_n)_{n \ge 1}$ converge presque sûrement vers une constante $a$, et si $g$ est une fonction continue en $a$, alors la suite $(g(A_n))_{n \ge 1}$ converge presque sûrement vers $g(a)$.
    Dans notre cas :
    *   La suite de variables aléatoires est $(Y_n)_{n \ge 1}$.
    *   Elle converge presque sûrement vers la constante $\mu$.
    *   La fonction $f(x)$ est continue sur $\mathbb{R}$, et donc en particulier continue au point $\mu$.

    Par conséquent, en appliquant le Théorème de l'Application Continue, nous pouvons affirmer que la suite $(f(Y_n))_{n \ge 1}$ converge presque sûrement vers $f(\mu)$.

5.  **Détermination de la limite :**
    La limite presque sûre de $Z_n$ est $f(\mu)$. Calculons cette valeur :
    $$ \lim_{n \to \infty} Z_n = f(\mu) = \frac{\mu^2}{1 + \mu^2} $$
    Cette convergence est presque sûre.

En conclusion, la suite de variables aléatoires $(Z_n)_{n \ge 1}$ converge presque sûrement vers la limite $\frac{\mu^2}{1 + \mu^2}$.