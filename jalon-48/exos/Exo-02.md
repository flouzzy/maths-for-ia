---
uuid: jalon-48-exo-02
title: "Exercice 2 : Calculs analytiques du Gradient (Variation 2)"
---
# Exercice 2 : Matrices Jacobiennes et Backpropagation - Cas 2 $\bigstar$$\bigstar$$\bigstar$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{3} \cdot \sigma(w_{2} x + b_{2}) + b_{3}) $$
avec $x, w_{2}, w_{3}, b_{2}, b_{3} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{2}$, notée $\frac{{\partial f}}{{\partial w_{2}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{2} x + b_{2}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{3} a_1 + b_{3}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{2}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{2}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{2}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{3}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{2}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{2}}} = \sigma'(z_2) \cdot w_{3} \cdot \sigma'(z_1) \cdot x $$
