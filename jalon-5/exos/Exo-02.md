# Jalon 5 : Applications, injections, surjections, bijections et composition de fonctions

## Exercice 2/10 : Injectivité et Surjectivité de Fonctions Réelles Simples

**Niveau de difficulté :** $\star \text{ (1 étoile sur 5)}$

### Énoncé

Soient les fonctions suivantes :

1.  $f_1: \mathbb{R} \to \mathbb{R}$ définie par $f_1(x) = ax+b$, où $a, b \in \mathbb{R}$ et $a \neq 0$.
2.  $f_2: \mathbb{R} \to \mathbb{R}$ définie par $f_2(x) = x^2$.
3.  $f_3: \mathbb{R} \to \mathbb{R}$ définie par $f_3(x) = e^x$.

Pour chacune de ces fonctions, déterminez si elle est injective, surjective, les deux (bijective), ou aucune des deux. Justifiez rigoureusement vos réponses.

### Analyse de l'énoncé

Cet exercice vise à consolider la compréhension des définitions d'injectivité et de surjectivité pour des fonctions réelles élémentaires. Il s'agit d'appliquer directement les définitions formelles :

*   **Injectivité :** Une fonction $f: E \to F$ est injective si et seulement si pour tout $x_1, x_2 \in E$, si $f(x_1) = f(x_2)$, alors $x_1 = x_2$. Autrement dit, chaque élément de l'ensemble d'arrivée est l'image d'au plus un élément de l'ensemble de départ.
*   **Surjectivité :** Une fonction $f: E \to F$ est surjective si et seulement si pour tout $y \in F$, il existe au moins un $x \in E$ tel que $f(x) = y$. Autrement dit, chaque élément de l'ensemble d'arrivée est l'image d'au moins un élément de l'ensemble de départ. L'ensemble image $f(E)$ est égal à l'ensemble d'arrivée $F$.

Pour prouver l'injectivité, on part de l'hypothèse $f(x_1) = f(x_2)$ pour des éléments arbitraires $x_1, x_2$ du domaine $E$, et on cherche à déduire $x_1 = x_2$. Pour prouver la non-injectivité, il suffit de trouver un contre-exemple : deux éléments distincts $x_1 \neq x_2$ dans $E$ qui ont la même image $f(x_1) = f(x_2)$.

Pour prouver la surjectivité, on prend un $y$ arbitraire dans l'ensemble d'arrivée $F$ et on cherche à résoudre l'équation $f(x) = y$ pour $x \in E$. Si une solution $x$ existe et appartient à $E$ pour tout $y \in F$, la fonction est surjective. Pour prouver la non-surjectivité, on cherche un contre-exemple : un élément $y \in F$ pour lequel l'équation $f(x) = y$ n'a aucune solution dans $E$.

La difficulté est faible car les fonctions sont bien connues et les manipulations algébriques sont simples. L'accent est mis sur la rigueur de la démonstration et la bonne application des définitions.

### Correction exhaustive pas-à-pas

Appliquons les définitions à chaque fonction.

#### 1. Fonction $f_1: \mathbb{R} \to \mathbb{R}$ définie par $f_1(x) = ax+b$, avec $a, b \in \mathbb{R}$ et $a \neq 0$.

##### Injectivité de $f_1$

Pour prouver l'injectivité, nous devons montrer que pour tout $x_1, x_2 \in \mathbb{R}$, si $f_1(x_1) = f_1(x_2)$, alors $x_1 = x_2$.

Soient $x_1, x_2 \in \mathbb{R}$ tels que $f_1(x_1) = f_1(x_2)$.
Par définition de $f_1$, l'égalité des images s'écrit :
$$ax_1 + b = ax_2 + b$$
Pour isoler les termes en $x$, nous soustrayons $b$ des deux côtés de l'équation :
$$ax_1 + b - b = ax_2 + b - b$$
$$ax_1 = ax_2$$
Puisque l'énoncé spécifie que $a \neq 0$, nous pouvons diviser les deux côtés de l'équation par $a$ :
$$\frac{ax_1}{a} = \frac{ax_2}{a}$$
$$x_1 = x_2$$
Nous avons démontré que si $f_1(x_1) = f_1(x_2)$, alors $x_1 = x_2$.
Par conséquent, la fonction $f_1$ est injective.

##### Surjectivité de $f_1$

