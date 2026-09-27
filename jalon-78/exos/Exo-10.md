# Exo 10 : Problème de Synthèse : Chaleur sur un anneau

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\bigstar


Considérons une tige métallique circulaire de longueur $2\pi$ (paramétrée par un angle $x \in [-\pi, \pi]$).
La température à la position $x$ et au temps $t \ge 0$ est $u(x,t)$. Elle vérifie l'équation de la chaleur :
$$ \frac{\partial u}{\partial t}(x,t) = \alpha \frac{\partial^2 u}{\partial x^2}(x,t) $$
avec $\alpha > 0$.
La condition initiale est un profil de température $u(x,0) = f(x)$.

En supposant qu'à chaque instant $t$, la fonction $x \mapsto u(x,t)$ peut être développée en série de Fourier spatiale, déterminer l'expression formelle de $u(x,t)$ en fonction des $c_n(f)$.

## Correction

Puisque la tige est circulaire de longueur $2\pi$, la fonction $x \mapsto u(x,t)$ est $2\pi$-périodique en $x$.
On peut écrire pour tout instant $t$, si on suppose la régularité nécessaire :
$$ u(x,t) = \sum_{n=-\infty}^{+\infty} C_n(t) e^{inx} $$
Les coefficients de Fourier $C_n$ dépendent désormais du temps $t$.

Injectons cette forme supposée dans l'équation de la chaleur.
On calcule la dérivée temporelle (en dérivant terme à terme, ce qu'on suppose légitime) :
$$ \frac{\partial u}{\partial t}(x,t) = \sum_{n=-\infty}^{+\infty} C_n'(t) e^{inx} $$

On calcule la dérivée spatiale seconde :
La dérivée première en $x$ multiplie le terme par $in$.
La dérivée seconde en $x$ multiplie par $(in)^2 = -n^2$.
$$ \frac{\partial^2 u}{\partial x^2}(x,t) = \sum_{n=-\infty}^{+\infty} (-n^2) C_n(t) e^{inx} $$

L'équation de la chaleur devient :
$$ \sum_{n=-\infty}^{+\infty} C_n'(t) e^{inx} = \alpha \sum_{n=-\infty}^{+\infty} (-n^2) C_n(t) e^{inx} $$
$$ \sum_{n=-\infty}^{+\infty} \left( C_n'(t) + \alpha n^2 C_n(t) \right) e^{inx} = 0 $$

Puisque la famille $(e^{inx})$ forme une base (les fonctions sont orthogonales), la seule façon pour que cette série soit nulle pour tout $x$ est que chaque coefficient soit nul.
Pour tout $n \in \mathbb{Z}$ :
$$ C_n'(t) + \alpha n^2 C_n(t) = 0 $$

C'est une équation différentielle linéaire ordinaire d'ordre 1 en $t$, à coefficients constants. Sa solution générale est :
$$ C_n(t) = C_n(0) e^{-\alpha n^2 t} $$

Or, à $t=0$, la condition initiale est $u(x,0) = f(x)$. La série de Fourier de $f$ est $f(x) = \sum c_n(f) e^{inx}$.
Donc, par identification, $C_n(0) = c_n(f)$.

La solution générale du problème de diffusion de la chaleur est formellement :
$$ u(x,t) = \sum_{n=-\infty}^{+\infty} c_n(f) e^{-\alpha n^2 t} e^{inx} $$

**Analyse Physique :**
- Le terme $e^{-\alpha n^2 t}$ est un facteur d'atténuation.
- Pour $n=0$ (la moyenne de la température), le terme est $c_0(f) e^0 = c_0(f)$. La température moyenne se conserve.
- Pour $n$ grand (les hautes fréquences, représentant des pics et des creux très rapprochés), le terme $n^2$ rend l'atténuation $e^{-\alpha n^2 t}$ extrêmement rapide.
- C'est l'essence du lissage de la chaleur : les variations brutales spatiales (grand $n$) s'estompent presque instantanément, conduisant rapidement à une température uniforme $c_0(f)$.
