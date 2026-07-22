# Exercice 10 : Équation différentielle résolue par limite
**Énoncé :**
On considère une suite d'approximations de Picard définie par $y_0(t) = 1$ et $y_{n+1}(t) = 1 + \int_0^t y_n(s) ds$.
Montrer que $y_n(t)$ converge uniformément vers $e^t$ sur tout compact $[-A, A]$.

**Solution Rigoureuse :**
1. **Construction des itérés :**
Calculons les premiers termes :
$y_0(t) = 1$
$y_1(t) = 1 + \int_0^t 1 ds = 1 + t$
$y_2(t) = 1 + \int_0^t (1+s) ds = 1 + t + \frac{t^2}{2}$
Par récurrence, on démontre que $y_n(t) = \sum_{k=0}^n \frac{t^k}{k!}$, qui est le développement en série de Taylor de l'exponentielle.
2. **Évaluation du reste (Convergence uniforme) :**
On sait que la limite simple est $\exp(t)$. Étudions la différence $|y_n(t) - e^t|$ sur $[-A, A]$.
$$|e^t - y_n(t)| = \left| \sum_{k=n+1}^{+\infty} \frac{t^k}{k!} \right| \le \sum_{k=n+1}^{+\infty} \frac{|t|^k}{k!} \le \sum_{k=n+1}^{+\infty} \frac{A^k}{k!}$$
Le majorant est indépendant de $t \in $[-A, A]$, et représente le reste de la série numérique de l'exponentielle au point $A$.
Comme cette série converge, son reste tend vers $0$ lorsque $n \to +\infty$.
Ainsi, $\lim_{n \to +\infty} \sup_{t \in [-A, A]} |y_n(t) - e^t| = 0$.
La convergence est **uniforme** sur tout segment de $\mathbb{R}$.
Le théorème de Picard-Lindelöf repose sur cette idée pour prouver l'existence globale des solutions aux EDO, soulignant que la convergence uniforme permet d'échanger limite et intégrale dans l'équation intégrale de point fixe.
