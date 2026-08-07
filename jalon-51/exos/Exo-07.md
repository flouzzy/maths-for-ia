## Exercice 7 : Distances équivalentes dans $\mathbb{R}^n$ \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Sur $\mathbb{R}^n$, on définit les distances $d_1(x,y) = \sum |x_i - y_i|$ et $d_\infty(x,y) = \max |x_i - y_i|$.
Montrer que $d_1$ et $d_\infty$ sont équivalentes.

**Correction :**
Soient $x, y \in \mathbb{R}^n$.
1. **Majoration de $d_\infty$ par $d_1$ :**
   Pour tout $j \in \{1, \dots, n\}$, $|x_j - y_j| \le \sum_{i=1}^n |x_i - y_i| = d_1(x,y)$.
   Puisque c'est vrai pour tout $j$, c'est vrai pour le maximum :
   $d_\infty(x,y) \le d_1(x,y)$. (Constante $C_1 = 1$).
2. **Majoration de $d_1$ par $d_\infty$ :**
   $d_1(x,y) = \sum_{i=1}^n |x_i - y_i|$.
   Chaque terme de la somme est majoré par le maximum des écarts, soit $d_\infty(x,y)$.
   $d_1(x,y) \le \sum_{i=1}^n d_\infty(x,y) = n \cdot d_\infty(x,y)$.
   Ce qui s'écrit $d_\infty(x,y) \ge \frac{1}{n} d_1(x,y)$.
En combinant, on a pour tout $x,y$ :
$$ \frac{1}{n} d_1(x,y) \le d_\infty(x,y) \le d_1(x,y) $$
Les distances sont donc équivalentes. $\blacksquare$
