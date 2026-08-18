---
uuid: "exo-jalon-63-05"
title: "Exercice 5 : Série de mesures"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Série de mesures

## Énoncé

Soit $(X, \mathcal{A})$ un espace mesurable. Soit $(\mu_n)_{n \in \mathbb{N}}$ une suite de mesures sur cet espace. Soit $(\alpha_n)_{n \in \mathbb{N}}$ une suite de réels strictement positifs. On pose pour tout $A \in \mathcal{A}$ : $\nu(A) = \sum_{n=0}^{+\infty} \alpha_n \mu_n(A)$. Montrer rigoureusement que $\nu$ est une mesure.

## Correction Détaillée

1. **Mesure de l'ensemble vide :**
Puisque chaque $\mu_n$ est une mesure, $\mu_n(\emptyset) = 0$ pour tout $n$.
Alors $\nu(\emptyset) = \sum_{n=0}^{+\infty} \alpha_n \mu_n(\emptyset) = \sum_{n=0}^{+\infty} 0 = 0$.

2. **$\sigma$-additivité et théorème de Fubini-Tonelli pour les séries :**
Soit $(A_k)_{k \in \mathbb{N}}$ une suite d'ensembles deux à deux disjoints de $\mathcal{A}$.
Nous avons par définition de $\nu$ et par $\sigma$-additivité de chaque $\mu_n$ :
$$ \nu\left( \bigcup_{k=0}^{+\infty} A_k \right) = \sum_{n=0}^{+\infty} \alpha_n \mu_n\left( \bigcup_{k=0}^{+\infty} A_k \right) = \sum_{n=0}^{+\infty} \alpha_n \left( \sum_{k=0}^{+\infty} \mu_n(A_k) \right) $$
Ceci est une série double à termes positifs (car $\alpha_n > 0$ et $\mu_n \geq 0$). Le théorème d'interversion des sommes pour les séries à termes positifs (corollaire du théorème de Beppo-Levi / Fubini-Tonelli sur $\mathbb{N} \times \mathbb{N}$) nous autorise formellement à permuter l'ordre de sommation sans modifier la limite (finie ou infinie) :
$$ \nu\left( \bigcup_{k=0}^{+\infty} A_k \right) = \sum_{k=0}^{+\infty} \left( \sum_{n=0}^{+\infty} \alpha_n \mu_n(A_k) \right) = \sum_{k=0}^{+\infty} \nu(A_k) $$
La $\sigma$-additivité est donc pleinement démontrée. $\nu$ est une mesure valide. $\blacksquare$
