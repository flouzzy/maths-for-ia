# Exercice 7/10 : Images directes et images réciproques d'ensembles

**Jalon 5 : Applications, injections, surjections, bijections et composition de fonctions**

**Niveau de difficulté :** $\star$$\star$$\star$$\star$☆

---

### Énoncé

Soient $E$ et $F$ deux ensembles non vides.
Soit $f: E \to F$ une application.

1.  Soient $A$ et $B$ deux sous-ensembles de $E$ (i.e., $A \subseteq E$ et $B \subseteq E$).
    Démontrer que l'image directe de l'union de $A$ et $B$ par $f$ est égale à l'union des images directes de $A$ et $B$ par $f$.
    Autrement dit, démontrer que $f(A \cup B) = f(A) \cup f(B)$.

2.  Soient $A'$ et $B'$ deux sous-ensembles de $F$ (i.e., $A' \subseteq F$ et $B' \subseteq F$).
    Démontrer que l'image réciproque de l'intersection de $A'$ et $B'$ par $f$ est égale à l'intersection des images réciproques de $A'$ et $B'$ par $f$.
    Autrement dit, démontrer que $f^{-1}(A' \cap B') = f^{-1}(A') \cap f^{-1}(B')$.

---

### Analyse de l'énoncé

Cet exercice vise à consolider la compréhension des définitions d'image directe et d'image réciproque d'ensembles par une application, ainsi que leur interaction avec les opérations ensemblistes fondamentales que sont l'union et l'intersection.

Pour démontrer l'égalité de deux ensembles $X$ et $Y$ (par exemple, $X = f(A \cup B)$ et $Y = f(A) \cup f(B)$), la méthode standard consiste à prouver la double inclusion :
1.  $X \subseteq Y$ (tout élément de $X$ est un élément de $Y$).
2.  $Y \subseteq X$ (tout élément de $Y$ est un élément de $X$).

Nous devrons nous appuyer rigoureusement sur les définitions :
*   **Image directe d'un ensemble $S \subseteq E$ :** $f(S) = \{y \in F \mid \exists x \in S, y = f(x)\}$.
*   **Image réciproque d'un ensemble $S' \subseteq F$ :** $f^{-1}(S') = \{x \in E \mid f(x) \in S'\}$.
*   **Union d'ensembles :** $x \in X \cup Y \iff x \in X \text{ ou } x \in Y$.
*   **Intersection d'ensembles :** $x \in X \cap Y \iff x \in X \text{ et } x \in Y$.

La difficulté réside dans la manipulation précise des quantificateurs ($\exists$, $\forall$) et des connecteurs logiques (et, ou) à chaque étape de la démonstration, sans aucune ellipse mathématique.

---

### Correction exhaustive pas-à-pas

#### Question 1 : Démontrer que $f(A \cup B) = f(A) \cup f(B)$

Pour démontrer cette égalité, nous allons prouver la double inclusion : $f(A \cup B) \subseteq f(A) \cup f(B)$ et $f(A) \cup f(B) \subseteq f(A \cup B)$.

##### Étape 1.1 : Démonstration de $f(A \cup B) \subseteq f(A) \cup f(B)$

Soit $y$ un élément quelconque de l'ensemble $f(A \cup B)$.
Par définition de l'image directe, cela signifie qu'il existe au moins un élément $x$ dans l'ensemble $A \cup B$ tel que $y = f(x)$.
$$y \in f(A \cup B) \implies \exists x \in A \cup B \text{ tel que } y = f(x)$$
Puisque $x \in A \cup B$, par définition de l'union, cela signifie que $x$ appartient à $A$ ou $x$ appartient à $B$.
$$x \in A \cup B \iff (x \in A \text{ ou } x \in B)$$
Nous avons donc deux cas possibles pour cet élément $x$ :

**Cas 1 :** $x \in A$.
Si $x \in A$ et $y = f(x)$, alors par définition de l'image directe, $y$ est un élément de $f(A)$.
$$x \in A \text{ et } y = f(x) \implies y \in f(A)$$

