---
title: "Exercice 9 - Topologie de l'ensemble des continuités"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 9 - Continuité et fonction de Dirichlet

**Énoncé :**
Soit $f : \mathbb{R} \to \mathbb{R}$ continue telle que $f(x) = 0$ pour tout $x \in \mathbb{Q}$. Montrer rigoureusement que $f(x) = 0$ pour tout $x \in \mathbb{R}$.

**Démonstration pas à pas :**
1. Soit $x \in \mathbb{R} \setminus \mathbb{Q}$.
2. Puisque $\mathbb{Q}$ est dense dans $\mathbb{R}$, on peut construire une suite $(q_n)$ de rationnels telle que $q_n \to x$.
3. Comme $f$ est continue, on a $\lim_{n \to \infty} f(q_n) = f(x)$.
4. Or, par hypothèse, pour tout $n$, $f(q_n) = 0$.
5. Donc la suite constante $(0)$ converge vers $f(x)$, ce qui implique $f(x) = 0$.
6. Ceci prouve qu'aucune fonction de type Dirichlet ne peut être continue (sauf si elle est identiquement nulle).
