# Exercice 7 : Le paradoxe de Saint-Pétersbourg et la LFGN \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X_n)_{n \geq 1}$ le gain d'un joueur lors du $n$-ième jeu de Saint-Pétersbourg : $X_n$ prend la valeur $2^k$ avec probabilité $1/2^k$ pour tout $k \geq 1$.
1. Montrer que l'espérance $\mathbb{E}[X_1]$ est infinie.
2. Que peut-on dire du comportement de $\frac{X_n}{n \log_2(n)}$ ? (Admis)
3. La loi forte des grands nombres s'applique-t-elle ici sous sa forme standard ? Justifier.
4. On tronque la variable en posant $Y_n = X_n \mathbf{1}_{\{X_n \leq n\}}$. La LFGN s'applique-t-elle à $Y_n$ ?

**Correction :**
1. Calculons l'espérance :
$$\mathbb{E}[X_1] = \sum_{k=1}^{\infty} 2^k \mathbb{P}(X_1 = 2^k) = \sum_{k=1}^{\infty} 2^k \frac{1}{2^k} = \sum_{k=1}^{\infty} 1 = +\infty$$
2. On admet que pour cette loi très particulière à queue lourde, Feller a montré que la somme $\sum_{i=1}^n X_i$ normalisée par $n \log_2(n)$ converge en probabilité vers 1. Ainsi, la moyenne croît comme $\log_2(n)$ et non vers une constante.
3. La LFGN standard (théorème de Kolmogorov) exige que la variable aléatoire admette une espérance finie, c'est-à-dire $\mathbb{E}[|X_1|] < \infty$. Ici, $\mathbb{E}[X_1] = +\infty$, donc la LFGN ne s'applique pas. La moyenne empirique $\bar{X}_n$ diverge presque sûrement vers l'infini.
4. Les variables $(Y_n)$ ne sont pas identiquement distribuées car le seuil de troncature dépend de $n$. Cependant, pour chaque $n$ fixé, $\mathbb{E}[Y_n] < \infty$. La théorie des sommes de variables aléatoires indépendantes non identiquement distribuées (avec des conditions de type Lyapounov ou un développement spécifique) est nécessaire pour étudier le comportement de $\frac{1}{n} \sum Y_i$. La LFGN usuelle pour les suites I.I.D. ne s'applique donc pas directement non plus.
