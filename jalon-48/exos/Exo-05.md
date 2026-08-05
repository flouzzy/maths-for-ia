---
uuid: jalon-48-exo-05
title: "Exercice 5 : Calculs analytiques du Gradient (Variation 5)"
---
# Exercice 5 : Matrices Jacobiennes et Backpropagation - Cas 5 $\bigstar$$\bigstar$$\bigstar$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{6} \cdot \sigma(w_{5} x + b_{5}) + b_{6}) $$
avec $x, w_{5}, w_{6}, b_{5}, b_{6} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{5}$, notée $\frac{{\partial f}}{{\partial w_{5}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{5} x + b_{5}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{6} a_1 + b_{6}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{5}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{5}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{5}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{6}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{5}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{5}}} = \sigma'(z_2) \cdot w_{6} \cdot \sigma'(z_1) \cdot x $$
