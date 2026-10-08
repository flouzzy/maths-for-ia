## Loi de la distance minimale au centre \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Un tireur à l'arc lance une flèche sur une cible circulaire de rayon $R$. On suppose que le point d'impact suit une loi uniforme sur l'aire de la cible.
Soit $D$ la variable aléatoire représentant la distance entre le point d'impact et le centre de la cible.
Déterminer la fonction de répartition puis la densité de probabilité de la variable $D$.

**Correction Explicative :**
1. Modélisation géométrique : Soit $\Omega$ le disque de centre $(0,0)$ et de rayon $R$ dans le plan $\mathbb{R}^2$.
   L'aire totale de la cible est $Area(\Omega) = \pi R^2$.
   Le tir étant uniforme, la probabilité que le point d'impact $(X, Y)$ tombe dans une région mesurable $A \subset \Omega$ est proportionnelle à l'aire de cette région. La mesure de probabilité géométrique est définie par :
   $$\mathbb{P}((X, Y) \in A) = \frac{Area(A)}{Area(\Omega)} = \frac{Area(A)}{\pi R^2}$$
2. Définition de la variable aléatoire : La distance au centre est donnée par $D = \sqrt{X^2 + Y^2}$. Le support de la variable aléatoire $D$ est l'intervalle $[0, R]$, puisqu'aucune flèche ne frappe en dehors de la cible.
3. Calculons la fonction de répartition $F_D(x) = \mathbb{P}(D \leq x)$ :
   - Si $x < 0$, la distance ne peut être négative, l'événement est impossible, donc $F_D(x) = 0$.
   - Si $x > R$, la flèche tombe toujours à une distance inférieure à $R$, l'événement est certain, donc $F_D(x) = 1$.
   - Considérons le cas intéressant où $0 \leq x \leq R$.
     L'événement $\{D \leq x\}$ signifie que le point d'impact se trouve dans un disque concentrique de rayon $x$.
     L'aire de cet événement, noté $Disque(0, x)$, est $\pi x^2$.
     En appliquant la loi géométrique uniforme :
     $$F_D(x) = \mathbb{P}(D \leq x) = \frac{Area(Disque(0, x))}{Area(\Omega)} = \frac{\pi x^2}{\pi R^2} = \frac{x^2}{R^2}$$
4. Synthèse de la fonction de répartition :
   $$F_D(x) = \begin{cases}
   0 & \text{si } x < 0 \\
   \left(\frac{x}{R}\right)^2 & \text{si } 0 \leq x \leq R \\
   1 & \text{si } x > R
   \end{cases}$$
   Nous constatons que la fonction $F_D$ est continue sur tout $\mathbb{R}$ et dérivable sur $\mathbb{R}$ sauf éventuellement en $0$ et en $R$.
5. Calculons la densité de probabilité $f_D(x)$ par dérivation de la fonction de répartition :
   - Pour $x < 0$ et $x > R$, la dérivée est nulle.
   - Pour $x \in ]0, R[$, nous dérivons $F_D(x) = \frac{x^2}{R^2}$ par rapport à $x$ :
     $$f_D(x) = \frac{d}{dx} \left( \frac{x^2}{R^2} \right) = \frac{2x}{R^2}$$
6. Conclusion : La densité de probabilité de la distance $D$ est donnée par :
   $$f_D(x) = \frac{2x}{R^2} \mathbf{1}_{[0, R]}(x)$$
   On observe une propriété fascinante : la densité n'est pas constante. Elle est nulle au centre ($x=0$) et maximale sur le bord de la cible ($x=R$). Il est géométriquement beaucoup plus probable de tomber loin du centre car l'aire de la couronne circulaire "extérieure" est infiniment plus grande que l'aire près du centre.
