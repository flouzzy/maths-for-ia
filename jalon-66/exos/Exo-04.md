# Propriété de l'ensemble de mesure nulle

**Difficulté :** $\star\star\star☆☆$

## Énoncé

Montrez que si $f \geq 0$ est mesurable et si $A \in \mathcal{A}$ vérifie $\mu(A) = 0$, alors $\int_X f \mathbb{1}_A \, d\mu = 0$.

---

## Correction détaillée

Soit $g = f \mathbb{1}_A$. On a $g(x) = f(x)$ si $x \in A$ et $g(x) = 0$ sinon.
Par définition, $\int_X g \, d\mu = \sup_{s \in \mathcal{E}^+, 0 \leq s \leq g} \int_X s \, d\mu$.
Soit $s \in \mathcal{E}^+$ telle que $0 \leq s \leq g$. Alors $s(x) = 0$ pour tout $x \notin A$. La fonction $s$ peut s'écrire sous forme canonique : $s = \sum_{i=1}^n \alpha_i \mathbb{1}_{B_i}$. Puisque $s=0$ hors de $A$, tous les ensembles $B_i$ correspondant à $\alpha_i > 0$ sont inclus dans $A$.
Par monotonie de la mesure, $\mu(B_i) \leq \mu(A) = 0$. Donc $\mu(B_i) = 0$.
Ainsi, l'intégrale de $s$ vaut $\sum \alpha_i \mu(B_i) = \sum \alpha_i \times 0 = 0$.
Le supremum d'un ensemble ne contenant que $0$ est $0$. CQFD.
