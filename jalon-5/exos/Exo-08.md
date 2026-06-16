# Jalon 5 : Applications, injections, surjections, bijections et composition de fonctions

## Exercice 8/10 : Injectivité et existence d'une fonction inverse à gauche

**Niveau de difficulté :** ★★★★☆

---

### Énoncé

Soient $E$ et $F$ deux ensembles non vides.
Soit $f: E \to F$ une application.

Démontrer que $f$ est injective si et seulement si il existe une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$.

Où $\text{Id}_E: E \to E$ est l'application identité sur $E$, définie par $\text{Id}_E(x) = x$ pour tout $x \in E$.

---

### Analyse de l'énoncé

Cet exercice nous demande de prouver une équivalence fondamentale en théorie des ensembles et des fonctions, reliant la propriété d'injectivité d'une fonction à l'existence d'une "inverse à gauche".

1.  **Comprendre l'injectivité :** Une application $f: E \to F$ est dite injective si et seulement si pour tous $x_1, x_2 \in E$, l'égalité $f(x_1) = f(x_2)$ implique $x_1 = x_2$. En d'autres termes, des éléments distincts de l'ensemble de départ $E$ sont toujours envoyés sur des éléments distincts de l'ensemble d'arrivée $F$. Il n'y a pas de "collisions" d'images.

2.  **Comprendre l'inverse à gauche :** L'existence d'une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$ signifie que la composition de $g$ avec $f$ redonne l'identité sur $E$. Cela implique que pour tout $x \in E$, $(g \circ f)(x) = g(f(x)) = x$. L'application $g$ "annule" l'effet de $f$ pour tout élément de $E$.

3.  **Structure de la preuve :** L'énoncé est un "si et seulement si" (équivalence logique), ce qui signifie que nous devons prouver deux implications distinctes :
    *   **Implication 1 ($\implies$) :** Si $f$ est injective, alors il existe une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$. Pour cette partie, nous devrons *construire* explicitement une telle fonction $g$.
    *   **Implication 2 ($\impliedesup$) :** S'il existe une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$, alors $f$ est injective. Pour cette partie, nous devrons utiliser la propriété de $g$ pour démontrer l'injectivité de $f$.

4.  **Considérations sur les ensembles :** L'énoncé précise que $E$ et $F$ sont des ensembles non vides. Cette condition est importante, notamment pour la construction de $g$ dans la première implication, où nous pourrions avoir besoin de choisir un élément arbitraire de $E$.

---

### Correction exhaustive pas-à-pas

Nous allons prouver les deux implications séparément.

#### Partie 1 : $f$ est injective $\implies$ il existe $g: F \to E$ telle que $g \circ f = \text{Id}_E$.

**Hypothèse :** $f: E \to F$ est une application injective.
**Objectif :** Construire une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$.

Puisque $E$ est un ensemble non vide, nous pouvons choisir et fixer un élément arbitraire $x_0 \in E$. Cet élément nous servira pour définir $g(y)$ lorsque $y$ n'est pas une image par $f$.

Nous allons définir l'application $g: F \to E$ de la manière suivante :