Pour prouver la surjectivité, nous devons montrer que pour tout $y \in \mathbb{R}$ (l'ensemble d'arrivée), il existe au moins un $x \in \mathbb{R}$ (l'ensemble de départ) tel que $f_1(x) = y$.

Soit $y \in \mathbb{R}$ un élément arbitraire de l'ensemble d'arrivée. Nous cherchons à trouver un $x \in \mathbb{R}$ tel que $f_1(x) = y$.
Par définition de $f_1$, cela revient à résoudre l'équation suivante pour $x$ :
$$ax + b = y$$
Pour isoler $x$, nous soustrayons $b$ des deux côtés de l'équation :
$$ax + b - b = y - b$$
$$ax = y - b$$
Puisque $a \neq 0$, nous pouvons diviser les deux côtés par $a$ :
$$x = \frac{y - b}{a}$$
Étant donné que $y \in \mathbb{R}$, $b \in \mathbb{R}$ et $a \in \mathbb{R}$ avec $a \neq 0$, la valeur $x = \frac{y - b}{a}$ est un nombre réel bien défini.
Ainsi, pour tout $y \in \mathbb{R}$, nous avons trouvé un $x \in \mathbb{R}$ tel que $f_1(x) = y$.
Par conséquent, la fonction $f_1$ est surjective.

##### Conclusion pour $f_1$

Puisque $f_1$ est à la fois injective et surjective, $f_1$ est une fonction bijective.

#### 2. Fonction $f_2: \mathbb{R} \to \mathbb{R}$ définie par $f_2(x) = x^2$.

##### Injectivité de $f_2$

Pour prouver la non-injectivité, nous devons trouver deux éléments distincts $x_1, x_2 \in \mathbb{R}$ tels que $f_2(x_1) = f_2(x_2)$.

Considérons les valeurs $x_1 = 2$ et $x_2 = -2$.
Ces deux éléments appartiennent à l'ensemble de départ $\mathbb{R}$ et sont distincts : $x_1 \neq x_2$ car $2 \neq -2$.
Calculons leurs images sous la fonction $f_2$:
$f_2(x_1) = f_2(2) = (2)^2 = 4$.
$f_2(x_2) = f_2(-2) = (-2)^2 = 4$.
Nous observons que $f_2(2) = f_2(-2)$ alors que $2 \neq -2$.
Par conséquent, la fonction $f_2$ n'est pas injective.

##### Surjectivité de $f_2$

Pour prouver la non-surjectivité, nous devons trouver un élément $y \in \mathbb{R}$ (l'ensemble d'arrivée) pour lequel il n'existe aucun $x \in \mathbb{R}$ (l'ensemble de départ) tel que $f_2(x) = y$.

Soit $y \in \mathbb{R}$ un élément arbitraire. Nous cherchons $x \in \mathbb{R}$ tel que $f_2(x) = y$.
Par définition de $f_2$, cela revient à résoudre l'équation :
$$x^2 = y$$
Nous savons que le carré de tout nombre réel est toujours un nombre réel positif ou nul. C'est-à-dire, pour tout $x \in \mathbb{R}$, $x^2 \ge 0$.
Considérons un $y$ strictement négatif, par exemple $y = -1$.
L'équation devient $x^2 = -1$.
Il n'existe aucun nombre réel $x$ dont le carré est égal à $-1$.
Par conséquent, pour $y = -1 \in \mathbb{R}$, il n'existe aucun $x \in \mathbb{R}$ tel que $f_2(x) = -1$.
Par conséquent, la fonction $f_2$ n'est pas surjective.

##### Conclusion pour $f_2$

Puisque $f_2$ n'est ni injective ni surjective, $f_2$ n'est pas une bijection.

#### 3. Fonction $f_3: \mathbb{R} \to \mathbb{R}$ définie par $f_3(x) = e^x$.

##### Injectivité de $f_3$

Pour prouver l'injectivité, nous devons montrer que pour tout $x_1, x_2 \in \mathbb{R}$, si $f_3(x_1) = f_3(x_2)$, alors $x_1 = x_2$.

Soient $x_1, x_2 \in \mathbb{R}$ tels que $f_3(x_1) = f_3(x_2)$.
Par définition de $f_3$, l'égalité des images s'écrit :
$$e^{x_1} = e^{x_2}$$
Pour résoudre cette équation, nous pouvons appliquer la fonction logarithme népérien (ln) aux deux côtés. La fonction ln est bien définie pour les nombres strictement positifs, et la fonction exponentielle $e^x$ est toujours strictement positive pour tout $x \in \mathbb{R}$.
$$\ln(e^{x_1}) = \ln(e^{x_2})$$
En utilisant la propriété fondamentale des logarithmes $\ln(e^u) = u$ pour tout $u \in \mathbb{R}$ :
$$x_1 = x_2$$
Nous avons démontré que si $f_3(x_1) = f_3(x_2)$, alors $x_1 = x_2$.
Par conséquent, la fonction $f_3$ est injective.

##### Surjectivité de $f_3$

Pour prouver la non-surjectivité, nous devons trouver un élément $y \in \mathbb{R}$ (l'ensemble d'arrivée) pour lequel il n'existe aucun $x \in \mathbb{R}$ (l'ensemble de départ) tel que $f_3(x) = y$.

