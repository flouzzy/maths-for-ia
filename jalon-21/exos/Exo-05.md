# Exercice 5 : La fonction indicatrice modifiée
**Énoncé :**
On pose $f_n(x) = \exp(-n x^2)$ sur $\mathbb{R}$.
Étudier la convergence simple et uniforme.

**Solution Rigoureuse :**
1. **Convergence simple :**
Soit $x \in \mathbb{R}$.
- Si $x = 0$, $f_n(0) = \exp(0) = 1$ pour tout $n$. Donc $\lim_{n \to +\infty} f_n(0) = 1$.
- Si $x \neq 0$, $x^2 > 0$, donc $\lim_{n \to +\infty} -n x^2 = -\infty$, ce qui implique $\lim_{n \to +\infty} \exp(-n x^2) = 0$.
La suite converge simplement sur $\mathbb{R}$ vers la fonction limite $f$ telle que $f(0) = 1$ et $f(x) = 0$ si $x \neq 0$.

2. **Convergence uniforme :**
Les fonctions $f_n$ sont continues sur $\mathbb{R}$, mais la fonction limite $f$ est discontinue en $x=0$.
D'après le théorème du transfert de continuité (par contraposée), la convergence **ne peut pas être uniforme** sur un intervalle contenant $0$, et a fortiori pas sur $\mathbb{R}$ entier.
Vérifions-le analytiquement :
$$\sup_{x \in \mathbb{R}} |f_n(x) - f(x)| \ge \lim_{x \to 0, x \neq 0} |f_n(x) - 0| = \lim_{x \to 0} \exp(-n x^2) = 1$$
La norme infinie de la différence vaut $1$, elle ne tend pas vers $0$.
Cependant, sur tout ensemble de la forme $E_a = \mathbb{R} \setminus ]-a, a[$ avec $a > 0$, la fonction $f$ est identiquement nulle, et :
$$\sup_{|x| \ge a} |f_n(x)| = \exp(-n a^2) \xrightarrow[n \to +\infty]{} 0$$
La convergence est donc uniforme sur les complémentaires de voisinages de l'origine.
