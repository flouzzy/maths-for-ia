# Exercice 4 : Limite d'une suite croissante impliquant un logarithme
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

### Énoncé

Calculer $\lim_{n \to +\infty} \int_0^1 \frac{n \ln(1 + \frac{x}{n})}{x \sqrt{x}} dx$.

---
### Correction détaillée

1. Considérons la suite de fonctions $f_n(x) = \frac{n \ln(1 + \frac{x}{n})}{x \sqrt{x}} = \frac{\ln(1 + \frac{x}{n})}{\frac{x}{n}} \cdot \frac{1}{\sqrt{x}}$.
2. Pour $x > 0$ fixé, posons $g(t) = \frac{\ln(1+t)}{t}$ avec $t = \frac{x}{n}$. La fonction $g(t)$ est décroissante sur $]0, +\infty[$. En effet, $g'(t) = \frac{\frac{t}{1+t} - \ln(1+t)}{t^2}$. Si $h(t) = \frac{t}{1+t} - \ln(1+t)$, alors $h'(t) = \frac{1}{(1+t)^2} - \frac{1}{1+t} = \frac{-t}{(1+t)^2} < 0$. Comme $h(0)=0$, $h(t) < 0$ pour $t>0$, donc $g'(t) < 0$.
3. Puisque $t = \frac{x}{n}$ décroît quand $n$ croît, la valeur de $g(\frac{x}{n})$ **croît** avec $n$.
4. Ainsi, la suite $(f_n)$ est une suite croissante de fonctions mesurables positives sur $]0, 1]$.
5. Calculons la limite ponctuelle : on sait que $\lim_{t \to 0} \frac{\ln(1+t)}{t} = 1$. Donc $\lim_{n \to +\infty} f_n(x) = \frac{1}{\sqrt{x}}$.
6. Le Théorème de Convergence Monotone de Beppo Levi s'applique :
   $$\lim_{n \to +\infty} \int_0^1 f_n(x) \, dx = \int_0^1 \lim_{n \to +\infty} f_n(x) \, dx = \int_0^1 \frac{1}{\sqrt{x}} \, dx$$
7. L'intégrale de Lebesgue coïncide avec l'intégrale généralisée de Riemann (car l'intégrande est positive) :
   $$\int_0^1 x^{-1/2} \, dx = \left[ 2 x^{1/2} \right]_0^1 = 2$$
8. Conclusion : la limite de l'intégrale est $2$.
