# Exercice 2 : Espace $L^2$ (★☆☆☆☆)

**Énoncé :**
On se place dans $L^2([-\pi, \pi])$. Montrer que pour tout entier $n \ge 1$, la norme de $f_n(x) = \sin(nx)$ est $\sqrt{\pi}$.

**Correction Détaillée :**
*Analyse de l'énoncé :* Il faut calculer l'intégrale du carré de la fonction.

*Résolution pas-à-pas :*
Par définition de la norme dans $L^2$ :
$$ \|f_n\|^2 = \int_{-\pi}^{\pi} \sin^2(nx) dx $$

On utilise la formule de linéarisation $\sin^2(nx) = \frac{1 - \cos(2nx)}{2}$ :
$$ \|f_n\|^2 = \int_{-\pi}^{\pi} \frac{1 - \cos(2nx)}{2} dx $$
$$ \|f_n\|^2 = \frac{1}{2} \int_{-\pi}^{\pi} 1 dx - \frac{1}{2} \int_{-\pi}^{\pi} \cos(2nx) dx $$

Calculons chaque terme :
$$ \frac{1}{2} \int_{-\pi}^{\pi} 1 dx = \frac{1}{2} [x]_{-\pi}^{\pi} = \frac{1}{2}(\pi - (-\pi)) = \pi $$
$$ \int_{-\pi}^{\pi} \cos(2nx) dx = \left[ \frac{\sin(2nx)}{2n} \right]_{-\pi}^{\pi} = \frac{\sin(2n\pi) - \sin(-2n\pi)}{2n} = 0 $$

Donc $\|f_n\|^2 = \pi$, ce qui implique $\|f_n\| = \sqrt{\pi}$.
