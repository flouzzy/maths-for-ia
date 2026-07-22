# Exercice 1 : Rayon de convergence élémentaire (Règle de d'Alembert)

**Énoncé :**
Déterminer le rayon de convergence $R$ de la série entière complexe $\sum_{n \geq 1} \frac{z^n}{n \cdot 2^n}$.

**Correction détaillée :**
Soit $a_n = \frac{1}{n \cdot 2^n}$ le coefficient général de notre série entière.
Puisque $a_n \neq 0$ pour tout $n \geq 1$, nous sommes autorisés à appliquer la règle de d'Alembert pour le calcul du rayon de convergence.
Évaluons le quotient en valeur absolue :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{\frac{1}{(n+1) \cdot 2^{n+1}}}{\frac{1}{n \cdot 2^n}} $$
Décomposons la fraction complexe par multiplication par l'inverse :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{n \cdot 2^n}{(n+1) \cdot 2^{n+1}} $$
Factorisons les puissances de 2 :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{n}{n+1} \cdot \frac{2^n}{2^n \cdot 2^1} = \frac{n}{n+1} \cdot \frac{1}{2} $$
Prenons la limite lorsque l'entier $n$ tend vers l'infini. Le terme rationnel $\frac{n}{n+1}$ se réécrit en factorisant par $n$ : $\frac{n}{n(1 + 1/n)} = \frac{1}{1 + 1/n}$, qui converge vers $1$.
Par suite :
$$ L = \lim_{n \to +\infty} \left| \frac{a_{n+1}}{a_n} \right| = 1 \cdot \frac{1}{2} = \frac{1}{2} $$
Selon le théorème associé à la règle de d'Alembert, le rayon de convergence $R$ est l'inverse de la limite $L$.
Ainsi,
$$ R = \frac{1}{1/2} = 2 $$
Le rayon de convergence de la série entière est donc exactement $R = 2$.
