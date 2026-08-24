---
title: "Exercice 10 : Non intégrabilité de 1/x à l'infini (Mesure de Lebesgue vs Discrète)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Non intégrabilité de 1/x à l'infini (Mesure de Lebesgue vs Discrète)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f(x) = \frac{1}{x} \mathbf{1}_{[1, \infty)}(x)$. Démontrer, en construisant une minoration explicite par une suite de fonctions simples, que $\int_{\mathbb{R}} f \, d\lambda = +\infty$.

---

## Correction détaillée

1. **Construction d'une fonction simple minorante :**
Pour tout entier $N \ge 1$, on partitionne l'intervalle $[1, N]$ en sous-intervalles $[k, k+1)$ pour $k=1, \dots, N-1$.
Sur l'intervalle $[k, k+1)$, la fonction $f(x) = 1/x$ est décroissante, donc elle est minorée par sa valeur à la borne droite, soit $1/(k+1)$.
Définissons la fonction simple $s_N = \sum_{k=1}^{N-1} \frac{1}{k+1} \mathbf{1}_{[k, k+1)}$.

2. **Minoration de f :**
Par construction, pour tout $x$, $0 \le s_N(x) \le f(x)$. En effet, si $x \in [k, k+1)$, $f(x) = 1/x > 1/(k+1) = s_N(x)$. Si $x \notin [1, N)$, $s_N(x) = 0 \le f(x)$.

3. **Calcul de l'intégrale de $s_N$ :**
$$ \int s_N \, d\lambda = \sum_{k=1}^{N-1} \frac{1}{k+1} \lambda([k, k+1)) = \sum_{k=1}^{N-1} \frac{1}{k+1} \cdot 1 = \sum_{k=2}^N \frac{1}{k} $$

4. **Passage au supremum (Intégrale de Lebesgue) :**
Par définition de l'intégrale de Lebesgue pour $f$ :
$$ \int f \, d\lambda = \sup_{0 \le s \le f} \int s \, d\lambda \ge \int s_N \, d\lambda = \sum_{k=2}^N \frac{1}{k} $$
La suite de sommes partielles de la série harmonique $\sum_{k=2}^N \frac{1}{k}$ diverge vers $+\infty$ quand $N \to \infty$.
Ainsi, le supremum est infiniment grand :
$$ \int f \, d\lambda = +\infty $$
La fonction n'est pas Lebesgue-intégrable sur $[1, \infty)$.
