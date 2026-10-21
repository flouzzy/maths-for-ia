Niveau de difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Considérons une fonction de perte empirique $\hat{H}_n(\theta) = - \frac{1}{n} \sum_{i=1}^n \ln q_\theta(x_i)$ calculée sur un échantillon i.i.d. tiré d'une distribution $P$.
Démontrez que l'espérance de la perte empirique est l'entropie croisée théorique $H(P, Q_\theta)$.

**Corrigé :**
Par définition de la perte empirique, nous avons :
$$\hat{H}_n(\theta) = - \frac{1}{n} \sum_{i=1}^n \ln q_\theta(X_i)$$
où les variables aléatoires $X_1, \dots, X_n$ sont identiquement distribuées selon $P$.
Par la linéarité de l'espérance :
$$\mathbb{E}_P[\hat{H}_n(\theta)] = \mathbb{E}_P\left[ - \frac{1}{n} \sum_{i=1}^n \ln q_\theta(X_i) \right] = - \frac{1}{n} \sum_{i=1}^n \mathbb{E}_P[ \ln q_\theta(X_i) ]$$
Puisque les variables sont identiquement distribuées, elles ont toutes la même espérance :
$$\mathbb{E}_P[ \ln q_\theta(X_i) ] = \int \ln q_\theta(x) p(x) dx$$
Donc :
$$\mathbb{E}_P[\hat{H}_n(\theta)] = - \frac{1}{n} \times n \times \mathbb{E}_P[ \ln q_\theta(X) ] = - \mathbb{E}_P[ \ln q_\theta(X) ]$$
Ce qui correspond exactement à la définition de l'entropie croisée :
$$H(P, Q_\theta) = - \mathbb{E}_{X \sim P}[\ln q_\theta(X)]$$
Ainsi, la perte empirique est un estimateur sans biais de l'entropie croisée théorique.
