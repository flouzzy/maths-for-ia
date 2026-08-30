# Exercice 8 : Transformation de Fourier de la loi Gamma \quad $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Justifier l'intégration terme à terme pour calculer la transformée de Fourier de $f(x) = e^{-x} \frac{x^{k-1}}{(k-1)!}$ (loi Gamma) en développant l'exponentielle complexe.

## Correction Détaillée
L'exponentielle complexe $e^{itx}$ n'est pas positive, on ne peut pas utiliser Beppo Levi directement. Il faut utiliser la convergence dominée. Cependant, Beppo Levi permet de justifier la majoration absolue : $\int |\sum \frac{(itx)^n}{n!}| f(x) dx \le \int e^x f(x) dx$, ce qui valide l'absolue sommabilité.
