---
uuid: "jalon-66-exo-02"
title: "Exercice 2 - Jalon 66"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 2 : Intégration par rapport à la mesure de Dirac

**Énoncé :**
Soit $\delta_a$ la mesure de Dirac au point $a \in \mathbb{R}$, définie sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ par $\delta_a(A) = 1$ si $a \in A$, et $0$ sinon.
Soit $f : \mathbb{R} \to \mathbb{R}_+$ une fonction mesurable positive.
Démontrer que $\int_{\mathbb{R}} f \, d\delta_a = f(a)$.

**Corrigé :**
Nous allons procéder par construction ascendante, fidèle à la définition de l'intégrale de Lebesgue.

**Étape 1 : Pour une fonction indicatrice**
Soit $A \in \mathcal{B}(\mathbb{R})$ et $f = \mathbf{1}_A$. Par définition :
$$\int_{\mathbb{R}} \mathbf{1}_A \, d\delta_a = 1 \times \delta_a(A) = \begin{cases} 1 & \text{si } a \in A \\ 0 & \text{si } a \notin A \end{cases}$$
Or, par définition de la fonction indicatrice, $\mathbf{1}_A(a) = 1$ si $a \in A$ et $0$ sinon.
Donc $\int_{\mathbb{R}} \mathbf{1}_A \, d\delta_a = \mathbf{1}_A(a)$.

**Étape 2 : Pour une fonction simple positive**
Soit $s = \sum_{i=1}^n c_i \mathbf{1}_{A_i}$ une fonction simple positive (les $A_i$ forment une partition).
Par linéarité de l'intégrale pour les fonctions simples :
$$\int_{\mathbb{R}} s \, d\delta_a = \sum_{i=1}^n c_i \int_{\mathbb{R}} \mathbf{1}_{A_i} \, d\delta_a = \sum_{i=1}^n c_i \mathbf{1}_{A_i}(a)$$
Or, par évaluation de la fonction $s$ au point $a$ :
$$s(a) = \sum_{i=1}^n c_i \mathbf{1}_{A_i}(a)$$
Donc $\int_{\mathbb{R}} s \, d\delta_a = s(a)$.

**Étape 3 : Pour une fonction mesurable positive quelconque**
Soit $f \in \mathcal{M}_+$. Par définition :
$$\int_{\mathbb{R}} f \, d\delta_a = \sup \left\lbrace \int_{\mathbb{R}} s \, d\delta_a \mid s \in \mathcal{E}^+, \, 0 \le s \le f \right\rbrace$$
D'après l'Étape 2, $\int_{\mathbb{R}} s \, d\delta_a = s(a)$. Ainsi :
$$\int_{\mathbb{R}} f \, d\delta_a = \sup \{s(a) \mid s \in \mathcal{E}^+, \, 0 \le s \le f\}$$
Puisque $0 \le s \le f$, on a $s(a) \le f(a)$ pour tout $s$. Donc le supremum est majoré par $f(a)$.
De plus, il existe une suite croissante de fonctions simples $(s_n)$ qui converge ponctuellement vers $f$ (théorème d'approximation). Pour cette suite, $s_n(a) \to f(a)$.
Le supremum est donc exactement atteint à la limite :
$$\int_{\mathbb{R}} f \, d\delta_a = f(a)$$
