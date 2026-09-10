---
uuid: "jalon-67-exo-03"
title: "Exercice 03 - Application avec la fonction indicatrice"
difficulty: "\bigstar\bigstar\star\star\star"
---

# Exercice 03 - Application avec la fonction indicatrice

## Énoncé

Soit $\mu$ une mesure finie sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. On pose $f_n(x) = \mathbf{1}_{[-n, n]}(x)$.
Que peut-on dire de $\lim_{n \to \infty} \int_{\mathbb{R}} f_n d\mu$ ?

## Correction Détaillée

1. **Nature de la suite :**
$f_n$ est la fonction indicatrice de l'intervalle $[-n, n]$. Pour tout $x$, $f_n(x) \in \{0, 1\}$, donc $f_n \ge 0$.
De plus, $[-n, n] \subset [-(n+1), n+1]$, donc $\mathbf{1}_{[-n, n]} \le \mathbf{1}_{[-(n+1), n+1]}$.
La suite $(f_n)$ est donc une suite croissante de fonctions mesurables positives.

2. **Limite simple :**
Pour tout réel $x$, il existe un entier $N$ tel que pour tout $n \ge N$, $x \in [-n, n]$.
Ainsi, $\lim_{n \to \infty} f_n(x) = 1$.

3. **Application du TCM :**
Par le théorème de convergence monotone,
$$\lim_{n \to \infty} \int_{\mathbb{R}} f_n d\mu = \int_{\mathbb{R}} \lim_{n \to \infty} f_n d\mu = \int_{\mathbb{R}} 1 d\mu = \mu(\mathbb{R}).$$
Ceci traduit simplement la continuité croissante de la mesure $\mu$.
