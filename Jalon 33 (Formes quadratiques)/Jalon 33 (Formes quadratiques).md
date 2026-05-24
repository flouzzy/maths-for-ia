---
uuid: "jalon-33"
title: "Formes quadratiques"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/optimisation
prev: "[[Jalon 32 (Preuve complète du théorème spectral pour les endomorphismes symétriques.).md]]"
next: "[[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]]"
---

# Jalon 33 : Formes quadratiques

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous marchez sur un terrain vallonné. À chaque endroit où vous posez le pied, le sol peut monter, descendre ou rester plat. Une **forme quadratique**, c'est comme une loupe mathématique qui regarde la courbure du sol juste sous votre pied. Elle nous dit si nous sommes au sommet d'une colline (tout redescend), au fond d'un vallon (tout remonte) ou sur un col de montagne (ça monte dans une direction et ça descend dans une autre, comme une selle de cheval).
- **Le "Pourquoi on a inventé ça" :** Les mathématiciens voulaient un outil simple pour mesurer des distances et des "énergies". Une forme linéaire (comme $f(x) = ax$) est trop simple : elle ne fait que des lignes droites. Pour capturer des courbes, des paraboles et des ellipses (qui sont partout en physique et en IA), il fallait passer au "degré 2". C'est l'étape charnière entre le monde plat (linéaire) et le monde courbe (analyse).
- **Visualisation :** Si vous lancez une bille dans un bol, le fond du bol est une forme quadratique "définie positive" (la bille revient toujours au centre). Si vous retournez le bol, c'est "définie négative". Une selle de cheval est "indéfinie".

## 2. Formalisation & Rigueur Académique

### A. Définitions Formelles

Soit $E$ un espace vectoriel de dimension finie $n$ sur le corps $\mathbb{K} = \mathbb{R}$.

> **Définition 1 (Forme Quadratique) :**
> On appelle **forme quadratique** sur $E$ toute application $q : E \to \mathbb{R}$ telle qu'il existe une forme bilinéaire symétrique $b : E \times E \to \mathbb{R}$ vérifiant :
> $$\forall x \in E, \quad q(x) = b(x, x)$$

> **Définition 2 (Forme Polaire) :**
> Pour toute forme quadratique $q$, il existe une unique forme bilinéaire symétrique $b$ associée, appelée **forme polaire** de $q$, définie par l'identité de polarisation :
> $$b(x, y) = \frac{1}{2} \left( q(x+y) - q(x) - q(y) \right)$$

> **Définition 3 (Matrice de q) :**
> Soit $\mathcal{B} = (e_1, \dots, e_n)$ une base de $E$. La matrice de $q$ dans $\mathcal{B}$ est la matrice symétrique $A \in \mathcal{M}_n(\mathbb{R})$ dont les coefficients sont $a_{ij} = b(e_i, e_j)$. On a alors :
> $$q(x) = X^T A X \quad \text{où } X \text{ est le vecteur colonne des coordonnées de } x.$$

### B. Théorèmes & Propriétés Fondamentales

> **Théorème de Réduction de Gauss :**
> Toute forme quadratique $q$ sur un espace de dimension $n$ peut s'écrire comme une combinaison linéaire de carrés de formes linéaires linéairement indépendantes :
> $$q(x) = \sum_{i=1}^r \lambda_i (\ell_i(x))^2$$
> où $r$ est le rang de $q$, $\lambda_i \in \mathbb{R}^*$, et $(\ell_1, \dots, \ell_r)$ est une famille libre de l'espace dual $E^*$.

> **Loi d'Inertie de Sylvester :**
> Dans toute décomposition de $q$ en somme de carrés de formes linéaires indépendantes, le nombre de coefficients strictement positifs (noté $n_+$) et le nombre de coefficients strictement négatifs (noté $n_-$) sont des invariants de $q$. Le couple $(n_+, n_-)$ est appelé la **signature** de $q$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème de Réduction de Gauss (Algorithme)

Nous procédons par récurrence sur la dimension $n$ de $E$.

1. **Initialisation / Cadre :**
   Soit $q(x) = \sum_{1 \le i \le j \le n} a_{ij} x_i x_j$ l'expression de $q$ dans une base donnée.

