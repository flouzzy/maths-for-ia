# Exercice 2 : Inégalité de Markov et $L^p$

Niveau : $\bigstar\bigstar\star\star\star$

Soit $X \sim \mathcal{N}(0, 1)$ et définissons $X_n = \frac{X}{n}$.
Montrer que $X_n \xrightarrow{L^2} 0$ puis en déduire sans calcul direct que $X_n \xrightarrow{\mathbb{P}} 0$.

## Correction

**1. Convergence dans $L^2$ :**
On calcule $\mathbb{E}[|X_n - 0|^2] = \mathbb{E}\left[\left(\frac{X}{n}\right)^2\right] = \frac{1}{n^2} \mathbb{E}[X^2]$.
Puisque $X$ suit une loi normale centrée réduite, sa variance est $\text{Var}(X) = 1$, et comme $\mathbb{E}[X] = 0$, on a $\mathbb{E}[X^2] = \text{Var}(X) + \mathbb{E}[X]^2 = 1$.
Donc $\mathbb{E}[|X_n - 0|^2] = \frac{1}{n^2}$.
En passant à la limite : $\lim_{n \to +\infty} \mathbb{E}[|X_n - 0|^2] = \lim_{n \to +\infty} \frac{1}{n^2} = 0$.
Par définition, on a bien $X_n \xrightarrow{L^2} 0$.

**2. Déduction pour la convergence en probabilité :**
Soit $\varepsilon > 0$. D'après l'inégalité de Markov appliquée à la variable aléatoire positive $|X_n - 0|^2$, on a :
$$\mathbb{P}(|X_n - 0| > \varepsilon) = \mathbb{P}(|X_n - 0|^2 > \varepsilon^2) \le \frac{\mathbb{E}[|X_n - 0|^2]}{\varepsilon^2}$$
D'après la question 1, on sait que $\mathbb{E}[|X_n - 0|^2] = \frac{1}{n^2}$.
On obtient donc :
$$\mathbb{P}(|X_n - 0| > \varepsilon) \le \frac{1}{n^2 \varepsilon^2}$$
Comme $\varepsilon$ est fixé, $\lim_{n \to +\infty} \frac{1}{n^2 \varepsilon^2} = 0$.
Par le théorème des gendarmes (puisque la probabilité est minorée par 0), on a :
$$\lim_{n \to +\infty} \mathbb{P}(|X_n - 0| > \varepsilon) = 0$$
Donc $X_n \xrightarrow{\mathbb{P}} 0$.
