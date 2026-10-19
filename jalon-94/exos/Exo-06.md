# Exercice 6 : Convergence en loi d'une variable Student vers une Gaussienne \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X_i)$ une suite de variables aléatoires de loi $\mathcal{N}(\mu, \sigma^2)$ I.I.D.
On définit la moyenne empirique $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$ et la variance empirique non biaisée $S_n^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X}_n)^2$.
Soit la statistique $T_n = \frac{\bar{X}_n - \mu}{S_n / \sqrt{n}}$.
En utilisant le théorème de Slutsky et le Théorème Central Limite, montrer que $T_n$ converge en loi vers $\mathcal{N}(0, 1)$ lorsque $n \to \infty$.

**Correction :**

La variable $T_n$ peut s'écrire sous la forme d'un produit de deux variables aléatoires :
$$T_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \times \frac{\sigma}{S_n}$$
Posons $U_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}}$ et $V_n = \frac{\sigma}{S_n}$.

Étape 1 : Comportement de $U_n$.
D'après le Théorème Central Limite (appliqué aux $X_i$ de variance $\sigma^2$), $U_n$ converge en loi vers $U \sim \mathcal{N}(0, 1)$. (C'est d'ailleurs exactement vrai pour tout $n$ puisque les $X_i$ sont gaussiennes, donc $U_n \sim \mathcal{N}(0, 1)$).

Étape 2 : Comportement de $V_n$.
Par la Loi Forte des Grands Nombres, $S_n^2$ est un estimateur fortement convergent de $\sigma^2$, c'est-à-dire $S_n^2 \xrightarrow{\text{p.s.}} \sigma^2$.
Par continuité de la fonction $x \mapsto \frac{\sigma}{\sqrt{x}}$ en $\sigma^2$ (qui est strictement positif), on en déduit que :
$$V_n = \frac{\sigma}{\sqrt{S_n^2}} \xrightarrow{\text{p.s.}} \frac{\sigma}{\sqrt{\sigma^2}} = 1$$
La convergence presque sûre implique la convergence en probabilité : $V_n \xrightarrow{\mathbb{P}} 1$.

Étape 3 : Application du théorème de Slutsky.
Le théorème de Slutsky affirme que si une suite $U_n$ converge en loi vers $U$ et une suite $V_n$ converge en probabilité vers une constante $c$, alors le produit $U_n V_n$ converge en loi vers $c U$.
Ici, $U_n \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$ et $V_n \xrightarrow{\mathbb{P}} 1$.
Donc $T_n = U_n V_n \xrightarrow{\mathcal{L}} 1 \times \mathcal{N}(0, 1) = \mathcal{N}(0, 1)$.

La statistique $T_n$, qui est utilisée pour les tests de Student lorsque la variance $\sigma^2$ est inconnue, se comporte donc exactement comme une loi Normale lorsque $n$ est très grand.
