# Exo 03 : Contre-exemple en l'absence de positivité ($\bigstar$\bigstar\star\star\star$)

## Énoncé
Soit la suite de fonctions définies sur $X = [0, 1]$ par la mesure de Lebesgue, posons :
$$ f_n(x) = \begin{cases} -n & \text{si } 0 < x < \frac{1}{n} \\ 0 & \text{sinon} \end{cases} $$
1. Montrer que la suite $(f_n)_{n \ge 1}$ converge simplement vers une fonction $f$ presque partout.
2. Déterminer $\lim_{n \to \infty} \int_0^1 f_n(x) \, dx$.
3. Le théorème de Beppo Levi s'applique-t-il ? Expliquez pourquoi.

## Correction Détaillée
**Étape 1 : Limite simple**
Pour $x = 0$, $f_n(0) = 0$ pour tout $n$, donc $f_n(0) \to 0$.
Soit $x > 0$. Il existe un rang $N$ tel que pour $n \ge N$, on ait $\frac{1}{n} \le x$.
Ainsi, pour tout $n \ge N$, $f_n(x) = 0$. Par suite, $\lim_{n \to \infty} f_n(x) = 0$.
La fonction converge simplement vers $f(x) = 0$ sur $[0, 1]$.

**Étape 2 : Calcul des intégrales**
L'intégrale de $f_n$ est l'aire algébrique sous un rectangle :
$$ \int_0^1 f_n(x) \, dx = \int_0^{\frac{1}{n}} -n \, dx = -n \times \frac{1}{n} = -1 $$
Donc $\lim_{n \to \infty} \int_0^1 f_n(x) \, dx = -1$.
D'autre part, l'intégrale de la limite $f(x)=0$ est :
$$ \int_0^1 f(x) \, dx = \int_0^1 0 \, dx = 0 $$

**Étape 3 : Analyse du théorème**
On observe que $-1 \neq 0$. L'égalité n'est pas respectée.
Pourquoi le théorème de convergence monotone ne s'applique-t-il pas ?
Pour que le théorème s'applique sur des fonctions non nécessairement positives, il faudrait que la suite soit *croissante* et minorée par une fonction intégrable (ce qui ramènerait au cas positif par translation).
Or, étudions la variation : soit $x \in ]\frac{1}{n+1}, \frac{1}{n}[$. On a $f_{n+1}(x) = 0$ et $f_n(x) = -n$. Ici, $f_n(x) < f_{n+1}(x)$ (ça monte).
Mais pour $x \in ]0, \frac{1}{n+1}[$, $f_n(x) = -n$ et $f_{n+1}(x) = -(n+1)$. Ici $f_n(x) > f_{n+1}(x)$ (ça descend).
La suite n'est ni globalement croissante, ni positive. Les hypothèses de Beppo Levi ne sont pas réunies, et l'interversion est invalide.
