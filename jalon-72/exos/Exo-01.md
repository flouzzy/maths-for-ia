## Exercice 1 : Divergence KL entre lois de Poisson (Variante 1) \quad $\bigstar\star\star\star\star$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{1})$ et $Q = \mathcal{P}(\mu_{1})$, avec $\lambda_{1} = 1$ et $\mu_{1} = 3$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{1}} \frac{\lambda_{1}^k}{k!}$ et $Q(X=k) = e^{-\mu_{1}} \frac{\mu_{1}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{1}} \lambda_{1}^k}{e^{-\mu_{1}} \mu_{1}^k} \right) = (\mu_{1} - \lambda_{1}) + k \ln\left(\frac{\lambda_{1}}{\mu_{1}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{1}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{1} - \lambda_{1}) + X \ln\left(\frac{\lambda_{1}}{\mu_{1}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{1} - \lambda_{1}) + \lambda_{1} \ln\left(\frac{\lambda_{1}}{\mu_{1}}\right) $$

3. Application numérique pour $\lambda_{1} = 1$ et $\mu_{1} = 3$ :
$$ D_{KL}(P \| Q) = (3 - 1) + 1 \ln\left(\frac{1}{3}\right) = 2 + 1 \ln\left(\frac{1}{3}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
