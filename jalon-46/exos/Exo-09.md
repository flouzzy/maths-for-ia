# Exercice 9 : Backpropagation manuelle sur un perceptron simple $\quad \bigstar\bigstar\bigstar\bigstar\star$
## Énoncé
Considérons une fonction $L(w) = \frac{1}{2} ( \sigma(wx) - y )^2$ où $x, y, w \in \mathbb{R}$ et $\sigma$ est la fonction sigmoïde.
Exprimer le gradient $\frac{\partial L}{\partial w}$ à l'aide de la Règle de la Chaîne.
## Correction Détaillée
Décomposons la fonction d'erreur $L(w)$ en une suite d'opérations élémentaires :
1. $z = wx$ (transformation affine)
2. $a = \sigma(z)$ (activation)
3. $L = \frac{1}{2} (a - y)^2$ (coût)

Appliquons la règle de la chaîne en remontant de la sortie vers l'entrée (Backpropagation) :
$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w} $$
Calculons chaque dérivée locale :
- $\frac{\partial L}{\partial a} = a - y$
- $\frac{\partial a}{\partial z} = \sigma'(z) = \sigma(z)(1 - \sigma(z))$ (propriété classique de la sigmoïde)
- $\frac{\partial z}{\partial w} = x$

En multipliant le tout :
$$ \frac{\partial L}{\partial w} = (a - y) \cdot \sigma'(wx) \cdot x = (\sigma(wx) - y) \sigma(wx)(1 - \sigma(wx)) x $$
Ceci est la formule d'apprentissage exacte pour mettre à jour le poids $w$ via descente de gradient.
$\blacksquare$
