# Exercice 7 : Identité de Parseval et Riemann Zêta $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
En utilisant la fonction $f(t) = t^2$ sur $]-\pi, \pi]$ :
1. Calculer sa série de Fourier.
2. Utiliser l'égalité de Parseval pour calculer $\zeta(4) = \sum_{n=1}^\infty \frac{1}{n^4}$.

**Correction Détaillée :**
1. **Série de Fourier :**
$f$ est paire, donc $b_n = 0$.
$a_0 = \frac{2}{\pi} \int_0^\pi t^2 dt = \frac{2\pi^2}{3}$.
Pour $n \ge 1$, $a_n = \frac{2}{\pi} \int_0^\pi t^2 \cos(nt) dt = \frac{4(-1)^n}{n^2}$ (par double IPP).
La série est $S(f)(t) = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n}{n^2} \cos(nt)$.

2. **Théorème de Parseval :**
La formule de Parseval stipule :
$$ \frac{1}{2\pi} \int_{-\pi}^\pi |f(t)|^2 dt = \frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty (a_n^2 + b_n^2) $$
Calcul du membre de gauche :
$$ \frac{1}{2\pi} \int_{-\pi}^\pi t^4 dt = \frac{2}{2\pi} \left[ \frac{t^5}{5} \right]_0^\pi = \frac{\pi^4}{5} $$
Calcul du membre de droite :
$$ \frac{1}{4} \left(\frac{2\pi^2}{3}\right)^2 + \frac{1}{2} \sum_{n=1}^\infty \left(\frac{4(-1)^n}{n^2}\right)^2 = \frac{\pi^4}{9} + \frac{16}{2} \sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{9} + 8\zeta(4) $$
Égalisation :
$$ \frac{\pi^4}{5} = \frac{\pi^4}{9} + 8\zeta(4) \implies 8\zeta(4) = \pi^4 \left( \frac{1}{5} - \frac{1}{9} \right) = \pi^4 \frac{4}{45} $$
$$ \zeta(4) = \frac{\pi^4}{90} $$
