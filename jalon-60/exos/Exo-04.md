# Exercice 4 : Propriété Discriminatoire $\bigstar\bigstar\bigstar\star\star$
Soit $\mu$ une mesure signée finie sur $\mathbb{R}$. Supposons que $\int_{\mathbb{R}} \exp(i w x) d\mu(x) = 0$ pour tout $w \in \mathbb{R}$. En déduire que $\mu = 0$.

\textbf{Correction détaillée}
L'hypothèse indique que la transformée de Fourier de la mesure $\mu$, notée $\mathcal{F}(\mu)(w) = \int_{\mathbb{R}} e^{-iwx} d\mu(x)$, est identiquement nulle pour tout $w \in \mathbb{R}$.
L'espace des mesures régulières signées finies sur $\mathbb{R}$ correspond au dual de l'espace des fonctions continues s'annulant à l'infini $C_0(\mathbb{R})$.
L'application qui à une mesure associe sa transformée de Fourier est injective. (Théorème d'inversion de Fourier étendu aux mesures, ou densité de l'algèbre engendrée par les caractères exponentiels via Stone-Weierstrass complexe sur la compactification).
Puisque $\mathcal{F}(\mu) = 0$, on conclut immédiatement que $\mu = 0$.
Cette propriété est cruciale dans la preuve de Cybenko lorsque l'on exprime la sigmoïde comme une superposition de fonctions exponentielles complexes (via la transformée de Fourier).
