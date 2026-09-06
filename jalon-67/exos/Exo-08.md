---
uuid: "exo-67-08"
title: "Exercice 08 : Comportement asymptotique d'une intégrale impropre"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 08 : Comportement asymptotique d'une intégrale impropre ($\bigstar\bigstar\bigstar\bigstar\star$)

## Énoncé

Soit $f_n(x) = \frac{nx}{1 + n^2 x^2}$ sur $[0, 1]$. Étudier $\lim_n \int_0^1 f_n(x) dx$ et comparer avec $\int_0^1 \lim f_n(x) dx$. Conclure sur le TCM.

## Corrigé Rigoureux

1. **Limite ponctuelle :** Pour $x=0$, $f_n(0) = 0 \to 0$. Pour $x > 0$, $f_n(x) \sim \frac{nx}{n^2 x^2} = \frac{1}{nx} \to 0$. Donc $f = \lim f_n = 0$. Ainsi $\int_0^1 f dx = 0$.
2. **Calcul de l'intégrale :** $\int_0^1 \frac{nx}{1+n^2 x^2} dx = \left[ \frac{1}{2n} \ln(1 + n^2 x^2) \right]_0^1 = \frac{\ln(1+n^2)}{2n}$.
La limite est $\lim_{n\to\infty} \frac{\ln(n^2)}{2n} = \lim \frac{\ln(n)}{n} = 0$.
Ici $\lim \int f_n = \int \lim f_n = 0$.
3. **Le TCM s'applique-t-il ?** Non ! La suite $(f_n(x))$ n'est pas croissante pour un $x > 0$ fixé (elle décroît à partir d'un certain rang). L'égalité des limites est vérifiée, mais par le théorème de convergence dominée (la fonction est bornée par $\frac{1}{2}$), et non par Beppo Levi.
