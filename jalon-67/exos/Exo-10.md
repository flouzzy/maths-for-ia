---
uuid: "jalon-67-exo-10"
---
# Exercice 10 : Application du Théorème de Beppo Levi \quad $\bigstar$

**Énoncé :**
Considérons l'espace mesuré $([0, 1], \mathcal{B}([0, 1]), \lambda)$ et la suite de fonctions $f_n(x) = \sum_{k=1}^n \frac{x^k}{(k+10)!}$.
Démontrer rigoureusement l'interversion de la limite et de l'intégrale en justifiant les hypothèses.

**Correction Détaillée :**
1. **Initialisation :**
   Les fonctions $u_k(x) = \frac{x^k}{(k+10)!}$ sont des fonctions polynomiales, donc continues et mesurables sur $[0, 1]$. De plus, pour tout $x \in [0, 1]$, $u_k(x) \ge 0$.
2. **Croissance :**
   La suite de sommes partielles $f_n(x)$ est définie par l'accumulation de termes positifs. Ainsi, $f_{n+1}(x) - f_n(x) = u_{n+1}(x) \ge 0$, garantissant que la suite $(f_n)$ est croissante presque partout.
3. **Application de Beppo Levi :**
   Les fonctions $f_n$ sont mesurables, positives et forment une suite croissante. Par le Théorème de Convergence Monotone :
   $$\lim_{n \to \infty} \int_0^1 f_n(x) d\lambda(x) = \int_0^1 \lim_{n \to \infty} f_n(x) d\lambda(x)$$
4. **Calcul explicite :**
   L'intégrale de $u_k(x)$ est $\int_0^1 \frac{x^k}{(k+10)!} dx = \frac{1}{(k+1)(k+10)!}$.
   La somme de cette série converge, donc l'intégrale de la limite existe et est finie.
