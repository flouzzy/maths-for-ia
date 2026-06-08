# Exercice 3 : Dimension VC des demi-droites
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}$. Montrer que la classe des intervalles $\mathcal{F} = \{ (-\infty, a] \mid a \in \mathbb{R} \}$ a une dimension VC égale à 1.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Il faut montrer qu'on peut pulvériser un point, mais pas deux points.
* *Résolution pas-à-pas :*
**Étape 1 : Pulvérisation d'un point.**
Soit $S = \{x_1\}$ un ensemble contenant 1 seul point. L'ensemble des parties de $S$ est $\{\emptyset, \{x_1\}\}$.
- Pour obtenir $\emptyset$, choisissons $a < x_1$. Alors $x_1 \notin (-\infty, a]$, donc $S \cap (-\infty, a] = \emptyset$.
- Pour obtenir $\{x_1\}$, choisissons $a \ge x_1$. Alors $x_1 \in (-\infty, a]$, donc $S \cap (-\infty, a] = \{x_1\}$.
Ainsi, la classe $\mathcal{F}$ peut pulvériser tout ensemble de taille 1. Donc $VC(\mathcal{F}) \ge 1$.

**Étape 2 : Impossibilité de pulvériser deux points.**
Soit $S = \{x_1, x_2\}$ un ensemble contenant 2 points quelconques. Sans perte de généralité, supposons $x_1 < x_2$. L'ensemble des parties de $S$ est $\{\emptyset, \{x_1\}, \{x_2\}, \{x_1, x_2\}\}$.
Considérons le sous-ensemble $T = \{x_2\}$. Pour obtenir $S \cap (-\infty, a] = \{x_2\}$, il faudrait que :
1. $x_2 \in (-\infty, a]$, ce qui implique $x_2 \le a$.
2. $x_1 \notin (-\infty, a]$, ce qui implique $x_1 > a$.
Or, si $x_1 > a$ et $x_2 \le a$, cela implique $x_1 > x_2$, ce qui contredit notre hypothèse de départ $x_1 < x_2$.
Par conséquent, aucun choix de $a$ ne permet d'isoler $\{x_2\}$ sans inclure $x_1$. L'ensemble $S$ de taille 2 ne peut pas être pulvérisé.
Puisque cela est vrai pour tout ensemble de taille 2, $VC(\mathcal{F}) < 2$.
En conclusion, $VC(\mathcal{F}) = 1$. $\blacksquare$
