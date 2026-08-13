# Exercice 6 : Application d'Arzelà-Ascoli (1)

## Énoncé
Soit $(f_n)$ une suite de fonctions de $\mathcal{C}([0, 1], \mathbb{R})$ telles que $f_n(0) = 0$ et $\forall n, \forall x \in [0, 1], |f_n'(x)| \le 2$.
Montrer qu'il existe une sous-suite $(f_{n_k})$ qui converge uniformément vers une fonction $f$.

## Correction Détaillée

Nous allons utiliser le théorème d'Arzelà-Ascoli. Soit $\mathcal{F} = \{f_n \mid n \in \mathbb{N}\}$. L'espace de départ est $[0, 1]$, qui est compact.
L'espace d'arrivée est $\mathbb{R}$.

1. **Équicontinuité :**
D'après l'inégalité des accroissements finis, puisque $|f_n'(x)| \le 2$, toutes les fonctions $f_n$ sont 2-lipschitziennes :
$\forall x, y \in [0, 1], |f_n(x) - f_n(y)| \le 2|x - y|$.
Pour $\epsilon > 0$, on prend $\delta = \epsilon/2$. Alors $|x-y| < \delta \implies |f_n(x)-f_n(y)| < \epsilon$.
La famille $\mathcal{F}$ est équicontinue.

2. **Compacité ponctuelle (Bornitude) :**
Soit $x \in [0, 1]$. On a :
$|f_n(x)| = |f_n(x) - f_n(0)| \le 2|x - 0| = 2x \le 2$.
Donc, pour tout $x \in [0, 1]$, l'ensemble $\{f_n(x) \mid n \in \mathbb{N}\}$ est inclus dans $[-2, 2]$, qui est borné dans $\mathbb{R}$, donc relativement compact (Bolzano-Weierstrass).

3. **Conclusion :**
Les conditions du théorème d'Arzelà-Ascoli sont vérifiées. L'ensemble $\mathcal{F}$ est relativement compact dans $(\mathcal{C}([0, 1]), \|\cdot\|_\infty)$.
Ainsi, de la suite $(f_n)$, on peut extraire une sous-suite $(f_{n_k})$ convergente pour la norme infinie, ce qui signifie qu'elle converge uniformément vers une fonction $f$.
