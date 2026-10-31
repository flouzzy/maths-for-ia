# Exercice 1 : Calcul de coefficients dans une base orthonormée $\bigstar\star\star\star\star$

**Énoncé :**
Dans $\mathbb{R}^3$ muni du produit scalaire canonique, on considère la famille de vecteurs $e_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right)$, $e_2 = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0\right)$ et $e_3 = (0, 0, 1)$.
1. Montrer que $\mathcal{B} = (e_1, e_2, e_3)$ est une base orthonormée de $\mathbb{R}^3$.
2. Calculer les coefficients de Fourier du vecteur $x = (2, 4, 3)$ dans cette base.
3. Vérifier l'identité de Parseval pour le vecteur $x$.

**Correction détaillée :**
1. On calcule les normes :
   $\|e_1\|^2 = \left(\frac{1}{\sqrt{2}}\right)^2 + \left(\frac{1}{\sqrt{2}}\right)^2 + 0 = \frac{1}{2} + \frac{1}{2} = 1$.
   $\|e_2\|^2 = \left(\frac{1}{\sqrt{2}}\right)^2 + \left(-\frac{1}{\sqrt{2}}\right)^2 + 0 = 1$.
   $\|e_3\|^2 = 0 + 0 + 1 = 1$.
   On calcule les produits scalaires croisés :
   $\langle e_1, e_2 \rangle = \frac{1}{2} - \frac{1}{2} + 0 = 0$.
   $\langle e_1, e_3 \rangle = 0 + 0 + 0 = 0$.
   $\langle e_2, e_3 \rangle = 0 + 0 + 0 = 0$.
   La famille $(e_1, e_2, e_3)$ est donc orthonormée. Étant composée de 3 vecteurs dans $\mathbb{R}^3$ dimension 3, c'est une base orthonormée.

2. Les coefficients de Fourier sont donnés par $c_i = \langle x, e_i \rangle$ :
   $c_1 = \langle (2, 4, 3), \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right) \rangle = \frac{2}{\sqrt{2}} + \frac{4}{\sqrt{2}} + 0 = \frac{6}{\sqrt{2}} = 3\sqrt{2}$.
   $c_2 = \langle (2, 4, 3), \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0\right) \rangle = \frac{2}{\sqrt{2}} - \frac{4}{\sqrt{2}} + 0 = -\frac{2}{\sqrt{2}} = -\sqrt{2}$.
   $c_3 = \langle (2, 4, 3), (0, 0, 1) \rangle = 0 + 0 + 3 = 3$.
   Ainsi, $x = 3\sqrt{2} e_1 - \sqrt{2} e_2 + 3 e_3$.

3. La norme au carré de $x$ dans la base canonique est :
   $\|x\|^2 = 2^2 + 4^2 + 3^2 = 4 + 16 + 9 = 29$.
   D'après l'identité de Parseval, on doit avoir $\|x\|^2 = c_1^2 + c_2^2 + c_3^2$.
   Calculons la somme des carrés des coefficients :
   $c_1^2 + c_2^2 + c_3^2 = (3\sqrt{2})^2 + (-\sqrt{2})^2 + 3^2 = 18 + 2 + 9 = 29$.
   L'identité de Parseval est bien vérifiée.
