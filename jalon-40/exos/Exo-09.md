---
title: "Exercice 9 : Intégrale de Fresnel"
difficulty: "$\star$$\star$$\star$$\star$$\star$"
---
# Exercice 9 : Intégrale de Fresnel ($\star$$\star$$\star$$\star$$\star$)

**Énoncé :**
Étudier la convergence et calculer l'intégrale $\int_0^{+\infty} \sin(t^2) dt$ en introduisant la fonction à paramètre $F(x) = \int_0^{+\infty} e^{-x^2 t^2} \sin(t^2) dt$ pour $x>0$.

**Démonstration pas-à-pas :**
1. La fonction $F(x)$ s'évalue en combinant le cosinus et le sinus via l'exponentielle complexe.
   $F(x) = Im\left(\int_0^{+\infty} e^{(-x^2 + i)t^2} dt\right)$.
2. On pose le changement de variable $u = t \sqrt{x^2-i}$. Le contour d'intégration dans le plan complexe se justifie par le théorème de Cauchy.
   On trouve $F(x) = Im\left( \frac{\sqrt{\pi}}{2 \sqrt{x^2 - i}} \right)$.
3. Pour trouver $\sqrt{x^2 - i}$, on utilise la forme polaire du nombre complexe et on prend la détermination principale.
   $\sqrt{x^2 - i} = (x^4 + 1)^{1/4} e^{-i \frac{\arctan(1/x^2)}{2}}$.
4. Ainsi $F(x) = \frac{\sqrt{\pi}}{2 (x^4+1)^{1/4}} \sin\left( \frac{\arctan(1/x^2)}{2} \right)$.
5. L'intégrale de Fresnel est obtenue en passant à la limite $x \to 0^+$.
   $\lim_{x \to 0^+} F(x) = \frac{\sqrt{\pi}}{2} \sin\left( \frac{\pi}{4} \right) = \frac{\sqrt{\pi}}{2} \frac{\sqrt{2}}{2} = \sqrt{\frac{\pi}{8}}$.
