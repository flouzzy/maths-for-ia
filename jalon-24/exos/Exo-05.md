---
title: "Exercice 5 : Phénomène de Runge - Cas Analytique"
difficulty: ★★★★☆
---
# Énoncé
On considère la fonction de Runge $f(x) = \frac{1}{1+x^2}$ sur $[-5, 5]$.
Si on interpole cette fonction avec un polynôme $P_n$ sur $n$ points équidistants, démontrer heuristiquement l'origine de la divergence près des bornes en étudiant le comportement asymptotique du polynôme d'erreur nodale $\omega_n(x) = \prod_{i=1}^n (x - x_i)$.

# Correction Détaillée
L'erreur d'interpolation en un point $x$ est donnée par la formule de Cauchy :
$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \omega_{n+1}(x)$ où $\xi \in ]-5, 5[$.
1. **Croissance du polynôme nodal $\omega_n(x)$ :**
   Pour des points équidistants, la fonction $\omega_n(x)$ présente des oscillations très asymétriques. Près du centre (x=0), les amplitudes sont petites. Près des bornes (x $\approx \pm 5$), la distance aux autres points est maximale, entraînant une croissance exponentielle de l'amplitude de $\omega_n(x)$ par rapport à $n$ : $\|\omega_n\|_\infty \sim C \left(\frac{10}{e}\right)^n$.
2. **Dérivées d'ordre supérieur de la fonction de Runge :**
   La fonction $f(z) = \frac{1}{1+z^2}$ admet des pôles complexes en $z = \pm i$. Par analyse complexe, le domaine de convergence du développement de Taylor ou d'interpolation est borné par la distance au pôle le plus proche. Sur $[-5, 5]$, la distance au pôle est largement inférieure à la demi-longueur de l'intervalle, forçant les dérivées d'ordre $n$ à croître extrêmement vite, compensant le $(n+1)!$ au dénominateur.
3. **Conclusion :**
   Le produit de la croissance de $\omega_{n+1}(x)$ près des bornes et des dérivées massives de $f$ induit $\lim_{n \to \infty} \|f - P_n\|_\infty = \infty$. La régularisation ou le choix de nœuds de Tchebychev (qui minimisent $\|\omega_n\|_\infty$) est obligatoire pour forcer la convergence uniforme.
