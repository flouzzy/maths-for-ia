## Exercice 8 : Inégalité de Wirtinger \quad \bigstar\bigstar\bigstar\bigstar\bigstar

Soit $f : [0, 2\pi] \to \mathbb{R}$ de classe $C^1$, telle que $f(0)=f(2\pi)$ et $\int_0^{2\pi} f(x)dx = 0$.
Montrer que $\int_0^{2\pi} f^2(x)dx \le \int_0^{2\pi} (f'(x))^2 dx$.

**Correction :**
La condition $\int_0^{2\pi} f(x)dx = 0$ implique que $c_0(f) = a_0(f) = 0$.
Par le théorème de Parseval (applicable aux fonctions $C^1$) :
$\frac{1}{2\pi} \int_0^{2\pi} f^2(x)dx = \sum_{n \neq 0} |c_n(f)|^2$.
Pour $f'$, on sait que $c_n(f') = in c_n(f)$.
Parseval pour $f'$ : $\frac{1}{2\pi} \int_0^{2\pi} (f'(x))^2 dx = \sum_{n \neq 0} |in c_n(f)|^2 = \sum_{n \neq 0} n^2 |c_n(f)|^2$.
Comme $n^2 \ge 1$ pour tout $n \neq 0$, on a $\sum_{n \neq 0} |c_n(f)|^2 \le \sum_{n \neq 0} n^2 |c_n(f)|^2$.
D'où l'inégalité de Wirtinger : $\int_0^{2\pi} f^2(x)dx \le \int_0^{2\pi} (f'(x))^2 dx$.
L'égalité est atteinte si et seulement si $c_n(f) = 0$ pour $|n| \ge 2$, c'est-à-dire $f(x) = A\cos(x) + B\sin(x)$.
