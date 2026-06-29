# Exercice 01 (1 $\star$) : Invariance de la Similarité Cosinus par Mise à l'Échelle Positive et son Interprétation Géométrique pour les Espaces de Plongement

## Énoncé
Soit $E = \mathbb{R}^n$ l'espace vectoriel euclidien standard, muni du produit scalaire canonique $\langle x, y \rangle = \sum_{i=1}^n x_i y_i$ pour $x=(x_1, \dots, x_n)$ et $y=(y_1, \dots, y_n)$ dans $E$. La norme euclidienne associée est $\|x\| = \sqrt{\langle x, x \rangle}$.
Soient $u$ et $v$ deux vecteurs non nuls de $E$.

1.  Définir rigoureusement la similarité cosinus $\text{sim}(u, v)$ entre les vecteurs $u$ et $v$.
2.  Soient $\alpha$ et $\beta$ deux scalaires réels strictement positifs, c'est-à-dire $\alpha \in \mathbb{R}^{+*}$ et $\beta \in \mathbb{R}^{+*}$. Démontrer que la similarité cosinus entre les vecteurs $u$ et $v$ est identique à la similarité cosinus entre les vecteurs $\alpha u$ et $\beta v$. C'est-à-dire, montrer que $\text{sim}(u, v) = \text{sim}(\alpha u, \beta v)$.
3.  Expliquer en quoi cette propriété fondamentale est cruciale pour la conception et le fonctionnement des moteurs de recherche sémantiques basés sur des espaces de plongement (embedding spaces).

## Correction Détaillée
### Analyse et Stratégie
Le problème se décompose en trois parties distinctes. Premièrement, il s'agit de rappeler la définition formelle de la similarité cosinus, qui est une mesure de l'angle entre deux vecteurs dans un espace euclidien. Deuxièmement, nous devons prouver une propriété d'invariance de cette mesure lorsque les vecteurs sont mis à l'échelle par des scalaires strictement positifs. Enfin, la troisième partie demande une interprétation de cette propriété dans le contexte spécifique des moteurs de recherche sémantiques et des espaces de plongement.

Pour la première partie, nous utiliserons la définition standard de la similarité cosinus, qui est le rapport du produit scalaire des vecteurs au produit de leurs normes euclidiennes. La condition que les vecteurs soient non nuls est cruciale pour assurer que les normes au dénominateur sont strictement positives.

Pour la deuxième partie, la démonstration de l'invariance, nous allons substituer les vecteurs mis à l'échelle $\alpha u$ et $\beta v$ dans la formule de la similarité cosinus. Nous exploiterons les propriétés de bilinéarité du produit scalaire et la propriété de la norme euclidienne concernant la multiplication par un scalaire, à savoir $\| \lambda x \| = |\lambda| \|x\|$. Étant donné que les scalaires $\alpha$ et $\beta$ sont strictement positifs, leurs valeurs absolues sont égales à eux-mêmes ($|\alpha|=\alpha$ et $|\beta|=\beta$), ce qui simplifiera les expressions. L'objectif est de montrer que les termes scalaires $\alpha$ et $\beta$ s'annulent dans la fraction finale, laissant l'expression originale de la similarité cosinus.

