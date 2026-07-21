---
uuid: "exo-21-05"
title: "Exercice 5 : Fonction limite discontinue"
difficulty: 3
---

# Exercice 5 : Fonction limite discontinue

**Niveau :** $★★★☆☆$

## Problème

Étudier la convergence de $f_n(x) = x^n$ sur $[0,1]$. La fonction limite est-elle continue ? Que peut-on dire de la convergence uniforme ?

## Démonstration et Solution

**Étape 1 : Étude de la convergence simple**
Nous avons démontré à l'Exercice 1 que la suite de fonctions $f_n(x) = x^n$ converge simplement sur $[0,1]$ vers la fonction limite $f$ définie par :
$f(x) = 0$ si $x \in [0, 1[$
$f(x) = 1$ si $x = 1$.

**Étape 2 : Continuité de la fonction limite**
Pour tout entier $n \geq 1$, la fonction $f_n(x) = x^n$ est une fonction polynôme, elle est donc parfaitement continue sur l'intervalle compact $[0,1]$.
Cependant, analysons la continuité de la fonction limite $f$ au point $x_0 = 1$.
Calculons la limite à gauche de $f$ en 1 :
Pour tout $x \in [0, 1[$, $f(x) = 0$. Donc, $\lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} 0 = 0$.
Or, la valeur de la fonction limite en 1 est $f(1) = 1$.
Puisque $\lim_{x \to 1^-} f(x) \neq f(1)$, la fonction $f$ présente une discontinuité de première espèce au point $x=1$. Elle n'est donc pas continue sur $[0,1]$.

**Étape 3 : Conséquence sur la convergence uniforme**
Le théorème fondamental de la continuité des limites de suites de fonctions stipule que si une suite de fonctions continues $(f_n)$ converge uniformément vers une fonction $f$ sur un intervalle $I$, alors la fonction limite $f$ est obligatoirement continue sur cet intervalle $I$.
Nous raisonnons ici par contraposée :
Puisque toutes les fonctions de la suite $f_n$ sont continues sur $[0,1]$, et puisque la fonction limite $f$ **n'est pas** continue sur $[0,1]$, la convergence de la suite $(f_n)$ vers $f$ **ne peut absolument pas** être uniforme sur $[0,1]$.
