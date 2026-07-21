---
uuid: "exo-21-08"
title: "Exercice 8 : Suite de fonctions continues vers continue sans CU"
difficulty: 4
---

# Exercice 8 : Suite de fonctions continues vers continue sans CU

**Niveau :** $★★★★☆$

## Problème

Construire une suite de fonctions continues sur $[0,1]$ qui converge simplement vers $0$, mais dont la norme infinie vaut toujours $1$.

## Démonstration et Solution

Pour répondre à la question, nous devons concevoir une suite de fonctions "chapeau" ou "pointe de tente" dont la hauteur reste constante égale à 1, mais dont la base se rétrécit vers 0 à mesure que $n$ augmente.

Définissons pour chaque entier $n \geq 2$ la fonction $f_n$ sur $[0,1]$ par des segments de droite reliant les points suivants :
- Point $A : (0, 0)$
- Point $B : (\frac{1}{2n}, 1)$
- Point $C : (\frac{1}{n}, 0)$
- Point $D : (1, 0)$
Explicitement, cela s'écrit formellement par morceaux :
$f_n(x) = 2nx$ si $x \in [0, \frac{1}{2n}[$
$f_n(x) = -2nx + 2$ si $x \in [\frac{1}{2n}, \frac{1}{n}[$
$f_n(x) = 0$ si $x \in [\frac{1}{n}, 1]$.
Par construction (raccordement continu aux points de rupture), chaque fonction $f_n$ est continue sur le segment $[0,1]$.

**Étape 1 : Convergence simple**
Fixons $x \in [0,1]$.
Si $x = 0$, $f_n(0) = 0$ pour tout $n$, donc la limite est 0.
Si $x > 0$, alors selon la propriété d'Archimède, il existe un entier $N$ tel que $\frac{1}{N} < x$.
Par conséquent, pour tout $n \geq N$, nous avons $\frac{1}{n} \leq \frac{1}{N} < x$.
Selon la définition de notre fonction par morceaux, si $x > \frac{1}{n}$, alors $f_n(x) = 0$.
Donc, pour un $x > 0$ fixé, la suite $f_n(x)$ est stationnaire à 0 à partir du rang $N$. Sa limite est donc 0.
La suite $(f_n)$ converge simplement vers la fonction limite continue $f(x)=0$ sur $[0,1]$.

**Étape 2 : Absence de convergence uniforme**
Calculons la norme infinie $\|f_n - f\|_\infty$ sur $[0,1]$.
Puisque $f(x)=0$, cela revient à trouver le supremum de $f_n$.
Par construction, le sommet du "chapeau" est situé à l'abscisse $x = \frac{1}{2n}$, et la valeur de la fonction en ce point est exactement $1$.
Donc, $\sup_{x \in [0,1]} |f_n(x) - 0| = f_n(\frac{1}{2n}) = 1$.
Ainsi, pour tout $n \geq 2$, $\|f_n - f\|_\infty = 1$.
La limite de la norme infinie est $\lim_{n \to \infty} 1 = 1 \neq 0$.
La convergence n'est donc pas uniforme sur $[0,1]$, bien que la suite soit constituée de fonctions continues convergeant vers une fonction continue.
