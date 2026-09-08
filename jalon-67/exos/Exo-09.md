# Exercice 9 : Généralisation à une suite indexée par un paramètre continu

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Montrer que si $f : \mathbb{R}_+ \times \mathbb{R}_+ \to \mathbb{R}_+$ est mesurable, et si pour presque tout $x$, $t \mapsto f(t,x)$ est croissante, alors la limite $t \to \infty$ de l'intégrale est l'intégrale de la limite $f(\infty, x)$.

## Démonstration rigoureuse pas à pas

Puisque la limite se fait selon un paramètre réel continu $t \to +\infty$, on peut la caractériser par des suites. Soit $L = \sup_{t} \int_X f(t,x) d\mu$. Pour toute suite $(t_n)$ croissant vers $+\infty$, la suite de fonctions $g_n(x) = f(t_n, x)$ est une suite croissante de fonctions mesurables positives convergeant simplement vers $f(\infty, x) = \sup_t f(t,x)$. Par Beppo-Levi, $\lim_{n \to \infty} \int_X g_n(x) d\mu = \int_X f(\infty, x) d\mu$. Puisque ceci est vrai pour toute suite $(t_n)$ tendant vers l'infini, la limite sur le paramètre continu $t$ est bien validée (propriété séquentielle de la limite).
