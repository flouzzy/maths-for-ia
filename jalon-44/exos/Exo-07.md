---
title: "Exercice 7 : Pathologie limite et factorisation"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 7 : Pathologie limite et factorisation

## Énoncé

Soit $f(x, y) = \frac{x^3 - y^3}{x - y}$, définie pour $x \neq y$.
Montrer que l'on peut prolonger $f$ par continuité en tout point de la droite $y = x$.

## Solution détaillée

1. **Identification du domaine et du problème** :
   La fonction est définie sur $D = \{ (x, y) \in \mathbb{R}^2 \mid x \neq y \}$.
   Le problème de continuité se pose sur la droite d'équation $y = x$, où on a une forme indéterminée "0/0".

2. **Factorisation algébrique** :
   L'expression au numérateur $x^3 - y^3$ est une identité remarquable classique.
   On peut la factoriser ainsi :
   $$ x^3 - y^3 = (x - y)(x^2 + xy + y^2) $$

3. **Simplification de la fonction sur son domaine** :
   Pour tout point $(x, y)$ tel que $x \neq y$ (c'est-à-dire là où $f$ est définie), le terme $(x - y)$ est non nul.
   On peut donc diviser le numérateur et le dénominateur par $(x - y)$ :
   $$ f(x, y) = \frac{(x - y)(x^2 + xy + y^2)}{x - y} = x^2 + xy + y^2 $$

4. **Étude de la limite aux points problématiques** :
   Soit $(a, a)$ un point quelconque de la droite $y = x$.
   Cherchons la limite de $f(x, y)$ lorsque $(x, y)$ s'approche de $(a, a)$ :
   $$ \lim_{(x,y) \to (a,a)} f(x, y) = \lim_{(x,y) \to (a,a)} (x^2 + xy + y^2) $$

   La nouvelle expression simplifiée $P(x, y) = x^2 + xy + y^2$ est un polynôme de deux variables. Un polynôme est une fonction partout continue sur $\mathbb{R}^2$.
   On peut donc évaluer sa limite en substituant directement $x=a$ et $y=a$ :
   $$ \lim_{(x,y) \to (a,a)} (x^2 + xy + y^2) = a^2 + a\cdot a + a^2 = a^2 + a^2 + a^2 = 3a^2 $$

5. **Conclusion et prolongement** :
   Pour tout point $(a, a)$ sur la diagonale, la limite existe et vaut $3a^2$.
   La fonction $f$ est donc prolongeable par continuité sur tout $\mathbb{R}^2$ en posant, pour les points où $x=y$ :
   $$ f(x, x) = 3x^2 $$
