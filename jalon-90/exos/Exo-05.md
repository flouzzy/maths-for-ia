# Exercice 5 : L'approximation d'une exponentielle
$\bigstar\bigstar\bigstar\star\star$


Soit $(X_n)$ une suite de variables aléatoires suivant une loi de Poisson de paramètre $n$. On pose $Y_n = \frac{X_n}{n}$.
1. Quelle est l'espérance et la variance de $Y_n$ ?
2. Étudiez la convergence dans $L^2$ de la suite $Y_n$.
3. Que pouvez-vous déduire sur la convergence en probabilité ?

**Correction :**
1. On sait que pour $X_n \sim \mathcal{P}(n)$, on a $\mathbb{E}[X_n] = n$ et $\mathbb{V}(X_n) = n$.
Pour la variable dilatée $Y_n$, par linéarité de l'espérance et propriété bilinéaire de la variance :
$$ \mathbb{E}[Y_n] = \frac{1}{n} \mathbb{E}[X_n] = \frac{n}{n} = 1 $$
$$ \mathbb{V}(Y_n) = \frac{1}{n^2} \mathbb{V}(X_n) = \frac{n}{n^2} = \frac{1}{n} $$
2. On cherche la limite de l'erreur quadratique moyenne par rapport à la constante $1$ (qui est aussi l'espérance) :
$$ \mathbb{E}[|Y_n - 1|^2] = \mathbb{E}[(Y_n - \mathbb{E}[Y_n])^2] = \mathbb{V}(Y_n) = \frac{1}{n} $$
Puisque $\lim_{n \to \infty} \frac{1}{n} = 0$, nous obtenons $\lim_{n \to \infty} \mathbb{E}[|Y_n - 1|^2] = 0$. La suite converge vers $1$ dans $L^2$.
3. La convergence dans un espace $L^p$ (ici $p=2$) impliquant la convergence en probabilité, on a directement $Y_n \xrightarrow{\mathbb{P}} 1$.
