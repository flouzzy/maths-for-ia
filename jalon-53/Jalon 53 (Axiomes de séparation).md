---
uuid: "jalon-53"
title: "Axiomes de séparation"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/abstraction
prev: "[[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]"
next: "[[Jalon 54 (Compacité générale).md]]"
---

# Jalon 53 : Axiomes de séparation

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez une fête où tout le monde est habillé exactement pareil. Si vous voyez deux personnes au loin, comment être sûr que ce sont bien deux individus différents et pas une illusion d'optique ? Les **Axiomes de séparation**, c'est comme une règle de politesse pour l'espace : pour que l'espace soit "propre" (Hausdorff), il faut que pour n'importe quelles deux personnes distinctes, on puisse dessiner deux cercles autour d'elles qui ne se touchent pas. Chacun a sa "bulle privée". Si l'espace ne respecte pas ça, il devient flou : deux points peuvent être si proches qu'on ne peut plus les distinguer avec des voisinages.
- **Le "Pourquoi on a inventé ça" :** En topologie générale, certains espaces sont pathologiques. Sans axiome de séparation, une suite de nombres pourrait converger vers deux cibles différentes en même temps ! C'est catastrophique pour le calcul. On a donc défini des niveaux de "séparation" pour garantir que nos objets mathématiques se comportent de manière saine.
- **Visualisation :** Deux points $x$ et $y$, entourés chacun par un nuage (ouvert) tel que les deux nuages sont totalement disjoints.

## 2. Formalisation

Soit $(X, \mathcal{T})$ un espace topologique.

### A. L'Espace de Hausdorff ($T_2$)

C'est l'axiome le plus important en analyse.

> **Définition (Espace $T_2$ ou de Hausdorff) :**
> On dit que $X$ est un **espace de Hausdorff** si pour tous $x, y \in X$ tels que $x \neq y$, il existe un voisinage $U$ de $x$ et un voisinage $V$ de $y$ tels que :
> $$U \cap V = \emptyset$$

### B. Autres Axiomes (Pour culture)

1. **$T_0$ (Kolmogorov) :** Pour deux points distincts, au moins l'un a un voisinage qui ne contient pas l'autre.
2. **$T_1$ (Fréchet) :** Chaque point a un voisinage qui ne contient pas l'autre (équivaut à dire que les singletons sont fermés).
3. **Hiérarchie :** $T_2 \implies T_1 \implies T_0$.

### C. Propriétés des Espaces de Hausdorff

> **Théorème (Unicité de la limite) :**
> Dans un espace de Hausdorff, si une suite $(x_n)$ converge, alors sa limite est **unique**.

> **Théorème (Singletons) :**
> Dans un espace de Hausdorff, tout singleton $\{x\}$ est un ensemble **fermé**.

## 3. Démonstrations

### Démonstration : Unicité de la limite dans un espace $T_2$

1. **Cadre :** Soit $(x_n)$ une suite dans un espace de Hausdorff $X$. Supposons par l'absurde que $x_n \to L_1$ et $x_n \to L_2$ avec $L_1 \neq L_2$.
2. **Utilisation de l'axiome $T_2$ :** Comme $L_1 \neq L_2$, il existe un ouvert $U$ contenant $L_1$ et un ouvert $V$ contenant $L_2$ tels que $U \cap V = \emptyset$.
3. **Application de la définition de limite :**
   - Comme $x_n \to L_1$, il existe un rang $N_1$ tel que pour $n \ge N_1$, $x_n \in U$.
   - Comme $x_n \to L_2$, il existe un rang $N_2$ tel que pour $n \ge N_2$, $x_n \in V$.
4. **Conclusion :** Pour tout $n \ge \max(N_1, N_2)$, on a $x_n \in U \cap V$. Or $U \cap V = \emptyset$. C'est une contradiction. Donc la limite est unique.

### Démonstration : Tout espace métrique est Hausdorff

1. **Cadre :** Soit $(X, d)$ un espace métrique. Soient $x, y \in X$ avec $x \neq y$.
2. **Choix du rayon :** Posons $r = d(x, y)$. Comme $x \neq y$, $r > 0$.
3. **Construction des ouverts :** Posons $\epsilon = r/3$. Considérons les boules ouvertes $B(x, \epsilon)$ et $B(y, \epsilon)$.
4. **Vérification de la séparation :** Supposons qu'il existe $z \in B(x, \epsilon) \cap B(y, \epsilon)$.
   Alors $d(x, z) < \epsilon$ et $d(y, z) < \epsilon$.
   Par inégalité triangulaire : $d(x, y) \le d(x, z) + d(z, y) < 2\epsilon = \frac{2}{3} r$.
5. **Conclusion :** On obtient $r < \frac{2}{3} r$, ce qui est impossible. Donc les boules sont disjointes. L'espace est Hausdorff.

## 4. Exercices d'Application

### Exercice 1 : La droite avec un point doublé
**Énoncé :** On prend deux copies de $\mathbb{R}$, notées $\mathbb{R}_a$ et $\mathbb{R}_b$. On identifie chaque $x \in \mathbb{R}_a \setminus \{0\}$ avec son correspondant dans $\mathbb{R}_b$. On obtient un espace $X$ qui ressemble à la droite réelle, mais avec "deux origines" $0_a$ et $0_b$. Cet espace est-il Hausdorff ?
**Correction Détaillée :**
Non. Tout voisinage de $0_a$ contient un intervalle du type $]-\epsilon, \epsilon[ \setminus \{0\}$. De même pour $0_b$. Ces deux voisinages se rencontreront toujours sur les points $x \neq 0$. On ne peut pas séparer les deux zéros. C'est l'exemple type d'un espace non-Hausdorff.

### Exercice 2 : Niveau Avancé (Graphe d'une fonction)
**Énoncé :** Soit $f : X \to Y$ continue. Montrer que si $Y$ est Hausdorff, alors le graphe de $f$, $\Gamma = \{ (x, f(x)) \mid x \in X \}$, est un fermé de $X \times Y$.
**Correction Détaillée :**
On montre que le complémentaire est ouvert. Soit $(x, y) \notin \Gamma$, donc $y \neq f(x)$. Comme $Y$ est Hausdorff, il existe $V_y$ et $V_{f(x)}$ disjoints. Par continuité, $U = f^{-1}(V_{f(x)})$ est un ouvert contenant $x$. Alors $U \times V_y$ est un voisinage de $(x, y)$ qui ne rencontre pas le graphe.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, la séparation est liée à l'**Identifiabilité des paramètres**. Si l'espace des modèles n'est pas "bien séparé", on ne peut pas garantir que l'apprentissage va converger vers une solution unique et stable.
- **Exemple Concret :**
    - **Modèles de Mélange (Gaussian Mixture Models) :** Si on ne définit pas d'ordre sur les composantes, le modèle est non-identifiable (on peut permuter les étiquettes des clusters sans changer la probabilité). L'espace des paramètres devient un espace quotient qui peut perdre certaines propriétés de séparation si on n'y prend pas garde.
    - **Embedding Disentanglement :** Dans les VAE ou les représentations auto-supervisées, on cherche à ce que chaque dimension du vecteur latent représente une caractéristique unique et "séparable" des autres. On veut éviter que deux concepts sémantiquement différents soient topologiquement inséparables dans l'espace latent.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 49 (Espaces topologiques généraux).md]], [[Jalon 51 (Espaces métriques).md]]
- **Concepts Futurs dépendants :** [[Jalon 54 (Compacité générale).md]], [[Jalon 73 (Définition des espaces Lp).md]]
