# Exercice 2: Noyau d'une forme linéaire
## Énoncé
Soit $\phi : \mathbb{R}^3 \to \mathbb{R}$ définie par $\phi(x, y, z) = 2x - y + 3z$. Déterminer une base de $\ker \phi$.

## Correction détaillée
1. **Définition du noyau :** Le noyau de $\phi$ est l'ensemble des vecteurs sur lesquels la forme linéaire s'annule.
   $$\ker \phi = \{ (x,y,z) \in \mathbb{R}^3 \mid 2x - y + 3z = 0 \}$$
2. **Résolution de l'équation cartésienne :** L'équation $2x - y + 3z = 0$ équivaut à exprimer une variable en fonction des autres. Isolons $y$ :
   $$y = 2x + 3z$$
3. **Paramétrisation des vecteurs du noyau :** Un vecteur $v \in \ker \phi$ s'écrit donc :
   $$v = (x, 2x+3z, z)$$
4. **Décomposition en combinaison linéaire :** On sépare les paramètres libres $x$ et $z$ :
   $$v = (x, 2x, 0) + (0, 3z, z) = x(1, 2, 0) + z(0, 3, 1)$$
5. **Famille génératrice :** Les vecteurs $u_1 = (1, 2, 0)$ et $u_2 = (0, 3, 1)$ engendrent donc $\ker \phi$.
6. **Indépendance linéaire :** Supposons $\lambda u_1 + \mu u_2 = 0$.
   $$\lambda(1, 2, 0) + \mu(0, 3, 1) = (\lambda, 2\lambda+3\mu, \mu) = (0, 0, 0)$$
   On obtient immédiatement $\lambda = 0$ et $\mu = 0$. La famille $(u_1, u_2)$ est libre.
7. **Conclusion :** La famille $((1,2,0), (0,3,1))$ est une base de $\ker \phi$, qui est bien un hyperplan (dimension $3 - 1 = 2$).
