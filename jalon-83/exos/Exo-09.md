---
uuid: jalon-83-exo-09
title: "Exercice 09 - Dérivation des distributions"
---

# Exercice 09 $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Le produit de convolution d'une distribution $T$ par une fonction test lisse $\phi \in \mathcal{D}(\mathbb{R})$ est défini par la fonction $(T * \phi)(x) = \langle T_y, \phi(x-y) \rangle$.
Démontrer que le résultat $f = T * \phi$ est non seulement une fonction usuelle, mais qu'elle est de classe $C^\infty$, et que sa dérivée classique vérifie :
$$ f' = T * \phi' = T' * \phi $$
(On justifiera la permutation formelle des opérateurs).

**Correction pas à pas :**
Démontrons que $f$ est dérivable et que $f'(x) = (T * \phi')(x)$.
Formons le taux d'accroissement de la fonction $f(x)$ :
$$ \frac{f(x+h) - f(x)}{h} = \frac{1}{h} \Big( \langle T_y, \phi(x+h-y) \rangle - \langle T_y, \phi(x-y) \rangle \Big) $$
Par linéarité de la distribution $T$ (agissant sur la variable $y$) :
$$ = \langle T_y, \frac{\phi(x+h-y) - \phi(x-y)}{h} \rangle $$
Puisque $\phi \in \mathcal{D}(\mathbb{R})$, elle est infiniment dérivable. Le taux d'accroissement de la fonction test converge vers sa dérivée par rapport à $x$, qui est $\phi'(x-y)$, uniformément et avec toutes ses dérivées sur un compact (car $\phi$ est à support compact).
Par la continuité de l'opérateur distribution $T$, on peut intervertir la limite $h \to 0$ et le crochet de dualité (c'est le fondement de la topologie de $\mathcal{D}'$) :
$$ \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = \langle T_y, \lim_{h \to 0} \frac{\phi(x+h-y) - \phi(x-y)}{h} \rangle $$
$$ f'(x) = \langle T_y, \partial_x \phi(x-y) \rangle = (T * \phi')(x) $$
Ceci prouve que $f$ est dérivable, et par récurrence, $C^\infty$.

Maintenant, montrons que $(T * \phi')(x) = (T' * \phi)(x)$.
Rappelons la règle de dérivation des fonctions composées par rapport à $y$ :
$$ \partial_y (\phi(x-y)) = -\phi'(x-y) $$
Donc $\phi'(x-y) = -\partial_y \phi(x-y)$.
Remplaçons dans l'expression de $f'$ :
$$ f'(x) = \langle T_y, \phi'(x-y) \rangle = \langle T_y, -\partial_y \phi(x-y) \rangle $$
$$ = - \langle T_y, \partial_y (\phi(x-y)) \rangle $$
Par définition de la dérivée distributionnelle d'une distribution $T$ (ici $T'$ par rapport à la variable $y$) :
$$ - \langle T_y, \partial_y \psi \rangle = \langle T'_y, \psi \rangle $$
En posant $\psi(y) = \phi(x-y)$, on obtient :
$$ f'(x) = \langle T'_y, \phi(x-y) \rangle = (T' * \phi)(x) $$
L'égalité est donc formellement établie, prouvant que la dérivation peut être "glissée" indifféremment sur la distribution ou sur la fonction de lissage. $\blacksquare$
