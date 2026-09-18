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

## 1. Formalisation Mathématique de l'Information

La divergence de Kullback-Leibler (ou entropie relative) est une mesure asymétrique de la dissimilitude entre deux distributions de probabilités $P$ et $Q$. Issu de la théorie de l'information (Shannon, 1948), ce concept quantifie l'excès d'information ou la pénalité asymptotique subie lorsque la distribution $Q$ est utilisée pour approximer la véritable distribution $P$.

En intelligence artificielle, la divergence de Kullback-Leibler est fondamentale. Elle sert de fonction objectif dans la minimisation de l'erreur d'approximation lors de l'entraînement de modèles génératifs (tels que les auto-encodeurs variationnels ou les modèles de diffusion) et constitue le fondement mathématique de la fonction de perte 	extit{Cross-Entropy}.

## 2. Formalisation

Soit $(\mathcal{X}, \mathcal{F}, \lambda)$ un espace mesuré (généralement $\mathbb{R}^n$ avec la mesure de Lebesgue). Soient $P$ et $Q$ deux mesures de probabilité sur cet espace.

### A. Définition via les densités

Supposons que $P$ et $Q$ admettent des densités $p$ et $q$ par rapport à $\lambda$.


### Exemples Concrets Immédiats

**Exemple 1 : Divergence entre deux pièces de monnaie (Variables de Bernoulli)**
Soit $P$ la loi d'une pièce biaisée avec $p=0.8$ (pile) et $1-p=0.2$ (face). Soit $Q$ la loi d'une pièce équilibrée $q=0.5$.
$$ D_{KL}(P || Q) = 0.8 \ln\left(\frac{0.8}{0.5}\right) + 0.2 \ln\left(\frac{0.2}{0.5}\right) \approx 0.8 \times 0.470 + 0.2 \times (-0.916) = 0.376 - 0.183 = 0.193 $$
L'asymétrie est visible si on calcule $D_{KL}(Q || P)$ :
$$ D_{KL}(Q || P) = 0.5 \ln\left(\frac{0.5}{0.8}\right) + 0.5 \ln\left(\frac{0.5}{0.2}\right) = 0.5 \times (-0.470) + 0.5 \times 0.916 = 0.223 $$
Ainsi, $D_{KL}(P || Q) \neq D_{KL}(Q || P)$.

**Exemple 2 : Divergence nulle pour des distributions identiques**
Si $P = Q$ (par exemple $p = 0.5, q = 0.5$), alors :
$$ D_{KL}(P || P) = 0.5 \ln(1) + 0.5 \ln(1) = 0 $$

**Exemple 3 : Divergence infinie (support non inclus)**
Si $P(X=1) = 1$ et $Q(X=1) = 0$, alors :
$$ D_{KL}(P || Q) = 1 \ln\left(\frac{1}{0}\right) = +\infty $$
Cela illustre l'absolue continuité requise : $P$ doit être absolument continue par rapport à $Q$ ($P \ll Q$).

**Exemple 4 : Deux lois uniformes**
Soient $P = \mathcal{U}([0, 1])$ et $Q = \mathcal{U}([0, 2])$.
Pour $x \in [0, 1]$, $p(x) = 1$ et $q(x) = 0.5$.
$$ D_{KL}(P || Q) = \int_{0}^{1} 1 \ln\left(\frac{1}{0.5}\right) dx = \ln(2) \approx 0.693 $$
À l'inverse, pour $x \in ]1, 2]$, $p(x) = 0$ et $q(x) = 0.5$. Comme $p(x)>0$ sur un ensemble où $q(x)=0$ n'arrive pas, mais pour $D_{KL}(Q || P)$, on intègre sur $[0, 2]$. Sur $]1, 2]$, $p(x) = 0$, d'où $D_{KL}(Q || P) = +\infty$.

**Exemple 5 : Divergence KL entre deux Gaussiennes univariées**
Soient $P = \mathcal{N}(\mu_1, \sigma_1^2)$ et $Q = \mathcal{N}(\mu_2, \sigma_2^2)$.
La formule analytique rigoureuse donne :
$$ D_{KL}(P || Q) = \ln\left(\frac{\sigma_2}{\sigma_1}\right) + \frac{\sigma_1^2 + (\mu_1 - \mu_2)^2}{2\sigma_2^2} - \frac{1}{2} $$
Si $\mu_1 = 0, \sigma_1 = 1$ et $\mu_2 = 2, \sigma_2 = 1$ :
$$ D_{KL}(P || Q) = \ln(1) + \frac{1 + 4}{2} - 0.5 = 2.0 $$
Cette forme quadratique par rapport aux moyennes explique l'efficacité de la KL pour approcher des gaussiennes.


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

## 3. Démonstrations

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

## 4. Exercices d'Application

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

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** La divergence KL est la fonction de perte par défaut pour tous les modèles probabilistes. Elle fait le lien entre la **Théorie de la Mesure** et la **Théorie de l'Information**.
- **Example Concret :**
    - **Variational Auto-Encoders (VAE) :** La fonction de coût est la somme d'une erreur de reconstruction et d'un terme KL qui force la distribution latente à être proche d'une Gaussienne standard.
    - **Apprentissage par Renforcement (PPO) :** L'algorithme Proximal Policy Optimization utilise une contrainte KL pour éviter que la nouvelle politique ne s'éloigne trop de l'ancienne, garantissant ainsi une mise à jour stable.
    - **Classification Multi-classe :** Le calcul de la perte Softmax est rigoureusement une minimisation de la divergence KL entre la distribution "one-hot" des étiquettes et les probabilités prédites par le réseau.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 71 (Théorèmes de Fubini-Tonelli).md]], [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]
- **Concepts Futurs dépendants :** [[Jalon 85 (Axiomes de Kolmogorov).md]], [[Jalon 140 (Classifieur de Bayes optimal).md]]
