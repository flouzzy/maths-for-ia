# Exercice 8

## Exercice 8 : Convergence faible et norme dans les espaces uniformément convexes \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $E$ un espace de Banach uniformément convexe. Montrer que si $x_n \rightharpoonup x$ faiblement et que $\|x_n\| \to \|x\|$, alors $x_n \to x$ fortement.

**Correction :**
*Analyse de l'énoncé :* La convergence faible plus la convergence des normes entraîne la convergence forte dans les espaces possédant une bonne géométrie (espaces uniformément convexes, comme les Hilbert ou les $L^p$).
*Résolution pas-à-pas :*
1. **Étape 1 : Cas où $x = 0$.**
   Si $x = 0$, l'hypothèse $\|x_n\| \to \|x\| = 0$ donne directement $x_n \to 0$ fortement, et la preuve est terminée. Supposons donc $x \neq 0$.
2. **Étape 2 : Normalisation.**
   Soient $y_n = \frac{x_n}{\|x_n\|}$ et $y = \frac{x}{\|x\|}$.
   Puisque $x_n \rightharpoonup x$ et $\|x_n\| \to \|x\|$, on a $y_n \rightharpoonup y$.
   De plus, $\|y_n\| = 1$ et $\|y\| = 1$.
3. **Étape 3 : Évaluation de la limite de la demi-somme.**
   Soit $f \in E^*$ telle que $\|f\| = 1$ et $f(y) = \|y\| = 1$ (théorème de Hahn-Banach).
   Comme $y_n \rightharpoonup y$, on a $f(y_n) \to f(y) = 1$.
   Considérons $\frac{y_n + y}{2}$.
   $$1 \ge \left\| \frac{y_n + y}{2} \right\| \ge f\left( \frac{y_n + y}{2} \right) = \frac{f(y_n) + 1}{2} \to 1$$
   Donc $\lim_{n \to \infty} \left\| \frac{y_n + y}{2} \right\| = 1$.
4. **Étape 4 : Utilisation de la convexité uniforme.**
   Dans un espace uniformément convexe, pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que si $\|u\| \le 1$, $\|v\| \le 1$ et $\|u - v\| \ge \epsilon$, alors $\| \frac{u+v}{2} \| \le 1 - \delta$.
   Si $\|y_n - y\|$ ne tendait pas vers 0, il existerait $\epsilon > 0$ et une sous-suite tels que $\|y_{\phi(n)} - y\| \ge \epsilon$.
   Par uniforme convexité, on aurait $\left\| \frac{y_{\phi(n)} + y}{2} \right\| \le 1 - \delta < 1$, contredisant l'étape 3 où cette norme tend vers 1.
   Par conséquent, $y_n \to y$ fortement.
5. **Étape 5 : Conclusion.**
   $x_n = \|x_n\| y_n$. Puisque $\|x_n\| \to \|x\|$ et $y_n \to y$, le produit tend fortement vers $\|x\|y = x$. Donc $x_n \to x$ fortement.