**Cas 2 :** $x \in B$.
Si $x \in B$ et $y = f(x)$, alors par définition de l'image directe, $y$ est un élément de $f(B)$.
$$x \in B \text{ et } y = f(x) \implies y \in f(B)$$

Dans les deux cas (soit $y \in f(A)$, soit $y \in f(B)$), nous pouvons conclure que $y$ appartient à l'union de $f(A)$ et $f(B)$.
$$(y \in f(A) \text{ ou } y \in f(B)) \implies y \in f(A) \cup f(B)$$
Puisque nous avons montré que si $y \in f(A \cup B)$, alors $y \in f(A) \cup f(B)$, nous avons prouvé l'inclusion :
$$f(A \cup B) \subseteq f(A) \cup f(B)$$

##### Étape 1.2 : Démonstration de $f(A) \cup f(B) \subseteq f(A \cup B)$

Soit $y$ un élément quelconque de l'ensemble $f(A) \cup f(B)$.
Par définition de l'union, cela signifie que $y$ appartient à $f(A)$ ou $y$ appartient à $f(B)$.
$$y \in f(A) \cup f(B) \iff (y \in f(A) \text{ ou } y \in f(B))$$
Nous avons donc deux cas possibles pour cet élément $y$ :

**Cas 1 :** $y \in f(A)$.
Si $y \in f(A)$, alors par définition de l'image directe, il existe au moins un élément $x_A$ dans $A$ tel que $y = f(x_A)$.
$$y \in f(A) \implies \exists x_A \in A \text{ tel que } y = f(x_A)$$
Puisque $x_A \in A$, par définition de l'union, il est également vrai que $x_A \in A \cup B$.
$$x_A \in A \implies x_A \in A \cup B$$
Ainsi, nous avons un élément $x_A \in A \cup B$ tel que $y = f(x_A)$. Par définition de l'image directe, cela signifie que $y \in f(A \cup B)$.
$$(\exists x_A \in A \cup B \text{ tel que } y = f(x_A)) \implies y \in f(A \cup B)$$

**Cas 2 :** $y \in f(B)$.
Si $y \in f(B)$, alors par définition de l'image directe, il existe au moins un élément $x_B$ dans $B$ tel que $y = f(x_B)$.
$$y \in f(B) \implies \exists x_B \in B \text{ tel que } y = f(x_B)$$
Puisque $x_B \in B$, par définition de l'union, il est également vrai que $x_B \in A \cup B$.
$$x_B \in B \implies x_B \in A \cup B$$
Ainsi, nous avons un élément $x_B \in A \cup B$ tel que $y = f(x_B)$. Par définition de l'image directe, cela signifie que $y \in f(A \cup B)$.
$$(\exists x_B \in A \cup B \text{ tel que } y = f(x_B)) \implies y \in f(A \cup B)$$

Dans les deux cas (soit $y \in f(A)$, soit $y \in f(B)$), nous avons montré que $y \in f(A \cup B)$.
Puisque nous avons montré que si $y \in f(A) \cup f(B)$, alors $y \in f(A \cup B)$, nous avons prouvé l'inclusion :
$$f(A) \cup f(B) \subseteq f(A \cup B)$$

##### Étape 1.3 : Conclusion pour la Question 1

Puisque nous avons démontré les deux inclusions $f(A \cup B) \subseteq f(A) \cup f(B)$ et $f(A) \cup f(B) \subseteq f(A \cup B)$, nous pouvons conclure que les deux ensembles sont égaux :
$$f(A \cup B) = f(A) \cup f(B)$$

#### Question 2 : Démontrer que $f^{-1}(A' \cap B') = f^{-1}(A') \cap f^{-1}(B')$

Pour démontrer cette égalité, nous allons prouver la double inclusion : $f^{-1}(A' \cap B') \subseteq f^{-1}(A') \cap f^{-1}(B')$ et $f^{-1}(A') \cap f^{-1}(B') \subseteq f^{-1}(A' \cap B')$.

##### Étape 2.1 : Démonstration de $f^{-1}(A' \cap B') \subseteq f^{-1}(A') \cap f^{-1}(B')$

