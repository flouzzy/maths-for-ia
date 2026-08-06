---
uuid: jalon-48-exo-10
title: "Exercice 10 : Calculs analytiques du Gradient (Variation 10)"
---
# Exercice 10 : Matrices Jacobiennes et Backpropagation - Cas 10 $\bigstar$$\bigstar$$\star$$\star$$\star$

**Énoncé :**
Considérons une variante du perceptron simple défini par la fonction scalaire :
$$ f(x) = \sigma(w_{11} \cdot \sigma(w_{10} x + b_{10}) + b_{11}) $$
avec $x, w_{10}, w_{11}, b_{10}, b_{11} \in \mathbb{R}$.
Calculer analytiquement la dérivée partielle de $f$ par rapport à $w_{10}$, notée $\frac{{\partial f}}{{\partial w_{10}}}$, en appliquant de manière rigoureuse le théorème de dérivation des fonctions composées.

**Correction Détaillée :**
1. Posons les variables intermédiaires pour décomposer le graphe de calcul :
   $z_1 = w_{10} x + b_{10}$
   $a_1 = \sigma(z_1)$
   $z_2 = w_{11} a_1 + b_{11}$
   $f = \sigma(z_2)$

2. Nous cherchons à évaluer $\frac{{\partial f}}{{\partial w_{10}}}$. Selon la règle de composition (Chain Rule) :
   $$ \frac{{\partial f}}{{\partial w_{10}}} = \frac{{\partial f}}{{\partial z_2}} \cdot \frac{{\partial z_2}}{{\partial a_1}} \cdot \frac{{\partial a_1}}{{\partial z_1}} \cdot \frac{{\partial z_1}}{{\partial w_{10}}} $$

3. Évaluons chaque terme séparément :
   - $\frac{{\partial f}}{{\partial z_2}} = \sigma'(z_2)$
   - $\frac{{\partial z_2}}{{\partial a_1}} = w_{11}$
   - $\frac{{\partial a_1}}{{\partial z_1}} = \sigma'(z_1)$
   - $\frac{{\partial z_1}}{{\partial w_{10}}} = x$

4. Par multiplication, le résultat final rigoureux sans aucune ellipse est :
   $$ \frac{{\partial f}}{{\partial w_{10}}} = \sigma'(z_2) \cdot w_{11} \cdot \sigma'(z_1) \cdot x $$
