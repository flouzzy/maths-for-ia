# Exercice 3 : Défaut d'équicontinuité

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit la famille de fonctions $\mathcal{F} = \{f_n : x \mapsto \sin(nx) \mid n \in \mathbb{N}^* \}$ définie sur $[0, \pi]$.
1. Cette famille est-elle ponctuellement bornée ?
2. Montrer rigoureusement, en revenant à la définition, que cette famille n'est pas équicontinue en $0$.

## Résolution Détaillée

### 1. Bornitude ponctuelle

Pour tout $x \in [0, \pi]$ et pour tout $n \in \mathbb{N}^*$, nous avons $f_n(x) = \sin(nx)$.
La fonction sinus prend ses valeurs dans $[-1, 1]$, donc $|f_n(x)| \le 1$.
Ainsi, pour tout $x \in [0, \pi]$, l'ensemble d'évaluation $\{f_n(x) \mid n \in \mathbb{N}^*\} \subset [-1, 1]$ est un ensemble borné de $\mathbb{R}$. La famille est donc uniformément bornée, et *a fortiori* ponctuellement bornée.

### 2. Défaut d'équicontinuité

Rappelons la définition de l'équicontinuité en $0$ :
$\forall \epsilon > 0, \exists \delta > 0, \forall f_n \in \mathcal{F}, \forall x \in [0, \pi], |x - 0| < \delta \implies |f_n(x) - f_n(0)| < \epsilon$.

La négation de cette propriété s'écrit :
$\exists \epsilon > 0, \forall \delta > 0, \exists f_n \in \mathcal{F}, \exists x \in [0, \pi], |x| < \delta \text{ et } |f_n(x) - 0| \ge \epsilon$.

Fixons $\epsilon = \frac{1}{2}$.
Soit un $\delta > 0$ arbitraire.
Nous devons trouver un rang $n \in \mathbb{N}^*$ et un point $x \in [0, \pi]$ tel que $x < \delta$ et $\sin(nx) \ge \frac{1}{2}$.

Par la propriété d'Archimède, il existe un entier $n$ suffisamment grand tel que $\frac{\pi}{2n} < \delta$.
Choisissons donc ce $n$, et posons $x = \frac{\pi}{2n}$.
Il est clair que $0 \le x < \delta$.
Évaluons la fonction en ce point :
$$ f_n(x) = \sin\left(n \frac{\pi}{2n}\right) = \sin\left(\frac{\pi}{2}\right) = 1 $$
Nous avons bien $1 \ge \epsilon = \frac{1}{2}$.

Il est donc impossible de trouver un $\delta$ commun à toutes les fonctions de la famille qui garantisse que les variations restent petites près de 0. Géométriquement, la "pente" de $f_n$ à l'origine vaut $n$, qui tend vers l'infini, rendant les oscillations arbitrairement serrées et violant l'équicontinuité. $\blacksquare$
