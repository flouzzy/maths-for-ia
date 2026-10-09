# Exercice 4

## Exercice 4 : Somme de deux variables aléatoires $\bigstar\bigstar\star\star\star$

Soient $X$ et $Y$ deux variables aléatoires sur l'espace mesurable $(\Omega, \mathcal{F})$.
Montrer que pour tout réel $a$, l'ensemble $\{ \omega \in \Omega \mid X(\omega) + Y(\omega) < a \}$ appartient à la tribu $\mathcal{F}$.
*Indication : Utiliser la densité de $\mathbb{Q}$ dans $\mathbb{R}$.*

### Correction pas à pas

1. **Réécriture de l'inégalité**
   L'événement s'écrit $A = \{ \omega \in \Omega \mid X(\omega) + Y(\omega) < a \}$.
   On peut le réécrire en séparant $X$ et $Y$ :
   $A = \{ \omega \in \Omega \mid X(\omega) < a - Y(\omega) \}$.

2. **Utilisation de la densité des rationnels**
   Si deux nombres réels vérifient $x < y$, la densité de $\mathbb{Q}$ dans $\mathbb{R}$ assure qu'il existe un nombre rationnel $q \in \mathbb{Q}$ tel que $x < q < y$.
   Ici, l'inégalité $X(\omega) < a - Y(\omega)$ implique l'existence d'un $q \in \mathbb{Q}$ tel que :
   $X(\omega) < q < a - Y(\omega)$.
   Ce qui se sépare en deux conditions simultanées :
   $X(\omega) < q$ ET $Y(\omega) < a - q$.

3. **Traduction ensembliste**
   L'ensemble $A$ peut donc s'écrire comme une union dénombrable (puisque $\mathbb{Q}$ est dénombrable) sur tous les rationnels $q$ :
   $A = \bigcup_{q \in \mathbb{Q}} \left( \{ \omega \mid X(\omega) < q \} \cap \{ \omega \mid Y(\omega) < a - q \} \right)$.

4. **Mesurabilité**
   Puisque $X$ est une variable aléatoire, l'ensemble $\{ \omega \mid X(\omega) < q \} = X^{-1}(]-\infty, q[)$ appartient à $\mathcal{F}$.
   De même, puisque $Y$ est une variable aléatoire, l'ensemble $\{ \omega \mid Y(\omega) < a - q \} = Y^{-1}(]-\infty, a-q[)$ appartient à $\mathcal{F}$.
   Leur intersection appartient à $\mathcal{F}$ (stabilité par intersection finie).
   L'union, indexée par l'ensemble dénombrable $\mathbb{Q}$, d'éléments de $\mathcal{F}$ appartient à $\mathcal{F}$ (stabilité par union dénombrable).
   Donc l'événement $\{ X + Y < a \}$ est bien dans $\mathcal{F}$, ce qui prouve que $X+Y$ est mesurable.
