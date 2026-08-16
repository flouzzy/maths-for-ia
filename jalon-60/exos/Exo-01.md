---
title: "Exercice 1 : Approximation d'une constante"
difficulty: $\bigstar\star\star\star\star$
---

# Exercice 1 : Approximation d'une constante

## Énoncé

Soit $f(x) = C$ une fonction constante sur l'intervalle $[0, 1]$. Montrez comment on peut représenter exactement cette fonction en utilisant un réseau de neurones à une couche cachée avec une seule fonction d'activation sigmoïde $\sigma(x) = \frac{1}{1 + e^{-x}}$.

## Correction Rigoureuse

**Étape 1 : Choix des poids et biais**
La fonction $\sigma$ est bornée entre 0 et 1.
Considérons le réseau $G(x) = \alpha \sigma(wx + b)$.
Pour obtenir une constante, la solution la plus simple est de rendre l'entrée de la sigmoïde constante, indépendante de $x$.
On choisit donc le poids $w = 0$.

**Étape 2 : Détermination de l'amplitude**
L'expression devient $G(x) = \alpha \sigma(b)$.
La valeur de $\sigma(b)$ est une constante. Pour simplifier, choisissons $b = 0$. On sait que $\sigma(0) = \frac{1}{1 + e^0} = 0.5$.
Ainsi, $G(x) = \alpha \times 0.5$.

**Étape 3 : Égalisation avec la fonction cible**
On souhaite que $G(x) = C$. On pose donc $0.5 \alpha = C$, ce qui donne $\alpha = 2C$.
Le réseau $G(x) = 2C \sigma(0 \cdot x + 0)$ représente de manière exacte la fonction constante $f(x) = C$ sur tout $\mathbb{R}$, et donc en particulier sur $[0, 1]$. $\blacksquare$
