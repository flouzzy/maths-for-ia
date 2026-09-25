# Exercice 2 : Densité et limite ponctuelle $\star\star\mathstrut\mathstrut\mathstrut$

**Énoncé :**
Montrer, par un contre-exemple, que si une suite de fonctions $(f_n)_{n \ge 1}$ de $L^2(\mathbb{R})$ est telle que $\lim_{n \to \infty} f_n(x) = 0$ pour presque tout $x$, cela n'implique pas que $\lim_{n \to \infty} \|f_n\|_{L^2} = 0$.
Quel théorème classique manque d'une hypothèse cruciale ici ?

**Correction détaillée :**
Considérons la suite de fonctions définie sur $\mathbb{R}$ par $f_n(x) = \sqrt{n} \cdot \mathbf{1}_{[0, 1/n]}(x)$.
1. **Convergence presque partout :** Soit $x \in \mathbb{R}$. Si $x \le 0$, $f_n(x) = 0$ pour tout $n$, donc $\lim_{n \to \infty} f_n(x) = 0$.
Si $x > 0$, par la propriété d'Archimède, il existe un entier $N$ tel que $1/N < x$. Alors pour tout $n \ge N$, on a $1/n \le 1/N < x$, et par conséquent $x \notin [0, 1/n]$, ce qui donne $f_n(x) = 0$.
Ainsi, $\lim_{n \to \infty} f_n(x) = 0$ pour tout $x \neq 0$. Puisque le singleton $\{0\}$ est de mesure de Lebesgue nulle, la suite converge vers $0$ presque partout.
2. **Calcul de la norme $L^2$ :**
Calculons le carré de la norme de $f_n$ :
$$ \|f_n\|_2^2 = \int_{\mathbb{R}} |f_n(x)|^2 \, dx = \int_{\mathbb{R}} \left( \sqrt{n} \cdot \mathbf{1}_{[0, 1/n]}(x) \right)^2 \, dx = \int_0^{1/n} n \, dx = n \times \frac{1}{n} = 1 $$
Ainsi, pour tout $n$, $\|f_n\|_2 = 1$.
3. **Conclusion :** La limite de la norme $L^2$ est $1$, et non $0$. La suite ne converge donc pas vers $0$ dans l'espace $L^2(\mathbb{R})$.
4. **Analyse de l'hypothèse manquante :** Le Théorème de Convergence Dominée (TCD) de Lebesgue permettrait de déduire $\|f_n\|_2 \to 0$ si les $|f_n|^2$ étaient dominées par une fonction $g \in L^1(\mathbb{R})$. Or, ici, la majorante minimale est $g(x) = \sup_n |f_n(x)|^2$, qui n'est pas intégrable autour de $0$, la condition de domination fait donc défaut. $\blacksquare$
