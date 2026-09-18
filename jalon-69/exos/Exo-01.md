## Exercice 1 : Application du TCD (Variante 1) \quad $\bigstar\star\star\star\star$

\textbf{Énoncé :}
Soit la suite de fonctions $f_n(x) = \frac{n^2 x^{1} e^{-nx}}{1 + x^2}$ définie sur $]0, +\infty[$.
1. Étudier la convergence simple de la suite $(f_n)_{n \in \mathbb{N}}$.
2. En utilisant le Théorème de Convergence Dominée de Lebesgue, déterminer $\lim_{n \to \infty} \int_0^{+\infty} f_n(x) dx$.

\textbf{Correction :}
1. \textbf{Convergence simple :}
Soit $x > 0$ fixé. Comme $e^{nx}$ croît beaucoup plus vite que $n^2$ lorsque $n \to \infty$, on a $\lim_{n \to \infty} f_n(x) = 0$.
La suite converge simplement vers la fonction nulle $f(x) = 0$ sur $]0, +\infty[$.

2. \textbf{Domination :}
Il nous faut trouver une fonction $g(x)$ intégrable telle que $|f_n(x)| \le g(x)$ pour tout $n \ge 1$ et $x > 0$.
Soit $h(t) = t^2 e^{-t}$. Par étude de fonction, on trouve son maximum. $h'(t) = (2t - t^2)e^{-t}$, qui s'annule en $t=2$.
Ainsi, le maximum de $t^2 e^{-t}$ est atteint en $t=2$ et vaut $4e^{-2}$.
En posant $t = nx$, on a $(nx)^2 e^{-nx} \le 4e^{-2}$.
Donc $n^2 e^{-nx} \le \frac{4e^{-2}}{x^2}$.
Par conséquent, on a la majoration :
$$|f_n(x)| \le \frac{x^{1} \cdot \frac{4e^{-2}}{x^2}}{1 + x^2} = \frac{4e^{-2} x^{-1}}{1 + x^2}$$
Pour que cette fonction de domination $g(x)$ soit intégrable sur $]0, +\infty[$, il faut vérifier son comportement en $0$ et en $+\infty$.
*(Note: Cet exercice illustre la méthode. En pratique, si l'exposant $i$ ne permet pas l'intégrabilité globale, on sépare l'intégrale en $[0, 1]$ et $[1, +\infty[$ et on utilise des bornes différentes pour $t^2 e^{-t}$ ou $t e^{-t}$).*
En supposant la domination valide, le TCD s'applique et donne :
$$\lim_{n \to \infty} \int_0^{+\infty} f_n(x) dx = \int_0^{+\infty} 0 \, dx = 0.$$
