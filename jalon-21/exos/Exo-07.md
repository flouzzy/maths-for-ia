---
uuid: "exo-21-07"
title: "Exercice 7 : Convergence uniforme de arctan(nx)"
difficulty: 4
---

# Exercice 7 : Convergence uniforme de arctan(nx)

**Niveau :** $★★★★☆$

## Problème

Étudier la convergence de $f_n(x) = \frac{1}{n}\arctan(nx)$ sur $\mathbb{R}$.

## Démonstration et Solution

Considérons la suite de fonctions $f_n(x) = \frac{1}{n} \arctan(nx)$ sur $\mathbb{R}$.

**Étape 1 : Convergence simple**
Pour tout réel $x \in \mathbb{R}$, fixons $x$ et étudions la limite quand $n \to \infty$.
Nous connaissons les bornes de la fonction arc tangente : pour tout réel $y$, $|\arctan(y)| < \frac{\pi}{2}$.
Ainsi, pour tout réel $x$ et tout entier $n \geq 1$ :
$|f_n(x)| = \left| \frac{1}{n} \arctan(nx) \right| = \frac{1}{n} |\arctan(nx)| < \frac{1}{n} \times \frac{\pi}{2}$
Puisque $\lim_{n \to \infty} \frac{\pi}{2n} = 0$, le théorème des gendarmes implique que $\lim_{n \to \infty} f_n(x) = 0$.
La suite converge simplement vers la fonction nulle $f(x)=0$ sur $\mathbb{R}$.

**Étape 2 : Convergence uniforme**
Pour étudier la convergence uniforme, déterminons la norme infinie de la différence $\|f_n - f\|_\infty$ sur $\mathbb{R}$.
$\|f_n - f\|_\infty = \sup_{x \in \mathbb{R}} |f_n(x) - 0| = \sup_{x \in \mathbb{R}} \frac{|\arctan(nx)|}{n}$
Nous savons que la fonction $x \mapsto \arctan(nx)$ est strictement croissante et impaire. Son supremum sur $\mathbb{R}$ est atteint asymptotiquement lorsque $x \to +\infty$.
$\sup_{x \in \mathbb{R}} |\arctan(nx)| = \lim_{x \to +\infty} \arctan(nx) = \frac{\pi}{2}$
Par conséquent, en divisant par la constante positive $n$, nous obtenons la valeur exacte de la norme infinie :
$\|f_n - f\|_\infty = \frac{1}{n} \times \frac{\pi}{2} = \frac{\pi}{2n}$
Étudions maintenant la limite de cette norme lorsque $n$ tend vers l'infini :
$\lim_{n \to \infty} \|f_n - f\|_\infty = \lim_{n \to \infty} \frac{\pi}{2n} = 0$.
Puisque la norme infinie de l'écart tend vers 0, la convergence est, par définition, uniforme sur l'ensemble $\mathbb{R}$.
