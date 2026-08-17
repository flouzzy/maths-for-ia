---
title: "Exercice 8 - Critère de Lebesgue pour l'intégrabilité de Riemann"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 8 - Lien avec la continuité

**Énoncé :**
Une fonction $f$ est Riemann-intégrable sur $[a, b]$ si et seulement si l'ensemble de ses points de discontinuité est de mesure de Lebesgue nulle. (Théorème de Lebesgue). Vérifier ce critère pour les fonctions de Dirichlet et de Thomae.

**Démonstration pas à pas :**
1. **Fonction de Dirichlet** : $f$ est discontinue en tout point de $[0, 1]$. En effet, pour tout $x \in [0, 1]$, et tout voisinage de $x$, $f$ oscille entre 0 et 1. L'ensemble des points de discontinuité est $[0, 1]$, dont la mesure (longueur) est $1 \neq 0$. Donc $f$ n'est pas Riemann-intégrable.
2. **Fonction de Thomae** : $T(x)$ est discontinue sur $\mathbb{Q} \cap (0, 1)$ et continue sur les irrationnels (puisque la limite de $T(y)$ quand $y \to x$ irrationnel est 0).
3. L'ensemble des discontinuités est $\mathbb{Q} \cap (0, 1)$. Étant dénombrable, sa mesure de Lebesgue est 0.
4. Le théorème de Lebesgue s'applique : $T$ est Riemann-intégrable, ce qui confirme l'Exercice 5.
