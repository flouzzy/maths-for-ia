---
uuid: "jalon-90-exo-09"
title: "Convergence asymptotique des valeurs extrêmes"
---

# Exercice 9 : Convergence asymptotique des valeurs extrêmes (Difficulté $\bigstar\bigstar\bigstar\bigstar\bigstar$)

Soit $(U_n)_{n \geq 1}$ une suite de variables aléatoires indépendantes suivant la loi uniforme sur l'intervalle $[0, 1]$.
Définissons le maximum empirique : $M_n = \max(U_1, U_2, \dots, U_n)$.
1. Montrer que la suite $(M_n)$ converge en probabilité.
2. Définissons la variable dilatée $Y_n = n(1 - M_n)$. Montrer que la suite $(Y_n)$ converge en loi et identifier la distribution limite.

## Correction Pas-à-Pas

1. **Convergence en probabilité de $M_n$ :**
   Il est intuitif que le maximum s'approche de $1$. Montrons que $M_n \xrightarrow{\mathbb{P}} 1$.
   Puisque toutes les $U_i$ sont dans $[0, 1]$, le maximum $M_n$ l'est aussi.
   Soit $\epsilon > 0$. Si $\epsilon \geq 1$, $\mathbb{P}(|M_n - 1| > \epsilon) = 0$. On suppose $0 < \epsilon < 1$.
   L'événement $\{|M_n - 1| > \epsilon\}$ correspond, puisque $M_n \leq 1$, à $\{ 1 - M_n > \epsilon \} = \{ M_n < 1 - \epsilon \}$.
   Pour que le maximum de $n$ variables indépendantes soit inférieur à $1 - \epsilon$, il faut que chacune des $n$ variables soit inférieure à $1 - \epsilon$.
   $$ \mathbb{P}(M_n < 1 - \epsilon) = \mathbb{P}(U_1 < 1 - \epsilon, \dots, U_n < 1 - \epsilon) $$
   Par indépendance des variables aléatoires :
   $$ \mathbb{P}(M_n < 1 - \epsilon) = \prod_{i=1}^n \mathbb{P}(U_i < 1 - \epsilon) $$
   Puisque la loi est uniforme sur $[0, 1]$, $\mathbb{P}(U_i < x) = x$ pour $x \in [0, 1]$.
   $$ \mathbb{P}(M_n < 1 - \epsilon) = (1 - \epsilon)^n $$
   Puisque $1 - \epsilon \in ]0, 1[$, la suite géométrique tend vers $0$ :
   $$ \lim_{n \to \infty} (1 - \epsilon)^n = 0 $$
   Donc $\lim_{n \to \infty} \mathbb{P}(|M_n - 1| > \epsilon) = 0$. $M_n$ converge bien en probabilité vers $1$.

2. **Convergence en loi de $Y_n = n(1 - M_n)$ :**
   $Y_n$ prend ses valeurs dans l'intervalle $[0, n]$.
   Évaluons la fonction de répartition de $Y_n$ pour un réel $t \geq 0$ fixé.
   $$ F_{Y_n}(t) = \mathbb{P}(Y_n \leq t) = \mathbb{P}(n(1 - M_n) \leq t) $$
   On isole le maximum $M_n$ :
   $$ F_{Y_n}(t) = \mathbb{P}\left(1 - M_n \leq \frac{t}{n}\right) = \mathbb{P}\left(M_n \geq 1 - \frac{t}{n}\right) $$
   Passons à l'événement complémentaire :
   $$ F_{Y_n}(t) = 1 - \mathbb{P}\left(M_n < 1 - \frac{t}{n}\right) $$
   Pour $n > t$, le terme $1 - t/n$ appartient à $]0, 1[$. En reprenant le calcul précédent (indépendance et loi uniforme) :
   $$ \mathbb{P}\left(M_n < 1 - \frac{t}{n}\right) = \left( 1 - \frac{t}{n} \right)^n $$
   Donc :
   $$ F_{Y_n}(t) = 1 - \left( 1 - \frac{t}{n} \right)^n $$
   Le passage à la limite utilise l'exponentielle comme limite de la suite de fonctions puissance :
   $$ \lim_{n \to \infty} \left( 1 - \frac{t}{n} \right)^n = e^{-t} $$
   Par conséquent, la limite de la fonction de répartition est :
   $$ \lim_{n \to \infty} F_{Y_n}(t) = 1 - e^{-t} $$
   On reconnaît exactement la fonction de répartition de la loi exponentielle de paramètre $\lambda = 1$.
   La suite $(Y_n)$ converge en loi vers une variable aléatoire suivant une loi exponentielle $\mathcal{E}(1)$.
   $\blacksquare$

