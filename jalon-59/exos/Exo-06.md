# Exercice 6 : Arzelà-Ascoli et dérivées

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $(f_n)_{n\in\mathbb{N}}$ une suite de fonctions de classe $\mathcal{C}^1$ sur $[0, 1]$.
On suppose que la suite est bornée ponctuellement en 0, c'est-à-dire que la suite de réels $(f_n(0))$ est bornée, et que la suite des dérivées $(f'_n)$ est uniformément bornée sur $[0, 1]$ par une constante $M > 0$ (pour tout $n$ et tout $x$, $|f'_n(x)| \le M$).

1. Montrer que la suite $(f_n)$ est uniformément bornée sur $[0, 1]$.
2. Montrer qu'on peut en extraire une sous-suite uniformément convergente.

## Résolution Détaillée

### 1. Majoration uniforme par le Théorème des Accroissements Finis

Par hypothèse, il existe $K > 0$ tel que pour tout $n \in \mathbb{N}$, $|f_n(0)| \le K$.
Pour un $n$ fixé et $x \in [0, 1]$, la fonction $f_n$ est $\mathcal{C}^1$ (donc continue et dérivable) sur $[0, 1]$.
Par le Théorème des Accroissements Finis (TAF) appliqué à $f_n$ sur le segment d'extrémités 0 et $x$ :
$$ |f_n(x) - f_n(0)| \le \sup_{t \in [0, 1]} |f'_n(t)| |x - 0| $$
L'hypothèse indique que $\sup_{t} |f'_n(t)| \le M$. De plus, $x \in [0, 1]$ donc $|x| \le 1$.
$$ |f_n(x) - f_n(0)| \le M |x| \le M $$
Par l'inégalité triangulaire inverse : $|f_n(x)| - |f_n(0)| \le |f_n(x) - f_n(0)| \le M$.
Donc, $|f_n(x)| \le M + |f_n(0)| \le M + K$.
Cette majoration ne dépend ni de $n$, ni de $x$.
La suite de fonctions $(f_n)$ est par conséquent uniformément bornée par la constante $M + K$.
Ceci assure la condition de bornitude ponctuelle du Théorème d'Arzelà-Ascoli.

### 2. Équicontinuité et Extraction

L'équicontinuité découle également de la majoration de la dérivée, qui garantit que les fonctions sont globalement Lipschitziennes.
Soient $x, y \in [0, 1]$ quelconques. Par le TAF appliqué à $f_n$ sur le segment $[x, y]$ :
$$ |f_n(y) - f_n(x)| \le \sup_{t} |f'_n(t)| |y - x| \le M|y - x| $$
Toutes les fonctions $f_n$ de la famille sont $M$-Lipschitziennes, avec la même constante $M$.
Ceci implique (comme démontré dans les exercices précédents) que la famille est équicontinue sur le compact $[0, 1]$.

En conclusion :
- Le domaine $[0, 1]$ est compact.
- L'espace d'arrivée $\mathbb{R}$ est complet.
- La famille $\{f_n \mid n \in \mathbb{N}\}$ est équicontinue (car uniformément Lipschitzienne).
- La famille est ponctuellement bornée (car uniformément bornée par $M+K$).

Le Théorème d'Arzelà-Ascoli s'applique de plein droit : la famille est relativement compacte pour la topologie de la convergence uniforme. Il existe donc une fonction d'extraction $\phi : \mathbb{N} \to \mathbb{N}$ telle que la sous-suite $(f_{\phi(n)})_{n\in\mathbb{N}}$ converge uniformément sur $[0, 1]$ vers une fonction continue. $\blacksquare$
