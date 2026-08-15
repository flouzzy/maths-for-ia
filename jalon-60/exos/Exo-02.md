---
title: "Exo 02 : Représentation de fonctions affines par des sigmoïdes"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exo 02 : Représentation de fonctions affines par des sigmoïdes

## Énoncé formel
Le théorème d'approximation universelle stipule qu'une fonction continue sur un compact peut être approximée. Montrez comment approximer l'opérateur linéaire identité $f(x) = x$ sur le segment $[-1, 1]$ à l'aide d'une fonction sigmoïde lisse $\sigma(t)$. Quelle est la limite des poids utilisés pour cette construction ?

---

## Démonstration et correction pas à pas
Si l'on considère le développement de Taylor de la fonction d'activation lisse $\sigma(t)$ en un point $t_0$ où la dérivée $\sigma'(t_0) \neq 0$. Supposons $t_0 = 0$ et soit $k = \sigma'(0) \neq 0$. \n\nOn a $\sigma(\epsilon x) = \sigma(0) + \epsilon x \sigma'(0) + O(\epsilon^2)$.\n\nIsolons le terme linéaire : $\epsilon x \sigma'(0) = \sigma(\epsilon x) - \sigma(0) - O(\epsilon^2)$.\n\nAinsi, on peut poser $g(x) = \frac{1}{\epsilon \sigma'(0)} \left[ \sigma(\epsilon x) - \sigma(0) \right]$. Remarquons que le terme constant $-\sigma(0)$ peut être obtenu comme une simple soustraction de poids de sortie. Cette fonction est de la forme autorisée par le réseau de neurones avec deux neurones (l'un valant la constante $\sigma(0)$ obtenue avec un poids nul, l'autre étant $\sigma(\epsilon x)$) ou simplement avec un biais de sortie. \n\nLorsque $\epsilon \to 0$, l'erreur résiduelle, gouvernée par $O(\epsilon^2) / \epsilon = O(\epsilon)$, tend uniformément vers zéro sur tout compact $[-1, 1]$. On voit donc qu'approximer la fonction linéaire parfaite nécessite un poids d'entrée $\epsilon \to 0$ et un poids de sortie $\frac{1}{\epsilon \sigma'(0)} \to \infty$. C'est typiquement ce qui mène aux instabilités numériques si la régularisation n'est pas appliquée lors de l'apprentissage.
