# Exercice 3 : Jacobienne du changement de coordonnées sphériques $\quad \bigstar\bigstar$
## Énoncé
Soit la fonction $f : \mathbb{R}^+ \times [0, 2\pi[ \times [0, \pi] \to \mathbb{R}^3$ :
$$ f(r, \theta, \phi) = \begin{pmatrix} r \cos \theta \sin \phi \\ r \sin \theta \sin \phi \\ r \cos \phi \end{pmatrix} $$
Calculer le déterminant jacobien de $f$.
## Correction Détaillée
1. **Construction de la matrice :**
   $$ J_f = \begin{pmatrix}
   \cos\theta\sin\phi & -r\sin\theta\sin\phi & r\cos\theta\cos\phi \\
   \sin\theta\sin\phi & r\cos\theta\sin\phi & r\sin\theta\cos\phi \\
   \cos\phi & 0 & -r\sin\phi
   \end{pmatrix} $$

2. **Calcul du déterminant :**
   Développons par rapport à la deuxième colonne (ou troisième ligne) :
   $\det(J_f) = \cos\phi (-r\sin\theta\sin\phi \cdot r\sin\theta\cos\phi - r\cos\theta\sin\phi \cdot r\cos\theta\cos\phi) - r\sin\phi (\cos\theta\sin\phi \cdot r\cos\theta\sin\phi - (-r\sin\theta\sin\phi) \cdot \sin\theta\sin\phi)$
   Simplifions :
   $\det(J_f) = \cos\phi (-r^2 \sin\phi \cos\phi (\sin^2\theta + \cos^2\theta)) - r\sin\phi (r\sin^2\phi(\cos^2\theta + \sin^2\theta))$
   $\det(J_f) = -r^2 \sin\phi \cos^2\phi - r^2 \sin^3\phi$
   $\det(J_f) = -r^2 \sin\phi (\cos^2\phi + \sin^2\phi) = -r^2 \sin\phi$.
   *Remarque : la valeur absolue donne $r^2 \sin\phi$, l'élément de volume standard en géométrie.*
$\blacksquare$
