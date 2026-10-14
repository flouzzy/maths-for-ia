# Exercice 5 : Limite d'une suite de maxima

$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(X_n)$ une suite de variables aléatoires indépendantes suivant la loi exponentielle $\mathcal{E}(1)$.
Posons $M_n = \max(X_1, X_2, \dots, X_n)$.
Montrer que $\limsup_{n \to \infty} \frac{X_n}{\ln(n)} = 1$ presque sûrement.

**Correction :**
Soit $c > 0$. Considérons l'événement $A_n = \left\{ \frac{X_n}{\ln(n)} \ge c \right\} = \{ X_n \ge c \ln(n) \}$.
Puisque $X_n \sim \mathcal{E}(1)$, sa fonction de survie est $\mathbb{P}(X_n \ge x) = e^{-x}$.
Ainsi, $\mathbb{P}(A_n) = \mathbb{P}(X_n \ge c \ln(n)) = e^{-c \ln(n)} = \frac{1}{n^c}$.
Étudions la série $\sum \mathbb{P}(A_n) = \sum \frac{1}{n^c}$.
Si $c > 1$, la série $\sum \frac{1}{n^c}$ converge (série de Riemann).
D'après le premier lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 0$.
Cela implique que presque sûrement, il n'y a qu'un nombre fini de $n$ tels que $\frac{X_n}{\ln(n)} \ge c$.
Donc $\limsup \frac{X_n}{\ln(n)} \le c$ p.s.
Ceci étant vrai pour tout $c > 1$, en faisant tendre $c \to 1^+$, on obtient $\limsup \frac{X_n}{\ln(n)} \le 1$ p.s.

Si $c = 1$, $\mathbb{P}(A_n) = \frac{1}{n}$. La série diverge.
De plus, les variables $X_n$ sont indépendantes, donc les événements $A_n$ le sont.
Par le second lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 1$.
Cela signifie que presque sûrement, $\frac{X_n}{\ln(n)} \ge 1$ pour une infinité d'indices $n$.
Donc $\limsup \frac{X_n}{\ln(n)} \ge 1$ p.s.
En combinant les deux résultats, on conclut rigoureusement que :
$$ \limsup_{n \to \infty} \frac{X_n}{\ln(n)} = 1 \text{ presque sûrement.} $$
