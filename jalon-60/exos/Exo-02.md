---
title: "Exercice 2 : Interpolation linéaire par morceaux avec ReLU"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 2 : Interpolation linéaire par morceaux avec ReLU

## Énoncé

La fonction ReLU est définie par $\sigma(x) = \max(0, x)$.
Construisez explicitement un réseau de neurones $G(x)$ combinant des fonctions ReLU qui approche la fonction "valeur absolue" $f(x) = |x|$ sur $[-1, 1]$.
Montrez que l'approximation peut être exacte avec un nombre fini de neurones.

## Correction Rigoureuse

**Étape 1 : Analyse de la fonction cible**
La fonction $f(x) = |x|$ est définie par :
- $f(x) = -x$ si $x \leq 0$
- $f(x) = x$ si $x \geq 0$

**Étape 2 : Utilisation des propriétés de ReLU**
Remarquons que pour tout réel $x$ :
$x = \max(0, x) - \max(0, -x) = \sigma(x) - \sigma(-x)$
$|x| = \max(0, x) + \max(0, -x) = \sigma(x) + \sigma(-x)$

**Étape 3 : Construction du réseau**
Nous pouvons donc poser directement :
$$G(x) = \sigma(x) + \sigma(-x)$$
Ce réseau utilise $N=2$ neurones dans sa couche cachée :
- Neurone 1 : poids $w_1 = 1$, biais $b_1 = 0$, amplitude $\alpha_1 = 1$
- Neurone 2 : poids $w_2 = -1$, biais $b_2 = 0$, amplitude $\alpha_2 = 1$

**Étape 4 : Conclusion**
Le réseau $G(x)$ reproduit exactement $f(x) = |x|$ sur tout $\mathbb{R}$, sans erreur. L'approximation est exacte avec $N=2$. $\blacksquare$
