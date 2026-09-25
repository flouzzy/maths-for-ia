# Exercice 3 : Approximation d'une fraction rationnelle

**Niveau :** \bigstar\bigstar\star\star\star

**Énoncé :**
Soit $f(x) = \frac{1}{1+x^2}$.
1. Justifier que $f \in L^2(\mathbb{R})$.
2. Construire une suite $(g_n)$ de fonctions à support compact convergeant vers $f$ dans $L^2(\mathbb{R})$.

**Correction Détaillée :**
1. **Intégrabilité :**
   Calculons l'intégrale de $|f|^2$ :
   $\int_{\mathbb{R}} |f(x)|^2 dx = \int_{-\infty}^{+\infty} \frac{1}{(1+x^2)^2} dx$.
   En posant $x = \tan(\theta)$, $dx = (1+\tan^2\theta) d\theta = \frac{1}{\cos^2\theta} d\theta$.
   $\int_{-\pi/2}^{\pi/2} \cos^4(\theta) \frac{1}{\cos^2\theta} d\theta = \int_{-\pi/2}^{\pi/2} \cos^2(\theta) d\theta$.
   Par linéarisation : $\cos^2(\theta) = \frac{1+\cos(2\theta)}{2}$.
   L'intégrale vaut $[\frac{\theta}{2} + \frac{\sin(2\theta)}{4}]_{-\pi/2}^{\pi/2} = \frac{\pi}{4} - (-\frac{\pi}{4}) = \frac{\pi}{2} < +\infty$.
   Donc $f \in L^2(\mathbb{R})$.

2. **Troncature (Fonctions à support compact) :**
   Considérons l'indicatrice $I_n = \mathbf{1}_{[-n, n]}$ et posons $g_n(x) = f(x) \cdot I_n(x)$.
   Les fonctions $g_n$ sont à support compact $[-n, n]$. De plus, elles sont bornées et continues presque partout.
   Montrons la convergence :
   $\|f - g_n\|_2^2 = \int_{\mathbb{R}} |f(x) - f(x)\mathbf{1}_{[-n, n]}(x)|^2 dx = \int_{|x|>n} \frac{1}{(1+x^2)^2} dx$.
   Comme l'intégrale totale sur $\mathbb{R}$ est convergente (elle vaut $\pi/2$), le reste de l'intégrale tend vers $0$ lorsque $n \to +\infty$.
   Ainsi, $\lim_{n \to \infty} \|f - g_n\|_2 = 0$.
   C'est l'étape classique pour passer de $L^p(\mathbb{R})$ aux fonctions à support compact.
