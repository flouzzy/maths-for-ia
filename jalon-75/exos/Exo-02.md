# Exercice 2 : La bosse fuyante (L'escargot)
**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Construire explicitement une suite de fonctions $(f_n)_{n \ge 1}$ dans $L^2([0,1])$ telle que $f_n$ converge vers $0$ dans $L^2$, mais que la suite $(f_n(x))$ ne converge pour aucun $x \in [0,1]$.

**Correction :**
On utilise le principe de l'escargot (intervalles balayant $[0,1]$ de plus en plus fins).
Pour tout entier $k \ge 1$, on divise $[0,1]$ en $k$ intervalles de même longueur $I_{k,j} = [\frac{j}{k}, \frac{j+1}{k}]$ pour $0 \le j \le k-1$.
On numérote ces intervalles en une suite simple $(A_n)_{n \ge 1}$ : $A_1 = I_{1,0}$, $A_2 = I_{2,0}$, $A_3 = I_{2,1}$, $A_4 = I_{3,0}$, etc. L'indice $n$ s'écrit de manière unique $n = \frac{k(k-1)}{2} + j + 1$.
On pose $f_n = \mathbf{1}_{A_n}$.
- **Convergence $L^2$ :** $\|f_n\|_2^2 = \int_0^1 \mathbf{1}_{A_n} dx = \lambda(A_n) = \frac{1}{k}$. Quand $n \to +\infty$, $k \to +\infty$, donc $\|f_n\|_2 \to 0$. Ainsi $f_n \to 0$ dans $L^2$.
- **Non-convergence ponctuelle :** Fixons $x \in [0,1]$. Pour chaque $k \ge 1$, il existe exactement un $j \in \{0, \dots, k-1\}$ tel que $x \in I_{k,j}$ (en ignorant l'ambiguïté dénombrable des bornes). Ainsi, pour chaque "tour" $k$, $f_n(x) = 1$ pour un certain $n$, et $f_n(x) = 0$ pour les autres. La suite $(f_n(x))$ est donc composée d'une infinité de $1$ et d'une infinité de $0$. Elle ne converge pas (ni vers $0$, ni vers rien).
