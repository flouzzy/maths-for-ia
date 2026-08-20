---
title: "Exercice 8 : L'ensemble de Vitali, existence d'un ensemble non-mesurable"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

## Énoncé

Le but de cet exercice est de démontrer, en utilisant l'axiome du choix, qu'il existe un sous-ensemble de $\mathbb{R}$ qui n'est pas mesurable au sens de Lebesgue.
Sur le segment $I = [0, 1]$, on définit la relation d'équivalence algébrique suivante :
$$x \sim y \iff x - y \in \mathbb{Q}$$
1. Construire l'ensemble de Vitali $V$.
2. En utilisant l'invariance par translation et la dénombrabilité de $\mathbb{Q}$, prouver par l'absurde que $V$ ne peut pas appartenir à la tribu de Lebesgue $\mathcal{L}(\mathbb{R})$.

## Correction Détaillée

### 1. Construction de l'ensemble de Vitali
La relation $x \sim y \iff x - y \in \mathbb{Q}$ est clairement une relation d'équivalence (réflexive, symétrique car $\mathbb{Q}$ est un groupe, transitive par additivité).
Elle partitionne le segment $[0, 1]$ en classes d'équivalence disjointes.
L'axiome du choix postule formellement qu'il existe une fonction de choix capable de sélectionner exactement un représentant unique au sein de chaque classe d'équivalence.
Définissons $V$ comme l'ensemble constitué de ces représentants. Par construction, $V \subset [0, 1]$ et pour tous éléments distincts $x, y \in V$, leur différence est purement irrationnelle ($x - y \notin \mathbb{Q}$).

### 2. Preuve de la non-mesurabilité par l'absurde
Raisonnons par l'absurde. Supposons au contraire que $V$ est un ensemble Lebesgue-mesurable, donc $V \in \mathcal{L}(\mathbb{R})$. Dans ce cas, il possède une mesure bien définie $\lambda(V) \ge 0$.
Considérons l'ensemble des rationnels compris dans $[-1, 1]$. Cet ensemble est dénombrable, nous pouvons donc l'énumérer sous la forme d'une suite $(q_k)_{k \ge 1}$.
Pour chaque entier $k$, considérons la translation de $V$ par le rationnel $q_k$ : $V_k = V + q_k = \{ v + q_k \mid v \in V \}$.

**A. Propriété de disjonction :**
Les translatés $V_k$ sont deux à deux disjoints. En effet, si un réel $z$ appartient à l'intersection $V_i \cap V_j$ avec $i \neq j$, il existerait $v_1, v_2 \in V$ tels que $z = v_1 + q_i = v_2 + q_j$.
Cela impliquerait $v_1 - v_2 = q_j - q_i \in \mathbb{Q}$. Or, par la règle stricte de construction de l'ensemble de Vitali, la différence de deux éléments distincts ne peut jamais être rationnelle. Donc $v_1 = v_2$, ce qui force $q_i = q_j$ et donc $i=j$, ce qui contredit l'hypothèse de départ. L'intersection est donc rigoureusement vide.

**B. Encadrement géométrique de l'union :**
Formons l'union dénombrable disjointe $U = \bigcup_{k=1}^{+\infty} V_k$.
Puisque $V \subset [0, 1]$ et que chaque $q_k \in [-1, 1]$, l'intervalle de variabilité pour tout élément $z = v + q_k$ est contraint par $0 - 1 \le z \le 1 + 1$. Ainsi, géométriquement :
$$U \subset [-1, 2]$$
D'autre part, soit $x \in [0, 1]$. Cet élément $x$ appartient nécessairement à l'une des classes d'équivalence de notre partition. Soit $v \in V$ le représentant unique de cette classe. Par définition de l'équivalence, $x - v \in \mathbb{Q}$.
De plus, $x \in [0, 1]$ et $v \in [0, 1]$, donc leur différence est bornée : $-1 \le x - v \le 1$.
Il s'ensuit que $x - v = q_m$ pour un certain indice $m$ de notre énumération. Ainsi $x = v + q_m \in V_m \subset U$.
Nous venons de démontrer la double inclusion d'encadrement topologique :
$$[0, 1] \subset U \subset [-1, 2]$$

**C. L'absurdité numérique :**
Appliquons l'opérateur de mesure de Lebesgue, qui préserve l'ordre de l'inclusion :
$$\lambda([0, 1]) \le \lambda\left( \bigcup_{k=1}^{+\infty} V_k \right) \le \lambda([-1, 2])$$
Par le théorème de $\sigma$-additivité sur des unions disjointes d'ensembles mesurables (car on a supposé $V$ mesurable, et la translation préserve la mesurabilité) :
$$1 \le \sum_{k=1}^{+\infty} \lambda(V_k) \le 3$$
Par l'invariance stricte de la mesure de Lebesgue par translation, $\lambda(V_k) = \lambda(V)$ pour tout entier $k$. La série devient une somme infinie d'une constante :
$$1 \le \sum_{k=1}^{+\infty} \lambda(V) \le 3$$
Examinons cette inégalité diophantienne implacable :
- Si la mesure $\lambda(V) = 0$, alors la somme infinie de zéros vaut exactement $0$. L'inégalité $1 \le 0$ est mathématiquement absurde.
- Si la mesure $\lambda(V) = c > 0$ (même infime), alors l'addition infinie d'une constante strictement positive diverge inévitablement vers $+\infty$. L'inégalité $+\infty \le 3$ est structurellement absurde.

**Conclusion :**
Les lois logiques du tiers exclu forcent la contradiction. L'hypothèse fondamentale était que l'ensemble de Vitali $V$ appartenait à la tribu de Lebesgue. Cette hypothèse est nécessairement fausse. Il existe donc des sous-ensembles de $\mathbb{R}$ qui ne sont pas Lebesgue-mesurables. On ne peut pas assigner une notion rigoureuse de "longueur" à toute partie de l'espace sans provoquer des contradictions mathématiques irrémédiables.
