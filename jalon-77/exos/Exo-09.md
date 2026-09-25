# Exercice 9 : Non-séparabilité de $L^\infty(\mathbb{R})$

**Niveau :** \bigstar\bigstar\bigstar\bigstar\bigstar

**Énoncé :**
Montrer que contrairement aux espaces $L^p$ pour $p < +\infty$, l'espace $L^\infty(\mathbb{R})$ (muni de la norme du supremum essentiel) n'est pas séparable.

**Correction Détaillée :**
1. **Définition d'une famille non-dénombrable non séparable :**
   Considérons la famille de fonctions $f_a = \mathbf{1}_{[0, a]}$ pour $a \in ]0, 1]$.
   Cette famille est indicée par $]0, 1]$, elle est donc non-dénombrable.

2. **Distance entre deux éléments :**
   Prenons $a, b \in ]0, 1]$ avec $a \neq b$. Supposons $a < b$.
   $f_b(x) - f_a(x) = \mathbf{1}_{]a, b]}(x)$.
   La valeur essentielle maximale de cette différence est $1$ sur l'intervalle $]a, b]$ (qui est de mesure strictement positive $b-a > 0$).
   Donc $\|f_b - f_a\|_\infty = 1$.

3. **Boules disjointes :**
   Considérons les boules ouvertes $B_a = B(f_a, 1/3)$ dans $L^\infty(\mathbb{R})$.
   Puisque pour $a \neq b$, $\|f_a - f_b\|_\infty = 1 > 2(1/3)$, les boules $B_a$ et $B_b$ sont disjointes.
   Nous avons ainsi construit une famille non-dénombrable de boules disjointes dans $L^\infty(\mathbb{R})$.

4. **Conclusion :**
   Si $L^\infty(\mathbb{R})$ admettait une partie dénombrable dense $D$, chaque boule $B_a$ devrait contenir au moins un point de $D$.
   Comme les boules sont disjointes, cela définirait une injection de l'ensemble non-dénombrable des indices vers l'ensemble dénombrable $D$, ce qui est impossible.
   $L^\infty(\mathbb{R})$ n'est donc pas séparable.
