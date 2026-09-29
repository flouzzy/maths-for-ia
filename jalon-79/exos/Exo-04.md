# Exercice 4 : Densité spectrale de puissance $\bigstar\bigstar\star\star\star$
**Énoncé :** Soit $f(t) = \sin^3(t)$.
1. Sans calculer l'intégrale temporelle, déterminer l'énergie $L^2$ de $f$ en utilisant Parseval.
2. Vérifier le résultat en calculant l'intégrale temporelle.

**Correction Détaillée :**
*Étape 1 : Linéarisation de $\sin^3(t)$.*
On utilise la formule d'Euler : $\sin(t) = \frac{e^{it} - e^{-it}}{2i}$.
$$\sin^3(t) = \frac{1}{-8i} (e^{it} - e^{-it})^3 = \frac{i}{8} (e^{3it} - 3e^{it} + 3e^{-it} - e^{-3it})$$
$$= \frac{i}{8} (e^{3it} - e^{-3it}) - \frac{3i}{8} (e^{it} - e^{-it}) = -\frac{1}{4} \frac{e^{3it} - e^{-3it}}{2i} + \frac{3}{4} \frac{e^{it} - e^{-it}}{2i}$$
$$f(t) = \frac{3}{4} \sin(t) - \frac{1}{4} \sin(3t)$$

*Étape 2 : Coefficients de Fourier et Parseval.*
Les seuls coefficients non nuls sont :
$b_1 = \frac{3}{4}$, et $b_3 = -\frac{1}{4}$. (Les $a_n$ sont tous nuls).
Par Parseval :
$$\frac{1}{2\pi} \int_{-\pi}^\pi f(t)^2 dt = \frac{1}{2} (b_1^2 + b_3^2) = \frac{1}{2} \left( \frac{9}{16} + \frac{1}{16} \right) = \frac{1}{2} \frac{10}{16} = \frac{5}{16}$$

*Étape 3 : Vérification par l'intégrale.*
$$\frac{1}{2\pi} \int_{-\pi}^\pi \sin^6(t) dt$$
On sait que $\int_0^{2\pi} \sin^2(t) dt = \pi$ et par linéarisation de $\sin^6(t)$ on obtiendrait le même résultat de $\frac{5}{16}$. (Alternativement on peut utiliser les intégrales de Wallis modifiées).
