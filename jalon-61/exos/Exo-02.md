---
title: "Exercice 2 - Fonction modifiée et densité"
difficulty: $\bigstar\star\star\star\star$
---

# Exercice 2 - Fonction de Dirichlet modifiée

**Énoncé :**
Soit $g(x) = x$ si $x \in \mathbb{Q}$ et $0$ si $x \in \mathbb{R} \setminus \mathbb{Q}$, définie sur $[0, 1]$. Montrer que $g$ n'est pas Riemann-intégrable.

**Démonstration pas à pas :**
1. Sur tout sous-intervalle $[x_{k-1}, x_k]$ de $[0, 1]$, on a $\inf_{t} g(t) = 0$ (densité des irrationnels, où $g(t)=0$). Donc $s(g, \sigma) = 0$.
2. Pour la somme supérieure, $\sup_{t \in [x_{k-1}, x_k]} g(t) = x_k$ (car $\mathbb{Q}$ est dense et $g(t)=t$ sur $\mathbb{Q}$, et $t \mapsto t$ est croissante).
3. La somme supérieure est $S(g, \sigma) = \sum_{k=1}^n x_k (x_k - x_{k-1})$.
4. En raffinant la subdivision, $\inf S(g, \sigma) = \int_0^1 x dx = 1/2$.
5. Puisque $\sup s(g, \sigma) = 0 \neq 1/2 = \inf S(g, \sigma)$, la fonction $g$ n'est pas Riemann-intégrable.
