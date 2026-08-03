---
title: "Exercice 10 : Preuve epsilon-delta"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 10 : Preuve Epsilon-Delta Rigoureuse

## Énoncé

Démontrer en utilisant exclusivement la définition formelle (avec $\varepsilon$ et $\delta$) que :
$$ \lim_{(x,y) \to (1,2)} (2x + 3y) = 8 $$

## Solution détaillée

1. **Rappel de la définition formelle** :
   Nous voulons prouver que :
   $$ \forall \varepsilon > 0, \exists \delta > 0, \forall (x,y) \in \mathbb{R}^2, $$
   $$ 0 < \sqrt{(x-1)^2 + (y-2)^2} < \delta \implies |(2x + 3y) - 8| < \varepsilon $$

2. **Phase de brouillon (Recherche de $\delta$)** :
   Évaluons la quantité $|f(x,y) - L|$ et tentons de la lier à la distance $\|(x,y) - (1,2)\|$.
   L'expression est : $|2x + 3y - 8|$.

   Nous devons faire apparaître les termes $(x-1)$ et $(y-2)$, qui sont les composantes du vecteur distance.
   Remarquons que $8 = 2(1) + 3(2)$. Substituons astucieusement :
   $$ |2x + 3y - 8| = |2x - 2 + 3y - 6| = |2(x-1) + 3(y-2)| $$

   En utilisant l'inégalité triangulaire $|a+b| \leq |a| + |b|$ :
   $$ |2(x-1) + 3(y-2)| \leq |2(x-1)| + |3(y-2)| = 2|x-1| + 3|y-2| $$

   Or, nous savons que $|x-1| = \sqrt{(x-1)^2} \leq \sqrt{(x-1)^2 + (y-2)^2}$.
   De même, $|y-2| = \sqrt{(y-2)^2} \leq \sqrt{(x-1)^2 + (y-2)^2}$.

   Soit $d = \sqrt{(x-1)^2 + (y-2)^2}$ la distance au point $(1,2)$. L'inégalité devient :
   $$ |2x + 3y - 8| \leq 2d + 3d = 5d $$

   Nous voulons que cette quantité soit strictement inférieure à $\varepsilon$ ($5d < \varepsilon$).
   Cela nous indique qu'il suffit de choisir $d < \varepsilon/5$.
   La relation de dépendance est trouvée : $\delta = \frac{\varepsilon}{5}$.

3. **Rédaction de la preuve formelle** :
   Soit $\varepsilon > 0$ un réel arbitraire.
   Posons $\delta = \frac{\varepsilon}{5}$. (Il est clair que $\delta > 0$).

   Soit $(x,y) \in \mathbb{R}^2$ tel que $0 < \|(x,y) - (1,2)\| < \delta$, c'est-à-dire :
   $$ \sqrt{(x-1)^2 + (y-2)^2} < \frac{\varepsilon}{5} $$

   Évaluons la distance entre $f(x,y)$ et la limite $L=8$ :
   $$ |(2x + 3y) - 8| = |2x - 2 + 3y - 6| = |2(x-1) + 3(y-2)| $$

   Par l'inégalité triangulaire :
   $$ \dots \leq 2|x-1| + 3|y-2| $$

   Puisque la valeur absolue d'un terme est inférieure à la norme euclidienne totale du vecteur :
   $$ \dots \leq 2\sqrt{(x-1)^2 + (y-2)^2} + 3\sqrt{(x-1)^2 + (y-2)^2} $$
   $$ \dots = 5\sqrt{(x-1)^2 + (y-2)^2} $$

   Par hypothèse sur $(x,y)$, la racine carrée est majorée par $\delta = \varepsilon/5$ :
   $$ \dots < 5 \times \frac{\varepsilon}{5} = \varepsilon $$

   **Conclusion finale :**
   Nous avons montré que :
   $\forall \varepsilon > 0, \exists \delta = \frac{\varepsilon}{5} > 0, \|(x,y) - (1,2)\| < \delta \implies |(2x + 3y) - 8| < \varepsilon$.
   La définition de la limite est rigoureusement satisfaite, donc $\lim_{(x,y) \to (1,2)} (2x + 3y) = 8$.
