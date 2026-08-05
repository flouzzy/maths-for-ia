# Exercice 5 : Équation aux dérivées partielles via Chain Rule $\quad \bigstar\bigstar\star\star\star$
## Énoncé
Soit $F : \mathbb{R}^2 \to \mathbb{R}$ une fonction différentiable. On pose $f(r, \theta) = F(r \cos \theta, r \sin \theta)$.
Montrer l'identité :
$$ \|\nabla F(x,y)\|^2 = \left( \frac{\partial f}{\partial r} \right)^2 + \frac{1}{r^2} \left( \frac{\partial f}{\partial \theta} \right)^2 $$
## Correction Détaillée
Posons $x(r,\theta) = r\cos\theta$ et $y(r,\theta) = r\sin\theta$.
Par la règle de la chaîne :
$$ \frac{\partial f}{\partial r} = \frac{\partial F}{\partial x} \frac{\partial x}{\partial r} + \frac{\partial F}{\partial y} \frac{\partial y}{\partial r} = \frac{\partial F}{\partial x} \cos\theta + \frac{\partial F}{\partial y} \sin\theta $$
$$ \frac{\partial f}{\partial \theta} = \frac{\partial F}{\partial x} \frac{\partial x}{\partial \theta} + \frac{\partial F}{\partial y} \frac{\partial y}{\partial \theta} = \frac{\partial F}{\partial x} (-r\sin\theta) + \frac{\partial F}{\partial y} (r\cos\theta) $$
Évaluons le membre de droite :
$\left( \frac{\partial f}{\partial r} \right)^2 = \left(\frac{\partial F}{\partial x}\right)^2 \cos^2\theta + \left(\frac{\partial F}{\partial y}\right)^2 \sin^2\theta + 2\frac{\partial F}{\partial x}\frac{\partial F}{\partial y}\sin\theta\cos\theta$
$\frac{1}{r^2}\left( \frac{\partial f}{\partial \theta} \right)^2 = \left(-\frac{\partial F}{\partial x}\sin\theta + \frac{\partial F}{\partial y}\cos\theta\right)^2 = \left(\frac{\partial F}{\partial x}\right)^2 \sin^2\theta + \left(\frac{\partial F}{\partial y}\right)^2 \cos^2\theta - 2\frac{\partial F}{\partial x}\frac{\partial F}{\partial y}\sin\theta\cos\theta$
En sommant les deux expressions, les termes croisés s'annulent :
$$ \left( \frac{\partial f}{\partial r} \right)^2 + \frac{1}{r^2} \left( \frac{\partial f}{\partial \theta} \right)^2 = \left(\frac{\partial F}{\partial x}\right)^2(\cos^2\theta + \sin^2\theta) + \left(\frac{\partial F}{\partial y}\right)^2(\sin^2\theta + \cos^2\theta) $$
$$ = \left(\frac{\partial F}{\partial x}\right)^2 + \left(\frac{\partial F}{\partial y}\right)^2 = \|\nabla F(x,y)\|^2 $$
L'identité est démontrée.
$\blacksquare$
