---
uuid: "jalon-67-exo-10"
title: "Exercice 10 - Probabilités et Temps d'arrêt"
difficulty: "\bigstar\bigstar\bigstar\bigstar\bigstar"
---

# Exercice 10 - Probabilités et Temps d'arrêt

## Énoncé

En théorie des probabilités, si $T$ est une variable aléatoire discrète à valeurs dans $\mathbb{N}^* \cup \{\infty\}$, montrer en utilisant le TCM que $\mathbb{E}[T] = \sum_{n=0}^\infty P(T > n)$.

## Correction Détaillée

1. **Définition de l'espérance :**
Par définition, $T = \sum_{n=1}^\infty n \mathbf{1}_{\{T=n\}}$. Son espérance est $\mathbb{E}[T] = \int_{\Omega} T d\mathbb{P}$.

2. **Réécriture de la variable aléatoire :**
Remarquons que l'entier $n$ peut s'écrire comme une somme de $1$ : $n = \sum_{k=1}^n 1$.
Ainsi, $T = \sum_{k=1}^T 1 = \sum_{k=1}^\infty \mathbf{1}_{\{T \ge k\}}$.
Pour chaque $\omega \in \Omega$, la somme infinie de droite compte exactement $1$ pour chaque entier $k$ tel que $T(\omega) \ge k$, ce qui donne bien la valeur $T(\omega)$.

3. **Application du TCM :**
Les variables $X_k = \mathbf{1}_{\{T \ge k\}}$ sont des fonctions mesurables (car $\{T \ge k\}$ est un événement mesurable) et positives.
D'après le corollaire du TCM pour les sommes, on peut intervertir l'espérance (qui est une intégrale sous la mesure $\mathbb{P}$) et la somme infinie :
$$\mathbb{E}[T] = \mathbb{E}\left[ \sum_{k=1}^\infty \mathbf{1}_{\{T \ge k\}} \right] = \sum_{k=1}^\infty \mathbb{E}[ \mathbf{1}_{\{T \ge k\}} ]$$

4. **Conclusion :**
L'espérance d'une fonction indicatrice est la probabilité de l'événement : $\mathbb{E}[ \mathbf{1}_{A} ] = \mathbb{P}(A)$.
Donc $\mathbb{E}[T] = \sum_{k=1}^\infty \mathbb{P}(T \ge k) = \sum_{n=0}^\infty \mathbb{P}(T > n)$ (en posant $n=k-1$).
C'est une formule fondamentale souvent appelée formule de l'espérance sans intégration (ou Area Formula en discret), rigoureusement démontrée grâce au TCM.
