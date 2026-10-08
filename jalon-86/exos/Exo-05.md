## Mesurabilité de la somme de deux V.A.R. \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $X_1$ et $X_2$ deux variables aléatoires réelles sur l'espace $(\Omega, \mathcal{F}, \mathbb{P})$.
Démontrer rigoureusement que la somme $S = X_1 + X_2$ est également une variable aléatoire réelle.
*Indication : On pourra utiliser le fait que l'ensemble des nombres rationnels $\mathbb{Q}$ est dénombrable et dense dans $\mathbb{R}$.*

**Correction Explicative :**
1. Pour démontrer que $S$ est une variable aléatoire réelle, il est suffisant, d'après le critère sur les générateurs de la tribu borélienne, de montrer que pour tout réel $a$, l'ensemble $A_a = \{ \omega \in \Omega \mid (X_1 + X_2)(\omega) < a \}$ appartient à la tribu $\mathcal{F}$.
2. Analysons l'inégalité définissant l'ensemble $A_a$ :
   $X_1(\omega) + X_2(\omega) < a \iff X_1(\omega) < a - X_2(\omega)$.
3. Entre deux nombres réels distincts ($X_1(\omega)$ et $a - X_2(\omega)$), on peut toujours intercaler un nombre rationnel en raison de la densité de $\mathbb{Q}$ dans $\mathbb{R}$. Ainsi, l'inégalité stricte est équivalente à l'existence d'un rationnel $q \in \mathbb{Q}$ tel que :
   $X_1(\omega) < q < a - X_2(\omega)$.
4. L'inégalité $q < a - X_2(\omega)$ peut se réécrire comme $X_2(\omega) < a - q$.
   Par conséquent, la condition s'exprime comme la conjonction de deux conditions faisant intervenir $X_1$ et $X_2$ séparément :
   $X_1(\omega) < q \quad \text{ET} \quad X_2(\omega) < a - q$.
5. Traduisons cette condition ensemblistiquement. L'existence d'un tel rationnel s'exprime par une union sur tous les rationnels de l'intersection de deux événements :
   $$A_a = \bigcup_{q \in \mathbb{Q}} \left( \{ \omega \in \Omega \mid X_1(\omega) < q \} \cap \{ \omega \in \Omega \mid X_2(\omega) < a - q \} \right)$$
6. Vérifions que cet ensemble appartient à la tribu $\mathcal{F}$ :
   - Par hypothèse, $X_1$ est une variable aléatoire, donc l'ensemble $\{ \omega \in \Omega \mid X_1(\omega) < q \}$ est dans $\mathcal{F}$ pour tout rationnel $q$.
   - Par hypothèse, $X_2$ est une variable aléatoire, donc l'ensemble $\{ \omega \in \Omega \mid X_2(\omega) < a - q \}$ est dans $\mathcal{F}$ pour tout rationnel $q$ (puisque $a-q$ est un nombre réel).
   - L'intersection de ces deux ensembles appartenant à la tribu appartient également à la tribu par stabilité de $\mathcal{F}$ par intersection finie.
   - L'ensemble $\mathbb{Q}$ des nombres rationnels est dénombrable. Ainsi, l'union sur $q \in \mathbb{Q}$ est une union dénombrable d'ensembles mesurables.
   - Par définition d'une tribu ($\sigma$-algèbre), elle est stable par union dénombrable.
7. Conclusion : L'ensemble $A_a = \{ \omega \in \Omega \mid S(\omega) < a \}$ appartient bien à $\mathcal{F}$ pour tout réel $a$. Cela prouve de manière exhaustive que $S = X_1 + X_2$ est une application mesurable, et donc une variable aléatoire réelle.
