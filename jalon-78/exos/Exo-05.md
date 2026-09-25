# Exercice 5 : Signal impulsionnel périodique \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f$ la fonction $2\pi$-périodique définie sur $[-\pi, \pi]$ par $f(t) = 1$ si $t \in [0, \alpha]$ (avec $0 < \alpha < \pi$) et $0$ sinon. Calculer ses coefficients de Fourier complexes.

**Correction Détaillée :**

1. \textbf{Formule des coefficients complexes :}
   Par définition, pour tout $n \in \mathbb{Z}$ :
   $$ c_n = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) e^{-int} dt $$
   Puisque $f(t)$ vaut 1 sur $[0, \alpha]$ et 0 ailleurs sur la période, l'intégrale se réduit à :
   $$ c_n = \frac{1}{2\pi} \int_0^\alpha e^{-int} dt $$

2. \textbf{Calcul de $c_0$ :}
   Pour $n = 0$, la fonction à intégrer est $1$.
   $$ c_0 = \frac{1}{2\pi} \int_0^\alpha 1 dt = \frac{\alpha}{2\pi} $$
   C'est le rapport cyclique du signal.

3. \textbf{Calcul de $c_n$ pour $n \neq 0$ :}
   La primitive de $e^{-int}$ est $\frac{e^{-int}}{-in}$.
   $$ c_n = \frac{1}{2\pi} \left[ \frac{e^{-int}}{-in} \right]_0^\alpha = \frac{e^{-in\alpha} - 1}{-2i\pi n} = \frac{1 - e^{-in\alpha}}{2i\pi n} $$

4. \textbf{Mise sous forme amplitude/phase (astuce de l'arc moitié) :}
   On factorise par $e^{-in\alpha/2}$ :
   $$ c_n = \frac{e^{-in\alpha/2} (e^{in\alpha/2} - e^{-in\alpha/2})}{2i\pi n} = \frac{e^{-in\alpha/2} \cdot 2i \sin(n\alpha/2)}{2i\pi n} = \frac{\sin(n\alpha/2)}{n\pi} e^{-in\alpha/2} $$
   C'est l'expression classique faisant apparaître un terme en sinus cardinal (sinc).
