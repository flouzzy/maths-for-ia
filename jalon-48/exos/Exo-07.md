---
uuid: jalon-48-exo-07
title: "Exercice 7 : Calculs analytiques du Gradient (Variation 7)"
---
# Exercice 7 : Matrices Jacobiennes et Backpropagation - Cas 7 $\bigstar$$\bigstar$$\star$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{8} \cdot \sigma(w_{7} x + b_{7}) + b_{8}) $$
avec $x, w_{7}, w_{8}, b_{7}, b_{8} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{7}$, notée $\frac{{\partial f}}{{\partial w_{7}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{7} x + b_{7}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{8} a_1 + b_{8}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{7}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{7}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{7}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{8}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{7}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{7}}} = \sigma'(z_2) \cdot w_{8} \cdot \sigma'(z_1) \cdot x $$
