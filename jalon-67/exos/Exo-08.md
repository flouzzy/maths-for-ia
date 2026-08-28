# Exercice 8 : Continuité d'une intégrale paramétrée ★★★★☆

**Énoncé :**
Soit $f(t) = \int_0^\infty e^{-tx} \frac{\sin^2(x)}{x^2} dx$. Prouver la continuité de $f$ sur $\mathbb{R}^+$

**Correction :**
1. On remarque que $f_n(x)$ n'est pas croissante en $n$. Pour la continuité, le théorème de convergence monotone seul ne suffit pas en général, mais on peut exprimer la différence.
2. Cependant, pour l'étude de la continuité à droite en 0, si on prend $t_n \downarrow 0$, alors la suite de fonctions $g_n(x) = e^{-t_n x} \frac{\sin^2(x)}{x^2}$ est bien **croissante**.
3. En effet, $t_n$ décroît, donc $-t_n x$ croît pour $x \ge 0$, donc $e^{-t_n x}$ croît. La fonction $\frac{\sin^2(x)}{x^2}$ est positive.
4. Les $g_n$ sont positives, mesurables et croissent vers $g(x) = 1 \cdot \frac{\sin^2(x)}{x^2}$.
5. Par le TCM, $\lim \int g_n = \int \lim g_n$, donc $\lim_{n \to \infty} f(t_n) = f(0)$.
6. Cela démontre la continuité à droite en 0.
