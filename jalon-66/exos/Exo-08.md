---
title: "Exercice 08 : Limite d'une intégrale avec atomes"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 08 : Limite d'une intégrale avec atomes

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $\lambda$ la mesure de Lebesgue sur $\mathbb{R}$.
Soit $f_n(x) = n \cdot \mathbf{1}_{[0, 1/n]}(x)$.
Calculez $\int_{\mathbb{R}} f_n \, d\lambda$.
Ensuite, déterminez la limite ponctuelle de $f_n$ (notons-la $f$) et calculez $\int_{\mathbb{R}} f \, d\lambda$.
Que concluez-vous sur l'interversion de la limite et de l'intégrale sans conditions dominantes ?

### Correction détaillée

1. **Calcul de l'intégrale de $f_n$ :**
   La fonction $f_n$ est une fonction simple positive. Son intégrale est :
   $$ \int_{\mathbb{R}} n \cdot \mathbf{1}_{[0, 1/n]} \, d\lambda = n \cdot \lambda\left(\left[0, \frac{1}{n}\right]\right) = n \cdot \left(\frac{1}{n} - 0\right) = 1 $$
   Donc, pour tout $n \ge 1$, $\int_{\mathbb{R}} f_n \, d\lambda = 1$.
2. **Limite de la suite des intégrales :**
   Il est trivial que $\lim_{n \to +\infty} \int_{\mathbb{R}} f_n \, d\lambda = 1$.
3. **Calcul de la limite ponctuelle de $f_n$ :**
   Étudions $f(x) = \lim_{n \to \infty} f_n(x)$ point par point.
   - Si $x < 0$, alors pour tout $n$, $x \notin [0, 1/n]$, donc $f_n(x) = 0$. Limite $f(x) = 0$.
   - Si $x > 0$, il existe un entier $N$ tel que $1/N < x$ (propriété d'Archimède). Pour tout $n > N$, $x \notin [0, 1/n]$, donc $f_n(x) = 0$. La suite stationne à 0. Limite $f(x) = 0$.
   - Si $x = 0$, $0 \in [0, 1/n]$ pour tout $n$. Donc $f_n(0) = n$. La limite en 0 est $+\infty$.
   La fonction limite $f$ est nulle partout sauf en 0 où elle vaut l'infini : $f(x) = \begin{cases} +\infty & \text{si } x = 0 \\ 0 & \text{sinon} \end{cases}$
4. **Calcul de l'intégrale de la limite $f$ :**
   La fonction $f$ est presque partout nulle par rapport à la mesure de Lebesgue (car le singleton $\{0\}$ est de mesure nulle).
   $$ \int_{\mathbb{R}} f \, d\lambda = 0 $$
5. **Conclusion :**
   On a $\lim_{n \to \infty} \int f_n = 1 \neq 0 = \int \lim_{n \to \infty} f_n$.
   L'interversion de la limite et de l'intégrale n'est pas automatique, même pour des fonctions mesurables positives. Ici, la "masse" s'échappe vers le haut infiniment étroitement (c'est le prélude au Lemme de Fatou, où on a seulement $\int \lim \inf f_n \le \lim \inf \int f_n$).
