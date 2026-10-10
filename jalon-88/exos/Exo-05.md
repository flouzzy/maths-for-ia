\subsection*{Exercice 5 : Variables de Poisson indépendantes \quad $\bigstar\bigstar\bigstar\star\star$}

Soient $X_1$ et $X_2$ deux variables aléatoires indépendantes suivant respectivement des lois de Poisson de paramètres $\lambda_1$ et $\lambda_2$. Montrer que $Z = X_1 + X_2$ suit une loi de Poisson de paramètre $\lambda_1 + \lambda_2$.

**Correction :**
1. Les valeurs de $X_1, X_2$ et $Z$ sont des entiers naturels. Soit $n \in \mathbb{N}$.
2. L'événement $\{Z = n\}$ s'écrit comme l'union disjointe des événements $\{X_1 = k, X_2 = n-k\}$ pour $k = 0, \ldots, n$.
3. $\mathbb{P}(Z = n) = \sum_{k=0}^{n} \mathbb{P}(X_1 = k, X_2 = n-k)$.
4. Par indépendance, $\mathbb{P}(Z = n) = \sum_{k=0}^{n} \mathbb{P}(X_1 = k)\mathbb{P}(X_2 = n-k)$.
5. On remplace par les expressions de la loi de Poisson :
   $\mathbb{P}(Z = n) = \sum_{k=0}^{n} \left( e^{-\lambda_1} \frac{\lambda_1^k}{k!} \right) \left( e^{-\lambda_2} \frac{\lambda_2^{n-k}}{(n-k)!} \right)$
6. On sort les termes constants de la somme :
   $\mathbb{P}(Z = n) = e^{-(\lambda_1+\lambda_2)} \frac{1}{n!} \sum_{k=0}^{n} \frac{n!}{k!(n-k)!} \lambda_1^k \lambda_2^{n-k}$
7. On reconnaît le coefficient binomial $\binom{n}{k}$, puis le développement du binôme de Newton :
   $\mathbb{P}(Z = n) = e^{-(\lambda_1+\lambda_2)} \frac{1}{n!} (\lambda_1 + \lambda_2)^n$
8. C'est exactement l'expression d'une loi de Poisson de paramètre $\lambda_1 + \lambda_2$.