# Hessienne de la norme euclidienne lissée

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f : \mathbb{R}^n \to \mathbb{R}$ définie par $f(x) = \sqrt{\|x\|^2 + \epsilon^2}$, où $\epsilon > 0$. C'est une approximation différentiable de la norme euclidienne.
Montrez que le gradient et la Hessienne s'expriment vectoriellement.
Calculez $H_f(x)$.

**Correction mathématique détaillée :**

1. **Gradient :**
   Notons $g(x) = \|x\|^2 + \epsilon^2 = \sum_{i=1}^n x_i^2 + \epsilon^2$. Alors $f(x) = g(x)^{1/2}$.
   Par différentiation en chaîne : $\frac{\partial f}{\partial x_k} = \frac{1}{2} g(x)^{-1/2} \frac{\partial g}{\partial x_k} = \frac{x_k}{\sqrt{\|x\|^2 + \epsilon^2}}$.
   Vectoriellement, $\nabla f(x) = \frac{x}{f(x)}$.

2. **Matrice Hessienne :**
   On dérive la fraction $\frac{x_k}{f(x)}$ par rapport à $x_j$ (quotient) :
   $$\frac{\partial^2 f}{\partial x_j \partial x_k} = \frac{\frac{\partial x_k}{\partial x_j} f(x) - x_k \frac{\partial f}{\partial x_j}}{(f(x))^2}$$
   Où $\frac{\partial x_k}{\partial x_j} = \delta_{kj}$ (symbole de Kronecker, valant 1 si $k=j$, 0 sinon).
   On sait que $\frac{\partial f}{\partial x_j} = \frac{x_j}{f(x)}$. En remplaçant :
   $$\frac{\partial^2 f}{\partial x_j \partial x_k} = \frac{\delta_{kj} f(x) - x_k \frac{x_j}{f(x)}}{f(x)^2} = \frac{\delta_{kj}}{f(x)} - \frac{x_k x_j}{f(x)^3}$$

3. **Écriture matricielle :**
   Le terme $\delta_{kj}$ correspond à la matrice identité $I_n$. Le terme $x_k x_j$ correspond à la matrice de rang 1 $x x^T$.
   Ainsi,
   $$H_f(x) = \frac{1}{f(x)} I_n - \frac{1}{f(x)^3} x x^T$$
   Cette matrice possède des valeurs propres toutes strictement positives car $I_n - \frac{xx^T}{f(x)^2}$ est définie positive (la norme spectrale de $xx^T / (\|x\|^2+\epsilon^2)$ est strictement inférieure à 1).
