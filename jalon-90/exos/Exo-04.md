# Exercice 4 : Convergence en probabilité vers une constante et convergence en loi
$\bigstar\bigstar\star\star\star$


Soit $(X_n)$ une suite de variables aléatoires et $c$ une constante réelle. Montrez que si $X_n \xrightarrow{\mathcal{L}} c$, alors $X_n \xrightarrow{\mathbb{P}} c$.
*Remarque :* C'est une situation où la convergence en loi implique la convergence en probabilité.

**Correction :**
1. Par définition de la convergence en loi, $F_n(x) \to F(x)$ en tout point de continuity de $F$.
2. Ici $X = c$ est une constante. La fonction de répartition $F$ de la constante $c$ est une marche : $F(x) = 0$ pour $x < c$ et $F(x) = 1$ pour $x \geq c$. Le seul point de discontinuité de $F$ est $c$.
3. Soit $\epsilon > 0$. Les points $c - \epsilon$ et $c + \epsilon$ sont des points de continuité de $F$.
4. Évaluons la probabilité de l'écart :
$$ \mathbb{P}(|X_n - c| > \epsilon) = \mathbb{P}(X_n < c - \epsilon) + \mathbb{P}(X_n > c + \epsilon) $$
$$ \mathbb{P}(|X_n - c| > \epsilon) \leq F_n(c-\epsilon) + (1 - F_n(c+\epsilon)) $$
5. Passons à la limite quand $n \to \infty$ :
- $F_n(c-\epsilon) \to F(c-\epsilon) = 0$ car $c-\epsilon < c$.
- $F_n(c+\epsilon) \to F(c+\epsilon) = 1$ car $c+\epsilon > c$.
6. Ainsi $\lim_{n\to\infty} \mathbb{P}(|X_n - c| > \epsilon) \leq 0 + 1 - 1 = 0$. La limite étant positive, elle est strictement égale à $0$, prouvant la convergence en probabilité.
