# Exercice 2 (Jalon 104)

**Difficulté :** $\star\star\star\star\star$

Considérons l'espace vectoriel réel $\mathbb{R}^3$ muni du produit scalaire euclidien standard. Ce produit scalaire est défini, pour tout $x = (x_1, x_2, x_3) \in \mathbb{R}^3$ et $y = (y_1, y_2, y_3) \in \mathbb{R}^3$, par la relation :
$$ \langle x, y \rangle = x_1 y_1 + x_2 y_2 + x_3 y_3 $$
La norme associée est donnée par $\|x\| = \sqrt{\langle x, x \rangle}$.

Soit $B$ l'ensemble de vecteurs suivant :
$$ B = \left\{ e_1, e_2, e_3 \right\} $$
où les vecteurs sont définis par :
$$ e_1 = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0 \right) $$
$$ e_2 = \left( -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0 \right) $$
$$ e_3 = \left( 0, 0, 1 \right) $$

**Question :** Déterminez si l'ensemble $B$ constitue une base hilbertienne de l'espace $\mathbb{R}^3$.

---

## Correction détaillée de l'Exercice 2

Pour déterminer si l'ensemble $B = \{e_1, e_2, e_3\}$ constitue une base hilbertienne de l'espace $\mathbb{R}^3$, nous devons vérifier deux propriétés fondamentales. Dans un espace de Hilbert de dimension finie $n$, une base hilbertienne est équivalente à un ensemble de $n$ vecteurs formant un système orthonormal et engendrant l'espace.

Plus précisément, un ensemble de vecteurs $\{e_i\}_{i=1}^n$ forme une base orthonormée (et donc une base hilbertienne) d'un espace vectoriel euclidien de dimension $n$ si et seulement si :
1.  **Orthogonalité :** Les vecteurs sont mutuellement orthogonaux. Pour tout $i, j \in \{1, \dots, n\}$ avec $i \neq j$, $\langle e_i, e_j \rangle = 0$.
2.  **Normalisation :** Chaque vecteur est de norme unitaire. Pour tout $i \in \{1, \dots, n\}$, $\|e_i\| = 1$.
3.  **Complétude (propriété de base) :** Dans un espace de dimension $n$, un ensemble de $n$ vecteurs qui est orthonormal est automatiquement une base de cet espace. L'espace $\mathbb{R}^3$ est de dimension $3$, et l'ensemble $B$ contient $3$ vecteurs.

Nous allons procéder à la vérification rigoureuse de ces conditions pour l'ensemble $B = \{e_1, e_2, e_3\}$.

### Étape 1 : Vérification de la normalisation des vecteurs

Nous calculons la norme au carré de chaque vecteur $e_i$, puis sa norme. Rappelons que $\|e_i\|^2 = \langle e_i, e_i \rangle$.

#### Calcul de la norme de $e_1$ :
Le vecteur $e_1$ est donné par $e_1 = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0 \right)$.
Nous calculons son produit scalaire avec lui-même en utilisant la définition du produit scalaire euclidien standard :
$$ \langle e_1, e_1 \rangle = \left( \frac{1}{\sqrt{2}} \right) \cdot \left( \frac{1}{\sqrt{2}} \right) + \left( \frac{1}{\sqrt{2}} \right) \cdot \left( \frac{1}{\sqrt{2}} \right) + (0) \cdot (0) $$
$$ \langle e_1, e_1 \rangle = \frac{1}{2} + \frac{1}{2} + 0 $$
$$ \langle e_1, e_1 \rangle = 1 $$
Par conséquent, la norme de $e_1$ est $\|e_1\| = \sqrt{1} = 1$.
Le vecteur $e_1$ est bien unitaire.

#### Calcul de la norme de $e_2$ :
Le vecteur $e_2$ est donné par $e_2 = \left( -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0 \right)$.
Nous calculons son produit scalaire avec lui-même :
$$ \langle e_2, e_2 \rangle = \left( -\frac{1}{\sqrt{2}} \right) \cdot \left( -\frac{1}{\sqrt{2}} \right) + \left( \frac{1}{\sqrt{2}} \right) \cdot \left( \frac{1}{\sqrt{2}} \right) + (0) \cdot (0) $$
$$ \langle e_2, e_2 \rangle = \frac{1}{2} + \frac{1}{2} + 0 $$
$$ \langle e_2, e_2 \rangle = 1 $$
Par conséquent, la norme de $e_2$ est $\|e_2\| = \sqrt{1} = 1$.
Le vecteur $e_2$ est bien unitaire.

