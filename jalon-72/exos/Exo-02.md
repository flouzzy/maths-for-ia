## Exercice 2 : Divergence KL entre lois de Poisson (Variante 2) \quad $\bigstar\star\star\star\star$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{2})$ et $Q = \mathcal{P}(\mu_{2})$, avec $\lambda_{2} = 2$ et $\mu_{2} = 4$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{2}} \frac{\lambda_{2}^k}{k!}$ et $Q(X=k) = e^{-\mu_{2}} \frac{\mu_{2}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{2}} \lambda_{2}^k}{e^{-\mu_{2}} \mu_{2}^k} \right) = (\mu_{2} - \lambda_{2}) + k \ln\left(\frac{\lambda_{2}}{\mu_{2}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{2}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{2} - \lambda_{2}) + X \ln\left(\frac{\lambda_{2}}{\mu_{2}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{2} - \lambda_{2}) + \lambda_{2} \ln\left(\frac{\lambda_{2}}{\mu_{2}}\right) $$

3. Application numérique pour $\lambda_{2} = 2$ et $\mu_{2} = 4$ :
$$ D_{KL}(P \| Q) = (4 - 2) + 2 \ln\left(\frac{2}{4}\right) = 2 + 2 \ln\left(\frac{2}{4}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
