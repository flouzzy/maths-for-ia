# Exercice 2 : Inclusions strictes sur un espace de mesure infinie \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
On se place sur $X = [1, +\infty[$ muni de la mesure de Lebesgue $\lambda$.
Trouver une fonction $f \in L^2(\lambda)$ qui n'est pas dans $L^1(\lambda)$.

**Correction :**
Considérons la fonction $f(x) = \frac{1}{x}$.
1. Vérifions si $f \in L^2(\lambda)$ :
$\int_1^{+\infty} |f(x)|^2 dx = \int_1^{+\infty} \frac{1}{x^2} dx = \left[ -\frac{1}{x} \right]_1^{+\infty} = 0 - (-1) = 1 < +\infty$.
Donc $f \in L^2(\lambda)$.

2. Vérifions si $f \in L^1(\lambda)$ :
$\int_1^{+\infty} |f(x)| dx = \int_1^{+\infty} \frac{1}{x} dx = \left[ \ln(x) \right]_1^{+\infty} = +\infty$.
Donc $f \notin L^1(\lambda)$.

Ceci montre que sur un espace de mesure infinie, l'inclusion $L^q \subset L^p$ (pour $q > p$) n'est pas nécessairement vraie.
