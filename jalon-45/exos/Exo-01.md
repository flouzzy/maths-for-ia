---
title: "Exercice 1 : Différentiabilité et Gradient"
difficulty: "★☆☆☆☆"
---

# Exercice 1 : Calcul de dérivées partielles élémentaires

**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit $f : \mathbb{R}^2 \to \mathbb{R}$ définie par $f(x, y) = 3x^2y - 5xy^3 + e^{2x}\cos(y)$. Calculer le gradient de $f$ en tout point $(x, y) \in \mathbb{R}^2$.

---
## Correction Détaillée

La fonction $f$ est une somme et un produit de fonctions usuelles différentiables sur $\mathbb{R}^2$, elle est donc différentiable sur $\mathbb{R}^2$.
Nous allons calculer ses dérivées partielles par rapport à $x$ et par rapport à $y$.

**1. Calcul de la dérivée partielle par rapport à $x$ :**
En fixant $y$ constant, on dérive par rapport à $x$ :
$$ \frac{\partial f}{\partial x}(x, y) = \frac{\partial}{\partial x} (3x^2y - 5xy^3 + e^{2x}\cos(y)) $$
$$ \frac{\partial f}{\partial x}(x, y) = 3y \cdot (2x) - 5y^3 \cdot (1) + \cos(y) \cdot (2e^{2x}) $$
$$ \frac{\partial f}{\partial x}(x, y) = 6xy - 5y^3 + 2e^{2x}\cos(y) $$

**2. Calcul de la dérivée partielle par rapport à $y$ :**
En fixant $x$ constant, on dérive par rapport à $y$ :
$$ \frac{\partial f}{\partial y}(x, y) = \frac{\partial}{\partial y} (3x^2y - 5xy^3 + e^{2x}\cos(y)) $$
$$ \frac{\partial f}{\partial y}(x, y) = 3x^2 \cdot (1) - 5x \cdot (3y^2) + e^{2x} \cdot (-\sin(y)) $$
$$ \frac{\partial f}{\partial y}(x, y) = 3x^2 - 15xy^2 - e^{2x}\sin(y) $$

**3. Expression du gradient :**
Le gradient de $f$ en $(x, y)$ est le vecteur colonne dont les composantes sont les dérivées partielles :
$$ \nabla f(x, y) = \begin{pmatrix} \frac{\partial f}{\partial x}(x, y) \\ \frac{\partial f}{\partial y}(x, y) \end{pmatrix} = \begin{pmatrix} 6xy - 5y^3 + 2e^{2x}\cos(y) \\ 3x^2 - 15xy^2 - e^{2x}\sin(y) \end{pmatrix} $$
