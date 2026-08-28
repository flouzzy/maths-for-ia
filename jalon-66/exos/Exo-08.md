---
uuid: "jalon-66-exo-08"
title: "Exercice 8 - Jalon 66"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 8 : Intégrale infinie

**Énoncé :**
Sur l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, on considère la fonction $f(x) = \frac{1}{x} \mathbf{1}_{]0, 1]}(x)$.
1. Montrer que $f$ est mesurable positive.
2. Démontrer, en utilisant des minorations par des fonctions simples judicieuses, que $\int_{\mathbb{R}} f \, d\lambda = +\infty$.

**Corrigé :**

1. **Mesurabilité :**
   $f$ est continue sur l'ouvert $]0, 1]$, donc mesurable sur cet intervalle. Elle vaut 0 ailleurs. Donc $f$ est globale borélienne positive.

2. **Minoration par des fonctions simples :**
   Nous voulons prouver que le supremum $\sup \{ \int s \, d\lambda \mid s \in \mathcal{E}^+, 0 \le s \le f \}$ est infini.
   Il suffit de construire une suite de fonctions simples $s_n \le f$ telle que $\lim_{n \to +\infty} \int s_n \, d\lambda = +\infty$.

   L'idée est de découper l'intervalle $]0, 1]$ en morceaux de type $]1/(k+1), 1/k]$.
   Sur l'intervalle $I_k = ]1/(k+1), 1/k]$, la fonction $f(x) = 1/x$ est décroissante, donc son minimum est atteint à la borne supérieure $1/k$, et vaut $k$.
   Ainsi, pour $x \in I_k$, $f(x) \ge k$.

   Définissons pour un entier $N \ge 1$, la fonction simple $s_N$ :
   $$s_N(x) = \sum_{k=1}^N k \mathbf{1}_{]1/(k+1), 1/k]}(x)$$
   Clairement, $s_N \in \mathcal{E}^+$. De plus, par construction, pour $x \in ]1/(k+1), 1/k]$, $s_N(x) = k \le f(x)$. Ailleurs $s_N=0 \le f$.
   Donc $0 \le s_N \le f$.

   Calculons l'intégrale de $s_N$ :
   $$\int_{\mathbb{R}} s_N \, d\lambda = \sum_{k=1}^N k \times \lambda\left(\left]\frac{1}{k+1}, \frac{1}{k}\right]\right)$$
   La longueur de l'intervalle est $\frac{1}{k} - \frac{1}{k+1} = \frac{k+1-k}{k(k+1)} = \frac{1}{k(k+1)}$.
   Ainsi :
   $$\int_{\mathbb{R}} s_N \, d\lambda = \sum_{k=1}^N k \times \frac{1}{k(k+1)} = \sum_{k=1}^N \frac{1}{k+1}$$

   On reconnaît la somme partielle de la série harmonique. Quand $N \to +\infty$, cette somme tend vers $+\infty$.
   $$\lim_{N \to +\infty} \int_{\mathbb{R}} s_N \, d\lambda = \sum_{k=1}^{+\infty} \frac{1}{k+1} = +\infty$$

   Puisque l'intégrale de $f$ est le supremum des intégrales des fonctions simples qui la minorent, on a :
   $$\int_{\mathbb{R}} f \, d\lambda \ge \int_{\mathbb{R}} s_N \, d\lambda \quad \forall N$$
   Donc $\int_{\mathbb{R}} f \, d\lambda = +\infty$.
   La fonction $f(x) = 1/x$ n'est pas intégrable sur $]0, 1]$.
