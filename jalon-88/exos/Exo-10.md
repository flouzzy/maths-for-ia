# Exercice 10 : Construction géométrique de variables indépendantes

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit un carré $\Omega = [0,1] \times [0,1]$ muni de la mesure de Lebesgue plane (l'aire géométrique usuelle) définie comme probabilité $\mathbb{P}$. L'aire totale de $\Omega$ vaut 1.
Soit un point aléatoire $(X,Y)$ tiré uniformément dans ce carré.
Considérons les deux événements suivants géométriques définis par :
- $A$ : "Le point tombe sous la diagonale principale", c'est-à-dire $A = \{{(x,y) \in \Omega \mid y \le x\}}$
- $B$ : "L'abscisse du point est inférieure à $1/2$", c'est-à-dire $B = \{{(x,y) \in \Omega \mid x \le 1/2\}}$

Montrer si les événements $A$ et $B$ sont indépendants.

---
**Correction détaillée :**

Puisque le tirage est uniforme sur le carré unitaire d'aire 1, la probabilité d'un événement correspond exactement à l'aire géométrique du sous-ensemble qui le représente.

1. **Calcul de la probabilité de $A$ :**
L'ensemble $A = \{{(x,y) \in [0,1]^2 \mid y \le x\}}$ forme le triangle inférieur délimité par la diagonale reliant les sommets $(0,0)$ et $(1,1)$.
C'est un triangle rectangle de base 1 et de hauteur 1.
Son aire est $ \text{{Aire}}(A) = \frac{{1 \times 1}}{{2}} = \frac{{1}}{{2}} $.
Ainsi, $\mathbb{P}(A) = \frac{{1}}{{2}}$.

2. **Calcul de la probabilité de $B$ :**
L'ensemble $B = \{{(x,y) \in [0,1]^2 \mid x \le 1/2\}}$ forme un rectangle occupant la moitié gauche du carré (de $x=0$ à $x=1/2$, pour $y$ allant de $0$ à $1$).
C'est un rectangle de largeur $1/2$ et de hauteur $1$.
Son aire est $ \text{{Aire}}(B) = \frac{{1}}{{2}} \times 1 = \frac{{1}}{{2}} $.
Ainsi, $\mathbb{P}(B) = \frac{{1}}{{2}}$.

3. **Calcul de la probabilité de l'intersection $A \cap B$ :**
L'événement $A \cap B$ correspond aux points vérifiant à la fois $y \le x$ ET $x \le 1/2$.
Géométriquement, il s'agit de la région située sous la diagonale et restreinte à la moitié gauche du carré.
Les bornes de cet ensemble sont : $x$ varie de $0$ à $1/2$. Pour un $x$ donné, $y$ varie de $0$ à $x$.
C'est un triangle rectangle dont les sommets sont $(0,0)$, $(1/2,0)$, et $(1/2,1/2)$.
La base de ce triangle est $1/2$, sa hauteur est $1/2$.
Son aire se calcule ainsi : $ \text{{Aire}}(A \cap B) = \frac{{\text{{base}} \times \text{{hauteur}}}}{{2}} = \frac{{1/2 \times 1/2}}{{2}} = \frac{{1/4}}{{2}} = \frac{{1}}{{8}} $.
Ainsi, $\mathbb{P}(A \cap B) = \frac{{1}}{{8}}$.

4. **Test de l'indépendance :**
Nous devons vérifier si $\mathbb{P}(A \cap B) = \mathbb{P}(A) \times \mathbb{P}(B)$.
D'une part, le produit des marginales est : $\mathbb{P}(A) \times \mathbb{P}(B) = \frac{{1}}{{2}} \times \frac{{1}}{{2}} = \frac{{1}}{{4}}$.
D'autre part, la probabilité conjointe est $\mathbb{P}(A \cap B) = \frac{{1}}{{8}}$.
Clairement, $\frac{{1}}{{8}} \neq \frac{{1}}{{4}}$.
L'égalité n'est pas vérifiée.

**Conclusion :**
Les événements $A$ et $B$ ne sont **pas** indépendants. Sur un plan intuitif, savoir que le point a été tiré dans la moitié gauche (abscisses petites, événement $B$) restreint l'espace des ordonnées possibles pour rester sous la diagonale (événement $A$), augmentant la difficulté pour que $A$ se réalise par rapport au tirage global. $\blacksquare$
