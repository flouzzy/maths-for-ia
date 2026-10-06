## Exercice 4 : Continuité descendante et probabilité d'un singleton
$\bigstar\bigstar\star\star\star$

### Énoncé

Soit $\Omega = [0, 1]$ muni de la tribu borélienne et de la mesure de Lebesgue (c'est-à-dire que pour tout intervalle $[a, b]$, $\mathbb{P}([a, b]) = b - a$).
1. Soit un point fixe $x \in [0, 1]$. On pose pour tout entier $n \ge 1$, $A_n = [x - \frac{1}{n}, x + \frac{1}{n}] \cap [0, 1]$. Calculer $\mathbb{P}(A_n)$ pour $n$ assez grand.
2. Montrer, en utilisant le théorème de continuité descendante de Kolmogorov, que la probabilité de tirer exactement le nombre $x$ est rigoureusement nulle : $\mathbb{P}(\{x\}) = 0$.


### Correction Détaillée

1. **Calcul de la probabilité de l'intervalle :**
Soit $x \in ]0, 1[$. Pour $n$ suffisamment grand (tel que $x - \frac{1}{n} \ge 0$ et $x + \frac{1}{n} \le 1$), l'intervalle $A_n$ est entièrement inclus dans $[0, 1]$.
$A_n = [x - \frac{1}{n}, x + \frac{1}{n}]$.
La mesure de cet intervalle est simplement sa longueur.
$\mathbb{P}(A_n) = \left(x + \frac{1}{n}\right) - \left(x - \frac{1}{n}\right) = \frac{2}{n}$.

2. **Application de la continuité descendante :**
Considérons la suite d'événements $(A_n)$.
On remarque que $A_1 \supset A_2 \supset A_3 \dots$ car si $n \le m$, l'intervalle avec une marge de $1/m$ est inclus dans celui avec une marge de $1/n$.
La suite $(A_n)$ est donc une suite décroissante d'événements.
Quelle est l'intersection infinie de tous ces intervalles ?
$\bigcap_{n=1}^\infty A_n = \bigcap_{n=1}^\infty [x - \frac{1}{n}, x + \frac{1}{n}]$.
L'unique point qui appartient à tous ces intervalles est $x$. En effet, si $y \neq x$, il existe un entier $N$ tel que $|y - x| > \frac{1}{N}$, donc $y \notin A_N$, ce qui exclut $y$ de l'intersection infinie.
Ainsi, $\bigcap_{n=1}^\infty A_n = \{x\}$.

Par le théorème de continuité descendante (qui dérive de l'axiome de $\sigma$-additivité) :
$\mathbb{P}(\{x\}) = \mathbb{P}\left(\bigcap_{n=1}^\infty A_n\right) = \lim_{n \to \infty} \mathbb{P}(A_n)$.
$\mathbb{P}(\{x\}) = \lim_{n \to \infty} \frac{2}{n} = 0$.
La probabilité de n'importe quel singleton dans l'intervalle $[0, 1]$ muni de la mesure de Lebesgue uniforme est rigoureusement de zéro.
