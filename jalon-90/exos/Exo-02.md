# Exercice 02

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Non-convergence dans L1 avec convergence p.s.

Construisez explicitement une suite de variables aléatoires $(X_n)_{n \in \mathbb{N}^*}$ qui converge presque sûrement vers $0$, mais qui diverge vers $+\infty$ dans $L^1$.

**Correction exhaustive :**
Considérons l'espace probabilisé usuel $(\Omega, \mathcal{F}, \mathbb{P}) = ([0, 1], \mathcal{B}([0, 1]), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Définissons la variable aléatoire $X_n : \Omega \to \mathbb{R}$ par :
$$ X_n(\omega) = n^2 \mathbf{1}_{\left[0, \frac{1}{n}\right]}(\omega) $$
Étudions la convergence presque sûre :
Fixons $\omega \in ]0, 1]$. Par la propriété d'Archimède, il existe un entier $N \ge 1$ tel que $\frac{1}{N} < \omega$.
Pour tout $n \ge N$, $\omega \notin \left[0, \frac{1}{n}\right]$, ce qui implique $X_n(\omega) = 0$.
Par conséquent, $\lim_{n \to \infty} X_n(\omega) = 0$ pour tout $\omega \in ]0, 1]$.
L'événement sur lequel la convergence n'a pas lieu est contenu dans $\{0\}$, qui est de mesure de Lebesgue nulle ($\lambda(\{0\}) = 0$).
Ainsi, $X_n \xrightarrow{p.s.} 0$.

Calculons l'espérance de $X_n$ (norme $L^1$) :
$$ \mathbb{E}[|X_n|] = \int_0^1 n^2 \mathbf{1}_{\left[0, \frac{1}{n}\right]}(\omega) \, d\lambda(\omega) = n^2 \cdot \lambda\left(\left[0, \frac{1}{n}\right]\right) = n^2 \cdot \frac{1}{n} = n $$
Lorsque $n \to \infty$, $\mathbb{E}[|X_n|] = n \to +\infty$.
La suite diverge donc grossièrement dans $L^1$, bien qu'elle s'écrase presque partout. Ceci illustre la rupture de l'uniforme intégrabilité.
