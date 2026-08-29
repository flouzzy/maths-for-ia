---
title: "Exercice 6 : Beppo Levi sur les séries doubles"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 6 : Beppo Levi sur les séries doubles

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Problème

Montrer en justifiant chaque passage que $\sum_{n=1}^\infty \sum_{m=1}^\infty \frac{1}{(n+m)^3} = \sum_{m=1}^\infty \sum_{n=1}^\infty \frac{1}{(n+m)^3}$.

## Démonstration et Résolution

### Étape 1 : Le formalisme de l'espace mesuré
Considérons l'espace mesurable $(\mathbb{N}^*, \mathcal{P}(\mathbb{N}^*))$, muni de la mesure de comptage $\nu$. Une somme infinie d'une suite $(u_k)_{k \ge 1}$ s'interprète rigoureusement comme l'intégrale de Lebesgue de la fonction $k \mapsto u_k$ par rapport à $\nu$ :
$$ \sum_{k=1}^\infty u_k = \int_{\mathbb{N}^*} u_k d\nu(k) $$

### Étape 2 : Fonction double et positivité
Définissons la fonction $f : \mathbb{N}^* \times \mathbb{N}^* \to \mathbb{R}$ par :
$$ f(n,m) = \frac{1}{(n+m)^3} $$
Pour tout couple $(n,m) \in (\mathbb{N}^*)^2$, le terme est strictement positif. La fonction $f$ est donc mesurable (toute fonction sur un espace discret est mesurable) et positive.

### Étape 3 : Application du Théorème de Fubini-Tonelli (Corollaire de Beppo Levi)
Le théorème de Fubini-Tonelli pour les espaces mesurés $\sigma$-finis (ce qui est le cas de la mesure de comptage) stipule que pour toute fonction mesurable positive sur l'espace produit $X \times Y$, l'ordre d'intégration peut être interverti. La démonstration fondamentale de Tonelli repose intimement sur le Théorème de Convergence Monotone appliqué aux sommes partielles.
Appliquons-le à notre fonction $f$ :
$$ \int_{\mathbb{N}^*} \left( \int_{\mathbb{N}^*} f(n,m) d\nu(n) \right) d\nu(m) = \int_{\mathbb{N}^*} \left( \int_{\mathbb{N}^*} f(n,m) d\nu(m) \right) d\nu(n) $$

### Étape 4 : Retour à la notation des séries
Remplaçons les intégrales par leurs sommes correspondantes. L'intégrale intérieure par rapport à $\nu(n)$ devient la somme sur $n$ :
$$ \int_{\mathbb{N}^*} f(n,m) d\nu(n) = \sum_{n=1}^\infty \frac{1}{(n+m)^3} $$
Ensuite, l'intégrale extérieure par rapport à $\nu(m)$ devient la somme sur $m$ :
$$ \sum_{m=1}^\infty \left( \sum_{n=1}^\infty \frac{1}{(n+m)^3} \right) = \sum_{n=1}^\infty \left( \sum_{m=1}^\infty \frac{1}{(n+m)^3} \right) $$
L'interversion est licite et inconditionnelle du moment que les termes sont positifs, même si la somme totale s'avérait infinie. (Dans ce cas précis, la somme double converge vers une constante finie proportionnelle à $\zeta(2)$).
