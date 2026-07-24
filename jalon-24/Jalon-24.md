---
uuid: "jalon-24"
title: "Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale et résolution d'un problème d'analyse de l'ENS sur les interversions de limites"
year: 1
trimester: 2
tags:
  - math/synthese
  - ia/regression-polynomiale
  - math/analyse-fonctionnelle
prev: "[[Jalon-23.md]]"
next: "[[Jalon 25 (Formes bilinéaires).md]]"
---
# 1. Intuition et genèse du concept

La quête de la prédiction parfaite a toujours été au cœur des mathématiques appliquées et de l'intelligence artificielle. Historiquement, le besoin d'ajuster des modèles continus à des observations discrètes et souvent bruitées a conduit Legendre et Gauss, indépendamment, à formuler la méthode des moindres carrés au début du XIXe siècle pour prédire les orbites cométaires. Mais au-delà de l'ajustement linéaire, la modélisation de phénomènes complexes nécessite une expressivité supérieure, souvent atteinte par la régression polynomiale.

Cependant, augmenter le degré d'un polynôme d'ajustement ne garantit nullement une meilleure généralisation. Au contraire, le mathématicien Carl Runge a démontré en 1901 un phénomène contre-intuitif et fondamental : pour certaines fonctions très régulières, l'interpolation polynomiale sur des nœuds équidistants diverge violemment aux bords de l'intervalle lorsque le degré augmente. Ce résultat théorique d'analyse met en lumière la dichotomie entre l'erreur empirique (sur les données d'apprentissage) et l'erreur de généralisation. L'analyse des critères de convergence d'une régression polynomiale exige ainsi une compréhension profonde des espaces de fonctions, de la géométrie euclidienne en dimension finie, et surtout des théorèmes d'interversion de limites, sujets classiques des concours de l'École Normale Supérieure. L'optimisation moderne s'appuie sur ces fondations pour régulariser les modèles et contraindre la complexité de l'espace d'hypothèses, illustrant l'élégance de l'analyse au service de l'apprentissage statistique.

# 2. Formalisation et structures algébriques

Soit $\mathcal{D} = \{(x_i, y_i)\}_{1 \le i \le n} \subset \mathbb{R} \times \mathbb{R}$ un ensemble d'apprentissage constitué de $n \in \mathbb{N}^*$ couples de points avec $x_i \neq x_j$ pour $i \neq j$. L'espace d'hypothèses est l'espace vectoriel des polynômes à coefficients réels de degré au plus $d \in \mathbb{N}$, noté $\mathcal{H} = \mathbb{R}_d[X]$.

**Définition (Matrice de conception de Vandermonde) :**
La matrice de conception $\mathbf{X} \in \mathcal{M}_{n, d+1}(\mathbb{R})$ est définie par ses coefficients $X_{i,j} = x_i^{j-1}$ pour $1 \le i \le n$ et $1 \le j \le d+1$. Le vecteur cible est $\mathbf{y} = (y_1, \dots, y_n)^\top \in \mathbb{R}^n$.

**Définition (Problème des moindres carrés polynomiaux) :**
Le vecteur des coefficients optimaux $\hat{\mathbf{a}} = (\hat{a}_0, \dots, \hat{a}_d)^\top \in \mathbb{R}^{d+1}$ est solution du problème d'optimisation convexe :
$$ \hat{\mathbf{a}} = \underset{\mathbf{a} \in \mathbb{R}^{d+1}}{\text{argmin}} \mathcal{L}(\mathbf{a}) \quad \text{où} \quad \mathcal{L}(\mathbf{a}) = \|\mathbf{X}\mathbf{a} - \mathbf{y}\|_2^2 $$
La fonction $\mathcal{L} : \mathbb{R}^{d+1} \to \mathbb{R}_+$ est de classe $\mathcal{C}^\infty$ et représente la somme des carrés des résidus. Le scalaire $\|\cdot\|_2$ désigne la norme euclidienne standard sur $\mathbb{R}^n$.

**Exemple :**
Pour un ajustement quadratique ($d=2$) avec $n=5$ observations $\mathcal{D} = \{(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)\}$, l'espace de recherche est paramétré par $\mathbf{a} = (a_0, a_1, a_2)^\top$. La matrice de Vandermonde associée est :
$$ \mathbf{X} = \begin{pmatrix} 1 & -2 & 4 \\ 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix} $$
Comme les $x_i$ sont distincts et $n > d$, le rang de $\mathbf{X}$ est maximal (égal à $d+1=3$).

**Cas pathologique (Sur-paramétrisation) :**
Si $d \ge n$, la matrice de Vandermonde devient rectangulaire (ou carrée si $d = n-1$) et le système $\mathbf{X}\mathbf{a} = \mathbf{y}$ possède au moins une solution exacte. Dans ce cas, $\mathcal{L}(\hat{\mathbf{a}}) = 0$. Cependant, $\mathbf{X}^\top\mathbf{X}$ n'est plus inversible si $d \ge n$, et le minimum n'est plus unique, entraînant une variance infinie des estimateurs hors de l'échantillon.

# 3. Démonstrations pas-à-pas

**Théorème (Équations normales et unicité) :**
Si les points d'apprentissage $(x_i)_{1 \le i \le n}$ sont deux à deux distincts et $n > d$, alors le problème d'optimisation admet une unique solution globale donnée analytiquement par :
$$ \hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y} $$

