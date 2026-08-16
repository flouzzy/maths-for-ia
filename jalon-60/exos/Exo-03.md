---
title: "Exercice 3 : La fonction porte (Bump Function) avec des échelons"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 3 : La fonction porte (Bump Function) avec des échelons

## Énoncé

Considérons une fonction d'activation échelon de Heaviside $H(x)$, valant $1$ si $x \geq 0$ et $0$ sinon.
Construisez mathématiquement une "porte" de hauteur $h$, qui vaut $h$ sur l'intervalle $[a, b]$ (avec $a < b$) et $0$ en dehors.

## Correction Rigoureuse

**Étape 1 : Translation de l'échelon**
La fonction $H(x - a)$ "s'allume" et passe à 1 pour tout $x \geq a$.
La fonction $H(x - b)$ "s'allume" et passe à 1 pour tout $x \geq b$.

**Étape 2 : Combinaison linéaire pour former un créneau**
Si nous soustrayons la seconde à la première, on obtient :
$\Pi_{[a, b)}(x) = H(x - a) - H(x - b)$
Cette fonction vaut :
- $0 - 0 = 0$ pour $x < a$
- $1 - 0 = 1$ pour $a \leq x < b$
- $1 - 1 = 0$ pour $x \geq b$
C'est exactement la fonction indicatrice de l'intervalle $[a, b)$.

**Étape 3 : Ajustement de l'amplitude**
Pour obtenir une hauteur $h$, il suffit de multiplier l'expression entière par $h$ :
$G(x) = h H(x - a) - h H(x - b)$
Ce réseau utilise $N=2$ neurones avec la fonction d'activation de Heaviside. $\blacksquare$
