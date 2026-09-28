# Exercice 6 : Calcul de la série $\sum 1/(n^2+1)$

**Difficulté :** \bigstar\bigstar\bigstar\star\star

**Énoncé :**
En utilisant le résultat de l'exercice précédent pour la fonction $f(t)=e^t$ sur $]-\pi, \pi[$, déduire la valeur de $\sum_{n=1}^{+\infty} \frac{1}{n^2+1}$.

**Correction :**
La série de Fourier est :
$$S(f)(t) = \frac{\sinh(\pi)}{\pi} + \frac{2\sinh(\pi)}{\pi} \sum_{n=1}^{+\infty} \frac{(-1)^n}{1+n^2} (\cos(nt) - n \sin(nt))$$
En évaluant en $t=\pi$, nous savons par le théorème de Dirichlet que $S(f)(\pi) = \cosh(\pi)$.
Par ailleurs, en insérant $t=\pi$ dans la série :
$$S(f)(\pi) = \frac{\sinh(\pi)}{\pi} + \frac{2\sinh(\pi)}{\pi} \sum_{n=1}^{+\infty} \frac{(-1)^n}{1+n^2} (\cos(n\pi) - n \sin(n\pi))$$
Or $\cos(n\pi) = (-1)^n$ et $\sin(n\pi) = 0$. Donc $(-1)^n \cos(n\pi) = (-1)^{2n} = 1$.
$$\cosh(\pi) = \frac{\sinh(\pi)}{\pi} + \frac{2\sinh(\pi)}{\pi} \sum_{n=1}^{+\infty} \frac{1}{1+n^2}$$
On divise le tout par $\frac{\sinh(\pi)}{\pi}$ :
$$\frac{\pi \cosh(\pi)}{\sinh(\pi)} = 1 + 2 \sum_{n=1}^{+\infty} \frac{1}{1+n^2}$$
Soit $\pi \coth(\pi) = 1 + 2 \sum_{n=1}^{+\infty} \frac{1}{1+n^2}$.
On isole la somme :
$$\sum_{n=1}^{+\infty} \frac{1}{1+n^2} = \frac{\pi \coth(\pi) - 1}{2}$$
