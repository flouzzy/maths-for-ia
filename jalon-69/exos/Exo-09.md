##{Exercice 9 : Domination délicate et TCD \quad $\bigstar\bigstar\bigstar\bigstar\star$}

\textbf{Énoncé :}
Montrer que la fonction $G(t) = \int_0^\infty e^{-tx^2} \cos(x) dx$ est de classe $C^1$ sur $]0, +\infty[$.

\textbf{Correction :}
Posons $h(x, t) = e^{-tx^2} \cos(x)$.
1. $t \mapsto h(x, t)$ est dérivable et $\frac{\partial h}{\partial t}(x, t) = -x^2 e^{-tx^2} \cos(x)$.
2. Cherchons une domination locale. Soit $[a, b] \subset ]0, +\infty[$ avec $a > 0$.
   Pour $t \in [a, b]$, on a :
   $\left| \frac{\partial h}{\partial t}(x, t) \right| = x^2 e^{-tx^2} |\cos(x)| \le x^2 e^{-ax^2}$.
3. La fonction $g(x) = x^2 e^{-ax^2}$ est intégrable sur $[0, +\infty[$ (décroissance exponentielle très rapide l'emportant sur le polynôme).
4. Le TCD pour la dérivation implique que $G$ est dérivable sur tout $[a, b]$, donc sur $]0, +\infty[$, et que $G'$ est continue car $\frac{\partial h}{\partial t}$ est dominée par $g$ et continue par rapport à $t$. $G$ est donc de classe $C^1$.
