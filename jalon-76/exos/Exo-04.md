## Exercice 4 : Projection orthogonale sur la fonction constante \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Dans $L^2([0,1])$, déterminer la projection orthogonale de la fonction $f(x) = e^x$ sur le sous-espace $M$ engendré par la fonction constante $\mathbf{1}$ (où $\mathbf{1}(x) = 1$).

**Correction Détaillée :**
1. **Analyse de l'énoncé :** $M = \text{Vect}(\mathbf{1})$. La projection orthogonale $p$ de $f$ sur $M$ est de la forme $p = \alpha \mathbf{1}$ où $\alpha \in \mathbb{R}$. Elle est caractérisée par $(f - p) \perp \mathbf{1}$.
2. **Écriture de l'orthogonalité :**
   $$ \langle f - \alpha \mathbf{1}, \mathbf{1} \rangle = 0 \iff \langle f, \mathbf{1} \rangle - \alpha \langle \mathbf{1}, \mathbf{1} \rangle = 0 $$
3. **Calcul des produits scalaires :**
   $$ \langle \mathbf{1}, \mathbf{1} \rangle = \int_0^1 1 \cdot 1 dx = 1 $$
   $$ \langle f, \mathbf{1} \rangle = \int_0^1 e^x \cdot 1 dx = \left[ e^x \right]_0^1 = e - 1 $$
4. **Déduction de la projection :**
   $$ \alpha \cdot 1 = e - 1 \implies \alpha = e - 1 $$
   La projection orthogonale de $e^x$ sur les fonctions constantes est la fonction constante $p(x) = e - 1$. C'est en fait la valeur moyenne de $f$ sur l'intervalle.
