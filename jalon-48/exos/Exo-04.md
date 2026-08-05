---
uuid: jalon-48-exo-04
title: "Exercice 4 : Calculs analytiques du Gradient (Variation 4)"
---
# Exercice 4 : Matrices Jacobiennes et Backpropagation - Cas 4 $\bigstar$$\bigstar$$\star$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{5} \cdot \sigma(w_{4} x + b_{4}) + b_{5}) $$
avec $x, w_{4}, w_{5}, b_{4}, b_{5} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{4}$, notée $\frac{{\partial f}}{{\partial w_{4}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{4} x + b_{4}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{5} a_1 + b_{5}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{4}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{4}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{4}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{5}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{4}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{4}}} = \sigma'(z_2) \cdot w_{5} \cdot \sigma'(z_1) \cdot x $$
