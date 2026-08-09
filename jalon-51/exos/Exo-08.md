---
title: "Exo-08 : Complétion d'un espace métrique"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exo-08 : Complétion d'un espace métrique


## 1. Énoncé

On considère l'espace $\mathbb{Q}$ muni de la distance usuelle $d(x, y) = |x - y|$.
Soit la suite $(u_n)$ définie par $u_0 = 1$ et $u_{n+1} = \frac{1}{2}(u_n + \frac{2}{u_n})$.

1. Montrer que $(u_n)$ est une suite de Cauchy dans $(\mathbb{Q}, d)$.
2. La suite $(u_n)$ converge-elle dans $\mathbb{Q}$ ?
3. Que conclut-on sur l'espace métrique $(\mathbb{Q}, d)$ ?

## 2. Correction détaillée

**Question 1 :**
La suite est la méthode de Héron pour approximer $\sqrt{2}$. Par une étude classique (niveau Bac S / L1), on montre que pour $n \ge 1$, $u_n \ge \sqrt{2}$ et que la suite est décroissante, minorée par $\sqrt{2}$.
Elle converge donc dans $\mathbb{R}$ vers $\sqrt{2}$.
Toute suite convergente dans $\mathbb{R}$ est une suite de Cauchy dans $\mathbb{R}$.
Cela signifie : $\forall \epsilon > 0, \exists N, \forall p,q \ge N, |u_p - u_q| < \epsilon$.
Cette définition de suite de Cauchy ne fait intervenir que la distance $|u_p - u_q|$ entre les termes, qui sont tous rationnels (récurrence évidente sur $\mathbb{Q}$).
Donc $(u_n)$ est une suite de Cauchy dans $\mathbb{Q}$.

**Question 2 :**
Si la suite convergeait dans $\mathbb{Q}$, elle aurait une limite $l \in \mathbb{Q}$.
Par passage à la limite dans la relation de récurrence (les opérations algébriques étant continues), on aurait $l = \frac{1}{2}(l + \frac{2}{l})$, ce qui équivaut à $l^2 = 2$.
Or, on sait (depuis les Grecs) qu'il n'existe aucun rationnel $l$ tel que $l^2 = 2$.
Donc, bien qu'elle soit de Cauchy, la suite $(u_n)$ ne converge pas dans $\mathbb{Q}$.

**Question 3 :**
Un espace métrique dans lequel toute suite de Cauchy converge est dit **complet**.
L'espace métrique $(\mathbb{Q}, d)$ possède des suites de Cauchy divergentes ; il n'est donc **pas complet**. Ce manque topologique justifie la construction (complétion) de l'ensemble des réels $\mathbb{R}$.
