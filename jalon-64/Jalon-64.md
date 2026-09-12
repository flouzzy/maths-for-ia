---
uuid: "jalon-64"
title: "Construction de la mesure de Lebesgue"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/abstraction
prev: "[[Jalon-63.md]]"
next: "[[Jalon-65.md]]"
---

# Construction de la mesure de Lebesgue

## 1. De l'intuition géométrique à la nécessité formelle

La théorie de l'intégration de Riemann, étudiée au Jalon 37, repose sur le découpage du domaine d'intégration en intervalles. Cette approche s'avère particulièrement puissante pour les fonctions continues ou continues par morceaux. Toutefois, lorsqu'on est confronté à des espaces plus complexes ou à des fonctions dont le comportement est fortement discontinu (comme la fonction indicatrice de $\mathbb{Q}$), l'approche de Riemann échoue. L'impasse géométrique réside dans notre incapacité à mesurer de façon cohérente des ensembles de points "éparpillés" sur la droite réelle en utilisant de simples longueurs d'intervalles finis.

Historiquement, Émile Borel et Henri Lebesgue, au tournant du 20ème siècle, ont radicalement changé de perspective. Au lieu de découper le domaine de départ en sous-intervalles pour évaluer l'aire sous une courbe, Lebesgue a proposé de mesurer la "taille" de l'ensemble des points de départ qui partagent des valeurs d'arrivée proches. Pour ce faire, il fallait construire un outil capable de mesurer la longueur, l'aire ou le volume d'ensembles infiniment plus complexes que de simples segments ou polygones : c'est la genèse de la mesure de Lebesgue.

Le processus constructif repose sur un principe physique fondamental de majoration : pour mesurer la taille d'un objet abstrait et irrégulier (un nuage de points), on le recouvre par une union dénombrable de briques élémentaires (des intervalles ouverts) dont on connaît la taille exacte. En cherchant le recouvrement le plus économique possible, on définit ce qu'on appelle la *mesure extérieure*.

## 2. Mesure Extérieure et Critère de Carathéodory

### Mesure Extérieure de Lebesgue

La première étape de la construction consiste à attribuer une valeur positive ou nulle à toute partie de $\mathbb{R}$.

> **Définition (Mesure extérieure de Lebesgue) :**
> Soit $A$ une partie quelconque de $\mathbb{R}$ ($A \in \mathcal{P}(\mathbb{R})$). La mesure extérieure de Lebesgue de $A$, notée $\lambda^*(A)$, est définie par :
> $$\lambda^*(A) = \inf \left\lbrace \sum_{n=1}^{+\infty} \ell(I_n) \;\middle|\; A \subset \bigcup_{n=1}^{+\infty} I_n \right\rbrace$$
> où $(I_n)_{n \in \mathbb{N}^*}$ est une suite d'intervalles ouverts de $\mathbb{R}$ tels que $I_n = ]a_n, b_n[$, et $\ell(I_n) = b_n - a_n$ désigne la longueur de l'intervalle $I_n$. Si un intervalle est non borné, sa longueur est $+\infty$.

Cette définition garantit que $\lambda^*$ est bien définie pour toute partie de $\mathbb{R}$, prenant ses valeurs dans $[0, +\infty]$.

**Exemple concret immédiat :**
Calculons la mesure extérieure d'un point isolé, disons $A = \{x_0\}$.
Pour tout $\epsilon > 0$, considérons l'intervalle ouvert $I_1 = ]x_0 - \frac{\epsilon}{2}, x_0 + \frac{\epsilon}{2}[$.
Clairement, $A \subset I_1$. Posons $I_n = \emptyset$ pour $n \ge 2$ (conventionnellement un intervalle ouvert de longueur 0).
La somme des longueurs de ce recouvrement est $\ell(I_1) = \epsilon$.
Par définition de l'infimum, on a donc $\lambda^*(\{x_0\}) \le \epsilon$. Comme cela est vrai pour tout $\epsilon > 0$ et que $\lambda^* \ge 0$, on conclut inexorablement que $\lambda^*(\{x_0\}) = 0$. Un point n'a pas d'épaisseur.

