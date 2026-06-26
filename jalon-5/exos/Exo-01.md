# Jalon 5 : Applications, injections, surjections, bijections et composition de fonctions

## Exercice 1/10

**Niveau de difficulté :** $\star \text{ sur } 5$

**Sujet :** Reconnaître une application, injection, surjection sur des ensembles finis (diagrammes sagittaux traduits en ensembles).

---

### Énoncé

Soient les ensembles finis $E = \{1, 2, 3\}$ et $F = \{a, b, c, d\}$.
On définit la relation $f$ de $E$ vers $F$ par l'ensemble de couples :
$$f = \{(1, a), (2, b), (3, a)\}$$

Déterminez, en justifiant rigoureusement chaque réponse :
1.  Si $f$ est une application de $E$ dans $F$.
2.  Si $f$ est une injection de $E$ dans $F$.
3.  Si $f$ est une surjection de $E$ dans $F$.

---

### Analyse de l'énoncé

Cet exercice introductif vise à solidifier la compréhension des définitions fondamentales d'une application, d'une injection et d'une surjection sur des ensembles finis. La relation $f$ est donnée explicitement sous forme d'un ensemble de couples, ce qui est une représentation directe d'un "diagramme sagittal" où les flèches sont les couples $(x, f(x))$.

Nous allons rappeler les définitions clés :

