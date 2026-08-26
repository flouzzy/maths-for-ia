---
title: "Exercice 06 : Sous-additivité sur les ensembles"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 06 : Sous-additivité sur les ensembles

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $f \in \mathcal{M}_+$.
Soient $A, B \in \mathcal{F}$. Montrez que :
$$ \int_{A \cup B} f \, d\mu \le \int_A f \, d\mu + \int_B f \, d\mu $$
L'intégrale sur un ensemble $E$ est définie par $\int_X f \cdot \mathbf{1}_E \, d\mu$.

### Correction détaillée

1. Réécrivons l'inégalité en utilisant les fonctions indicatrices :
   On veut montrer $\int_X f \cdot \mathbf{1}_{A \cup B} \, d\mu \le \int_X f \cdot \mathbf{1}_A \, d\mu + \int_X f \cdot \mathbf{1}_B \, d\mu$.
2. Observons les fonctions indicatrices de ces ensembles.
   Pour tout point $x \in X$, par la théorie des ensembles, on a :
   $\mathbf{1}_{A \cup B}(x) \le \mathbf{1}_A(x) + \mathbf{1}_B(x)$.
   *(En effet, si $x \in A \cap B$, $1 \le 1 + 1 = 2$. Si $x$ est dans un seul, $1 \le 1 + 0 = 1$. Si $x$ n'est dans aucun, $0 \le 0 + 0 = 0$. L'inégalité est universellement vraie).*
3. Puisque $f$ est une fonction positive (à valeurs dans $[0, +\infty]$), on peut multiplier l'inégalité précédente par $f(x)$ en conservant le sens :
   $$ f(x) \cdot \mathbf{1}_{A \cup B}(x) \le f(x) \cdot \mathbf{1}_A(x) + f(x) \cdot \mathbf{1}_B(x) $$
4. En posant $g(x) = f(x) \cdot \mathbf{1}_{A \cup B}(x)$ et $h(x) = f(x) \cdot \mathbf{1}_A(x) + f(x) \cdot \mathbf{1}_B(x)$, nous avons $g \le h$ sur tout $X$, et $g, h \in \mathcal{M}_+$.
5. Par le théorème de monotonie (croissance) de l'intégrale de Lebesgue :
   $$ \int_X g \, d\mu \le \int_X h \, d\mu $$
6. Par ailleurs, l'additivité de l'intégrale des fonctions positives (linéarité pour la somme) garantit que :
   $$ \int_X (f \cdot \mathbf{1}_A + f \cdot \mathbf{1}_B) \, d\mu = \int_X f \cdot \mathbf{1}_A \, d\mu + \int_X f \cdot \mathbf{1}_B \, d\mu $$
   *(Note : cette additivité pour toute fonction mesurable positive résulte directement de l'additivité sur les fonctions simples et du passage à la limite supérieure, que l'on suppose démontrée dans le cours complet).*
7. En combinant les étapes 5 et 6, on obtient l'inégalité cherchée :
   $$ \int_{A \cup B} f \, d\mu \le \int_A f \, d\mu + \int_B f \, d\mu $$
