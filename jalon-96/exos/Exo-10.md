Niveau de difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Considérons une modélisation paramétrique où $Q_\theta$ est une famille exponentielle. Déduisez les conditions d'optimalité pour la minimisation de la Cross-Entropy et faites le lien avec le Maximum de Vraisemblance (MLE).

**Corrigé :**
Soit un modèle de famille exponentielle de la forme $q_\theta(x) = h(x) \exp(\langle \theta, T(x) \rangle - A(\theta))$, où $\theta$ est le paramètre naturel, $T(x)$ la statistique exhaustive, et $A(\theta)$ la fonction de partition log-normale.
La fonction objectif à minimiser (entropie croisée empirique sur un échantillon de taille $n$) est :
$$\hat{L}(\theta) = - \frac{1}{n} \sum_{i=1}^n \ln q_\theta(x_i)$$
En substituant la forme de la famille exponentielle :
$$\hat{L}(\theta) = - \frac{1}{n} \sum_{i=1}^n \left( \ln h(x_i) + \langle \theta, T(x_i) \rangle - A(\theta) \right)$$
$$\hat{L}(\theta) = - \frac{1}{n} \sum_{i=1}^n \ln h(x_i) - \langle \theta, \frac{1}{n} \sum_{i=1}^n T(x_i) \rangle + A(\theta)$$
Pour trouver le minimum, on annule le gradient par rapport à $\theta$ :
$$\nabla_\theta \hat{L}(\theta) = - \frac{1}{n} \sum_{i=1}^n T(x_i) + \nabla_\theta A(\theta) = 0$$
Une propriété fondamentale des familles exponentielles est que $\nabla_\theta A(\theta) = \mathbb{E}_{X \sim Q_\theta}[T(X)]$.
Ainsi, la condition d'optimalité est :
$$\mathbb{E}_{X \sim Q_\theta}[T(X)] = \frac{1}{n} \sum_{i=1}^n T(x_i)$$
Cette équation signifie que le paramètre optimal $\theta^*$ est celui pour lequel l'espérance de la statistique exhaustive sous le modèle $Q_{\theta^*}$ correspond à la moyenne empirique de cette même statistique calculée sur l'échantillon d'entraînement.
Cette méthode d'estimation correspond très exactement à la méthode du Maximum de Vraisemblance, car minimiser l'entropie croisée empirique est mathématiquement identique à la maximisation de la log-vraisemblance des données sous le modèle $Q_\theta$.
