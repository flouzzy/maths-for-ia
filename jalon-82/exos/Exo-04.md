# Exercice 4 : Fonction localement non-intégrable

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Montrer que la fonction $f(x) = \frac{1}{x^2}$ ne définit pas une distribution régulière sur $\mathbb{R}$.

**Correction Détaillée :**
1. **Rappel de la définition :**
   Pour qu'une fonction $f$ définisse une distribution régulière, il faut qu'elle soit localement intégrable, c'est-à-dire que pour tout segment $[a, b]$, $\int_a^b |f(x)|dx < +\infty$.
2. **Étude autour de 0 :**
   Considérons un intervalle contenant 0, par exemple $[0, 1]$.
   $\int_0^1 \frac{1}{x^2} dx = \lim_{\epsilon \to 0^+} \int_\epsilon^1 x^{-2} dx = \lim_{\epsilon \to 0^+} \left[ -x^{-1} \right]_\epsilon^1 = \lim_{\epsilon \to 0^+} \left( -1 + \frac{1}{\epsilon} \right) = +\infty$.
3. **Conclusion :**
   La fonction $f(x) = 1/x^2$ n'est pas localement intégrable autour de $0$. Donc elle ne définit pas de distribution régulière $T_f$. On verra plus tard qu'on peut lui associer une distribution via la notion de "partie finie" de Hadamard ou par dérivation au sens des distributions, mais ce n'est pas une distribution *régulière*.
