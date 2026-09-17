## Exercice 7 : Divergence KL entre lois de Poisson (Variante 7) \quad $\bigstar\bigstar\bigstar\bigstar\star$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{7})$ et $Q = \mathcal{P}(\mu_{7})$, avec $\lambda_{7} = 7$ et $\mu_{7} = 9$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{7}} \frac{\lambda_{7}^k}{k!}$ et $Q(X=k) = e^{-\mu_{7}} \frac{\mu_{7}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{7}} \lambda_{7}^k}{e^{-\mu_{7}} \mu_{7}^k} \right) = (\mu_{7} - \lambda_{7}) + k \ln\left(\frac{\lambda_{7}}{\mu_{7}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{7}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{7} - \lambda_{7}) + X \ln\left(\frac{\lambda_{7}}{\mu_{7}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{7} - \lambda_{7}) + \lambda_{7} \ln\left(\frac{\lambda_{7}}{\mu_{7}}\right) $$

3. Application numérique pour $\lambda_{7} = 7$ et $\mu_{7} = 9$ :
$$ D_{KL}(P \| Q) = (9 - 7) + 7 \ln\left(\frac{7}{9}\right) = 2 + 7 \ln\left(\frac{7}{9}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
