# Hessienne de l'entropie croisée dans la régression logistique

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
En régression logistique, pour une étiquette binaire $y \in \{0,1\}$ et une probabilité prédite $p = \sigma(w^T x)$, où $\sigma(z) = 1/(1+e^{-z})$, la fonction de perte est la log-loss :
$$L(w) = -y \log(p) - (1-y)\log(1-p)$$
1. Montrez que la dérivée du sigmoïde est $\sigma'(z) = \sigma(z)(1-\sigma(z))$.
2. Calculez $\nabla L(w)$ en fonction de $x, y$ et $p$.
3. Montrez que la Hessienne $H_L(w)$ est semi-définie positive.

**Correction mathématique détaillée :**

1. **Dérivée du sigmoïde :**
   $$\sigma(z) = (1+e^{-z})^{-1} \implies \sigma'(z) = -(1+e^{-z})^{-2}(-e^{-z}) = \frac{e^{-z}}{(1+e^{-z})^2}$$
   Or $\frac{e^{-z}}{1+e^{-z}} = 1 - \frac{1}{1+e^{-z}} = 1 - \sigma(z)$.
   Donc $\sigma'(z) = \sigma(z)(1-\sigma(z))$.

2. **Calcul du gradient :**
   $p(w) = \sigma(w^T x)$. Le gradient par rapport à $w$ est $\nabla p(w) = \sigma'(w^T x) x = p(1-p)x$.
   Par dérivation en chaîne sur la perte :
   $$\nabla L(w) = -y \frac{1}{p} \nabla p - (1-y) \frac{1}{1-p}(-\nabla p)$$
   $$\nabla L(w) = \left( - \frac{y}{p} + \frac{1-y}{1-p} \right) p(1-p) x = \left(-y(1-p) + (1-y)p\right) x = (p - y) x$$

3. **Calcul de la Hessienne :**
   Il faut dériver le gradient $(p - y)x$. Le seul terme dépendant de $w$ est $p = \sigma(w^T x)$.
   La jacobienne du gradient scalaire $(p-y)$ est sa dérivée transposée : $(\nabla p)^T = (p(1-p)x)^T = p(1-p)x^T$.
   Ainsi, en utilisant le fait que pour une fonction $g(w)$ et une constante matricielle $A$, le jacobien de $g(w)A$ est $A (\nabla g)^T$ :
   $$H_L(w) = x (\nabla p)^T = x (p(1-p)x)^T = p(1-p) x x^T$$

4. **Analyse de la positivité :**
   Pour tout vecteur $v$, $v^T H_L(w) v = p(1-p) v^T (x x^T) v = p(1-p) (v^T x)^2$.
   Puisque $0 < p < 1$, $p(1-p) > 0$. Le carré $(v^T x)^2 \geq 0$.
   Donc $v^T H_L(w) v \geq 0$. La Hessienne est semi-définie positive, ce qui garantit que le problème de la régression logistique est convexe et ne possède aucun minimum local parasite.
