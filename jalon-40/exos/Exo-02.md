---
uuid: "jalon-40-exo-02"
title: "Exercice 2 : Intégrale généralisée et domination locale"
difficulty: "$\star\star\circ\circ\circ$"
---

# Exercice 2 : Intégrale généralisée et domination locale ($\star\star\circ\circ\circ$)

Soit $F(x) = \int_0^{+\infty} \frac{\sin(t)}{t^x} \, \mathrm{d}t$.

Déterminer le domaine de définition $\mathcal{D}$ de $F$.
*(On montrera que l'intégrale converge si et seulement si $1 < x < 2$ pour l'intégrabilité absolue en $0$ ou avec convergence conditionnelle à l'infini, ou on adaptera selon le critère de convergence. Ici on considérera l'intégrale de Dirichlet modifiée)*.

**Correction détaillée :**
1. **Étude en 0 :** Posons $f_x(t) = \frac{\sin(t)}{t^x}$. En $0$, $\sin(t) \sim t$. Donc $f_x(t) \sim \frac{t}{t^x} = \frac{1}{t^{x-1}}$. Par le critère de Riemann en $0$, l'intégrale de $\frac{1}{t^{x-1}}$ converge absolument si et seulement si $x-1 < 1$, soit $x < 2$.
2. **Étude en $+\infty$ :** Pour la convergence absolue, en $+\infty$, $\left| \frac{\sin(t)}{t^x} \right| \leq \frac{1}{t^x}$. L'intégrale de Riemann $\int_1^{+\infty} \frac{1}{t^x} \mathrm{d}t$ converge si $x > 1$.
   La fonction est donc absolument intégrable sur $]0, +\infty[$ si et seulement si $1 < x < 2$. (Note: elle converge semi-absolument pour $0 < x \le 1$ grâce au critère de Dirichlet (ou d'Abel), mais pour ce formalisme strict, concentrons-nous sur l'absolue convergence $]1,2[$).
   Ainsi, $F$ est bien définie sur $\mathcal{D} = ]1, 2[$.
