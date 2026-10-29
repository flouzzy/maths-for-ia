# Exercice 3 : Moyenne empirique d'une loi continue \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X_1, \dots, X_{100}$ des variables aléatoires indépendantes suivant une loi uniforme continue sur l'intervalle $[0, 3]$.
On note $\bar{X}_{100} = \frac{1}{100} \sum_{i=1}^{100} X_i$ la moyenne empirique.
Déterminer approximativement la probabilité que la moyenne empirique s'éloigne de sa moyenne théorique de plus de $0.1$.

**Correction :**

Chaque $X_i$ suit $\mathcal{U}([0, 3])$.
L'espérance est $\mu = \frac{0 + 3}{2} = 1.5$.
La variance est $\sigma^2 = \frac{(3 - 0)^2}{12} = \frac{9}{12} = 0.75$.

On étudie la moyenne empirique $\bar{X}_{100}$. Son espérance est $\mathbb{E}[\bar{X}_{100}] = \mu = 1.5$, et sa variance est $\text{Var}(\bar{X}_{100}) = \frac{\sigma^2}{100} = \frac{0.75}{100} = 0.0075$.
L'écart-type de la moyenne empirique est $\sigma_{\bar{X}} = \sqrt{0.0075} \approx 0.0866$.

On cherche à évaluer $\mathbb{P}\left( |\bar{X}_{100} - 1.5| > 0.1 \right)$.
D'après le TCL, la variable $Z = \frac{\bar{X}_{100} - 1.5}{\sqrt{0.0075}}$ suit approximativement une loi $\mathcal{N}(0, 1)$.

L'inégalité se réécrit :
$$|\bar{X}_{100} - 1.5| > 0.1 \iff \left| \frac{\bar{X}_{100} - 1.5}{\sqrt{0.0075}} \right| > \frac{0.1}{\sqrt{0.0075}}$$
$$|Z| > \frac{0.1}{0.0866} \approx 1.1547$$

La probabilité recherchée est donc :
$$\mathbb{P}(|Z| > 1.155) = 2 \times (1 - \Phi(1.155))$$
On lit $\Phi(1.15) \approx 0.8749$ et $\Phi(1.16) \approx 0.8770$, donc $\Phi(1.155) \approx 0.876$.
La probabilité est donc environ $2 \times (1 - 0.876) = 2 \times 0.124 = 0.248$.
Il y a donc environ $24.8\%$ de chance que la moyenne empirique s'écarte de plus de $0.1$ de son espérance.
