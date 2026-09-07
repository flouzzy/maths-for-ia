# Exercice 9 : Produit infini et intégration

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
On s'intéresse à l'intégrale $\int_0^1 \prod_{k=1}^n \left( 1 + \frac{x^k}{k} \right) dx$.
Montrer que la limite quand $n \to \infty$ de cette intégrale existe et justifier s'il est possible d'inverser limite et intégrale.

**Solution Détaillée :**
1. Considérons les fonctions $P_n(x) = \prod_{k=1}^n \left( 1 + \frac{x^k}{k} \right)$ pour $x \in [0, 1]$.
2. Les termes du produit sont strictement supérieurs à 1 car $x > 0$ sur $]0, 1]$.
3. On calcule le rapport successif : $\frac{P_{n+1}(x)}{P_n(x)} = 1 + \frac{x^{n+1}}{n+1} \ge 1$.
Donc la suite $(P_n)$ est **croissante** et positive.
4. Convergence du produit infini : Le produit $\prod (1 + a_k)$ avec $a_k > 0$ converge si et seulement si la série $\sum a_k$ converge. Ici, $a_k = \frac{x^k}{k}$. Pour $x \in [0, 1[$, la série entière converge. En $x=1$, la série $\sum 1/k$ diverge, mais c'est un point unique (de mesure de Lebesgue nulle, donc n'affecte pas l'intégrale globale).
Ainsi, $P_n(x)$ converge vers une fonction mesurable positive $P(x)$ sur $[0, 1[$.
5. D'après Beppo Levi, puisque $(P_n)$ est croissante et positive :
$$\lim_{n \to \infty} \int_0^1 P_n(x) dx = \int_0^1 \left( \prod_{k=1}^\infty \left( 1 + \frac{x^k}{k} \right) \right) dx$$
Ici, Beppo Levi est la clé unique : aucune majoration globale simple par une fonction constante intégrable n'est requise, car la simple propriété de monotonie multiplicative suffit à garantir la conservation du comportement asymptotique intégral.