2. **Étape 1 : Cas où il existe un terme au carré ($a_{ii} \neq 0$) :**
   Supposons, sans perte de généralité, que $a_{11} \neq 0$. On regroupe tous les termes contenant $x_1$ :
   $$q(x) = a_{11} x_1^2 + x_1 \sum_{j=2}^n a_{1j} x_j + Q(x_2, \dots, x_n)$$
   On utilise la forme canonique $(A + B)^2 = A^2 + 2AB + B^2$, donc $A^2 + 2AB = (A+B)^2 - B^2$.
   Ici, $A^2 = a_{11} x_1^2$, donc $A = \sqrt{|a_{11}|} x_1$. Pour simplifier, posons $A^2 + 2AB = a_{11} (x_1^2 + \frac{1}{a_{11}} x_1 \sum a_{1j} x_j)$.
   $$q(x) = a_{11} \left[ x_1 + \frac{1}{2a_{11}} \sum_{j=2}^n a_{1j} x_j \right]^2 - \frac{1}{4a_{11}} \left( \sum_{j=2}^n a_{1j} x_j \right)^2 + Q(x_2, \dots, x_n)$$
   Le premier terme est de la forme $\lambda_1 \ell_1(x)^2$ avec $\ell_1(x) = x_1 + \dots$. Les termes restants ne dépendent plus de $x_1$. On réitère sur $n-1$.

3. **Étape 2 : Cas où tous les $a_{ii} = 0$ :**
   S'il existe un terme rectangle $a_{12} x_1 x_2 \neq 0$. On utilise l'identité $xy = \frac{1}{4} [ (x+y)^2 - (x-y)^2 ]$.
   On pose $x_1 = \frac{1}{2}(u+v)$ et $x_2 = \frac{1}{2}(u-v)$, ce qui fait apparaître des carrés $u^2$ et $v^2$. On revient au cas précédent.

4. **Conclusion :**
   Par itération, on obtient une somme de $r$ carrés.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Réduction d'une forme quadratique
**Énoncé :** Réduire par la méthode de Gauss la forme quadratique sur $\mathbb{R}^3$ :
$$q(x, y, z) = x^2 + y^2 + 2z^2 + 2xy + 4xz + 4yz$$

**Correction Détaillée :**
* *Analyse :* On voit un terme $x^2$, on va regrouper les termes en $x$.
* *Résolution :*
  1. Regroupement des $x$ : $q(x, y, z) = [x^2 + 2x(y + 2z)] + y^2 + 2z^2 + 4yz$.
  2. Complétion du carré : $x^2 + 2x(y + 2z) = (x + y + 2z)^2 - (y + 2z)^2$.
  3. Remplacement : $q(x, y, z) = (x + y + 2z)^2 - (y^2 + 4yz + 4z^2) + y^2 + 2z^2 + 4yz$.
  4. Simplification : $q(x, y, z) = (x + y + 2z)^2 - y^2 - 4yz - 4z^2 + y^2 + 2z^2 + 4yz$.
  5. Résultat final : $q(x, y, z) = (x + y + 2z)^2 - 2z^2$.
  La signature est $(1, 1)$, le rang est $2$. Elle est dégénérée.

### Exercice 2 : Niveau Avancé
**Énoncé :** Soit $A \in \mathcal{S}_n(\mathbb{R})$. Montrer que $A$ est définie positive si et seulement si tous ses mineurs principaux dominants sont strictement positifs (Critère de Sylvester).

**Correction Détaillée :**
* *Analyse :* On utilise la réduction de Gauss et l'interprétation matricielle.
* *Résolution :* La réduction de Gauss préserve le signe du déterminant des sous-matrices. Si on peut écrire $q(x) = \sum \alpha_i \ell_i(x)^2$, le $k$-ième mineur dominant est lié au produit $\alpha_1 \dots \alpha_k$. Pour que $q$ soit définie positive, il faut $\alpha_i > 0$ pour tout $i$, donc tous les produits (mineurs) doivent être $>0$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, les formes quadratiques sont au cœur de l'**optimisation de second ordre**. La fonction de perte $L(\theta)$ autour d'un minimum peut être approximée par son développement de Taylor :
  $$L(\theta) \approx L(\theta^*) + \frac{1}{2} (\theta - \theta^*)^T \mathbf{H} (\theta - \theta^*)$$
  où $\mathbf{H}$ est la matrice Hessienne. Cette approximation est une **forme quadratique**.
- **Exemple Concret :** Dans la **descente de gradient**, la vitesse de convergence est dictée par le "conditionnement" de cette forme quadratique (le rapport entre la plus grande et la plus petite valeur propre de la Hessienne). Si la forme quadratique est très allongée (comme une vallée étroite), le gradient oscille et l'apprentissage est lent. On utilise alors des méthodes comme **Adam** ou **RMSProp** pour normaliser ces courbures.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 25 (Formes bilinéaires).md]], [[Jalon 32 (Preuve complète du théorème spectral pour les endomorphismes symétriques.).md]]
- **Concepts Futurs dépendants :** [[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]], [[Jalon 121 (Ensembles convexes).md]]
