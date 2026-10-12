# Exercice 7 : Somme de deux variables de Poisson indépendantes

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soient $X_1$ et $X_2$ deux variables aléatoires indépendantes suivant respectivement des lois de Poisson de paramètres $\lambda_1 > 0$ et $\lambda_2 > 0$.
Autrement dit, pour $k \in \mathbb{N}$, $\mathbb{P}(X_i = k) = e^{{-\lambda_i}} \frac{{\lambda_i^k}}{{k!}}$ pour $i \in \{{1,2\}}$.
Soit la variable aléatoire $Y = X_1 + X_2$.
Démontrer rigoureusement par le calcul que la somme $Y$ suit une loi de Poisson dont vous déterminerez le paramètre.

---
**Correction détaillée :**

Puisque $X_1$ et $X_2$ prennent des valeurs dans $\mathbb{N}$, leur somme $Y$ prend également ses valeurs dans $\mathbb{N}$. Soit $n \in \mathbb{N}$. Nous cherchons à calculer $\mathbb{P}(Y = n)$.

1. **Utilisation du théorème des probabilités totales (Produit de convolution discret) :**
L'événement $\{{Y = n\}}$ correspond à $\{{X_1 + X_2 = n\}}$.
On peut partitionner cet événement selon les valeurs possibles prises par $X_1$. Si $X_1 = k$, alors nécessairement $X_2 = n - k$.
Comme $X_2 \ge 0$, l'indice $k$ varie de $0$ à $n$.
$$ \mathbb{P}(Y = n) = \sum_{{k=0}}^n \mathbb{P}(X_1 = k \cap X_2 = n - k) $$

2. **Exploitation de l'indépendance :**
Par hypothèse, $X_1$ et $X_2$ sont indépendantes. La probabilité de l'intersection est donc le produit des probabilités :
$$ \mathbb{P}(Y = n) = \sum_{{k=0}}^n \mathbb{P}(X_1 = k) \mathbb{P}(X_2 = n - k) $$

3. **Substitution par les densités discrètes de Poisson :**
$$ \mathbb{P}(Y = n) = \sum_{{k=0}}^n \left( e^{{-\lambda_1}} \frac{{\lambda_1^k}}{{k!}} \right) \left( e^{{-\lambda_2}} \frac{{\lambda_2^{{n-k}}}}{{(n-k)!}} \right) $$

4. **Réarrangement algébrique :**
Factorisons les termes qui ne dépendent pas de l'indice de sommation $k$ :
$$ \mathbb{P}(Y = n) = e^{{-\lambda_1}} e^{{-\lambda_2}} \sum_{{k=0}}^n \frac{{1}}{{k! (n-k)!}} \lambda_1^k \lambda_2^{{n-k}} $$
$$ \mathbb{P}(Y = n) = e^{{-(\lambda_1 + \lambda_2)}} \sum_{{k=0}}^n \frac{{1}}{{k! (n-k)!}} \lambda_1^k \lambda_2^{{n-k}} $$

5. **Utilisation de la formule du binôme de Newton :**
Pour faire apparaître les coefficients binomiaux $\binom{{n}}{{k}} = \frac{{n!}}{{k!(n-k)!}}$, nous multiplions et divisons l'expression par $n!$ :
$$ \mathbb{P}(Y = n) = e^{{-(\lambda_1 + \lambda_2)}} \frac{{1}}{{n!}} \sum_{{k=0}}^n \frac{{n!}}{{k! (n-k)!}} \lambda_1^k \lambda_2^{{n-k}} $$
$$ \mathbb{P}(Y = n) = e^{{-(\lambda_1 + \lambda_2)}} \frac{{1}}{{n!}} \sum_{{k=0}}^n \binom{{n}}{{k}} \lambda_1^k \lambda_2^{{n-k}} $$
D'après la formule du binôme de Newton, $\sum_{{k=0}}^n \binom{{n}}{{k}} a^k b^{{n-k}} = (a + b)^n$. L'expression de la somme devient alors $(\lambda_1 + \lambda_2)^n$.
$$ \mathbb{P}(Y = n) = e^{{-(\lambda_1 + \lambda_2)}} \frac{{(\lambda_1 + \lambda_2)^n}}{{n!}} $$

6. **Conclusion :**
Nous reconnaissons exactement l'expression de la fonction de masse d'une loi de Poisson de paramètre $\lambda = \lambda_1 + \lambda_2$.
La somme de deux variables de Poisson indépendantes est donc une variable de Poisson dont le paramètre est la somme des paramètres. $\blacksquare$
