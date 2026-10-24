\subsection*{Exercice 7 : Théorème de Mazur \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Soit $(x_n)_{n \in \mathbb{N}}$ une suite qui converge faiblement vers $x$ dans un espace de Banach $E$. Montrer qu'il existe une suite $(y_n)$ de combinaisons convexes des $(x_k)_{k \ge n}$ qui converge fortement vers $x$.

**Correction :**

1. Soit $C = \text{Conv}(\{ x_k \mid k \in \mathbb{N} \})$ l'enveloppe convexe de la suite.
2. Supposons par l'absurde que $x$ n'appartient pas à l'adhérence forte $\overline{C}$.
3. Par Hahn-Banach (séparation stricte), il existe $f \in E^*$ et $\alpha \in \mathbb{R}$ tels que $\forall y \in \overline{C}, f(y) \le \alpha < f(x)$.
4. En particulier, pour tout $k$, $f(x_k) \le \alpha$.
5. Comme $(x_n)$ converge faiblement vers $x$, la définition de la convergence faible implique que $f(x_n) \to f(x)$.
6. Ainsi, par passage à la limite, $f(x) \le \alpha$, ce qui contredit $\alpha < f(x)$.
7. Par conséquent, $x \in \overline{C}$.
8. Ainsi, il existe une suite d'éléments de $C$ (donc des combinaisons convexes des $x_k$) qui converge fortement vers $x$. Par une construction par blocs itérative, on assure la condition $k \ge n$.