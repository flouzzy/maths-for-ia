---
uuid: "exo-14-8"
title: "Exercice 8 - Suites (Difficulté 4 étoiles)"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence
  - exercice
---
# Exercice 8
Soit $u_n = \cos\left(\frac{n\pi}{3}\right)$. Montrer rigoureusement que la suite $(u_n)_{n \in \mathbb{N}}$ diverge, en construisant deux sous-suites convergeant vers des limites différentes.

## Correction

Pour montrer qu'une suite diverge, il suffit de trouver deux sous-suites extraites convergeant vers des limites différentes.
Une sous-suite de $(u_n)$ s'écrit $(u_{\phi(n)})$ où $\phi : \mathbb{N} \to \mathbb{N}$ est une application strictement croissante.

Posons la première application extractrice $\phi_1(n) = 6n$.
La sous-suite correspondante est :
$$
\begin{align*}
v_n &= u_{\phi_1(n)} = u_{6n} \\
&= \cos\left(\frac{6n\pi}{3}\right) \\
&= \cos(2n\pi)
\end{align*}
$$
Pour tout entier naturel $n$, on sait que $\cos(2n\pi) = 1$.
Ainsi, la sous-suite $(v_n)$ est la suite constante égale à $1$. Elle converge donc vers $l_1 = 1$.

Posons une deuxième application extractrice $\phi_2(n) = 6n + 3$.
La sous-suite correspondante est :
$$
\begin{align*}
w_n &= u_{\phi_2(n)} = u_{6n+3} \\
&= \cos\left(\frac{(6n+3)\pi}{3}\right) \\
&= \cos(2n\pi + \pi)
\end{align*}
$$
Par la périodicité et les propriétés de la fonction cosinus, $\cos(x + \pi) = -\cos(x)$.
$$
\begin{align*}
w_n &= -\cos(2n\pi) \\
&= -1
\end{align*}
$$
La sous-suite $(w_n)$ est la suite constante égale à $-1$. Elle converge donc vers $l_2 = -1$.

Puisque nous avons extrait deux sous-suites $(u_{6n})_{n \in \mathbb{N}}$ et $(u_{6n+3})_{n \in \mathbb{N}}$ convergeant vers des limites distinctes ($l_1 = 1 \neq -1 = l_2$), la suite globale $(u_n)_{n \in \mathbb{N}}$ ne peut pas admettre de limite. Elle est donc divergente.
