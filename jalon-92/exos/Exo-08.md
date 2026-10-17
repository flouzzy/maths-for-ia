# Exercice 8 : Théorème de Weierstrass probabiliste via les polynômes de Bernstein \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $f$ une fonction continue sur $[0,1]$. Soit $S_n \sim \mathcal{B}(n, x)$ pour $x \in [0,1]$.
On pose $B_n(f)(x) = \mathbb{E}\left[f\left(\frac{S_n}{n}\right)\right]$.
Montrer en utilisant la loi faible/forte que $B_n(f)(x)$ converge uniformément vers $f(x)$ sur $[0,1]$. (Esquisse de la preuve rigoureuse demandée).

## Correction Détaillée
### Étape 1 : Expression du polynôme de Bernstein
La loi de $S_n$ est binomiale. Donc $\mathbb{P}(S_n = k) = \binom{n}{k} x^k (1-x)^{n-k}$. L'espérance devient :
$$ B_n(f)(x) = \sum_{k=0}^n f\left(\frac{k}{n}\right) \binom{n}{k} x^k (1-x)^{n-k} $$
C'est bien un polynôme en $x$.

### Étape 2 : Continuité uniforme et borne
Puisque $f$ est continue sur le segment compact $[0,1]$, elle est bornée : il existe $M > 0$ tel que $|f(y)| \le M$ pour tout $y$.
De plus, par le théorème de Heine, $f$ est uniformément continue : pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que $|y - x| < \delta \implies |f(y) - f(x)| < \epsilon/2$.

### Étape 3 : Séparation de l'espérance
On veut majorer $|B_n(f)(x) - f(x)|$. Comme $\sum \mathbb{P}(S_n=k) = 1$, on a $f(x) = \mathbb{E}[f(x)]$.
$$ |B_n(f)(x) - f(x)| \le \mathbb{E}\left[ \left| f\left(\frac{S_n}{n}\right) - f(x) \right| \right] $$
On décompose cette espérance sur deux événements : $A = \left\{ \left| \frac{S_n}{n} - x \right| < \delta \right\}$ et son complémentaire $A^c$.

### Étape 4 : Majoration des deux termes
Sur $A$, par continuité uniforme, l'écart est majoré par $\epsilon/2$. Donc l'espérance sur $A$ est $\le \epsilon/2 \cdot \mathbb{P}(A) \le \epsilon/2$.
Sur $A^c$, l'écart maximal entre deux valeurs de $f$ est $2M$. L'espérance est donc majorée par $2M \mathbb{P}(A^c)$.
Il faut donc évaluer $\mathbb{P}(A^c) = \mathbb{P}\left( \left| \frac{S_n}{n} - x \right| \ge \delta \right)$.
Par l'inégalité de Bienaymé-Tchebychev (puisque $S_n$ a pour variance $nx(1-x)$) :
$$ \mathbb{P}(A^c) \le \frac{\text{Var}(S_n/n)}{\delta^2} = \frac{x(1-x)}{n \delta^2} $$
Le numérateur $x(1-x)$ atteint son maximum sur $[0,1]$ en $1/2$, où il vaut $1/4$.
Donc $\mathbb{P}(A^c) \le \frac{1}{4n\delta^2}$.

### Étape 5 : Conclusion sur la convergence uniforme
On regroupe les majorations :
$$ \sup_{x \in [0,1]} |B_n(f)(x) - f(x)| \le \frac{\epsilon}{2} + 2M \frac{1}{4n\delta^2} $$
Pour $\epsilon$ fixé, $\delta$ est fixé. Si l'on prend $n > \frac{M}{\epsilon \delta^2}$, le second terme devient strictement inférieur à $\epsilon/2$.
Ainsi, pour un tel $n$, l'erreur uniforme est strictement inférieure à $\epsilon$.
Ceci démontre la convergence uniforme de $B_n(f)$ vers $f$ (Théorème de Weierstrass probabiliste approché par la loi des grands nombres). $\blacksquare$
