# Exo 04 : L'intégrale de Gauss et l'approximation monotone ($\bigstar$\bigstar\star\star\star$)

## Énoncé
Soit la fonction $f(x) = e^{-x^2}$ définie sur $\mathbb{R}$.
Soit la suite de fonctions $f_n(x) = \left(1 - \frac{x^2}{n}\right)^n \mathbf{1}_{[-\sqrt{n}, \sqrt{n}]}(x)$.
1. Montrer que la suite $(f_n)$ est positive et croissante.
2. Déterminer sa limite ponctuelle.
3. En déduire que $\int_{\mathbb{R}} e^{-x^2} \, dx = \lim_{n \to \infty} \int_{-\sqrt{n}}^{\sqrt{n}} \left(1 - \frac{x^2}{n}\right)^n dx$.

## Correction Détaillée
**Étape 1 : Positivité et croissance**
Pour $x \in [-\sqrt{n}, \sqrt{n}]$, $0 \le \frac{x^2}{n} \le 1$. Donc $1 - \frac{x^2}{n} \ge 0$, d'où $f_n(x) \ge 0$.
Pour la croissance, étudions $u_n = \ln(f_n(x))$ pour $x^2 \le n$ :
$u_n = n \ln\left(1 - \frac{x^2}{n}\right)$.
En dérivant judicieusement par rapport au paramètre (ou en utilisant la concavité de $t \mapsto \ln t$), on montre de manière classique que la suite $\left(1 + \frac{y}{n}\right)^n$ est croissante pour tout $y \in \mathbb{R}$ dès que le terme est positif. Avec $y = -x^2$, la suite $f_n(x)$ est croissante. L'ensemble support $]-\sqrt{n}, \sqrt{n}[$ s'élargit avec $n$, préservant la croissance.

**Étape 2 : Limite ponctuelle**
Soit $x \in \mathbb{R}$. Pour $n > x^2$, on utilise le développement limité de $\ln(1 - u)$ en $0$ :
$n \ln\left(1 - \frac{x^2}{n}\right) = n \left( -\frac{x^2}{n} + o\left(\frac{1}{n}\right) \right) = -x^2 + o(1)$.
Par composition avec l'exponentielle (continue), $f_n(x) \to e^{-x^2}$ lorsque $n \to \infty$.

**Étape 3 : Application du Théorème de Convergence Monotone**
La suite $(f_n)$ est positive et croissante vers $x \mapsto e^{-x^2}$.
D'après le théorème de Beppo Levi :
$$ \int_{\mathbb{R}} e^{-x^2} \, dx = \lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) \, dx $$
Comme $f_n$ est nulle en dehors de $[-\sqrt{n}, \sqrt{n}]$, cela devient :
$$ \int_{\mathbb{R}} e^{-x^2} \, dx = \lim_{n \to \infty} \int_{-\sqrt{n}}^{\sqrt{n}} \left(1 - \frac{x^2}{n}\right)^n dx $$
Cette propriété est fondamentale pour le calcul de l'intégrale de Gauss sans passer par les intégrales doubles.