Soit $y \in \mathbb{R}$ un élément arbitraire. Nous cherchons $x \in \mathbb{R}$ tel que $f_3(x) = y$.
Par définition de $f_3$, cela revient à résoudre l'équation :
$$e^x = y$$
Nous savons que la fonction exponentielle $e^x$ est toujours strictement positive pour tout $x \in \mathbb{R}$. C'est-à-dire, pour tout $x \in \mathbb{R}$, $e^x > 0$.
Considérons un $y$ négatif ou nul, par exemple $y = 0$.
L'équation devient $e^x = 0$. Il n'existe aucun nombre réel $x$ tel que $e^x = 0$.
De même, si nous prenons $y = -5$, l'équation devient $e^x = -5$. Il n'existe aucun nombre réel $x$ tel que $e^x = -5$, car $e^x$ doit toujours être positif.
Par conséquent, pour tout $y \in \mathbb{R}$ tel que $y \le 0$, il n'existe aucun $x \in \mathbb{R}$ tel que $f_3(x) = y$.
Par exemple, pour $y = -10 \in \mathbb{R}$, il n'existe aucun $x \in \mathbb{R}$ tel que $f_3(x) = -10$.
Par conséquent, la fonction $f_3$ n'est pas surjective.

##### Conclusion pour $f_3$

Puisque $f_3$ est injective mais n'est pas surjective, $f_3$ n'est pas une bijection.

### Liens avec l'Intelligence Artificielle

Les concepts d'injectivité et de surjectivité, bien que fondamentaux en mathématiques pures, trouvent des échos significatifs dans plusieurs domaines de l'Intelligence Artificielle, notamment en traitement de données, en apprentissage automatique et en cryptographie.

1.  **Représentations et Encodages :** En IA, les données brutes sont souvent transformées en représentations numériques (encodages) pour être traitées par des algorithmes. Une fonction d'encodage idéale est injective. Si un encodage n'est pas injectif (comme $f_2(x)=x^2$ où $2$ et $-2$ sont mappés à $4$), cela signifie que différentes entrées peuvent produire la même représentation. Cela peut entraîner une perte d'information ou une ambiguïté, rendant impossible de distinguer les entrées originales. Par exemple, dans l'encodage de mots (word embeddings), on souhaite que des mots sémantiquement distincts aient des représentations distinctes.

2.  **Fonctions de Hachage :** Les fonctions de hachage sont utilisées pour mapper des données de taille arbitraire à des valeurs de taille fixe. Elles sont cruciales pour les tables de hachage, la vérification d'intégrité et la cryptographie. Idéalement, une fonction de hachage devrait être "quasi-injective" pour minimiser les collisions (où différentes entrées produisent la même sortie). Bien qu'il soit impossible d'avoir une fonction de hachage parfaitement injective pour des domaines potentiellement infinis vers des codomaines finis, l'objectif est de s'en approcher le plus possible pour garantir l'unicité des identifiants ou la robustesse des signatures numériques.

3.  **Compression de Données :** Les algorithmes de compression de données visent à réduire la taille des données. Une compression "sans perte" est une fonction qui est bijective de l'ensemble des données originales vers l'ensemble des données compressées. Cela garantit que les données originales peuvent être entièrement reconstruites à partir des données compressées, ce qui implique que la fonction de compression doit être injective (pas de perte d'information) et surjective (toutes les données compressées peuvent être décompressées).

4.  **Modèles Génératifs (GANs, VAEs) :** Dans les modèles génératifs, on cherche à générer de nouvelles données (images, textes, etc.) à partir d'un espace latent de variables aléatoires. La "qualité" de la génération peut être liée à la capacité de la fonction de génération (le générateur) à couvrir l'espace des données réelles (surjectivité) et à produire des échantillons variés et non redondants (injectivité dans l'espace latent). Un générateur qui n'est pas suffisamment surjectif pourrait souffrir de "mode collapse", où il ne génère qu'une petite variété d'échantillons.

5.  **Fonctions d'Activation dans les Réseaux de Neurones :** Bien que l'injectivité et la surjectivité ne soient pas des critères directs pour les fonctions d'activation (comme ReLU, Sigmoid, Tanh), la compréhension de leur comportement sur leur domaine et codomaine est essentielle. Par exemple, la fonction sigmoïde mappe $\mathbb{R}$ à $(0,1)$, elle est injective mais pas surjective sur $\mathbb{R}$. Cela signifie qu'elle compresse l'information dans un intervalle borné, ce qui peut être utile pour la normalisation mais peut aussi entraîner une perte de gradient pour des entrées très grandes ou très petites.

En somme, la compréhension des propriétés d'injectivité et de surjectivité permet d'évaluer la fidélité, la réversibilité et la couverture des transformations de données, des concepts cruciaux pour la conception et l'analyse des algorithmes d'Intelligence Artificielle.
