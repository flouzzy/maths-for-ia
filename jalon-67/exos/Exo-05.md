---
title: "Application aux lois de probabilité"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---
# Application aux lois de probabilité
**Énoncé :**
Soit $X$ une variable aléatoire réelle positive de fonction de répartition $F_X$. En utilisant le TCM, exprimer l'espérance $\mathbb{E}[X]$ comme une intégrale de $1 - F_X$.

**Correction :**
1. Soit $X$ de densité $f$. $\mathbb{E}[X] = \int_0^{+\infty} x f(x) dx$.
2. On écrit $x = \int_0^x 1 \, dt = \int_0^{+\infty} \mathbf{1}_{\{t < x\}} dt$.
3. Alors $\mathbb{E}[X] = \int_0^{+\infty} \left( \int_0^{+\infty} \mathbf{1}_{\{t < x\}} dt \right) f(x) dx$.
4. Comme tout est positif, on peut appliquer Tonelli (qui est un cas particulier du corollaire du TCM pour l'interversion) :
   $\mathbb{E}[X] = \int_0^{+\infty} \left( \int_0^{+\infty} \mathbf{1}_{\{x > t\}} f(x) dx \right) dt$.
5. Or $\int_0^{+\infty} \mathbf{1}_{\{x > t\}} f(x) dx = \mathbb{P}(X > t) = 1 - F_X(t)$.
6. D'où $\mathbb{E}[X] = \int_0^{+\infty} (1 - F_X(t)) dt$.
