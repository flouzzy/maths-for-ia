---
uuid: "jalon-72"
title: "Livrable IA T6 : Formalisation de la divergence de Kullback-Leibler"
year: 2
trimester: 6
tags:
  - math/probabilites
  - ia/theorie-information
prev: "[[Jalon 71 (Théorèmes de Fubini-Tonelli).md]]"
next: "[[Jalon 73 (Définition des espaces Lp).md]]"
---

# Jalon 72 : Livrable IA T6 : Formalisation de la divergence de Kullback-Leibler

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous deviez ranger des livres dans une bibliothèque.
    - Vous avez un plan idéal de rangement ($P$, la réalité).
    - Mais vous utilisez un plan simplifié et un peu faux ($Q$, votre modèle).
    - La **Divergence de Kullback-Leibler (KL)** mesure le "désordre" supplémentaire ou le temps perdu que vous allez subir à cause de l'erreur dans votre plan. C'est le coût de l'approximation. Si votre plan est parfait ($Q=P$), la perte est de zéro. Plus votre plan est mauvais, plus le score KL est élevé.
- **Le "Pourquoi on a inventé ça" :** En IA, on ne peut pas simplement dire "le modèle est proche de la réalité". On a besoin d'un nombre précis pour mesurer l'erreur. Comme nous travaillons avec des probabilités, on utilise une mesure issue de la théorie de l'information. C'est la "boussole" qui guide l'apprentissage : on modifie le modèle pour réduire le score KL.
- **Visualisation :** Deux cloches (Gaussiennes). La divergence KL est une surface qui mesure l'aire où les deux cloches ne se superposent pas, pondérée par l'importance (la probabilité) de chaque zone.

## 2. Formalisation & Rigueur Académique

Soit $(\mathcal{X}, \mathcal{F}, \lambda)$ un espace mesuré (généralement $\mathbb{R}^n$ avec la mesure de Lebesgue). Soient $P$ et $Q$ deux mesures de probabilité sur cet espace.

### A. Définition via les densités

Supposons que $P$ et $Q$ admettent des densités $p$ et $q$ par rapport à $\lambda$.

> **Définition (Divergence de Kullback-Leibler) :**
> On définit la divergence KL de $Q$ par rapport à $P$ par l'intégrale de Lebesgue :
> $$D_{KL}(P \| Q) = \int_{\mathcal{X}} p(x) \ln\left( \frac{p(x)}{q(x)} \right) d\lambda(x)$$
> *Condition :* On suppose que $P$ est absolument continue par rapport à $Q$ ($P \ll Q$), c'est-à-dire que $q(x)=0 \implies p(x)=0$. Sinon, la divergence est $+\infty$.

### B. Propriétés Fondamentales

> **Inégalité de Gibbs (Positivité) :**
> Pour toutes distributions de probabilité $P$ et $Q$ :
> $$D_{KL}(P \| Q) \ge 0$$
> Avec égalité $D_{KL}(P \| Q) = 0$ si et seulement si $P = Q$ presque partout.

> **Asymétrie :** Attention, en général $D_{KL}(P \| Q) \neq D_{KL}(Q \| P)$. Ce n'est donc pas une "distance" au sens métrique du terme (Jalon 51).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration de la positivité (via l'inégalité de Jensen)

1. **Réécriture :** $D_{KL}(P \| Q) = \int p(x) [-\ln(q(x)/p(x))] d\lambda(x) = \mathbb{E}_P [ -\ln(Q/P) ]$.
2. **Utilisation de la convexité :** La fonction $\phi(u) = -\ln(u)$ est strictement convexe sur $]0, +\infty[$.
3. **Inégalité de Jensen :** Pour toute variable aléatoire $U$ et fonction convexe $\phi$ :
   $$\mathbb{E}[\phi(U)] \ge \phi(\mathbb{E}[U])$$
4. **Application :** Posons $U = q(X)/p(X)$ où $X \sim P$.
   $$D_{KL}(P \| Q) = \mathbb{E}_P [ \phi(U) ] \ge \phi(\mathbb{E}_P[U])$$
5. **Calcul de l'espérance de U :**
   $$\mathbb{E}_P[U] = \int p(x) \frac{q(x)}{p(x)} d\lambda(x) = \int q(x) d\lambda(x) = 1$$ (car $Q$ est une probabilité).
6. **Conclusion :**
   $D_{KL}(P \| Q) \ge \phi(1) = -\ln(1) = 0$.
   La positivité est démontrée.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : KL entre deux Gaussiennes
**Énoncé :** Calculer $D_{KL}(P \| Q)$ pour $P = \mathcal{N}(\mu_1, \sigma^2)$ et $Q = \mathcal{N}(\mu_2, \sigma^2)$.
**Correction Détaillée :**
1. **Log-ratio :** $\ln(p(x)/q(x)) = \frac{1}{2\sigma^2} [ (x-\mu_2)^2 - (x-\mu_1)^2 ]$.
2. **Développement :** $(x-\mu_2)^2 - (x-\mu_1)^2 = x^2 - 2x\mu_2 + \mu_2^2 - (x^2 - 2x\mu_1 + \mu_1^2) = 2x(\mu_1 - \mu_2) + \mu_2^2 - \mu_1^2$.
3. **Intégration par rapport à P :** $\mathbb{E}_P[x] = \mu_1$.
   $D_{KL} = \frac{1}{2\sigma^2} [ 2\mu_1(\mu_1 - \mu_2) + \mu_2^2 - \mu_1^2 ] = \frac{1}{2\sigma^2} [ \mu_1^2 - 2\mu_1\mu_2 + \mu_2^2 ]$.
4. **Résultat :** $D_{KL}(P \| Q) = \frac{(\mu_1 - \mu_2)^2}{2\sigma^2}$.
La divergence augmente avec le carré de la distance entre les moyennes.

### Exercice 2 : Niveau Avancé (Lien avec l'Entropie Croisée)
**Énoncé :** Montrer que minimiser la Cross-Entropy entre des données et un modèle revient à minimiser la divergence KL.
**Correction Détaillée :**
$H(P, Q) = -\int p(x) \ln q(x) dx$.
On remarque que $D_{KL}(P \| Q) = \int p \ln p - \int p \ln q = -H(P) + H(P, Q)$.
Comme l'entropie des données $H(P)$ est constante par rapport aux paramètres du modèle, minimiser $H(P, Q)$ est équivalent à minimiser $D_{KL}$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** La divergence KL est la fonction de perte par défaut pour tous les modèles probabilistes. Elle fait le lien entre la **Théorie de la Mesure** et la **Théorie de l'Information**.
- **Example Concret :**
    - **Variational Auto-Encoders (VAE) :** La fonction de coût est la somme d'une erreur de reconstruction et d'un terme KL qui force la distribution latente à être proche d'une Gaussienne standard.
    - **Apprentissage par Renforcement (PPO) :** L'algorithme Proximal Policy Optimization utilise une contrainte KL pour éviter que la nouvelle politique ne s'éloigne trop de l'ancienne, garantissant ainsi une mise à jour stable.
    - **Classification Multi-classe :** Le calcul de la perte Softmax est rigoureusement une minimisation de la divergence KL entre la distribution "one-hot" des étiquettes et les probabilités prédites par le réseau.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 71 (Théorèmes de Fubini-Tonelli).md]], [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]
- **Concepts Futurs dépendants :** [[Jalon 85 (Axiomes de Kolmogorov).md]], [[Jalon 140 (Classifieur de Bayes optimal).md]]
