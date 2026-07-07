# Exercice 09 (5 $\star$) : Optimisation de la Pertinence Sémantique Généralisée dans les Espaces de Plongement

## Énoncé
Soit $(E, \langle \cdot, \cdot \rangle)$ un espace vectoriel euclidien réel de dimension finie $n \ge 1$. On note $\|\cdot\|$ la norme euclidienne associée.
Soit $A \in \mathcal{L}(E)$ un opérateur linéaire auto-adjoint et positif défini.
Soit $F$ un sous-espace vectoriel de $E$ de dimension $k \ge 1$.
Soit $q \in E \setminus \{0\}$ un vecteur de requête fixe.

Pour tout $x \in E \setminus \{0\}$, nous définissons une fonction de pertinence sémantique généralisée $R(x)$ par :
$$R(x) = \frac{\langle q, x \rangle^2}{\langle x, Ax \rangle}$$

L'objectif de cet exercice est de déterminer le vecteur $x_0 \in F \setminus \{0\}$ (à un facteur d'échelle près) qui maximise $R(x)$ sur $F$, et de calculer la valeur maximale de $R(x)$.

1.  **Propriétés de l'opérateur $A$ et du produit scalaire induit.**
    *   a) Prouver que la forme bilinéaire $B(u,v) = \langle u, Av \rangle$ définit un produit scalaire sur $E$. On notera ce produit scalaire $(\cdot, \cdot)_A$ et la norme associée $\|\cdot\|_A$.
    *   b) Justifier que $R(x)$ est bien définie et positive pour tout $x \in E \setminus \{0\}$.
    *   c) Montrer qu'il existe un unique opérateur $A^{1/2} \in \mathcal{L}(E)$ tel que $(A^{1/2})^2 = A$, et que $A^{1/2}$ est auto-adjoint et positif défini.

2.  **Transformation du problème d'optimisation.**
    *   a) En utilisant l'opérateur $A^{1/2}$, effectuer un changement de variable $y = A^{1/2}x$. Expliciter $x$ en fonction de $y$.
    *   b) Montrer que la maximisation de $R(x)$ pour $x \in F \setminus \{0\}$ est équivalente à la maximisation d'une expression de la forme $\frac{\langle q', y \rangle^2}{\|y\|^2}$ pour un certain vecteur $q' \in E$ et $y$ appartenant à un sous-espace $F' \subseteq E$. Expliciter $q'$ et $F'$.

