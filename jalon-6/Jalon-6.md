---
uuid: "jalon-6"
title: "Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps)"
year: 1
trimester: 1
tags:
  - math/fondations
  - ia/topologie-donnees
prev: "[[Jalon-5.md]]"
next: "[[Jalon-7.md]]"
---
# Jalon 6 : Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps)

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** 
  - **Relation d'équivalence :** C'est comme trier des Lego par couleur. Peu importe la forme de la brique, si elle est rouge, elle va dans le bac des rouges. Toutes les briques rouges sont "équivalentes" du point de vue de la couleur. Le bac rouge est une **classe d'équivalence**.
  - **Relation d'ordre :** C'est comme ranger des livres par taille sur une étagère. On peut dire qu'un livre est "plus petit ou égal" à un autre. C'est ce qui nous permet de comparer et de classer.
  - **Structures (Groupes, Anneaux, Corps) :** Imaginez un jeu de société. Les éléments sont les pièces, et les structures sont les **règles du jeu**. Un "Groupe", c'est un jeu où l'on peut toujours "annuler" un coup (faire l'inverse). Un "Corps", c'est un jeu plus riche où l'on peut additionner, soustraire, multiplier et même diviser (sauf par zéro), comme avec les nombres réels.
- **Le "Pourquoi on a inventé ça" :** On a besoin de simplifier le monde. Au lieu d'étudier chaque objet individuellement, on les regroupe par propriétés communes (quotients) ou on définit des règles de calcul universelles (structures) pour ne pas avoir à réinventer la roue pour chaque nouveau type de nombre ou d'objet.
- **Visualisation :** L'**ensemble quotient**, c'est comme regarder une ville depuis très haut : les détails des maisons disparaissent et on ne voit plus que des "quartiers". Chaque quartier est un point unique dans un nouvel ensemble simplifié.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $E$ un ensemble non vide. Une relation binaire $\mathcal{R}$ sur $E$ est un sous-ensemble de $E \times E$. On note $x \mathcal{R} y$ au lieu de $(x,y) \in \mathcal{R}$.

1. **Relation d'équivalence :** $\mathcal{R}$ est une relation d'équivalence si elle est :
   - Réflexive : $\forall x \in E, x \mathcal{R} x$.
   - Symétrique : $\forall x, y \in E, x \mathcal{R} y \Rightarrow y \mathcal{R} x$.
   - Transitive : $\forall x, y, z \in E, (x \mathcal{R} y \land y \mathcal{R} z) \Rightarrow x \mathcal{R} z$.
   La **classe d'équivalence** de $x$ est $\dot{x} = \{ y \in E \mid x \mathcal{R} y \}$. L'**ensemble quotient** est $E/\mathcal{R} = \{ \dot{x} \mid x \in E \}$.

2. **Relation d'ordre :** $\mathcal{R}$ est une relation d'ordre (notée $\le$) si elle est réflexive, transitive et **antisymétrique** ($x \mathcal{R} y \land y \mathcal{R} x \Rightarrow x = y$).

3. **Groupe $(G, \star)$ :** Un ensemble muni d'une loi de composition interne $\star$ telle que :
   - $\star$ est associative.
   - Il existe un élément neutre $e \in G$.
   - Tout élément $x \in G$ possède un symétrique $x^{-1} \in G$.
   Si $\star$ est commutative, le groupe est dit **abélien**.

4. **Anneau $(A, +, \times)$ :** $(A, +)$ est un groupe abélien, $\times$ est associative, distributive sur $+$, et possède un neutre $1_A$.

5. **Corps $(\mathbb{K}, +, \times)$ :** Un anneau commutatif où tout élément non nul possède un inverse pour $\times$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème Fondamental des Relations d'Équivalence :**
> Les classes d'équivalence d'une relation $\mathcal{R}$ sur $E$ forment une **partition** de $E$. Inversement, toute partition de $E$ définit une relation d'équivalence unique.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Structure de Groupe de $(\mathbb{Z}/n\mathbb{Z}, +)$
Soit $n \in \mathbb{N}^*$. On définit la relation de congruence modulo $n$ sur $\mathbb{Z}$ par : $x \equiv y [n] \iff \exists k \in \mathbb{Z}, x - y = kn$.
Démontrons que l'ensemble quotient $\mathbb{Z}/n\mathbb{Z}$ muni de l'addition induite est un groupe abélien.

1. **Initialisation / Cadre :** Prouvons d'abord que la relation $\equiv [n]$ est une relation d'équivalence.
   - **Réflexivité :** Pour tout $x \in \mathbb{Z}$, on a $x - x = 0 = 0 \times n$. Comme $0 \in \mathbb{Z}$, alors $x \equiv x [n]$.
   - **Symétrie :** Soient $x, y \in \mathbb{Z}$ tels que $x \equiv y [n]$. Alors il existe $k \in \mathbb{Z}$ tel que $x - y = kn$. On peut réécrire ceci comme $y - x = (-k)n$. Comme $-k \in \mathbb{Z}$, alors $y \equiv x [n]$.
   - **Transitivité :** Soient $x, y, z \in \mathbb{Z}$ tels que $x \equiv y [n]$ et $y \equiv z [n]$. Alors il existe $k_1, k_2 \in \mathbb{Z}$ tels que $x - y = k_1n$ et $y - z = k_2n$. En additionnant ces deux équations, on obtient $(x - y) + (y - z) = k_1n + k_2n$, soit $x - z = (k_1 + k_2)n$. Comme $k_1 + k_2 \in \mathbb{Z}$, alors $x \equiv z [n]$.
   La relation $\equiv [n]$ est donc bien une relation d'équivalence. On note $\dot{x}$ (ou $\overline{x}$) la classe de $x$. On définit l'addition sur l'ensemble quotient $\mathbb{Z}/n\mathbb{Z}$ par : $\dot{x} + \dot{y} = \overline{x+y}$.

2. **Étape 1 : Vérification de la bonne définition de la loi**
   Soient $x, x', y, y' \in \mathbb{Z}$ tels que $\dot{x} = \dot{x'}$ et $\dot{y} = \dot{y'}$.
   - $\dot{x} = \dot{x'} \implies \exists k_1 \in \mathbb{Z}, x' = x + k_1 n$.
   - $\dot{y} = \dot{y'} \implies \exists k_2 \in \mathbb{Z}, y' = y + k_2 n$.
   Calculons $x' + y'$ :
   $x' + y' = (x + k_1 n) + (y + k_2 n)$
   $x' + y' = (x + y) + (k_1 + k_2) n$.
   Comme $(k_1 + k_2) \in \mathbb{Z}$, on a $(x' + y') \equiv (x + y) [n]$, d'où $\overline{x' + y'} = \overline{x + y}$.
   La loi $+$ est bien définie sur le quotient.

3. **Étape 2 : Associativité et Commutativité**
   Elles découlent directement des propriétés de $+$ dans $\mathbb{Z}$ :
   $(\dot{x} + \dot{y}) + \dot{z} = \overline{x+y} + \dot{z} = \overline{(x+y)+z} = \overline{x+(y+z)} = \dot{x} + (\dot{y} + \dot{z})$.
   $\dot{x} + \dot{y} = \overline{x+y} = \overline{y+x} = \dot{y} + \dot{x}$.

4. **Étape 3 : Élément neutre et symétrique**
   - Le neutre est $\dot{0}$ car $\dot{x} + \dot{0} = \overline{x+0} = \dot{x}$.
   - Le symétrique de $\dot{x}$ est $\overline{-x}$ car $\dot{x} + \overline{-x} = \overline{x-x} = \dot{0}$.

5. **Conclusion :** $(\mathbb{Z}/n\mathbb{Z}, +)$ est un groupe abélien de cardinal $n$.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Relation d'ordre)
**Énoncé :** Sur $\mathbb{R}^2$, on définit la relation $(x,y) \preceq (x',y') \iff (x \le x' \text{ et } y \le y')$. Est-ce une relation d'ordre total ?
**Correction Détaillée :**
1. **Réflexivité :** $(x,y) \preceq (x,y)$ car $x \le x$ et $y \le y$.
2. **Antisymétrie :** Si $(x,y) \preceq (x',y')$ et $(x',y') \preceq (x,y)$, alors $x \le x', x' \le x \implies x = x'$ et $y \le y', y' \le y \implies y = y'$. Donc $(x,y) = (x',y')$.
3. **Transitivité :** Si $(x,y) \preceq (x',y')$ et $(x',y') \preceq (x'',y'')$, alors $x \le x' \le x''$ et $y \le y' \le y''$, donc $(x,y) \preceq (x'',y'')$.
4. **Totalité ?** Comparons $(1,0)$ et $(0,1)$.
   - $1 \le 0$ est faux, donc $(1,0) \preceq (0,1)$ est faux.
   - $1 \le 0$ (pour la 2ème composante) est faux, donc $(0,1) \preceq (1,0)$ est faux.
**Conclusion :** C'est une relation d'ordre **partiel**, mais pas total car certains éléments sont incomparables.

### Exercice 2 : Niveau Avancé (Groupe des inversibles)
**Énoncé :** Démontrer que si $(\mathbb{K}, +, \times)$ est un corps, alors l'ensemble $\mathbb{K}^* = \mathbb{K} \setminus \{0\}$ muni de $\times$ est un groupe.
**Correction Détaillée :**
1. **LCI :** Soient $x, y \in \mathbb{K}^*$. Comme $\mathbb{K}$ est un corps, c'est un anneau intègre. Donc $x \times y = 0 \Rightarrow (x = 0 \text{ ou } y = 0)$. Par contraposée, comme $x \neq 0$ et $y \neq 0$, alors $x \times y \neq 0$. Donc $x \times y \in \mathbb{K}^*$.
2. **Associativité :** Héritée de la structure d'anneau de $\mathbb{K}$.
3. **Neutre :** $1_{\mathbb{K}}$ appartient à $\mathbb{K}^*$ (un corps n'est pas réduit à $\{0\}$ par définition, donc $1 \neq 0$). $x \times 1 = 1 \times x = x$.
4. **Inverse :** Par définition d'un corps, tout élément non nul $x$ possède un inverse $x^{-1}$ tel que $x \times x^{-1} = 1$. Comme $1 \neq 0$, alors $x^{-1} \neq 0$ (sinon $x \times 0 = 1$ impossible), donc $x^{-1} \in \mathbb{K}^*$.
**Conclusion :** $(\mathbb{K}^*, \times)$ est un groupe (abélien puisque le corps est commutatif).

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Les relations d'équivalence et les quotients sont à la base de la **Topologie des Données** (TDA - Topological Data Analysis).
- **Exemple Concret :** Dans les algorithmes de **Clustering** (comme DBSCAN ou Single-Linkage), on définit une relation d'équivalence "être dans le même groupe" basée sur une distance seuil. L'ensemble des clusters n'est rien d'autre que l'**ensemble quotient** de l'ensemble des points de données par la relation "être connectés". De même, dans les **Graphes de Connaissances**, on quotient l'espace des entités pour fusionner les synonymes (Entity Resolution).

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon-4]], [[Jalon-5.md|Jalon 5]]
- **Concepts Futurs dépendants :** [[Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon 62 (Algèbres)]], [[Jalon 119 (Connexions avec les groupes de Lie)]]
