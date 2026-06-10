---
uuid: "jalon-95"
title: "Vecteurs gaussiens"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/fondations
prev: "[[Jalon 94 (Démonstration du théorème central limite).md]]"
next: "[[Jalon 96 (Livrable IA).md]]"
---

# Jalon 95 : Vecteurs gaussiens

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous lâchiez des gouttes de peinture du haut d'une échelle sur une toile posée au sol.
    - Si vous visez bien le centre, les gouttes vont former une tache ronde, plus dense au milieu et s'éclaircissant vers les bords (une loi Normale en 2D).
    - Maintenant, imaginez qu'il y ait du vent soufflant toujours dans la même direction. La tache va s'étirer pour devenir une ellipse.
    - Un **Vecteur Gaussien**, c'est la version mathématique de cette tache de peinture dans un espace à n dimensions.
    - La **Moyenne** vous dit où se trouve le centre de la tache.
    - La **Matrice de Covariance** vous donne la forme de la tache : est-elle ronde ? allongée ? penchée ? Elle résume comment les différentes dimensions (ex: la taille et le poids) sont liées entre elles.
- **Le "Pourquoi on a inventé ça" :** Dans la nature, les variables ne sont jamais isolées. Le climat dépend de la pression ET de la température. Pour modéliser ces dépendances de manière simple et puissante, on utilise les vecteurs gaussiens. C'est la brique de base de presque toutes les statistiques multidimensionnelles.
- **Visualisation :** Une colline en 3D (ou une "patate" en dimension supérieure). Si vous coupez cette colline par un plan horizontal, vous obtenez toujours une ellipse.

## 2. Formalisation

### A. Définition Fondamentale

Soit $X = (X_1, \dots, X_n)^T$ un vecteur aléatoire à valeurs dans $\mathbb{R}^n$.

> **Définition (Vecteur Gaussien) :**
> On dit que $X$ est un **vecteur gaussien** si toute combinaison linéaire de ses composantes est une variable aléatoire gaussienne réelle.
> $$\forall a \in \mathbb{R}^n, \quad a^T X = \sum_{i=1}^n a_i X_i \text{ suit une loi normale.}$$

### B. Caractérisation par la fonction caractéristique

> **Théorème :**
> La loi d'un vecteur gaussien $X$ est entièrement caractérisée par son vecteur espérance $\mu = \mathbb{E}[X]$ et sa matrice de covariance $\Sigma = \mathbb{E}[(X-\mu)(X-\mu)^T]$.
> Sa fonction caractéristique est :
> $$\phi_X(u) = \mathbb{E}[e^{i u^T X}] = \exp\left( i u^T \mu - \frac{1}{2} u^T \Sigma u \right)$$

### C. Densité de probabilité (Cas non dégénéré)

Si la matrice $\Sigma$ est inversible (définie positive), $X$ admet une densité par rapport à la mesure de Lebesgue sur $\mathbb{R}^n$ :
$$f_X(x) = \frac{1}{(2\pi)^{n/2} \sqrt{\det \Sigma}} \exp\left( -\frac{1}{2} (x-\mu)^T \Sigma^{-1} (x-\mu) \right)$$

## 3. Démonstrations

### Propriété : Transformation linéaire d'un vecteur gaussien

Montrons que si $X \sim \mathcal{N}(\mu, \Sigma)$ est un vecteur gaussien, alors $Y = AX + B$ (où $A \in \mathcal{M}_{p,n}$) est aussi un vecteur gaussien.

1. **Cadre :** On utilise la définition par les combinaisons linéaires. Soit $v \in \mathbb{R}^p$. On veut montrer que $v^T Y$ suit une loi normale.
2. **Développement :**
   $v^T Y = v^T (AX + B) = v^T A X + v^T B = (A^T v)^T X + \text{constante}$.
3. **Application de la définition :** Posons $a = A^T v \in \mathbb{R}^n$.
   Par hypothèse sur $X$, $a^T X$ est une variable normale réelle.
