---
title: "Exercice 7"
---
## Exercice 7 : Transformation de Laplace et Beppo Levi $\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f : [0, +\infty[ \to \mathbb{R}^+$ une fonction mesurable. La transformée de Laplace est $\mathcal{L}(f)(p) = \int_0^\infty f(x) e^{-px} dx$.
Montrer que si $p \to 0^+$, alors $\mathcal{L}(f)(p) \to \int_0^\infty f(x) dx$ (qui peut être $+\infty$).

**Correction Détaillée :**
1. Considérons une suite de réels $(p_n)_{n \in \mathbb{N}}$ strictement positifs telle que $p_n \downarrow 0$.
2. Posons $g_n(x) = f(x) e^{-p_n x}$.
3. Comme la suite $(p_n)$ est décroissante, pour tout $x \ge 0$, la suite $(-p_n x)$ est croissante.
4. L'exponentielle étant croissante, $e^{-p_n x}$ est croissante en $n$.
5. Comme $f(x) \ge 0$, la suite de fonctions $g_n(x)$ est une suite \textbf{croissante} de fonctions mesurables positives.
6. La limite simple de $g_n(x)$ quand $n \to \infty$ (donc $p_n \to 0$) est $f(x) e^{0} = f(x)$.
7. D'après le théorème de convergence monotone, l'intégrale de la limite est la limite des intégrales :
   $$\lim_{n \to \infty} \int_0^\infty f(x) e^{-p_n x} dx = \int_0^\infty \lim_{n \to \infty} (f(x) e^{-p_n x}) dx = \int_0^\infty f(x) dx$$
8. Ceci étant vrai pour toute suite $p_n \to 0$, cela prouve la limite de la fonction $\mathcal{L}(f)$ en $0^+$.
