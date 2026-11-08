# Exercice 04

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires telles que $\mathbb{E}[X_n] = \mu$ et $\text{Var}(X_n) = \sigma_n^2$.
Démontrez que si $\lim_{n \to \infty} \sigma_n^2 = 0$, alors la suite $X_n$ converge en probabilité vers la constante $\mu$.

**Correction :**

Nous devons démontrer que pour tout réel $\varepsilon > 0$, la limite de la probabilité que $X_n$ dévie de $\mu$ de plus de $\varepsilon$ est nulle.
Le lien fondamental entre l'écart à la moyenne (ici le paramètre de notre convergence) et la variance est fourni par l'inégalité de Bienaymé-Chebyshev.

**Démonstration étape par étape :**

1. Fixons un écart $\varepsilon > 0$ arbitraire.
2. La variable aléatoire $X_n$ admet une variance finie $\sigma_n^2$, ce qui implique qu'elle est de carré intégrable. Nous pouvons donc appliquer l'inégalité de Bienaymé-Chebyshev directement à $X_n$.
Cette inégalité stipule que pour toute variable aléatoire $X$ d'espérance finie et de variance finie, et pour tout $a > 0$ :
$$ \mathbb{P}(|X - \mathbb{E}[X]| \ge a) \le \frac{\text{Var}(X)}{a^2} $$
3. En instanciant cette inégalité avec notre variable $X_n$, son espérance $\mu$ et notre seuil $\varepsilon$, nous obtenons la majoration fondamentale :
$$ \mathbb{P}(|X_n - \mu| \ge \varepsilon) \le \frac{\text{Var}(X_n)}{\varepsilon^2} $$
Substituons l'expression de la variance donnée dans l'énoncé :
$$ \mathbb{P}(|X_n - \mu| \ge \varepsilon) \le \frac{\sigma_n^2}{\varepsilon^2} $$
4. Les probabilités étant des quantités positives ou nulles, nous avons l'encadrement complet :
$$ 0 \le \mathbb{P}(|X_n - \mu| \ge \varepsilon) \le \frac{\sigma_n^2}{\varepsilon^2} $$
5. Passons maintenant à la limite lorsque $n \to \infty$. Par hypothèse de l'énoncé, la suite des variances tend vers zéro : $\lim_{n \to \infty} \sigma_n^2 = 0$.
Puisque $\varepsilon$ est une constante fixée (indépendante de $n$), le terme de droite tend vers zéro :
$$ \lim_{n \to \infty} \frac{\sigma_n^2}{\varepsilon^2} = \frac{0}{\varepsilon^2} = 0 $$
6. Par application rigoureuse du théorème d'encadrement (ou théorème des gendarmes) sur les suites réelles, le terme central est forcé de converger vers zéro :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - \mu| \ge \varepsilon) = 0 $$

Ceci constitue très exactement la définition de la convergence en probabilité. Nous concluons donc formellement que :
$$ X_n \xrightarrow{\mathbb{P}} \mu $$
Cet exercice constitue une brique essentielle pour la démonstration classique de la loi faible des grands nombres.
