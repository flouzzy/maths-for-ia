---
uuid: "exo-14-7"
title: "Exercice 7 - Suites (Difficulté 4 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 7
Soit $u_n = \sum_{k=0}^n \frac{1}{k!}$ pour $n \in \mathbb{N}$.
Montrer que $(u_n)_{n \in \mathbb{N}}$ est convergente. On utilisera une majoration rigoureuse.

## Correction

Étape 1 : Sens de variation
Pour tout $n \in \mathbb{N}$, on a :
$$ u_{n+1} - u_n = \sum_{k=0}^{n+1} \frac{1}{k!} - \sum_{k=0}^n \frac{1}{k!} = \frac{1}{(n+1)!} $$
Comme $\frac{1}{(n+1)!} > 0$, la suite $(u_n)$ est strictement croissante.

Étape 2 : Majoration
Nous allons majorer $k!$.
Pour $k=0$, $0! = 1$.
Pour $k=1$, $1! = 1$.
Pour $k \ge 2$,
$$ k! = 1 \cdot 2 \cdot 3 \dots \cdot k $$
Dans ce produit, il y a $k-1$ facteurs qui sont supérieurs ou égaux à 2.
Donc $k! \ge 1 \cdot 2 \cdot 2 \dots \cdot 2 = 2^{k-1}$.
Cette inégalité $k! \ge 2^{k-1}$ est vérifiée pour tout $k \ge 1$ (pour $k=1$, $1! = 1 \ge 2^0 = 1$).

Par conséquent, pour $k \ge 1$, $\frac{1}{k!} \le \frac{1}{2^{k-1}}$.

Majorons $u_n$ pour $n \ge 1$ :
$$
\begin{align*}
u_n &= 1 + \sum_{k=1}^n \frac{1}{k!} \\
&\le 1 + \sum_{k=1}^n \frac{1}{2^{k-1}} \\
\end{align*}
$$
Effectuons le changement d'indice $j = k-1$. La somme va de $j=0$ à $j=n-1$.
$$
\begin{align*}
u_n &\le 1 + \sum_{j=0}^{n-1} \left(\frac{1}{2}\right)^j \\
\end{align*}
$$
On reconnaît la somme des termes d'une suite géométrique de raison $q = 1/2$.
$$
\begin{align*}
\sum_{j=0}^{n-1} \left(\frac{1}{2}\right)^j &= \frac{1 - (1/2)^n}{1 - 1/2} \\
&= \frac{1 - (1/2)^n}{1/2} \\
&= 2 \left(1 - \frac{1}{2^n}\right) \\
&= 2 - \frac{1}{2^{n-1}} < 2
\end{align*}
$$

Ainsi, pour tout $n \ge 1$ :
$$ u_n \le 1 + \left(2 - \frac{1}{2^{n-1}}\right) = 3 - \frac{1}{2^{n-1}} < 3 $$
La suite $(u_n)$ est majorée par 3.

Étape 3 : Conclusion
La suite $(u_n)_{n \in \mathbb{N}}$ est croissante et majorée. D'après le théorème de la convergence monotone, elle converge. Sa limite est par définition le nombre $e$.