**Démonstration :**
La fonction $\mathcal{L}(\mathbf{a}) = \|\mathbf{X}\mathbf{a} - \mathbf{y}\|_2^2 = (\mathbf{X}\mathbf{a} - \mathbf{y})^\top(\mathbf{X}\mathbf{a} - \mathbf{y})$ est développable par bilinéarité du produit scalaire euclidien.
$$ \mathcal{L}(\mathbf{a}) = \mathbf{a}^\top\mathbf{X}^\top\mathbf{X}\mathbf{a} - \mathbf{y}^\top\mathbf{X}\mathbf{a} - \mathbf{a}^\top\mathbf{X}^\top\mathbf{y} + \mathbf{y}^\top\mathbf{y} $$
Puisque le produit matriciel $\mathbf{a}^\top\mathbf{X}^\top\mathbf{y}$ est un scalaire de dimension $1 \times 1$, il est égal à sa propre transposée, soit $\mathbf{y}^\top\mathbf{X}\mathbf{a}$. L'expression se simplifie en :
$$ \mathcal{L}(\mathbf{a}) = \mathbf{a}^\top(\mathbf{X}^\top\mathbf{X})\mathbf{a} - 2\mathbf{a}^\top\mathbf{X}^\top\mathbf{y} + \mathbf{y}^\top\mathbf{y} $$
Cette fonction est une forme quadratique affine en $\mathbf{a}$. Nous calculons son gradient par rapport au vecteur $\mathbf{a}$ en utilisant les règles de dérivation matricielle. Pour une matrice symétrique $\mathbf{M} = \mathbf{X}^\top\mathbf{X}$, $\nabla_{\mathbf{a}} (\mathbf{a}^\top\mathbf{M}\mathbf{a}) = 2\mathbf{M}\mathbf{a}$. Pour un vecteur constant $\mathbf{c} = \mathbf{X}^\top\mathbf{y}$, $\nabla_{\mathbf{a}} (\mathbf{a}^\top\mathbf{c}) = \mathbf{c}$.
$$ \nabla \mathcal{L}(\mathbf{a}) = 2\mathbf{X}^\top\mathbf{X}\mathbf{a} - 2\mathbf{X}^\top\mathbf{y} $$
Une condition nécessaire d'optimalité de premier ordre est l'annulation du gradient, ce qui fournit les équations normales :
$$ \mathbf{X}^\top\mathbf{X}\mathbf{a} = \mathbf{X}^\top\mathbf{y} $$
Pour établir l'unicité de la solution, il est impératif de prouver que la matrice carrée $\mathbf{X}^\top\mathbf{X} \in \mathcal{M}_{d+1}(\mathbb{R})$ est inversible. Étudions son noyau.
Soit $\mathbf{u} \in \mathbb{R}^{d+1}$ tel que $\mathbf{X}^\top\mathbf{X}\mathbf{u} = \mathbf{0}_{d+1}$.
Multiplions à gauche par $\mathbf{u}^\top$ :
$$ \mathbf{u}^\top\mathbf{X}^\top\mathbf{X}\mathbf{u} = 0 \iff (\mathbf{X}\mathbf{u})^\top(\mathbf{X}\mathbf{u}) = 0 \iff \|\mathbf{X}\mathbf{u}\|_2^2 = 0 \iff \mathbf{X}\mathbf{u} = \mathbf{0}_n $$
L'équation vectorielle $\mathbf{X}\mathbf{u} = \mathbf{0}_n$ se traduit par le système suivant de $n$ équations :
$$ \forall i \in \llbracket 1, n \rrbracket, \quad \sum_{j=0}^{d} u_j x_i^j = 0 $$
Considérons le polynôme $Q \in \mathbb{R}_d[X]$ défini par $Q(X) = \sum_{j=0}^{d} u_j X^j$. Le système précédent signifie exactement que les $n$ abscisses $x_i$ sont des racines de $Q$.
Cependant, $Q$ est un polynôme de degré inférieur ou égal à $d$. Comme les $x_i$ sont distincts par hypothèse, $Q$ admet $n$ racines distinctes. Or, $n > d$. Par le théorème fondamental de l'algèbre (et ses conséquences sur $\mathbb{R}$), le seul polynôme de degré $\le d$ possédant strictement plus de $d$ racines est le polynôme identiquement nul.
Par conséquent, tous les coefficients de $Q$ sont nuls, ce qui implique $\mathbf{u} = \mathbf{0}_{d+1}$.
Le noyau de $\mathbf{X}^\top\mathbf{X}$ est réduit au vecteur nul. La matrice est donc injective, et puisqu'elle est carrée de dimension finie, elle est inversible.
En multipliant l'équation normale à gauche par l'inverse $(\mathbf{X}^\top\mathbf{X})^{-1}$, nous obtenons l'expression analytique unique :
$$ \hat{\mathbf{a}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y} $$
De plus, la Hessienne $\nabla^2 \mathcal{L}(\mathbf{a}) = 2\mathbf{X}^\top\mathbf{X}$ étant définie positive, la fonction objectif est strictement convexe, garantissant que ce point critique est l'unique minimum global. $\blacksquare$
