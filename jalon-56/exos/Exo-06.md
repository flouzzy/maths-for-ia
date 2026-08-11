## Exercice 6 : Complétude et suites de Cauchy (Intermédiaire) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Montrer que l'espace $\mathcal{C}([0,1], \mathbb{R})$ muni de la norme $\|\cdot\|_\infty$ est complet.

\textbf{Correction Détaillée :}
1. Soit $(f_n)$ une suite de Cauchy dans $\mathcal{C}([0,1], \mathbb{R})$.
2. Pour chaque $x \in [0,1]$, $|f_p(x) - f_q(x)| \leq \|f_p - f_q\|_\infty$.
3. La suite de réels $(f_n(x))$ est donc de Cauchy dans $\mathbb{R}$. Comme $\mathbb{R}$ est complet, elle converge vers un réel qu'on note $f(x)$.
4. Montrons la convergence uniforme. Soit $\epsilon > 0$. Il existe $N$ tel que pour $p, q \ge N$ et $x \in [0,1]$, $|f_p(x) - f_q(x)| < \epsilon/2$.
5. Fixons $p \ge N$ et passons à la limite quand $q \to \infty$ : $|f_p(x) - f(x)| \leq \epsilon/2 < \epsilon$.
6. Ceci étant vrai pour tout $x$, $\|f_p - f\|_\infty \leq \epsilon/2 < \epsilon$ pour $p \ge N$. La convergence est uniforme.
7. Par le théorème de transfert de continuité, une limite uniforme de fonctions continues est continue.
8. Donc $f \in \mathcal{C}([0,1], \mathbb{R})$. L'espace est complet.
