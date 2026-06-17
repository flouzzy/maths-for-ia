# Exercice 4/10 : Jalon 5 - Applications, injections, surjections, bijections et composition de fonctions

**Niveau de difficulté :** ★★☆☆☆

---

## Énoncé

Soient $E$, $F$ et $G$ trois ensembles non vides.
Soient $f: F \to G$ et $g: E \to F$ deux applications.

Démontrer l'implication suivante :
$$ (f \circ g \text{ est injective}) \implies (g \text{ est injective}) $$

---

## Analyse de l'énoncé

Cet exercice nous demande de prouver une propriété fondamentale de la composition d'applications concernant l'injectivité. Nous sommes dans un cadre purement abstrait, où les ensembles $E, F, G$ et les applications $f, g$ ne sont pas spécifiés au-delà de leurs types.

**Rappel des définitions clés :**

1.  **Application $h: A \to B$ :** Pour tout élément $a \in A$, il existe un unique élément $b \in B$ tel que $h(a) = b$.
2.  **Application $h: A \to B$ injective :** Pour tous $a_1, a_2 \in A$, si $h(a_1) = h(a_2)$, alors $a_1 = a_2$. Autrement dit, des éléments distincts de l'ensemble de départ sont toujours envoyés sur des éléments distincts de l'ensemble d'arrivée.
3.  **Application composée $f \circ g : E \to G$ :** Pour tout $x \in E$, $(f \circ g)(x) = f(g(x))$. L'application $g$ est appliquée en premier, puis $f$ est appliquée au résultat de $g$.

**Ce que l'on nous donne (hypothèse) :**
L'application $f \circ g: E \to G$ est injective.
Cela signifie que pour tous $x_1, x_2 \in E$, si $(f \circ g)(x_1) = (f \circ g)(x_2)$, alors $x_1 = x_2$.

**Ce que l'on doit démontrer (conclusion) :**
L'application $g: E \to F$ est injective.
Cela signifie que pour tous $x_1, x_2 \in E$, si $g(x_1) = g(x_2)$, alors $x_1 = x_2$.

**Stratégie de démonstration :**
Pour prouver que $g$ est injective, nous devons partir de l'hypothèse $g(x_1) = g(x_2)$ pour des éléments arbitraires $x_1, x_2 \in E$, et en déduire que $x_1 = x_2$. L'information cruciale à utiliser sera l'injectivité de $f \circ g$.

---

## Correction exhaustive "pas-à-pas"

Soient $E$, $F$ et $G$ trois ensembles non vides.
Soient $f: F \to G$ et $g: E \to F$ deux applications.

Nous voulons démontrer que si $f \circ g$ est injective, alors $g$ est injective.

**Étape 1 : Rappel des définitions formelles.**

*   L'application composée $f \circ g$ est définie pour tout $x \in E$ par $(f \circ g)(x) = f(g(x))$. Son ensemble de départ est $E$ et son ensemble d'arrivée est $G$.
*   L'hypothèse que $f \circ g$ est injective signifie que :
    Pour tous $x_1, x_2 \in E$, si $(f \circ g)(x_1) = (f \circ g)(x_2)$, alors $x_1 = x_2$.
*   La conclusion que nous voulons atteindre est que $g$ est injective, ce qui signifie que :
    Pour tous $x_1, x_2 \in E$, si $g(x_1) = g(x_2)$, alors $x_1 = x_2$.

**Étape 2 : Début de la démonstration de l'injectivité de $g$.**

Pour démontrer que $g$ est injective, nous devons prendre deux éléments arbitraires $x_1$ et $x_2$ dans l'ensemble de départ de $g$, qui est $E$, et supposer que leurs images par $g$ sont égales. Ensuite, nous devrons montrer que cela implique que $x_1$ et $x_2$ sont en fait le même élément.

Soient $x_1 \in E$ et $x_2 \in E$ deux éléments quelconques.
Supposons que $g(x_1) = g(x_2)$.

**Étape 3 : Application de $f$ et utilisation de l'hypothèse d'injectivité de $f \circ g$.**

Puisque $g(x_1)$ et $g(x_2)$ sont des éléments de l'ensemble $F$ (l'ensemble d'arrivée de $g$ et l'ensemble de départ de $f$), et que nous avons supposé qu'ils sont égaux, nous pouvons appliquer l'application $f$ à ces deux images égales.

Appliquons $f$ aux deux membres de l'égalité $g(x_1) = g(x_2)$ :
$$ f(g(x_1)) = f(g(x_2)) $$

