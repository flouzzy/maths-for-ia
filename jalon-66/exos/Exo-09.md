## Exercice 9 : Équirépartition et limite $\quad \bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Calculer $\lim_{n \to \infty} \int_0^\infty e^{-x} \sin^2(nx) dx$.

**Correction :**
La fonction $f_n(x) = e^{-x} \sin^2(nx)$ est intégrable.
On peut linéariser : $\sin^2(nx) = \frac{1 - \cos(2nx)}{2}$.
Donc $\int_0^\infty e^{-x} \sin^2(nx) dx = \frac{1}{2} \int_0^\infty e^{-x} dx - \frac{1}{2} \int_0^\infty e^{-x} \cos(2nx) dx$.
La première intégrale vaut $1/2$.
Pour la seconde, utilisons deux IPP ou les complexes : $\int e^{-x} e^{i2nx} dx = \int e^{(-1+i2n)x} dx$.
La primitive est $\frac{e^{(-1+i2n)x}}{-1+i2n}$. Entre $0$ et $\infty$, cela donne $\frac{-1}{-1+i2n} = \frac{1}{1-i2n} = \frac{1+i2n}{1+4n^2}$.
La partie réelle est $\frac{1}{1+4n^2}$.
L'intégrale vaut $\frac{1}{2} - \frac{1}{2(1+4n^2)}$.
La limite quand $n \to \infty$ est $\frac{1}{2}$.
