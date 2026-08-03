---
title: "Exercice 1 : Calcul de limite par majoration (1)"
difficulty: $\bigstar\star\star\star\star$
---

# Exercice 1 : Calcul de limite par majoration

## Énoncé

Déterminer la limite, si elle existe, de la fonction suivante en $(0,0)$ :
$$ f(x, y) = \frac{x^2 y}{x^2 + y^2} $$

## Solution détaillée

1. **Étude au point $(0,0)$** :
   La fonction $f$ est définie sur $\mathbb{R}^2 \setminus \{(0,0)\}$.

2. **Recherche d'une majoration** :
   Nous devons trouver une limite lorsque $(x,y) \to (0,0)$. Regardons la valeur absolue :
   $$ |f(x, y)| = \frac{x^2 |y|}{x^2 + y^2} $$

   Nous savons que $x^2 \leq x^2 + y^2$ (puisque $y^2 \geq 0$).
   Par conséquent, on a l'inégalité suivante :
   $$ \frac{x^2}{x^2 + y^2} \leq 1 $$

   En multipliant par $|y|$ (qui est positif), on obtient :
   $$ |f(x, y)| = \left( \frac{x^2}{x^2 + y^2} \right) |y| \leq 1 \cdot |y| = |y| $$

3. **Conclusion par le théorème d'encadrement** :
   Nous avons établi que :
   $$ 0 \leq |f(x, y)| \leq |y| $$

   Or, $\lim_{(x,y) \to (0,0)} |y| = 0$.
   D'après le théorème des gendarmes (ou d'encadrement), on en déduit que :
   $$ \lim_{(x,y) \to (0,0)} |f(x, y)| = 0 $$
   Ce qui équivaut à :
   $$ \lim_{(x,y) \to (0,0)} f(x, y) = 0 $$
