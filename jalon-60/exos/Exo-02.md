# Exercice 2 : La porte logique NOT $\bigstar\star\star\star\star$
Approcher la fonction $f(x) = 1 - x$ sur $[0,1]$ avec un réseau à une couche cachée utilisant l'activation linéaire par morceaux $\sigma(x) = \max(0, \min(1, x))$ (activation Hard Sigmoid).

\textbf{Correction détaillée}
La fonction cible est affine : $f(x) = -x + 1$.
La fonction d'activation est $\sigma(t) = t$ pour $t \in [0,1]$.
Si on choisit l'argument $w x + b$ tel qu'il reste dans $[0,1]$ pour tout $x \in [0,1]$.
Posons $w = 1, b = 0$, on a $\sigma(x) = x$ pour $x \in [0,1]$.
On cherche $G(x) = \alpha \sigma(wx+b) + c$ où on autorise un biais de sortie.
Le théorème d'approximation dit qu'on peut utiliser une combinaison linéaire : $G(x) = \alpha_1 \sigma(w_1 x + b_1) + \alpha_2 \sigma(w_2 x + b_2)$.
En choisissant $w_1 = 1, b_1 = 0$, on a $\sigma(x)$.
En choisissant $w_2 = 0, b_2 = 1$, on a $\sigma(1) = 1$.
Ainsi, $G(x) = -\sigma(x) + \sigma(1) = -x + 1$.
La fonction est modélisée exactement avec deux neurones.
