---
uuid: "jalon-90"
title: "Les modes de convergence en probabilités"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon 89 (Lemmes de Borel-Cantelli).md]]"
next: "[[Jalon 91 (Inégalités de concentration).md]]"
---

# Jalon 90 : Les modes de convergence en probabilités

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous appreniez à tirer à l'arc. Chaque flèche tirée est une tentative ($X_n$). La cible est le centre ($X$).
    - **Convergence Presque Sûre :** Après beaucoup d'entraînement, vous finissez par mettre TOUTES vos flèches dans le mille, sans plus jamais faire d'erreur (sauf peut-être une fois tous les milliards d'années).
    - **Convergence en Probabilité :** Vous êtes devenu très bon. À n'importe quel tir, la chance de rater la cible est minuscule. Mais il n'est pas impossible qu'une fois de temps en temps, une bourrasque de vent dévie une flèche.
    - **Convergence dans $L^p$ :** Votre score moyen s'améliore. Si on fait la moyenne de la distance entre vos flèches et le centre, cette moyenne tend vers zéro.
    - **Convergence en Loi :** Vous ne visez pas forcément le centre, mais la "forme" de votre nuage de flèches finit par ressembler exactement à la forme du nuage d'un champion. Vous imitez son style, pas forcément sa précision point par point.
- **Le "Pourquoi on a inventé ça" :** En statistiques, on ne peut jamais être sûr à 100% de la valeur d'un paramètre. On a donc besoin de plusieurs langages pour dire à quel point on "s'approche" de la vérité. Certains langages sont très exigeants (presque sûre), d'autres sont plus souples (en loi).
- **Visualisation :** Un entonnoir. Dans les convergences fortes, les points s'accumulent au fond. Dans la convergence en loi, c'est la "cloche" de la distribution qui se déplace et se stabilise.

## 2. Formalisation & Rigueur Académique

Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires et $X$ une variable aléatoire définies sur $(\Omega, \mathcal{F}, P)$.

### A. Définitions des Convergences

> **1. Convergence Presque Sûre ($X_n \xrightarrow{p.s.} X$) :**
> $$P(\{ \omega \in \Omega \mid \lim_{n \to \infty} X_n(\omega) = X(\omega) \}) = 1$$

> **2. Convergence en Probabilité ($X_n \xrightarrow{P} X$) :**
> $$\forall \epsilon > 0, \quad \lim_{n \to \infty} P(|X_n - X| > \epsilon) = 0$$

> **3. Convergence dans $L^p$ ($X_n \xrightarrow{L^p} X$) :**
> $$\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0$$

> **4. Convergence en Loi ($X_n \xrightarrow{\mathcal{L}} X$) :**
> Pour toute fonction $h$ continue et bornée : $\lim_{n \to \infty} \mathbb{E}[h(X_n)] = \mathbb{E}[h(X)]$.
> Équivaut à $\lim F_{X_n}(x) = F_X(x)$ en tout point de continuité de $F_X$.

### B. Hiérarchie des convergences

> **Théorème (Implications) :**
> - $(X_n \xrightarrow{L^p} X) \implies (X_n \xrightarrow{P} X)$
> - $(X_n \xrightarrow{p.s.} X) \implies (X_n \xrightarrow{P} X)$
> - $(X_n \xrightarrow{P} X) \implies (X_n \xrightarrow{\mathcal{L}} X)$
> *Attention :* Les réciproques sont fausses en général.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : $L^p \implies P$ (Inégalité de Markov)

1. **Cadre :** Supposons $X_n \to X$ dans $L^p$. Soit $\epsilon > 0$.
2. **Utilisation de l'inégalité de Markov (Jalon 87) :**
   Appliquée à la variable positive $|X_n - X|^p$ avec le seuil $\epsilon^p$ :
   $$P(|X_n - X| > \epsilon) = P(|X_n - X|^p > \epsilon^p) \le \frac{\mathbb{E}[|X_n - X|^p]}{\epsilon^p}$$
3. **Passage à la limite :** Comme le numérateur tend vers 0 par hypothèse $L^p$, alors la probabilité tend vers 0.
4. **Conclusion :** La convergence en probabilité est démontrée.

### Démonstration : $P \implies \mathcal{L}$

1. **Idée :** Soit $h$ une fonction continue bornée. On veut montrer $|\mathbb{E}[h(X_n)] - \mathbb{E}[h(X)]| \to 0$.
2. **Décomposition :** On découpe l'intégrale sur l'événement $\{ |X_n - X| \le \delta \}$ (où $h(X_n) \approx h(X)$ par continuité) et son complémentaire (dont la probabilité tend vers 0 par hypothèse $P$).
3. **Conclusion :** On peut rendre l'écart arbitrairement petit.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : La "bosse" qui s'échappe
**Énoncé :** Soit $X_n$ une suite telle que $P(X_n = n) = 1/n$ and $P(X_n = 0) = 1 - 1/n$.
1. Étudier la convergence en probabilité.
2. Étudier la convergence dans $L^1$.
**Correction Détaillée :**
1. Soit $\epsilon \in ]0, 1[$. $P(|X_n - 0| > \epsilon) = P(X_n = n) = 1/n \to 0$.
   Donc $X_n \xrightarrow{P} 0$.
2. $\mathbb{E}[|X_n - 0|] = n \cdot P(X_n=n) + 0 \cdot P(X_n=0) = n \cdot (1/n) = 1$.
   La moyenne est constante et égale à 1, elle ne tend pas vers 0.
**Conclusion :** La suite converge en probabilité vers 0, mais pas dans $L^1$. La masse "s'envole" vers l'infini.

### Exercice 2 : Niveau Avancé (Lien P et p.s.)
**Énoncé :** Montrer que si $X_n \xrightarrow{P} X$, on peut extraire une sous-suite $(X_{\phi(n)})$ telle que $X_{\phi(n)} \xrightarrow{p.s.} X$.
**Correction Détaillée :**
C'est le même argument que pour le théorème de Riesz-Fischer (Jalon 75). On choisit $\phi(n)$ tel que $P(|X_{\phi(n)} - X| > 1/2^n) < 1/2^n$. La série des probabilités converge, et on conclut par le lemme de Borel-Cantelli (Jalon 89).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on distingue la **Consistance** (convergence en probabilité) de la **Consistance Forte** (convergence presque sûre) d'un algorithme d'apprentissage.
- **Example Concret :**
    - **Convergence de SGD :** On prouve que les poids du réseau $\theta_n$ convergent presque sûrement vers un minimum local si le pas d'apprentissage $\eta_n$ décroît selon les conditions de Robbins-Monro ($\sum \eta_n = \infty, \sum \eta_n^2 < \infty$).
    - **Théorème Central Limite :** C'est une convergence **en loi**. Il explique pourquoi l'erreur d'un modèle (somme de petites erreurs indépendantes) finit toujours par ressembler à une cloche de Gauss. C'est ce qui permet de définir des intervalles de confiance sur les prédictions.
    - **Quantification d'incertitude :** Dans les modèles de prédiction météo ou financière, on ne s'intéresse pas seulement à la convergence de la moyenne ($L^1$), mais à la convergence de toute la distribution (en loi) pour capturer les risques extrêmes.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 87 (Intégration et Espérance mathématique).md]], [[Jalon 89 (Lemmes de Borel-Cantelli).md]]
- **Concepts Futurs dépendants :** [[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]], [[Jalon 94 (Démonstration du théorème central limite).md]]
