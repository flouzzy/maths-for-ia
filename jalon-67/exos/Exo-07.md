# Exercice 7 : Convergence vers la mesure de Dirac
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

### Énoncé

Soit $f_n(x) = \frac{n}{2} \chi_{[-1/n, 1/n]}(x)$. Étudier la convergence ponctuelle de cette suite. Calculer l'intégrale des $f_n$ et l'intégrale de la limite. Le TCM est-il applicable ? Quelle est la véritable nature géométrique de cette limite au sens de la théorie de la mesure ?

---
### Correction détaillée

1. Convergence ponctuelle :
   - Pour $x \neq 0$, il existe $N$ tel que pour $n \ge N$, on a $|x| > 1/n$. Donc pour tout $n \ge N$, $f_n(x) = 0$. La limite ponctuelle pour $x \neq 0$ est donc 0.
   - Pour $x = 0$, $f_n(0) = n/2$ pour tout $n$, ce qui tend vers $+\infty$.
   Donc la fonction limite est $f(x) = 0$ presque partout (puisque le point singulier $\{0\}$ est de mesure de Lebesgue nulle).
2. Calcul des intégrales :
   $$\int_{\mathbb{R}} f_n(x) \, d\lambda(x) = \int_{-1/n}^{1/n} \frac{n}{2} \, dx = \frac{n}{2} \left[ x \right]_{-1/n}^{1/n} = \frac{n}{2} \left( \frac{1}{n} - \left(-\frac{1}{n}\right) \right) = \frac{n}{2} \left( \frac{2}{n} \right) = 1$$
   La limite des intégrales est donc 1.
3. Intégrale de la limite ponctuelle : la fonction limite $f$ est nulle presque partout. Son intégrale de Lebesgue vaut donc strictement 0.
4. Applicabilité du TCM : Le TCM stipule l'égalité sous l'hypothèse stricte que la suite est **croissante presque partout**. Or, pour un point $x = 0.5$, $f_1(0.5) = \frac{1}{2}$, mais $f_2(0.5) = 0$. La suite des valeurs décroît. La suite $(f_n)$ n'est donc pas croissante, justifiant l'échec de l'inversion limite-intégrale.
5. Nature géométrique : La suite de fonctions $(f_n)$ représente des rectangles de base de plus en plus étroite centrée en zéro et de hauteur de plus en plus grande, avec une aire constamment égale à 1. Dans le cadre des distributions (ou de la théorie des mesures), cette suite ne converge pas vers la fonction identiquement nulle, mais converge faiblement (au sens des mesures) vers la **mesure de Dirac** $\delta_0$ concentrée en zéro. L'intégrale d'une mesure limite n'est pas réductible à l'intégrale de la limite ponctuelle au sens des fonctions de Lebesgue classiques.
