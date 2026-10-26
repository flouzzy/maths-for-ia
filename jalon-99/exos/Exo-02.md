# Exercice 2
**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $E$ un espace vectoriel normé réel. Soit $C$ un convexe fermé de $E$, non vide, et $x_0$ un point de $E$ n'appartenant pas à $C$ ($x_0 \notin C$).
Montrer qu'il existe un hyperplan affine strictement séparateur entre le point $x_0$ et le convexe $C$.

**Correction :**
1. **Identification des sous-ensembles :**
   Posons $A = C$ et $B = \{x_0\}$.
2. **Vérification des hypothèses de la deuxième forme de Hahn-Banach :**
   - $A$ est un convexe fermé par hypothèse.
   - $B$ est un singleton. Un singleton est toujours compact, car toute suite extraite de $B$ converge trivialement vers $x_0 \in B$. Un singleton est également un sous-ensemble convexe (le segment reliant $x_0$ à $x_0$ est réduit à $x_0$).
   - $A$ et $B$ sont disjoints car $x_0 \notin C$, donc $\{x_0\} \cap C = \emptyset$.
3. **Application du théorème :**
   Puisque $A$ est convexe fermé, $B$ est convexe compact, et $A \cap B = \emptyset$, la deuxième forme géométrique du théorème de Hahn-Banach s'applique.
4. **Conclusion :**
   Il existe une forme linéaire continue non nulle $f \in E^*$ et un scalaire $\alpha \in \mathbb{R}$, et un $\varepsilon > 0$ tels que :
   $\forall x \in C, \, f(x) \le \alpha - \varepsilon$
   et pour l'unique point $y \in B$, $f(x_0) \ge \alpha + \varepsilon$.
   L'hyperplan $H = \{ x \in E \mid f(x) = \alpha \}$ sépare strictement le point $x_0$ et le convexe fermé $C$. Cette construction est la base du théorème de projection sur un convexe fermé dans les espaces de Hilbert, bien qu'elle soit vraie dans tout espace normé.
