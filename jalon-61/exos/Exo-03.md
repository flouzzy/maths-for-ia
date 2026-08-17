---
title: "Exercice 3 - L'indicatrice d'un ensemble fini"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 3 - L'indicatrice d'un ensemble fini

**Énoncé :**
Soit $A = \{a_1, \dots, a_p\} \subset [0, 1]$ un ensemble fini. Soit $h = 1_A$. Prouver que $h$ est Riemann-intégrable et que $\int_0^1 h(x) dx = 0$.

**Démonstration pas à pas :**
1. $h(x) = 1$ si $x \in A$, et $0$ sinon.
2. Pour $\epsilon > 0$, on construit une subdivision $\sigma$ telle que chaque $a_i$ est enfermé dans un sous-intervalle de longueur au plus $\epsilon / (2p)$.
3. La somme des longueurs de ces intervalles est au plus $p \cdot (\epsilon / 2p) = \epsilon/2$.
4. Sur ces intervalles, le supremum de $h$ est au plus 1. Sur les autres intervalles, $h$ vaut 0.
5. Donc $S(h, \sigma) \le 1 \cdot (\epsilon/2) = \epsilon/2 < \epsilon$.
6. De plus, $\inf h = 0$ partout, donc $s(h, \sigma) = 0$.
7. Comme on peut rendre $S - s < \epsilon$ pour tout $\epsilon > 0$, $h$ est Riemann-intégrable, et $\int_0^1 h = 0$.
