# Exercice 2 : Base hilbertienne de l'espace des fonctions complexes de carré intégrable $\bigstar\bigstar\star\star\star$

**Énoncé :**
Dans $H = L^2([-\pi, \pi], \mathbb{C})$ muni du produit scalaire $\langle f, g \rangle = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) \overline{g(t)} dt$, on considère la famille $e_n(t) = e^{int}$ pour $n \in \mathbb{Z}$.
Soit la fonction $f(t) = e^t$.
1. Calculer les coefficients de Fourier complexes $c_n$ de la fonction $f$.
2. En appliquant l'identité de Parseval, en déduire la valeur de la somme de la série $\sum_{n=-\infty}^{+\infty} \frac{1}{n^2 + 1}$.

**Correction détaillée :**
1. Le coefficient de Fourier d'indice $n$ est :
   $c_n = \langle f, e_n \rangle = \frac{1}{2\pi} \int_{-\pi}^\pi e^t e^{-int} dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{(1-in)t} dt$
   $c_n = \frac{1}{2\pi} \left[ \frac{e^{(1-in)t}}{1-in} \right]_{-\pi}^\pi$
   Puisque $e^{-in\pi} = (-1)^n = (-1)^{-n} = e^{in\pi}$, nous avons :
   $c_n = \frac{1}{2\pi(1-in)} (e^\pi (-1)^n - e^{-\pi} (-1)^n) = \frac{(-1)^n}{2\pi(1-in)} (e^\pi - e^{-\pi}) = \frac{(-1)^n \sinh(\pi)}{\pi(1-in)}$
   Pour séparer la partie réelle et imaginaire au dénominateur, multiplions par le conjugué :
   $c_n = \frac{(-1)^n \sinh(\pi) (1+in)}{\pi(1+n^2)}$

2. Calculons la norme au carré de la fonction $f$ :
   $\|f\|^2 = \langle f, f \rangle = \frac{1}{2\pi} \int_{-\pi}^\pi e^t e^t dt = \frac{1}{2\pi} \int_{-\pi}^\pi e^{2t} dt = \frac{1}{2\pi} \left[ \frac{e^{2t}}{2} \right]_{-\pi}^\pi = \frac{e^{2\pi} - e^{-2\pi}}{4\pi} = \frac{\sinh(2\pi)}{2\pi}$
   L'identité de Parseval stipule que $\|f\|^2 = \sum_{n=-\infty}^{+\infty} |c_n|^2$.
   Calculons $|c_n|^2$ :
   $|c_n|^2 = c_n \overline{c_n} = \left| \frac{(-1)^n \sinh(\pi)}{\pi(1-in)} \right|^2 = \frac{\sinh^2(\pi)}{\pi^2 (1^2 + (-n)^2)} = \frac{\sinh^2(\pi)}{\pi^2 (1+n^2)}$
   Ainsi, par l'identité de Parseval :
   $\frac{\sinh(2\pi)}{2\pi} = \sum_{n=-\infty}^{+\infty} \frac{\sinh^2(\pi)}{\pi^2 (1+n^2)}$
   $\sum_{n=-\infty}^{+\infty} \frac{1}{n^2 + 1} = \frac{\pi^2 \sinh(2\pi)}{2\pi \sinh^2(\pi)}$
   On sait que $\sinh(2\pi) = 2\sinh(\pi)\cosh(\pi)$, donc :
   $\sum_{n=-\infty}^{+\infty} \frac{1}{n^2 + 1} = \frac{\pi \times 2\sinh(\pi)\cosh(\pi)}{2 \sinh^2(\pi)} = \frac{\pi \cosh(\pi)}{\sinh(\pi)} = \pi \coth(\pi)$.
