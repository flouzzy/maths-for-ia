# Exercice 05

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $X_n$ distribuée selon une loi Normale $\mathcal{N}\left(0, \frac{1}{n}\right)$.
Démontrez que $X_n$ converge en probabilité vers $0$ en utilisant l'inégalité de Bienaymé-Tchebychev.

**Correction :**
L'espérance de $X_n$ est $\mathbb{E}[X_n] = 0$ et sa variance est $\text{Var}(X_n) = \frac{1}{n}$.
Nous cherchons à évaluer $\mathbb{P}(|X_n - 0| > \epsilon)$ pour un $\epsilon > 0$ fixé.
D'après l'inégalité de Bienaymé-Tchebychev, pour toute variable aléatoire $Y$ d'espérance $\mu$ et de variance $\sigma^2$ :
$$ \mathbb{P}(|Y - \mu| \ge \epsilon) \le \frac{\sigma^2}{\epsilon^2} $$
Appliquée à $X_n$ :
$$ \mathbb{P}(|X_n| \ge \epsilon) \le \frac{1/n}{\epsilon^2} = \frac{1}{n\epsilon^2} $$
En passant à la limite quand $n \to \infty$, pour tout $\epsilon > 0$ fixe :
$$ \lim_{n \to \infty} \frac{1}{n\epsilon^2} = 0 $$
Ainsi, $\lim_{n \to \infty} \mathbb{P}(|X_n| \ge \epsilon) = 0$.
La suite converge bien en probabilité vers $0$.
