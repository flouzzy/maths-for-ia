# Exercice 5
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $E$ un espace vectoriel normé réel et $A, B \subset E$ deux ensembles convexes disjoints.
Montrer que si $A$ est d'intérieur non vide (c'est-à-dire $\text{Int}(A) \ne \emptyset$), alors on peut séparer $A$ et $B$ au sens large.
*Indication : Appliquer le théorème de séparation à $\text{Int}(A)$ et $B$, puis étendre le résultat en utilisant les propriétés topologiques de l'adhérence.*

**Correction :**
1. **Application préliminaire sur l'intérieur :**
   Posons $A^\circ = \text{Int}(A)$. Par hypothèse, $A^\circ$ est non vide.
   Puisque $A$ est convexe, l'intérieur d'un convexe (lorsqu'il est non vide) est également convexe.
   $A^\circ$ est un ensemble ouvert.
   De plus, comme $A^\circ \subset A$ et que $A \cap B = \emptyset$, on a $A^\circ \cap B = \emptyset$.
   Nous sommes exactement dans les conditions de la première forme géométrique du théorème de Hahn-Banach pour les ensembles $A^\circ$ et $B$.
2. **Existence de l'hyperplan sur l'intérieur :**
   Il existe une forme linéaire continue non nulle $f \in E^*$ et un réel $\alpha$ tels que :
   $\forall x \in A^\circ, \, f(x) < \alpha$
   $\forall y \in B, \, f(y) \ge \alpha$
3. **Extension par passage à l'adhérence :**
   Nous devons montrer que l'inégalité $f(x) \le \alpha$ (au sens large) reste vraie pour tout $x \in A$.
   Puisque $A$ est convexe et d'intérieur non vide, un résultat classique de topologie convexe affirme que $A \subset \overline{A^\circ}$ (l'ensemble est inclus dans l'adhérence de son intérieur).
   Soit $x \in A$. Alors $x \in \overline{A^\circ}$. Par caractérisation séquentielle de l'adhérence dans les espaces normés, il existe une suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $A^\circ$ telle que $\lim_{n \to \infty} x_n = x$.
   Pour tout $n \in \mathbb{N}$, l'élément $x_n$ appartient à l'intérieur, donc nous avons l'inégalité stricte vérifiée :
   $f(x_n) < \alpha$
   La forme linéaire $f$ est continue par construction du théorème de Hahn-Banach topologique. En passant à la limite quand $n \to \infty$ dans l'inégalité stricte, nous obtenons une inégalité large pour la limite :
   $f(\lim_{n \to \infty} x_n) \le \alpha \implies f(x) \le \alpha$.
4. **Conclusion :**
   Nous avons établi que pour tout $x \in A$, $f(x) \le \alpha$, et pour tout $y \in B$, $f(y) \ge \alpha$.
   La forme linéaire $f$ et le réel $\alpha$ définissent donc un hyperplan qui sépare au sens large $A$ et $B$, validant ainsi l'extension.
