## Exercice 3 : Divergence KL entre lois de Poisson (Variante 3) \quad $\bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Soit $\mathcal{X} = \mathbb{N}$ avec la mesure de comptage.
Considérons deux lois de Poisson $P = \mathcal{P}(\lambda_{3})$ et $Q = \mathcal{P}(\mu_{3})$, avec $\lambda_{3} = 3$ et $\mu_{3} = 5$.
Calculez la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

\textbf{Correction :}
Les probabilités sont données par :
$P(X=k) = e^{-\lambda_{3}} \frac{\lambda_{3}^k}{k!}$ et $Q(X=k) = e^{-\mu_{3}} \frac{\mu_{3}^k}{k!}$.

1. Le log-ratio des probabilités est :
$$ \ln\left(\frac{P(X=k)}{Q(X=k)}\right) = \ln\left( \frac{e^{-\lambda_{3}} \lambda_{3}^k}{e^{-\mu_{3}} \mu_{3}^k} \right) = (\mu_{3} - \lambda_{3}) + k \ln\left(\frac{\lambda_{3}}{\mu_{3}}\right) $$

2. On prend l'espérance sous la loi $P$. On sait que pour une loi de Poisson, $\mathbb{E}_P[X] = \lambda_{3}$.
$$ D_{KL}(P \| Q) = \mathbb{E}_P\left[ (\mu_{3} - \lambda_{3}) + X \ln\left(\frac{\lambda_{3}}{\mu_{3}}\right) \right] $$
$$ D_{KL}(P \| Q) = (\mu_{3} - \lambda_{3}) + \lambda_{3} \ln\left(\frac{\lambda_{3}}{\mu_{3}}\right) $$

3. Application numérique pour $\lambda_{3} = 3$ et $\mu_{3} = 5$ :
$$ D_{KL}(P \| Q) = (5 - 3) + 3 \ln\left(\frac{3}{5}\right) = 2 + 3 \ln\left(\frac{3}{5}\right) $$
Puisque $\ln(1 - x) < 0$, ce terme est négatif, mais globalement la somme reste strictement positive par l'inégalité de Gibbs.
