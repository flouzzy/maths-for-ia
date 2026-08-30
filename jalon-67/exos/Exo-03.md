---
title: "Exercice 3 : Série géométrique fonctionnelle"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 3 : Série géométrique fonctionnelle

## Énoncé

On considère l'intégrale $I = \int_0^1 \frac{1}{1-x} dx$.
En utilisant le théorème de Beppo Levi (corollaire des séries), montrer rigoureusement que cette intégrale diverge vers $+\infty$.

## Correction

1. **Développement en série :**
Pour tout $x \in [0, 1[$, on sait que $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
Posons $u_n(x) = x^n$.
Les fonctions $u_n$ sont mesurables et **strictement positives** sur l'intervalle $]0, 1[$.

2. **Application du corollaire de Beppo Levi :**
Le corollaire nous autorise à intervertir l'intégrale et la somme infinie de termes positifs :
$$ \int_0^1 \left( \sum_{n=0}^\infty x^n \right) dx = \sum_{n=0}^\infty \int_0^1 x^n dx $$

3. **Calcul explicite :**
On calcule l'intégrale de chaque monôme :
$$ \int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1} $$
En remplaçant dans la somme :
$$ I = \sum_{n=0}^\infty \frac{1}{n+1} = \sum_{k=1}^\infty \frac{1}{k} $$

4. **Conclusion :**
On reconnaît la série harmonique. Or on sait (par minoration par une intégrale ou critère de Cauchy) que la série harmonique diverge.
Donc $\sum_{k=1}^\infty \frac{1}{k} = +\infty$.
Par conséquent, l'intégrale $I$ vaut exactement $+\infty$. La démonstration est complète et rigoureuse, l'interversion a garanti la justesse du passage à la limite.
