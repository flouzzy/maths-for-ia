# Exercice 6 : Convergence Faible des Suites
$\bigstar\bigstar\bigstar\star\star$
**Énoncé :**
Soit $E$ un espace de Banach et $(x_n)$ une suite d'éléments de $E$.
On dit que la suite $(x_n)$ converge faiblement vers $x \in E$ si, pour toute forme linéaire continue $f \in E^*$, on a $\lim_{n \to \infty} f(x_n) = f(x)$.
Démontrer que toute suite faiblement convergente est bornée.

**Correction :**
1. Nous allons utiliser l'injection canonique $J : E \to E^{**}$ définie par $J(x)(f) = f(x)$ pour tout $f \in E^*$.
   On sait que $J(x)$ est une forme linéaire continue sur l'espace de Banach $E^*$, et que $\|J(x)\|_{E^{**}} = \|x\|_E$.
2. Considérons la famille d'opérateurs $(J(x_n))_{n \in \mathbb{N}}$ de $E^*$ vers $\mathbb{K}$.
   Par hypothèse de convergence faible, pour tout $f \in E^*$, la suite $(f(x_n))_{n}$ est convergente, donc elle est bornée.
   Ainsi, pour tout $f \in E^*$, $\sup_n |J(x_n)(f)| = \sup_n |f(x_n)| < \infty$.
   La famille $(J(x_n))$ est donc ponctuellement bornée sur $E^*$.
3. L'espace $E^*$ est un espace de Banach. Par le théorème de Banach-Steinhaus, la famille $(J(x_n))$ est uniformément bornée :
   $\sup_n \|J(x_n)\|_{E^{**}} < \infty$.
4. Puisque $\|J(x_n)\|_{E^{**}} = \|x_n\|_E$, on conclut que $\sup_n \|x_n\|_E < \infty$.
   La suite $(x_n)$ est donc bien bornée.