3.  **Détermination du vecteur optimal et de la valeur maximale.**
    *   a) En utilisant le résultat de la question 2.b) et l'inégalité de Cauchy-Schwarz, déterminer le vecteur $y_0 \in F' \setminus \{0\}$ (à un facteur d'échelle près) qui maximise l'expression $\frac{\langle q', y \rangle^2}{\|y\|^2}$. Exprimer $y_0$ en fonction de $q'$ et de la projection orthogonale $P_{F'}$ sur $F'$ (par rapport au produit scalaire standard $\langle \cdot, \cdot \rangle$).
    *   b) En déduire le vecteur $x_0 \in F \setminus \{0\}$ (à un facteur d'échelle près) qui maximise $R(x)$.
    *   c) Calculer la valeur maximale $R_{max}$ de $R(x)$.
    *   d) Interpréter géométriquement $x_0$ et $R_{max}$ en termes de "proximité" dans l'espace $(E, (\cdot, \cdot)_A)$.


### Matrice de Gram et Indépendance Linéaire
Étant donné un ensemble de vecteurs $\{u_1, \dots, u_k\}$, leur matrice de Gram $G$ a pour coefficients $G_{i,j} = \langle u_i, u_j \rangle$. La normalisation de la matrice de Gram donne directement la matrice des similarités cosinus. Si $G$ est inversible, la famille est libre, prouvant que les concepts sémantiques correspondants ne sont pas colinéaires.

## Correction Détaillée
### Analyse et Stratégie
Le problème nous demande de maximiser une fonction de pertinence $R(x)$ définie comme le rapport d'une forme quadratique (liée au produit scalaire standard) et d'une autre forme quadratique (liée à l'opérateur $A$). L'opérateur $A$ est auto-adjoint et positif défini, ce qui est une information cruciale.

La stratégie générale sera la suivante :
1.  **Caractériser le produit scalaire induit par $A$** : La première étape consiste à montrer que $B(u,v) = \langle u, Av \rangle$ est bien un produit scalaire. Cela nous permettra de comprendre la structure de l'espace de "plongement sémantique" induit par $A$.
2.  **Utiliser l'opérateur racine carrée $A^{1/2}$** : L'existence et les propriétés de $A^{1/2}$ sont fondamentales pour simplifier l'expression de $R(x)$. Cet opérateur permet de "diagonaliser" la forme quadratique au dénominateur et de la ramener à une norme euclidienne standard après un changement de variable.
3.  **Changement de variable et projection** : En effectuant un changement de variable $y = A^{1/2}x$, nous transformerons le problème d'optimisation original en un problème de maximisation d'un rapport de formes quadratiques plus simple, qui peut être résolu par l'inégalité de Cauchy-Schwarz et la notion de projection orthogonale.
4.  **Retour à l'espace original et interprétation** : Une fois le vecteur optimal $y_0$ trouvé dans l'espace transformé, nous le retransformerons en $x_0$ dans l'espace original $E$. Enfin, nous interpréterons géométriquement le résultat en termes de dualité et de géométrie des espaces de plongement, en utilisant le produit scalaire $(\cdot, \cdot)_A$.

### Résolution Pas-à-Pas

1.  **Propriétés de l'opérateur $A$ et du produit scalaire induit.**
    *   a) Prouvons que la forme bilinéaire $B(u,v) = \langle u, Av \rangle$ définit un produit scalaire sur $E$.
        Pour qu'une forme bilinéaire soit un produit scalaire, elle doit satisfaire les propriétés suivantes :
        *   **Bilinearité :** Pour $u, v, w \in E$ et $\alpha \in \mathbb{R}$ :
            *   $B(u, \alpha v + w) = \langle u, A(\alpha v + w) \rangle = \langle u, \alpha Av + Aw \rangle$. Par linéarité du produit scalaire $\langle \cdot, \cdot \rangle$ dans la deuxième composante, on a :
                $B(u, \alpha v + w) = \alpha \langle u, Av \rangle + \langle u, Aw \rangle = \alpha B(u,v) + B(u,w)$.
            *   $B(\alpha u + w, v) = \langle \alpha u + w, Av \rangle$. Par linéarité du produit scalaire $\langle \cdot, \cdot \rangle$ dans la première composante, on a :
                $B(\alpha u + w, v) = \alpha \langle u, Av \rangle + \langle w, Av \rangle = \alpha B(u,v) + B(w,v)$.
            La bilinéarité est donc vérifiée.
        *   **Symétrie :** Pour $u, v \in E$ :
            $B(u,v) = \langle u, Av \rangle$. Puisque $A$ est auto-adjoint, par définition, $\langle u, Av \rangle = \langle Au, v \rangle$. Par symétrie de la forme bilinéaire du produit scalaire $\langle \cdot, \cdot \rangle$, on a $\langle Au, v \rangle = \langle v, Au \rangle$. Donc $B(u,v) = \langle v, Au \rangle = B(v,u)$.
            La symétrie est donc vérifiée.
        *   **Positivité définie :** Pour $u \in E$ :
            $B(u,u) = \langle u, Au \rangle$. Puisque $A$ est positif défini, par définition, $\langle u, Au \rangle > 0$ pour tout $u \neq 0$, et $\langle 0, A0 \rangle = 0$.
            La positivité définie est donc vérifiée.
        En conclusion, $B(u,v) = \langle u, Av \rangle$ définit bien un produit scalaire sur $E$. Nous le noterons $(\cdot, \cdot)_A$, et la norme associée $\|\cdot\|_A = \sqrt{(u,u)_A} = \sqrt{\langle u, Au \rangle}$.

    *   b) Justifions que $R(x)$ est bien définie et positive pour tout $x \in E \setminus \{0\}$.
        Le numérateur est $\langle q, x \rangle^2$. C'est le carré d'un nombre réel, donc il est toujours $\ge 0$.
        Le dénominateur est $\langle x, Ax \rangle$. D'après la question 1.a), puisque $A$ est positif défini, $\langle x, Ax \rangle > 0$ pour tout $x \in E \setminus \{0\}$.
        Ainsi, pour tout $x \in E \setminus \{0\}$, le dénominateur est non nul et strictement positif. La fonction $R(x)$ est donc bien définie et $R(x) \ge 0$.

    *   c) Montrons qu'il existe un unique opérateur $A^{1/2} \in \mathcal{L}(E)$ tel que $(A^{1/2})^2 = A$, et que $A^{1/2}$ est auto-adjoint et positif défini.
        Puisque $E$ est un espace euclidien de dimension finie et $A$ est un opérateur auto-adjoint, d'après le théorème spectral, il existe une base orthonormée de $E$, disons $(e_1, \dots, e_n)$, constituée de vecteurs propres de $A$. Soient $\lambda_1, \dots, \lambda_n$ les valeurs propres correspondantes.
        Puisque $A$ est positif défini, pour tout $x \neq 0$, $\langle x, Ax \rangle > 0$. En particulier, pour chaque vecteur propre $e_i$, $\langle e_i, Ae_i \rangle = \langle e_i, \lambda_i e_i \rangle = \lambda_i \langle e_i, e_i \rangle = \lambda_i \|e_i\|^2 = \lambda_i$. Donc $\lambda_i > 0$ pour tout $i=1, \dots, n$.
        Nous pouvons alors définir l'opérateur $A^{1/2}$ sur cette base de vecteurs propres par $A^{1/2}e_i = \sqrt{\lambda_i}e_i$ pour chaque $i$.
        *   **Existence :** L'opérateur $A^{1/2}$ est bien défini par sa restriction à une base.
        *   **Propriété $(A^{1/2})^2 = A$ :** Pour tout $e_i$, $(A^{1/2})^2 e_i = A^{1/2}(A^{1/2}e_i) = A^{1/2}(\sqrt{\lambda_i}e_i) = \sqrt{\lambda_i}A^{1/2}e_i = \sqrt{\lambda_i}(\sqrt{\lambda_i}e_i) = \lambda_i e_i = Ae_i$. Puisque $(A^{1/2})^2$ et $A$ agissent de la même manière sur une base, ils sont égaux.
        *   **Auto-adjoint :** Pour $u = \sum u_i e_i$ et $v = \sum v_i e_i$:
            $\langle u, A^{1/2}v \rangle = \langle \sum u_i e_i, \sum v_j \sqrt{\lambda_j} e_j \rangle = \sum_i \sum_j u_i v_j \sqrt{\lambda_j} \langle e_i, e_j \rangle = \sum_i u_i v_i \sqrt{\lambda_i}$.
            $\langle A^{1/2}u, v \rangle = \langle \sum u_i \sqrt{\lambda_i} e_i, \sum v_j e_j \rangle = \sum_i \sum_j u_i \sqrt{\lambda_i} v_j \langle e_i, e_j \rangle = \sum_i u_i \sqrt{\lambda_i} v_i$.
            Donc $\langle u, A^{1/2}v \rangle = \langle A^{1/2}u, v \rangle$, ce qui prouve que $A^{1/2}$ est auto-adjoint.
        *   **Positif défini :** Pour tout $u = \sum u_i e_i \neq 0$:
            $\langle u, A^{1/2}u \rangle = \sum_i u_i^2 \sqrt{\lambda_i}$. Puisque $u \neq 0$, au moins un $u_i \neq 0$. Puisque tous les $\sqrt{\lambda_i} > 0$, on a $\sum_i u_i^2 \sqrt{\lambda_i} > 0$. Donc $A^{1/2}$ est positif défini.
        *   **Unicité :** Supposons qu'il existe un autre opérateur $B \in \mathcal{L}(E)$ tel que $B^2=A$, $B$ auto-adjoint et positif défini. Alors $B$ est diagonalisable dans une base orthonormée avec des valeurs propres positives. Soit $u$ un vecteur propre de $B$ avec valeur propre $\mu$. Alors $Bu = \mu u$, et $B^2 u = \mu^2 u$. Puisque $B^2=A$, $Au = \mu^2 u$. Donc $u$ est aussi un vecteur propre de $A$ avec valeur propre $\mu^2$. Puisque les valeurs propres de $A$ sont $\lambda_i$, alors $\mu^2$ doit être l'une des $\lambda_i$. Donc $\mu = \sqrt{\lambda_i}$ (puisque $\mu > 0$). Ainsi, $B$ doit avoir les mêmes valeurs propres que $A^{1/2}$ et les mêmes espaces propres. Par conséquent, $B=A^{1/2}$.

