# Exercice 09

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(T_n)_{n \ge 1}$ une suite de variables I.I.D. strictement positives, d'espérance $\mu = \mathbb{E}[T_1] > 0$.
Posons $S_0 = 0$ et $S_n = \sum_{i=1}^n T_i$. $S_n$ représente l'instant du $n$-ième événement (processus de renouvellement).
Soit $N(t) = \max \{ n \in \mathbb{N} \mid S_n \le t \}$ le nombre d'événements jusqu'à l'instant $t$.
Montrer rigoureusement que $\lim_{t \to +\infty} \frac{N(t)}{t} = \frac{1}{\mu}$ presque sûrement.

**Correction :**
1. Par définition de $N(t)$, l'événement $N(t)$ est encadré par les instants d'arrivées :
$S_{N(t)} \le t < S_{N(t)+1}$.
2. Divisons cette double inégalité par $N(t)$ (valable pour $t$ assez grand de sorte que $N(t) \ge 1$) :
$\frac{S_{N(t)}}{N(t)} \le \frac{t}{N(t)} < \frac{S_{N(t)+1}}{N(t)+1} \frac{N(t)+1}{N(t)}$.
3. Par hypothèse, $T_1 > 0$ p.s. implique $\lim_{n \to \infty} S_n = +\infty$ p.s.
Par suite, quand $t \to +\infty$, le nombre d'événements $N(t)$ tend vers $+\infty$ p.s.
4. La LFGN s'applique à la suite $(T_i)$ :
$\lim_{n \to \infty} \frac{S_n}{n} = \mu$ p.s.
Puisque $N(t) \to \infty$ quand $t \to \infty$, par composition des limites des suites, on a :
$\lim_{t \to \infty} \frac{S_{N(t)}}{N(t)} = \mu$ p.s.
De même, $\lim_{t \to \infty} \frac{S_{N(t)+1}}{N(t)+1} = \mu$ p.s., et $\lim_{t \to \infty} \frac{N(t)+1}{N(t)} = 1$.
5. En passant à la limite dans les encadrements (théorème des gendarmes) :
$\mu \le \liminf_{t \to \infty} \frac{t}{N(t)} \le \limsup_{t \to \infty} \frac{t}{N(t)} \le \mu \times 1$.
Donc $\lim_{t \to \infty} \frac{t}{N(t)} = \mu$ p.s.
6. En prenant l'inverse, on obtient le résultat :
$\lim_{t \to \infty} \frac{N(t)}{t} = \frac{1}{\mu}$ p.s.
