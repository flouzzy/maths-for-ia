# Exercice 7

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Limite supérieure d'une loi exponentielle

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires indépendantes suivant la loi exponentielle de paramètre $\lambda = 1$.
Montrer que $\limsup_{n \to \infty} \frac{X_n}{\ln n} = 1$ presque sûrement.

**Correction détaillée :**
1. Étape 1 : Majoration. Soit $c > 1$. Étudions l'événement $A_n = \{X_n > c \ln n\}$.
2. On a $\mathbb{P}(A_n) = e^{-c \ln n} = \frac{1}{n^c}$.
3. Comme $c > 1$, la série $\sum \mathbb{P}(A_n)$ converge (série de Riemann).
4. Par le premier lemme, $\mathbb{P}(\limsup A_n) = 0$. Ainsi, pour tout $c > 1$, il n'existe presque sûrement qu'un nombre fini de $n$ tels que $\frac{X_n}{\ln n} > c$. Par suite, $\limsup \frac{X_n}{\ln n} \le c$ p.s.
5. En prenant l'intersection dénombrable de ces événements pour une suite $c_k \to 1^+$, on obtient $\limsup \frac{X_n}{\ln n} \le 1$ p.s.
6. Étape 2 : Minoration. Soit $c \le 1$. Étudions l'événement $B_n = \{X_n > c \ln n\}$.
7. $\mathbb{P}(B_n) = \frac{1}{n^c}$. Puisque $c \le 1$, la série diverge.
8. Les variables $(X_n)$ sont indépendantes, donc les événements $(B_n)$ le sont. Par le second lemme, $\mathbb{P}(\limsup B_n) = 1$.
9. Presque sûrement, il y a une infinité de $n$ pour lesquels $\frac{X_n}{\ln n} > c$, d'où $\limsup \frac{X_n}{\ln n} \ge c$ p.s.
10. En prenant $c \to 1^-$, $\limsup \frac{X_n}{\ln n} \ge 1$ p.s.
11. Conclusion : Les deux inégalités imposent $\limsup_{n \to \infty} \frac{X_n}{\ln n} = 1$ presque sûrement.
