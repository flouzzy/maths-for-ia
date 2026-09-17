## Exercice 4 : Divergence KL entre lois de Poisson (Variante 4) \quad $\bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{4})$ et $Q = \mathcal{P}(\mu_{4})$, avec $\lambda_{4} = 4$ et $\mu_{4} = 6$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{4}} \frac{\lambda_{4}^k}{k!}$ et $Q(X=k) = e^{-\mu_{4}} \frac{\mu_{4}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{4}} \lambda_{4}^k}{e^{-\mu_{4}} \mu_{4}^k} \right) = (\mu_{4} - \lambda_{4}) + k \ln\left(\frac{\lambda_{4}}{\mu_{4}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{4}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{4} - \lambda_{4}) + X \ln\left(\frac{\lambda_{4}}{\mu_{4}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{4} - \lambda_{4}) + \lambda_{4} \ln\left(\frac{\lambda_{4}}{\mu_{4}}\right) $$

3. Application numérique pour $\lambda_{4} = 4$ et $\mu_{4} = 6$ :
$$ D_{KL}(P \| Q) = (6 - 4) + 4 \ln\left(\frac{4}{6}\right) = 2 + 4 \ln\left(\frac{4}{6}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
