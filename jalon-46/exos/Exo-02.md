# Exercice 2 : Jacobienne du changement de coordonnées cylindriques $\quad \bigstar$
## Énoncé
Soit la fonction de changement en coordonnées cylindriques $f : \mathbb{R}^+ \times [0, 2\pi[ \times \mathbb{R} \to \mathbb{R}^3$ :
$$ f(r, \theta, z) = \begin{pmatrix} r \cos \theta \\ r \sin \theta \\ z \end{pmatrix} $$
Calculer $J_f(r, \theta, z)$ et son déterminant.
## Correction Détaillée
1. **Dérivées partielles :**
   - Par rapport à $r$ : $\cos \theta$, $\sin \theta$, $0$
   - Par rapport à $\theta$ : $-r \sin \theta$, $r \cos \theta$, $0$
   - Par rapport à $z$ : $0$, $0$, $1$

2. **Matrice Jacobienne :**
   $$ J_f(r, \theta, z) = \begin{pmatrix} \cos \theta & -r \sin \theta & 0 \\ \sin \theta & r \cos \theta & 0 \\ 0 & 0 & 1 \end{pmatrix} $$

3. **Déterminant (Le Jacobien) :**
   En développant par rapport à la dernière ligne :
   $$ \det(J_f) = 1 \cdot \det \begin{pmatrix} \cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{pmatrix} $$
   $$ \det(J_f) = r \cos^2 \theta - (-r \sin^2 \theta) = r(\cos^2 \theta + \sin^2 \theta) = r $$
$\blacksquare$
