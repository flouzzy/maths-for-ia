# Exercice 03

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Pour l'exercice 1, étudiez la convergence de $X_n$ dans $L^1$ et dans $L^2$.

**Correction :**
Rappelons que $\mathbb{P}(X_n = 1) = \frac{1}{n}$ et $\mathbb{P}(X_n = 0) = 1 - \frac{1}{n}$.
**Convergence $L^1$ :**
On calcule l'espérance de l'écart :
$$ \mathbb{E}[|X_n - 0|] = 1 \cdot \mathbb{P}(X_n = 1) + 0 \cdot \mathbb{P}(X_n = 0) = \frac{1}{n} $$
Puisque $\lim_{n \to \infty} \frac{1}{n} = 0$, la suite converge dans $L^1$ vers $0$.

**Convergence $L^2$ :**
$$ \mathbb{E}[|X_n - 0|^2] = 1^2 \cdot \mathbb{P}(X_n = 1) + 0^2 \cdot \mathbb{P}(X_n = 0) = \frac{1}{n} $$
Puisque $\lim_{n \to \infty} \frac{1}{n} = 0$, la suite converge également dans $L^2$ vers $0$.
