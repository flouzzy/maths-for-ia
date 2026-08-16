---
title: "Exercice 6 : Construction d'un chapeau avec ReLU"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 6 : Construction d'un chapeau avec ReLU

## Énoncé

Construisez une "fonction chapeau" (triangle isocèle de base $[-1, 1]$ et de hauteur $1$) à l'aide de la fonction d'activation ReLU $\sigma(x) = \max(0, x)$.
Explicitez les poids et démontrez l'exactitude de l'expression.

## Correction Rigoureuse

**Étape 1 : Définition formelle de la fonction cible**
On cherche $T(x)$ telle que :
- $T(x) = 0$ si $x \leq -1$
- $T(x) = x + 1$ si $-1 \leq x \leq 0$
- $T(x) = 1 - x$ si $0 \leq x \leq 1$
- $T(x) = 0$ si $x \geq 1$

**Étape 2 : Agencement des charnières (ReLUs)**
La fonction change de pente (dérivée) aux points $x = -1, x = 0, x = 1$.
- En $x = -1$, la pente passe de $0$ à $+1$. L'incrément de pente est $+1$.
- En $x = 0$, la pente passe de $+1$ à $-1$. L'incrément de pente est $-2$.
- En $x = 1$, la pente passe de $-1$ à $0$. L'incrément de pente est $+1$.

**Étape 3 : Construction de l'expression**
Une fonction continue affine par morceaux peut s'écrire comme une somme de termes $\sigma(x - t_i)$ pondérés par les variations de pentes en $t_i$.
On pose donc :
$$T(x) = 1 \cdot \sigma(x + 1) - 2 \cdot \sigma(x - 0) + 1 \cdot \sigma(x - 1)$$

**Étape 4 : Vérification algébrique**
- Si $x \leq -1$, tous les termes dans les $\max$ sont $\leq 0$. Donc $T(x) = 0$.
- Si $-1 < x \leq 0$, $\sigma(x+1) = x+1$, les autres sont nuls. $T(x) = x+1$.
- Si $0 < x \leq 1$, $\sigma(x+1) = x+1$ et $\sigma(x) = x$. $T(x) = (x+1) - 2x = 1-x$.
- Si $x > 1$, $\sigma(x+1)=x+1$, $\sigma(x)=x$, $\sigma(x-1)=x-1$. $T(x) = (x+1) - 2x + (x-1) = 0$.
L'expression avec 3 neurones est donc parfaitement exacte. $\blacksquare$
