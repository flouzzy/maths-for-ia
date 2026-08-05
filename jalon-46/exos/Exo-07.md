# Exercice 7 : Application de la Chain Rule à une fonction matricielle $\quad \bigstar\bigstar\bigstar\star\star$
## Énoncé
Soit $f : \mathcal{M}_n(\mathbb{R}) \to \mathcal{M}_n(\mathbb{R})$ définie par $f(X) = X^2$.
Soit $g : \mathcal{M}_n(\mathbb{R}) \to \mathbb{R}$ définie par $g(X) = \mathrm{Tr}(X)$.
Calculer la différentielle de $h = g \circ f$ en $A$.
## Correction Détaillée
Calculons d'abord les différentielles séparément.
1. Différentielle de $f(X) = X^2$ :
   $f(A+H) = (A+H)^2 = A^2 + AH + HA + H^2$.
   La partie linéaire en $H$ est $df_A(H) = AH + HA$, avec reste $\|H^2\| = O(\|H\|^2)$.
2. Différentielle de $g(X) = \mathrm{Tr}(X)$ :
   Comme la trace est linéaire, sa différentielle est elle-même : $dg_B(K) = \mathrm{Tr}(K)$.
3. Règle de la chaîne :
   $dh_A(H) = dg_{f(A)}(df_A(H)) = \mathrm{Tr}(df_A(H)) = \mathrm{Tr}(AH + HA)$.
   Par linéarité de la trace : $\mathrm{Tr}(AH + HA) = \mathrm{Tr}(AH) + \mathrm{Tr}(HA)$.
   Par propriété de symétrie cyclique : $\mathrm{Tr}(HA) = \mathrm{Tr}(AH)$.
   Donc $dh_A(H) = 2\mathrm{Tr}(AH)$.
La différentielle, au sens scalaire (gradient matriciel), correspond à la matrice $\nabla h(A) = 2A^T$.
$\blacksquare$
