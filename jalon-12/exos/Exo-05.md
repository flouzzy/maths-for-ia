# Exercice 05 (3 $\star$) : Optimisation de la Similarité Cosinus et Dualité dans les Espaces de Plongement Sémantiques

## Énoncé

Soit $E = \mathbb{R}^n$ un espace vectoriel euclidien de dimension $n \ge 1$, muni du produit scalaire standard $\langle u, v \rangle = u^T v$ pour $u, v \in E$, et de la norme euclidienne associée $\|u\| = \sqrt{\langle u, u \rangle}$.

Dans le contexte des espaces de plongement (embedding spaces) pour la recherche sémantique, nous introduisons une matrice $A \in \mathcal{M}_n(\mathbb{R})$ qui représente une "pondération sémantique". On suppose que $A$ est une matrice symétrique définie positive.

1.  Montrer que l'application $(u, v) \mapsto \langle u, v \rangle_A = \langle u, Av \rangle = u^T A v$ définit un produit scalaire sur $E$. Nous noterons la norme associée $\|u\|_A = \sqrt{\langle u, u \rangle_A}$.

2.  Soit $q \in E$ un vecteur de requête (query vector) non nul et fixé. Nous recherchons un vecteur document $d \in E$ qui maximise la similarité cosinus standard $\cos(\theta(q,d)) = \frac{\langle q, d \rangle}{\|q\| \|d\|}$, sous la contrainte que le vecteur document $d$ possède une norme sémantiquement pondérée unitaire, c'est-à-dire $\|d\|_A = 1$.
    Déterminer le vecteur $d^*$ qui maximise cette quantité et exprimer la valeur maximale atteinte en fonction de $q$ et $A$.

3.  Pour tout vecteur $v \in E$, on considère la forme linéaire $L_v: E \to \mathbb{R}$ définie par $L_v(u) = \langle u, v \rangle_A$.
    En vertu du théorème de représentation de Riesz pour les espaces euclidiens, il existe un unique vecteur $v' \in E$ tel que $L_v(u) = \langle u, v' \rangle$ pour tout $u \in E$.
    Exprimer $v'$ en fonction de $v$ et $A$. Interpréter ce résultat dans le contexte de la dualité entre le produit scalaire standard et le produit scalaire sémantiquement pondéré.

## Correction Détaillée

### Analyse et Stratégie

Cet exercice explore la géométrie des espaces de plongement sous l'influence d'une pondération sémantique représentée par une matrice symétrique définie positive $A$.

1.  **Question 1 (Produit Scalaire):** Il s'agit de vérifier les axiomes d'un produit scalaire : bilinéarité, symétrie et positivité définie. La symétrie et la positivité définie de $A$ seront cruciales.

2.  **Question 2 (Optimisation):** Nous devons maximiser une fonction (la similarité cosinus standard) sous une contrainte (norme sémantiquement pondérée unitaire).
    La stratégie consistera à transformer le problème d'optimisation en un problème plus simple dans un espace où la contrainte devient une norme euclidienne standard. Pour cela, nous utiliserons la racine carrée de la matrice $A$, notée $A^{1/2}$, qui est également symétrique définie positive. Cette transformation permettra d'appliquer l'inégalité de Cauchy-Schwarz pour trouver le maximum.

3.  **Question 3 (Dualité):** Le théorème de Riesz établit une correspondance entre les formes linéaires continues et les vecteurs de l'espace. Ici, nous avons une forme linéaire définie par un produit scalaire non standard. L'objectif est de trouver le vecteur qui représente cette forme linéaire dans le cadre du produit scalaire standard. Cela implique une manipulation algébrique directe des définitions des produits scalaires.

### Résolution Pas-à-Pas

#### Question 1 : Preuve que $\langle u, v \rangle_A$ est un produit scalaire

Soient $u, v, w \in E$ et $\alpha, \beta \in \mathbb{R}$.

