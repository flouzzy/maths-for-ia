# Exercice 5 : Suite de primitives

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $(f_n)_{n\in\mathbb{N}}$ une suite de fonctions continues sur $[a, b]$, à valeurs réelles.
On suppose que la suite $(f_n)$ est uniformément bornée, c'est-à-dire qu'il existe $M > 0$ tel que pour tout $n \in \mathbb{N}$ et pour tout $x \in [a, b]$, $|f_n(x)| \le M$.

Pour tout $n \in \mathbb{N}$, on définit la primitive $F_n$ de $f_n$ s'annulant en $a$ :
$$ F_n(x) = \int_a^x f_n(t) dt $$
Montrer que la suite $(F_n)$ admet une sous-suite uniformément convergente sur $[a, b]$.

## Résolution Détaillée

Pour prouver ce résultat, nous allons appliquer le théorème d'Arzelà-Ascoli à la famille $\mathcal{G} = \{F_n \mid n \in \mathbb{N}\}$. L'espace de départ $[a, b]$ est compact. Nous devons démontrer la bornitude ponctuelle et l'équicontinuité.

### 1. Bornitude ponctuelle (et uniforme) de la famille

Évaluons $F_n(x)$ en module. Pour $x \in [a, b]$ :
$$ |F_n(x)| = \left| \int_a^x f_n(t) dt \right| \le \int_a^x |f_n(t)| dt $$
D'après l'hypothèse, $|f_n(t)| \le M$ uniformément, donc :
$$ \int_a^x |f_n(t)| dt \le \int_a^x M dt = M(x - a) \le M(b - a) $$
Ainsi, pour tout $x \in [a, b]$ et pour tout $n \in \mathbb{N}$, $|F_n(x)| \le M(b - a)$.
La famille $(F_n)$ est donc uniformément bornée, ce qui implique que pour chaque $x$, l'ensemble d'évaluation $\{F_n(x) \mid n \in \mathbb{N}\}$ est inclus dans le compact $[-M(b-a), M(b-a)]$. La condition de bornitude ponctuelle est amplement satisfaite.

### 2. Équicontinuité de la famille

Considérons deux points quelconques $x, y \in [a, b]$ (supposons $x < y$). Évaluons l'écart $|F_n(y) - F_n(x)|$ :
$$ F_n(y) - F_n(x) = \int_a^y f_n(t) dt - \int_a^x f_n(t) dt = \int_x^y f_n(t) dt $$
On applique l'inégalité triangulaire pour les intégrales :
$$ |F_n(y) - F_n(x)| \le \int_x^y |f_n(t)| dt \le \int_x^y M dt = M|y - x| $$
Cette inégalité prouve que chaque fonction $F_n$ est $M$-Lipschitzienne.
Soit $\epsilon > 0$. En choisissant $\delta = \frac{\epsilon}{M} > 0$, on obtient, indépendamment de $n$ :
$$ |x - y| < \delta \implies |F_n(x) - F_n(y)| \le M|x - y| < M \frac{\epsilon}{M} = \epsilon $$
La famille $\mathcal{G} = (F_n)_{n\in\mathbb{N}}$ est donc équicontinue.

### 3. Conclusion par le Théorème d'Arzelà-Ascoli

Les fonctions $F_n$ sont définies sur le compact $[a, b]$, à valeurs dans le métrique complet $\mathbb{R}$. La famille est équicontinue et ponctuellement bornée. D'après le théorème d'Arzelà-Ascoli, la famille $\mathcal{G}$ est relativement compacte pour la norme uniforme. Ainsi, de la suite $(F_n)$, on peut extraire une sous-suite uniformément convergente vers une fonction limite continue sur $[a, b]$. $\blacksquare$
