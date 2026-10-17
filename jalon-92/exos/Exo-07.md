# Exercice 7 : Convergence des fonctions continues de la moyenne \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $(X_n)$ une suite de variables i.i.d. telles que $\mathbb{E}[|X_1|] < \infty$ et $\mathbb{E}[X_1] = \mu$.
Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction continue.
Montrer que $f\left(\frac{1}{n} \sum_{i=1}^n X_i\right) \xrightarrow{p.s.} f(\mu)$.

## Correction Détaillée
### Étape 1 : Application de la LFGN classique
Soit $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.
Puisque la suite $(X_n)$ est i.i.d. et dans $L^1$, le théorème de la Loi Forte des Grands Nombres nous assure que $\bar{X}_n$ converge presque sûrement vers $\mu$ :
$$ \mathbb{P}\left(\left\{\omega \in \Omega \mid \lim_{n \to \infty} \bar{X}_n(\omega) = \mu \right\}\right) = 1 $$
Soit $N \subset \Omega$ l'ensemble de mesure de probabilité nulle tel que pour tout $\omega \in \Omega \setminus N$, on ait $\lim_{n \to \infty} \bar{X}_n(\omega) = \mu$.

### Étape 2 : Composition par une fonction continue
Fixons un $\omega \in \Omega \setminus N$. Nous avons une suite de nombres réels $x_n = \bar{X}_n(\omega)$ qui converge vers la limite réelle $l = \mu$.
Puisque la fonction $f$ est continue sur $\mathbb{R}$, elle satisfait la caractérisation séquentielle de la continuité : pour toute suite réelle $(x_n)$ convergeant vers $l$, la suite $f(x_n)$ converge vers $f(l)$.
Ainsi, pour ce choix de $\omega$, on a :
$$ \lim_{n \to \infty} f(\bar{X}_n(\omega)) = f(\mu) $$

### Étape 3 : Conclusion probatoire
L'ensemble des $\omega$ pour lesquels la convergence $f(\bar{X}_n(\omega)) \to f(\mu)$ a lieu contient $\Omega \setminus N$. Or $\mathbb{P}(\Omega \setminus N) = 1$.
Donc l'événement $\left\{ \omega \in \Omega \mid \lim_{n \to \infty} f(\bar{X}_n(\omega)) = f(\mu) \right\}$ a une probabilité de 1.
Cela prouve exactement que $f(\bar{X}_n) \xrightarrow{p.s.} f(\mu)$. C'est le théorème de composition ou \Continuous Mapping Theorem" appliqué à la convergence presque sûre. $\blacksquare$
