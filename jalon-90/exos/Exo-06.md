# Exercice 06

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $Z_n$ une suite de variables aléatoires telles que $\mathbb{P}(Z_n = \sqrt{n}) = \frac{1}{n}$ et $\mathbb{P}(Z_n = 0) = 1 - \frac{1}{n}$.
Montrez que $Z_n$ converge en probabilité vers $0$, mais qu'elle ne converge pas dans $L^2$.

**Correction :**
**Convergence en Probabilité :**
Soit $\epsilon \in ]0, 1[$. Puisque $Z_n$ vaut $0$ ou $\sqrt{n}$ (avec $n \ge 1$), on a :
$$ \mathbb{P}(|Z_n - 0| > \epsilon) = \mathbb{P}(Z_n = \sqrt{n}) = \frac{1}{n} $$
Par passage à la limite, $\lim_{n \to \infty} \mathbb{P}(|Z_n| > \epsilon) = 0$. Donc $Z_n \xrightarrow{\mathbb{P}} 0$.

**Convergence $L^2$ :**
Calculons l'espérance du carré :
$$ \mathbb{E}[|Z_n - 0|^2] = (\sqrt{n})^2 \cdot \mathbb{P}(Z_n = \sqrt{n}) + 0^2 \cdot \mathbb{P}(Z_n = 0) $$
$$ \mathbb{E}[Z_n^2] = n \cdot \frac{1}{n} = 1 $$
La limite de $\mathbb{E}[|Z_n - 0|^2]$ est $1$, qui n'est pas égale à $0$. Par conséquent, $Z_n$ ne converge pas vers $0$ dans l'espace de Hilbert $L^2$.
