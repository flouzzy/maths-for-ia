# Exercice 5 : Équicontinuité

## Énoncé
Soit $M > 0$. On considère $\mathcal{F} = \left\lbrace f \in \mathcal{C}^1([0, 1], \mathbb{R}) \mid \forall x \in [0, 1], |f'(x)| \le M \right\rbrace$.
Montrer que $\mathcal{F}$ est une famille équicontinue.

## Correction Détaillée

Soit $f \in \mathcal{F}$. Par l'inégalité des accroissements finis, pour tous $x, y \in [0, 1]$, on a :
$$|f(x) - f(y)| \le \sup_{t \in [0, 1]} |f'(t)| \cdot |x - y|$$
Par hypothèse, $|f'(t)| \le M$, d'où :
$$|f(x) - f(y)| \le M |x - y|$$
Cela signifie que toutes les fonctions de $\mathcal{F}$ sont $M$-lipschitziennes.

Soit $\epsilon > 0$. Posons $\delta = \frac{\epsilon}{M} > 0$.
Pour toute fonction $f \in \mathcal{F}$ et pour tous $x, y \in [0, 1]$, si $|x - y| < \delta$, alors :
$$|f(x) - f(y)| \le M |x - y| < M \left(\frac{\epsilon}{M}\right) = \epsilon$$

Le $\delta$ choisi ne dépend que de $\epsilon$ (et de la constante $M$), mais ni de $x$, ni de $y$, ni surtout du choix de la fonction $f$ dans la famille $\mathcal{F}$.
La famille $\mathcal{F}$ est donc uniformément équicontinue sur $[0, 1]$.
