---
title: "Exercice 10 : Inégalité de Wirtinger"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Inégalité de Wirtinger (Généralisation $L^2$)

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f : \mathbb{R} \to \mathbb{C}$ de classe $\mathcal{C}^1$, $2\pi$-périodique, telle que $\int_0^{2\pi} f(t) dt = 0$.
Montrer, en utilisant l'identité de Parseval, que :
$$\int_0^{2\pi} |f(t)|^2 dt \le \int_0^{2\pi} |f'(t)|^2 dt$$
et déterminer les cas d'égalité.

## Correction Détaillée

1. **Preuve par Parseval :**
Puisque $f$ est $\mathcal{C}^1$, sa dérivée $f'$ est continue par morceaux, et les deux fonctions admettent des coefficients de Fourier $c_n(f)$ et $c_n(f')$.
D'après les théorèmes d'analyse de Fourier, $c_n(f') = in c_n(f)$.
La condition $\int_0^{2\pi} f(t) dt = 0$ implique que $c_0(f) = \frac{1}{2\pi} \int_0^{2\pi} f(t) dt = 0$.
Par l'identité de Parseval appliquée à $f$ et $f'$ :
$$ \frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt = \sum_{n \in \mathbb{Z} \setminus \{0\}} |c_n(f)|^2 $$
$$ \frac{1}{2\pi} \int_0^{2\pi} |f'(t)|^2 dt = \sum_{n \in \mathbb{Z} \setminus \{0\}} |in c_n(f)|^2 = \sum_{n \in \mathbb{Z} \setminus \{0\}} n^2 |c_n(f)|^2 $$

2. **Majoration :**
Pour tout entier non nul $n$, on a $n^2 \ge 1$. Par conséquent, $n^2 |c_n(f)|^2 \ge |c_n(f)|^2$.
En sommant sur tous les $n \neq 0$ :
$$ \sum_{n \in \mathbb{Z} \setminus \{0\}} |c_n(f)|^2 \le \sum_{n \in \mathbb{Z} \setminus \{0\}} n^2 |c_n(f)|^2 $$
Ce qui se traduit immédiatement, en multipliant par $2\pi$, par l'inégalité de Wirtinger cherchée.

3. **Cas d'égalité :**
L'égalité a lieu si et seulement si, pour tout $n \notin \{-1, 0, 1\}$, $c_n(f) = 0$.
Ainsi, $f$ doit être de la forme $f(t) = c_{-1} e^{-it} + c_1 e^{it}$, soit $f(t) = A \cos(t) + B \sin(t)$.
