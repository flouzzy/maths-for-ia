---
uuid: jalon-48-exo-09
title: "Exercice 9 : Calculs analytiques du Gradient (Variation 9)"
---
# Exercice 9 : Matrices Jacobiennes et Backpropagation - Cas 9 $\bigstar$$\star$$\star$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{10} \cdot \sigma(w_{9} x + b_{9}) + b_{10}) $$
avec $x, w_{9}, w_{10}, b_{9}, b_{10} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{9}$, notée $\frac{{\partial f}}{{\partial w_{9}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{9} x + b_{9}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{10} a_1 + b_{10}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{9}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{9}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{9}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{10}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{9}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{9}}} = \sigma'(z_2) \cdot w_{10} \cdot \sigma'(z_1) \cdot x $$
