---
title: "Exercice 01 : Calcul élémentaire pour une fonction en escalier"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 01 : Calcul élémentaire pour une fonction en escalier

**Difficulté :** $\bigstar\star\star\star\star$

On munit $\mathbb{R}$ de la tribu borélienne et de la mesure de Lebesgue $\lambda$.
Soit $f : \mathbb{R} \to \mathbb{R}$ définie par $f(x) = 2 \cdot \mathbf{1}_{[0, 3]}(x) + 4 \cdot \mathbf{1}_{[3, 7]}(x) + 1 \cdot \mathbf{1}_{\{10\}}(x)$.
Calculez l'intégrale de Lebesgue $\int_{\mathbb{R}} f \, d\lambda$.

### Correction détaillée

1. La fonction $f$ ne prend qu'un nombre fini de valeurs positives : 2, 4, 1 et 0. Elle est donc étagée et positive.
2. Écrivons les ensembles de niveau disjoints :
   - Pour la valeur 2 : $A_1 = [0, 3]$. Sa mesure de Lebesgue est $\lambda([0, 3]) = 3 - 0 = 3$.
   - Pour la valeur 4 : $A_2 = ]3, 7]$ (on exclut 3 pour avoir des ensembles disjoints, mais la valeur ponctuelle en 3 ne change pas l'intégrale puisque $\lambda(\{3\}) = 0$. Adoptons $A_2 = ]3, 7]$). La mesure est $\lambda(A_2) = 7 - 3 = 4$.
   - Pour la valeur 1 : $A_3 = \{10\}$. Un singleton a une mesure de Lebesgue nulle : $\lambda(\{10\}) = 0$.
   - Pour la valeur 0 : $A_4 = \mathbb{R} \setminus ([0, 7] \cup \{10\})$.
3. Par définition de l'intégrale d'une fonction simple positive :
   $$ \int_{\mathbb{R}} f \, d\lambda = 2 \cdot \lambda(A_1) + 4 \cdot \lambda(A_2) + 1 \cdot \lambda(A_3) $$
   $$ \int_{\mathbb{R}} f \, d\lambda = 2 \cdot 3 + 4 \cdot 4 + 1 \cdot 0 $$
   $$ \int_{\mathbb{R}} f \, d\lambda = 6 + 16 + 0 = 22 $$
L'intégrale vaut 22.
