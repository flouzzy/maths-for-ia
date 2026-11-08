# Exercice 05

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Montrez de manière explicite que si une suite $(X_n)$ converge dans $L^1(\Omega)$ vers une variable $X$, alors elle converge en probabilité vers $X$.
*Indication : Utilisez l'inégalité de Markov.*

**Correction :**

L'objectif est d'établir l'implication fondamentale : Convergence $L^1 \implies$ Convergence en probabilité.
Traduisons les hypothèses. La convergence dans $L^1$ se formule ainsi :
$$ \lim_{n \to \infty} \mathbb{E}[|X_n - X|] = 0 $$
Nous devons aboutir à la définition de la convergence en probabilité : pour tout $\varepsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| \ge \varepsilon) = 0$.

**Démonstration pas à pas :**

1. Fixons un seuil d'écartement $\varepsilon > 0$ arbitraire. L'événement dont nous devons contrôler la probabilité est $\{ \omega \in \Omega \mid |X_n(\omega) - X(\omega)| \ge \varepsilon \}$.
2. Considérons la nouvelle variable aléatoire $Y_n = |X_n - X|$. Cette variable est positive presque sûrement ($Y_n \ge 0$).
De plus, par hypothèse de convergence $L^1$, l'espérance de $Y_n$ existe, est finie, et tend vers $0$.
3. Appliquons l'inégalité de Markov à la variable positive $Y_n$. Pour tout $a > 0$, l'inégalité s'écrit :
$$ \mathbb{P}(Y_n \ge a) \le \frac{\mathbb{E}[Y_n]}{a} $$
4. Instancions cette inégalité avec le seuil $a = \varepsilon$. Nous obtenons la majoration cruciale :
$$ \mathbb{P}(|X_n - X| \ge \varepsilon) \le \frac{\mathbb{E}[|X_n - X|]}{\varepsilon} $$
5. Tout comme dans l'inégalité de Bienaymé-Chebyshev, cette probabilité est trivialement minorée par $0$. Nous posons donc l'encadrement :
$$ 0 \le \mathbb{P}(|X_n - X| \ge \varepsilon) \le \frac{\mathbb{E}[|X_n - X|]}{\varepsilon} $$
6. Analysons le comportement asymptotique de cet encadrement lorsque $n \to \infty$.
Le paramètre $\varepsilon$ est constant et strictement positif.
Le numérateur $\mathbb{E}[|X_n - X|]$ tend vers zéro par hypothèse stricte de convergence dans $L^1$.
Ainsi, la limite du majorant est :
$$ \lim_{n \to \infty} \frac{\mathbb{E}[|X_n - X|]}{\varepsilon} = \frac{0}{\varepsilon} = 0 $$
7. Par le théorème d'encadrement des limites de suites, il en résulte inévitablement que :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| \ge \varepsilon) = 0 $$
Cette égalité étant vérifiée pour tout $\varepsilon > 0$ arbitrairement choisi, la preuve est achevée.
La suite $(X_n)$ converge bien en probabilité vers $X$.
