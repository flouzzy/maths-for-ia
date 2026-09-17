## Exercice 9 : Divergence KL entre lois de Poisson (Variante 9) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{9})$ et $Q = \mathcal{P}(\mu_{9})$, avec $\lambda_{9} = 9$ et $\mu_{9} = 11$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{9}} \frac{\lambda_{9}^k}{k!}$ et $Q(X=k) = e^{-\mu_{9}} \frac{\mu_{9}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{9}} \lambda_{9}^k}{e^{-\mu_{9}} \mu_{9}^k} \right) = (\mu_{9} - \lambda_{9}) + k \ln\left(\frac{\lambda_{9}}{\mu_{9}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{9}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{9} - \lambda_{9}) + X \ln\left(\frac{\lambda_{9}}{\mu_{9}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{9} - \lambda_{9}) + \lambda_{9} \ln\left(\frac{\lambda_{9}}{\mu_{9}}\right) $$

3. Application numérique pour $\lambda_{9} = 9$ et $\mu_{9} = 11$ :
$$ D_{KL}(P \| Q) = (11 - 9) + 9 \ln\left(\frac{9}{11}\right) = 2 + 9 \ln\left(\frac{9}{11}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
