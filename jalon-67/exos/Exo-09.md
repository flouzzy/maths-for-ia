# Exercice 9 : Continuité d'une intégrale paramétrée (cas positif) $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $f : \mathbb{R} \times X \to \mathbb{R}_+$ telle que pour tout $x \in X$, la fonction $t \mapsto f(t, x)$ est croissante et continue à gauche sur $\mathbb{R}$. Soit $\mu$ une mesure sur $X$.
Posons $g(t) = \int_X f(t, x) d\mu(x)$.
Montrer que $g$ est croissante et continue à gauche sur $\mathbb{R}$.

## Correction Détaillée
1. **Croissance de $g$** : Soit $s \le t$. Pour tout $x \in X$, $f(s, x) \le f(t, x)$. En intégrant cette inégalité par rapport à $\mu$ (croissance de l'intégrale), on obtient $g(s) \le g(t)$.
2. **Continuité à gauche** : Soit $t_0 \in \mathbb{R}$ et $(t_n)_{n \in \mathbb{N}}$ une suite réelle croissante convergeant vers $t_0$ (avec $t_n \le t_0$).
3. Pour tout $x \in X$, la suite de fonctions $f_n(x) = f(t_n, x)$ est mesurable et positive.
4. Comme $t \mapsto f(t, x)$ est croissante, la suite de fonctions $(f_n(x))_{n}$ est croissante : $f_n(x) \le f_{n+1}(x)$.
5. La continuité à gauche de $f(\cdot, x)$ implique que $\lim_{n \to \infty} f_n(x) = f(t_0, x)$.
6. Les hypothèses du Théorème de Convergence Monotone de Beppo Levi sont vérifiées pour la suite $(f_n)$. On peut donc intervertir limite et intégrale :
   $$ \lim_{n \to \infty} \int_X f(t_n, x) d\mu(x) = \int_X \lim_{n \to \infty} f(t_n, x) d\mu(x) $$
   C'est-à-dire : $\lim_{n \to \infty} g(t_n) = \int_X f(t_0, x) d\mu(x) = g(t_0)$.
7. Cette propriété étant vraie pour toute suite croissante $(t_n)$ tendant vers $t_0$, la fonction $g$ est séquentiellement continue à gauche en $t_0$, donc continue à gauche.
