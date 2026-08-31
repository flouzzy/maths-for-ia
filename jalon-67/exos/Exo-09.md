---
title: "Généralisation à une suite non croissante avec inf"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---
# Généralisation à une suite non croissante avec inf
**Énoncé :**
Montrer que pour toute suite $(g_n)$ de fonctions mesurables positives, $\int \liminf_{n \to \infty} g_n d\mu \le \liminf_{n \to \infty} \int g_n d\mu$ (Lemme de Fatou) en utilisant le Théorème de Convergence Monotone.

**Correction :**
1. Posons $h_k(x) = \inf_{n \ge k} g_n(x)$.
2. Par définition, pour un $x$ fixé, l'infimum d'un ensemble qui rétrécit ne peut que croître, donc $h_k(x) \le h_{k+1}(x)$. La suite $(h_k)$ est croissante et positive.
3. La limite de $h_k$ est par définition la limite inférieure de $g_n$ : $\lim_{k \to \infty} h_k = \liminf g_n$.
4. Appliquons le TCM à la suite $(h_k)$ :
   $\int \liminf g_n d\mu = \lim_{k \to \infty} \int h_k d\mu$.
5. Or, par définition, $h_k(x) \le g_k(x)$ pour tout $k$. En intégrant, $\int h_k d\mu \le \int g_k d\mu$.
6. En prenant la limite inférieure des deux côtés :
   $\lim_{k \to \infty} \int h_k d\mu \le \liminf_{k \to \infty} \int g_k d\mu$.
7. D'où $\int \liminf g_n d\mu \le \liminf \int g_n d\mu$.
