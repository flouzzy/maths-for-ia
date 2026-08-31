---
title: "Intégrale paramétrique et dérivabilité monotone"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---
# Intégrale paramétrique et dérivabilité monotone
**Énoncé :**
Soit $f(x, t)$ mesurable en $x$, différentiable en $t$. On suppose $f$ croissante en $t$. Montrer qu'on peut dériver sous le signe intégrale $\frac{d}{dt} \int f(x,t) dx = \int \frac{\partial f}{\partial t}(x,t) dx$ via le TCM (en supposant des bornes adaptées).

**Correction :**
1. Pour calculer la dérivée en $t_0$, considérons une suite $(h_n)$ de réels positifs tendant vers 0.
2. Posons $\Delta_n(x) = \frac{f(x, t_0+h_n) - f(x, t_0)}{h_n}$.
3. Par hypothèse, $f$ est croissante en $t$, donc $\Delta_n(x) \ge 0$.
4. Si on suppose de plus que la fonction est convexe en $t$, les pentes formées par les accroissements sont décroissantes quand $h_n \to 0$. Si on prend une suite $h_n \to 0$ décroissante, alors la suite $\Delta_n(x)$ n'est *pas* croissante. Le TCM seul ne suffit pas directement, mais on peut appliquer le TCM sur une fonction modifiée (ou via Fatou inversé).
5. Supposons plutôt l'inverse, que $h_n \to 0$ croissante par valeurs négatives (on approxime par la gauche). $h_n < 0$. $t_0+h_n$ croît. Donc $\Delta_n(x)$ croît !
6. Par le TCM sur $\Delta_n(x)$ positive, on intervertit limite et intégrale. On déduit que la limite à gauche de la dérivée de l'intégrale est l'intégrale de la dérivée. Le TCM justifie rigoureusement la dérivation.
