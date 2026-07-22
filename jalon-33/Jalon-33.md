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

## 1. L'Échafaudage Cognitif & Traçabilité Historique

Les formes quadratiques constituent le prolongement naturel et non linéaire de l'algèbre linéaire classique. Historiquement, leur émergence est intrinsèquement liée aux tentatives de généralisation du théorème de Pythagore et à l'étude des coniques par les géomètres de l'Antiquité (Apollonius de Perge), bien avant que le formalisme algébrique moderne ne soit forgé par des figures telles que Carl Friedrich Gauss et James Joseph Sylvester au XIXe siècle.

Le passage de l'étude des applications linéaires (degré 1) à celle des formes quadratiques (degré 2) répond à une nécessité impérieuse : modéliser l'énergie, la courbure, et la distance. En physique, l'énergie cinétique est une forme quadratique de la vitesse. En géométrie riemannienne, le tenseur métrique local définit une forme quadratique mesurant la longueur infinitésimale. En intelligence artificielle et en optimisation convexe, la matrice hessienne (dérivée seconde) définit localement une forme quadratique qui dicte la géométrie de l'espace des paramètres, déterminant la vitesse et la stabilité des algorithmes d'apprentissage profond tels que la descente de gradient, Newton-Raphson ou L-BFGS.

Le saut conceptuel majeur réside dans la non-linéarité : alors qu'une forme linéaire est trivialement caractérisée par ses valeurs sur une base, une forme quadratique encapsule des interactions croisées entre les différentes dimensions (les termes "rectangles" ou "croisés"). L'effort mathématique, magistralement orchestré par la réduction de Gauss, consiste à décortiquer ce tissu complexe d'interactions pour révéler une structure fondamentalement diagonale et découplée, ramenant l'étude de tout espace courbé à une simple somme algébrique de dimensions indépendantes.

## 2. Le Protocole d'Exégèse Conceptuelle

### 2.1. Définition et Forme Polaire

**A. Énoncé Symbolique Strict**

Soit $E$ un espace vectoriel sur un corps $\mathbb{K}$ de caractéristique différente de 2 (en pratique, $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$).
Une application $q : E \to \mathbb{K}$ est une **forme quadratique** s'il existe une forme bilinéaire symétrique $b : E \times E \to \mathbb{K}$ telle que :
$$ \forall x \in E, \quad q(x) = b(x, x) $$

L'application $b$ est unique et est appelée la **forme polaire** de $q$. Elle est explicitement donnée par la formule de polarisation :
$$ \forall (x, y) \in E^2, \quad b(x, y) = \frac{1}{2} \left( q(x + y) - q(x) - q(y) \right) $$

**B. Anatomie et Typage Chirurgical**

- **$E$** : Un espace vectoriel, qui sert de substrat géométrique. Les éléments $x, y$ sont des vecteurs de $E$.
- **$\mathbb{K}$** : Le corps de base. La restriction de caractéristique différente de 2 est cruciale car la formule de polarisation divise par $2$. Si la caractéristique était 2 (ex: $\mathbb{Z}/2\mathbb{Z}$), $1+1=0$, et l'inverse de 2 n'existerait pas.
- **$q$** : L'application qui à un vecteur associe un scalaire de $\mathbb{K}$. Elle n'est pas linéaire ($q(\lambda x) = \lambda^2 q(x)$).
- **$b$** : Une forme bilinéaire symétrique ($b(x, y) = b(y, x)$). L'unicité de $b$ découle directement de la symétrie.

**C. Exemples de Validation**