Soit $x$ un élément quelconque de l'ensemble $f^{-1}(A' \cap B')$.
Par définition de l'image réciproque, cela signifie que l'image de $x$ par $f$, c'est-à-dire $f(x)$, appartient à l'ensemble $A' \cap B'$.
$$x \in f^{-1}(A' \cap B') \implies f(x) \in A' \cap B'$$
Puisque $f(x) \in A' \cap B'$, par définition de l'intersection, cela signifie que $f(x)$ appartient à $A'$ et $f(x)$ appartient à $B'$.
$$f(x) \in A' \cap B' \iff (f(x) \in A' \text{ et } f(x) \in B')$$
Nous pouvons séparer cette conjonction en deux affirmations :

1.  $f(x) \in A'$.
    Par définition de l'image réciproque, si $f(x) \in A'$, alors $x$ est un élément de $f^{-1}(A')$.
    $$f(x) \in A' \implies x \in f^{-1}(A')$$

2.  $f(x) \in B'$.
    Par définition de l'image réciproque, si $f(x) \in B'$, alors $x$ est un élément de $f^{-1}(B')$.
    $$f(x) \in B' \implies x \in f^{-1}(B')$$

Puisque $x \in f^{-1}(A')$ et $x \in f^{-1}(B')$, par définition de l'intersection, nous pouvons conclure que $x$ appartient à l'intersection de $f^{-1}(A')$ et $f^{-1}(B')$.
$$(x \in f^{-1}(A') \text{ et } x \in f^{-1}(B')) \implies x \in f^{-1}(A') \cap f^{-1}(B')$$
Puisque nous avons montré que si $x \in f^{-1}(A' \cap B')$, alors $x \in f^{-1}(A') \cap f^{-1}(B')$, nous avons prouvé l'inclusion :
$$f^{-1}(A' \cap B') \subseteq f^{-1}(A') \cap f^{-1}(B')$$

##### Étape 2.2 : Démonstration de $f^{-1}(A') \cap f^{-1}(B') \subseteq f^{-1}(A' \cap B')$

