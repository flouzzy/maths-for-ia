---
uuid: jalon-48-exo-03
title: "Exercice 3 : Calculs analytiques du Gradient (Variation 3)"
---
# Exercice 3 : Matrices Jacobiennes et Backpropagation - Cas 3 $\bigstar$$\star$$\star$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{4} \cdot \sigma(w_{3} x + b_{3}) + b_{4}) $$
avec $x, w_{3}, w_{4}, b_{3}, b_{4} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{3}$, notée $\frac{{\partial f}}{{\partial w_{3}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{3} x + b_{3}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{4} a_1 + b_{4}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{3}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{3}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{3}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{4}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{3}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{3}}} = \sigma'(z_2) \cdot w_{4} \cdot \sigma'(z_1) \cdot x $$
