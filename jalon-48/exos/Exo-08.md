---
uuid: jalon-48-exo-08
title: "Exercice 8 : Calculs analytiques du Gradient (Variation 8)"
---
# Exercice 8 : Matrices Jacobiennes et Backpropagation - Cas 8 $\bigstar$$\bigstar$$\bigstar$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{9} \cdot \sigma(w_{8} x + b_{8}) + b_{9}) $$
avec $x, w_{8}, w_{9}, b_{8}, b_{9} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{8}$, notée $\frac{{\partial f}}{{\partial w_{8}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{8} x + b_{8}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{9} a_1 + b_{9}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{8}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{8}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{8}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{9}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{8}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{8}}} = \sigma'(z_2) \cdot w_{9} \cdot \sigma'(z_1) \cdot x $$
