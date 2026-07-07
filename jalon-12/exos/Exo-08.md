# Exercice 08 (4 $\star$) : Optimisation de la Similarité Cosinus Quadratique et Géométrie des Espaces de Plongement

## Énoncé
Soit $(E, \langle \cdot, \cdot \rangle)$ un espace vectoriel euclidien réel de dimension finie $m \ge 1$. On note $\|\cdot\|$ la norme associée à l'espace euclidien.
Soit $S = \{v_1, v_2, \dots, v_N\}$ un ensemble fini de $N$ vecteurs non nuls de $E$, où $N \ge 1$. Ces vecteurs peuvent être interprétés comme des plongements (embeddings) sémantiques de documents ou de concepts.
Nous cherchons à trouver un vecteur unitaire $x \in E$ (c'est-à-dire $\|x\|=1$) qui maximise la somme des carrés des similarités cosinus avec les vecteurs de l'ensemble $S$.
La fonction objectif est définie par :
$$ f(x) = \sum_{i=1}^N \left(\frac{\langle x, v_i \rangle}{\|x\| \|v_i\|}\right)^2 $$

1.  Montrer que le problème de maximisation de $f(x)$ sous la contrainte $\|x\|=1$ est équivalent à la maximisation d'une forme quadratique $x^T M x$ pour une certaine matrice symétrique $M$. Définir explicitement la matrice $M$ et justifier ses propriétés (symétrie, semi-définie positive).
2.  Caractériser le(s) vecteur(s) $x$ qui maximise(nt) $f(x)$ et déterminer la valeur maximale de $f(x)$.
3.  Interpréter la matrice $M$ et le(s) vecteur(s) $x$ maximisant $f(x)$ en termes de géométrie de l'espace de plongement et du concept de "direction sémantique principale".
4.  Soit $E^*$ le dual de l'espace $E$. Pour chaque $v_i \in E$, on définit le fonctionnel linéaire $\phi_i \in E^*$ par $\phi_i(y) = \langle v_i, y \rangle$ pour tout $y \in E$. Reformuler le problème de maximisation en termes de fonctionnels linéaires. Établir la connexion entre la matrice $M$ et la matrice de Gram des fonctionnels $\psi_i = \mathcal{R}(u_i)$ où $u_i = v_i/\|v_i\|$ et $\mathcal{R}: E \to E^*$ est l'isomorphisme de Riesz.


### Isométries et Conservation des Angles
Les opérateurs orthogonaux $Q \in O(d)$ préservent le produit scalaire par définition : $\langle Qu, Qv \rangle = \langle u, v \rangle$. De ce fait, ils préservent également les normes : $\|Qu\| = \|u\|$. Conséquemment, la similarité cosinus est un invariant absolu sous l'action du groupe orthogonal $O(d)$. Une rotation globale de l'espace de plongement ne modifie pas les relations sémantiques.

## Correction Détaillée
### Analyse et Stratégie
Le problème nous demande de maximiser une fonction $f(x)$ qui est une somme de carrés de similarités cosinus, sous la contrainte que $x$ est un vecteur unitaire. La première étape consistera à simplifier l'expression de $f(x)$ en utilisant la contrainte $\|x\|=1$ et en normalisant les vecteurs $v_i$. Nous montrerons ensuite que cette expression se ramène à une forme quadratique $x^T M x$, où $M$ est une matrice symétrique. La maximisation d'une forme quadratique sous contrainte unitaire est un problème classique de l'algèbre linéaire, résolu par la théorie spectrale des matrices symétriques (valeurs propres et vecteurs propres).

Pour l'interprétation géométrique, nous analyserons la structure de $M$ et la signification des vecteurs propres principaux. Enfin, pour la partie sur la dualité, nous utiliserons l'isomorphisme de Riesz pour relier les vecteurs de $E$ à leurs fonctionnels linéaires correspondants dans $E^*$. Nous reformulerons l'objectif en termes de ces fonctionnels et établirons un lien avec la matrice de Gram, en exploitant la relation entre les matrices $A^T A$ et $A A^T$.

### Résolution Pas-à-Pas

#### 1. Transformation en forme quadratique
Soit $f(x) = \sum_{i=1}^N \left(\frac{\langle x, v_i \rangle}{\|x\| \|v_i\|}\right)^2$.
Puisque nous cherchons à maximiser $f(x)$ sous la contrainte $\|x\|=1$, l'expression de $f(x)$ se simplifie en :
$$ f(x) = \sum_{i=1}^N \frac{\langle x, v_i \rangle^2}{\|v_i\|^2} $$
Les vecteurs $v_i$ sont non nuls par hypothèse, donc $\|v_i\| \neq 0$.
Définissons les vecteurs normalisés $u_i = \frac{v_i}{\|v_i\|}$ pour $i=1, \dots, N$. Ces vecteurs $u_i$ sont unitaires, c'est-à-dire $\|u_i\|=1$.
L'expression de $f(x)$ devient alors :
$$ f(x) = \sum_{i=1}^N \langle x, u_i \rangle^2 $$
Soit $\{e_1, \dots, e_m\}$ une base orthonormée de $E$. Tout vecteur $x \in E$ peut être représenté par ses coordonnées $x = \sum_{j=1}^m x_j e_j$, et de même pour $u_i = \sum_{j=1}^m (u_i)_j e_j$.
Dans cette base, le produit scalaire $\langle x, u_i \rangle$ s'écrit comme le produit matriciel $x^T u_i$, où $x$ et $u_i$ sont des vecteurs colonnes de leurs coordonnées.
Alors $\langle x, u_i \rangle^2 = (x^T u_i)^2 = (x^T u_i)(u_i^T x)$.
En substituant cela dans l'expression de $f(x)$ :
$$ f(x) = \sum_{i=1}^N (x^T u_i)(u_i^T x) $$
Par la linéarité de la somme et la distributivité du produit matriciel, nous pouvons réécrire ceci comme :
$$ f(x) = x^T \left(\sum_{i=1}^N u_i u_i^T\right) x $$
Nous définissons la matrice $M$ comme :
$$ M = \sum_{i=1}^N u_i u_i^T $$
Chaque terme $u_i u_i^T$ est une matrice de taille $m \times m$.
La matrice $u_i u_i^T$ est symétrique, car $(u_i u_i^T)^T = (u_i^T)^T u_i^T = u_i u_i^T$.
Puisque $M$ est une somme de matrices symétriques, $M$ est elle-même une matrice symétrique.
De plus, pour tout vecteur $y \in E$, la forme quadratique associée à $M$ est :
$$ y^T M y = y^T \left(\sum_{i=1}^N u_i u_i^T\right) y = \sum_{i=1}^N y^T u_i u_i^T y = \sum_{i=1}^N (y^T u_i)(u_i^T y) = \sum_{i=1}^N \langle y, u_i \rangle^2 $$
Puisque $\langle y, u_i \rangle^2 \ge 0$ pour tout $i$, la somme $\sum_{i=1}^N \langle y, u_i \rangle^2$ est toujours supérieure ou égale à zéro.
Donc, $y^T M y \ge 0$ pour tout $y \in E$. Cela signifie que $M$ est une matrice semi-définie positive.

Le problème de maximisation de $f(x)$ sous la contrainte $\|x\|=1$ est donc équivalent à la maximisation de la forme quadratique $x^T M x$ sous la contrainte $\|x\|^2 = x^T x = 1$.

#### 2. Caractérisation du(des) vecteur(s) maximisant(s) et valeur maximale
Le problème de la maximisation d'une forme quadratique $x^T M x$ sous la contrainte $\|x\|^2=1$ pour une matrice symétrique $M$ est un résultat fondamental de la théorie spectrale.
Soient $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_m$ les valeurs propres de $M$, ordonnées par ordre décroissant.
Le théorème spectral pour les matrices symétriques garantit que toutes les valeurs propres sont réelles et qu'il existe une base orthonormée de $E$ composée de vecteurs propres de $M$.
Pour tout vecteur $x$ unitaire, la valeur de $x^T M x$ est bornée par la plus grande et la plus petite valeur propre de $M$. Plus précisément :
$$ \lambda_m \le x^T M x \le \lambda_1 $$
La valeur maximale de $x^T M x$ est $\lambda_1$, la plus grande valeur propre de $M$.
Le(s) vecteur(s) $x$ qui atteigne(nt) ce maximum sont les vecteurs propres unitaires associés à cette plus grande valeur propre $\lambda_1$.
Si $\lambda_1$ est une valeur propre simple, alors il y a deux vecteurs unitaires qui maximisent $f(x)$, à savoir $e_1$ et $-e_1$, où $e_1$ est le vecteur propre unitaire associé à $\lambda_1$.
Si $\lambda_1$ est une valeur propre de multiplicité $k > 1$, alors tout vecteur unitaire appartenant au sous-espace propre $E_{\lambda_1}$ (de dimension $k$) maximise $f(x)$.

En résumé :
*   La valeur maximale de $f(x)$ est $\lambda_{\max}(M)$, la plus grande valeur propre de $M$.
*   Le(s) vecteur(s) $x$ qui maximise(nt) $f(x)$ sont les vecteurs propres unitaires de $M$ associés à $\lambda_{\max}(M)$.

#### 3. Interprétation géométrique
*   **Interprétation de la matrice $M$**:
    La matrice $M = \sum_{i=1}^N u_i u_i^T$ est une somme de matrices de projection orthogonale. Chaque terme $u_i u_i^T$ est la matrice de projection orthogonale sur la droite vectorielle engendrée par le vecteur unitaire $u_i$.
    $M$ peut être vue comme une matrice qui agrège les directions des vecteurs normalisés $u_i$. Elle capture la "variance" ou la "dispersion" des directions des documents dans l'espace de plongement. Si les vecteurs $u_i$ sont fortement alignés dans une certaine direction, $M$ aura une grande valeur propre dans cette direction.
    Si l'on considère la matrice $A$ de taille $N \times m$ dont la $i$-ème ligne est le vecteur $u_i^T$ (transposé du vecteur colonne $u_i$), alors $M = A^T A$. Cette construction est similaire à celle de la matrice de covariance dans l'Analyse en Composantes Principales (PCA), mais appliquée aux directions des vecteurs plutôt qu'à leurs positions absolues (et sans centrage).

*   **Interprétation du(des) vecteur(s) $x$ maximisant(s)**:
    Le(s) vecteur(s) $x$ qui maximise(nt) $f(x)$ sont les vecteurs propres unitaires associés à la plus grande valeur propre de $M$. Cette direction $x$ est celle le long de laquelle la somme des carrés des projections des vecteurs $u_i$ est maximale.
    En d'autres termes, $x$ représente la "direction principale" ou la "direction sémantique dominante" de l'ensemble des documents $S$. C'est la direction dans l'espace de plongement qui est la plus fortement alignée avec l'ensemble des documents normalisés.
    Dans le contexte d'un moteur de recherche sémantique, ce vecteur $x$ pourrait être utilisé comme un "représentant" ou un "prototype" sémantique pour le groupe de documents $S$. Un nouveau document ou une nouvelle requête pourrait être comparé à $x$ pour évaluer sa similarité globale avec l'ensemble $S$.

#### 4. Dualité et connexion avec la matrice de Gram
Soit $E^*$ le dual de $E$. Puisque $E$ est un espace euclidien de dimension finie, il existe un isomorphisme canonique entre $E$ et $E^*$, connu sous le nom d'isomorphisme de Riesz.
L'isomorphisme de Riesz $\mathcal{R}: E \to E^*$ est défini par $\mathcal{R}(v)(y) = \langle v, y \rangle$ pour tout $v, y \in E$.
Pour chaque $v_i \in E$, le fonctionnel $\phi_i \in E^*$ est donné par $\phi_i(y) = \langle v_i, y \rangle$.
De même, pour les vecteurs normalisés $u_i = v_i/\|v_i\|$, nous définissons les fonctionnels $\psi_i = \mathcal{R}(u_i) \in E^*$, de sorte que $\psi_i(y) = \langle u_i, y \rangle$.

Le problème de maximisation est $f(x) = \sum_{i=1}^N \langle x, u_i \rangle^2$ sous la contrainte $\|x\|=1$.
En utilisant la définition de $\psi_i$, nous pouvons réécrire l'objectif comme :
$$ f(x) = \sum_{i=1}^N (\psi_i(x))^2 $$
L'isomorphisme de Riesz permet également de définir un produit scalaire sur $E^*$. Pour $\chi, \zeta \in E^*$, on définit $\langle \chi, \zeta \rangle_{E^*} = \langle \mathcal{R}^{-1}(\chi), \mathcal{R}^{-1}(\zeta) \rangle_E$.
La norme associée dans $E^*$ est $\|\chi\|_{E^*} = \|\mathcal{R}^{-1}(\chi)\|_E$.
Ainsi, la contrainte $\|x\|=1$ est équivalente à $\|\mathcal{R}(x)\|_{E^*} = 1$.
Soit $\chi = \mathcal{R}(x) \in E^*$. Alors $x = \mathcal{R}^{-1}(\chi)$.
L'expression $\psi_i(x)$ peut être réécrite en utilisant le produit scalaire dans $E^*$:
$$ \psi_i(x) = \langle u_i, x \rangle_E = \langle \mathcal{R}^{-1}(\psi_i), \mathcal{R}^{-1}(\chi) \rangle_E = \langle \psi_i, \chi \rangle_{E^*} $$
Donc, le problème de maximisation peut être reformulé dans l'espace dual $E^*$ comme :
Maximiser $\sum_{i=1}^N \langle \psi_i, \chi \rangle_{E^*}^2$ sous la contrainte $\|\chi\|_{E^*} = 1$.
Ceci est exactement le même type de problème que celui initial, mais formulé dans l'espace dual $E^*$ avec les fonctionnels $\psi_i$ et la variable d'optimisation $\chi$.

**Connexion entre $M$ et la matrice de Gram des fonctionnels $\psi_i$**:
Soit $\{e_1, \dots, e_m\}$ une base orthonormée de $E$. Soit $A$ la matrice de taille $N \times m$ dont la $i$-ème ligne est le vecteur de coordonnées de $u_i$ dans cette base, c'est-à-dire $A_{ij} = (u_i)_j$.
Alors, comme établi précédemment, $M = A^T A$.

La matrice de Gram $G$ des fonctionnels $\{\psi_1, \dots, \psi_N\}$ est une matrice de taille $N \times N$ dont les entrées sont $G_{jk} = \langle \psi_j, \psi_k \rangle_{E^*}$.
En utilisant la définition du produit scalaire dans $E^*$ et l'isomorphisme de Riesz :
$$ G_{jk} = \langle \mathcal{R}^{-1}(\psi_j), \mathcal{R}^{-1}(\psi_k) \rangle_E = \langle u_j, u_k \rangle_E $$
Dans la base orthonormée, $\langle u_j, u_k \rangle_E = u_j^T u_k$.
Considérons le produit matriciel $A A^T$:
$$ (A A^T)_{jk} = \sum_{l=1}^m A_{jl} (A^T)_{lk} = \sum_{l=1}^m A_{jl} A_{kl} = \sum_{l=1}^m (u_j)_l (u_k)_l = u_j^T u_k $$
Donc, la matrice de Gram $G$ des fonctionnels $\psi_i$ est $G = A A^T$.

Nous avons $M = A^T A$ et $G = A A^T$. Il est un résultat connu de l'algèbre linéaire que les matrices $A^T A$ et $A A^T$ ont les mêmes valeurs propres non nulles.
Par conséquent, la valeur maximale de $f(x)$, qui est $\lambda_{\max}(M)$, est également la plus grande valeur propre de la matrice de Gram $G$.
Si $y \in \mathbb{R}^N$ est un vecteur propre de $G$ associé à la valeur propre $\lambda_{\max}(G)$, alors $G y = \lambda_{\max}(G) y$, ce qui signifie $A A^T y = \lambda_{\max}(G) y$.
En multipliant par $A^T$ à gauche, on obtient $A^T A A^T y = \lambda_{\max}(G) A^T y$.
Puisque $M = A^T A$, cela donne $M (A^T y) = \lambda_{\max}(G) (A^T y)$.
Ainsi, $A^T y$ est un vecteur propre de $M$ associé à la valeur propre $\lambda_{\max}(G)$.
Le vecteur $x$ qui maximise $f(x)$ est alors donné par la normalisation de $A^T y$:
$$ x = \frac{A^T y}{\|A^T y\|} $$
où $y$ est un vecteur propre unitaire de $G$ associé à sa plus grande valeur propre. Cette relation offre une méthode alternative pour trouver le vecteur $x$, potentiellement plus efficace si $N < m$ (car $G$ est de taille $N \times N$ tandis que $M$ est de taille $m \times m$).

### Conclusion
Nous avons montré que le problème de maximisation de la somme des carrés des similarités cosinus d'un vecteur unitaire $x$ avec un ensemble de vecteurs de plongement $S = \{v_1, \dots, v_N\}$ se ramène à la maximisation d'une forme quadratique $x^T M x$ sous la contrainte $\|x\|=1$. La matrice $M = \sum_{i=1}^N u_i u_i^T$ (où $u_i = v_i/\|v_i\|$) est symétrique et semi-définie positive.

Le(s) vecteur(s) $x$ qui maximise(nt) cette fonction sont les vecteurs propres unitaires de $M$ associés à sa plus grande valeur propre $\lambda_{\max}(M)$. La valeur maximale de la fonction objectif est $\lambda_{\max}(M)$.

Géométriquement, la matrice $M$ agrège les directions des vecteurs de plongement normalisés, et le vecteur $x$ maximisant représente la "direction sémantique principale" de l'ensemble des documents, c'est-à-dire la direction qui capture le mieux l'orientation moyenne des plongements normalisés.

Enfin, en utilisant l'isomorphisme de Riesz, nous avons reformulé le problème dans l'espace dual $E^*$. La matrice $M$ est liée à la matrice de Gram $G = A A^T$ des fonctionnels $\psi_i = \mathcal{R}(u_i)$ par la relation $M = A^T A$, où $A$ est la matrice dont les lignes sont les coordonnées des $u_i$. Les matrices $M$ et $G$ partagent les mêmes valeurs propres non nulles, et le vecteur $x$ maximisant peut être obtenu à partir du vecteur propre principal de $G$.

Ce cadre mathématique fournit une base solide pour identifier des directions sémantiques dominantes dans des collections de plongements, ce qui est fondamental pour la conception de moteurs de recherche sémantiques et l'analyse de clusters de documents.
