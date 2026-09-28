# Exercice 5 : Estimation de l'erreur quadratique $\bigstar\bigstar\bigstar\star\star$
**Énoncé :** Soit $f(t) = \pi - t$ sur $]0, 2\pi[$.
On approche $f(t)$ par son polynôme trigonométrique partiel $S_N(f)(t) = \sum_{n=1}^N \frac{2}{n} \sin(nt)$.
Calculer l'erreur quadratique moyenne $E_N = \frac{1}{2\pi} \int_0^{2\pi} (f(t) - S_N(f)(t))^2 dt$ en fonction de $N$. Quelle est sa limite quand $N \to \infty$ ?

**Correction Détaillée :**
*Étape 1 : Coefficients de Fourier de $f$.*
On a $a_0 = \frac{1}{\pi} \int_0^{2\pi} (\pi - t) dt = \frac{1}{\pi} [\pi t - t^2/2]_0^{2\pi} = \frac{1}{\pi} (2\pi^2 - 2\pi^2) = 0$.
$a_n = 0$ car la fonction, translatée, se comporte comme une fonction impaire.
$$b_n = \frac{1}{\pi} \int_0^{2\pi} (\pi - t) \sin(nt) dt = \frac{1}{\pi} \left[ (\pi - t) \frac{-\cos(nt)}{n} \right]_0^{2\pi} - \frac{1}{\pi} \int_0^{2\pi} (-1) \frac{-\cos(nt)}{n} dt$$
$$b_n = \frac{1}{\pi} \left( (\pi - 2\pi) \frac{-1}{n} - \pi \frac{-1}{n} \right) - 0 = \frac{1}{\pi} \left( \frac{\pi}{n} + \frac{\pi}{n} \right) = \frac{2}{n}$$
Donc $S_N(f)$ est bien la somme partielle de Fourier de $f$.

*Étape 2 : Énergie totale de $f$.*
$$\frac{1}{2\pi} \int_0^{2\pi} (\pi - t)^2 dt = \frac{1}{2\pi} \left[ \frac{-(\pi - t)^3}{3} \right]_0^{2\pi} = \frac{1}{2\pi} \left( \frac{-(-\pi)^3}{3} - \frac{-\pi^3}{3} \right) = \frac{1}{2\pi} \frac{2\pi^3}{3} = \frac{\pi^2}{3}$$

*Étape 3 : Calcul de l'erreur quadratique $E_N$.*
Par le théorème de Pythagore (ou identité de Parseval tronquée) :
$$E_N = \| f - S_N(f) \|_2^2 = \| f \|_2^2 - \| S_N(f) \|_2^2$$
Or $\| S_N(f) \|_2^2 = \frac{1}{2} \sum_{n=1}^N b_n^2 = \frac{1}{2} \sum_{n=1}^N \frac{4}{n^2} = 2 \sum_{n=1}^N \frac{1}{n^2}$.
Donc $E_N = \frac{\pi^2}{3} - 2 \sum_{n=1}^N \frac{1}{n^2}$.

*Étape 4 : Limite.*
Quand $N \to \infty$, la série $\sum \frac{1}{n^2}$ converge vers $\frac{\pi^2}{6}$.
Donc $\lim E_N = \frac{\pi^2}{3} - 2 \left( \frac{\pi^2}{6} \right) = \frac{\pi^2}{3} - \frac{\pi^2}{3} = 0$.
Ceci confirme bien le théorème de convergence en moyenne quadratique.
