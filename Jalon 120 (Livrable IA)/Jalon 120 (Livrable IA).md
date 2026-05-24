---
uuid: "jalon-120"
title: "Livrable IA T10 : Invariance et Équivariance en Geometric Deep Learning"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/fondations
prev: "[[Jalon 119 (Connexions avec les groupes de Lie).md]]"
next: "[[Jalon 121 (Ensembles convexes).md]]"
---

# Jalon 120 : Livrable IA T10 : Invariance et Équivariance en Geometric Deep Learning

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous montriez une photo de chat à une IA.
    - Si vous décalez la photo de 10 pixels vers la gauche, l'IA doit toujours dire "C'est un chat". C'est l'**Invariance par translation**.
    - Si vous faites tourner la photo, l'IA doit toujours dire "C'est un chat", mais elle doit aussi être capable de dire "le chat a tourné de 90°". C'est l'**Équivariance**.
    - Les mathématiques des variétés et des groupes nous permettent de construire des réseaux de neurones qui possèdent ces "super-pouvoirs" de naissance : ils n'ont pas besoin d'apprendre que la rotation ne change pas l'objet, ils le "savent" par construction géométrique.
- **Le "Pourquoi on a inventé ça" :** Pour rendre l'IA plus efficace. Sans ces contraintes, une IA doit voir des millions d'images de chats dans TOUTES les positions possibles pour apprendre. Avec l'équivariance, une seule photo suffit pour que l'IA comprenne toutes les versions tournées ou décalées de ce chat. On gagne énormément en temps de calcul et en quantité de données.
- **Visualisation :** Un filtre qui glisse sur une image. Peu importe où l'objet se trouve, le filtre réagira de la même manière. Si l'objet tourne, le filtre doit "tourner" lui aussi pour capter l'information.

## 2. Formalisation & Rigueur Académique

Soit $X$ un espace de données (ex: $\mathbb{R}^n$ pour des images ou une variété $M$ pour des graphes). Soit $G$ un groupe de Lie (ex: $SO(3)$ pour les rotations).

### A. Actions de Groupe

> **Définition 1 (Action de groupe) :**
> Une action de $G$ sur $X$ est une application $(g, x) \mapsto g \cdot x$ qui respecte la structure de groupe. Elle induit une transformation sur les fonctions (signaux) définies sur $X$ :
> $$[L_g f](x) = f(g^{-1} \cdot x)$$

### B. Invariance et Équivariance

Soit $\Phi : \mathcal{F}(X) \to \mathcal{F}(Y)$ une couche d'un réseau de neurones.

> **Définition 2 (Invariance) :**
> $\Phi$ est **invariante** sous $G$ si :
> $$\forall g \in G, \forall f, \quad \Phi(L_g f) = \Phi(f)$$
> Le résultat final ne dépend pas de la transformation subie par l'entrée.

> **Définition 3 (Équivariance) :**
> $\Phi$ est **équivariante** sous $G$ si :
> $$\forall g \in G, \forall f, \quad \Phi(L_g f) = L'_g \Phi(f)$$
> Transformer l'entrée puis appliquer la couche revient au même que d'appliquer la couche puis transformer la sortie.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Pourquoi la convolution est-elle équivariante par translation ?

Soit $\Phi(f) = f * k$ où $k$ est un noyau de convolution. Soit $T_\tau$ l'opérateur de translation $T_\tau f(x) = f(x-\tau)$.

1. **Calcul de la sortie translatée :**
   $[\Phi(T_\tau f)](x) = ((T_\tau f) * k)(x) = \int (T_\tau f)(x-y) k(y) dy$.
2. **Substitution :**
   $[\Phi(T_\tau f)](x) = \int f(x-y-\tau) k(y) dy$.
3. **Calcul de la translation de la sortie :**
   $[T_\tau (\Phi f)](x) = (f * k)(x-\tau) = \int f((x-\tau)-y) k(y) dy$.
4. **Comparaison :**
   Les deux expressions sont identiques.
5. **Conclusion :** $\Phi \circ T_\tau = T_\tau \circ \Phi$. La convolution "commute" avec la translation. C'est ce qui permet aux CNN de détecter des motifs n'importe où dans une image.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Pooling et Invariance
**Énoncé :** Montrer que l'opération de Global Average Pooling ($f \mapsto \int_X f(x) dx$) est invariante par translation si $X = \mathbb{R}^n$.
**Correction Détaillée :**
$\int f(x-\tau) dx = \int f(u) du$ (par changement de variable $u=x-\tau$, le Jacobien vaut 1). La valeur de l'intégrale totale ne change pas. C'est pourquoi on utilise un pooling à la fin des réseaux pour obtenir une prédiction de classe unique indépendante de la position de l'objet.

### Exercice 2 : Niveau Avancé (Graph Neural Networks)
**Énoncé :** Sur un graphe, le groupe des symétries est le groupe des permutations des nœuds $\mathcal{S}_n$. Quelle opération remplace la convolution pour être équivariante aux permutations ?
**Correction Détaillée :**
C'est le **Message Passing**. Si on change l'ordre des noms des nœuds, le résultat du calcul sur chaque nœud doit changer de la même manière. On montre que cela impose d'utiliser des fonctions d'agrégation symétriques (comme la somme ou le max) sur les voisinages.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le **Geometric Deep Learning** unifie les CNN (données sur grilles), les GNN (données sur graphes) et les réseaux sur variétés. Tout repose sur le choix du groupe $G$.
- **Example Concret :**
    - **AlphaFold (Protéines) :** Pour prédire la forme d'une protéine, le réseau doit être équivariant par rotation et translation en 3D ($SE(3)$). Si vous tournez la molécule, les forces physiques tournent avec elle. AlphaFold utilise des couches d'attention équivariantes.
    - **Imagerie Médicale :** On utilise des réseaux équivariants par rotation pour analyser des IRM ou des coupes de tissus, car l'orientation de l'organe dans le scanner est aléatoire.
    - **Cosmologie :** Les réseaux de neurones sphériques analysent le fond diffus cosmologique (données sur la sphère $S^2$) en utilisant l'équivariance sous le groupe $SO(3)$.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 119 (Connexions avec les groupes de Lie).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]] (Convolution)
- **Concepts Futurs dépendants :** [[Jalon 143 (Théorie spectrale des graphes).md]], [[Jalon 145 à 152 (PAC pour Attention).md]]
