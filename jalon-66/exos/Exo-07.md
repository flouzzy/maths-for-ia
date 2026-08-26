---
title: "Exercice 07 : Inégalité de Markov classique"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 07 : Inégalité de Markov classique

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Soit $f \in \mathcal{M}_+$ une fonction mesurable positive, et $c > 0$ un réel strictement positif.
Démontrez rigoureusement, à partir de la définition de l'intégrale, l'inégalité de Markov :
$$ \mu(\{x \in X \mid f(x) \ge c\}) \le \frac{1}{c} \int_X f \, d\mu $$

### Correction détaillée

1. Considérons l'ensemble $A = \{x \in X \mid f(x) \ge c\}$. C'est un ensemble mesurable car $f$ est une fonction mesurable.
2. Définissons une fonction $g$ très simple sur $X$ : $g(x) = c \cdot \mathbf{1}_A(x)$.
3. Comparons $f(x)$ et $g(x)$ pour chaque $x \in X$ :
   - Si $x \notin A$, alors $g(x) = c \cdot 0 = 0$. Puisque $f \in \mathcal{M}_+$, on a $f(x) \ge 0 = g(x)$.
   - Si $x \in A$, alors par définition de $A$, $f(x) \ge c$. Or, $g(x) = c \cdot 1 = c$. Donc $f(x) \ge g(x)$.
   Dans tous les cas, $f(x) \ge g(x)$ pour tout $x \in X$.
4. Par le théorème de monotonie (croissance) de l'intégrale de Lebesgue démontré dans le cours :
   $$ \int_X g \, d\mu \le \int_X f \, d\mu $$
5. Or, $g$ est une fonction étagée de la forme $\alpha \mathbf{1}_A$. Son intégrale est par définition :
   $$ \int_X g \, d\mu = c \cdot \mu(A) $$
6. En substituant dans l'inégalité de l'étape 4 :
   $$ c \cdot \mu(A) \le \int_X f \, d\mu $$
7. Puisque $c > 0$, nous pouvons diviser les deux membres par $c$ sans changer le sens de l'inégalité :
   $$ \mu(A) \le \frac{1}{c} \int_X f \, d\mu $$
8. En remplaçant $A$ par sa définition, la démonstration de l'inégalité de Markov est achevée.
