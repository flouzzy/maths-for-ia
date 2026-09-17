# Exercice 6 : VAE et KL $\quad \bigstar\bigstar\bigstar\bigstar\star$

\textbf{Énoncé :}
Dans un VAE (Variational Auto-Encoder), on calcule la KL entre $q_\phi(z|x) = \mathcal{N}(\mu, \sigma^2)$ et $p(z) = \mathcal{N}(0, 1)$. Calculer cette valeur.

\textbf{Correction :}
C'est un cas particulier de l'exercice 2 avec des variances différentes.
$p(z) = \mathcal{N}(0, 1)$, donc $\ln p(z) = -\frac{1}{2}\ln(2\pi) - \frac{z^2}{2}$.
$q(z) = \mathcal{N}(\mu, \sigma^2)$, donc $\ln q(z) = -\frac{1}{2}\ln(2\pi\sigma^2) - \frac{(z-\mu)^2}{2\sigma^2}$.
$$D_{KL}(q \| p) = \mathbb{E}_q [ \ln q(z) - \ln p(z) ]$$
$$= \mathbb{E}_q \left[ -\frac{1}{2}\ln(2\pi\sigma^2) - \frac{(z-\mu)^2}{2\sigma^2} + \frac{1}{2}\ln(2\pi) + \frac{z^2}{2} \right]$$
$$= -\frac{1}{2}\ln(\sigma^2) - \frac{1}{2\sigma^2} \mathbb{E}_q[(z-\mu)^2] + \frac{1}{2} \mathbb{E}_q[z^2]$$
On sait que $\mathbb{E}_q[(z-\mu)^2] = \sigma^2$ et $\mathbb{E}_q[z^2] = \mu^2 + \sigma^2$.
$$= -\frac{1}{2}\ln(\sigma^2) - \frac{1}{2} + \frac{1}{2}(\mu^2 + \sigma^2)$$
$$D_{KL}(q \| p) = \frac{1}{2} \left( \sigma^2 + \mu^2 - 1 - \ln(\sigma^2) \right)$$
C'est la fameuse "loss KL" utilisée dans les VAEs.