4. **Conclusion :** Ajouter une constante ($v^T B$) à une variable normale produit une autre variable normale. Donc $v^T Y$ est normale pour tout $v$. $Y$ est donc un vecteur gaussien.
5. **Paramètres de Y :**
   - $\mathbb{E}[Y] = A\mu + B$.
   - $Cov(Y) = A \Sigma A^T$.

## 4. Exercices d'Application

### Exercice 1 : Indépendance et Covariance
**Énoncé :** Soit $X = (X_1, X_2)^T$ un vecteur gaussien. Montrer que $X_1$ et $X_2$ sont indépendants si et seulement si leur covariance est nulle.
**Correction Détaillée :**
1. **Sens ($\implies$) :** Vrai pour toutes variables (Jalon 88).
2. **Sens ($\impliedby$) :** Si $Cov(X_1, X_2) = 0$, la matrice $\Sigma$ est diagonale : $\Sigma = \text{diag}(\sigma_1^2, \sigma_2^2)$.
3. La fonction caractéristique se factorise :
   $\phi_X(u_1, u_2) = \exp(i u^T \mu - \frac{1}{2} (u_1^2 \sigma_1^2 + u_2^2 \sigma_2^2)) = \phi_{X_1}(u_1) \cdot \phi_{X_2}(u_2)$.
4. Par le théorème d'injectivité (Jalon 93), la loi jointe est le produit des lois marginales. Donc $X_1$ et $X_2$ sont indépendants.
*Attention :* Ce résultat est **faux** si le couple $(X_1, X_2)$ n'est pas un vecteur gaussien (même si $X_1$ et $X_2$ sont individuellement gaussiens).

### Exercice 2 : Niveau Avancé (Loi du $\chi^2$)
**Énoncé :** Soit $X \sim \mathcal{N}(0, I_n)$. Quelle est l'espérance de $\|X\|^2$ ?
**Correction Détaillée :**
$\|X\|^2 = \sum_{i=1}^n X_i^2$. Par linéarité : $\mathbb{E}[\|X\|^2] = \sum \mathbb{E}[X_i^2]$.
Comme $X_i \sim \mathcal{N}(0, 1)$, $\mathbb{E}[X_i^2] = Var(X_i) + \mathbb{E}[X_i]^2 = 1 + 0 = 1$.
**Résultat :** $\mathbb{E}[\|X\|^2] = n$. En moyenne, un vecteur gaussien de dimension $n$ se trouve à une distance $\sqrt{n}$ de l'origine.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Le vecteur gaussien est le modèle de base pour les **modèles génératifs** et l'**inférence Bayésienne**.
- **Example Concret :**
    - **Analyse en Composantes Principales (PCA) :** On cherche les vecteurs propres de la matrice de covariance $\Sigma$ d'un vecteur gaussien. Cela revient à trouver les axes principaux de l'ellipse de probabilité.
    - **Variational Auto-Encoders (VAE) :** On force l'espace latent à suivre une loi $\mathcal{N}(0, I)$. L'encodeur prédit pour chaque image un vecteur de moyennes $\mu$ et un vecteur de variances $\sigma$ (diagonale de $\Sigma$).
    - **Processus Gaussiens (GP) :** C'est l'extension des vecteurs gaussiens à une dimension infinie. On les utilise en IA pour faire de la régression avec une estimation de l'incertitude (Bayesian Optimization).
    - **Kalman Filters :** Utilisés dans les robots et les voitures autonomes pour fusionner les données des capteurs. Chaque estimation de position est traitée comme un vecteur gaussien.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 93 (Fonctions caractéristiques).md]], [[Jalon 9 (Calcul matriciel).md]]
- **Concepts Futurs dépendants :** [[Jalon 129 (Optimisation stochastique).md]], [[Jalon 140 (Classifieur de Bayes optimal).md]]
