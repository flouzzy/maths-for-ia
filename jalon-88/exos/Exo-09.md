# Somme de Poissons indépendantes

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soient $X \sim \mathcal{P}(\lambda)$ et $Y \sim \mathcal{P}(\mu)$ deux variables aléatoires discrètes suivant des lois de Poisson. On suppose que $X$ et $Y$ sont indépendantes.
Démontrer formellement, par le calcul de convolution discrète, que la variable aléatoire $S = X + Y$ suit une loi de Poisson dont on déterminera le paramètre.

### Correction

Soient $X$ et $Y$ deux variables indépendantes telles que $X \sim \mathcal{P}(\lambda)$ et $Y \sim \mathcal{P}(\mu)$.
Rappelons la probabilité d'une loi de Poisson : $\mathbb{P}(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}$ pour $k \in \mathbb{N}$.
La variable somme $S = X + Y$ prend ses valeurs dans $\mathbb{N}$. Soit $n \in \mathbb{N}$.
L'événement $\{S = n\}$ peut s'écrire comme l'union disjointe de toutes les configurations de $X$ et $Y$ dont la somme vaut $n$ :
$\{S = n\} = \bigcup_{k=0}^n \left( \{X = k\} \cap \{Y = n - k\} \right)$
Par axiome d'additivité dénombrable sur les ensembles disjoints :
$\mathbb{P}(S = n) = \sum_{k=0}^n \mathbb{P}(X = k \cap Y = n - k)$
On applique l'hypothèse d'indépendance de $X$ et $Y$ :
$\mathbb{P}(S = n) = \sum_{k=0}^n \mathbb{P}(X = k)\mathbb{P}(Y = n - k)$
On substitue maintenant les expressions analytiques des lois de Poisson :
$\mathbb{P}(S = n) = \sum_{k=0}^n \left( e^{-\lambda} \frac{\lambda^k}{k!} \right) \left( e^{-\mu} \frac{\mu^{n-k}}{(n-k)!} \right)$
On extrait les facteurs exponentiels qui ne dépendent pas de l'indice de sommation $k$ :
$\mathbb{P}(S = n) = e^{-(\lambda + \mu)} \sum_{k=0}^n \frac{\lambda^k \mu^{n-k}}{k!(n-k)!}$
Afin de faire apparaître la formule du binôme de Newton, on multiplie et on divise par la factorielle $n!$ :
$\mathbb{P}(S = n) = e^{-(\lambda + \mu)} \frac{1}{n!} \sum_{k=0}^n \frac{n!}{k!(n-k)!} \lambda^k \mu^{n-k}$
On identifie la définition formelle du coefficient binomial $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ :
$\mathbb{P}(S = n) = e^{-(\lambda + \mu)} \frac{1}{n!} \sum_{k=0}^n \binom{n}{k} \lambda^k \mu^{n-k}$
On applique le théorème du binôme de Newton : $\sum_{k=0}^n \binom{n}{k} x^k y^{n-k} = (x+y)^n$ :
$\mathbb{P}(S = n) = e^{-(\lambda + \mu)} \frac{(\lambda + \mu)^n}{n!}$
Cette expression est très exactement la fonction de masse d'une loi de Poisson de paramètre $(\lambda + \mu)$.
**Conclusion :** La somme de deux variables de Poisson indépendantes suit rigoureusement une loi de Poisson, $\mathcal{P}(\lambda + \mu)$.
