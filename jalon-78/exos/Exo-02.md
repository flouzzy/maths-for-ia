# Exercice 2 : Signal triangulaire et convergence uniforme $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $g$ la fonction $2\pi$-périodique définie par $g(t) = |t|$ sur $]-\pi, \pi]$.
1. Calculer ses coefficients de Fourier réels.
2. Déterminer la somme de la série $\sum_{k=0}^{+\infty} \frac{1}{(2k+1)^2}$.

**Correction Détaillée :**
1. **Coefficients :**
La fonction $g$ est paire, donc $b_n = 0$ pour tout $n \ge 1$.
Calculons $a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} |t| dt = \frac{2}{\pi} \int_0^\pi t dt = \frac{2}{\pi} \left[\frac{t^2}{2}\right]_0^\pi = \pi$.
Pour $n \ge 1$, $a_n = \frac{2}{\pi} \int_0^\pi t \cos(nt) dt$.
Par intégration par parties : $u=t, v'=\cos(nt) \implies u'=1, v=\frac{\sin(nt)}{n}$.
$$ a_n = \frac{2}{\pi} \left( \left[ t\frac{\sin(nt)}{n} \right]_0^\pi - \int_0^\pi \frac{\sin(nt)}{n} dt \right) $$
Le terme crochet est nul car $\sin(n\pi)=0$. Reste :
$$ a_n = -\frac{2}{n\pi} \left[ \frac{-\cos(nt)}{n} \right]_0^\pi = \frac{2}{n^2\pi} (\cos(n\pi) - 1) = \frac{2}{n^2\pi} ((-1)^n - 1) $$
Si $n=2k$, $a_{2k} = 0$. Si $n=2k+1$, $a_{2k+1} = \frac{-4}{(2k+1)^2\pi}$.
La série s'écrit :
$$ S(g)(t) = \frac{\pi}{2} - \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{\cos((2k+1)t)}{(2k+1)^2} $$

2. **Somme de série numérique :**
$g$ est continue et de classe $C^1$ par morceaux, donc la série converge ponctuellement vers $g(t)$ pour tout $t$ (Théorème de Dirichlet).
Évaluons en $t=0$ : $g(0) = 0$.
$$ 0 = \frac{\pi}{2} - \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{1}{(2k+1)^2} \implies \sum_{k=0}^{+\infty} \frac{1}{(2k+1)^2} = \frac{\pi^2}{8} $$
