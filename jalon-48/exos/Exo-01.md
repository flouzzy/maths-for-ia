---
uuid: jalon-48-exo-01
title: "Exercice 1 : Calculs analytiques du Gradient (Variation 1)"
---
# Exercice 1 : Matrices Jacobiennes et Backpropagation - Cas 1 $\bigstar$$\bigstar$$\star$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{2} \cdot \sigma(w_{1} x + b_{1}) + b_{2}) $$
avec $x, w_{1}, w_{2}, b_{1}, b_{2} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{1}$, notée $\frac{{\partial f}}{{\partial w_{1}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{1} x + b_{1}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{2} a_1 + b_{2}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{1}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{1}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{1}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{2}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{1}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{1}}} = \sigma'(z_2) \cdot w_{2} \cdot \sigma'(z_1) \cdot x $$
