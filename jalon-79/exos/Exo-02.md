# Exercice 2 : Calcul de somme via la fonction $t^2$ $\bigstar\star\star\star\star$
**Énoncé :** Soit la fonction $f$ paire, $2\pi$-périodique, telle que $f(t) = t^2$ pour $t \in [-\pi, \pi]$.
Montrer que $a_0 = \frac{2\pi^2}{3}$ et $a_n = \frac{4(-1)^n}{n^2}$ pour $n \ge 1$.
En déduire la valeur de $\sum_{n=1}^\infty \frac{1}{n^4}$.

**Correction Détaillée :**
*Étape 1 : Calcul des coefficients de Fourier.*
$f$ est paire, donc $b_n = 0$.
$$a_0 = \frac{2}{\pi} \int_0^\pi t^2 dt = \frac{2}{\pi} \left[ \frac{t^3}{3} \right]_0^\pi = \frac{2\pi^2}{3}$$
Pour $n \ge 1$, on intègre par parties deux fois :
$$a_n = \frac{2}{\pi} \int_0^\pi t^2 \cos(nt) dt = \frac{2}{\pi} \left( \left[ t^2 \frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi 2t \frac{\sin(nt)}{n} dt \right)$$
Le premier terme est nul.
$$a_n = -\frac{4}{n\pi} \int_0^\pi t \sin(nt) dt = -\frac{4}{n\pi} \left( \left[ t \frac{-\cos(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{-\cos(nt)}{n} dt \right)$$
$$a_n = -\frac{4}{n\pi} \left( -\frac{\pi (-1)^n}{n} - 0 \right) = \frac{4(-1)^n}{n^2}$$

*Étape 2 : Calcul de l'énergie temporelle.*
$$\frac{1}{2\pi} \int_{-\pi}^\pi (t^2)^2 dt = \frac{1}{\pi} \int_0^\pi t^4 dt = \frac{1}{\pi} \frac{\pi^5}{5} = \frac{\pi^4}{5}$$

*Étape 3 : Application de l'identité de Parseval.*
$$\frac{\pi^4}{5} = \frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty a_n^2 = \frac{4\pi^4}{36} + \frac{1}{2} \sum_{n=1}^\infty \frac{16}{n^4} = \frac{\pi^4}{9} + 8 \sum_{n=1}^\infty \frac{1}{n^4}$$
$$8 \sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{5} - \frac{\pi^4}{9} = \frac{9\pi^4 - 5\pi^4}{45} = \frac{4\pi^4}{45}$$
$$\sum_{n=1}^\infty \frac{1}{n^4} = \frac{\pi^4}{90}$$