Soit $x$ un élément quelconque de l'ensemble $f^{-1}(A') \cap f^{-1}(B')$.
Par définition de l'intersection, cela signifie que $x$ appartient à $f^{-1}(A')$ et $x$ appartient à $f^{-1}(B')$.
$$x \in f^{-1}(A') \cap f^{-1}(B') \iff (x \in f^{-1}(A') \text{ et } x \in f^{-1}(B'))$$
Nous pouvons séparer cette conjonction en deux affirmations :

1.  $x \in f^{-1}(A')$.
    Par définition de l'image réciproque, si $x \in f^{-1}(A')$, alors l'image de $x$ par $f$, c'est-à-dire $f(x)$, appartient à $A'$.
    $$x \in f^{-1}(A') \implies f(x) \in A'$$

2.  $x \in f^{-1}(B')$.
    Par définition de l'image réciproque, si $x \in f^{-1}(B')$, alors l'image de $x$ par $f$, c'est-à-dire $f(x)$, appartient à $B'$.
    $$x \in f^{-1}(B') \implies f(x) \in B'$$

Puisque $f(x) \in A'$ et $f(x) \in B'$, par définition de l'intersection, nous pouvons conclure que $f(x)$ appartient à l'intersection de $A'$ et $B'$.
$$(f(x) \in A' \text{ et } f(x) \in B') \implies f(x) \in A' \cap B'$$
Enfin, si $f(x) \in A' \cap B'$, par définition de l'image réciproque, cela signifie que $x$ est un élément de $f^{-1}(A' \cap B')$.
$$f(x) \in A' \cap B' \implies x \in f^{-1}(A' \cap B')$$
Puisque nous avons montré que si $x \in f^{-1}(A') \cap f^{-1}(B')$, alors $x \in f^{-1}(A' \cap B')$, nous avons prouvé l'inclusion :
$$f^{-1}(A') \cap f^{-1}(B') \subseteq f^{-1}(A' \cap B')$$

##### Étape 2.3 : Conclusion pour la Question 2

Puisque nous avons démontré les deux inclusions $f^{-1}(A' \cap B') \subseteq f^{-1}(A') \cap f^{-1}(B')$ et $f^{-1}(A') \cap f^{-1}(B') \subseteq f^{-1}(A' \cap B')$, nous pouvons conclure que les deux ensembles sont égaux :
$$f^{-1}(A' \cap B') = f^{-1}(A') \cap f^{-1}(B')$$

---

### Liens avec l'Intelligence Artificielle

Les concepts d'images directes et réciproques d'ensembles, ainsi que leurs propriétés en relation avec les opérations ensemblistes, sont des fondations mathématiques omniprésentes en Intelligence Artificielle, bien que souvent implicites dans les applications de haut niveau.

1.  **Traitement et Transformation des Données (Feature Engineering) :**
    En IA, les données sont fréquemment transformées d'un espace à un autre (par exemple, réduction de dimensionnalité, encodage, normalisation). Une telle transformation peut être modélisée comme une application $f: E \to F$, où $E$ est l'espace des données brutes et $F$ l'espace des caractéristiques transformées.
    *   La propriété $f(A \cup B) = f(A) \cup f(B)$ signifie que si nous avons deux groupes de données $A$ et $B$ (par exemple, des images de chats et des images de chiens), l'ensemble des caractéristiques transformées pour l'ensemble combiné (chats ou chiens) est simplement l'union des caractéristiques transformées pour les chats et des caractéristiques transformées pour les chiens. Cette propriété intuitive est cruciale pour la cohérence des pipelines de traitement de données.

2.  **Classification et Reconnaissance de Formes :**
    Dans les tâches de classification, une fonction $f$ (le modèle de classification) mappe un ensemble d'entrées $E$ (par exemple, des images) à un ensemble de sorties $F$ (par exemple, des étiquettes de classe).
    *   La propriété $f^{-1}(A' \cap B') = f^{-1}(A') \cap f^{-1}(B')$ est particulièrement pertinente. Supposons que $A'$ représente l'ensemble des sorties "chat" et $B'$ l'ensemble des sorties "animal à quatre pattes". L'intersection $A' \cap B'$ serait l'ensemble des sorties "chat ET animal à quatre pattes". La propriété démontrée signifie que l'ensemble des images qui sont classées comme "chat ET animal à quatre pattes" est exactement l'intersection des images classées comme "chat" et des images classées comme "animal à quatre pattes". Cela garantit une interprétation logique et cohérente des prédictions du modèle, essentielle pour la robustesse et l'explicabilité des systèmes d'IA.

3.  **Vérification Formelle et Robustesse des Modèles :**
    Pour les systèmes d'IA critiques (véhicules autonomes, médecine), il est vital de prouver formellement certaines propriétés de leur comportement. Les identités ensemblistes comme celles-ci sont des briques de base pour des preuves plus complexes. Par exemple, pour analyser la robustesse d'un réseau de neurones face à des perturbations adverses, on pourrait étudier comment des ensembles d'entrées "sûres" (ou "dangereuses") se transforment à travers les couches du réseau, ou comment des ensembles de sorties désirées (ou indésirables) se "rétro-projettent" dans l'espace d'entrée.

4.  **Représentation des Connaissances et Raisonnement Symbolique :**
    Dans l'IA symbolique, les connaissances sont souvent représentées par des ensembles et des relations. Les opérations ensemblistes et leurs propriétés sous des transformations fonctionnelles sont fondamentales pour l'inférence logique et la manipulation de concepts. Par exemple, si "mammifère" est un ensemble $A'$ et "carnivore" est un ensemble $B'$, alors "mammifère carnivore" est $A' \cap B'$. Comprendre comment les fonctions (relations) interagissent avec ces ensembles est au cœur du raisonnement automatique.

En somme, ces propriétés fondamentales de la théorie des ensembles et des fonctions, bien que simples en apparence, sont les piliers logiques qui sous-tendent la capacité des systèmes d'IA à traiter, transformer et interpréter des informations de manière cohérente et prévisible.
