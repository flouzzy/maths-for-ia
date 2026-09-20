# Exercice 4 : Minkowski pour p=1

**Difficulté :** ★★☆☆☆


## Énoncé
Démontrer l'inégalité de Minkowski dans $L^1(\mathbb{R})$, c'est-à-dire :
$$ \int_{\mathbb{R}} |f(x) + g(x)| \, dx \le \int_{\mathbb{R}} |f(x)| \, dx + \int_{\mathbb{R}} |g(x)| \, dx $$

## Correction Détaillée
La preuve repose sur l'inégalité triangulaire de la valeur absolue dans $\mathbb{R}$.
Pour tout réel $x \in \mathbb{R}$, on a ponctuellement :
$$ |f(x) + g(x)| \le |f(x)| + |g(x)| $$
En utilisant la croissance de l'intégrale de Lebesgue (si $A \le B$ presque partout, alors $\int A \le \int B$), on intègre cette inégalité ponctuelle sur $\mathbb{R}$ :
$$ \int_{\mathbb{R}} |f(x) + g(x)| \, dx \le \int_{\mathbb{R}} \left( |f(x)| + |g(x)| \right) \, dx $$
Par linéarité de l'intégrale :
$$ \int_{\mathbb{R}} \left( |f(x)| + |g(x)| \right) \, dx = \int_{\mathbb{R}} |f(x)| \, dx + \int_{\mathbb{R}} |g(x)| \, dx $$
Ce qui conclut la preuve, donnant la norme $\|f+g\|_1 \le \|f\|_1 + \|g\|_1$.
