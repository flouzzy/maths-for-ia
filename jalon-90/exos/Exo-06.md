\subsection*{Exercice 6 : Convergence en loi d'un maximum \quad $\bigstar\bigstar\bigstar\star\star$}

Soit $(X_i)_{1 \le i \le n}$ des variables aléatoires indépendantes et identiquement distribuées selon la loi uniforme sur $[0, \theta]$.
Soit $M_n = \max(X_1, X_2, \dots, X_n)$.
Montrer que $n(\theta - M_n)$ converge en loi vers une variable exponentielle que l'on précisera.

**Correction :**
Exprimons la fonction de répartition de $M_n$. Pour tout $x \in [0, \theta]$ :
$F_{M_n}(x) = \mathbb{P}(M_n \le x) = \mathbb{P}(X_1 \le x, \dots, X_n \le x) = \mathbb{P}(X_1 \le x)^n = \left(\frac{x}{\theta}\right)^n$.
Soit $Y_n = n(\theta - M_n)$. Calculons sa fonction de répartition $F_{Y_n}(y)$ pour un $y \ge 0$.
$F_{Y_n}(y) = \mathbb{P}(Y_n \le y) = \mathbb{P}(n(\theta - M_n) \le y) = \mathbb{P}\left(M_n \ge \theta - \frac{y}{n}\right) = 1 - \mathbb{P}\left(M_n < \theta - \frac{y}{n}\right)$.
Pour $n$ suffisamment grand (dès que $\frac{y}{n} < \theta$), nous avons :
$F_{Y_n}(y) = 1 - \left(\frac{\theta - y/n}{\theta}\right)^n = 1 - \left(1 - \frac{y/\theta}{n}\right)^n$.
Un résultat classique d'analyse garantit que la suite numérique $(1 - \frac{z}{n})^n$ converge vers $e^{-z}$.
En l'appliquant avec $z = \frac{y}{\theta}$, nous obtenons :
$\lim_{n \to \infty} F_{Y_n}(y) = 1 - e^{-y/\theta}$.
Cette limite est la fonction de répartition de la loi exponentielle de paramètre $\lambda = \frac{1}{\theta}$.
Puisque la fonction de répartition limite est continue partout, la convergence en loi est établie vers la distribution $\mathcal{E}(1/\theta)$.
