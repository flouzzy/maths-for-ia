---
uuid: "jalon-44"
title: "Fonctions de plusieurs variables"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/topologie
prev: "[[Jalon 43 (Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.).md]]"
next: "[[Jalon 45 (Différentiabilité).md]]"
---

# Jalon 44 : Fonctions de plusieurs variables

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous utilisez une application de cartographie. Votre position est donnée par deux nombres : la latitude et la longitude. L'altitude à laquelle vous vous trouvez est une fonction qui dépend de ces deux nombres. C'est une **fonction de plusieurs variables**. Si vous bougez un tout petit peu, l'altitude change normalement un tout petit peu (c'est la continuité). Mais sur une falaise abrupte, un petit pas peut provoquer une chute énorme (discontinuité).
- **Le "Pourquoi on a inventé ça" :** Le monde n'est pas unidimensionnel. Pour décrire le climat, on a besoin de la pression, de la température et de l'humidité en chaque point de l'espace. En IA, on ne manipule jamais un seul nombre, mais des milliers de caractéristiques (pixels d'une image, mots d'une phrase). On doit donc apprendre à faire de l'analyse dans des espaces à $n$ dimensions.
- **Visualisation :** Une surface ondulée au-dessus d'un plan. Les "lignes de niveau" sur une carte de randonnée sont la visualisation parfaite de ces fonctions : elles relient les points de même altitude.

## 2. Formalisation & Rigueur Académique

### A. Topologie de $\mathbb{R}^n$ (Rappels)

Soit $\mathbb{R}^n$ muni de sa structure d'espace vectoriel normé (généralement la norme euclidienne $\| \cdot \|_2$).

> **Définition 1 (Domaine de définition) :**
> Une fonction de $n$ variables est une application $f : D \to \mathbb{R}$ où $D \subset \mathbb{R}^n$ est le domaine de définition. On dit que $f$ est définie au voisinage de $a \in \mathbb{R}^n$ s'il existe une boule ouverte $B(a, r)$ incluse dans $D$.

### B. Limites et Continuité

> **Définition 2 (Limite) :**
> On dit que $f$ admet une limite $L$ en $a$ si :
> $$\forall \epsilon > 0, \exists \delta > 0, \forall x \in D, \quad \|x - a\| < \delta \implies |f(x) - L| < \epsilon$$
> *Attention :* Pour que la limite existe, elle doit être la même quel que soit le "chemin" emprunté pour arriver en $a$.

> **Définition 3 (Continuité) :**
> $f$ est **continue** en $a \in D$ si $\lim_{x \to a} f(x) = f(a)$.
> $f$ est continue sur $D$ si elle est continue en tout point de $D$.

### C. Théorèmes Fondamentaux

> **Théorème de Composition :**
> Si $f$ est continue en $a$ et $g$ est continue en $f(a)$, alors $g \circ f$ est continue en $a$.

> **Théorème des Valeurs Intermédiaires (Version plusieurs variables) :**
> Si $f$ est continue sur un ensemble **connexe** (d'un seul tenant), alors l'image de cet ensemble par $f$ est un intervalle de $\mathbb{R}$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Le Piège de la Continuité : Pourquoi les limites directionnelles ne suffisent pas

Il est tentant de croire que si une fonction est continue selon chaque axe séparément, elle est continue globalement. C'est **FAUX**.

1. **Contre-exemple classique :** $f(x, y) = \frac{xy}{x^2 + y^2}$ pour $(x, y) \neq (0, 0)$ et $f(0, 0) = 0$.
2. **Approche par les axes :**
   - Sur l'axe $x$ ($y=0$) : $f(x, 0) = 0 \to 0$.
   - Sur l'axe $y$ ($x=0$) : $f(0, y) = 0 \to 0$.
   La limite semble être 0.
3. **Approche par la diagonale :**
   - Sur la droite $y=x$ : $f(x, x) = \frac{x^2}{x^2 + x^2} = \frac{x^2}{2x^2} = \frac{1}{2}$.
   Ici, la limite est $1/2$.
4. **Conclusion :** Comme on trouve des limites différentes selon le chemin, la fonction n'admet pas de limite en $(0, 0)$ et n'est donc pas continue.

### Utilisation des coordonnées polaires pour prouver une limite

1. **Méthode :** Pour étudier la limite en $(0, 0)$, on pose $x = r \cos \theta$ and $y = r \sin \theta$.
2. **Condition :** Si $|f(r \cos \theta, r \sin \theta) - L|$ peut être majoré par une fonction $h(r)$ telle que $h(r) \to 0$ (indépendamment de $\theta$), alors la limite est $L$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Étude de limite
**Énoncé :** Étudier la continuité en $(0, 0)$ de $f(x, y) = \frac{x^2 y^2}{x^2 + y^2}$.
**Correction Détaillée :**
1. **Passage en polaires :** $f(r \cos \theta, r \sin \theta) = \frac{r^2 \cos^2 \theta \cdot r^2 \sin^2 \theta}{r^2} = r^2 \cos^2 \theta \sin^2 \theta$.
2. **Majoration :** On sait que $|\cos \theta| \le 1$ et $|\sin \theta| \le 1$.
   Donc $|f(x, y)| \le r^2 = x^2 + y^2$.
3. **Limite :** Comme $x^2 + y^2 \to 0$ quand $(x, y) \to (0, 0)$, par le théorème des gendarmes, $\lim f = 0$.
4. **Résultat :** La fonction est prolongeable par continuité en $(0, 0)$ en posant $f(0, 0) = 0$.

### Exercice 2 : Niveau Avancé (Topologie et Convexité)
**Énoncé :** Montrer que si $f$ est continue sur $\mathbb{R}^n$, l'ensemble $\{ x \in \mathbb{R}^n \mid f(x) < c \}$ est un ouvert.
**Correction Détaillée :**
C'est une application directe de la définition topologique de la continuité : "l'image réciproque d'un ouvert par une application continue est un ouvert". Ici, $f^{-1}(]-\infty, c[)$. Comme $]-\infty, c[$ est un ouvert de $\mathbb{R}$, son image réciproque est un ouvert de $\mathbb{R}^n$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le Deep Learning consiste à optimiser une **fonction de perte** (Loss Function) qui dépend de millions de paramètres. C'est l'exemple ultime d'une fonction de plusieurs variables.
- **Exemple Concret :**
    - **Surface de perte (Loss Surface) :** On visualise souvent la perte comme une surface en 3D (2 variables de poids). On y cherche les "trous" (minima). La topologie de cette surface (présence de points selles, de plateaux) détermine si le modèle va apprendre vite ou rester bloqué.
    - **Normalisation des données (Input Normalization) :** Si les variables d'entrée ont des échelles très différentes (ex: une entre 0 et 1, l'autre entre 0 et 1000), la fonction de plusieurs variables devient "étirée" dans une direction. Cela rend l'optimisation par descente de gradient très difficile. C'est pourquoi on ramène toutes les variables à la même échelle.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]], [[Jalon 18 (Continuité des fonctions d'une variable réelle).md]]
- **Concepts Futurs dépendants :** [[Jalon 45 (Différentiabilité).md]], [[Jalon 121 (Ensembles convexes).md]]
