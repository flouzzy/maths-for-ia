---
title: "Exercice 4 : Mesure de Dirac et Beppo Levi"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 4 : Mesure de Dirac et Beppo Levi

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Problème

Soit $\mu$ la mesure sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ définie par $\mu = \sum_{k=1}^\infty \delta_k$. Calculer de façon détaillée l'intégrale $\int_{\mathbb{R}} e^{-x} d\mu(x)$.

## Démonstration et Résolution

### Étape 1 : Construction et approximation de la mesure
La mesure $\mu$ est définie comme une somme infinie de mesures de Dirac, qui sont des mesures positives.
Définissons la suite de mesures finies $\mu_n = \sum_{k=1}^n \delta_k$.
Pour tout borélien $A \in \mathcal{B}(\mathbb{R})$, la suite $\mu_n(A)$ est croissante et on a :
$$ \mu(A) = \lim_{n \to \infty} \mu_n(A) = \sum_{k=1}^\infty \delta_k(A) $$

### Étape 2 : Formuler en termes de suites de fonctions ou de mesures
L'intégrale d'une fonction positive $f(x) = e^{-x}$ par rapport à $\mu$ peut être vue par la linéarité sur la somme des mesures. Plus rigoureusement, définissons la suite de fonctions sur l'espace mesurable fondamental muni d'une mesure de comptage, ou utilisons la version mesure du théorème de Beppo Levi.
L'intégration par rapport à une somme dénombrable de mesures positives obéit à l'interversion série-intégrale.
$$ \int_{\mathbb{R}} f(x) d\mu(x) = \int_{\mathbb{R}} f(x) d\left(\sum_{k=1}^\infty \delta_k\right)(x) = \sum_{k=1}^\infty \int_{\mathbb{R}} f(x) d\delta_k(x) $$
Cette interversion est un corollaire direct du Théorème de Convergence Monotone appliqué à des fonctions étagées approchant $f$.

### Étape 3 : Calcul des intégrales individuelles sur Dirac
Par définition de l'intégrale par rapport à la mesure de Dirac centrée en $k$ :
$$ \int_{\mathbb{R}} e^{-x} d\delta_k(x) = e^{-k} $$

### Étape 4 : Évaluation de la série numérique
Il reste à calculer la somme de la série géométrique :
$$ S = \sum_{k=1}^\infty e^{-k} = \sum_{k=1}^\infty \left(\frac{1}{e}\right)^k $$
Il s'agit d'une série géométrique de premier terme $r = \frac{1}{e}$ et de raison $r = \frac{1}{e}$. La raison vérifie $|r| < 1$, donc la série est convergente et sa somme vaut :
$$ S = \frac{\text{Premier terme}}{1 - \text{Raison}} = \frac{e^{-1}}{1 - e^{-1}} $$
En multipliant le numérateur et le dénominateur par $e$, nous obtenons :
$$ S = \frac{1}{e - 1} $$
L'intégrale totale vaut donc $\frac{1}{e - 1}$.