Par définition de la composition d'applications, nous savons que $f(g(x_1)) = (f \circ g)(x_1)$ et $f(g(x_2)) = (f \circ g)(x_2)$.
Donc, l'égalité précédente peut être réécrite comme :
$$ (f \circ g)(x_1) = (f \circ g)(x_2) $$

À ce stade, nous avons établi que si $g(x_1) = g(x_2)$, alors $(f \circ g)(x_1) = (f \circ g)(x_2)$.
Or, l'hypothèse de l'énoncé est que l'application $f \circ g$ est injective.
Par définition de l'injectivité de $f \circ g$, si $(f \circ g)(x_1) = (f \circ g)(x_2)$, alors cela implique que les éléments de départ $x_1$ et $x_2$ doivent être égaux.
Donc, en utilisant l'injectivité de $f \circ g$, nous déduisons :
$$ x_1 = x_2 $$

**Étape 4 : Conclusion.**

Nous avons commencé par supposer que $g(x_1) = g(x_2)$ pour des $x_1, x_2 \in E$ arbitraires, et nous avons logiquement déduit que $x_1 = x_2$.
Ceci correspond précisément à la définition de l'injectivité de l'application $g$.

Par conséquent, nous avons démontré que si $f \circ g$ est injective, alors $g$ est injective.

---

## Liens avec l'Intelligence Artificielle

Le concept d'injectivité et de composition de fonctions est fondamental en Intelligence Artificielle, en particulier dans le domaine de l'apprentissage profond (Deep Learning).

1.  **Réseaux de Neurones comme Compositions de Fonctions :**
    Un réseau de neurones profond est intrinsèquement une composition de fonctions. Chaque couche du réseau peut être vue comme une application $f_i: \mathbb{R}^{d_i} \to \mathbb{R}^{d_{i+1}}$, où $d_i$ est la dimension de l'espace d'entrée de la couche $i$. Un réseau de $L$ couches est alors la composition $F = f_L \circ f_{L-1} \circ \dots \circ f_1$.
    L'injectivité de la composition $f \circ g$ implique l'injectivité de $g$ est une propriété cruciale ici. Si la première couche ($g$) d'un réseau de neurones n'est pas injective, elle "fusionne" des informations distinctes dès le début. Aucune couche subséquente ($f$) ne pourra "dé-fusionner" ces informations, car l'information perdue est irrécupérable.

2.  **Préservation de l'Information et Représentations Latentes :**
    Dans des architectures comme les auto-encodeurs, l'objectif est d'apprendre une représentation latente (un encodage) des données d'entrée. L'encodeur $g: \text{Données} \to \text{Latent}$ cherche à compresser l'information. Le décodeur $f: \text{Latent} \to \text{Données}$ tente de reconstruire l'entrée à partir de la représentation latente.
    Si l'encodeur $g$ n'est pas injectif, cela signifie que différentes données d'entrée peuvent être mappées à la même représentation latente. Dans ce cas, même un décodeur parfait $f$ ne pourrait pas reconstruire l'entrée originale de manière unique, car il y aurait une ambiguïté sur quelle entrée originale correspond à cette représentation latente.
    La propriété démontrée ici signifie que si l'auto-encodeur complet ($f \circ g$) est capable de reconstruire l'entrée de manière unique (ce qui est une forme d'injectivité si l'on considère l'identité comme la fonction cible), alors l'encodeur $g$ lui-même doit avoir été injectif pour ne pas perdre d'information essentielle.

3.  **Fonctions de Hachage et Collisions :**
    Bien que les fonctions de hachage ne soient généralement pas injectives (elles sont conçues pour mapper un grand espace d'entrée à un espace de sortie plus petit, entraînant des "collisions"), le concept est pertinent. Si une fonction de hachage $g$ est utilisée comme première étape d'un processus, et qu'elle n'est pas injective, alors toute fonction $f$ appliquée ensuite à la sortie de $g$ ne pourra pas distinguer les entrées originales qui ont produit la même valeur de hachage. L'injectivité de $g$ est une condition nécessaire pour la préservation de la distinction des entrées à travers une composition.

En résumé, cette propriété mathématique souligne l'importance de l'injectivité des premières étapes d'un pipeline de traitement de l'information (comme un réseau de neurones) pour garantir que l'information pertinente n'est pas perdue prématurément, ce qui limiterait la capacité des étapes ultérieures à accomplir leur tâche.
