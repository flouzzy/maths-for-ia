---
title: "Exercice 8 : Échec de l'approximation avec des polynômes"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 8 : Échec de l'approximation avec des polynômes

## Énoncé

Le théorème de Leshno (1993) stipule que $\mathcal{N}_\sigma$ n'est pas dense si la fonction d'activation $\sigma$ est un polynôme. Démontrez formellement ce résultat.

## Correction Rigoureuse

**Étape 1 : Hypothèse polynomiale**
Supposons que $\sigma(x)$ est un polynôme de degré $d$. Alors on peut l'écrire $\sigma(x) = \sum_{k=0}^d c_k x^k$.

**Étape 2 : Expression du réseau**
Considérons le réseau à une couche cachée $G(x) = \sum_{i=1}^N \alpha_i \sigma(w_i^T x + b_i)$.
Substituons $\sigma$ par son expression polynomiale :
$$G(x) = \sum_{i=1}^N \alpha_i \sum_{k=0}^d c_k (w_i^T x + b_i)^k$$

**Étape 3 : Analyse du degré**
Puisque $(w_i^T x + b_i)^k$ est un polynôme à plusieurs variables de degré global au plus $k$, chaque terme de la double somme est un polynôme de degré global au plus $d$.
La combinaison linéaire d'un nombre fini (même grand) de polynômes de degré au plus $d$ reste un polynôme de degré au plus $d$.
Ainsi, quel que soit $N$, la fonction $G(x)$ appartient à l'espace vectoriel des polynômes multivariés de degré au plus $d$. Cet espace est de dimension finie.

**Étape 4 : Conclusion topologique**
L'espace vectoriel des polynômes de degré $\leq d$ est fermé dans $\mathcal{C}(K)$ (car il est de dimension finie). Or, l'espace des fonctions continues est de dimension infinie, et contient des polynômes de degré $d+1$, des fonctions transcendantes (sinus, exponentielle) qui ne peuvent pas être approchées uniformément à une précision arbitraire par des polynômes de degré uniformément borné.
L'ensemble $\mathcal{N}_\sigma$ est donc confiné dans un sous-espace fermé strict, il ne peut donc pas être dense dans $\mathcal{C}(K)$. $\blacksquare$
