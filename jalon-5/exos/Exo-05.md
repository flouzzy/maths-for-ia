# Exercice 5/10 : Jalon 5 - Applications, injections, surjections, bijections et composition de fonctions

**Professeur Émérite :** Chers étudiantes et étudiants, abordons aujourd'hui un résultat fondamental concernant la surjectivité et la composition de fonctions. Ce type de démonstration abstraite est essentiel pour développer une intuition solide en algèbre et en analyse, et pour comprendre la structure des transformations.

---

### Énoncé de l'Exercice (Difficulté : ★★★☆☆)

Soient $E$, $F$ et $G$ trois ensembles non vides.
Considérons deux fonctions :
*   $g: E \to F$
*   $f: F \to G$

On suppose que la fonction composée $f \circ g: E \to G$ est surjective.

Démontrez rigoureusement que la fonction $f: F \to G$ est surjective.

---

### Analyse de l'Énoncé

Cet exercice nous demande de prouver une implication : si la composition de deux fonctions est surjective, alors la seconde fonction (celle qui est appliquée en dernier) doit nécessairement être surjective.

1.  **Comprendre la surjectivité :**
    *   Une fonction $h: A \to B$ est dite surjective si et seulement si pour tout élément $b$ de l'ensemble d'arrivée $B$, il existe au moins un élément $a$ de l'ensemble de départ $A$ tel que $h(a) = b$. En d'autres termes, l'image de $h$ est égale à son ensemble d'arrivée : $\text{Im}(h) = B$.

2.  **Hypothèse :** $f \circ g: E \to G$ est surjective.
    *   Cela signifie que pour tout $z \in G$, il existe au moins un $x \in E$ tel que $(f \circ g)(x) = z$.
    *   Par définition de la composition, cela équivaut à $f(g(x)) = z$.

3.  **Conclusion à démontrer :** $f: F \to G$ est surjective.
    *   Cela signifie que pour tout $z \in G$, il existe au moins un $y \in F$ tel que $f(y) = z$.

4.  **Stratégie de démonstration :**
    *   Pour prouver que $f$ est surjective, nous devons partir d'un élément arbitraire $z$ dans l'ensemble d'arrivée de $f$ (qui est $G$).
    *   Notre objectif est de trouver un élément $y$ dans l'ensemble de départ de $f$ (qui est $F$) tel que $f(y) = z$.
    *   L'hypothèse sur la surjectivité de $f \circ g$ est notre seule source d'information. Elle nous donne un $x \in E$ tel que $f(g(x)) = z$.
    *   L'expression $f(g(x)) = z$ contient déjà la forme $f(\text{quelque chose}) = z$. Le "quelque chose" est $g(x)$.
    *   Si nous posons $y = g(x)$, alors $y$ est un élément de $F$ (car $g: E \to F$) et nous aurons $f(y) = z$. C'est précisément ce que nous cherchons !

---

### Correction Exhaustive Pas-à-Pas

Pour démontrer que $f: F \to G$ est surjective, nous devons montrer que pour tout élément $z$ de l'ensemble d'arrivée $G$, il existe au moins un élément $y$ de l'ensemble de départ $F$ tel que $f(y) = z$.

1.  **Initialisation :** Soit $z$ un élément quelconque et arbitrairement choisi de l'ensemble $G$. Notre but est de trouver un $y \in F$ tel que $f(y) = z$.