2.  **Transformation du problème d'optimisation.**
    *   a) Utilisons l'opérateur $A^{1/2}$ pour un changement de variable.
        Puisque $A^{1/2}$ est positif défini, toutes ses valeurs propres $\sqrt{\lambda_i}$ sont strictement positives. Cela implique que $A^{1/2}$ est inversible. Son inverse, noté $A^{-1/2}$, est également auto-adjoint et positif défini.
        Posons $y = A^{1/2}x$. Alors $x = (A^{1/2})^{-1}y = A^{-1/2}y$.

    *   b) Montrons l'équivalence de la maximisation.
        Substituons $x = A^{-1/2}y$ dans l'expression de $R(x)$ :
        *   **Dénominateur :** $\langle x, Ax \rangle = \langle A^{-1/2}y, A(A^{-1/2}y) \rangle$.
            Puisque $A = (A^{1/2})^2$, on a $A(A^{-1/2}y) = A^{1/2}(A^{1/2}A^{-1/2}y) = A^{1/2}y$.
            Donc $\langle x, Ax \rangle = \langle A^{-1/2}y, A^{1/2}y \rangle$.
            Puisque $A^{1/2}$ est auto-adjoint, $\langle A^{-1/2}y, A^{1/2}y \rangle = \langle y, (A^{-1/2})^* A^{1/2}y \rangle = \langle y, A^{-1/2} A^{1/2}y \rangle = \langle y, Iy \rangle = \langle y, y \rangle = \|y\|^2$.
            Ainsi, le dénominateur devient $\|y\|^2$.
        *   **Numérateur :** $\langle q, x \rangle^2 = \langle q, A^{-1/2}y \rangle^2$.
            Posons $q' = A^{-1/2}q$. Alors le numérateur devient $\langle q', y \rangle^2$.
        La fonction de pertinence $R(x)$ se transforme en $R'(y) = \frac{\langle q', y \rangle^2}{\|y\|^2}$.
        Le vecteur $x$ appartient au sous-espace $F$. Donc $y = A^{1/2}x$ appartient au sous-espace $F' = A^{1/2}(F)$.
        $F'$ est bien un sous-espace vectoriel de $E$ car $A^{1/2}$ est un opérateur linéaire et $F$ est un sous-espace.
        La maximisation de $R(x)$ pour $x \in F \setminus \{0\}$ est donc équivalente à la maximisation de $R'(y) = \frac{\langle q', y \rangle^2}{\|y\|^2}$ pour $y \in F' \setminus \{0\}$, avec $q' = A^{-1/2}q$ et $F' = A^{1/2}(F)$.

