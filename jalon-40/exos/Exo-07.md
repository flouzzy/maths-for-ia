---
uuid: "jalon-40-exo-07"
title: "Exercice 7 : Fonction de Bessel et développement"
difficulty: "$\star\star\star\star\star$"
---

# Exercice 7 : Fonction de Bessel et développement ($\star\star\star\star\star$)

Soit la fonction de Bessel d'ordre 0 : $J_0(x) = \frac{1}{\pi} \int_0^\pi \cos(x \sin(t)) \mathrm{d}t$.
Montrer que $J_0$ vérifie l'équation différentielle $x y'' + y' + x y = 0$.

**Correction détaillée :**
1. L'intervalle est compact $[0, \pi]$, l'intégrande $f(x,t) = \cos(x \sin(t))$ est de classe $\mathcal{C}^\infty$ en $x$. Domination acquise gratuitement pour toutes dérivées (bornées par 1).
2. Calcul des dérivées par Leibniz :
   $J_0'(x) = -\frac{1}{\pi} \int_0^\pi \sin(t) \sin(x \sin(t)) \mathrm{d}t$
   $J_0''(x) = -\frac{1}{\pi} \int_0^\pi \sin^2(t) \cos(x \sin(t)) \mathrm{d}t$.
3. Substituons dans l'équation :
   $x J_0''(x) + J_0'(x) + x J_0(x) = \frac{1}{\pi} \int_0^\pi [ -x\sin^2(t)\cos(x\sin(t)) - \sin(t)\sin(x\sin(t)) + x\cos(x\sin(t)) ] \mathrm{d}t$.
   En remarquant que $1 - \sin^2(t) = \cos^2(t)$, le terme devient $\frac{1}{\pi} \int_0^\pi [ x\cos^2(t)\cos(x\sin(t)) - \sin(t)\sin(x\sin(t)) ] \mathrm{d}t$.
4. Intégrons par parties le premier terme : $\int_0^\pi x\cos(t) \cdot (\cos(t)\cos(x\sin(t))) \mathrm{d}t$.
   Posons $u' = x\cos(t)\cos(x\sin(t))$ d'où $u = \sin(x\sin(t))$, et $v = \cos(t)$ d'où $v' = -\sin(t)$.
   Le terme de bord $[\cos(t)\sin(x\sin(t))]_0^\pi = \cos(\pi)\sin(0) - \cos(0)\sin(0) = 0$.
   Reste $-\int_0^\pi -\sin(t)\sin(x\sin(t)) \mathrm{d}t = \int_0^\pi \sin(t)\sin(x\sin(t)) \mathrm{d}t$.
   Ceci annule exactement le second terme de l'intégrale globale, d'où le résultat est $0$.
