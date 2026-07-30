---
uuid: "jalon-40-exo-06"
title: "Exercice 6 : Limite d'intégrale (Théorème d'Abel)"
difficulty: "$\star\star\star\star\circ$"
---

# Exercice 6 : Limite d'intégrale (Théorème d'Abel) ($\star\star\star\star\circ$)

Évaluer $\lim_{x \to 0^+} \int_0^{+\infty} e^{-xt} \frac{1-\cos(t)}{t^2} \mathrm{d}t$.

**Correction détaillée :**
Posons $f(x,t) = e^{-xt} \frac{1-\cos(t)}{t^2}$.
Pour $x \geq 0$, $|f(x,t)| \leq \frac{1-\cos(t)}{t^2}$.
La fonction $\varphi(t) = \frac{1-\cos(t)}{t^2}$ est prolongable par continuité en $0$ par la limite $\frac{1}{2}$, et en $+\infty$, $\varphi(t) \leq \frac{2}{t^2}$, intégrable par Riemann.
L'hypothèse de domination globale est satisfaite sur $[0, +\infty[$.
Par le théorème de convergence dominée (ou continuité), $\lim_{x \to 0^+} \int_0^{+\infty} f(x,t) \mathrm{d}t = \int_0^{+\infty} f(0,t) \mathrm{d}t = \int_0^{+\infty} \frac{1-\cos(t)}{t^2} \mathrm{d}t = \frac{\pi}{2}$ (par IPP).
