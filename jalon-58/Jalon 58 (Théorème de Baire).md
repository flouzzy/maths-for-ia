---
uuid: "jalon-58"
title: "Théorème de Baire"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 57 (Théorème du point fixe de Banach).md]]"
next: "[[Jalon 59 (Topologie des espaces de fonctions).md]]"
---

# Jalon 58 : Théorème de Baire

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez une grande feuille de papier (un espace complet). Vous décidez de la percer avec une épingle. Un trou d'épingle, c'est minuscule, ça ne "remplit" rien (c'est nulle part dense). Maintenant, imaginez que vous perciez des millions, des milliards, voire une infinité (dénombrable) de trous. Le **Théorème de Baire** dit que, peu importe le nombre de trous que vous faites, il restera toujours de la "matière" sur votre feuille. Vous ne pourrez jamais faire disparaître toute la feuille en ne faisant que des trous isolés. La feuille est "trop solide" pour être détruite par des poussières de vide.
- **Le "Pourquoi on a inventé ça" :** Parfois, on veut prouver qu'un objet bizarre existe (ex: une fonction qui est continue partout mais qui n'a de pente nulle part). Au lieu de construire cet objet à la main, on prouve que l'ensemble des objets "normaux" est tout petit, et que la "grande majorité" des objets de l'espace sont bizarres. Baire est l'outil qui permet de dire : "ce que vous croyez impossible est en fait le cas général".
- **Visualisation :** Un fromage de Gruyère infini. Même avec une infinité de trous, il reste toujours du fromage entre les trous.

## 2. Formalisation & Rigueur Académique

### A. Ensembles Nulle Part Denses

Soit $(X, d)$ un espace métrique.

> **Définition 1 (Nulle part dense) :**
> Une partie $A \subset X$ est dite **nulle part dense** si son adhérence est d'intérieur vide : $\mathring{\bar{A}} = \emptyset$.
> Cela signifie que $\bar{A}$ ne contient aucune boule ouverte. C'est un ensemble "plein de trous".

### B. Le Théorème de Baire

> **Théorème de Baire (Version 1) :**
> Soit $X$ un espace métrique **complet**. La réunion dénombrable d'ensembles fermés d'intérieur vide est d'intérieur vide.
> $$\forall (F_n)_{n \in \mathbb{N}} \text{ fermés}, \quad (\forall n, \mathring{F}_n = \emptyset) \implies \left( \bigcup_{n \in \mathbb{N}} F_n \right)^{\circ} = \emptyset$$

> **Théorème de Baire (Version 2 - Ouverts denses) :**
> Dans un espace métrique complet, toute intersection dénombrable d'ouverts denses est dense.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Version des ouverts denses

1. **Cadre :** Soit $(U_n)_{n \in \mathbb{N}}$ une suite d'ouverts denses dans un complet $X$. Montrons que $D = \bigcap U_n$ est dense.
2. **Stratégie :** Soit $B_0$ une boule ouverte quelconque. Montrons qu'elle rencontre $D$.
3. **Construction de boules emboîtées :**
   - Comme $U_0$ est dense, $B_0 \cap U_0$ est un ouvert non vide. On peut donc y choisir une boule fermée $\bar{B}_1$ de rayon $r_1 < 1$.
   - Comme $U_1$ est dense, $\mathring{\bar{B}}_1 \cap U_1$ est non vide. On y choisit une boule fermée $\bar{B}_2 \subset \mathring{\bar{B}}_1 \cap U_1$ de rayon $r_2 < 1/2$.
   - Par récurrence, on construit une suite de boules fermées $(\bar{B}_n)$ telles que $\bar{B}_{n+1} \subset \bar{B}_n \cap U_n$ et $r_n \to 0$.
4. **Complétude :** Les centres des boules forment une suite de Cauchy (car les boules sont emboîtées et le rayon tend vers 0). Comme $X$ est complet, cette suite converge vers un point $x$.
5. **Conclusion :** Comme les boules sont fermées, $x \in \bar{B}_n$ pour tout $n$.
   Comme $\bar{B}_{n+1} \subset U_n$, alors $x \in U_n$ pour tout $n$.
   Donc $x \in \bigcap U_n$ et $x \in B_0$. L'intersection rencontre toutes les boules, elle est donc dense.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : $\mathbb{Q}$ n'est pas un $G_\delta$ de $\mathbb{R}$
**Énoncé :** Un ensemble est un $G_\delta$ s'il est une intersection dénombrable d'ouverts. Montrer que $\mathbb{Q}$ ne peut pas être un $G_\delta$ de $\mathbb{R}$.
**Correction Détaillée :**
Si $\mathbb{Q} = \bigcap U_n$, alors $\mathbb{R} \setminus \mathbb{Q} = \bigcup ( \mathbb{R} \setminus U_n )$. Les $\mathbb{R} \setminus U_n$ sont des fermés d'intérieur vide (car $\mathbb{Q}$ est dense). De plus, chaque singleton $\{q\}$ de $\mathbb{Q}$ est un fermé d'intérieur vide. Alors $\mathbb{R} = (\bigcup \{q\}) \cup (\bigcup (\mathbb{R} \setminus U_n))$ serait une union dénombrable de fermés d'intérieur vide. Par Baire, $\mathbb{R}$ serait d'intérieur vide. Contradiction.

### Exercice 2 : Niveau Avancé (Fonctions non dérivables)
**Énoncé :** On considère $E = \mathcal{C}([0, 1], \mathbb{R})$ muni de la norme uniforme. Montrer que l'ensemble des fonctions dérivables en au moins un point est un ensemble "maigre" (union dénombrable de nulle part denses).
**Correction Détaillée :**
C'est l'application la plus célèbre de Baire (via le théorème de Banach-Mazur). On définit $F_n = \{ f \in E \mid \exists x \in [0, 1], \forall h, |f(x+h)-f(x)| \le n|h| \}$. On montre que $F_n$ est fermé et d'intérieur vide. L'union des $F_n$ contient toutes les fonctions dérivables. Par Baire, le complémentaire (les fonctions nulle part dérivables) est dense !

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on s'intéresse à la **Généricité** des propriétés des réseaux de neurones. Une propriété est générique si elle est vraie sur un ouvert dense de l'espace des modèles.
- **Example Concret :**
    - **Initialisation des poids :** Dans l'étude des points selles des fonctions de perte, on prouve que pour "presque toutes" les initialisations (un ensemble dense au sens de Baire ou de la mesure de Lebesgue), la descente de gradient va éviter les points selles instables.
    - **Capacité de mémorisation :** On montre que pour un réseau assez large, la propriété de pouvoir mémoriser parfaitement $N$ points de données est générique : si vous prenez un réseau au hasard, il aura cette capacité avec une probabilité de 1, car l'ensemble des "mauvais" réseaux est de "première catégorie" (maigre).
    - **Stabilité Structurelle :** On veut que les prédictions d'une IA soient stables par rapport à des petites perturbations topologiques de l'espace des entrées. Le théorème de Baire aide à comprendre la structure des zones de stabilité.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 56 (Espaces métriques complets).md]], [[Jalon 50 (Opérateurs topologiques).md]]
- **Concepts Futurs dépendants :** [[Jalon 100 (Démonstration du théorème de Banach-Steinhaus).md]], [[Jalon 101 (Théorème de l'application ouverte et théorème du graphe fermé.).md]]
