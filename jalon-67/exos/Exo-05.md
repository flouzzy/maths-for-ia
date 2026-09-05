# Exercice 5 : Inversion Limite-Intégrale sans convergence uniforme \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $f_n(x) = \frac{n \sqrt{x}}{1 + n^2 x^2}$ sur $[0, 1]$.

**Question :** La suite $(f_n)$ est-elle croissante ? Peut-on appliquer le théorème de convergence monotone pour calculer $\lim \int_{0}^{1} f_n$ ?

**Solution Détaillée :**
1. Étudions la fonction $f_n(x)$. Pour $x = 0$, $f_n(0) = 0$. Pour $x > 0$, $\lim_{n \to \infty} f_n(x) = 0$.
2. La limite simple est donc $f(x) = 0$ pour tout $x \in [0, 1]$.
3. Étudions le maximum de $f_n$.
   En dérivant $f_n$, le maximum est atteint en $x_n = \frac{1}{n\sqrt{3}}$, et $f_n(x_n)$ tend vers l'infini avec $n$.
4. La suite $(f_n(x))$ n'est manifestement pas croissante en $n$. Pour $x > 0$ fixé, $f_n(x)$ finit par décroître vers 0.
5. On **ne peut pas** appliquer le théorème de convergence monotone directement à $(f_n)$ ou $(-f_n)$ pour $x \in ]0, 1]$.
6. Cependant, on peut calculer directement l'intégrale :
   Par changement de variable $u = n x$, $\int_{0}^{1} f_n(x) dx = \int_{0}^{n} \frac{\sqrt{u/n}}{1+u^2} du = \frac{1}{\sqrt{n}} \int_{0}^{n} \frac{\sqrt{u}}{1+u^2} du$.
   L'intégrale $\int_{0}^{\infty} \frac{\sqrt{u}}{1+u^2} du$ est finie, donc $\int f_n \sim \frac{C}{\sqrt{n}} \to 0$.
7. Cet exercice illustre un cas où la limite et l'intégrale commutent (toutes deux valent 0), mais où la convergence monotone ne s'applique pas. (On utiliserait plutôt la convergence dominée ici).
