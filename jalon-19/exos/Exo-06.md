---
titre: "Exercice 6 : Dérivabilité"
difficulte: "★★★☆☆"
---

# Exercice 6 : Pratique et maîtrise conceptuelle

**Énoncé :**
Soit $f$ de classe $\mathcal{C}^2$ sur $\mathbb{R}$. Si $f$ et $f''$ sont bornées sur $\mathbb{R}$, montrer que $f'$ est bornée sur $\mathbb{R}$ (Inégalité de Landau-Kolmogorov : $\|f'\|_\infty \leq \sqrt{2 \|f\|_\infty \|f''\|_\infty}$).

**Résolution Zéro Ellipse :**
1. Posons $M_0 = \sup_{\mathbb{R}} |f(x)|$ et $M_2 = \sup_{\mathbb{R}} |f''(x)|$.
2. Écrivons le développement de Taylor-Lagrange à l'ordre 2 entre $x$ et un point perturbé $x+h$ ($h > 0$) :
   $f(x+h) = f(x) + h f'(x) + \frac{h^2}{2} f''(c_1)$ avec $c_1 \in ]x, x+h[$.
3. Écrivons-le symétriquement pour $x-h$ :
   $f(x-h) = f(x) - h f'(x) + \frac{h^2}{2} f''(c_2)$ avec $c_2 \in ]x-h, x[$.
4. Soustrayons les deux expressions pour isoler le terme linéaire $f'(x)$ :
   $f(x+h) - f(x-h) = 2h f'(x) + \frac{h^2}{2} (f''(c_1) - f''(c_2))$.
5. Isolons algébriquement $f'(x)$ :
   $f'(x) = \frac{f(x+h) - f(x-h)}{2h} - \frac{h}{4} (f''(c_1) - f''(c_2))$.
6. Appliquons l'inégalité triangulaire :
   $|f'(x)| \leq \frac{|f(x+h)| + |f(x-h)|}{2h} + \frac{h}{4} (|f''(c_1)| + |f''(c_2)|)$.
7. Les fonctions étant bornées, on majore uniformément :
   $|f'(x)| \leq \frac{2M_0}{2h} + \frac{h}{4} (2M_2) = \frac{M_0}{h} + \frac{M_2}{2} h$.
8. Cette majoration est valide pour tout $x \in \mathbb{R}$ et tout $h > 0$. Pour obtenir la borne la plus fine, minimisons la fonction de $h : \psi(h) = \frac{M_0}{h} + \frac{M_2}{2} h$.
9. En annulant la dérivée $\psi'(h) = -\frac{M_0}{h^2} + \frac{M_2}{2} = 0$, on trouve le minimum pour $h_0 = \sqrt{2 \frac{M_0}{M_2}}$.
10. En substituant $h_0$, on obtient la borne désirée $\sqrt{2 M_0 M_2}$. $\blacksquare$
