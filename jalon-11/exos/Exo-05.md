# Exercice 5: Équation d'un hyperplan en dimension n
## Énoncé
Soit $E$ un espace vectoriel de dimension $n \ge 2$. Soient $H_1$ et $H_2$ deux hyperplans de $E$.
Montrer que si $H_1 \neq H_2$, alors $\dim(H_1 \cap H_2) = n - 2$.


## Correction détaillée
1. **Caractérisation par une forme linéaire :** Par définition, un hyperplan $H$ est le noyau d'une forme linéaire non nulle, notons-la $\phi : E \to \mathbb{K}$.
   $$H = \{ x \in E \mid \phi(x) = 0 \}$$
2. **Décomposition dans la base :** Soit un vecteur quelconque $x \in E$. Il admet une unique décomposition dans la base $(e_1, \dots, e_n)$ :
   $$x = \sum_{i=1}^n x_i e_i$$
   où les $x_i$ sont les coordonnées de $x$.
3. **Application de la linéarité :** Appliquons $\phi$ au vecteur $x$ :
   $$\phi(x) = \phi\left(\sum_{i=1}^n x_i e_i\right)$$
   Par linéarité de $\phi$, la somme et les scalaires sortent :
   $$\phi(x) = \sum_{i=1}^n x_i \phi(e_i)$$
4. **Identification des coefficients :** Posons pour tout $i \in \{1, \dots, n\}$, $a_i = \phi(e_i)$. L'équation d'appartenance à $H$ devient alors :
   $$\sum_{i=1}^n a_i x_i = 0$$
5. **Non-nullité des coefficients :** Comme $\phi$ est une forme linéaire non nulle, il existe au moins un vecteur de base $e_{i_0}$ tel que $\phi(e_{i_0}) \neq 0$. Donc, il existe au moins un $a_i$ tel que $a_i \neq 0$.
6. **Conclusion :** Tout hyperplan est rigoureusement caractérisé par une équation linéaire homogène dont les coefficients ne sont pas tous nuls.

$\blacksquare$
