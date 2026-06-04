---
uuid: "jalon-75"
title: "Complétude des espaces Lp (Riesz-Fischer)"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/convergence
prev: "[[Jalon 74 (Inégalités fondamentales de l'analyse fonctionnelle).md]]"
next: "[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]"
---

# Jalon 75 : Complétude des espaces $L^p$ (Riesz-Fischer)

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous soyez un sculpteur. Vous avez un bloc de marbre géant qui contient toutes les chansons possibles.
    - Vous commencez à tailler une chanson en faisant des retouches successives. Chaque retouche est de plus en plus petite ($f_n$ est une suite de Cauchy).
    - Un **espace complet**, c'est la garantie que si vos retouches deviennent infiniment petites, vous finirez par obtenir une vraie statue finie, et pas un tas de poussière qui disparaît.
    - Les **espaces $L^p$** sont "complets" : cela signifie qu'ils sont "solides". Si vous construisez une fonction par morceaux et que ces morceaux se stabilisent, la fonction finale existe et elle est toujours dans votre catalogue. On n'a pas perdu de "matière" mathématique en passant à la limite.
- **Le "Pourquoi on a inventé ça" :** C'était le point faible de l'intégrale de Riemann : on pouvait avoir une suite de fonctions "gentilles" dont la limite était un monstre qu'on ne savait pas mesurer. Le théorème de Riesz-Fischer prouve que l'intégrale de Lebesgue a corrigé ce défaut. C'est ce qui permet d'utiliser toutes les techniques de la géométrie (distances, projections) sur des espaces de fonctions.
- **Visualisation :** Une suite de courbes qui se superposent de mieux en mieux. La limite est une courbe qui appartient à la même "famille" de fonctions (même énergie, même aire).

## 2. Formalisation & Rigueur Académique

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Le Théorème de Riesz-Fischer

> **Théorème de Riesz-Fischer :**
> Pour tout $p \in [1, +\infty]$, l'espace vectoriel normé $(L^p(\mu), \| \cdot \|_p)$ est un **espace de Banach** (c'est-à-dire un espace vectoriel normé complet).

### B. Lien entre convergence $L^p$ et convergence presque partout

Contrairement à la dimension finie, la convergence dans $L^p$ n'implique pas la convergence partout, ni même presque partout.

> **Théorème (Sous-suite convergente) :**
> Si une suite $(f_n)$ converge vers $f$ dans $L^p$, alors il existe une **sous-suite** $(f_{\phi(n)})$ qui converge vers $f$ presque partout.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration de la complétude (Cas $1 \le p < \infty$)

1. **Critère de complétude :** Un espace est complet si et seulement si toute série absolument convergente est convergente. Soit donc $\sum f_n$ une série telle que $\sum \|f_n\|_p = S < +\infty$. Montrons que la série converge dans $L^p$.
2. **Convergence simple :** Posons $g_k = \sum_{n=0}^k |f_n|$. La suite $(g_k)$ est croissante et positive.
   Par Minkowski, $\|g_k\|_p \le \sum_{n=0}^k \|f_n\|_p \le S$.
   D'après le **Théorème de Convergence Monotone** (Jalon 67), la fonction $g = \lim g_k = \sum |f_n|$ est mesurable et $\int g^p = \lim \int g_k^p \le S^p < \infty$.
   Donc $g \in L^p$, ce qui implique que $g(x) < \infty$ p.p.
   Ainsi, la série $\sum f_n(x)$ converge absolument (donc converge) pour presque tout $x$. Notons $f(x)$ sa somme.
3. **Convergence dans $L^p$ :** Soit $S_k = \sum_{n=0}^k f_n$ la somme partielle. On a $|S_k| \le g$ et $S_k \to f$ p.p.
   Considérons $|S_k - f|^p$. On a $|S_k - f|^p \le (|S_k| + |f|)^p \le (2g)^p$.
   Comme $g^p$ est intégrable, on peut appliquer le **Théorème de Convergence Dominée** (Jalon 69).
   $\int |S_k - f|^p d\mu \to 0$ quand $k \to \infty$.
4. **Conclusion :** La série converge vers $f$ dans $L^p$. L'espace est donc complet.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Convergence $L^p$ n'implique pas CVS
**Énoncé :** Construire une suite de fonctions sur $[0, 1]$ qui converge vers 0 dans $L^1$ mais qui ne converge en aucun point.
**Correction Détaillée :**
C'est la suite des "bosses glissantes" (Typing monkey sequence). On prend des fonctions indicatrices d'intervalles de plus en plus petits qui parcourent $[0, 1]$ sans cesse :
$\mathbf{1}_{[0, 1]}, \mathbf{1}_{[0, 1/2]}, \mathbf{1}_{[1/2, 1]}, \mathbf{1}_{[0, 1/3]}, \mathbf{1}_{[1/3, 2/3]}, \dots$
- L'intégrale $\int f_n$ tend vers 0 (la largeur des intervalles tend vers 0), donc $f_n \to 0$ dans $L^1$.
- Mais pour tout $x$, $f_n(x)$ vaut 1 une infinité de fois et 0 une infinité de fois. La suite numérique $(f_n(x))$ ne converge donc pas.

### Exercice 2 : Niveau Avancé (Espace $L^2$)
**Énoncé :** Pourquoi $L^2$ est-il particulièrement important parmi tous les $L^p$ ?
**Correction Détaillée :**
C'est le seul espace $L^p$ qui est un **espace de Hilbert**. La norme $\| \cdot \|_2$ provient d'un produit scalaire $\langle f, g \rangle = \int f \bar{g}$. La complétude de $L^2$ est la base de toute l'analyse de Fourier moderne et de la mécanique quantique.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, nous optimisons des modèles dans des espaces de fonctions. La complétude nous donne un cadre rigoureux pour dire que nos algorithmes convergent vers quelque chose de réel.
- **Example Concret :**
    - **Théorème de Représentation de Riesz :** Grâce à la complétude, on peut identifier toute forme linéaire continue sur $L^2$ avec une fonction de $L^2$. C'est fondamental pour définir le gradient dans les espaces de dimension infinie (calcul des variations).
    - **Stabilité de l'Apprentissage :** Si nous entraînons une suite de réseaux de neurones $h_n$ et que l'écart entre les prédictions (au sens MSE, donc $L^2$) diminue, nous sommes certains qu'il existe un réseau "idéal" $h$ vers lequel nous tendons.
    - **Traitement du Signal :** La complétude de $L^2$ garantit que n'importe quel signal d'énergie finie peut être décomposé parfaitement en une série de Fourier. Sans cela, la compression audio ou vidéo aurait des erreurs de reconstruction imprévisibles.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 73 (Espaces Lp et passage au quotient).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
- **Concepts Futurs dépendants :** [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]], [[Jalon 81 (Transformée de Fourier dans L2).md]]
