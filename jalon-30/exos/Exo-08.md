# Exercice 8 : Dunford et Systèmes Dynamiques Récurrents (★★★★)

On modélise un Réseau de Neurones Récurrent (RNN) linéaire simplifié évoluant à temps discret selon $h_{t+1} = W h_t$.
La matrice des poids synaptiques est $W = \begin{pmatrix} 0.5 & 1 \\ 0 & 0.5 \end{pmatrix}$.
Trouver la décomposition de Dunford de $W$, et donner l'expression analytique de l'état du réseau $h_t$ en fonction de l'état initial $h_0 = (1, 1)^T$.
Analyser le comportement limite lorsque $t \to +\infty$.

### Solution :

**Étape 1 : Décomposition de Dunford de $W$**
La matrice $W$ est triangulaire supérieure, ses valeurs propres se lisent sur la diagonale : $\lambda = 0.5$ (de multiplicité 2).
La décomposition de Dunford évidente est $W = D + N$ avec :
$D = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix} = 0.5 I_2$
$N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$
$D$ est diagonale, $N^2 = 0$ donc nilpotente, et $DN = ND$ car $D$ est scalaire.

**Étape 2 : Évolution de l'état $h_t$**
L'évolution récurrente donne $h_t = W^t h_0$.
Calculons $W^t = (D + N)^t$. Puisque $D$ et $N$ commutent :
$W^t = \sum_{k=0}^{t} \binom{t}{k} D^{t-k} N^k$
Comme $N^2 = 0$, la somme se restreint à $k=0$ et $k=1$ (pour $t \geq 1$) :
$W^t = D^t + t D^{t-1} N$
$D^t = (0.5)^t I_2$
$D^{t-1} N = (0.5)^{t-1} I_2 N = (0.5)^{t-1} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$
Donc $W^t = \begin{pmatrix} 0.5^t & t \cdot 0.5^{t-1} \\ 0 & 0.5^t \end{pmatrix}$.

Appliquons cette matrice à $h_0$ :
$$ h_t = \begin{pmatrix} 0.5^t & t \cdot 0.5^{t-1} \\ 0 & 0.5^t \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0.5^t + t \cdot 0.5^{t-1} \\ 0.5^t \end{pmatrix} $$

**Étape 3 : Analyse limite**
Regardons la limite de chaque composante lorsque $t \to +\infty$.
La deuxième composante est $(0.5)^t$. Or $|0.5| < 1$, donc $\lim_{t \to +\infty} 0.5^t = 0$.
La première composante est $0.5^t + 2t \cdot 0.5^t = (1+2t)(0.5)^t$.
Par croissance comparée (les puissances l'emportent sur les polynômes en l'infini), la limite de $t \cdot (0.5)^t$ est $0$.
Donc $\lim_{t \to +\infty} h_t = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.

*Note IA:* Bien que l'état tende vers $0$, le terme $t \cdot \lambda^{t-1}$ introduit par la composante nilpotente est fondamental dans l'étude de "l'explosion ou la disparition du gradient" (vanishing/exploding gradient) lors de la rétropropagation à travers le temps (BPTT). C'est ce terme polynomial multiplicatif qui retarde l'évanouissement exponentiel de l'information.
