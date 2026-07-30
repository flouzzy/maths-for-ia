---
uuid: "jalon-40-exo-05"
title: "Exercice 5 : Étude d'une fonction Gamma modifiée"
difficulty: "$\star\star\star\star\circ$"
---

# Exercice 5 : Étude d'une fonction Gamma modifiée ($\star\star\star\star\circ$)

Soit $\Gamma_1(x) = \int_0^{+\infty} t^{x-1} e^{-t} \mathrm{d}t$. Démontrer sa classe $\mathcal{C}^\infty$ sur $]0, +\infty[$.

**Correction détaillée :**
1. L'intégrande $f(x,t) = t^{x-1} e^{-t}$ est indéfiniment dérivable par rapport à $x$ sur $]0, +\infty[$. La dérivée $k$-ième est $\frac{\partial^k f}{\partial x^k}(x,t) = (\ln t)^k t^{x-1} e^{-t}$.
2. Domination sur tout compact $[a,b] \subset ]0, +\infty[$ :
   Soit $a \leq x \leq b$.
   - Pour $t \in ]0, 1]$, $|\frac{\partial^k f}{\partial x^k}(x,t)| \leq |\ln t|^k t^{a-1}$. Cette fonction est intégrable en $0$ car $a > 0$ (les logarithmes sont absorbés par les puissances).
   - Pour $t \in [1, +\infty[$, $|\frac{\partial^k f}{\partial x^k}(x,t)| \leq (\ln t)^k t^{b-1} e^{-t}$. Par croissances comparées, l'exponentielle écrase les puissances et log, donc intégrable en $+\infty$.
3. En posant la fonction majorante (somme des deux domaines), la règle de Leibniz s'applique récursivement. Donc $\Gamma_1$ est $\mathcal{C}^\infty$ et $\Gamma_1^{(k)}(x) = \int_0^{+\infty} (\ln t)^k t^{x-1} e^{-t} \mathrm{d}t$.
