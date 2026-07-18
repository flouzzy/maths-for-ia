# Exercice 3 : Polynômes annulateurs et Nilpotence (★★)

Soit $f \in \mathcal{L}(E)$ un endomorphisme d'un espace vectoriel de dimension $n$.
On suppose que $f$ est nilpotent. Montrer, sans utiliser le polynôme caractéristique ni le théorème de Cayley-Hamilton, que $f^n = 0_{\mathcal{L}(E)}$.

### Solution :

Puisque $f$ est nilpotent, il existe un entier $p \in \mathbb{N}^*$ tel que $f^p = 0_{\mathcal{L}(E)}$.
On définit l'indice de nilpotence de $f$, noté $k$, comme le plus petit entier strictement positif tel que $f^k = 0$.
Par définition, $f^{k-1} \neq 0$.
Il existe donc un vecteur $x \in E$ tel que $f^{k-1}(x) \neq 0_E$.

Considérons la famille de vecteurs $\mathcal{F} = \left( x, f(x), f^2(x), \ldots, f^{k-1}(x) \right)$.
Montrons que cette famille est libre dans $E$.
Soient $\lambda_0, \lambda_1, \ldots, \lambda_{k-1} \in \mathbb{K}$ tels que :
$$ \sum_{i=0}^{k-1} \lambda_i f^i(x) = 0_E $$
Appliquons l'opérateur $f^{k-1}$ à cette égalité.
Puisque $f$ est un endomorphisme, on a :
$$ \sum_{i=0}^{k-1} \lambda_i f^{k-1+i}(x) = 0_E $$
Or, pour tout $i \geq 1$, l'exposant $k-1+i \geq k$. Par définition de l'indice de nilpotence $k$, $f^{k-1+i}(x) = 0_E$.
Ainsi, la somme se réduit à son premier terme :
$$ \lambda_0 f^{k-1}(x) = 0_E $$
Puisque $f^{k-1}(x) \neq 0_E$, on déduit que $\lambda_0 = 0$.

L'égalité initiale devient alors $\sum_{i=1}^{k-1} \lambda_i f^i(x) = 0_E$.
On applique ensuite $f^{k-2}$ à cette nouvelle égalité, ce qui annule tous les termes sauf celui en $\lambda_1$, donnant $\lambda_1 f^{k-1}(x) = 0_E \implies \lambda_1 = 0$.
Par une récurrence finie évidente, on obtient successivement $\lambda_0 = \lambda_1 = \ldots = \lambda_{k-1} = 0$.
La famille $\mathcal{F}$ est donc une famille libre de $E$.

Puisque $E$ est un espace vectoriel de dimension $n$, la taille maximale d'une famille libre dans $E$ est exactement $n$.
La famille $\mathcal{F}$ contient $k$ vecteurs.
Par le théorème de la dimension, on en déduit que $k \leq n$.
Puisque $f^k = 0$, et que $n \geq k$, on a $f^n = f^{n-k} \circ f^k = f^{n-k} \circ 0 = 0_{\mathcal{L}(E)}$.
Ce résultat est un préliminaire fondamental pour l'étude de la partie nilpotente dans la décomposition de Dunford.
