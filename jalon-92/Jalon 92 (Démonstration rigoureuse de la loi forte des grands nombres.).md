---
uuid: "jalon-92"
title: "Loi forte des grands nombres (LFGN)"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon 91 (Inégalités de concentration).md]]"
next: "[[Jalon 93 (Fonctions caractéristiques).md]]"
---

# Jalon 92 : Loi forte des grands nombres (LFGN)

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez une pièce de monnaie truquée qui tombe sur "Pile" avec une chance sur trois.
    - Si vous la lancez 3 fois, vous pourriez très bien obtenir trois fois "Face". Vous auriez l'impression que la chance est de 0%.
    - Si vous la lancez 100 fois, vous aurez environ 33 fois "Pile".
    - Si vous la lancez 1 million de fois, vous aurez presque exactement 333 333 fois "Pile".
    - La **Loi forte des grands nombres**, c'est la promesse mathématique que le hasard finit par "s'annuler" quand on répète l'expérience. La moyenne de vos résultats va inévitablement s'écraser sur la vérité théorique (l'espérance). C'est ce qui rend le monde prévisible malgré le chaos individuel.
- **Le "Pourquoi on a inventé ça" :** Pour justifier les statistiques. On ne peut pas observer une "probabilité" directement dans la nature. On observe des fréquences. La LFGN est le pont qui nous permet de dire : "puisque j'ai observé 33% de Pile sur un grand nombre d'essais, alors la probabilité réelle est de 1/3".
- **Visualisation :** Un graphique montrant la moyenne glissante d'un lancer de dé. Au début, la courbe zigzague violemment entre 1 et 6. Plus le temps passe, plus elle se stabilise en une ligne droite horizontale parfaite à la hauteur 3,5.

## 2. Formalisation & Rigueur Académique

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires indépendantes et identiquement distribuées (I.I.D.) définies sur $(\Omega, \mathcal{F}, P)$. On note $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.

### A. Énoncé de la LFGN (Kolmogorov)

> **Théorème (Loi Forte des Grands Nombres) :**
> Si les $X_i$ admettent une espérance finie $\mu = \mathbb{E}[X_1]$, alors la moyenne empirique converge **presque sûrement** vers $\mu$ :
> $$P\left( \lim_{n \to \infty} \bar{X}_n = \mu \right) = 1$$

### B. Distinction avec la Loi Faible

La loi faible (Jalon 91) garantit seulement une convergence **en probabilité**. La loi forte est beaucoup plus puissante car elle garantit que pour presque chaque univers possible ($\omega$), la trajectoire complète de la moyenne converge.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration sous l'hypothèse d'un moment d'ordre 4 fini

Supposons $\mathbb{E}[X^4] < \infty$ et $\mu = 0$.

1. **Calcul du moment d'ordre 4 de la somme :**
   $S_n = \sum_{i=1}^n X_i$. On veut estimer $\mathbb{E}[S_n^4] = \mathbb{E}[ (\sum X_i)^4 ]$.
   En développant, par indépendance et comme $\mathbb{E}[X_i]=0$, les seuls termes non nuls sont de la forme $X_i^4$ and $X_i^2 X_j^2$.
   $$\mathbb{E}[S_n^4] = n \mathbb{E}[X_1^4] + 3n(n-1) (\mathbb{E}[X_1^2])^2 \le C n^2$$
2. **Inégalité de concentration :** Appliquons Markov (Jalon 91) à la variable $S_n^4$ :
   $$P(|\bar{X}_n| \ge \epsilon) = P(S_n^4 \ge (n\epsilon)^4) \le \frac{\mathbb{E}[S_n^4]}{n^4 \epsilon^4} \le \frac{Cn^2}{n^4 \epsilon^4} = \frac{C}{n^2 \epsilon^4}$$
3. **Application de Borel-Cantelli :**
   La série $\sum_{n=1}^\infty P(|\bar{X}_n| \ge \epsilon) \le \sum \frac{C}{n^2 \epsilon^4}$ converge.
   D'après le premier lemme de Borel-Cantelli (Jalon 89), l'événement $\{ |\bar{X}_n| \ge \epsilon \text{ infiniment souvent} \}$ a une probabilité nulle.
4. **Conclusion :** Pour tout $\epsilon$, $\bar{X}_n$ reste dans $[\mu-\epsilon, \mu+\epsilon]$ pour tout $n$ assez grand, presque sûrement. Donc $\bar{X}_n \xrightarrow{p.s.} \mu$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Monte-Carlo pour le calcul de $\pi$
**Énoncé :** On tire $n$ points $(x, y)$ uniformément dans le carré $[0, 1]^2$. On note $X_i = 1$ si $x^2 + y^2 \le 1$ and 0 sinon. Que vaut la limite de $4 \bar{X}_n$ ?
**Correction Détaillée :**
1. Les $X_i$ sont IID de loi de Bernoulli.
2. L'espérance $\mathbb{E}[X_1]$ est la probabilité que le point tombe dans le quart de disque unité.
   $\mathbb{E}[X_1] = \text{Aire(Disque)} / \text{Aire(Carré)} = (\pi/4) / 1 = \pi/4$.
3. Par la LFGN, $\bar{X}_n \xrightarrow{p.s.} \pi/4$.
4. Donc $4 \bar{X}_n \xrightarrow{p.s.} \pi$.
C'est la méthode de Monte-Carlo pour estimer $\pi$.

### Exercice 2 : Niveau Avancé (Le piège de la loi de Cauchy)
**Énoncé :** Soit $X_i$ des variables suivant une loi de Cauchy (densité $\frac{1}{\pi(1+x^2)}$). La LFGN s'applique-t-elle ?
**Correction Détaillée :**
Non. L'intégrale $\int |x| \frac{1}{1+x^2} dx$ diverge (en $\ln|x|$). La loi de Cauchy n'a pas d'espérance finie. En simulant, on remarque que la moyenne $\bar{X}_n$ continue de zigzaguer sauvagement sans jamais se stabiliser, quelle que soit la taille de $n$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** La LFGN est ce qui permet de passer de la théorie (la perte attendue sur tous les futurs possibles) à la pratique (la perte moyenne sur un jeu de données fixe).
- **Example Concret :**
    - **Validation Croisée (Cross-Validation) :** On suppose que la performance moyenne sur nos $k$ plis converge vers la performance réelle du modèle sur des données infinies.
    - **Large Batch Training :** Plus le "batch" utilisé pour calculer le gradient est grand, plus le gradient estimé est proche du vrai gradient théorique (par la LFGN). C'est pourquoi les batchs plus grands sont plus stables mais nécessitent plus de mémoire.
    - **Évaluation des LLM (Benchmarks) :** Quand on teste une IA sur 10 000 questions, on utilise la LFGN pour dire que son score de 85% reflète sa "vraie" compétence sur ce type de sujet.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 91 (Inégalités de concentration).md]], [[Jalon 89 (Lemmes de Borel-Cantelli).md]]
- **Concepts Futurs dépendants :** [[Jalon 94 (Démonstration du théorème central limite).md]], [[Jalon 133 (Modèle PAC).md]]
