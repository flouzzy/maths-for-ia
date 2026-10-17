# Exercice 05

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
On tire indépendamment une suite de points $(U_i, V_i)$ uniformément sur le carré $[0, 1] \times [0, 1]$.
On définit la variable indicatrice $Z_i = \mathbf{1}_{U_i^2 + V_i^2 \le 1}$.
On pose $\Pi_n = \frac{4}{n} \sum_{i=1}^n Z_i$.
1. Donner l'espérance $\mathbb{E}[Z_1]$.
2. Justifier que $\Pi_n$ converge presque sûrement vers $\pi$.

**Correction :**
1. La probabilité que le point $(U_i, V_i)$ tombe dans le quart de disque unité (équation $x^2 + y^2 \le 1, x\ge 0, y\ge 0$) est donnée par le rapport des aires :
Aire du quart de disque = $\frac{\pi \times 1^2}{4} = \frac{\pi}{4}$.
Aire du carré = $1 \times 1 = 1$.
Donc $\mathbb{P}(U_i^2 + V_i^2 \le 1) = \frac{\pi}{4}$.
Comme $Z_i$ est une variable de Bernoulli, son espérance est $\mathbb{E}[Z_1] = \mathbb{P}(Z_1 = 1) = \frac{\pi}{4}$.
2. Les points $(U_i, V_i)$ étant tirés de manière indépendante, les variables $Z_i$ sont I.I.D.
Leur espérance existe et est finie ($\frac{\pi}{4}$).
D'après la LFGN, la moyenne empirique $\frac{1}{n} \sum_{i=1}^n Z_i$ converge presque sûrement vers $\mathbb{E}[Z_1] = \frac{\pi}{4}$.
Par multiplication par 4 (la convergence p.s. est préservée par multiplication par un scalaire),
$\Pi_n = 4 \times \frac{1}{n} \sum_{i=1}^n Z_i \xrightarrow{p.s.} 4 \times \frac{\pi}{4} = \pi$.
La suite $\Pi_n$ converge presque sûrement vers $\pi$.
