# Exercice 9 - Difficulté: Niveau 5

## 1. Énoncé
Démontrer le théorème des valeurs intermédiaires par dichotomie (construction de deux suites adjacentes).

## 2. Démonstration (Zéro Ellipse)
Soit $f : [a, b] \to \mathbb{R}$ continue telle que $f(a) \le 0 \le f(b)$.
Construisons deux suites $(a_n)_{n \in \mathbb{N}}$ et $(b_n)_{n \in \mathbb{N}}$ par récurrence.
**Initialisation :** Posons $a_0 = a$ et $b_0 = b$. On a bien $f(a_0) \le 0 \le f(b_0)$ et $b_0 - a_0 = b - a \ge 0$.
**Hérédité (Construction) :** Supposons $a_n$ et $b_n$ construits tels que $f(a_n) \le 0 \le f(b_n)$ et $b_n - a_n = \frac{b-a}{2^n}$.
Soit $c_n = \frac{a_n + b_n}{2}$ le milieu du segment $[a_n, b_n]$. On évalue $f(c_n)$.
Deux cas se présentent :
1. Si $f(c_n) \le 0$ : On pose $a_{n+1} = c_n$ et $b_{n+1} = b_n$.
   Ainsi, $f(a_{n+1}) = f(c_n) \le 0$ et $f(b_{n+1}) = f(b_n) \ge 0$.
2. Si $f(c_n) > 0$ : On pose $a_{n+1} = a_n$ et $b_{n+1} = c_n$.
   Ainsi, $f(a_{n+1}) = f(a_n) \le 0$ et $f(b_{n+1}) = f(c_n) > 0 \ge 0$.

Dans les deux cas, on a $f(a_{n+1}) \le 0 \le f(b_{n+1})$.
De plus, $b_{n+1} - a_{n+1} = \frac{b_n - a_n}{2} = \frac{b-a}{2^{n+1}}$.
Par récurrence, les suites $(a_n)$ et $(b_n)$ sont bien définies.

**Propriétés des suites :**
- Par construction, $a_n \le a_{n+1} \le b_{n+1} \le b_n$. La suite $(a_n)$ est donc croissante et $(b_n)$ est décroissante.
- La différence $b_n - a_n = \frac{b-a}{2^n}$ tend vers $0$ lorsque $n \to +\infty$.
Les suites $(a_n)$ et $(b_n)$ sont donc **adjacentes**. D'après le théorème des suites adjacentes, elles convergent vers une même limite commune $c \in [a, b]$.

**Conclusion via la continuité :**
La fonction $f$ est continue en $c$. Comme $\lim_{n \to +\infty} a_n = c$, on a $\lim_{n \to +\infty} f(a_n) = f(c)$. Puisque pour tout $n$, $f(a_n) \le 0$, le passage à la limite préserve l'inégalité : $f(c) \le 0$.
De même, comme $\lim_{n \to +\infty} b_n = c$, on a $\lim_{n \to +\infty} f(b_n) = f(c)$. Puisque pour tout $n$, $f(b_n) \ge 0$, le passage à la limite préserve l'inégalité : $f(c) \ge 0$.
En combinant $f(c) \le 0$ et $f(c) \ge 0$, on obtient inéluctablement $f(c) = 0$. Le théorème est démontré par dichotomie.
