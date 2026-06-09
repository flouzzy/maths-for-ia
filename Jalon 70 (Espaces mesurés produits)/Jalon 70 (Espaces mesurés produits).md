---
uuid: "jalon-70"
title: "Espaces mesurés produits"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/probabilites
prev: "[[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]"
next: "[[Jalon 71 (Théorèmes de Fubini-Tonelli).md]]"
---

# Jalon 70 : Espaces mesurés produits

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez deux règles. L'une mesure des longueurs sur un axe horizontal ($X$), l'autre mesure des longueurs sur un axe vertical ($Y$). Si vous croisez ces deux règles, vous créez un monde en 2D (le produit $X \times Y$).
    - Une **Tribu produit**, c'est décider que les "rectangles" (un ensemble de $X$ croisé avec un ensemble de $Y$) sont nos nouvelles briques de base pour mesurer des surfaces.
    - Une **Mesure produit**, c'est dire que la surface d'un rectangle est simplement sa largeur multipliée par sa hauteur.
    C'est la manière naturelle de construire des mesures complexes à partir de mesures simples.
- **Le "Pourquoi on a inventé ça" :** La plupart des phénomènes réels dépendent de plusieurs facteurs. Pour calculer le volume d'un objet, ou la probabilité que deux événements indépendants arrivent en même temps, on a besoin de savoir comment "multiplier" les mesures entre elles de manière rigoureuse.
- **Visualisation :** Un quadrillage. On définit la mesure sur chaque petit carreau, puis on étend cette définition à toutes les formes bizarres que l'on peut construire en assemblant des carreaux.

## 2. Formalisation

Soient $(X_1, \mathcal{F}_1, \mu_1)$ et $(X_2, \mathcal{F}_2, \mu_2)$ deux espaces mesurés.

### A. La Tribu Produit

> **Définition 1 (Rectangle mesurable) :**
> On appelle **rectangle mesurable** toute partie de $X_1 \times X_2$ de la forme $A_1 \times A_2$ où $A_1 \in \mathcal{F}_1$ et $A_2 \in \mathcal{F}_2$.

> **Définition 2 (Tribu Produit) :**
> La **tribu produit**, notée $\mathcal{F}_1 \otimes \mathcal{F}_2$, est la tribu engendrée par l'ensemble des rectangles mesurables sur $X_1 \times X_2$.

### B. La Mesure Produit

> **Théorème (Existence et Unicité) :**
> Si les mesures $\mu_1$ et $\mu_2$ sont **$\sigma$-finies**, alors il existe une unique mesure $\pi$ sur $(X_1 \times X_2, \mathcal{F}_1 \otimes \mathcal{F}_2)$, notée $\mu_1 \otimes \mu_2$, telle que pour tout rectangle mesurable $A_1 \times A_2$ :
> $$\pi(A_1 \times A_2) = \mu_1(A_1) \cdot \mu_2(A_2)$$

### C. Sections d'un ensemble

Soit $E \in \mathcal{F}_1 \otimes \mathcal{F}_2$. Pour tout $x \in X_1$, on définit la **section** de $E$ en $x$ par :
$$E_x = \{ y \in X_2 \mid (x, y) \in E \}$$
*Propriété :* Pour tout $x$, $E_x \in \mathcal{F}_2$ (la section d'un mesurable est mesurable).

## 3. Démonstrations

### Démonstration : Calcul de la mesure par intégration des sections

Montrons que $\pi(E) = \int_{X_1} \mu_2(E_x) d\mu_1(x)$.

1. **Cas des rectangles :** Soit $E = A_1 \times A_2$.
   - Si $x \in A_1$, alors $E_x = A_2$. Sa mesure est $\mu_2(A_2)$.
   - Si $x \notin A_1$, alors $E_x = \emptyset$. Sa mesure est 0.
   - Donc $\mu_2(E_x) = \mu_2(A_2) \mathbf{1}_{A_1}(x)$.
   - En intégrant par rapport à $\mu_1$ : $\int \mu_2(A_2) \mathbf{1}_{A_1}(x) d\mu_1 = \mu_2(A_2) \mu_1(A_1) = \pi(E)$.
2. **Généralisation :** On utilise le théorème des classes monotones (ou de transport de propriété). La propriété est vraie sur les rectangles, qui forment un $\pi$-système engendrant la tribu. Elle est stable par union dénombrable croissante et par passage au complémentaire.
3. **Conclusion :** La formule est vraie pour tout ensemble de la tribu produit. Cela montre que la mesure produit est "cohérente" avec l'intégration couche par couche.

## 4. Exercices d'Application

### Exercice 1 : Mesure de Lebesgue sur $\mathbb{R}^2$
**Énoncé :** On définit la mesure de Lebesgue sur $\mathbb{R}^2$ comme le produit $\lambda \otimes \lambda$. Calculer la mesure du triangle $T = \{ (x, y) \in [0, 1]^2 \mid y \le x \}$.
**Correction Détaillée :**
1. **Section :** Pour un $x$ fixé, $T_x = [0, x]$. Sa mesure de Lebesgue 1D est $\lambda(T_x) = x$.
2. **Intégration :** $\pi(T) = \int_0^1 \lambda(T_x) dx = \int_0^1 x dx$.
3. **Calcul :** $[x^2/2]_0^1 = 1/2$.
Le triangle occupe bien la moitié du carré unité.

### Exercice 2 : Niveau Avancé (Mesures non $\sigma$-finies)
**Énoncé :** Pourquoi la $\sigma$-finitude est-elle requise pour l'unicité ? (Contre-exemple avec la mesure de comptage sur $\mathbb{R}$).
**Correction Détaillée :**
Si l'une des mesures est la mesure de comptage sur un ensemble non dénombrable, on peut construire plusieurs mesures produits qui coïncident sur les rectangles mais diffèrent sur d'autres ensembles (comme la diagonale). C'est un piège classique qui souligne l'importance des hypothèses techniques.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on travaille presque exclusivement dans des espaces produits. Une image de $224 \times 224$ pixels est un point dans un espace produit de dimension 50 176.
- **Example Concret :**
    - **Indépendance Statistique :** Deux variables aléatoires $X$ et $Y$ sont indépendantes si et seulement si leur mesure de probabilité jointe $P_{X,Y}$ est égale à la mesure produit des marginales $P_X \otimes P_Y$. C'est la définition mathématique de l'absence de corrélation.
    - **Modèles Génératifs (GANs, VAEs) :** On essaie souvent de factoriser la distribution des données dans un espace latent où les dimensions sont indépendantes. Topologiquement, cela revient à forcer la mesure latente à être une mesure produit.
    - **Calcul de l'erreur moyenne (Risk) :** Le risque est une intégrale sur l'espace produit "Données $\times$ Étiquettes". Pour l'estimer, on suppose que les exemples sont "IID" (indépendants et identiquement distribués), ce qui permet d'utiliser la structure de mesure produit.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 63 (Définition axiomatique d'une mesure).md]], [[Jalon 62 (Algèbres).md]]
- **Concepts Futurs dépendants :** [[Jalon 71 (Théorèmes de Fubini-Tonelli).md]], [[Jalon 88 (Indépendance d'événements).md]]
