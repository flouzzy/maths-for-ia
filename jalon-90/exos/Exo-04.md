---
uuid: "jalon-90-exo-04"
title: "Convergence en loi d'une variable uniforme"
---

# Exercice 4 : Convergence en loi d'une variable uniforme (Difficulté $\bigstar\bigstar\star\star\star$)

Soit $X_n$ une variable aléatoire suivant une loi uniforme discrète sur l'ensemble $\{ \frac{1}{n}, \frac{2}{n}, \dots, \frac{n}{n} \}$.
Démontrer que la suite $(X_n)$ converge en loi vers une variable aléatoire continue $X$ suivant la loi uniforme sur l'intervalle $[0, 1]$.

## Correction Pas-à-Pas

1. **Rappel des fonctions de répartition :**
   La loi limite conjecturée est $X \sim \mathcal{U}([0, 1])$. Sa fonction de répartition est :
   $$ F_X(x) = \mathbb{P}(X \leq x) = \begin{cases} 0 & \text{si } x < 0 \\ x & \text{si } 0 \leq x \leq 1 \\ 1 & \text{si } x > 1 \end{cases} $$
   Cette fonction est continue sur tout $\mathbb{R}$. Il suffit donc de montrer que $\lim_{n \to \infty} F_{X_n}(x) = F_X(x)$ pour tout $x \in \mathbb{R}$.

2. **Calcul de la fonction de répartition de $X_n$ :**
   $X_n$ prend les valeurs $k/n$ avec une probabilité uniforme de $1/n$.
   Soit $x \in [0, 1]$. Le nombre d'éléments de l'ensemble $\{ \frac{1}{n}, \frac{2}{n}, \dots, \frac{n}{n} \}$ qui sont inférieurs ou égaux à $x$ est la partie entière $\lfloor n x \rfloor$.
   $$ F_{X_n}(x) = \mathbb{P}(X_n \leq x) = \sum_{k=1}^{\lfloor n x \rfloor} \frac{1}{n} = \frac{\lfloor n x \rfloor}{n} $$

   Pour $x < 0$, $\lfloor n x \rfloor$ n'intersecte pas l'ensemble (valeurs positives), donc $F_{X_n}(x) = 0$.
   Pour $x > 1$, tous les éléments de l'ensemble sont inférieurs à $x$, donc $F_{X_n}(x) = 1$.

3. **Passage à la limite :**
   L'encadrement classique de la partie entière est :
   $$ n x - 1 < \lfloor n x \rfloor \leq n x $$
   En divisant par $n$ (strictement positif) :
   $$ x - \frac{1}{n} < \frac{\lfloor n x \rfloor}{n} \leq x $$
   Par le théorème d'encadrement des limites (théorème des gendarmes), pour tout $x \in [0, 1]$ :
   $$ \lim_{n \to \infty} \frac{\lfloor n x \rfloor}{n} = x $$
   Ainsi, pour tout $x \in \mathbb{R}$, $\lim_{n \to \infty} F_{X_n}(x) = F_X(x)$.
   La suite $(X_n)$ converge bien en loi vers la loi uniforme sur $[0, 1]$.
   $\blacksquare$

