## Exercice 8 : Divergence KL entre lois de Poisson (Variante 8) \quad $\bigstar\bigstar\bigstar\bigstar\star$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{8})$ et $Q = \mathcal{P}(\mu_{8})$, avec $\lambda_{8} = 8$ et $\mu_{8} = 10$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{8}} \frac{\lambda_{8}^k}{k!}$ et $Q(X=k) = e^{-\mu_{8}} \frac{\mu_{8}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{8}} \lambda_{8}^k}{e^{-\mu_{8}} \mu_{8}^k} \right) = (\mu_{8} - \lambda_{8}) + k \ln\left(\frac{\lambda_{8}}{\mu_{8}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{8}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{8} - \lambda_{8}) + X \ln\left(\frac{\lambda_{8}}{\mu_{8}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{8} - \lambda_{8}) + \lambda_{8} \ln\left(\frac{\lambda_{8}}{\mu_{8}}\right) $$

3. Application numérique pour $\lambda_{8} = 8$ et $\mu_{8} = 10$ :
$$ D_{KL}(P \| Q) = (10 - 8) + 8 \ln\left(\frac{8}{10}\right) = 2 + 8 \ln\left(\frac{8}{10}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