1.  **Bilinéraité :**
    *   Linéarité par rapport à la première variable :
        $\langle \alpha u + \beta v, w \rangle_A = (\alpha u + \beta v)^T A w$
        $= (\alpha u^T + \beta v^T) A w$
        $= \alpha u^T A w + \beta v^T A w$
        $= \alpha \langle u, w \rangle_A + \beta \langle v, w \rangle_A$.
    *   Linéarité par rapport à la deuxième variable :
        $\langle u, \alpha v + \beta w \rangle_A = u^T A (\alpha v + \beta w)$
        $= u^T (\alpha A v + \beta A w)$
        $= \alpha u^T A v + \beta u^T A w$
        $= \alpha \langle u, v \rangle_A + \beta \langle u, w \rangle_A$.
    L'application est bilinéaire.

2.  **Symétrie :**
    $\langle u, v \rangle_A = u^T A v$.
    Puisque $u^T A v$ est un scalaire, il est égal à sa propre transposée :
    $u^T A v = (u^T A v)^T = v^T A^T u$.
    Comme $A$ est symétrique, $A^T = A$.
    Donc, $v^T A^T u = v^T A u = \langle v, u \rangle_A$.
    L'application est symétrique.

3.  **Positivité définie :**
    $\langle u, u \rangle_A = u^T A u$.
    Puisque $A$ est une matrice définie positive, par définition, $u^T A u > 0$ pour tout $u \in E, u \ne 0$.
    De plus, si $u = 0$, alors $\langle 0, 0 \rangle_A = 0^T A 0 = 0$.
    Donc, $\langle u, u \rangle_A \ge 0$ et $\langle u, u \rangle_A = 0 \iff u = 0$.
    L'application est définie positive.

Les trois propriétés étant vérifiées, $\langle u, v \rangle_A$ est bien un produit scalaire sur $E$.

#### Question 2 : Optimisation de la similarité cosinus standard sous contrainte de norme sémantique

Nous cherchons à maximiser $\cos(\theta(q,d)) = \frac{\langle q, d \rangle}{\|q\| \|d\|}$ sous la contrainte $\|d\|_A = 1$.
Puisque $q$ est un vecteur non nul fixé, $\|q\|$ est une constante positive. Maximiser $\cos(\theta(q,d))$ est équivalent à maximiser $\frac{\langle q, d \rangle}{\|d\|}$ (car le cosinus est positif pour le maximum, et $\|d\|$ sera non nul).

La matrice $A$ est symétrique définie positive. Il existe donc une unique matrice $A^{1/2}$, également symétrique définie positive, telle que $(A^{1/2})^2 = A$. De même, $A^{-1/2} = (A^{1/2})^{-1}$ est symétrique définie positive.

Effectuons un changement de variable. Soit $x = A^{1/2} d$. Puisque $A^{1/2}$ est inversible, $d = A^{-1/2} x$.

1.  **Transformation de la contrainte :**
    La contrainte est $\|d\|_A = 1$, ce qui signifie $\langle d, d \rangle_A = 1$.
    Substituons $d = A^{-1/2} x$ :
    $\langle A^{-1/2} x, A^{-1/2} x \rangle_A = (A^{-1/2} x)^T A (A^{-1/2} x)$
    $= x^T (A^{-1/2})^T A A^{-1/2} x$.
    Puisque $A^{1/2}$ est symétrique, $(A^{1/2})^T = A^{1/2}$, et donc $(A^{-1/2})^T = A^{-1/2}$.
    $= x^T A^{-1/2} A A^{-1/2} x$.
    Comme $A = A^{1/2} A^{1/2}$, on a $A^{-1/2} A A^{-1/2} = A^{-1/2} (A^{1/2} A^{1/2}) A^{-1/2} = (A^{-1/2} A^{1/2}) (A^{1/2} A^{-1/2}) = I \cdot I = I$.
    Donc, la contrainte devient $x^T I x = x^T x = \|x\|^2 = 1$.
    Le problème est maintenant de maximiser une expression sous la contrainte $\|x\|=1$.

