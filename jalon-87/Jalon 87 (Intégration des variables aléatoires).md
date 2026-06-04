---
uuid: "jalon-87"
title: "Intégration et Espérance mathématique"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 86 (Variables aléatoires vues comme des applications mesurables).md]]"
next: "[[Jalon 88 (Indépendance d'événements).md]]"
---

# Jalon 87 : Intégration et Espérance mathématique

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous jouiez à un jeu de hasard où vous pouvez gagner différentes sommes d'argent.
    - L'**Espérance ($\mathbb{E}$)**, c'est le gain moyen que vous pouvez espérer si vous jouez une infinité de fois. C'est le "prix juste" d'un ticket de jeu.
    - Pour la calculer, on fait une moyenne pondérée : on multiplie chaque gain possible par sa chance d'arriver, puis on additionne tout.
    - La **Variance**, c'est une mesure de la "peur" ou de l'incertitude : est-ce que vos gains sont toujours proches de la moyenne, ou est-ce qu'ils sautent de très haut à très bas ?
- **Le "Pourquoi on a inventé ça" :** Les probabilités nous disent *ce qui peut arriver*. L'espérance nous dit *ce qui arrive en moyenne*. C'est l'outil qui permet de passer du hasard pur à la gestion de risque et à la prise de décision rationnelle.
- **Visualisation :** Le centre de gravité d'un objet. Si vous posez la distribution de probabilité sur une règle, l'espérance est le point précis où la règle tient en équilibre.

## 2. Formalisation & Rigueur Académique

Soit $(\Omega, \mathcal{F}, P)$ un espace de probabilité.

### A. Définition de l'Espérance

L'espérance est simplement l'intégrale de Lebesgue de la variable aléatoire sur l'univers $\Omega$.

> **Définition 1 (Espérance) :**
> Soit $X$ une variable aléatoire réelle. On dit que $X$ admet une **espérance** si elle est intégrable par rapport à $P$ ($X \in L^1(P)$). On note :
> $$\mathbb{E}[X] = \int_{\Omega} X(\omega) dP(\omega)$$

### B. Le Théorème de Transfert (Loi du statisticien conscient)

Ce théorème est fondamental car il permet de calculer l'espérance sans connaître l'univers $\Omega$, en utilisant seulement la loi de la variable sur $\mathbb{R}$.

> **Théorème de Transfert :**
> Soit $X$ une variable aléatoire de loi $P_X$. Pour toute fonction borélienne $g$ telle que $g(X)$ soit intégrable :
> $$\mathbb{E}[g(X)] = \int_{\mathbb{R}} g(x) dP_X(x)$$
> - Si $X$ est discrète : $\mathbb{E}[g(X)] = \sum x_i P(X=x_i)$.
> - Si $X$ a une densité $f$ : $\mathbb{E}[g(X)] = \int_{-\infty}^{+\infty} g(x) f(x) dx$.

### C. Moments et Variance

> **Définition 2 :**
> - Moment d'ordre $k$ : $m_k = \mathbb{E}[X^k]$.
> - **Variance :** $Var(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$.
> - Écart-type : $\sigma(X) = \sqrt{Var(X)}$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Linéarité de l'espérance

Montrons que $\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$.

1. **Cadre :** L'espérance est définie comme une intégrale de Lebesgue.
2. **Propriété de l'intégrale :** On a vu au Jalon 66 que l'intégrale de Lebesgue est une application linéaire sur l'espace des fonctions intégrables.
3. **Application directe :**
   $$\mathbb{E}[aX + bY] = \int_{\Omega} (aX(\omega) + bY(\omega)) dP(\omega)$$
   $$= \int_{\Omega} aX(\omega) dP(\omega) + \int_{\Omega} bY(\omega) dP(\omega)$$
   $$= a \int_{\Omega} X dP + b \int_{\Omega} Y dP = a\mathbb{E}[X] + b\mathbb{E}[Y]$$
4. **Conclusion :** L'espérance respecte toujours les combinaisons linéaires, même si les variables ne sont pas indépendantes.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Espérance d'une loi exponentielle
**Énoncé :** Soit $X$ de densité $f(x) = \lambda e^{-\lambda x}$ sur $[0, +\infty[$. Calculer $\mathbb{E}[X]$.
**Correction Détaillée :**
1. **Intégrale :** $\mathbb{E}[X] = \int_0^\infty x \lambda e^{-\lambda x} dx$.
2. **IPP :** $u=x, v'=\lambda e^{-\lambda x} \implies u'=1, v=-e^{-\lambda x}$.
3. **Calcul :** $\mathbb{E}[X] = [-x e^{-\lambda x}]_0^\infty + \int_0^\infty e^{-\lambda x} dx$.
4. **Résultat :** $0 + [- \frac{1}{\lambda} e^{-\lambda x} ]_0^\infty = 1/\lambda$.

### Exercice 2 : Niveau Avancé (Inégalité de Markov)
**Énoncé :** Montrer que pour toute V.A. positive $X$ et tout $a > 0$ : $P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$.
**Correction Détaillée :**
1. On remarque que $X \ge X \cdot \mathbf{1}_{X \ge a} \ge a \cdot \mathbf{1}_{X \ge a}$.
2. En prenant l'espérance (croissance de l'intégrale) :
   $\mathbb{E}[X] \ge \mathbb{E}[a \cdot \mathbf{1}_{X \ge a}] = a \cdot P(X \ge a)$.
3. On divise par $a$ pour obtenir le résultat.
**Utilité :** Cela permet de borner la probabilité d'un événement rare en ne connaissant que la moyenne.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Tout l'apprentissage automatique (Machine Learning) repose sur la minimisation d'une espérance : le **Risque Attendu** $R(\theta) = \mathbb{E}_{(x,y) \sim P} [ \mathcal{L}(f_\theta(x), y) ]$.
- **Example Concret :**
    - **Fonction de Perte (MSE) :** La Mean Squared Error est l'espérance du carré de l'erreur. Minimiser la MSE revient mathématiquement à chercher l'espérance conditionnelle $f(x) = \mathbb{E}[Y|X=x]$.
    - **Monte-Carlo Integration :** Comme on ne connaît pas la loi $P$, on remplace l'espérance théorique par une moyenne sur $N$ données : $\frac{1}{N} \sum \mathcal{L}_i$. La loi des grands nombres (Jalon 92) garantit que cette approximation converge vers la vraie espérance.
    - **Batch Normalization :** Cette technique d'IA consiste à recentrer les activations des neurones en soustrayant leur espérance et en divisant par leur écart-type ($\sigma$). Cela stabilise l'apprentissage en normalisant les moments de premier et second ordre.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 86 (Variables aléatoires vues comme des applications mesurables).md]], [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]
- **Concepts Futurs dépendants :** [[Jalon 90 (Les modes de convergence).md]], [[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]]
