## Exercice 10 : Divergence KL entre lois de Poisson (Variante 10) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{10})$ et $Q = \mathcal{P}(\mu_{10})$, avec $\lambda_{10} = 10$ et $\mu_{10} = 12$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{10}} \frac{\lambda_{10}^k}{k!}$ et $Q(X=k) = e^{-\mu_{10}} \frac{\mu_{10}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{10}} \lambda_{10}^k}{e^{-\mu_{10}} \mu_{10}^k} \right) = (\mu_{10} - \lambda_{10}) + k \ln\left(\frac{\lambda_{10}}{\mu_{10}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{10}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{10} - \lambda_{10}) + X \ln\left(\frac{\lambda_{10}}{\mu_{10}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{10} - \lambda_{10}) + \lambda_{10} \ln\left(\frac{\lambda_{10}}{\mu_{10}}\right) $$

3. Application numérique pour $\lambda_{10} = 10$ et $\mu_{10} = 12$ :
$$ D_{KL}(P \| Q) = (12 - 10) + 10 \ln\left(\frac{10}{12}\right) = 2 + 10 \ln\left(\frac{10}{12}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