2.  **Transformation de la fonction objectif :**
    Nous voulons maximiser $\frac{\langle q, d \rangle}{\|d\|}$. Substituons $d = A^{-1/2} x$:
    *   Numérateur : $\langle q, d \rangle = \langle q, A^{-1/2} x \rangle$.
        Puisque $A^{-1/2}$ est symétrique, $\langle q, A^{-1/2} x \rangle = \langle A^{-1/2} q, x \rangle$.
        Soit $q' = A^{-1/2} q$. Alors le numérateur est $\langle q', x \rangle$.
    *   Dénominateur : $\|d\| = \|A^{-1/2} x\|$.

    Le problème d'optimisation devient : maximiser $\frac{\langle q', x \rangle}{\|q\| \|A^{-1/2} x\|}$ sous la contrainte $\|x\|=1$.
    Par l'inégalité de Cauchy-Schwarz pour le produit scalaire standard :
    $\langle q', x \rangle \le \|q'\| \|x\|$.
    Puisque $\|x\|=1$, nous avons $\langle q', x \rangle \le \|q'\|$.
    L'égalité est atteinte lorsque $x$ est colinéaire à $q'$, c'est-à-dire $x = \alpha q'$ pour un scalaire $\alpha$.
    Avec la contrainte $\|x\|=1$, nous avons $\|\alpha q'\|=1 \implies |\alpha| \|q'\|=1$.
    Pour maximiser $\langle q', x \rangle$, nous choisissons $\alpha = \frac{1}{\|q'\|}$ (pour que $\langle q', x \rangle$ soit positif).
    Donc, $x^* = \frac{q'}{\|q'\|}$.

3.  **Détermination de $d^*$ :**
    Nous avons $d^* = A^{-1/2} x^* = A^{-1/2} \left( \frac{q'}{\|q'\|} \right)$.
    En substituant $q' = A^{-1/2} q$:
    $d^* = A^{-1/2} \left( \frac{A^{-1/2} q}{\|A^{-1/2} q\|} \right) = \frac{A^{-1/2} A^{-1/2} q}{\|A^{-1/2} q\|} = \frac{A^{-1} q}{\|A^{-1/2} q\|}$.

    Vérifions le dénominateur $\|A^{-1/2} q\|$.
    $\|A^{-1/2} q\|^2 = \langle A^{-1/2} q, A^{-1/2} q \rangle = (A^{-1/2} q)^T (A^{-1/2} q)$.
    Puisque $A^{-1/2}$ est symétrique, $(A^{-1/2})^T = A^{-1/2}$.
    $= q^T A^{-1/2} A^{-1/2} q = q^T A^{-1} q = \langle q, A^{-1} q \rangle$.
    Donc, $\|A^{-1/2} q\| = \sqrt{\langle q, A^{-1} q \rangle}$.

    Le vecteur $d^*$ qui maximise la similarité cosinus standard est $d^* = \frac{A^{-1} q}{\sqrt{\langle q, A^{-1} q \rangle}}$.

4.  **Calcul de la valeur maximale :**
    La valeur maximale est $\cos(\theta(q,d^*)) = \frac{\langle q, d^* \rangle}{\|q\| \|d^*\|}$.
    *   Calculons le numérateur :
        $\langle q, d^* \rangle = \left\langle q, \frac{A^{-1} q}{\sqrt{\langle q, A^{-1} q \rangle}} \right\rangle = \frac{1}{\sqrt{\langle q, A^{-1} q \rangle}} \langle q, A^{-1} q \rangle = \sqrt{\langle q, A^{-1} q \rangle}$.
    *   Calculons le dénominateur $\|d^*\|$ :
        $\|d^*\| = \left\| \frac{A^{-1} q}{\sqrt{\langle q, A^{-1} q \rangle}} \right\| = \frac{1}{\sqrt{\langle q, A^{-1} q \rangle}} \|A^{-1} q\|$.

    En substituant ces expressions dans la formule du cosinus :
    $\cos(\theta(q,d^*)) = \frac{\sqrt{\langle q, A^{-1} q \rangle}}{\|q\| \frac{1}{\sqrt{\langle q, A^{-1} q \rangle}} \|A^{-1} q\|} = \frac{\langle q, A^{-1} q \rangle}{\|q\| \|A^{-1} q\|}$.

    La valeur maximale de la similarité cosinus standard est $\frac{\langle q, A^{-1} q \rangle}{\|q\| \|A^{-1} q\|}$.

#### Question 3 : Dualité et représentation de Riesz

Nous avons la forme linéaire $L_v: E \to \mathbb{R}$ définie par $L_v(u) = \langle u, v \rangle_A$.
Nous cherchons $v' \in E$ tel que $L_v(u) = \langle u, v' \rangle$ pour tout $u \in E$.

Par définition, $L_v(u) = \langle u, Av \rangle$.
Nous voulons que $\langle u, Av \rangle = \langle u, v' \rangle$ pour tout $u \in E$.
Ceci implique que $\langle u, Av - v' \rangle = 0$ pour tout $u \in E$.
Par la propriété de non-dégénérescence du produit scalaire standard, cela signifie que $Av - v' = 0$.
Donc, $v' = Av$.

**Interprétation :**
Le vecteur $v'$ qui représente la forme linéaire $L_v$ (définie par le produit scalaire sémantiquement pondéré avec $v$) dans l'espace euclidien standard est obtenu en appliquant l'opérateur de pondération sémantique $A$ au vecteur original $v$.
Cela signifie que la "direction" ou "orientation" sémantique de $v$ (telle que perçue par le produit scalaire $\langle \cdot, \cdot \rangle_A$) est transformée par $A$ pour être représentée comme une direction dans l'espace euclidien standard. En d'autres termes, l'opérateur $A$ agit comme un pont entre la géométrie sémantiquement pondérée et la géométrie euclidienne standard, en transformant les vecteurs pour qu'ils représentent la même forme linéaire. C'est une illustration concrète de la dualité où l'opérateur $A$ (ou son inverse $A^{-1}$) peut être vu comme un "changement de base" entre l'espace et son dual, ou entre différentes métriques sur le même espace.

### Conclusion

1.  Nous avons rigoureusement démontré que l'application $(u, v) \mapsto u^T A v$ définit un produit scalaire sur $E$, grâce aux propriétés de symétrie et de positivité définie de la matrice $A$.

2.  Le vecteur document $d^*$ qui maximise la similarité cosinus standard avec un vecteur de requête $q$ sous la contrainte d'une norme sémantiquement pondérée unitaire ($\|d\|_A=1$) est donné par :
    $$d^* = \frac{A^{-1} q}{\sqrt{\langle q, A^{-1} q \rangle}}$$
    La valeur maximale de la similarité cosinus standard atteinte est :
    $$\max_{d: \|d\|_A=1} \cos(\theta(q,d)) = \frac{\langle q, A^{-1} q \rangle}{\|q\| \|A^{-1} q\|}$$
    Ce résultat montre que pour optimiser la similarité standard sous une contrainte sémantique, il faut "dé-pondérer" le vecteur de requête $q$ par l'inverse de la matrice sémantique $A$.

3.  Le vecteur $v'$ qui représente la forme linéaire $L_v(u) = \langle u, v \rangle_A$ dans le produit scalaire standard est $v' = Av$. Ce résultat illustre comment l'opérateur de pondération sémantique $A$ transforme les vecteurs pour aligner la géométrie sémantiquement pondérée avec la géométrie euclidienne standard dans le contexte de la dualité.
