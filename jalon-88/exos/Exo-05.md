# Exercice 5 : Stabilité de la loi de Poisson par l'addition \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**

Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant des lois de Poisson de paramètres respectifs $\lambda_1 > 0$ et $\lambda_2 > 0$.
Démontrer rigoureusement que la somme $Z = X + Y$ suit une loi de Poisson de paramètre $\lambda_1 + \lambda_2$.

**Correction Détaillée :**

1. Les variables $X$ et $Y$ prennent leurs valeurs dans l'ensemble des entiers naturels $\mathbb{N}$. Leur somme $Z$ prend donc également ses valeurs dans $\mathbb{N}$.
2. Soit $n \in \mathbb{N}$. Calculons la probabilité de l'événement $\{Z = n\}$.
   L'événement $\{X + Y = n\}$ peut se réaliser par la réunion disjointe des événements $\{X = k\} \cap \{Y = n - k\}$ pour toutes les valeurs possibles de $k$ allant de $0$ à $n$.
3. Par additivité, on applique la formule des probabilités totales (aussi appelée produit de convolution discret) :
   $$ \mathbb{P}(Z = n) = \sum_{k=0}^{n} \mathbb{P}(X = k \text{ et } Y = n - k) $$
4. Puisque $X$ et $Y$ sont indépendantes, la probabilité de l'intersection se factorise :
   $$ \mathbb{P}(Z = n) = \sum_{k=0}^{n} \mathbb{P}(X = k) \cdot \mathbb{P}(Y = n - k) $$
5. On remplace les probabilités par les formules de la loi de Poisson : $\mathbb{P}(X=k) = e^{-\lambda_1} \frac{\lambda_1^k}{k!}$ et $\mathbb{P}(Y=n-k) = e^{-\lambda_2} \frac{\lambda_2^{n-k}}{(n-k)!}$.
   $$ \mathbb{P}(Z = n) = \sum_{k=0}^{n} \left( e^{-\lambda_1} \frac{\lambda_1^k}{k!} \right) \left( e^{-\lambda_2} \frac{\lambda_2^{n-k}}{(n-k)!} \right) $$
6. On extrait les facteurs qui ne dépendent pas de l'indice de sommation $k$ :
   $$ \mathbb{P}(Z = n) = e^{-(\lambda_1 + \lambda_2)} \sum_{k=0}^{n} \frac{\lambda_1^k \lambda_2^{n-k}}{k!(n-k)!} $$
7. On multiplie et on divise par $n!$ afin de faire apparaître un coefficient binomial :
   $$ \mathbb{P}(Z = n) = e^{-(\lambda_1 + \lambda_2)} \frac{1}{n!} \sum_{k=0}^{n} \frac{n!}{k!(n-k)!} \lambda_1^k \lambda_2^{n-k} $$
8. On reconnaît le coefficient binomial $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ :
   $$ \mathbb{P}(Z = n) = e^{-(\lambda_1 + \lambda_2)} \frac{1}{n!} \sum_{k=0}^{n} \binom{n}{k} \lambda_1^k \lambda_2^{n-k} $$
9. Par la formule du binôme de Newton, on sait que $\sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k} = (a+b)^n$. On l'applique ici avec $a = \lambda_1$ et $b = \lambda_2$ :
   $$ \sum_{k=0}^{n} \binom{n}{k} \lambda_1^k \lambda_2^{n-k} = (\lambda_1 + \lambda_2)^n $$
10. En substituant ce résultat dans l'équation, on obtient :
    $$ \mathbb{P}(Z = n) = e^{-(\lambda_1 + \lambda_2)} \frac{(\lambda_1 + \lambda_2)^n}{n!} $$
11. Cette expression est exactement la fonction de masse de probabilité d'une loi de Poisson de paramètre $\lambda_1 + \lambda_2$.
12. La démonstration est achevée, $Z \sim \mathcal{P}(\lambda_1 + \lambda_2)$.
