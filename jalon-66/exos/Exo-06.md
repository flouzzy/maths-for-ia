---
title: "Exercice 06 : Sous-additivité stricte pour les intégrales (Approche par fonctions simples)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 06 : Sous-additivité stricte pour les intégrales (Approche par fonctions simples)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soient $s, t$ deux fonctions simples positives. Prouver rigoureusement que $\int (s + t) \, d\mu = \int s \, d\mu + \int t \, d\mu$.

---

## Correction détaillée

1. **Décomposition canonique conjointe :**
Soit $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ et $t = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$ où les $(A_i)$ et $(B_j)$ forment des partitions mesurables de $X$.
Remarquons que les ensembles $E_{i,j} = A_i \cap B_j$ forment une nouvelle partition de $X$ constituée de $n \times m$ ensembles.

2. **Réécriture sur la partition fine :**
Sur chaque $E_{i,j}$, la fonction $s$ prend la valeur constante $a_i$ et la fonction $t$ prend la valeur constante $b_j$.
On peut donc réécrire les fonctions simples sur cette partition :
$s = \sum_{i,j} a_i \mathbf{1}_{E_{i,j}}$
$t = \sum_{i,j} b_j \mathbf{1}_{E_{i,j}}$
Leur somme est donc aussi une fonction simple qui s'écrit :
$s + t = \sum_{i,j} (a_i + b_j) \mathbf{1}_{E_{i,j}}$

3. **Calcul de l'intégrale :**
Par définition de l'intégrale (qui ne dépend pas du choix de la partition, bien que la forme canonique regroupe les termes de même valeur) :
$$ \int (s + t) \, d\mu = \sum_{i,j} (a_i + b_j) \mu(E_{i,j}) $$
$$ \int (s + t) \, d\mu = \sum_{i,j} a_i \mu(E_{i,j}) + \sum_{i,j} b_j \mu(E_{i,j}) $$

4. **Regroupement des termes :**
Par $\sigma$-additivité (et additivité finie) de $\mu$, à $i$ fixé, $\bigcup_{j} E_{i,j} = A_i \cap (\bigcup_j B_j) = A_i \cap X = A_i$. Donc $\sum_j \mu(E_{i,j}) = \mu(A_i)$.
Ainsi :
$$ \sum_{i,j} a_i \mu(E_{i,j}) = \sum_i a_i \left( \sum_j \mu(E_{i,j}) \right) = \sum_i a_i \mu(A_i) = \int s \, d\mu $$
De même pour $t$, d'où $\int (s + t) \, d\mu = \int s \, d\mu + \int t \, d\mu$.
