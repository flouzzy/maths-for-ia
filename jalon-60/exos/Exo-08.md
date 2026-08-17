## Exercice 8 : Régularité et borne d'erreur de Barron \quad $\bigstar\bigstar\bigstar\bigstar\star$

Le théorème de Cybenko ne précise pas la vitesse de convergence. Citer et utiliser le résultat de Barron (1993) pour borner l'erreur d'approximation en fonction du nombre de neurones $N$ pour une fonction $f$ ayant un moment d'ordre 1 fini pour sa transformée de Fourier.

**Correction :**
Le théorème de Barron stipule que si la transformée de Fourier de $f$, notée $\hat{f}(\omega)$, vérifie $C_f = \int_{\mathbb{R}^n} |\omega| |\hat{f}(\omega)| d\omega < \infty$, alors il existe un réseau $G_N$ avec $N$ neurones (couche cachée) tel que l'erreur quadratique moyenne vérifie :
$$\int_{I_n} (f(x) - G_N(x))^2 dx \le \frac{C_f^2}{N}$$
L'erreur décroît donc en $\mathcal{O}(1/\sqrt{N})$.
Il est remarquable que cette borne de convergence $1/\sqrt{N}$ est indépendante de la dimension de l'espace d'entrée $n$, ce qui permet aux réseaux de neurones d'échapper partiellement à la malédiction de la dimension, contrairement aux méthodes d'approximation traditionnelles (par exemple par polynômes ou splines) dont l'erreur typique décroît en $\mathcal{O}(N^{-s/n})$ où $s$ est la régularité.
