---
title: "Exercice 02 : Intégration et mesure de comptage"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 02 : Intégration et mesure de comptage

**Difficulté :** $\bigstar\bigstar\star\star\star$

Soit $\mathbb{N}$ muni de la tribu $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu_c$, définie par $\mu_c(A) = \text{card}(A)$ si $A$ est fini, et $+\infty$ sinon.
Soit $f : \mathbb{N} \to \mathbb{R}_+$ définie par $f(n) = \frac{1}{2^n}$.
Exprimez l'intégrale de Lebesgue de $f$ par rapport à $\mu_c$ comme une somme de série et calculez sa valeur.

### Correction détaillée

1. L'espace est discret. Construisons une suite de fonctions simples.
   Pour tout $N \in \mathbb{N}$, définissons $s_N(n) = f(n)$ si $n \le N$ et $0$ sinon.
   $s_N$ est une fonction simple car elle prend un nombre fini de valeurs non nulles : $s_N = \sum_{k=0}^N \frac{1}{2^k} \mathbf{1}_{\{k\}}$.
2. Calculons l'intégrale de $s_N$ :
   $$ \int_{\mathbb{N}} s_N \, d\mu_c = \sum_{k=0}^N \frac{1}{2^k} \mu_c(\{k\}) $$
   Puisque $\mu_c(\{k\}) = 1$ pour tout singleton :
   $$ \int_{\mathbb{N}} s_N \, d\mu_c = \sum_{k=0}^N \frac{1}{2^k} $$
3. La fonction $f$ est la borne supérieure (et la limite croissante) de la suite $s_N$.
   Par la construction de l'intégrale (et le passage au supremum des fonctions simples qui minorant $f$), l'intégrale de Lebesgue coïncide avec la limite de l'intégrale des $s_N$ :
   $$ \int_{\mathbb{N}} f \, d\mu_c = \lim_{N \to \infty} \sum_{k=0}^N \frac{1}{2^k} $$
4. C'est la somme d'une série géométrique de raison $1/2$ et de premier terme 1.
   $$ \int_{\mathbb{N}} f \, d\mu_c = \frac{1}{1 - 1/2} = 2 $$
L'intégrale de Lebesgue généralise parfaitement les séries numériques pour la mesure de comptage.
