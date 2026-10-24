\subsection*{Exercice 6 : Lemme de Farkas-Minkowski \quad $\bigstar\bigstar\bigstar\star\star$}

Soient $a_1, \dots, a_m, b \in \mathbb{R}^n$. Montrer que l'une et seulement l'une des deux affirmations suivantes est vraie :
(i) $\exists x \ge 0$ tel que $\sum_{i=1}^m x_i a_i = b$.
(ii) $\exists y \in \mathbb{R}^n$ tel que $\forall i, \langle y, a_i \rangle \ge 0$ et $\langle y, b \rangle < 0$.

**Correction :**

1. Ce lemme est une conséquence directe de Hahn-Banach en dimension finie.
2. Soit $C = \{ \sum_{i=1}^m x_i a_i \mid x_i \ge 0 \}$. $C$ est un cône convexe engendré par un nombre fini de vecteurs, il est donc fermé.
3. L'affirmation (i) équivaut à dire que $b \in C$.
4. Si $b \in C$, alors pour tout $y$ tel que $\langle y, a_i \rangle \ge 0$, on a $\langle y, b \rangle = \sum x_i \langle y, a_i \rangle \ge 0$, donc (ii) est fausse.
5. Si $b \notin C$, alors comme $C$ est fermé, on peut séparer strictement $b$ et $C$.
6. Il existe $y \in \mathbb{R}^n$ et $\alpha \in \mathbb{R}$ tels que $\forall z \in C, \langle y, z \rangle > \alpha > \langle y, b \rangle$.
7. Comme $0 \in C$, $\alpha < 0$, donc $\langle y, b \rangle < 0$.
8. Si pour un $a_i$ on a $\langle y, a_i \rangle < 0$, alors en prenant $z = \lambda a_i \in C$, on aurait $\langle y, \lambda a_i \rangle > \alpha$ pour tout $\lambda > 0$, absurde.
9. Ainsi $\langle y, a_i \rangle \ge 0$ pour tout $i$, ce qui vérifie l'affirmation (ii).