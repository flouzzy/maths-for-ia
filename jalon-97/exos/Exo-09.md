# Exercice 9

**Difficulté :** $\star\star\star\star\☆$

**Énoncé :**
Montrer que l'espace des fonctions lipschitziennes sur $[0,1]$ s'annulant en 0, noté $Lip_0([0,1])$, muni de la norme $\|f\|_{Lip} = \sup_{x \neq y} \frac{|f(x) - f(y)|}{|x - y|}$ est un espace de Banach.

**Correction Détaillée :**
1. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $Lip_0([0,1])$.
2. Puisque $f_n(0) = 0$, pour tout $x \in (0,1]$, on a $|f_n(x)| = |f_n(x) - f_n(0)| \le \|f_n\|_{Lip} |x - 0| \le \|f_n\|_{Lip}$.
3. La suite $(f_n)$ étant de Cauchy pour $\|\cdot\|_{Lip}$, la suite de réels $\|f_n\|_{Lip}$ est bornée par une constante $M$. Donc $\|f_n\|_\infty \le M$. De plus, pour tout $x$, la suite $(f_n(x))$ est de Cauchy dans $\mathbb{R}$. Elle converge ponctuellement vers une fonction $f$.
4. La convergence est uniforme. Fixons $\varepsilon > 0$. Il existe $N$ tel que pour $p, q \ge N$, $\|f_p - f_q\|_{Lip} < \varepsilon$. Alors $|f_p(x) - f_q(x)| = |(f_p - f_q)(x) - (f_p - f_q)(0)| \le \|f_p - f_q\|_{Lip} |x| \le \varepsilon$. En faisant tendre $q \to \infty$, $|f_p(x) - f(x)| \le \varepsilon$ pour tout $x$. La suite converge uniformément vers $f$.
5. Il reste à montrer que $f \in Lip_0([0,1])$ et que la convergence a lieu pour $\|\cdot\|_{Lip}$.
6. Reprenons $p, q \ge N$. Pour tout $x \neq y$, $|(f_p - f_q)(x) - (f_p - f_q)(y)| \le \|f_p - f_q\|_{Lip} |x - y| \le \varepsilon |x - y|$.
7. Fixons $p$ et faisons tendre $q \to \infty$. Par continuité de la valeur absolue, on obtient $|(f_p - f)(x) - (f_p - f)(y)| \le \varepsilon |x - y|$.
8. Ceci montre premièrement que pour $p \ge N$, $f_p - f$ est lipschitzienne (et $f_p$ l'étant, par linéarité, $f = f_p - (f_p - f)$ est bien lipschitzienne). $f(0)=0$ est préservé par convergence simple.
9. De plus, cela prouve que pour tout $p \ge N$, la constante de Lipschitz de $f_p - f$ est majorée par $\varepsilon$, c'est-à-dire $\|f_p - f\|_{Lip} \le \varepsilon$.
10. La suite $(f_n)$ converge bien vers $f$ dans $Lip_0([0,1])$ pour la norme $\|\cdot\|_{Lip}$. L'espace est donc un espace de Banach.
