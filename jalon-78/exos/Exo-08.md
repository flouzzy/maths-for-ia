# Exercice 8 : Produit de signaux et décalage en fréquence \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f$ une fonction $2\pi$-périodique de coefficients de Fourier $c_n(f)$. On définit le signal modulé $g(t) = f(t) \cos(n_0 t)$ pour un entier $n_0 > 0$. Exprimer les $c_n(g)$ en fonction des $c_k(f)$.

**Correction Détaillée :**

1. \textbf{Utilisation des formules d'Euler :}
   On sait que $\cos(n_0 t) = \frac{e^{in_0 t} + e^{-in_0 t}}{2}$.
   Ainsi, on peut écrire :
   $$ g(t) = f(t) \frac{e^{in_0 t} + e^{-in_0 t}}{2} = \frac{1}{2} f(t)e^{in_0 t} + \frac{1}{2} f(t)e^{-in_0 t} $$

2. \textbf{Calcul du coefficient $c_n(g)$ par linéarité :}
   Par définition :
   $$ c_n(g) = \frac{1}{2\pi} \int_0^{2\pi} \left( \frac{1}{2} f(t)e^{in_0 t} + \frac{1}{2} f(t)e^{-in_0 t} \right) e^{-int} dt $$
   $$ c_n(g) = \frac{1}{2} \left( \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-i(n-n_0)t} dt + \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-i(n+n_0)t} dt \right) $$

3. \textbf{Identification avec les $c_k(f)$ :}
   L'intégrale $\frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-i(n-n_0)t} dt$ est exactement la définition de $c_{n-n_0}(f)$.
   De même, la seconde intégrale est $c_{n+n_0}(f)$.
   Ainsi :
   $$ c_n(g) = \frac{1}{2} (c_{n-n_0}(f) + c_{n+n_0}(f)) $$
   Cette propriété est fondamentale en télécommunications (modulation de fréquence), car elle montre que multiplier un signal par un cosinus décale son spectre d'une valeur $n_0$ vers la droite et vers la gauche.
