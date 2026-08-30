---
title: "Exercice 1 : Application directe : Intégrale de Dirichlet"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 1 : Application directe : Intégrale de Dirichlet

## Énoncé

Soit l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.
Considérons la suite de fonctions $f_n(x) = \mathbf{1}_{\mathbb{Q} \cap [0, n]}(x)$.
1. Montrer que la suite $(f_n)$ est croissante et mesurable positive.
2. Déterminer sa limite ponctuelle $f$.
3. Calculer $\lim_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda$ et $\int_{\mathbb{R}} f d\lambda$. Le théorème de Beppo Levi est-il vérifié ?

## Correction

1. **Mesurabilité et monotonie :**
L'ensemble $\mathbb{Q} \cap [0, n]$ est dénombrable, donc c'est un borélien. L'indicatrice $f_n$ est donc une fonction mesurable. Elle ne prend que les valeurs 0 et 1, donc elle est positive.
Pour $x \in \mathbb{R}$ fixé, si $x \in \mathbb{Q} \cap [0, n]$, alors $x \in \mathbb{Q} \cap [0, n+1]$. Ainsi, $f_n(x) \le f_{n+1}(x)$. La suite est croissante.

2. **Limite ponctuelle :**
Fixons $x \in \mathbb{R}$. Si $x \in \mathbb{Q} \cap [0, +\infty[$, il existe $N \in \mathbb{N}$ tel que $x \le N$. Pour tout $n \ge N$, $f_n(x) = 1$. Donc $f(x) = 1$.
Si $x \notin \mathbb{Q} \cap [0, +\infty[$, alors pour tout $n$, $f_n(x) = 0$. Donc $f(x) = 0$.
La limite $f$ est la fonction indicatrice de $\mathbb{Q} \cap [0, +\infty[$.

3. **Intégration :**
L'ensemble $\mathbb{Q} \cap [0, n]$ est dénombrable, sa mesure de Lebesgue est nulle. Donc $\int_{\mathbb{R}} f_n d\lambda = 0$ pour tout $n$.
La limite est donc $\lim_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda = 0$.
L'ensemble $\mathbb{Q} \cap [0, +\infty[$ est aussi dénombrable, sa mesure est nulle. Donc $\int_{\mathbb{R}} f d\lambda = 0$.
On a bien $0 = 0$, le théorème de Beppo Levi est parfaitement vérifié.
