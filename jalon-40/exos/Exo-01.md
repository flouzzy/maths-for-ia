---
uuid: "jalon-40-exo-01"
title: "Exercice 1 : Intégrale sur un segment fini"
difficulty: "$\star\circ\circ\circ\circ$"
---

# Exercice 1 : Intégrale sur un segment fini ($\star\circ\circ\circ\circ$)

Soit la fonction $F(x) = \int_0^1 \frac{e^{-xt}}{1+t^2} \, \mathrm{d}t$, pour $x \in \mathbb{R}$.

1. Montrer que $F$ est de classe $\mathcal{C}^1$ sur $\mathbb{R}$.
2. Calculer sa dérivée $F'(x)$ sous forme d'une intégrale.
3. Déterminer le signe de $F'(x)$ et en déduire le sens de variation de $F$.

**Correction détaillée :**
1. **Régularité et intégrabilité :** Posons $f(x,t) = \frac{e^{-xt}}{1+t^2}$. L'intervalle d'intégration $I = [0,1]$ est un segment fini. Pour tout $t \in [0,1]$, l'application $x \mapsto f(x,t)$ est de classe $\mathcal{C}^\infty$ sur $\mathbb{R}$, avec $\frac{\partial f}{\partial x}(x,t) = \frac{-t e^{-xt}}{1+t^2}$. Pour tout $x \in \mathbb{R}$, $t \mapsto f(x,t)$ et $t \mapsto \frac{\partial f}{\partial x}(x,t)$ sont continues sur $[0,1]$.
   **Domination sur un segment compact :** Pour obtenir une majoration indépendante de $x$, fixons un intervalle borné $[-A, A]$. Pour tout $(x,t) \in [-A,A] \times [0,1]$, on a $\left| \frac{\partial f}{\partial x}(x,t) \right| \leq \frac{1 \cdot e^{A\cdot 1}}{1+0} = e^A$. La constante $\psi(t) = e^A$ est une fonction constante donc trivialement intégrable sur le segment fini $[0,1]$. Par application du théorème de Leibniz sur tout $[-A, A]$, $F$ est $\mathcal{C}^1$ sur $\mathbb{R}$.
2. **Calcul de la dérivée :** Le théorème nous donne l'autorisation d'intervertir :
   $$ F'(x) = \int_0^1 \frac{\partial}{\partial x} \left( \frac{e^{-xt}}{1+t^2} \right) \, \mathrm{d}t = \int_0^1 \frac{-t e^{-xt}}{1+t^2} \, \mathrm{d}t $$
3. **Analyse du signe :** Sur $I = [0,1]$ (à part en $0$ où l'intégrande est nul), on a $t > 0$, $e^{-xt} > 0$ et $1+t^2 > 0$. Par positivité de l'intégrale d'une fonction strictement négative sur presque tout le segment, $F'(x) < 0$ pour tout $x \in \mathbb{R}$. Ainsi, $F$ est strictement décroissante sur $\mathbb{R}$.
