# Exercice 5 : Calcul avec un signal non centré

**Difficulté :** \bigstar\bigstar\bigstar\star\star

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique définie par $f(t) = e^t$ sur $]-\pi, \pi[$.
1. Calculer les coefficients complexes de Fourier $c_n$ de $f$.
2. Écrire la série de Fourier en utilisant la notation réelle.
3. Que vaut la série en $t=\pi$ ?

**Correction :**
1. Calcul des coefficients complexes $c_n$ :
   $$c_n = \frac{1}{2\pi} \int_{-\pi}^\pi e^t e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(1-in)t} dt$$
   $$c_n = \frac{1}{2\pi} \left[ \frac{e^{(1-in)t}}{1-in} \right]_{-\pi}^\pi = \frac{1}{2\pi (1-in)} (e^{(1-in)\pi} - e^{-(1-in)\pi})$$
   Or, $e^{-in\pi} = (-1)^n = e^{in\pi}$. On obtient donc :
   $$c_n = \frac{(-1)^n}{2\pi (1-in)} (e^\pi - e^{-\pi}) = \frac{(-1)^n \sinh(\pi)}{\pi (1-in)}$$
   En multipliant le dénominateur par son conjugué $1+in$ :
   $$c_n = \frac{(-1)^n \sinh(\pi)}{\pi (1+n^2)} (1+in)$$
2. Pour repasser aux coefficients réels, on a $a_n = c_n + c_{-n}$ et $b_n = i(c_n - c_{-n})$.
   $$a_n = 2 \text{Re}(c_n) = \frac{2(-1)^n \sinh(\pi)}{\pi (1+n^2)}$$
   $$b_n = -2 \text{Im}(c_n) = -\frac{2(-1)^n n \sinh(\pi)}{\pi (1+n^2)}$$
   La série s'écrit (avec $a_0 = 2\frac{\sinh(\pi)}{\pi}$) :
   $$S(f)(t) = \frac{\sinh(\pi)}{\pi} + \frac{2\sinh(\pi)}{\pi} \sum_{n=1}^{+\infty} \frac{(-1)^n}{1+n^2} (\cos(nt) - n \sin(nt))$$
3. La fonction est de classe $C^1$ par morceaux, avec une discontinuité en $\pi$. Selon le théorème de Dirichlet, la série en $t=\pi$ converge vers $\frac{f(\pi^-) + f(-\pi^+)}{2} = \frac{e^\pi + e^{-\pi}}{2} = \cosh(\pi)$.
