---
uuid: "jalon-20-exo-10"
title: "Exercice 10 : ★★★★★"
---
# Exercice 10

## Énoncé
Inégalités de Kolmogorov. Soit $f : \mathbb{R} \to \mathbb{R}$ de classe $C^2$. On suppose que $f$ et $f''$ sont bornées sur $\mathbb{R}$, c'est-à-dire qu'il existe $M_0$ et $M_2$ tels que $\sup_{\mathbb{R}} |f| = M_0$ et $\sup_{\mathbb{R}} |f''| = M_2$. Montrer que $f'$ est bornée sur $\mathbb{R}$ et que $\sup_{\mathbb{R}} |f'| \le \sqrt{2 M_0 M_2}$.

## Correction
1. Soit $x \in \mathbb{R}$ et $h > 0$. Appliquons la formule de Taylor-Lagrange à l'ordre 1 entre $x$ et $x+h$ :
   $f(x+h) = f(x) + h f'(x) + \frac{h^2}{2} f''(c_1)$ avec $c_1 \in ]x, x+h[$.
2. Isolons $f'(x)$ :
   $h f'(x) = f(x+h) - f(x) - \frac{h^2}{2} f''(c_1)$.
   $f'(x) = \frac{f(x+h) - f(x)}{h} - \frac{h}{2} f''(c_1)$.
3. Utilisons l'inégalité triangulaire et les bornes $M_0, M_2$ :
   $|f'(x)| \le \frac{|f(x+h)| + |f(x)|}{h} + \frac{h}{2} |f''(c_1)|$.
   $|f'(x)| \le \frac{2M_0}{h} + \frac{h M_2}{2}$.
4. Cette inégalité est vraie pour tout $h > 0$. Considérons la fonction $\varphi(h) = \frac{2M_0}{h} + \frac{h M_2}{2}$ sur $]0, +\infty[$.
   Cherchons son minimum. $\varphi'(h) = -\frac{2M_0}{h^2} + \frac{M_2}{2} = 0 \iff h^2 = \frac{4M_0}{M_2} \iff h = 2\sqrt{\frac{M_0}{M_2}}$.
5. La valeur de $\varphi$ en ce point de minimum est :
   $\varphi(2\sqrt{\frac{M_0}{M_2}}) = \frac{2M_0}{2\sqrt{M_0/M_2}} + \frac{2\sqrt{M_0/M_2} M_2}{2} = \sqrt{M_0 M_2} + \sqrt{M_0 M_2} = 2\sqrt{M_0 M_2}$.
   Ici, nous devons ajuster l'inégalité classique. Taylor symétrique donne une meilleure borne :
6. Utilisons Taylor-Lagrange entre $x$ et $x-h$ :
   $f(x-h) = f(x) - h f'(x) + \frac{h^2}{2} f''(c_2)$.
7. Soustrayons la seconde relation à la première :
   $f(x+h) - f(x-h) = 2h f'(x) + \frac{h^2}{2} (f''(c_1) - f''(c_2))$.
   $f'(x) = \frac{f(x+h) - f(x-h)}{2h} - \frac{h}{4} (f''(c_1) - f''(c_2))$.
8. Majoration :
   $|f'(x)| \le \frac{2M_0}{2h} + \frac{h}{4} (M_2 + M_2) = \frac{M_0}{h} + \frac{h M_2}{2}$.
9. Minimisons $\psi(h) = \frac{M_0}{h} + \frac{h M_2}{2}$. $\psi'(h) = 0 \implies h = \sqrt{\frac{2M_0}{M_2}}$.
10. La valeur minimale est $\psi(\sqrt{\frac{2M_0}{M_2}}) = M_0 \sqrt{\frac{M_2}{2M_0}} + \frac{M_2}{2} \sqrt{\frac{2M_0}{M_2}} = \sqrt{\frac{M_0 M_2}{2}} + \sqrt{\frac{M_0 M_2}{2}} = \sqrt{2 M_0 M_2}$.
11. Donc pour tout $x$, $|f'(x)| \le \sqrt{2 M_0 M_2}$. Le résultat est prouvé. $\blacksquare$