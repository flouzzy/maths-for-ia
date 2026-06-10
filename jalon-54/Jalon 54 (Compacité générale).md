---
uuid: "jalon-54"
title: "Compacité générale"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/convergence
prev: "[[Jalon 53 (Axiomes de séparation).md]]"
next: "[[Jalon 55 (Connexité).md]]"
---
# Jalon 54 : Compacité générale

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous vouliez surveiller une grande salle avec des caméras de sécurité. Chaque caméra a un champ de vision limité (un ouvert). Si la salle est **compacte**, cela signifie que peu importe le nombre infini de caméras que vous pourriez installer, vous pourrez toujours en choisir un nombre **fini** (disons 10 ou 20) qui suffiront à surveiller toute la salle sans laisser d'angle mort. C'est la propriété de "finitude cachée" dans l'infini.
- **Le "Pourquoi on a inventé ça" :** En mathématiques, on travaille souvent avec des objets infinis. La compacité est la propriété magique qui permet de traiter ces objets infinis comme s'ils étaient finis. C'est ce qui garantit qu'une fonction continue ne peut pas s'envoler vers l'infini et qu'elle atteint forcément son maximum et son minimum.
- **Visualisation :** Un élastique fermé. Vous pouvez le déformer, mais il reste "petit" et "complet". Contrairement à une droite qui s'étend à l'infini ou à un intervalle ouvert qui a des "trous" à ses extrémités.

## 2. Formalisation

### A. Définition de Borel-Lebesgue

Soit $(X, \mathcal{T})$ un espace topologique.

> **Définition 1 (Recouvrement) :**
> On appelle **recouvrement ouvert** de $X$ une famille d'ouverts $(U_i)_{i \in I}$ telle que $X = \bigcup_{i \in I} U_i$.

> **Définition 2 (Espace Compact) :**
> Un espace $X$ est dit **compact** s'il est de Hausdorff ($T_2$) et s'il vérifie la propriété de Borel-Lebesgue : de tout recouvrement ouvert de $X$, on peut extraire un recouvrement **fini**.
> $$\forall (U_i)_{i \in I} \in \mathcal{T}^I, \quad X = \bigcup_{i \in I} U_i \implies \exists J \subset I, J \text{ fini, } X = \bigcup_{j \in J} U_j$$

### B. Lien avec les suites

> **Théorème (Bolzano-Weierstrass généralisé) :**
> Dans un espace métrique, la compacité (Borel-Lebesgue) est équivalente à la compacité séquentielle : de toute suite, on peut extraire une sous-suite convergente.

### C. Le Théorème de Tychonoff

> **Théorème de Tychonoff (Version finie) :**
> Le produit d'un nombre fini d'espaces topologiques compacts est compact pour la topologie produit.

## 3. Démonstrations

### Démonstration : L'image continue d'un compact est compacte

1. **Cadre :** Soit $f : X \to Y$ une application continue. Supposons $X$ compact. Montrons que $K = f(X)$ est compact.
2. **Soit un recouvrement ouvert de K :** Soit $(V_i)_{i \in I}$ une famille d'ouverts de $Y$ telle que $K \subset \bigcup_{i \in I} V_i$.
3. **Retour dans X :** Par continuité de $f$, chaque $U_i = f^{-1}(V_i)$ est un ouvert de $X$.
   Comme $f(X) \subset \bigcup V_i$, alors $X \subset \bigcup f^{-1}(V_i) = \bigcup U_i$.
4. **Utilisation de la compacité de X :** Comme $X$ est compact, on peut extraire une sous-famille finie $J \subset I$ telle que $X = \bigcup_{j \in J} U_j$.
5. **Retour dans Y :**
   $f(X) = f(\bigcup_{j \in J} U_j) = \bigcup_{j \in J} f(U_j) = \bigcup_{j \in J} f(f^{-1}(V_j))$.
   Comme $f(f^{-1}(V_j)) \subset V_j$, on a $f(X) \subset \bigcup_{j \in J} V_j$.
6. **Conclusion :** On a extrait un sous-recouvrement fini. $f(X)$ est donc compact.

## 4. Exercices d'Application

### Exercice 1 : Compacité de $[0, 1]$
**Énoncé :** Utiliser la propriété de la borne supérieure pour montrer que $[0, 1]$ est compact (Lemme de Cousin).
**Correction Détaillée :**
Soit $\mathcal{U}$ un recouvrement ouvert. Soit $E = \{ x \in [0, 1] \mid [0, x] \text{ est recouvert par une sous-famille finie de } \mathcal{U} \}$.
$0 \in E$. $E$ est borné par 1. Soit $s = \sup E$.
On montre par l'absurde que $s=1$ et que $1 \in E$. Si $s < 1$, $s$ est dans un ouvert $U \in \mathcal{U}$, donc on peut trouver un $s' > s$ encore dans $U$ et recouvert, ce qui contredit le fait que $s$ est le supremum.

### Exercice 2 : Niveau Avancé (Intersection de compacts)
**Énoncé :** Montrer qu'une suite décroissante de fermés non vides dans un espace compact a une intersection non vide.
**Correction Détaillée :**
Soit $F_n$ une telle suite. Supposons $\bigcap F_n = \emptyset$.
Alors $X \setminus (\bigcap F_n) = \bigcup (X \setminus F_n) = X$.
Les $U_n = X \setminus F_n$ forment un recouvrement ouvert de $X$.
Par compacité, il existe $N$ tel que $\bigcup_{n=1}^N U_n = X$.
Comme les $F_n$ sont décroissants, les $U_n$ sont croissants, donc $U_N = X$.
Cela signifie que $X \setminus F_N = X$, donc $F_N = \emptyset$. Contradiction.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En apprentissage statistique, on cherche à minimiser le risque empirique $R_n(\theta)$. Pour garantir qu'il existe une solution optimale $\theta^*$, on suppose souvent que l'espace des paramètres $\Theta$ est **compact**.
- **Example Concret :**
    - **Existence de l'estimateur du Maximum de Vraisemblance (MLE) :** Si la vraisemblance est continue et que l'espace des paramètres est compact, le MLE existe toujours.
    - **Théorème d'Approximation Universelle :** On prouve qu'un réseau de neurones peut approcher n'importe quelle fonction continue sur un ensemble **compact**. La compacité est cruciale ici car sur un ensemble non borné, l'erreur pourrait diverger à l'infini.
    - **Généralisation :** Les bornes de généralisation (PAC Learning, Jalon 133) dépendent souvent de la "taille" de l'espace des fonctions. Si cet espace est compact, sa "Complexité de Rademacher" est finie, ce qui garantit que le modèle ne va pas sur-apprendre (overfitting) de manière catastrophique.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 35 (Caractérisation séquentielle des ouverts).md]], [[Jalon 53 (Axiomes de séparation).md]]
- **Concepts Futurs dépendants :** [[Jalon 56 (Espaces métriques complets).md]], [[Jalon 134 (Complexite des classes de fonctions).md]]
