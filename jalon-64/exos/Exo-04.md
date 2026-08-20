---
title: "Exercice 4 : Mesure de l'ensemble de Cantor"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

## Énoncé

L'ensemble de Cantor (ou poussière de Cantor) $\mathcal{C}$ est construit de manière itérative sur le segment $C_0 = [0, 1]$.
À l'étape $n=1$, on retire le tiers central ouvert de $C_0$, obtenant $C_1 = [0, 1/3] \cup [2/3, 1]$.
À l'étape $n+1$, on retire le tiers central ouvert de chacun des segments composant $C_n$ pour former $C_{n+1}$.
L'ensemble de Cantor est l'intersection de toutes ces itérations : $\mathcal{C} = \bigcap_{n=0}^{+\infty} C_n$.

Démontrer rigoureusement que la mesure de Lebesgue de l'ensemble de Cantor est nulle : $\lambda(\mathcal{C}) = 0$.

## Correction Détaillée

1. **Calcul de la mesure à l'étape $n$ :**
À l'étape initiale $n=0$, on a un seul segment $C_0 = [0, 1]$. Sa longueur totale est $\lambda(C_0) = 1$.
À l'étape $n=1$, on retire un intervalle de longueur $1/3$. La mesure restante est :
$$\lambda(C_1) = \lambda([0, 1/3]) + \lambda([2/3, 1]) = \frac{1}{3} + \frac{1}{3} = \frac{2}{3}$$
Procédons par récurrence. Supposons que $C_n$ soit l'union disjointe de $2^n$ segments fermés, chacun de longueur $\left(\frac{1}{3}\right)^n$. La mesure totale est donc $\lambda(C_n) = 2^n \times \left(\frac{1}{3}\right)^n = \left(\frac{2}{3}\right)^n$.
Pour passer de $C_n$ à $C_{n+1}$, on divise chaque segment de longueur $L$ en trois et on retire la partie centrale. Chaque segment laisse place à deux segments de longueur $L/3$.
Ainsi, $C_{n+1}$ sera composé de $2 \times 2^n = 2^{n+1}$ segments fermés, chacun ayant pour longueur $\frac{1}{3} \times \left(\frac{1}{3}\right)^n = \left(\frac{1}{3}\right)^{n+1}$.
La mesure totale de $C_{n+1}$ est donc :
$$\lambda(C_{n+1}) = 2^{n+1} \times \left(\frac{1}{3}\right)^{n+1} = \left(\frac{2}{3}\right)^{n+1}$$
La relation de récurrence est prouvée. Pour tout $n \in \mathbb{N}$, on a $\lambda(C_n) = \left(\frac{2}{3}\right)^n$.

2. **Monotonie et passage à la limite :**
Par construction géométrique, on a une suite décroissante d'ensembles pour l'inclusion :
$$C_0 \supset C_1 \supset C_2 \supset \dots \supset C_n \supset C_{n+1} \dots$$
L'ensemble de Cantor $\mathcal{C}$ est défini comme l'intersection : $\mathcal{C} = \bigcap_{n=0}^{+\infty} C_n$.
Par conséquent, pour tout entier $n$, on a l'inclusion $\mathcal{C} \subset C_n$.
Par monotonie de la mesure extérieure (démontrée à l'Exercice 3), nous pouvons majorer la mesure de l'ensemble de Cantor :
$$\forall n \in \mathbb{N}, \quad \lambda^*(\mathcal{C}) \le \lambda^*(C_n) = \left(\frac{2}{3}\right)^n$$
La mesure extérieure étant nécessairement positive, on a l'encadrement :
$$0 \le \lambda^*(\mathcal{C}) \le \left(\frac{2}{3}\right)^n$$

3. **Conclusion algébrique :**
La suite géométrique $u_n = \left(\frac{2}{3}\right)^n$ a pour raison $q = 2/3$. Comme $|q| < 1$, la suite $(u_n)$ converge irrémédiablement vers $0$ lorsque $n$ tend vers l'infini.
En passant à la limite $n \to +\infty$ dans l'encadrement précédent, le théorème des gendarmes impose inexorablement :
$$\lambda^*(\mathcal{C}) = 0$$
L'ensemble de Cantor est un ensemble fermé (intersection de fermés), donc borélien, donc mesurable au sens de Lebesgue. On conclut donc formellement que sa mesure de Lebesgue est nulle : $\lambda(\mathcal{C}) = 0$.

*(Note topologique : Bien que de mesure nulle, l'ensemble de Cantor n'est absolument pas dénombrable. Il a la puissance du continu (même cardinalité que $\mathbb{R}$), illustrant de façon saisissante qu'un sous-ensemble "indénombrable" peut tout à fait être "infiniment fin" spatialement).*