- *Exemple Trivial* : Sur $E = \mathbb{R}^n$, l'application $q(x) = x_1^2 + x_2^2 + \dots + x_n^2$ est la forme quadratique standard (norme euclidienne au carré). Sa forme polaire est le produit scalaire standard $b(x, y) = x_1 y_1 + \dots + x_n y_n$.
- *Exemple Complexe* : Sur $E = \mathcal{M}_n(\mathbb{R})$ (l'espace des matrices carrées), l'application $q(M) = \mathrm{Tr}(M^T M)$ est une forme quadratique (norme de Frobenius au carré). Sa forme polaire est $b(M, N) = \mathrm{Tr}(M^T N)$.

**D. Cas Pathologiques et Contre-exemples**

- L'application valeur absolue sur $\mathbb{R}$, $f(x) = |x|$, n'est pas une forme quadratique. En effet, $f(\lambda x) = |\lambda| f(x)$, et non $\lambda^2 f(x)$.
- Si l'on prend $\mathbb{K} = \mathbb{F}_2$ (le corps à deux éléments), la notion usuelle de polarisation s'effondre, car la division par 2 (qui est congru à 0 modulo 2) est indéfinie, ce qui dissocie la théorie des formes quadratiques de celle des formes bilinéaires symétriques en caractéristique 2.

### 2.2. Réduction de Gauss

**A. Énoncé Symbolique Strict**

Pour toute forme quadratique $q$ sur un $\mathbb{K}$-espace vectoriel $E$ de dimension finie $n$, il existe une base $(e_1, \dots, e_n)$ de $E$ et des scalaires $(\lambda_1, \dots, \lambda_n) \in \mathbb{K}^n$ tels que pour tout $x = \sum_{i=1}^n x_i e_i \in E$ :
$$ q(x) = \sum_{i=1}^n \lambda_i (\ell_i(x))^2 $$
où les $(\ell_1, \dots, \ell_n)$ constituent la base duale associée de $E^*$. En d'autres termes, toute forme quadratique peut s'écrire comme une combinaison linéaire de carrés de formes linéaires indépendantes.

**B. Anatomie et Typage Chirurgical**

- **$n$** : La dimension de l'espace vectoriel $E$. L'algorithme de réduction s'applique en dimension finie.
- **$\lambda_i$** : Des scalaires dans $\mathbb{K}$. Le nombre de $\lambda_i$ non nuls est exactement le **rang** de la forme quadratique $q$.
- **$\ell_i$** : Des formes linéaires (éléments du dual $E^*$). L'indépendance linéaire de ces formes est la garantie que le système de coordonnées peut être inversé pour former une véritable base de $E$.

**C. Exemples de Validation**

- *Exemple Trivial* : $q(x_1, x_2) = x_1^2 + 2x_1 x_2 + x_2^2$. Par identité remarquable, $q(x_1, x_2) = (x_1 + x_2)^2$. Ici $\lambda_1 = 1, \ell_1(x) = x_1 + x_2$, et la forme est de rang 1.
- *Exemple Complexe* : $q(x_1, x_2, x_3) = x_1 x_2 + x_2 x_3 + x_3 x_1$. Il n'y a pas de terme au carré. On pose le changement de variables (polarisation) $x_1 = u+v, x_2 = u-v$, d'où $x_1 x_2 = u^2 - v^2$, pour relancer l'algorithme.

**D. Cas Pathologiques et Contre-exemples**

- Si on se restreint à imposer que les $\ell_i$ soient de simples projections canoniques partielles (sans changement de base), la décomposition échoue face aux termes croisés (rectangles). L'indépendance linéaire stricte de la famille $(\ell_1, \dots, \ell_r)$ est la clé, sinon une décomposition comme $(x_1)^2 + (x_2)^2 - (x_1+x_2)^2$ n'est pas une réduction de Gauss valide car les arguments des carrés sont liés.

### 2.3. Loi d'Inertie de Sylvester

**A. Énoncé Symbolique Strict**

Sur un $\mathbb{R}$-espace vectoriel de dimension finie, le nombre de coefficients strictement positifs (noté $s$) et le nombre de coefficients strictement négatifs (noté $t$) dans une décomposition en carrés de Gauss de $q$ sont invariants et indépendants du choix de la base de réduction. Le couple $(s, t)$ est appelé la **signature** de $q$.

**B. Anatomie et Typage Chirurgical**

- **$\mathbb{R}$-espace vectoriel** : Ce théorème fondamental requiert le corps des réels (ou un corps ordonné). Sur $\mathbb{C}$, il n'y a pas de loi d'inertie (la signature perd son sens) car tout nombre complexe a une racine carrée, transformant tout carré négatif en carré positif via la multiplication par $i$.
- **$s, t \in \mathbb{N}$** : Entiers naturels. La somme $s + t = \mathrm{rg}(q)$ (le rang). Si $s = n$ et $t = 0$, $q$ est **définie positive**. Si $s+t < n$, $q$ est **dégénérée**.

**C. Exemples de Validation**

- *Exemple Trivial* : La métrique de Minkowski en relativité restreinte, définie sur $\mathbb{R}^4$ par $q(t, x, y, z) = c^2 t^2 - x^2 - y^2 - z^2$. Sa signature est invariante $(1, 3)$ ou $(3, 1)$ selon la convention, peu importe le repère inertiel choisi (transformations de Lorentz).

**D. Cas Pathologiques et Contre-exemples**

- Comme souligné, sur $\mathbb{C}$, la forme $q(x, y) = x^2 - y^2$ peut s'écrire $q(x, y) = x^2 + (iy)^2$. La notion de "signe" des coefficients s'effondre.

## 3. Zéro Ellipse dans les Démonstrations à Blanc

### Démonstration de la Formule de Polarisation (Unicité de la Forme Polaire)

**Objectif** : Prouver que si $q(x) = b(x, x)$ avec $b$ bilinéaire symétrique, alors $b$ est uniquement déterminée.

**Preuve pas à pas** :
1. Soient $x, y \in E$. Évaluons la forme quadratique sur la somme vectorielle $(x+y)$ :
   $$ q(x+y) = b(x+y, x+y) $$
2. En utilisant la bilinéarité de $b$ (linéarité à gauche et à droite), nous développons l'expression :
   $$ b(x+y, x+y) = b(x, x+y) + b(y, x+y) $$
   $$ b(x+y, x+y) = b(x, x) + b(x, y) + b(y, x) + b(y, y) $$
3. Par définition, nous savons que $q(x) = b(x, x)$ et $q(y) = b(y, y)$. Substituons ces valeurs :
   $$ q(x+y) = q(x) + b(x, y) + b(y, x) + q(y) $$
4. En invoquant la symétrie de la forme polaire $b$, nous avons $b(y, x) = b(x, y)$. En remplaçant :
   $$ q(x+y) = q(x) + 2b(x, y) + q(y) $$
5. Isolons le terme $2b(x, y)$ en soustrayant $q(x)$ et $q(y)$ des deux côtés :
   $$ 2b(x, y) = q(x+y) - q(x) - q(y) $$
6. En divisant par 2 (ce qui est mathématiquement licite puisque la caractéristique du corps $\mathbb{K}$ est supposée différente de 2) :
   $$ b(x, y) = \frac{1}{2} \left( q(x+y) - q(x) - q(y) \right) $$
7. **Conclusion** : La forme bilinéaire symétrique $b$ s'exprime de manière unique et explicite uniquement en termes des évaluations de l'application $q$. Cela garantit l'existence d'au plus une forme polaire, donc son unicité intrinsèque. $\blacksquare$

### Démonstration de la Loi d'Inertie de Sylvester

**Objectif** : Montrer que si une forme quadratique $q$ se décompose dans deux bases de réduction différentes, le nombre de carrés positifs $s$ est un invariant.

**Preuve pas à pas** :
1. Supposons deux décompositions de Gauss pour la même forme quadratique $q$ sur un $\mathbb{R}$-espace vectoriel $E$ de dimension $n$ :
   $$ q(x) = \sum_{i=1}^{s} (\ell_i(x))^2 - \sum_{j=1}^{t} (m_j(x))^2 $$
   $$ q(x) = \sum_{i=1}^{s'} (\ell'_i(x))^2 - \sum_{j=1}^{t'} (m'_j(x))^2 $$
   Où $(\ell_1, \dots, \ell_s, m_1, \dots, m_t)$ constituent une famille libre de $E^*$ (que l'on complète en base), et de même pour l'autre système avec des "primes". (Les constantes multiplicatives ont été absorbées dans les carrés, ex: $\lambda \ell^2 = (\sqrt{\lambda}\ell)^2$ pour $\lambda > 0$).
2. Définissons deux sous-espaces vectoriels fondamentaux de $E$ basés sur la dualité (noyaux des formes linéaires) :
   $$ F = \bigcap_{j=1}^{t} \ker(m_j) $$
   $$ G = \bigcap_{i=1}^{s'} \ker(\ell'_i) $$
3. Calculons les dimensions de $F$ et $G$ grâce au théorème du rang et aux familles libres. L'intersection de noyaux de formes linéaires indépendantes fait chuter la dimension d'exactement $1$ par forme linéaire :
   $$ \dim(F) = n - t $$
   $$ \dim(G) = n - s' $$
4. Raisonnons par l'absurde. Supposons que $s > s'$. Dans l'équation des dimensions, comme le rang $r$ de $q$ est un invariant de la matrice (rang algébrique), on sait que $r = s+t = s'+t'$.
   Si $s > s'$, alors $t = r - s < r - s' = t'$, donc $t < t'$.
5. Observons l'intersection $F \cap G$. Par la formule de Grassmann vectorielle :
   $$ \dim(F \cap G) + \dim(F + G) = \dim(F) + \dim(G) $$
   Puisque $\dim(F + G) \le n$, nous avons :
   $$ \dim(F \cap G) \ge \dim(F) + \dim(G) - n = (n - t) + (n - s') - n = n - t - s' $$
6. Reprenons l'inégalité supposée : $s > s'$, c'est-à-dire $s - s' \ge 1$.
   Ajoutons $-t$ des deux côtés : $s - t - s' \ge 1 - t$. Mais nous savons que $s + t \le n$, donc $n - t \ge s$.
   L'équation $n - t - s'$ devient strictement positive car $n - t \ge s > s'$. Donc $\dim(F \cap G) > 0$.
7. Puisque la dimension est strictement positive, l'intersection n'est pas réduite au vecteur nul. Il existe un vecteur $x \in F \cap G$ avec $x \neq 0_E$.
8. Évaluons $q(x)$ en utilisant les deux décompositions :
   - Puisque $x \in F$, $x$ annule toutes les formes $m_j$. Donc la première décomposition donne :
     $$ q(x) = \sum_{i=1}^{s} (\ell_i(x))^2 \ge 0 $$
   - Puisque $x \in G$, $x$ annule toutes les formes $\ell'_i$. Donc la seconde décomposition donne :
     $$ q(x) = - \sum_{j=1}^{t'} (m'_j(x))^2 \le 0 $$
9. Par conséquent, $q(x) = 0$. Mais $q(x) = \sum_{i=1}^{s} (\ell_i(x))^2 = 0$. Une somme de carrés réels étant nulle si et seulement si chaque carré est nul, on en déduit que $\ell_i(x) = 0$ pour tout $i=1 \dots s$.
10. Or, $x$ annule déjà tous les $m_j$ par construction ($x \in F$). Ainsi, $x$ annule toute la famille libre $(\ell_1, \dots, \ell_s, m_1, \dots, m_t)$. Cette famille contenant toutes les formes non nulles de la base duale réduisant $q$, complétée par d'éventuelles formes du noyau géométrique.
11. Plus formellement, $x$ est orthogonal à tous les covecteurs définissant la topologie de $E$ relative à $q$. Mais si la base de formes linéaires est complète, $x$ doit être le vecteur nul, $x = 0_E$.
12. C'est une contradiction directe avec le fait (démontré à l'étape 7) qu'il existe un $x \neq 0_E$.
13. Notre supposition initiale par l'absurde, $s > s'$, est donc fausse.
14. Par un raisonnement symétrique parfait, nous pouvons inverser les rôles et montrer que la supposition $s' > s$ mène également à une contradiction.
15. Conclusion finale inéluctable : $s = s'$.
16. Puisque le rang est invariant matriciel ($s+t = s'+t'$), on déduit immédiatement que $t = t'$.
17. Le couple d'invariants $(s, t)$ ne dépend donc pas du choix de la base et définit intrinsèquement la signature de la forme quadratique. $\blacksquare$
