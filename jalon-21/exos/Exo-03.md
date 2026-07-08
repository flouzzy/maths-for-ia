---
uuid: "exo-21-03"
title: "Exercice 3 : Convergence uniforme de x/n"
difficulty: 2
---

# Exercice 3 : Convergence uniforme de x/n

**Niveau :** $★★☆☆☆$

## Problème

Montrer que $f_n(x) = x/n$ ne converge pas uniformément sur $\mathbb{R}$.

## Démonstration et Solution (Zéro Ellipse)

D'après l'exercice précédent, la suite de fonctions $f_n(x) = \frac{x}{n}$ converge simplement vers la fonction nulle $f(x) = 0$ sur $\mathbb{R}$.
Pour déterminer si cette convergence est uniforme sur $\mathbb{R}$, nous devons évaluer la norme de la convergence uniforme, c'est-à-dire le supremum de l'écart absolu entre les fonctions $f_n$ et la fonction limite $f$ sur l'ensemble du domaine de définition.

Posons la norme infinie de la différence :
$\|f_n - f\|_\infty = \sup_{x \in \mathbb{R}} |f_n(x) - f(x)|$
En remplaçant par nos fonctions :
$\|f_n - f\|_\infty = \sup_{x \in \mathbb{R}} \left| \frac{x}{n} - 0 \right| = \sup_{x \in \mathbb{R}} \frac{|x|}{n}$

Pour un entier $n \geq 1$ fixé, regardons le comportement de la fonction $x \mapsto \frac{|x|}{n}$ sur $\mathbb{R}$.
Lorsque $x$ tend vers $+\infty$, la quantité $\frac{|x|}{n}$ tend vers $+\infty$.
L'ensemble des valeurs $\left\{ \frac{|x|}{n} \mid x \in \mathbb{R} \right\}$ n'est donc pas majoré. Son supremum dans $\mathbb{R} \cup \{+\infty\}$ est donc infini.
Par conséquent, pour tout $n \geq 1$, $\|f_n - f\|_\infty = +\infty$.

Puisque la suite des normes $\|f_n - f\|_\infty$ ne tend pas vers 0 (elle est constante égale à $+\infty$), la convergence n'est par définition pas uniforme sur l'ensemble $\mathbb{R}$.
