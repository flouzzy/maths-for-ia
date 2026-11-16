# Exercice 7 : Théorème de Slutsky

Niveau : $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X_n)$ une suite de v.a. convergeant en loi vers une v.a. $X$ de loi continue, et $(Y_n)$ une suite convergeant en probabilité vers une constante $c$.
Le théorème de Slutsky affirme que $X_n + Y_n \xrightarrow{\mathcal{L}} X + c$ et $X_n Y_n \xrightarrow{\mathcal{L}} cX$.
Appliquer ce théorème : soit $Z_1, \dots, Z_n$ i.i.d. de moyenne $\mu$ et variance $\sigma^2 > 0$. Notons $\bar{Z}_n = \frac{1}{n} \sum Z_i$ et $S_n^2$ l'estimateur sans biais de la variance (qui converge p.s. vers $\sigma^2$).
Montrer que $U_n = \frac{\sqrt{n}(\bar{Z}_n - \mu)}{S_n} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$.

## Correction

**1. Convergence au numérateur (TCL) :**
D'après le Théorème Central Limite (TCL), puisque les $Z_i$ sont i.i.d. avec une variance finie $\sigma^2$, on a :
$$V_n = \frac{\sqrt{n}(\bar{Z}_n - \mu)}{\sigma} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$

**2. Convergence au dénominateur :**
On sait par la loi forte des grands nombres (et le fait que $S_n^2$ est consistant) que $S_n^2 \xrightarrow{\text{p.s.}} \sigma^2$.
Puisque la convergence presque sûre implique la convergence en probabilité, $S_n^2 \xrightarrow{\mathbb{P}} \sigma^2$.
La fonction racine carrée $x \mapsto \sqrt{x}$ étant continue sur $]0, +\infty[$, par le théorème de continuité (Continuous Mapping Theorem), on a $S_n \xrightarrow{\mathbb{P}} \sigma$.
Et, comme $\sigma \neq 0$, par continuité de l'inverse, $\frac{\sigma}{S_n} \xrightarrow{\mathbb{P}} 1$.

**3. Application de Slutsky :**
On peut réécrire $U_n$ comme :
$$U_n = \frac{\sqrt{n}(\bar{Z}_n - \mu)}{S_n} = \frac{\sqrt{n}(\bar{Z}_n - \mu)}{\sigma} \times \frac{\sigma}{S_n} = V_n \times W_n$$
où $V_n \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$ et $W_n \xrightarrow{\mathbb{P}} 1$ (une constante).
D'après le lemme de Slutsky concernant le produit, on a :
$$V_n W_n \xrightarrow{\mathcal{L}} 1 \times \mathcal{N}(0, 1) = \mathcal{N}(0, 1)$$
Ainsi, on a démontré rigoureusement que $U_n \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$. Ceci justifie l'utilisation des tests de Student asymptotiques avec écart-type empirique.
