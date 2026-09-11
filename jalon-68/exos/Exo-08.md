# Exercice 8 : Application du lemme de Fatou $$\bigstar$$$$\bigstar$$$$\bigstar$$$$\bigstar$$$$\bigstar$$

**Énoncé :**
Montrer une application spécifique du lemme de Fatou ou de l'intégrabilité pour une suite de fonctions (niveau 8).
Soit $f_n(x) = \frac{n^2 x}{1 + n^3 x^2}$ sur $[0, 1]$.
Étudier la limite et appliquer le lemme de Fatou.

**Correction Détaillée :**
1. Pour $x > 0$ fixé, $f_n(x) \sim \frac{n^2 x}{n^3 x^2} = \frac{1}{n x} \to 0$. Donc $f_n \to 0$ simplement.
2. $\liminf f_n = 0$, donc $\int_0^1 \liminf f_n = 0$.
3. Calcul de l'intégrale : $\int_0^1 \frac{n^2 x}{1 + n^3 x^2} dx$.
   Posons $u = 1 + n^3 x^2$, $du = 2 n^3 x dx$.
   L'intégrale devient $\frac{1}{2n} \int_1^{1+n^3} \frac{du}{u} = \frac{\ln(1+n^3)}{2n}$.
4. Limite : $\frac{\ln(1+n^3)}{2n} \to 0$.
5. L'inégalité $0 \le 0$ est vérifiée. La limite des intégrales est égale à l'intégrale de la limite.