Pour tout $y \in F$:
*   **Cas 1 :** Si $y \in \text{Im}(f)$ (l'image de $f$), cela signifie qu'il existe au moins un $x \in E$ tel que $f(x) = y$.
    Puisque $f$ est injective, si $f(x_1) = y$ et $f(x_2) = y$, alors $f(x_1) = f(x_2)$, ce qui implique $x_1 = x_2$ par définition de l'injectivité.
    Par conséquent, pour chaque $y \in \text{Im}(f)$, il existe un *unique* $x \in E$ tel que $f(x) = y$.
    Dans ce cas, nous définissons $g(y) = x$, où $x$ est l'unique antécédent de $y$ par $f$.

*   **Cas 2 :** Si $y \notin \text{Im}(f)$, cela signifie qu'il n'existe aucun $x \in E$ tel que $f(x) = y$.
    Dans ce cas, nous définissons $g(y) = x_0$, où $x_0$ est l'élément arbitraire de $E$ que nous avons fixé au début.

Cette définition de $g$ est bien une application de $F$ vers $E$, car pour chaque élément $y \in F$, $g(y)$ est défini de manière unique et appartient à $E$.

Maintenant, nous devons vérifier que $g \circ f = \text{Id}_E$.
Pour cela, nous devons montrer que pour tout $x \in E$, $(g \circ f)(x) = x$.

Soit $x \in E$ un élément quelconque.
Calculons $(g \circ f)(x)$:
1.  D'abord, nous évaluons $f(x)$. Soit $y_x = f(x)$.
2.  Par définition de l'image, $y_x = f(x)$ est un élément de $\text{Im}(f)$.
3.  Puisque $y_x \in \text{Im}(f)$, la définition de $g$ pour ce $y_x$ relève du Cas 1.
4.  Selon le Cas 1, $g(y_x)$ est défini comme l'unique antécédent de $y_x$ par $f$.
5.  Nous savons que $x$ est un antécédent de $y_x$ par $f$, car $f(x) = y_x$.
6.  Puisque $x$ est l'unique antécédent de $y_x$ par $f$, il s'ensuit que $g(y_x) = x$.
7.  En substituant $y_x = f(x)$, nous obtenons $g(f(x)) = x$.

Cette égalité $g(f(x)) = x$ est vraie pour tout $x \in E$.
Par conséquent, $g \circ f = \text{Id}_E$.

Nous avons donc construit une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$.
L'implication $f \text{ est injective} \implies \text{il existe } g: F \to E \text{ telle que } g \circ f = \text{Id}_E$ est démontrée.

#### Partie 2 : Il existe $g: F \to E$ telle que $g \circ f = \text{Id}_E \implies f$ est injective.

**Hypothèse :** Il existe une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$.
**Objectif :** Démontrer que $f$ est injective.

Pour prouver que $f$ est injective, nous devons montrer que pour tous $x_1, x_2 \in E$, si $f(x_1) = f(x_2)$, alors $x_1 = x_2$.

Soient $x_1, x_2 \in E$ deux éléments quelconques de $E$.
Supposons que $f(x_1) = f(x_2)$.

Puisque $f(x_1)$ et $f(x_2)$ sont des éléments de $F$, nous pouvons appliquer l'application $g$ à ces deux éléments.
En appliquant $g$ aux deux membres de l'égalité $f(x_1) = f(x_2)$, nous obtenons :
$g(f(x_1)) = g(f(x_2))$.

Par définition de la composition d'applications, nous avons :
$(g \circ f)(x_1) = (g \circ f)(x_2)$.

Par notre hypothèse, nous savons que $g \circ f = \text{Id}_E$.
Donc, nous pouvons remplacer $(g \circ f)(x_1)$ par $\text{Id}_E(x_1)$ et $(g \circ f)(x_2)$ par $\text{Id}_E(x_2)$.
L'égalité devient :
$\text{Id}_E(x_1) = \text{Id}_E(x_2)$.

Par définition de l'application identité $\text{Id}_E$, nous avons $\text{Id}_E(x_1) = x_1$ et $\text{Id}_E(x_2) = x_2$.
Par conséquent, l'égalité se simplifie en :
$x_1 = x_2$.

Nous avons donc montré que si $f(x_1) = f(x_2)$, alors $x_1 = x_2$.
Ceci est précisément la définition de l'injectivité de $f$.

L'implication $\text{il existe } g: F \to E \text{ telle que } g \circ f = \text{Id}_E \implies f \text{ est injective}$ est démontrée.

#### Conclusion

Puisque nous avons prouvé les deux implications, nous pouvons conclure que $f$ est injective si et seulement si il existe une application $g: F \to E$ telle que $g \circ f = \text{Id}_E$.

---

### Liens avec l'Intelligence Artificielle

Le concept d'injectivité et d'inverse à gauche trouve des résonances profondes dans plusieurs domaines de l'Intelligence Artificielle, notamment en ce qui concerne la représentation des données, la compression et la robustesse des modèles.

1.  **Représentation et Encodage des Données (Autoencodeurs) :**
    *   Dans les réseaux de neurones, en particulier les autoencodeurs, l'objectif est d'apprendre une représentation compacte (un encodage) des données d'entrée. Un autoencodeur est composé d'un encodeur $f: X \to Z$ (où $X$ est l'espace d'entrée et $Z$ est l'espace latent) et d'un décodeur $g: Z \to X$.
    *   Idéalement, nous souhaiterions que l'encodeur $f$ soit une fonction injective. Si $f$ est injective, cela signifie que chaque donnée d'entrée unique $x \in X$ est mappée à une représentation latente unique $z \in Z$. Aucune information n'est perdue lors de l'encodage.
    *   Dans ce scénario idéal, le décodeur $g$ agirait comme une inverse à gauche (et même une inverse tout court si $f$ est surjective sur $Z$), permettant de reconstruire parfaitement l'entrée originale $x$ à partir de sa représentation latente $z = f(x)$, c'est-à-dire $g(f(x)) = x$.
    *   En pratique, les autoencodeurs ne garantissent pas l'injectivité (surtout si la dimension de $Z$ est inférieure à celle de $X$), mais la recherche d'une reconstruction fidèle ($g \circ f \approx \text{Id}_X$) est une tentative d'approcher cette propriété.

2.  **Compression de Données sans Perte (Lossless Compression) :**
    *   Les algorithmes de compression sans perte visent à transformer des données (par exemple, un fichier texte ou une image) en une représentation plus compacte sans aucune perte d'information.
    *   Le processus de compression peut être vu comme une fonction $f: \text{Données Originales} \to \text{Données Compressées}$. Pour que la compression soit sans perte, $f$ doit être injective. Si $f$ n'était pas injective, deux ensembles de données originaux distincts pourraient être compressés en la même représentation, rendant impossible de déterminer l'original lors de la décompression.
    *   La décompression est alors l'application $g: \text{Données Compressées} \to \text{Données Originales}$, qui doit agir comme une inverse à gauche (et même une inverse tout court) pour restaurer les données originales : $g \circ f = \text{Id}_{\text{Données Originales}}$.

3.  **Fonctions de Hachage et Indexation :**
    *   Les fonctions de hachage sont utilisées pour mapper des données de taille arbitraire à des valeurs de taille fixe (les "hachages"). Elles sont fondamentales pour l'indexation de données (tables de hachage) et la vérification d'intégrité.
    *   Idéalement, une fonction de hachage "parfaite" serait injective sur l'ensemble des clés utilisées, c'est-à-dire qu'elle ne produirait jamais de collisions (deux clés différentes donnant le même hachage).
    *   Si une fonction de hachage $h: K \to V$ (où $K$ est l'ensemble des clés et $V$ l'ensemble des valeurs de hachage) était injective, alors il existerait une fonction $g: V \to K$ telle que $g \circ h = \text{Id}_K$, permettant de retrouver la clé originale à partir de son hachage. En pratique, les fonctions de hachage ne sont pas injectives sur l'ensemble de toutes les entrées possibles, mais elles sont conçues pour minimiser les collisions sur l'ensemble des entrées attendues.

4.  **Cryptographie :**
    *   Les fonctions injectives sont cruciales en cryptographie. Par exemple, une fonction de chiffrement $E: \text{Message Clair} \to \text{Message Chiffré}$ doit être injective. Si deux messages clairs différents pouvaient être chiffrés en le même message chiffré, il serait impossible de déchiffrer de manière unique le message original.
    *   La fonction de déchiffrement $D: \text{Message Chiffré} \to \text{Message Clair}$ agit alors comme une inverse à gauche (et une inverse à droite) de la fonction de chiffrement, assurant que $D \circ E = \text{Id}_{\text{Message Clair}}$.

En somme, la propriété d'injectivité garantit qu'une transformation ne perd pas d'information, et l'existence d'une inverse à gauche est la manifestation concrète de cette capacité à "revenir en arrière" ou à "annuler" la transformation pour les éléments qui ont été effectivement transformés. C'est un principe fondamental pour la réversibilité et la fidélité des processus en IA.
