---
uuid: "jalon-86"
title: "Variables aléatoires et Applications mesurables"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 85 (Axiomes de Kolmogorov).md]]"
next: "[[Jalon 87 (Intégration des variables aléatoires).md]]"
---

# Jalon 86 : Variables aléatoires et Applications mesurables

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous fassiez rouler un dé sur une table.
    - L'**Univers ($\Omega$)**, c'est tout ce qui se passe sur la table (le mouvement du dé, le vent, la poussière).
    - Une **Variable Aléatoire ($X$)**, c'est un traducteur qui ne regarde que la face du dé à l'arrêt et qui lui donne un score. Par exemple, si le dé affiche "6", le traducteur crie "TU AS GAGNÉ 10 POINTS !".
    - Pour que ce traducteur soit "honnête" (mesurable), il faut que si je lui pose une question simple sur le résultat (ex: "est-ce que j'ai gagné plus de 5 points ?"), il soit capable de me dire exactement quels lancers de dés satisfont cette condition.
- **Le "Pourquoi on a inventé ça" :** Dans la nature, les événements sont abstraits. On ne peut pas faire de calculs sur "il pleut" ou "le client achète". On doit transformer ces événements en **nombres** pour faire des statistiques. La théorie de la mesure garantit que cette transformation ne perd pas la notion de probabilité en route.
- **Visualisation :** Une flèche qui part d'un point dans un nuage abstrait ($\Omega$) et qui atterrit sur un point précis de la droite graduée ($\mathbb{R}$).

## 2. Formalisation & Rigueur Académique

Soit $(\Omega, \mathcal{F}, P)$ un espace de probabilité.

### A. Définition de la Variable Aléatoire

> **Définition 1 (Variable Aléatoire Réelle) :**
> Une variable aléatoire (V.A.R.) $X$ est une application mesurable de $(\Omega, \mathcal{F})$ vers $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.
> Cela signifie que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque est un événement mesurable :
> $$X^{-1}(B) = \{ \omega \in \Omega \mid X(\omega) \in B \} \in \mathcal{F}$$

### B. Loi d'une Variable Aléatoire

> **Définition 2 (Mesure Image / Loi) :**
> On appelle **loi de probabilité** de $X$ la mesure de probabilité $P_X$ sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ définie par :
> $$\forall B \in \mathcal{B}(\mathbb{R}), \quad P_X(B) = P(X^{-1}(B)) = P(X \in B)$$
> C'est l'image de la mesure $P$ par l'application $X$.

### C. Fonction de Répartition

> **Définition 3 (Fonction de Répartition) :**
> La fonction $F_X : \mathbb{R} \to [0, 1]$ définie par $F_X(x) = P(X \le x)$ caractérise entièrement la loi de $X$. Elle est croissante, continue à droite, et ses limites en $\pm \infty$ sont 0 et 1.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Critère de mesurabilité simplifié

Montrons qu'il suffit de vérifier la mesurabilité sur les intervalles du type $]-\infty, a]$ pour que $X$ soit une variable aléatoire.

1. **Cadre :** On sait que $X$ est mesurable si $X^{-1}(B) \in \mathcal{F}$ pour tout $B$ dans la tribu de Borel $\mathcal{B}(\mathbb{R})$.
2. **Utilisation de la tribu engendrée :** On sait (Jalon 62) que $\mathcal{B}(\mathbb{R})$ est la tribu engendrée par la famille $\mathcal{E} = \{ ]-\infty, a] \mid a \in \mathbb{R} \}$.
3. **Propriété des images réciproques :** L'opération d'image réciproque $X^{-1}$ préserve toutes les opérations ensemblistes (union, intersection, complémentaire).
   $X^{-1}(\cup B_n) = \cup X^{-1}(B_n)$ et $X^{-1}(B^c) = (X^{-1}(B))^c$.
4. **Stabilité :** La famille des ensembles $B$ tels que $X^{-1}(B) \in \mathcal{F}$ forme donc une tribu.
5. **Conclusion :** Si cette tribu contient $\mathcal{E}$ (les intervalles), elle contient nécessairement la plus petite tribu contenant $\mathcal{E}$, c'est-à-dire $\mathcal{B}(\mathbb{R})$.
   Donc, si $P(X \le a)$ est défini pour tout $a$, $X$ est une variable aléatoire.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Loi d'une transformation (Carré)
**Énoncé :** Soit $X$ une variable aléatoire de loi uniforme sur $[-1, 1]$. Déterminer la fonction de répartition de $Y = X^2$.
**Correction Détaillée :**
1. Pour $y < 0$, $F_Y(y) = P(X^2 \le y) = 0$.
2. Pour $y \in [0, 1]$ : $F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y})$.
3. Comme $X$ est uniforme sur $[-1, 1]$, sa densité est $1/2$.
   $P(-\sqrt{y} \le X \le \sqrt{y}) = \int_{-\sqrt{y}}^{\sqrt{y}} \frac{1}{2} dt = \sqrt{y}$.
4. Pour $y > 1$, $F_Y(y) = 1$.
**Résultat :** $F_Y(y) = \sqrt{y}$ sur $[0, 1]$. En dérivant, on obtient la densité $f_Y(y) = \frac{1}{2\sqrt{y}}$.

### Exercice 2 : Niveau Avancé (V.A. discrètes vs continues)
**Énoncé :** Montrer que toute fonction constante par morceaux sur une partition mesurable de $\Omega$ est une variable aléatoire.
**Correction Détaillée :**
C'est la définition des fonctions simples (Jalon 65). Comme une fonction simple est une somme finie de fonctions indicatrices d'ensembles mesurables, elle est mesurable. Les variables aléatoires discrètes sont exactement les fonctions simples (ou limites de fonctions simples).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, tout est variable aléatoire : les **Données ($X$)**, les **Poids ($W$)**, et les **Labels ($Y$)**. La mesurabilité garantit que l'on peut manipuler ces objets de manière cohérente à travers les couches du réseau.
- **Example Concret :**
    - **Data Preprocessing :** Faire un "Scaling" (ex: $(x-\mu)/\sigma$) revient à créer une nouvelle variable aléatoire $X'$ dont on connaît la loi à partir de celle de $X$.
    - **Activation Functions :** Appliquer une ReLU sur une sortie de neurone $Z$ crée une nouvelle variable $A = \max(0, Z)$. Si $Z$ suivait une loi Normale, $A$ suivra une loi "Rectified Gaussian". Le cadre des applications mesurables permet de calculer cette nouvelle distribution.
    - **Génération de bruit :** Dans les modèles de diffusion ou les GANs, on part d'une variable simple (Gaussienne blanche) et on apprend l'application mesurable $G$ la plus complexe possible pour que la loi de $G(Z)$ ressemble à la loi des images réelles.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 65 (Fonctions mesurables).md]], [[Jalon 85 (Axiomes de Kolmogorov).md]]
- **Concepts Futurs dépendants :** [[Jalon 87 (Intégration des variables aléatoires).md]], [[Jalon 90 (Les modes de convergence).md]]