Pour la troisième partie, l'explication de l'importance, nous nous appuierons sur l'interprétation géométrique de la similarité cosinus comme le cosinus de l'angle entre les vecteurs. Nous discuterons de la manière dont les espaces de plongement représentent des entités sémantiques et comment la direction d'un vecteur encode le sens, tandis que sa magnitude peut représenter d'autres informations (comme la fréquence ou l'importance). L'invariance par mise à l'échelle signifie que la similarité sémantique, mesurée par l'angle, n'est pas affectée par ces facteurs de magnitude, ce qui est souhaitable pour une recherche sémantique pure.

### Résolution Pas-à-Pas

1.  **Définition de la similarité cosinus**
    Soient $u$ et $v$ deux vecteurs non nuls de l'espace euclidien $E = \mathbb{R}^n$.
    Le produit scalaire canonique entre $u$ et $v$ est $\langle u, v \rangle = \sum_{i=1}^n u_i v_i$.
    La norme euclidienne de $u$ est $\|u\| = \sqrt{\langle u, u \rangle} = \sqrt{\sum_{i=1}^n u_i^2}$. De même, $\|v\| = \sqrt{\langle v, v \rangle} = \sqrt{\sum_{i=1}^n v_i^2}$.
    Puisque $u$ et $v$ sont des vecteurs non nuls, leurs normes $\|u\|$ et $\|v\|$ sont strictement positives.
    La similarité cosinus entre $u$ et $v$, notée $\text{sim}(u, v)$, est définie par :
    $$ \text{sim}(u, v) = \frac{\langle u, v \rangle}{\|u\| \|v\|} $$
    Cette définition est bien posée car le dénominateur est non nul.

2.  **Démonstration de l'invariance par mise à l'échelle positive**
    Nous voulons démontrer que pour $\alpha, \beta \in \mathbb{R}^{+*}$, on a $\text{sim}(u, v) = \text{sim}(\alpha u, \beta v)$.
    Commençons par calculer la similarité cosinus entre les vecteurs $\alpha u$ et $\beta v$ en utilisant la définition établie en partie 1 :
    $$ \text{sim}(\alpha u, \beta v) = \frac{\langle \alpha u, \beta v \rangle}{\|\alpha u\| \|\beta v\|} $$

    **Calcul du numérateur :**
    Le produit scalaire $\langle \alpha u, \beta v \rangle$ est calculé en utilisant la bilinéarité du produit scalaire canonique dans $\mathbb{R}^n$. Pour tout $x, y \in E$ et tout $\lambda, \mu \in \mathbb{R}$, nous avons $\langle \lambda x, \mu y \rangle = \lambda \mu \langle x, y \rangle$.
    En appliquant cette propriété :
    $$ \langle \alpha u, \beta v \rangle = \alpha \beta \langle u, v \rangle $$

    **Calcul du dénominateur :**
    Le dénominateur est le produit des normes de $\alpha u$ et $\beta v$. Nous utilisons la propriété de la norme euclidienne qui stipule que pour tout scalaire $\lambda \in \mathbb{R}$ et tout vecteur $x \in E$, $\| \lambda x \| = |\lambda| \|x\|$.
    Puisque $\alpha \in \mathbb{R}^{+*}$, $\alpha$ est strictement positif, donc $|\alpha| = \alpha$. Par conséquent :
    $$ \|\alpha u\| = |\alpha| \|u\| = \alpha \|u\| $$
    De même, puisque $\beta \in \mathbb{R}^{+*}$, $\beta$ est strictement positif, donc $|\beta| = \beta$. Par conséquent :
    $$ \|\beta v\| = |\beta| \|v\| = \beta \|v\| $$
    En multipliant ces deux expressions pour obtenir le dénominateur :
    $$ \|\alpha u\| \|\beta v\| = (\alpha \|u\|) (\beta \|v\|) = \alpha \beta \|u\| \|v\| $$

    **Substitution et simplification :**
    Maintenant, nous substituons les expressions obtenues pour le numérateur et le dénominateur dans la formule de la similarité cosinus pour $\alpha u$ et $\beta v$ :
    $$ \text{sim}(\alpha u, \beta v) = \frac{\alpha \beta \langle u, v \rangle}{\alpha \beta \|u\| \|v\|} $$
    Puisque $\alpha \in \mathbb{R}^{+*}$ et $\beta \in \mathbb{R}^{+*}$, leur produit $\alpha \beta$ est également un scalaire strictement positif. Nous pouvons donc diviser le numérateur et le dénominateur par $\alpha \beta$ :
    $$ \text{sim}(\alpha u, \beta v) = \frac{\langle u, v \rangle}{\|u\| \|v\|} $$
    En comparant cette expression avec la définition de $\text{sim}(u, v)$ de la partie 1, nous constatons qu'elles sont identiques.
    Ainsi, nous avons rigoureusement démontré que :
    $$ \text{sim}(u, v) = \text{sim}(\alpha u, \beta v) $$
    La similarité cosinus est bien invariante par mise à l'échelle par des scalaires strictement positifs.

3.  **Importance pour les moteurs de recherche sémantiques**
    Dans le domaine des moteurs de recherche sémantiques, des entités telles que des mots, des phrases, des documents ou des requêtes sont transformées en vecteurs numériques dans un espace de plongement (embedding space) de haute dimension. Ces vecteurs sont conçus de telle sorte que leur position et leur orientation dans cet espace encodent leur signification sémantique. La similarité cosinus est une métrique couramment utilisée pour quantifier la proximité sémantique entre ces entités.

    Géométriquement, la similarité cosinus est égale au cosinus de l'angle $\theta$ entre les deux vecteurs $u$ et $v$, c'est-à-dire $\text{sim}(u, v) = \cos(\theta)$. Un cosinus proche de 1 (angle petit) indique une forte similarité sémantique, tandis qu'un cosinus proche de -1 (angle grand, vecteurs opposés) indique une forte dissemblance.

    La propriété d'invariance démontrée ci-dessus est cruciale car elle signifie que la similarité cosinus ne dépend pas de la *magnitude* (longueur) des vecteurs, mais uniquement de leur *direction* relative. Dans les espaces de plongement, la magnitude d'un vecteur peut parfois être influencée par des facteurs non sémantiques, tels que la fréquence d'apparition d'un mot dans un corpus (par exemple, un mot très fréquent pourrait avoir un vecteur de plus grande magnitude) ou la longueur d'un document.

    Si un moteur de recherche utilisait une métrique de distance euclidienne (qui dépend de la magnitude) pour la similarité sémantique, un mot rare mais sémantiquement pertinent pourrait être jugé "moins similaire" à un mot fréquent simplement à cause de la différence de magnitude de leurs vecteurs, même si leurs directions sémantiques sont très proches.

    En utilisant la similarité cosinus, le moteur de recherche se concentre exclusivement sur l'alignement directionnel des vecteurs. Cela permet de mesurer la similarité sémantique pure, en ignorant les variations de magnitude qui pourraient être des artefacts du processus de plongement ou des caractéristiques non pertinentes pour la sémantique. Par exemple, si "voiture" et "automobile" sont sémantiquement très proches, leurs vecteurs $u$ et $v$ pointeront dans des directions très similaires, et leur similarité cosinus sera élevée, indépendamment du fait que l'un des mots soit beaucoup plus fréquent que l'autre dans le corpus d'entraînement et ait, par conséquent, un vecteur de magnitude différente. Cette robustesse aux variations d'échelle est essentielle pour une recherche sémantique efficace et pertinente.

### Conclusion
Nous avons défini la similarité cosinus comme le rapport du produit scalaire au produit des normes des vecteurs. Nous avons ensuite démontré rigoureusement que la similarité cosinus est invariante par mise à l'échelle par des scalaires strictement positifs, c'est-à-dire que $\text{sim}(u, v) = \text{sim}(\alpha u, \beta v)$ pour tout $\alpha, \beta \in \mathbb{R}^{+*}$. Cette propriété est d'une importance capitale pour les moteurs de recherche sémantiques, car elle garantit que la mesure de similarité se concentre exclusivement sur la direction des vecteurs de plongement, qui encode l'information sémantique, et n'est pas influencée par leur magnitude. Cela permet une évaluation robuste et pertinente de la proximité conceptuelle entre les entités représentées dans les espaces de plongement.
