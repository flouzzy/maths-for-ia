---
title: "Exercice 3 : Série de fonctions et exponentielle"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 3 : Série de fonctions et exponentielle

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Problème

En développant la fonction $x \mapsto e^x$ en série entière, montrer rigoureusement que $\int_0^\infty e^{-2x} e^x dx$ peut être calculé terme à terme, et aboutir à une contradiction apparente justifiant l'importance du domaine de convergence.

## Démonstration et Résolution

### Étape 1 : Développement en série
Considérons la fonction $x \mapsto e^x$. Son développement en série entière sur $\mathbb{R}$ est donné par :
$$ e^x = \sum_{n=0}^\infty \frac{x^n}{n!} $$
Multiplions par la fonction positive $e^{-2x}$. Nous obtenons, pour tout $x \ge 0$ :
$$ e^{-2x} e^x = \sum_{n=0}^\infty e^{-2x} \frac{x^n}{n!} $$

### Étape 2 : Justification de l'interversion
Posons $u_n(x) = e^{-2x} \frac{x^n}{n!}$.
Pour tout $n \in \mathbb{N}$ et tout $x \in [0, +\infty)$, $u_n(x)$ est le produit de fonctions continues positives. Ainsi, $u_n$ est une fonction mesurable et positive sur $[0, +\infty)$.
D'après le corollaire du théorème de Beppo Levi pour la sommation des fonctions positives, nous pouvons intervertir la somme infinie et l'intégrale :
$$ \int_0^\infty \left( \sum_{n=0}^\infty e^{-2x} \frac{x^n}{n!} \right) dx = \sum_{n=0}^\infty \int_0^\infty e^{-2x} \frac{x^n}{n!} dx $$

### Étape 3 : Calcul explicite du terme général
Évaluons l'intégrale $I_n = \int_0^\infty e^{-2x} x^n dx$.
Effectuons un changement de variable affine $u = 2x$, d'où $du = 2 dx$ et $x = \frac{u}{2}$.
Les bornes restent $0$ et $+\infty$.
$$ I_n = \int_0^\infty e^{-u} \left(\frac{u}{2}\right)^n \frac{du}{2} = \frac{1}{2^{n+1}} \int_0^\infty u^n e^{-u} du $$
Reconnaissons ici l'intégrale eulérienne Gamma : $\int_0^\infty u^n e^{-u} du = \Gamma(n+1) = n!$.
Donc, $I_n = \frac{n!}{2^{n+1}}$.

### Étape 4 : Sommation et conclusion
Remplaçons $I_n$ dans la somme de notre équation initiale :
$$ \sum_{n=0}^\infty \frac{1}{n!} I_n = \sum_{n=0}^\infty \frac{1}{n!} \frac{n!}{2^{n+1}} = \sum_{n=0}^\infty \frac{1}{2^{n+1}} = \frac{1}{2} \sum_{n=0}^\infty \left(\frac{1}{2}\right)^n $$
Il s'agit d'une série géométrique de raison $q = 1/2$. Sa somme est :
$$ \frac{1}{2} \cdot \frac{1}{1 - 1/2} = \frac{1}{2} \cdot 2 = 1 $$
D'autre part, évaluons directement l'intégrale de gauche :
$$ \int_0^\infty e^{-2x} e^x dx = \int_0^\infty e^{-x} dx = \left[ -e^{-x} \right]_0^\infty = 1 $$
Les deux méthodes coïncident parfaitement. Beppo Levi garantit que le calcul terme à terme est formellement exact sans avoir recours aux rayons de convergence classiques.