3.  **Détermination du vecteur optimal et de la valeur maximale.**
    *   a) Déterminons $y_0 \in F' \setminus \{0\}$ qui maximise $\frac{\langle q', y \rangle^2}{\|y\|^2}$.
        L'expression à maximiser est $\frac{\langle q', y \rangle^2}{\|y\|^2}$.
        D'après l'inégalité de Cauchy-Schwarz, pour tout $y \in F'$, on a $\langle q', y \rangle^2 \le \|q'\|^2 \|y\|^2$.
        Donc $\frac{\langle q', y \rangle^2}{\|y\|^2} \le \|q'\|^2$.
        L'égalité est atteinte si et seulement si $y$ est colinéaire à $q'$. Cependant, $y$ doit également appartenir à $F'$.
        Par conséquent, la maximisation de $\frac{\langle q', y \rangle^2}{\|y\|^2}$ pour $y \in F' \setminus \{0\}$ est atteinte lorsque $y$ est colinéaire à la projection orthogonale de $q'$ sur $F'$.
        Soit $P_{F'}$ l'opérateur de projection orthogonale sur $F'$ par rapport au produit scalaire standard $\langle \cdot, \cdot \rangle$.
        Le vecteur $y_0$ (à un facteur d'échelle près) qui maximise l'expression est $y_0 = P_{F'}(q')$.
        La valeur maximale de l'expression est alors $\frac{\langle q', P_{F'}(q') \rangle^2}{\|P_{F'}(q')\|^2}$.
        Puisque $P_{F'}(q')$ est la projection orthogonale de $q'$ sur $F'$, on a $\langle q', P_{F'}(q') \rangle = \langle P_{F'}(q') + (q' - P_{F'}(q')), P_{F'}(q') \rangle = \langle P_{F'}(q'), P_{F'}(q') \rangle + \langle q' - P_{F'}(q'), P_{F'}(q') \rangle$.
        Par définition de la projection orthogonale, $q' - P_{F'}(q')$ est orthogonal à $F'$, donc $\langle q' - P_{F'}(q'), P_{F'}(q') \rangle = 0$.
        Ainsi, $\langle q', P_{F'}(q') \rangle = \|P_{F'}(q')\|^2$.
        La valeur maximale est donc $\frac{(\|P_{F'}(q')\|^2)^2}{\|P_{F'}(q')\|^2} = \|P_{F'}(q')\|^2$.
        Si $P_{F'}(q') = 0$, alors $q'$ est orthogonal à $F'$, et la valeur maximale est 0. Dans ce cas, tout $y \in F' \setminus \{0\}$ donne une valeur de 0.

    *   b) Déduisons le vecteur optimal $x_0 \in F \setminus \{0\}$.
        Nous avons $y_0 = P_{F'}(q')$.
        En utilisant la relation $x = A^{-1/2}y$, nous obtenons :
        $x_0 = A^{-1/2}y_0 = A^{-1/2}P_{F'}(q')$.
        En substituant $q' = A^{-1/2}q$ et $F' = A^{1/2}(F)$ :
        $x_0 = A^{-1/2}P_{A^{1/2}(F)}(A^{-1/2}q)$.
        Ce vecteur $x_0$ est défini à un facteur d'échelle près.

    *   c) Calculons la valeur maximale $R_{max}$ de $R(x)$.
        La valeur maximale de $R'(y)$ est $\|P_{F'}(q')\|^2$.
        Donc, $R_{max} = \|P_{F'}(q')\|^2$.
        En substituant $q' = A^{-1/2}q$ et $F' = A^{1/2}(F)$ :
        $R_{max} = \|P_{A^{1/2}(F)}(A^{-1/2}q)\|^2$.

    *   d) Interprétons géométriquement $x_0$ et $R_{max}$ en termes de "proximité" dans l'espace $(E, (\cdot, \cdot)_A)$.
        Rappelons que le problème est de maximiser $R(x) = \frac{\langle q, x \rangle^2}{\langle x, Ax \rangle}$ pour $x \in F \setminus \{0\}$.
        Nous avons montré que $(\cdot, \cdot)_A$ est un produit scalaire sur $E$.
        Considérons la forme linéaire $f_q: E \to \mathbb{R}$ définie par $f_q(x) = \langle q, x \rangle$.
        D'après le théorème de représentation de Riesz pour le produit scalaire $(\cdot, \cdot)_A$, il existe un unique vecteur $v_q \in E$ tel que $f_q(x) = (x, v_q)_A$ pour tout $x \in E$.
        C'est-à-dire $\langle q, x \rangle = \langle x, Av_q \rangle$.
        Par symétrie de la forme bilinéaire du produit scalaire standard, $\langle q, x \rangle = \langle Av_q, x \rangle$.
        Puisque cette égalité doit être vraie pour tout $x \in E$, on doit avoir $q = Av_q$.
        Puisque $A$ est inversible (car positif défini), $v_q = A^{-1}q$.
        Ainsi, la fonction de pertinence peut s'écrire :
        $R(x) = \frac{(x, A^{-1}q)_A^2}{\|x\|_A^2}$.
        Cette expression est le carré du cosinus de l'angle entre $x$ et $A^{-1}q$ dans l'espace euclidien $(E, (\cdot, \cdot)_A)$.
        Plus précisément, si $\theta_A(x, A^{-1}q)$ est l'angle entre $x$ et $A^{-1}q$ dans l'espace $(E, (\cdot, \cdot)_A)$, alors $R(x) = \cos^2(\theta_A(x, A^{-1}q))$.
        Maximiser $R(x)$ revient donc à maximiser $\cos^2(\theta_A(x, A^{-1}q))$, ce qui est équivalent à minimiser l'angle $\theta_A(x, A^{-1}q)$.
        Le vecteur $x_0 \in F \setminus \{0\}$ qui minimise l'angle avec $A^{-1}q$ (dans l'espace $(E, (\cdot, \cdot)_A)$) est la projection orthogonale de $A^{-1}q$ sur $F$ par rapport au produit scalaire $(\cdot, \cdot)_A$.
        On note cette projection $P_F^A(A^{-1}q)$.
        Donc, $x_0 = P_F^A(A^{-1}q)$ (à un facteur d'échelle près).
        La valeur maximale $R_{max}$ est alors $\cos^2(\theta_A(P_F^A(A^{-1}q), A^{-1}q))$.
        Puisque $P_F^A(A^{-1}q)$ est la projection de $A^{-1}q$ sur $F$, l'angle entre $P_F^A(A^{-1}q)$ et $A^{-1}q$ est le plus petit possible.
        La valeur maximale est $\|P_F^A(A^{-1}q)\|_A^2$.
        En effet, si $x_0 = P_F^A(A^{-1}q)$, alors $(x_0, A^{-1}q)_A = (x_0, x_0)_A = \|x_0\|_A^2$.
        Donc $R_{max} = \frac{\|x_0\|_A^4}{\|x_0\|_A^2} = \|x_0\|_A^2$.
        Géométriquement, $x_0$ est le vecteur dans le sous-espace $F$ qui est le "plus proche" de $A^{-1}q$ en termes d'angle dans la géométrie définie par l'opérateur $A$. $R_{max}$ représente le carré de la norme de cette projection dans la métrique $A$.

### Conclusion
Le vecteur $x_0 \in F \setminus \{0\}$ qui maximise la fonction de pertinence sémantique généralisée $R(x) = \frac{\langle q, x \rangle^2}{\langle x, Ax \rangle}$ est donné par :
$$x_0 = A^{-1/2}P_{A^{1/2}(F)}(A^{-1/2}q)$$
où $P_{A^{1/2}(F)}$ est l'opérateur de projection orthogonale sur le sous-espace $A^{1/2}(F)$ par rapport au produit scalaire euclidien standard $\langle \cdot, \cdot \rangle$.

La valeur maximale de $R(x)$ est :
$$R_{max} = \|P_{A^{1/2}(F)}(A^{-1/2}q)\|^2$$

Géométriquement, $x_0$ est le vecteur (à un facteur d'échelle près) dans le sous-espace $F$ qui minimise l'angle avec le vecteur $A^{-1}q$ dans l'espace euclidien $(E, (\cdot, \cdot)_A)$, où $(\cdot, \cdot)_A$ est le produit scalaire défini par $\langle u, Av \rangle$. La valeur maximale $R_{max}$ est le carré de la norme de cette projection $A$-orthogonale de $A^{-1}q$ sur $F$, c'est-à-dire $\|P_F^A(A^{-1}q)\|_A^2$.