#### Calcul de la norme de $e_3$ :
Le vecteur $e_3$ est donné par $e_3 = \left( 0, 0, 1 \right)$.
Nous calculons son produit scalaire avec lui-même :
$$ \langle e_3, e_3 \rangle = (0) \cdot (0) + (0) \cdot (0) + (1) \cdot (1) $$
$$ \langle e_3, e_3 \rangle = 0 + 0 + 1 $$
$$ \langle e_3, e_3 \rangle = 1 $$
Par conséquent, la norme de $e_3$ est $\|e_3\| = \sqrt{1} = 1$.
Le vecteur $e_3$ est bien unitaire.

Conclusion de l'Étape 1 : Tous les vecteurs de l'ensemble $B$ sont de norme unitaire. La condition de normalisation est satisfaite.

### Étape 2 : Vérification de l'orthogonalité mutuelle des vecteurs

Nous calculons le produit scalaire entre chaque paire distincte de vecteurs. Le résultat doit être zéro pour qu'ils soient orthogonaux.

#### Calcul de $\langle e_1, e_2 \rangle$ :
$$ \langle e_1, e_2 \rangle = \left( \frac{1}{\sqrt{2}} \right) \cdot \left( -\frac{1}{\sqrt{2}} \right) + \left( \frac{1}{\sqrt{2}} \right) \cdot \left( \frac{1}{\sqrt{2}} \right) + (0) \cdot (0) $$
$$ \langle e_1, e_2 \rangle = -\frac{1}{2} + \frac{1}{2} + 0 $$
$$ \langle e_1, e_2 \rangle = 0 $$
Les vecteurs $e_1$ et $e_2$ sont orthogonaux.

#### Calcul de $\langle e_1, e_3 \rangle$ :
$$ \langle e_1, e_3 \rangle = \left( \frac{1}{\sqrt{2}} \right) \cdot (0) + \left( \frac{1}{\sqrt{2}} \right) \cdot (0) + (0) \cdot (1) $$
$$ \langle e_1, e_3 \rangle = 0 + 0 + 0 $$
$$ \langle e_1, e_3 \rangle = 0 $$
Les vecteurs $e_1$ et $e_3$ sont orthogonaux.

#### Calcul de $\langle e_2, e_3 \rangle$ :
$$ \langle e_2, e_3 \rangle = \left( -\frac{1}{\sqrt{2}} \right) \cdot (0) + \left( \frac{1}{\sqrt{2}} \right) \cdot (0) + (0) \cdot (1) $$
$$ \langle e_2, e_3 \rangle = 0 + 0 + 0 $$
$$ \langle e_2, e_3 \rangle = 0 $$
Les vecteurs $e_2$ et $e_3$ sont orthogonaux.

Conclusion de l'Étape 2 : Toutes les paires distinctes de vecteurs de l'ensemble $B$ sont orthogonales. La condition d'orthogonalité est satisfaite.

### Étape 3 : Conclusion sur la nature de l'ensemble $B$

À partir des étapes précédentes, nous avons démontré que l'ensemble $B = \{e_1, e_2, e_3\}$ est un système orthonormal de vecteurs dans $\mathbb{R}^3$. C'est-à-dire, pour tout $i, j \in \{1, 2, 3\}$, nous avons $\langle e_i, e_j \rangle = \delta_{ij}$, où $\delta_{ij}$ est le symbole de Kronecker (égal à 1 si $i=j$ et 0 si $i \neq j$).

L'espace $\mathbb{R}^3$ est un espace de Hilbert de dimension finie égale à $3$.
L'ensemble $B$ contient exactement $3$ vecteurs.
Dans un espace vectoriel de dimension $n$, tout ensemble de $n$ vecteurs qui est orthonormal constitue automatiquement une base de cet espace. Cet ensemble est linéairement indépendant et engendre l'espace.

Par conséquent, l'ensemble $B$ est une base orthonormée de $\mathbb{R}^3$.
Puisqu'une base hilbertienne dans un espace de Hilbert de dimension finie est, par définition, une base orthonormée, nous pouvons conclure.

**Conclusion finale :** L'ensemble $B = \left\{ \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0 \right), \left( -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0 \right), \left( 0, 0, 1 \right) \right\}$ constitue bien une base hilbertienne de l'espace $\mathbb{R}^3$ muni du produit scalaire euclidien standard.