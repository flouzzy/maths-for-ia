# Exercice 5

\subsection*{Exercice 5 : Somme de variables de Poisson indépendantes \quad $\bigstar\bigstar\bigstar\star\star$}

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant des lois de Poisson de paramètres respectifs $\lambda$ et $\mu$.
Montrer que $Z = X + Y$ suit une loi de Poisson de paramètre $\lambda + \mu$.

**Correction :**
1. Les variables $X$ et $Y$ prennent leurs valeurs dans $\mathbb{N}$. La somme $Z = X + Y$ prend aussi ses valeurs dans $\mathbb{N}$.
2. Soit $n \in \mathbb{N}$. Calculons $P(Z = n)$.
3. L'événement $\{X + Y = n\}$ se décompose selon toutes les valeurs possibles pour $X$. Si $X = k$ (avec $0 \le k \le n$), alors $Y$ doit valoir $n - k$.
   $P(Z = n) = \sum_{k=0}^{n} P(X = k, Y = n - k)$.
4. Par indépendance de $X$ et $Y$ :
   $P(Z = n) = \sum_{k=0}^{n} P(X = k) P(Y = n - k)$.
5. On utilise la formule de la loi de Poisson : $P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}$ et $P(Y=n-k) = e^{-\mu} \frac{\mu^{n-k}}{(n-k)!}$.
   $P(Z = n) = \sum_{k=0}^{n} \left( e^{-\lambda} \frac{\lambda^k}{k!} \right) \left( e^{-\mu} \frac{\mu^{n-k}}{(n-k)!} \right)$.
6. On réarrange les termes :
   $P(Z = n) = e^{-(\lambda + \mu)} \sum_{k=0}^{n} \frac{\lambda^k \mu^{n-k}}{k! (n-k)!}$.
7. Pour faire apparaître le binôme de Newton, on multiplie et divise par $n!$ :
   $P(Z = n) = e^{-(\lambda + \mu)} \frac{1}{n!} \sum_{k=0}^{n} \frac{n!}{k! (n-k)!} \lambda^k \mu^{n-k}$.
8. On reconnaît le coefficient binomial $\binom{n}{k} = \frac{n!}{k! (n-k)!}$ :
   $P(Z = n) = e^{-(\lambda + \mu)} \frac{1}{n!} \sum_{k=0}^{n} \binom{n}{k} \lambda^k \mu^{n-k}$.
9. D'après la formule du binôme de Newton, $\sum_{k=0}^{n} \binom{n}{k} \lambda^k \mu^{n-k} = (\lambda + \mu)^n$.
10. Finalement, $P(Z = n) = e^{-(\lambda + \mu)} \frac{(\lambda + \mu)^n}{n!}$.
11. On reconnaît exactement la fonction de masse d'une loi de Poisson de paramètre $\lambda + \mu$. Donc $Z \sim \mathcal{P}(\lambda + \mu)$.
