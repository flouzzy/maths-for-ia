# Exercice 1 : Convergence simple vs uniforme : Défaut de continuité

**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit la suite de fonctions $f_n : [0, 1] \to \mathbb{R}$ définie par $f_n(x) = x^n$ pour tout $n \in \mathbb{N}$ et $x \in [0, 1]$.
1. Déterminer la limite simple $f$ de la suite $(f_n)$ sur $[0, 1]$.
2. La convergence de $(f_n)$ vers $f$ est-elle uniforme sur $[0, 1]$ ? Justifier rigoureusement par le calcul, puis par le théorème de conservation de la continuité.

## Résolution Détaillée

### 1. Limite simple

Soit $x \in [0, 1]$. Fixons $x$ et étudions la limite de la suite numérique $(x^n)_{n\in\mathbb{N}}$.
- Si $x \in [0, 1[$, alors la suite géométrique $x^n$ tend vers $0$ lorsque $n \to +\infty$.
- Si $x = 1$, alors pour tout $n$, $f_n(1) = 1^n = 1$. Ainsi, $\lim_{n \to \infty} f_n(1) = 1$.

La suite $(f_n)$ converge donc simplement sur $[0, 1]$ vers la fonction $f$ définie par :
$$ f(x) = \begin{cases} 0 & \text{si } 0 \le x < 1 \\ 1 & \text{si } x = 1 \end{cases} $$

### 2. Étude de la convergence uniforme

**Méthode 1 : Par le calcul direct de la norme infinie**
Évaluons la distance uniforme $\|f_n - f\|_\infty$ sur $[0, 1]$.
$$ \sup_{x \in [0, 1]} |f_n(x) - f(x)| = \max \left( \sup_{x \in [0, 1[} |x^n - 0|, |1^n - 1| \right) $$
Sur $[0, 1[$, la fonction $x \mapsto x^n$ est strictement croissante et tend vers $1$ lorsque $x \to 1$.
Donc $\sup_{x \in [0, 1[} |x^n| = 1$.
Ainsi, $\|f_n - f\|_\infty = 1$.
Puisque la norme infinie ne tend pas vers $0$ quand $n \to +\infty$, la convergence n'est pas uniforme sur $[0, 1]$.

**Méthode 2 : Par le théorème de conservation de la continuité**
Pour tout $n \in \mathbb{N}$, la fonction $f_n : x \mapsto x^n$ est polynomiale, donc continue sur le compact $[0, 1]$.
Or, la fonction limite $f$ présente une discontinuité en $x = 1$ (car $\lim_{x \to 1^-} f(x) = 0 \neq f(1) = 1$).
D'après le théorème de conservation de la continuité, si la convergence était uniforme, la limite $f$ d'une suite de fonctions continues serait continue. La discontinuité de $f$ interdit donc catégoriquement la convergence uniforme. $\blacksquare$
