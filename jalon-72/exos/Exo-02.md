# Exercice 2 : KL entre deux Gaussiennes $\quad \bigstar\bigstar\star\star\star$

\textbf{Énoncé :}
Calculer $D_{KL}(P \| Q)$ pour $P = \mathcal{N}(\mu_1, \sigma^2)$ et $Q = \mathcal{N}(\mu_2, \sigma^2)$.

\textbf{Correction :}
1. Posons les densités $p(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu_1)^2}{2\sigma^2}\right)$ et $q(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu_2)^2}{2\sigma^2}\right)$.
2. Calculons le log-ratio :
   $$\ln\left(\frac{p(x)}{q(x)}\right) = -\frac{(x-\mu_1)^2}{2\sigma^2} + \frac{(x-\mu_2)^2}{2\sigma^2}$$
   $$= \frac{1}{2\sigma^2} \left[ x^2 - 2\mu_2 x + \mu_2^2 - (x^2 - 2\mu_1 x + \mu_1^2) \right]$$
   $$= \frac{1}{2\sigma^2} \left[ 2x(\mu_1 - \mu_2) + \mu_2^2 - \mu_1^2 \right]$$
3. On intègre par rapport à $P(x)dx$ (l'espérance) :
   $$D_{KL}(P \| Q) = \mathbb{E}_{X \sim P}\left[ \frac{1}{2\sigma^2} \left( 2X(\mu_1 - \mu_2) + \mu_2^2 - \mu_1^2 \right) \right]$$
   Comme $\mathbb{E}[X] = \mu_1$ :
   $$D_{KL}(P \| Q) = \frac{1}{2\sigma^2} \left( 2\mu_1(\mu_1 - \mu_2) + \mu_2^2 - \mu_1^2 \right)$$
   $$= \frac{1}{2\sigma^2} \left( 2\mu_1^2 - 2\mu_1\mu_2 + \mu_2^2 - \mu_1^2 \right) = \frac{(\mu_1 - \mu_2)^2}{2\sigma^2}$$
