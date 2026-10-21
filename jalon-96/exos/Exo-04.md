# Exercice 4 : Minimisation empirique (Maximum de Vraisemblance)

$\bigstar\bigstar\bigstar\star\star$


Soit un échantillon $x_1, \dots, x_n$ indépendant et identiquement distribué, tiré d'une loi de Bernoulli de paramètre $p$ inconnu. On utilise un modèle paramétrique avec une distribution Bernoulli de paramètre $\theta \in ]0, 1[$.

**1.** Écrire la fonction de perte Cross-Entropy empirique $\hat{H}_n(\theta)$.
**2.** Montrer que minimiser $\hat{H}_n(\theta)$ revient à effectuer une estimation par maximum de vraisemblance, et trouver la valeur optimale $\hat{\theta}$.

**Correction :**

**1.** La distribution prédite pour un élément $x_i \in \{0, 1\}$ est $q_\theta(x_i) = \theta^{x_i}(1-\theta)^{1-x_i}$.
La fonction de perte Cross-Entropy empirique (qui est la Negative Log-Likelihood moyenne) est :
$$\hat{H}_n(\theta) = - \frac{1}{n} \sum_{i=1}^n \ln(q_\theta(x_i))$$
$$\hat{H}_n(\theta) = - \frac{1}{n} \sum_{i=1}^n [x_i \ln \theta + (1-x_i) \ln(1-\theta)]$$

**2.** La minimisation de cette quantité est strictement équivalente à la maximisation de l'expression opposée :
$$\frac{1}{n} \sum_{i=1}^n \ln(q_\theta(x_i)) = \frac{1}{n} \ln \left( \prod_{i=1}^n q_\theta(x_i) \right)$$
Ceci est exactement la log-vraisemblance moyenne (Maximum de Vraisemblance).
Pour trouver l'optimum $\hat{\theta}$, dérivons $\hat{H}_n(\theta)$ par rapport à $\theta$ :
$$\frac{\partial}{\partial \theta} \hat{H}_n(\theta) = - \frac{1}{n} \sum_{i=1}^n \left[ \frac{x_i}{\theta} - \frac{1-x_i}{1-\theta} \right]$$
On annule la dérivée :
$$ \frac{1}{n} \sum_{i=1}^n \frac{x_i}{\theta} = \frac{1}{n} \sum_{i=1}^n \frac{1-x_i}{1-\theta}$$
Soit $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$ la moyenne empirique. On obtient :
$$\frac{\bar{x}}{\theta} = \frac{1-\bar{x}}{1-\theta}$$
$$\bar{x}(1-\theta) = \theta(1-\bar{x}) \implies \bar{x} - \bar{x}\theta = \theta - \theta\bar{x} \implies \theta = \bar{x}$$
La valeur optimale est la moyenne empirique $\hat{\theta} = \bar{x}$.
