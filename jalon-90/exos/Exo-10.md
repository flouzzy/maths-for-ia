# Exercice 10

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Théorème de Slutsky (Cas Particulier).
Soient $X_n \xrightarrow{\mathcal{L}} X$ (convergence en loi) et $Y_n \xrightarrow{\mathbb{P}} c$ (convergence en probabilité vers une constante $c$).
Montrez que la somme $X_n + Y_n \xrightarrow{\mathcal{L}} X + c$.

**Correction :**
Nous voulons montrer que pour toute fonction $f$ continue et bornée (et supposons-la uniformément continue, ce qui suffit par densité), $\mathbb{E}[f(X_n + Y_n)] \to \mathbb{E}[f(X + c)]$.
Décomposons la différence :
$$ |\mathbb{E}[f(X_n + Y_n)] - \mathbb{E}[f(X + c)]| \le \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|] + |\mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)]| $$

1. **Deuxième terme :** Puisque $X_n \xrightarrow{\mathcal{L}} X$, et que la fonction $g(x) = f(x + c)$ est continue et bornée, on a par définition de la convergence en loi :
$$ \lim_{n \to \infty} \mathbb{E}[f(X_n + c)] = \mathbb{E}[f(X + c)] $$
Donc le deuxième terme tend vers zéro.

2. **Premier terme :** Soit $M$ un majorant de $f$. Pour un $\epsilon > 0$ donné, par uniforme continuité de $f$, il existe $\delta > 0$ tel que si $|a - b| < \delta$, alors $|f(a) - f(b)| < \epsilon$.
Ici $| (X_n + Y_n) - (X_n + c) | = |Y_n - c|$.
On sépare l'espérance en conditionnant par $|Y_n - c| < \delta$ et $|Y_n - c| \ge \delta$ :
$$ \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|] \le \epsilon \cdot \mathbb{P}(|Y_n - c| < \delta) + 2M \cdot \mathbb{P}(|Y_n - c| \ge \delta) $$
Or, puisque $Y_n \xrightarrow{\mathbb{P}} c$, on sait que $\lim_{n \to \infty} \mathbb{P}(|Y_n - c| \ge \delta) = 0$.
Ainsi, en prenant la limite sup :
$$ \limsup_{n \to \infty} \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|] \le \epsilon \cdot 1 + 2M \cdot 0 = \epsilon $$
Puisque $\epsilon$ est arbitraire, ce terme tend vers $0$.

En additionnant les deux résultats, on trouve que $\lim_{n \to \infty} \mathbb{E}[f(X_n + Y_n)] = \mathbb{E}[f(X + c)]$, ce qui démontre la convergence en loi de la somme.
