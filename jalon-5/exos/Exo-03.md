# Exercice 3/10 - Jalon 5 : Composition et propriétés des fonctions

**Niveau de difficulté :** $\star\star$

---

### Énoncé

Soient les fonctions $f$ et $g$ définies comme suit :
*   $f: \mathbb{R} \to \mathbb{R}$, donnée par $f(x) = x-1$.
*   $g: \mathbb{R} \to \mathbb{R}$, donnée par $g(x) = x^2$.

On considère la fonction composée $h = g \circ f$.

1.  Déterminer l'expression explicite de la fonction $h(x)$. Préciser rigoureusement son ensemble de départ et son ensemble d'arrivée.
2.  Étudier l'injectivité de la fonction $h$. Justifier votre réponse de manière exhaustive.
3.  Étudier la surjectivité de la fonction $h$. Justifier votre réponse de manière exhaustive.

---

### Analyse de l'énoncé

Cet exercice vise à évaluer la compréhension des concepts fondamentaux de composition de fonctions, d'injectivité et de surjectivité.

1.  **Composition de fonctions ($h = g \circ f$) :** Il s'agit d'appliquer la fonction $f$ en premier, puis la fonction $g$ au résultat de $f$. La définition formelle $(g \circ f)(x) = g(f(x))$ sera utilisée. Il est crucial de vérifier que les ensembles de définition et d'arrivée sont compatibles pour que la composition soit bien définie. Ici, l'ensemble d'arrivée de $f$ est $\mathbb{R}$, qui est aussi l'ensemble de départ de $g$, donc la composition est bien définie sur $\mathbb{R}$. L'ensemble de départ de $h$ sera celui de $f$, et l'ensemble d'arrivée de $h$ sera celui de $g$.
2.  **Injectivité :** Une fonction $\phi: E \to F$ est injective si et seulement si pour tout $x_1, x_2 \in E$, l'égalité $\phi(x_1) = \phi(x_2)$ implique $x_1 = x_2$. Pour prouver qu'une fonction n'est *pas* injective, il suffit de trouver un contre-exemple, c'est-à-dire deux éléments distincts $x_1 \neq x_2$ dans l'ensemble de départ qui ont la même image par $\phi$.
3.  **Surjectivité :** Une fonction $\phi: E \to F$ est surjective si et seulement si pour tout $y \in F$ (l'ensemble d'arrivée), il existe au moins un $x \in E$ (l'ensemble de départ) tel que $\phi(x) = y$. Pour prouver qu'une fonction n'est *pas* surjective, il suffit de trouver un élément $y_0$ dans l'ensemble d'arrivée $F$ pour lequel il n'existe aucun $x$ dans l'ensemble de départ $E$ tel que $\phi(x) = y_0$.

Les fonctions $f$ et $g$ sont des fonctions polynomiales simples. La fonction $f(x) = x-1$ est une translation, qui est bijective. La fonction $g(x) = x^2$ est une fonction quadratique, qui n'est ni injective ni surjective sur $\mathbb{R}$. La composition de ces deux fonctions devrait hériter des propriétés de la fonction quadratique en termes d'injectivité et de surjectivité.

---

### Correction exhaustive pas-à-pas

#### Question 1 : Déterminer l'expression explicite de $h(x)$ et préciser ses ensembles.

Soient les fonctions :
*   $f: \mathbb{R} \to \mathbb{R}$, définie par $f(x) = x-1$.
*   $g: \mathbb{R} \to \mathbb{R}$, définie par $g(x) = x^2$.

Nous cherchons la fonction composée $h = g \circ f$.

**Étape 1 : Vérification de la compatibilité des ensembles.**
L'ensemble d'arrivée de $f$ est $\mathbb{R}$.
L'ensemble de départ de $g$ est $\mathbb{R}$.
Puisque l'ensemble d'arrivée de $f$ est égal à l'ensemble de départ de $g$ ($\mathbb{R} = \mathbb{R}$), la composition $g \circ f$ est bien définie.

**Étape 2 : Détermination des ensembles de départ et d'arrivée de $h$.**
L'ensemble de départ de $h = g \circ f$ est l'ensemble de départ de $f$, qui est $\mathbb{R}$.
L'ensemble d'arrivée de $h = g \circ f$ est l'ensemble d'arrivée de $g$, qui est $\mathbb{R}$.
Ainsi, $h: \mathbb{R} \to \mathbb{R}$.

**Étape 3 : Calcul de l'expression explicite de $h(x)$.**
Par définition de la composition de fonctions, pour tout $x \in \mathbb{R}$ :
$$h(x) = (g \circ f)(x) = g(f(x))$$
Nous substituons l'expression de $f(x)$ dans $g$:
$$h(x) = g(x-1)$$
Maintenant, nous appliquons la définition de $g$, qui est $g(u) = u^2$ pour tout $u \in \mathbb{R}$. Ici, $u = x-1$.
$$h(x) = (x-1)^2$$
Pour une expression développée, nous pouvons utiliser l'identité remarquable $(a-b)^2 = a^2 - 2ab + b^2$:
$$h(x) = x^2 - 2 \cdot x \cdot 1 + 1^2$$
$$h(x) = x^2 - 2x + 1$$

**Conclusion de la Question 1 :**
La fonction $h$ est définie par $h: \mathbb{R} \to \mathbb{R}$, et son expression explicite est $h(x) = (x-1)^2$ (ou $h(x) = x^2 - 2x + 1$).

#### Question 2 : Étudier l'injectivité de la fonction $h$.

Pour étudier l'injectivité de $h: \mathbb{R} \to \mathbb{R}$ définie par $h(x) = (x-1)^2$, nous devons vérifier si pour tout $x_1, x_2 \in \mathbb{R}$, l'égalité $h(x_1) = h(x_2)$ implique $x_1 = x_2$.

**Étape 1 : Poser l'hypothèse d'égalité des images.**
Soient $x_1, x_2 \in \mathbb{R}$ tels que $h(x_1) = h(x_2)$.
Ceci signifie :
$$(x_1-1)^2 = (x_2-1)^2$$

**Étape 2 : Résoudre l'équation pour $x_1$ et $x_2$.**
L'équation $A^2 = B^2$ est équivalente à $A = B$ ou $A = -B$.
Donc, nous avons deux cas possibles :
*   **Cas 1 :** $x_1-1 = x_2-1$
    En ajoutant $1$ aux deux membres de l'équation, nous obtenons :
    $x_1 = x_2$
    Ce cas correspond à la condition d'injectivité.

*   **Cas 2 :** $x_1-1 = -(x_2-1)$
    $x_1-1 = -x_2+1$
    En ajoutant $1$ aux deux membres de l'équation :
    $x_1 = -x_2+2$

**Étape 3 : Chercher un contre-exemple (si la fonction n'est pas injective).**
Le Cas 2 montre qu'il est possible d'avoir $h(x_1) = h(x_2)$ sans que $x_1 = x_2$.
Pour prouver que $h$ n'est pas injective, il suffit de trouver un exemple concret de $x_1 \neq x_2$ tels que $h(x_1) = h(x_2)$.
Choisissons une valeur pour $x_1$, par exemple $x_1 = 0$.
Alors $h(0) = (0-1)^2 = (-1)^2 = 1$.
Nous cherchons un $x_2 \neq 0$ tel que $h(x_2) = 1$.
$(x_2-1)^2 = 1$
Ceci implique $x_2-1 = 1$ ou $x_2-1 = -1$.
Si $x_2-1 = 1$, alors $x_2 = 1+1 = 2$.
Si $x_2-1 = -1$, alors $x_2 = -1+1 = 0$.
Nous avons trouvé $x_2 = 2$.
Vérifions : $h(2) = (2-1)^2 = 1^2 = 1$.
Nous avons donc $h(0) = 1$ et $h(2) = 1$.
Puisque $0 \neq 2$ mais $h(0) = h(2)$, la fonction $h$ n'est pas injective.

**Conclusion de la Question 2 :**
La fonction $h$ n'est pas injective. Par exemple, $h(0) = 1$ et $h(2) = 1$, alors que $0 \neq 2$.

#### Question 3 : Étudier la surjectivité de la fonction $h$.

Pour étudier la surjectivité de $h: \mathbb{R} \to \mathbb{R}$ définie par $h(x) = (x-1)^2$, nous devons vérifier si pour tout $y \in \mathbb{R}$ (l'ensemble d'arrivée), il existe au moins un $x \in \mathbb{R}$ (l'ensemble de départ) tel que $h(x) = y$.

**Étape 1 : Poser l'équation $h(x) = y$.**
Nous cherchons à savoir si, pour tout $y \in \mathbb{R}$, l'équation $(x-1)^2 = y$ admet au moins une solution $x \in \mathbb{R}$.

**Étape 2 : Analyser l'équation $(x-1)^2 = y$.**
Le terme $(x-1)^2$ est le carré d'un nombre réel $(x-1)$.
Par les propriétés des nombres réels, le carré de tout nombre réel est toujours supérieur ou égal à zéro.
Donc, pour tout $x \in \mathbb{R}$, nous avons $(x-1)^2 \ge 0$.
Ceci signifie que l'image de la fonction $h$ (l'ensemble des valeurs que $h(x)$ peut prendre) est l'intervalle $[0, +\infty[$.

**Étape 3 : Comparer l'image avec l'ensemble d'arrivée.**
L'ensemble d'arrivée de $h$ est $\mathbb{R}$.
L'image de $h$ est $[0, +\infty[$.
Puisque $[0, +\infty[ \neq \mathbb{R}$, la fonction $h$ n'est pas surjective.

**Étape 4 : Fournir un contre-exemple (si la fonction n'est pas surjective).**
Pour prouver que $h$ n'est pas surjective, il suffit de trouver un $y_0 \in \mathbb{R}$ tel qu'il n'existe aucun $x \in \mathbb{R}$ vérifiant $h(x) = y_0$.
Choisissons un $y_0$ qui n'est pas dans l'image de $h$, c'est-à-dire un nombre réel strictement négatif.
Par exemple, soit $y_0 = -1$.
Nous cherchons un $x \in \mathbb{R}$ tel que $h(x) = -1$.
$$(x-1)^2 = -1$$
Comme nous l'avons établi, le carré de tout nombre réel est non-négatif. Il est donc impossible qu'un carré soit égal à $-1$ dans l'ensemble des nombres réels.
L'équation $(x-1)^2 = -1$ n'admet aucune solution réelle $x$.
Par conséquent, il n'existe aucun $x \in \mathbb{R}$ tel que $h(x) = -1$.

**Conclusion de la Question 3 :**
La fonction $h$ n'est pas surjective. Par exemple, la valeur $-1$ appartient à l'ensemble d'arrivée $\mathbb{R}$, mais il n'existe aucun $x \in \mathbb{R}$ tel que $h(x) = -1$.

---

### Liens avec l'Intelligence Artificielle

Les concepts d'applications, d'injectivité, de surjectivité et de composition sont absolument fondamentaux en Intelligence Artificielle, en particulier dans le domaine de l'apprentissage profond (Deep Learning).

1.  **Composition de fonctions et Réseaux de Neurones :** Un réseau de neurones profond est, par essence, une composition de fonctions. Chaque "couche" du réseau applique une transformation (souvent une combinaison linéaire suivie d'une fonction d'activation non linéaire) aux données d'entrée. Si $L_1, L_2, \dots, L_k$ sont les fonctions représentant les couches successives d'un réseau, alors la fonction globale apprise par le réseau est $L_k \circ L_{k-1} \circ \dots \circ L_1$. Comprendre la composition est donc essentiel pour saisir comment les informations sont transformées et traitées à travers les différentes étapes d'un modèle d'IA.

2.  **Injectivité et Surjectivité dans les Modèles Génératifs :**
    *   **Modèles Génératifs (GANs, VAEs) :** Ces modèles apprennent à générer de nouvelles données (images, textes, etc.) à partir d'un "espace latent" (un espace de vecteurs de faible dimension). La fonction qui mappe l'espace latent à l'espace des données est une application complexe.
    *   **Injectivité :** Si cette application n'est pas injective, cela signifie que différents points dans l'espace latent peuvent produire la même sortie dans l'espace des données. C'est un problème connu sous le nom de "mode collapse" dans les GANs, où le générateur ne produit qu'une variété limitée d'échantillons, ignorant d'autres "modes" (types de données) de la distribution cible. Une perte d'injectivité implique une perte d'information lors de la transformation.
    *   **Surjectivité :** Si l'application de l'espace latent à l'espace des données n'est pas surjective (par rapport à la distribution de données réelles), cela signifie que le modèle ne peut pas générer certains types de données qui existent dans la distribution réelle. Le modèle ne couvre pas l'intégralité de l'espace des données, ce qui limite sa capacité à produire des échantillons diversifiés et réalistes.

3.  **Réseaux de Neurones Inversibles (Invertible Neural Networks - INN) :** Certains architectures de réseaux de neurones sont spécifiquement conçues pour être bijectives (à la fois injectives et surjectives). Ces INN sont utilisés dans des domaines comme l'estimation de densité, la compression de données sans perte, ou la génération d'images. La bijectivité garantit qu'il n'y a pas de perte d'information lors du passage à travers le réseau et que chaque sortie correspond à une entrée unique, et vice-versa. Cela permet, par exemple, de calculer la vraisemblance exacte des données, ce qui est crucial pour certaines tâches.

4.  **Représentation et Réduction de Dimension :** Lorsque l'on utilise des fonctions pour transformer des données brutes en "features" (caractéristiques) plus significatives, les propriétés d'injectivité et de surjectivité sont importantes. Une transformation non injective peut entraîner une perte d'information, où des données d'entrée distinctes sont représentées de manière identique, rendant leur discrimination impossible par la suite. La surjectivité est liée à la capacité de la représentation à capturer toutes les variations pertinentes des données originales.

En somme, une compréhension approfondie de ces concepts mathématiques permet aux chercheurs et ingénieurs en IA de concevoir, d'analyser et de diagnostiquer les comportements de modèles complexes, en particulier lorsqu'il s'agit de transformations de données et de génération de contenu.
