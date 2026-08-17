---
title: "Exercice 7 - Oscillation en un point"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 7 - Oscillation en un point

**Énoncé :**
L'oscillation d'une fonction $f$ sur un intervalle $I$ est $\omega(f, I) = \sup_I f - \inf_I f$. Démontrer que la somme supérieure moins la somme inférieure s'écrit $\sum_{k=1}^n \omega(f, [x_{k-1}, x_k]) \Delta x_k$.

**Démonstration pas à pas :**
1. Par définition, $S(f, \sigma) = \sum \sup_{I_k} f \Delta x_k$.
2. Et $s(f, \sigma) = \sum \inf_{I_k} f \Delta x_k$.
3. En soustrayant terme à terme, $S(f, \sigma) - s(f, \sigma) = \sum (\sup_{I_k} f - \inf_{I_k} f) \Delta x_k$.
4. En remplaçant par la définition de l'oscillation, on obtient $\sum \omega(f, I_k) \Delta x_k$.
5. Pour que $f$ soit intégrable, cette somme pondérée d'oscillations doit pouvoir être rendue arbitrairement petite.
