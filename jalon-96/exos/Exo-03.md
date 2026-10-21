# Exercice 3 : Entropie d'une loi de Poisson

$\bigstar\bigstar\star\star\star$


Soit $X$ une variable aléatoire suivant une loi de Poisson de paramètre $\lambda > 0$, $X \sim \mathcal{P}(\lambda)$.

**1.** Exprimer l'entropie de Shannon $H(X)$ sous forme d'une série.
**2.** Montrer que si $\lambda$ est très grand, une approximation par la formule de Stirling pourrait lier cette entropie à l'entropie d'une loi normale discrétisée.

**Correction :**

**1.** La fonction de masse de probabilité de la loi de Poisson est $P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}$ pour $k \in \mathbb{N}$.
L'entropie de Shannon (en nats) est :
$$H(X) = - \sum_{k=0}^{\infty} P(X=k) \ln(P(X=k))$$
Développons le logarithme :
$$\ln(P(X=k)) = \ln(e^{-\lambda} \frac{\lambda^k}{k!}) = -\lambda + k \ln \lambda - \ln(k!)$$
En substituant dans l'expression de l'entropie :
$$H(X) = - \sum_{k=0}^{\infty} P(X=k) (-\lambda + k \ln \lambda - \ln(k!))$$
Par la linéarité de l'espérance, on obtient :
$$H(X) = \lambda - (\mathbb{E}[X] \ln \lambda) + \mathbb{E}[\ln(X!)]$$
Puisque pour une loi de Poisson, $\mathbb{E}[X] = \lambda$, cela se simplifie en :
$$H(X) = \lambda(1 - \ln \lambda) + e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k \ln(k!)}{k!}$$

**2.** Pour $\lambda \to \infty$, l'approximation de Stirling donne $\ln(k!) \approx k \ln k - k$. De plus, la loi de Poisson converge vers une loi normale $\mathcal{N}(\lambda, \lambda)$. L'entropie tend asymptotiquement vers celle d'une gaussienne, soit $H(X) \approx \frac{1}{2} \ln(2\pi e \lambda)$.
