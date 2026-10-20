# Exercice 9 : Entropie d'une distribution Gaussienne Multivariée

$\bigstar\bigstar\bigstar\bigstar\bigstar$


Soit un vecteur aléatoire $X \in \mathbb{R}^d$ suivant une distribution normale multivariée $\mathcal{N}(\mu, \Sigma)$, avec $\Sigma$ une matrice de covariance symétrique définie positive.
La densité de probabilité est :
$$p(x) = \frac{1}{\sqrt{(2\pi)^d \det(\Sigma)}} \exp\left( -\frac{1}{2} (x-\mu)^T \Sigma^{-1} (x-\mu) \right)$$

**1.** Démontrer que l'entropie différentielle de cette source est $H(X) = \frac{1}{2} \ln \left( (2\pi e)^d \det(\Sigma) \right)$.
**2.** Si un modèle approximait cette source avec une gaussienne d'une autre covariance, qu'adviendrait-il de l'entropie croisée ?

**Correction :**

**1.** L'entropie différentielle est $H(X) = \mathbb{E}_{X \sim P}[-\ln p(X)]$.
Calculons $-\ln p(X)$ :
$$-\ln p(X) = \ln \left( \sqrt{(2\pi)^d \det(\Sigma)} \right) + \frac{1}{2} (X-\mu)^T \Sigma^{-1} (X-\mu)$$
L'espérance est linéaire, donc :
$$H(X) = \frac{1}{2} \ln \left( (2\pi)^d \det(\Sigma) \right) + \frac{1}{2} \mathbb{E} \left[ (X-\mu)^T \Sigma^{-1} (X-\mu) \right]$$
Le second terme est l'espérance d'une forme quadratique. En utilisant la trace, on a :
$$\mathbb{E} \left[ (X-\mu)^T \Sigma^{-1} (X-\mu) \right] = \mathbb{E} \left[ \text{Tr}\left( (X-\mu)^T \Sigma^{-1} (X-\mu) \right) \right]$$
Par invariance cyclique de la trace :
$$\mathbb{E} \left[ \text{Tr}\left( \Sigma^{-1} (X-\mu)(X-\mu)^T \right) \right] = \text{Tr}\left( \Sigma^{-1} \mathbb{E}[(X-\mu)(X-\mu)^T] \right)$$
Or, par définition de la matrice de covariance, $\mathbb{E}[(X-\mu)(X-\mu)^T] = \Sigma$.
Donc :
$$\text{Tr}(\Sigma^{-1} \Sigma) = \text{Tr}(I_d) = d$$
Ainsi, l'entropie est :
$$H(X) = \frac{1}{2} \ln \left( (2\pi)^d \det(\Sigma) \right) + \frac{d}{2}$$
Puisque $\frac{d}{2} = \frac{1}{2} \ln(e^d)$, nous pouvons regrouper les logarithmes :
$$H(X) = \frac{1}{2} \ln \left( (2\pi e)^d \det(\Sigma) \right)$$

**2.** Si le modèle approxime la source avec une distribution normale de même moyenne mais de covariance $\Sigma'$, la divergence KL sera non nulle. L'entropie croisée sera strictement supérieure à $H(X)$ (la perte sera sous-optimale), mesurant le coût d'encoder la véritable distribution avec des paramètres de covariance incorrects.