*   **Application (ou fonction) :** Une relation $f$ de $E$ vers $F$ est une application si et seulement si tout élément $x \in E$ possède une unique image $y \in F$. Formellement :
    1.  Pour tout $x \in E$, il existe $y \in F$ tel que $(x, y) \in f$. (Existence d'une image)
    2.  Pour tout $x \in E$, si $(x, y_1) \in f$ et $(x, y_2) \in f$, alors $y_1 = y_2$. (Unicité de l'image)
    En d'autres termes, chaque élément de l'ensemble de départ $E$ doit être le premier élément d'exactement un couple dans $f$.

*   **Injection :** Une application $f: E \to F$ est injective si et seulement si deux éléments distincts de $E$ ont toujours des images distinctes dans $F$. Formellement :
    Pour tout $x_1, x_2 \in E$, si $x_1 \neq x_2$, alors $f(x_1) \neq f(x_2)$.
    Une formulation équivalente, souvent plus pratique pour la démonstration, est la contraposée :
    Pour tout $x_1, x_2 \in E$, la condition formelle exige que si $f(x_1) = f(x_2)$, alors nécessairement $x_1 = x_2$, ce qui démontre l'absence d'information perdue.
    En d'autres termes, chaque élément de l'ensemble d'arrivée $F$ possède au plus une pré-image dans $E$.

*   **Surjection :** Une application $f: E \to F$ est surjective si et seulement si tout élément $y \in F$ possède au moins une pré-image $x \in E$. Formellement :
    Pour tout $y \in F$, il existe $x \in E$ tel que $f(x) = y$.
    Ceci est équivalent à dire que l'image de l'application, notée $f(E) = \{f(x) \mid x \in E\}$, est égale à l'ensemble d'arrivée $F$.
    En d'autres termes, chaque élément de l'ensemble d'arrivée $F$ doit être le second élément d'au moins un couple dans $f$.

Pour des ensembles finis, ces propriétés peuvent être vérifiées par inspection directe de tous les éléments et de leurs images/pré-images.

---

### Correction exhaustive pas-à-pas

Soient les ensembles $E = \{1, 2, 3\}$ et $F = \{a, b, c, d\}$.
La relation $f$ est donnée par $f = \{(1, a), (2, b), (3, a)\}$.

#### 1. $f$ est-elle une application de $E$ dans $F$ ?

Pour que $f$ soit une application, chaque élément de $E$ doit avoir une et une seule image dans $F$. Nous allons vérifier cette condition pour chaque élément de $E$.

*   **Pour l'élément $1 \in E$ :**
    Nous cherchons les couples dans $f$ dont le premier élément est $1$.
    Nous trouvons le couple $(1, a)$.
    Il n'y a pas d'autre couple dans $f$ dont le premier élément est $1$.
    Donc, l'élément $1$ a une unique image, qui est $a$.

*   **Pour l'élément $2 \in E$ :**
    Nous cherchons les couples dans $f$ dont le premier élément est $2$.
    Nous trouvons le couple $(2, b)$.
    Il n'y a pas d'autre couple dans $f$ dont le premier élément est $2$.
    Donc, l'élément $2$ a une unique image, qui est $b$.

*   **Pour l'élément $3 \in E$ :**
    Nous cherchons les couples dans $f$ dont le premier élément est $3$.
    Nous trouvons le couple $(3, a)$.
    Il n'y a pas d'autre couple dans $f$ dont le premier élément est $3$.
    Donc, l'élément $3$ a une unique image, qui est $a$.

Puisque chaque élément de $E$ (à savoir $1, 2, 3$) possède une et une seule image dans $F$, la relation $f$ satisfait la définition d'une application.

**Conclusion pour la question 1 :** Oui, $f$ est une application de $E$ dans $F$.

#### 2. $f$ est-elle une injection de $E$ dans $F$ ?

Pour que $f$ soit une injection, des éléments distincts de $E$ doivent avoir des images distinctes dans $F$. Autrement dit, si $f(x_1) = f(x_2)$, alors $x_1$ doit être égal à $x_2$.

Nous allons examiner les images des éléments de $E$ :
*   $f(1) = a$
*   $f(2) = b$
*   $f(3) = a$

Nous observons que $f(1) = a$ et $f(3) = a$.
Nous avons donc $f(1) = f(3)$.
Cependant, les éléments de départ sont $1$ et $3$, et $1 \neq 3$.
Puisque nous avons trouvé deux éléments distincts de $E$ (à savoir $1$ et $3$) qui ont la même image dans $F$ (à savoir $a$), la condition d'injectivité n'est pas remplie.

**Conclusion pour la question 2 :** Non, $f$ n'est pas une injection de $E$ dans $F$.

#### 3. $f$ est-elle une surjection de $E$ dans $F$ ?

Pour que $f$ soit une surjection, chaque élément de $F$ doit avoir au moins une pré-image dans $E$. Autrement dit, l'image de $f$, notée $f(E)$, doit être égale à l'ensemble d'arrivée $F$.

Calculons l'image de $f$, $f(E)$ :
$f(E) = \{f(x) \mid x \in E\}$
$f(E) = \{f(1), f(2), f(3)\}$
En utilisant les images que nous avons identifiées :
$f(E) = \{a, b, a\}$
En éliminant les doublons pour obtenir un ensemble :
$f(E) = \{a, b\}$

Maintenant, comparons $f(E)$ avec l'ensemble d'arrivée $F = \{a, b, c, d\}$.
Nous avons $f(E) = \{a, b\}$ et $F = \{a, b, c, d\}$.
Pour que $f$ soit surjective, il faut que $f(E) = F$.
Cependant, nous constatons que $c \in F$ mais $c \notin f(E)$.
De même, $d \in F$ mais $d \notin f(E)$.
Puisque les éléments $c$ et $d$ de $F$ n'ont aucune pré-image dans $E$, la condition de surjectivité n'est pas remplie.

**Conclusion pour la question 3 :** Non, $f$ n'est pas une surjection de $E$ dans $F$.

---

### Liens avec l'Intelligence Artificielle

Les concepts d'applications, d'injections et de surjections sont fondamentaux en mathématiques discrètes et ont des répercussions directes dans de nombreux domaines de l'Intelligence Artificielle, même si leur application n'est pas toujours explicite au premier abord.

1.  **Représentation des Données et des Relations :**
    *   En IA, les données sont souvent représentées sous forme de structures discrètes (graphes, bases de données relationnelles, ensembles de tuples). Une relation comme celle de l'exercice peut être vue comme une table dans une base de données où $E$ est un ensemble de clés et $F$ un ensemble de valeurs.
    *   Vérifier si une relation est une application, c'est s'assurer de l'intégrité des données : chaque "clé" (élément de $E$) doit correspondre à une "valeur" unique (élément de $F$). C'est une contrainte de base pour de nombreux systèmes de gestion de données utilisés en IA.

2.  **Fonctions de Hachage et Tables de Hachage :**
    *   Les fonctions de hachage, essentielles pour l'efficacité des structures de données comme les tables de hachage (utilisées pour l'accès rapide aux données en IA), sont des applications. Idéalement, une fonction de hachage serait injective (pas de collisions), mais en pratique, ce n'est pas le cas pour des ensembles de départ plus grands que l'ensemble d'arrivée. L'étude des collisions (non-injectivité) est cruciale pour la performance des algorithmes.

3.  **Apprentissage Automatique (Machine Learning) :**
    *   **Classification :** Un classifieur en apprentissage automatique est une application $h: X \to Y$, où $X$ est l'espace des caractéristiques d'entrée et $Y$ est l'ensemble des étiquettes de classe. Pour un classifieur, il est essentiel que chaque entrée ait une unique prédiction (c'est une application). La surjectivité est souvent souhaitable (le modèle doit pouvoir prédire toutes les classes possibles), tandis que l'injectivité est rarement une propriété recherchée ou réalisable (des entrées différentes peuvent et doivent souvent être classées de la même manière).
    *   **Intégration de Caractéristiques (Feature Engineering) :** Les transformations de caractéristiques (par exemple, la normalisation, la vectorisation de texte) sont des applications. Comprendre si ces transformations sont injectives (préservent l'information unique de chaque donnée) ou non (introduisent des collisions ou une perte d'information) est crucial pour la conception de modèles performants.
    *   **Réseaux de Neurones :** Chaque couche d'un réseau de neurones applique une fonction (combinaison linéaire suivie d'une fonction d'activation) à son entrée. L'ensemble du réseau est une composition de telles applications. L'analyse de la surjectivité des couches de sortie est liée à la capacité du réseau à générer une diversité de sorties.

4.  **Logique et Raisonnement Automatisé :**
    *   Dans la logique formelle et les systèmes de raisonnement automatisé, les relations et les fonctions sont utilisées pour modéliser des connaissances et des inférences. La vérification des propriétés de ces relations est une étape fondamentale pour garantir la cohérence et la validité des systèmes.

En somme, bien que l'exercice porte sur des ensembles finis très simples, les principes sous-jacents de l'existence et de l'unicité des images (application), de la distinction des pré-images (injection) et de la couverture de l'espace d'arrivée (surjection) sont des concepts mathématiques omniprésents qui structurent la conception, l'analyse et l'optimisation de nombreux algorithmes et systèmes d'Intelligence Artificielle.
