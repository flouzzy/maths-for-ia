---
title: "Exercice 9 : Intégration d'une fonction Gamma sur $\mathbb{R}$"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Intégration d'une fonction Gamma sur $\mathbb{R}$

## Énoncé

Soit $F(a) = \int_0^\infty \frac{x^{a-1}}{1+x} dx$, pour $0 < a < 1$.
En développant $\frac{1}{1+x}$ en série géométrique sur l'intervalle $]0, 1[$, montrer par Beppo Levi que $\int_0^1 \frac{x^{a-1}}{1-x^2} dx = \sum_{k=0}^\infty \frac{1}{2k+a}$.
(Le but n'est pas le calcul complet de l'intégrale eulérienne, mais la validation de l'outil d'interversion sur une série particulière associée).

## Correction

1. **Série fonctionnelle :**
Sur l'intervalle $x \in ]0, 1[$, on a l'égalité $\frac{1}{1-x^2} = \sum_{k=0}^\infty (x^2)^k = \sum_{k=0}^\infty x^{2k}$.
La fonction sous l'intégrale se réécrit alors comme une série infinie :
$$ u(x) = \frac{x^{a-1}}{1-x^2} = x^{a-1} \sum_{k=0}^\infty x^{2k} = \sum_{k=0}^\infty x^{2k+a-1}. $$
Posons la suite de fonctions $u_k(x) = x^{2k+a-1}$.

2. **Validation des hypothèses :**
Pour tout $x \in ]0, 1[$ et tout $k \in \mathbb{N}$, comme $x>0$, on a $x^{2k+a-1} > 0$.
Les fonctions sont continues donc mesurables.
Nous avons une série de fonctions mesurables strictement positives.

3. **Application du corollaire :**
On applique le théorème de Beppo Levi pour la sommation des séries positives :
$$ \int_0^1 \left( \sum_{k=0}^\infty x^{2k+a-1} \right) dx = \sum_{k=0}^\infty \int_0^1 x^{2k+a-1} dx. $$

4. **Calcul de l'intégrale des termes généraux :**
Évaluons l'intégrale pour un rang $k$ donné :
$$ \int_0^1 x^{2k+a-1} dx $$
Une primitive de $x^p$ est $\frac{x^{p+1}}{p+1}$. Ici $p = 2k+a-1$. L'exposant incrémenté est $p+1 = 2k+a$.
Puisque $a > 0$ et $k \ge 0$, on a $2k+a > 0$, donc la primitive ne diverge pas en $0$.
L'intégrale vaut donc :
$$ \left[ \frac{x^{2k+a}}{2k+a} \right]_0^1 = \frac{1^{2k+a}}{2k+a} - 0 = \frac{1}{2k+a}. $$

5. **Conclusion :**
En remplaçant le terme intégral dans la somme de l'étape 3, on obtient bien l'identité demandée :
$$ \int_0^1 \frac{x^{a-1}}{1-x^2} dx = \sum_{k=0}^\infty \frac{1}{2k+a}. $$
Cette procédure est la fondation des techniques analytiques de Weierstrass et Euler pour la décomposition en produits infinis de la fonction Gamma.
