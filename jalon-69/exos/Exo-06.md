##{Exercice 6 : Dérivation sous le signe somme (TCD continu) \quad $\bigstar\bigstar\bigstar\bigstar\star$}

\textbf{Énoncé :}
Soit $F(t) = \int_0^\infty e^{-tx} \frac{\sin x}{x} dx$ pour $t > 0$.
Montrer que $F$ est dérivable sur $]0, +\infty[$ et calculer $F'(t)$.

\textbf{Correction :}
Posons $f(x, t) = e^{-tx} \frac{\sin x}{x}$.
1. $t \mapsto f(x, t)$ est dérivable et $\frac{\partial f}{\partial t}(x, t) = -x e^{-tx} \frac{\sin x}{x} = -e^{-tx} \sin x$.
2. Fixons $a > 0$. Pour tout $t \ge a$ et $x > 0$, on a la domination :
   $\left| \frac{\partial f}{\partial t}(x, t) \right| = e^{-tx} |\sin x| \le e^{-ax}$.
3. La fonction $g(x) = e^{-ax}$ est intégrable sur $[0, +\infty[$.
Par le TCD (version paramétrique, théorème de Leibniz), $F$ est dérivable sur $[a, +\infty[$ et :
$F'(t) = \int_0^\infty -e^{-tx} \sin x dx$.
Calculons cette intégrale en utilisant la partie imaginaire de $\int_0^\infty e^{(-t+i)x} dx$ :
$\int_0^\infty e^{(-t+i)x} dx = \left[ \frac{e^{(-t+i)x}}{-t+i} \right]_0^\infty = \frac{1}{t-i} = \frac{t+i}{t^2+1}$.
La partie imaginaire est $\frac{1}{t^2+1}$. Donc $F'(t) = -\frac{1}{t^2+1}$.