**Cas pathologique :**
Bien que la mesure extérieure soit définie pour toute partie de $\mathbb{R}$, elle souffre d'un défaut fatal : elle n'est pas additive sur tout $\mathcal{P}(\mathbb{R})$. On peut construire (grâce à l'axiome du choix, construction de Vitali) des ensembles disjoints $A$ et $B$ tels que $\lambda^*(A \cup B) < \lambda^*(A) + \lambda^*(B)$. C'est inacceptable pour une notion de "mesure" physique rigoureuse. Il faut donc restreindre le domaine de $\lambda^*$ aux ensembles qui se comportent "bien".

### Tribu de Lebesgue et Critère de Carathéodory

Pour pallier le défaut de la mesure extérieure, Constantin Carathéodory a formulé un critère de découpage permettant d'isoler les sous-ensembles "mesurables".

> **Définition (Ensemble Lebesgue-mesurable et Critère de Carathéodory) :**
> Une partie $E \subset \mathbb{R}$ est dite **mesurable au sens de Lebesgue** si elle découpe toute autre partie de $\mathbb{R}$ de manière additive vis-à-vis de la mesure extérieure. Précisément, pour tout ensemble $A \subset \mathbb{R}$ (qu'on appelle "ensemble test") :
> $$\lambda^*(A) = \lambda^*(A \cap E) + \lambda^*(A \cap E^c)$$
> où $E^c = \mathbb{R} \setminus E$ est le complémentaire de $E$.
> L'ensemble de toutes les parties Lebesgue-mesurables de $\mathbb{R}$ est noté $\mathcal{L}(\mathbb{R})$.

Il est remarquable (et c'est un théorème fondamental de la théorie de la mesure) que la classe $\mathcal{L}(\mathbb{R})$ ne soit pas un simple ensemble, mais forme une véritable **tribu** (ou $\sigma$-algèbre). De plus, la restriction de $\lambda^*$ à cette tribu $\mathcal{L}(\mathbb{R})$ est bien une mesure, c'est-à-dire qu'elle vérifie l'axiome de $\sigma$-additivité.

> **Définition (Mesure de Lebesgue) :**
> La **mesure de Lebesgue** sur $\mathbb{R}$, notée $\lambda$, est la restriction de la mesure extérieure $\lambda^*$ à la tribu des ensembles Lebesgue-mesurables $\mathcal{L}(\mathbb{R})$.
> Pour tout $E \in \mathcal{L}(\mathbb{R})$, on a :
> $$\lambda(E) = \lambda^*(E)$$
> Le triplet $(\mathbb{R}, \mathcal{L}(\mathbb{R}), \lambda)$ constitue l'espace mesuré fondamental de l'analyse réelle.

## 3. Démonstrations Fondamentales

Nous allons démontrer rigoureusement qu'un ensemble dénombrable est de mesure nulle au sens de Lebesgue. Ce résultat est le socle de l'intégration moderne.

> **Théorème :** Si $A \subset \mathbb{R}$ est un ensemble dénombrable (ou fini), alors $\lambda^*(A) = 0$. Par conséquent, $A$ est mesurable et $\lambda(A) = 0$.

**Démonstration ligne par ligne :**

Soit $A$ un sous-ensemble dénombrable de $\mathbb{R}$. Puisque $A$ est dénombrable, il existe une bijection (ou surjection) de $\mathbb{N}^*$ dans $A$. Nous pouvons donc énumérer les éléments de $A$ sous la forme d'une suite :
$$A = \{ x_1, x_2, x_3, \dots, x_n, \dots \}$$

Soit $\epsilon > 0$ un réel arbitrairement petit.
Nous cherchons à recouvrir $A$ par une suite d'intervalles ouverts $(I_n)_{n \in \mathbb{N}^*}$ dont la somme des longueurs est majorée par $\epsilon$.

Pour chaque entier $n \ge 1$, considérons l'intervalle ouvert $I_n$ centré sur $x_n$ et de longueur $\frac{\epsilon}{2^n}$. Explicitons ses bornes :
$$I_n = \left] x_n - \frac{\epsilon}{2^{n+1}}, x_n + \frac{\epsilon}{2^{n+1}} \right[$$
La longueur de $I_n$ est bien calculée par :
$$\ell(I_n) = \left( x_n + \frac{\epsilon}{2^{n+1}} \right) - \left( x_n - \frac{\epsilon}{2^{n+1}} \right) = \frac{2\epsilon}{2^{n+1}} = \frac{\epsilon}{2^n}$$

Par construction, le point $x_n$ appartient à l'intervalle $I_n$. Ainsi, l'ensemble $A$ est totalement inclus dans l'union de ces intervalles :
$$A \subset \bigcup_{n=1}^{+\infty} I_n$$

Par définition de la mesure extérieure comme infimum des sommes des longueurs des recouvrements, nous avons l'inégalité de majoration :
$$\lambda^*(A) \le \sum_{n=1}^{+\infty} \ell(I_n)$$

Substituons l'expression de la longueur :
$$\lambda^*(A) \le \sum_{n=1}^{+\infty} \frac{\epsilon}{2^n}$$
On peut factoriser $\epsilon$ car il est indépendant de l'indice de sommation $n$ :
$$\lambda^*(A) \le \epsilon \sum_{n=1}^{+\infty} \frac{1}{2^n}$$

Reconnaissons la somme d'une série géométrique de raison $q = \frac{1}{2}$, dont le premier terme (pour $n=1$) est $\frac{1}{2}$. La somme de cette série classique est connue :
$$\sum_{n=1}^{+\infty} \left(\frac{1}{2}\right)^n = \frac{\frac{1}{2}}{1 - \frac{1}{2}} = 1$$

Nous obtenons donc :
$$\lambda^*(A) \le \epsilon \times 1 = \epsilon$$

Puisque la mesure extérieure est par définition positive ou nulle, nous avons :
$$0 \le \lambda^*(A) \le \epsilon$$
Cette double inégalité étant vraie pour tout $\epsilon > 0$, la seule possibilité logique en passant à la limite $\epsilon \to 0$ est que :
$$\lambda^*(A) = 0$$

Enfin, un ensemble de mesure extérieure nulle satisfait trivialement le critère de Carathéodory (puisque pour tout ensemble test $E$, $\lambda^*(E \cap A) = 0$ et $\lambda^*(E \cap A^c) \le \lambda^*(E)$), donc $A \in \mathcal{L}(\mathbb{R})$ et $\lambda(A) = 0$. $\blacksquare$

## 4. Répercussions en Probabilités et Intelligence Artificielle

La construction formelle de la mesure de Lebesgue n'est pas un artéfact de mathématiciens en quête d'abstraction ; c'est le langage natif des variables aléatoires continues, au cœur du Machine Learning et de l'IA moderne.

**Densités de Probabilité (PDF) et Variables Aléatoires Continues :**
Lorsqu'un réseau de neurones modélise l'incertitude via une loi de probabilité continue (comme les Variational Autoencoders ou les modèles de diffusion), l'espace sous-jacent est muni de la mesure de Lebesgue. On dit qu'une variable aléatoire réelle $X$ admet une densité $f$ si pour tout sous-ensemble borélien $B$ :
$$P(X \in B) = \int_B f(x) \, d\lambda(x)$$
C'est précisément l'intégrale par rapport à la mesure de Lebesgue $\lambda$. La certitude que la mesure d'un point isolé ou d'un ensemble dénombrable est nulle explique pourquoi la probabilité de tirer *exactement* une valeur précise (par exemple $P(X=0.42)$) pour une loi continue est rigoureusement zéro.

**Supports en Manifold Learning et GANs :**
Dans la théorie des Generative Adversarial Networks (GANs), on suppose souvent que les données d'apprentissage (des images haute résolution en dimension $N = 1024 \times 1024 \times 3$) ne remplissent pas tout l'espace $\mathbb{R}^N$, mais se trouvent sur une sous-variété de dimension intrinsèque beaucoup plus faible $d \ll N$. Par rapport à la mesure de Lebesgue en dimension $N$, cette sous-variété a une mesure nulle. Cette absence d'intersection en termes de mesure de Lebesgue entre la distribution générée et la distribution réelle est la cause mathématique profonde du phénomène d'évanouissement du gradient (vanishing gradient) lorsque l'on utilise des métriques de divergence statistiques basiques, nécessitant alors le recours à la distance de Wasserstein (Optimal Transport) qui ne dépend pas de l'existence d'une densité par rapport à la mesure de Lebesgue sur l'espace complet.
