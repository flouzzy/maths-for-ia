---
title: "Exercice 2 : Différentiabilité et Gradient"
difficulty: "★★☆☆☆"
---

# Exercice 2 : Dérivée directionnelle et plus forte pente

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

On considère la surface définie par $f(x, y) = 4 - x^2 - 2y^2$. Calculer la dérivée directionnelle de $f$ au point $A(1, 1)$ dans la direction du vecteur $v = (1, \sqrt{3})^T$. Déterminer la direction de la plus forte pente au point $A$.

---
## Correction Détaillée

**1. Calcul du gradient au point $A$ :**
La fonction est polynomiale donc différentiable. Ses dérivées partielles sont :
$$ \frac{\partial f}{\partial x}(x, y) = -2x \quad \text{et} \quad \frac{\partial f}{\partial y}(x, y) = -4y $$
Au point $A(1, 1)$, le gradient est :
$$ \nabla f(1, 1) = \begin{pmatrix} -2(1) \\ -4(1) \end{pmatrix} = \begin{pmatrix} -2 \\ -4 \end{pmatrix} $$

**2. Calcul de la dérivée directionnelle dans la direction $v$ :**
Le vecteur $v = (1, \sqrt{3})^T$ a pour norme euclidienne $\|v\| = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = \sqrt{4} = 2$.
Le vecteur unitaire définissant la direction est $u = \frac{v}{\|v\|} = \left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)^T$.
La fonction $f$ étant différentiable, la dérivée directionnelle dans la direction $u$ est donnée par le produit scalaire :
$$ D_u f(1, 1) = \langle \nabla f(1, 1), u \rangle = (-2) \cdot \frac{1}{2} + (-4) \cdot \frac{\sqrt{3}}{2} $$
$$ D_u f(1, 1) = -1 - 2\sqrt{3} $$
La valeur est négative, indiquant que la fonction décroît dans cette direction.

**3. Direction de la plus forte pente :**
La direction de la plus forte pente (croissance maximale) est donnée par la direction du gradient $\nabla f(1, 1)$.
Le vecteur unitaire correspondant est :
$$ u_{\text{max}} = \frac{\nabla f(1, 1)}{\|\nabla f(1, 1)\|} = \frac{1}{\sqrt{(-2)^2 + (-4)^2}} \begin{pmatrix} -2 \\ -4 \end{pmatrix} = \frac{1}{\sqrt{20}} \begin{pmatrix} -2 \\ -4 \end{pmatrix} = \frac{1}{2\sqrt{5}} \begin{pmatrix} -2 \\ -4 \end{pmatrix} = \begin{pmatrix} -\frac{1}{\sqrt{5}} \\ -\frac{2}{\sqrt{5}} \end{pmatrix} $$
