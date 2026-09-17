## Exercice 6 : Divergence KL entre lois de Poisson (Variante 6) \quad $\bigstar\bigstar\bigstar\star\star$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{6})$ et $Q = \mathcal{P}(\mu_{6})$, avec $\lambda_{6} = 6$ et $\mu_{6} = 8$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{6}} \frac{\lambda_{6}^k}{k!}$ et $Q(X=k) = e^{-\mu_{6}} \frac{\mu_{6}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{6}} \lambda_{6}^k}{e^{-\mu_{6}} \mu_{6}^k} \right) = (\mu_{6} - \lambda_{6}) + k \ln\left(\frac{\lambda_{6}}{\mu_{6}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{6}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{6} - \lambda_{6}) + X \ln\left(\frac{\lambda_{6}}{\mu_{6}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{6} - \lambda_{6}) + \lambda_{6} \ln\left(\frac{\lambda_{6}}{\mu_{6}}\right) $$

3. Application numérique pour $\lambda_{6} = 6$ et $\mu_{6} = 8$ :
$$ D_{KL}(P \| Q) = (8 - 6) + 6 \ln\left(\frac{6}{8}\right) = 2 + 6 \ln\left(\frac{6}{8}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
