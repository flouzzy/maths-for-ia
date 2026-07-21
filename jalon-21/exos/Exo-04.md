---
uuid: "exo-21-04"
title: "Exercice 4 : Convergence uniforme sur segment"
difficulty: 2
---

# Exercice 4 : Convergence uniforme sur segment

**Niveau :** $★★☆☆☆$

## Problème

Montrer que $f_n(x) = x/n$ converge uniformément sur tout segment $[-M, M]$ avec $M > 0$.

## Démonstration et Solution

Considérons le segment fini $[-M, M]$ où $M$ est un réel strictement positif.
Nous savons que la suite $f_n(x) = \frac{x}{n}$ converge simplement vers la fonction nulle $f(x) = 0$ sur ce segment (puisque cela est vrai sur tout $\mathbb{R}$).

Évaluons maintenant la norme de la différence sur ce segment restreint :
$\|f_n - f\|_{\infty, [-M,M]} = \sup_{x \in [-M, M]} |f_n(x) - f(x)| = \sup_{x \in [-M, M]} \frac{|x|}{n}$

Pour tout $x \in [-M, M]$, nous avons l'inégalité stricte ou large : $|x| \leq M$.
Par conséquent, en divisant par l'entier strictement positif $n$, nous obtenons pour tout $x \in [-M, M]$ :
$\frac{|x|}{n} \leq \frac{M}{n}$
Puisque la borne $M/n$ est atteinte en posant $x=M$ (ou $x=-M$), le supremum est exactement égal à cette valeur :
$\|f_n - f\|_{\infty, [-M,M]} = \frac{M}{n}$

Étudions la limite de cette suite de normes :
$\lim_{n \to \infty} \|f_n - f\|_{\infty, [-M,M]} = \lim_{n \to \infty} \frac{M}{n} = M \times \lim_{n \to \infty} \frac{1}{n} = M \times 0 = 0$.

**Conclusion :**
La norme infinie de la différence entre $f_n$ et $f$ sur le segment $[-M, M]$ tend rigoureusement vers 0 lorsque $n$ tend vers l'infini. Par définition, cela signifie que la suite de fonctions $(f_n)$ converge uniformément vers la fonction nulle sur le segment $[-M, M]$.
