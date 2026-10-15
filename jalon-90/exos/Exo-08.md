# Exercice 08

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Prouvez que la convergence en probabilité vers une constante implique la convergence en loi vers cette même constante. (Cas particulier du théorème du cours).

**Correction :**
Soit $X_n \xrightarrow{\mathbb{P}} c$ où $c \in \mathbb{R}$ est une constante déterministe. On veut montrer que $\lim F_{X_n}(x) = F_c(x)$ pour tout point de continuité de $F_c$.
La fonction de répartition de $c$ est la fonction indicatrice (Dirac en $c$) :
$$ F_c(x) = \begin{cases} 0 & \text{si } x < c \\ 1 & \text{si } x \ge c \end{cases} $$
Le seul point de discontinuité est $x = c$. Il suffit donc de vérifier la convergence pour $x < c$ et pour $x > c$.

**Cas 1 : $x < c$.** Posons $\epsilon = c - x > 0$.
$$ \mathbb{P}(X_n \le x) = \mathbb{P}(X_n - c \le x - c) = \mathbb{P}(X_n - c \le -\epsilon) \le \mathbb{P}(|X_n - c| \ge \epsilon) $$
Par hypothèse, $\mathbb{P}(|X_n - c| \ge \epsilon) \to 0$, donc $\mathbb{P}(X_n \le x) \to 0 = F_c(x)$.

**Cas 2 : $x > c$.** Posons $\epsilon = x - c > 0$.
$$ \mathbb{P}(X_n \le x) = 1 - \mathbb{P}(X_n > x) = 1 - \mathbb{P}(X_n - c > x - c) = 1 - \mathbb{P}(X_n - c > \epsilon) $$
Puisque $\mathbb{P}(X_n - c > \epsilon) \le \mathbb{P}(|X_n - c| > \epsilon) \to 0$, on a :
$$ \mathbb{P}(X_n \le x) \to 1 = F_c(x) $$
Ceci prouve la convergence en loi vers $c$.
