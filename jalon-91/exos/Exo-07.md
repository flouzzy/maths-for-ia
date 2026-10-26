# Exercice 7 : Chernoff pour la loi de Poisson

$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $X$ une variable aléatoire suivant une loi de Poisson de paramètre $\lambda > 0$.
Montrer par la méthode de Chernoff que pour tout $x > \lambda$ :
$$ \mathbb{P}(X \ge x) \le \exp(-\lambda + x - x \ln(x/\lambda)) $$

**Correction :**
La fonction génératrice des moments de $X \sim \mathcal{P}(\lambda)$ est :
$$ \mathbb{E}[e^{tX}] = \sum_{k=0}^\infty e^{tk} e^{-\lambda} \frac{\lambda^k}{k!} = e^{-\lambda} \sum_{k=0}^\infty \frac{(\lambda e^t)^k}{k!} = e^{-\lambda} \exp(\lambda e^t) = \exp(\lambda(e^t - 1)) $$
On cherche à borner $\mathbb{P}(X \ge x)$ pour $x > \lambda$.
Pour tout $t > 0$, l'inégalité de Markov sur $e^{tX}$ donne :
$$ \mathbb{P}(X \ge x) = \mathbb{P}(e^{tX} \ge e^{tx}) \le \frac{\mathbb{E}[e^{tX}]}{e^{tx}} = \exp(\lambda(e^t - 1) - tx) $$
Pour optimiser cette borne, il faut minimiser la fonction en exposant $f(t) = \lambda(e^t - 1) - tx$ pour $t > 0$.
La dérivée est $f'(t) = \lambda e^t - x$.
Elle s'annule pour $t^* = \ln(x/\lambda)$. Comme $x > \lambda$, on a bien $t^* > 0$.
Calculons $f(t^*)$ :
$$ f(t^*) = \lambda\left(e^{\ln(x/\lambda)} - 1\right) - x \ln(x/\lambda) = \lambda\left(\frac{x}{\lambda} - 1\right) - x \ln(x/\lambda) $$
$$ f(t^*) = x - \lambda - x \ln(x/\lambda) $$
En injectant cette valeur minimale dans l'exponentielle, on obtient la borne de Chernoff :
$$ \mathbb{P}(X \ge x) \le \exp(-\lambda + x - x \ln(x/\lambda)) $$
La démonstration est terminée.