2.  **Utilisation de l'hypothèse :** Nous savons par hypothèse que la fonction composée $f \circ g: E \to G$ est surjective.
    *   Par définition de la surjectivité, cela signifie que pour tout élément de l'ensemble d'arrivée $G$, il existe au moins un élément dans l'ensemble de départ $E$ qui lui est appliqué.
    *   Puisque $z \in G$ (choisi à l'étape 1), il existe donc au moins un élément $x_0 \in E$ tel que $(f \circ g)(x_0) = z$.

3.  **Décomposition de la composition :** Par définition de la composition de fonctions, l'expression $(f \circ g)(x_0)$ est équivalente à $f(g(x_0))$.
    *   En substituant cette équivalence dans l'équation de l'étape 2, nous obtenons :
        $$f(g(x_0)) = z$$

4.  **Identification du candidat pour $y$ :** Nous cherchons un élément $y \in F$ tel que $f(y) = z$. L'équation $f(g(x_0)) = z$ nous fournit directement un tel candidat.
    *   Posons $y_0 = g(x_0)$.

5.  **Vérification de l'appartenance de $y_0$ à $F$ :** La fonction $g$ est définie comme $g: E \to F$.
    *   Puisque $x_0 \in E$, l'image de $x_0$ par $g$, qui est $y_0 = g(x_0)$, est nécessairement un élément de l'ensemble $F$.
    *   Donc, $y_0 \in F$.

6.  **Vérification de la condition $f(y_0) = z$ :** En substituant $y_0$ dans l'équation de l'étape 3, nous obtenons :
    *   $f(y_0) = z$.

7.  **Conclusion :** Nous avons démontré que pour tout $z \in G$ (choisi arbitrairement au début), il existe un élément $y_0 \in F$ (spécifiquement $y_0 = g(x_0)$ pour un certain $x_0 \in E$) tel que $f(y_0) = z$.
    *   Ceci est précisément la définition de la surjectivité de la fonction $f: F \to G$.

Par conséquent, si la fonction composée $f \circ g$ est surjective, alors la fonction $f$ est surjective.

---

### Liens avec l'Intelligence Artificielle

Le concept de surjectivité et de composition de fonctions est omniprésent en Intelligence Artificielle, particulièrement dans le domaine de l'apprentissage profond (Deep Learning).

1.  **Réseaux de Neurones comme Compositions de Fonctions :**
    *   Un réseau de neurones est fondamentalement une composition de fonctions. Chaque couche du réseau peut être vue comme une fonction $f_i: H_{i-1} \to H_i$, où $H_{i-1}$ et $H_i$ sont les espaces des activations de la couche précédente et de la couche actuelle, respectivement.
    *   Le réseau entier est alors une fonction composée $F = f_L \circ f_{L-1} \circ \dots \circ f_1: X \to Y$, où $X$ est l'espace d'entrée et $Y$ est l'espace de sortie.
    *   Dans notre exercice, $g$ pourrait représenter les premières couches du réseau ($f_{L-1} \circ \dots \circ f_1$), et $f$ la dernière couche (ou les dernières couches) du réseau ($f_L$).

2.  **Surjectivité et Capacité Représentative :**
    *   Si le réseau global $F = f \circ g$ est capable de produire n'importe quelle sortie désirée dans l'espace $G$ (c'est-à-dire qu'il est "surjectif" sur l'espace des cibles), alors notre démonstration implique que la dernière partie du réseau, $f$, doit elle-même être surjective.
    *   Cela signifie que la couche de sortie (ou le "head" du modèle) doit avoir une capacité suffisante pour mapper les représentations internes (les "features" produites par $g$) à l'ensemble complet des sorties possibles. Si $f$ n'était pas surjective, il existerait des sorties cibles que le réseau ne pourrait jamais atteindre, peu importe la qualité des représentations générées par $g$.

3.  **Modèles Génératifs (GANs, VAEs) :**
    *   Dans les modèles génératifs, comme les Generative Adversarial Networks (GANs) ou les Variational Autoencoders (VAEs), le générateur $G$ est une fonction qui mappe un espace latent $Z$ (souvent un bruit aléatoire) vers l'espace des données réelles $X$. L'objectif est que $G$ soit "surjectif" sur la variété des données réelles, c'est-à-dire qu'il puisse générer n'importe quelle donnée réaliste.
    *   Si le générateur $G$ est lui-même un réseau profond, $G = G_k \circ \dots \circ G_1$, alors la surjectivité de l'ensemble $G$ implique que la dernière couche $G_k$ doit être capable de couvrir l'espace des données. Si $G_k$ est trop restrictive, le modèle ne pourra pas générer toute la diversité des données, même si les couches précédentes ont appris des représentations latentes riches.

4.  **Implications pour la Conception de Modèles :**
    *   Ce théorème souligne l'importance de la conception de la couche de sortie. Si l'on sait que le problème requiert une couverture complète de l'espace de sortie (par exemple, classification multi-classes où toutes les classes sont possibles, ou génération d'images avec une grande diversité), alors la fonction de la dernière couche doit être choisie de manière à être potentiellement surjective.
    *   Par exemple, pour une classification, une couche `softmax` est souvent utilisée, qui peut en principe produire n'importe quelle distribution de probabilité sur les classes, permettant ainsi à la fonction $f$ d'être "surjective" sur l'espace des distributions de probabilité.

En somme, ce résultat mathématique simple a des répercussions profondes sur la compréhension de la capacité et des limitations des architectures d'apprentissage profond, en soulignant que la "puissance" de la transformation finale est cruciale pour la capacité globale du système à atteindre toutes les cibles possibles.
