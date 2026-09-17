## Exercice 7 : Divergence KL et vraisemblance \quad $\bigstar\bigstar\bigstar$
### Énoncé
Montrez que la maximisation de la log-vraisemblance équivaut à minimiser la divergence KL empirique.
### Correction
Soit $P_{emp}$ la distribution empirique. $D_{KL}(P_{emp} || Q_\theta) = \sum P_{emp}(x) \ln\frac{P_{emp}(x)}{Q_\theta(x)}$.
Minimiser ceci par rapport à $\theta$ revient à maximiser $\sum P_{emp}(x) \ln Q_\theta(x) = \frac{1}{N} \sum_{i=1}^N \ln Q_\theta(x_i)$, qui est la log-vraisemblance.
