Madame, Monsieur, chers étudiants,

En ma qualité de Professeur Émérite de Mathématiques, j'ai l'honneur de vous présenter cet Exercice 10, de difficulté 5 étoiles, conçu pour approfondir votre compréhension des fondements mathématiques sous-jacents à la conception de moteurs de recherche sémantiques. Cet exercice se situe au cœur du Jalon 12 de votre parcours IA T1 et explore la dualité et la géométrie des espaces de plongement en lien avec la similarité cosinus. Il emprunte la rigueur et la structure d'un problème classique d'algèbre de l'École Polytechnique.

---

## Exercice 10 : Optimisation d'un Vecteur de Requête Sémantique par Dualité et Géométrie des Espaces de Plongement

**Contexte :**
Dans le domaine de l'intelligence artificielle, et plus particulièrement du traitement automatique du langage naturel (TALN), les mots, phrases ou documents sont souvent représentés par des vecteurs numériques dans des espaces de grande dimension, appelés "espaces de plongement" (embedding spaces). La "similarité sémantique" entre deux entités est alors fréquemment quantifiée par la similarité cosinus entre leurs vecteurs de plongement. Cet exercice vise à formaliser la notion d'un "vecteur de requête optimal" à partir d'exemples de documents jugés pertinents ou non pertinents, en explorant les liens fondamentaux entre la géométrie euclidienne et les concepts de dualité linéaire.

---

### Énoncé Détaillé

Soit $E$ un $\mathbb{R}$-espace vectoriel de dimension finie $n \ge 1$. On munit $E$ d'un produit scalaire $\langle \cdot, \cdot \rangle : E \times E \to \mathbb{R}$, et de la norme euclidienne associée $\|x\| = \sqrt{\langle x, x \rangle}$ pour tout $x \in E$.
On note $E^*$ l'espace dual de $E$, qui est l'ensemble des formes linéaires $f: E \to \mathbb{R}$.

**Partie I : Représentation Sémantique et Similarité Cosinus**

1.  **Définition de l'Espace de Plongement et des Vecteurs Normalisés :**
    Un document (ou une requête) est représenté par un vecteur $x \in E$. La "direction sémantique" est souvent plus importante que l'amplitude du vecteur.
    On définit la sphère unité $S(E) = \{x \in E \mid \|x\|=1\}$.
    Expliquer pourquoi, dans le contexte de la similarité cosinus, il est courant de normaliser les vecteurs, c'est-à-dire de les projeter sur $S(E)$. Préciser la formule de normalisation pour un vecteur non nul $x \in E$.

2.  **Définition de la Similarité Cosinus :**
    Soient $u$ et $v$ deux vecteurs non nuls de $E$.
    Définir la similarité cosinus $\text{sim}_{\text{cos}}(u, v)$ entre $u$ et $v$.
    Montrer que si $u'$ et $v'$ sont les versions normalisées de $u$ et $v$ respectivement, alors $\text{sim}_{\text{cos}}(u, v) = \langle u', v' \rangle$.
    Interpréter géométriquement la similarité cosinus en termes d'angle. Préciser le domaine de valeurs de $\text{sim}_{\text{cos}}(u, v)$.

**Partie II : Dualité et Requêtes Sémantiques**

1.  **Isomorphisme de Riesz :**
    Pour tout vecteur $v \in E$, on définit l'application $\phi_v : E \to \mathbb{R}$ par $\phi_v(x) = \langle v, x \rangle$ pour tout $x \in E$.
    Montrer que $\phi_v$ est une forme linéaire, c'est-à-dire $\phi_v \in E^*$.
    Montrer que l'application $\Phi : E \to E^*$ définie par $\Phi(v) = \phi_v$ est un isomorphisme d'espaces vectoriels. (C'est l'isomorphisme de Riesz en dimension finie).

2.  **Requêtes comme Formes Linéaires :**
    Dans un moteur de recherche sémantique, une requête peut être conçue comme un vecteur $q \in E$. Cependant, elle peut aussi être vue comme une "fonction d'évaluation" sur les documents.
    En utilisant l'isomorphisme de Riesz, expliquer comment une requête $q \in E$ peut naturellement être interprétée comme une forme linéaire $\phi_q \in E^*$ qui évalue la pertinence d'un document $d \in E$.
    Quel est le lien entre l'évaluation $\phi_q(d)$ et la similarité cosinus $\text{sim}_{\text{cos}}(q, d)$ si $q$ et $d$ sont normalisés ?

**Partie III : Optimisation d'un Vecteur de Requête à partir d'Exemples**

Considérons deux ensembles finis non vides de vecteurs de documents normalisés sur $S(E)$:
*   $P = \{p_1, p_2, \dots, p_k\} \subset S(E)$ est l'ensemble des "documents positifs" (jugés pertinents).
*   $N = \{n_1, n_2, \dots, n_m\} \subset S(E)$ est l'ensemble des "documents négatifs" (jugés non pertinents).
Un vecteur de requête optimal $q_0 \in S(E)$ est recherché tel qu'il maximise la différence moyenne de similarité cosinus entre les documents positifs et négatifs.

1.  **Formulation du Problème d'Optimisation :**
    On définit la fonction objectif $J: S(E) \to \mathbb{R}$ par :
    $$J(q) = \left( \frac{1}{k} \sum_{i=1}^k \langle q, p_i \rangle \right) - \left( \frac{1}{m} \sum_{j=1}^m \langle q, n_j \rangle \right)$$
    L'objectif est de trouver $q_0 \in S(E)$ tel que $J(q_0) = \sup_{q \in S(E)} J(q)$.

    a.  **Simplification de $J(q)$ :**
        On introduit les vecteurs centroïdes $c_P = \frac{1}{k} \sum_{i=1}^k p_i \in E$ et $c_N = \frac{1}{m} \sum_{j=1}^m n_j \in E$.
        Montrer que $J(q)$ peut être réécrit sous la forme $J(q) = \langle q, c_P - c_N \rangle$.

    b.  **Existence et Unicité de $q_0$ :**
        On pose $v = c_P - c_N \in E$.
        On suppose dans un premier temps que $v \ne 0_E$ (où $0_E$ est le vecteur nul de $E$).
        Montrer, en utilisant l'inégalité de Cauchy-Schwarz, que l'optimum $q_0$ existe et est unique.
        Déterminer l'expression de $q_0$ en fonction de $v$.

    c.  **Cas $v = 0_E$ :**
        Que se passe-t-il si $v = 0_E$? Dans ce cas, les centroïdes des documents positifs et négatifs sont identiques.
        Quelle est la valeur de $J(q)$ pour tout $q \in S(E)$?
        Le problème d'optimisation admet-il toujours un unique optimum $q_0$? Justifier rigoureusement.

2.  **Interprétation Géométrique et Sémantique :**
    Supposons que $v \ne 0_E$.

    a.  **Direction Optimale :**
        Décrire géométriquement la direction du vecteur $q_0$ par rapport aux centroïdes $c_P$ et $c_N$.
        Interpréter cette direction optimale $q_0$ dans le contexte de la recherche sémantique : pourquoi ce vecteur est-il un bon candidat pour une requête distinguant $P$ de $N$?

    b.  **Hyperplan de Séparation :**
        L'hyperplan $H = \{x \in E \mid \langle q_0, x \rangle = 0 \}$ sépare l'espace en deux demi-espaces.
        Quelle est la signification de $\langle q_0, x \rangle$ pour un document $x \in S(E)$ par rapport à cet hyperplan?
        Décrire la position relative des centroïdes $c_P$ et $c_N$ par rapport à cet hyperplan $H$.
        Expliquer comment ce vecteur $q_0$ peut être utilisé pour classer un nouveau document $d_{nouveau} \in S(E)$ comme "positif" ou "négatif".

    c.  **Lien avec la Dualité :**
        En utilisant l'isomorphisme de Riesz $\Phi$, quelle forme linéaire $\phi_{q_0} \in E^*$ correspond au vecteur de requête optimal $q_0$?
        Comment l'évaluation $\phi_{q_0}(x)$ d'un document $x \in E$ peut-elle être interprétée comme un "score de pertinence" par rapport à cette requête optimale?

---

### Correction Détaillée

**Partie I : Représentation Sémantique et Similarité Cosinus**

1.  **Définition de l'Espace de Plongement et des Vecteurs Normalisés :**
    Un vecteur $x \in E$ représente une entité sémantique. Dans le cadre de la similarité cosinus, l'orientation du vecteur dans l'espace est primordiale car elle encode le "sens" ou la "caractéristique" sémantique. La magnitude (norme) du vecteur est souvent considérée comme moins pertinente ou peut introduire un biais lié à la fréquence ou à la longueur du document plutôt qu'à son contenu intrinsèque. Normaliser les vecteurs permet de projeter tous les vecteurs non nuls sur la sphère unité $S(E)$, où la distance angulaire (et donc la similarité cosinus) devient la mesure unique de la proximité sémantique.
    Pour un vecteur non nul $x \in E$, sa version normalisée $x' \in S(E)$ est donnée par :
    $$x' = \frac{x}{\|x\|}$$

2.  **Définition de la Similarité Cosinus :**
    Soient $u$ et $v$ deux vecteurs non nuls de $E$. La similarité cosinus $\text{sim}_{\text{cos}}(u, v)$ est définie par :
    $$\text{sim}_{\text{cos}}(u, v) = \frac{\langle u, v \rangle}{\|u\| \|v\|}$$
    Démontrons que si $u'$ et $v'$ sont les versions normalisées de $u$ et $v$ respectivement, alors $\text{sim}_{\text{cos}}(u, v) = \langle u', v' \rangle$.
    Par définition, $u' = \frac{u}{\|u\|}$ et $v' = \frac{v}{\|v\|}$.
    Alors :
    $$\langle u', v' \rangle = \left\langle \frac{u}{\|u\|}, \frac{v}{\|v\|} \right\rangle$$
    Par bilinéarité du produit scalaire :
    $$\langle u', v' \rangle = \frac{1}{\|u\| \|v\|} \langle u, v \rangle$$
    Ce qui est précisément la définition de $\text{sim}_{\text{cos}}(u, v)$.
    Géométriquement, la similarité cosinus est le cosinus de l'angle $\theta$ entre les vecteurs $u$ et $v$, où $\theta \in [0, \pi]$. En effet, par définition de l'angle entre deux vecteurs dans un espace euclidien :
    $$\cos(\theta) = \frac{\langle u, v \rangle}{\|u\| \|v\|}$$
    Le domaine de valeurs de $\text{sim}_{\text{cos}}(u, v)$ est donc $[-1, 1]$.
    *   Une valeur de $1$ indique que les vecteurs sont colinéaires et de même direction (angle de $0$).
    *   Une valeur de $-1$ indique que les vecteurs sont colinéaires et de directions opposées (angle de $\pi$).
    *   Une valeur de $0$ indique que les vecteurs sont orthogonaux (angle de $\pi/2$).

**Partie II : Dualité et Requêtes Sémantiques**

1.  **Isomorphisme de Riesz :**
    Pour tout vecteur $v \in E$, on a défini $\phi_v : E \to \mathbb{R}$ par $\phi_v(x) = \langle v, x \rangle$.
    Montrons que $\phi_v$ est une forme linéaire. Pour cela, nous devons prouver la linéarité, c'est-à-dire que pour tout $x_1, x_2 \in E$ et tout $\alpha, \beta \in \mathbb{R}$ :
    $$\phi_v(\alpha x_1 + \beta x_2) = \alpha \phi_v(x_1) + \beta \phi_v(x_2)$$
    Par définition de $\phi_v$:
    $$\phi_v(\alpha x_1 + \beta x_2) = \langle v, \alpha x_1 + \beta x_2 \rangle$$
    Par la bilinéarité du produit scalaire (spécifiquement la linéarité par rapport au second argument) :
    $$\langle v, \alpha x_1 + \beta x_2 \rangle = \alpha \langle v, x_1 \rangle + \beta \langle v, x_2 \rangle$$
    Par définition de $\phi_v$:
    $$\alpha \langle v, x_1 \rangle + \beta \langle v, x_2 \rangle = \alpha \phi_v(x_1) + \beta \phi_v(x_2)$$
    Donc, $\phi_v$ est bien une forme linéaire, ce qui signifie $\phi_v \in E^*$.

    Montrons que l'application $\Phi : E \to E^*$ définie par $\Phi(v) = \phi_v$ est un isomorphisme d'espaces vectoriels.
    Nous devons prouver que $\Phi$ est linéaire, injective et surjective.

    *   **Linéarité de $\Phi$ :**
        Pour tout $v_1, v_2 \in E$ et tout $\alpha, \beta \in \mathbb{R}$, nous devons montrer que $\Phi(\alpha v_1 + \beta v_2) = \alpha \Phi(v_1) + \beta \Phi(v_2)$.
        Cela signifie que pour tout $x \in E$:
        $$(\Phi(\alpha v_1 + \beta v_2))(x) = (\alpha \Phi(v_1) + \beta \Phi(v_2))(x)$$
        Par définition de $\Phi$:
        $$(\Phi(\alpha v_1 + \beta v_2))(x) = \langle \alpha v_1 + \beta v_2, x \rangle$$
        Par la bilinéarité du produit scalaire (spécifiquement la linéarité par rapport au premier argument) :
        $$\langle \alpha v_1 + \beta v_2, x \rangle = \alpha \langle v_1, x \rangle + \beta \langle v_2, x \rangle$$
        Par définition de $\phi_{v_1}$ et $\phi_{v_2}$:
        $$\alpha \langle v_1, x \rangle + \beta \langle v_2, x \rangle = \alpha \phi_{v_1}(x) + \beta \phi_{v_2}(x)$$
        Enfin, par définition de l'addition et de la multiplication scalaire dans $E^*$:
        $$\alpha \phi_{v_1}(x) + \beta \phi_{v_2}(x) = (\alpha \phi_{v_1} + \beta \phi_{v_2})(x) = (\alpha \Phi(v_1) + \beta \Phi(v_2))(x)$$
        Donc, $\Phi$ est linéaire.

    *   **Injectivité de $\Phi$ :**
        Nous devons montrer que $\ker(\Phi) = \{0_E\}$. Soit $v \in \ker(\Phi)$. Alors $\Phi(v) = 0_{E^*}$, ce qui signifie que $\phi_v$ est la forme linéaire nulle.
        Ainsi, pour tout $x \in E$, $\phi_v(x) = \langle v, x \rangle = 0$.
        En particulier, en prenant $x = v$, on a $\langle v, v \rangle = 0$, ce qui implique $\|v\|^2 = 0$.
        Puisque la norme est définie positive, $\|v\| = 0$ implique $v = 0_E$.
        Donc, $\ker(\Phi) = \{0_E\}$, et $\Phi$ est injective.

    *   **Surjectivité de $\Phi$ :**
        Puisque $E$ est un $\mathbb{R}$-espace vectoriel de dimension finie $n$, son espace dual $E^*$ a également pour dimension $n$.
        Une application linéaire $\Phi: E \to E^*$ entre des espaces vectoriels de même dimension finie est surjective si et seulement si elle est injective.
        Ayant déjà montré que $\Phi$ est injective, il s'ensuit que $\Phi$ est également surjective.

    Puisque $\Phi$ est linéaire, injective et surjective, c'est un isomorphisme d'espaces vectoriels.

2.  **Requêtes comme Formes Linéaires :**
    Une requête $q \in E$ peut être naturellement interprétée comme une forme linéaire $\phi_q = \Phi(q) \in E^*$ via l'isomorphisme de Riesz. Cette forme linéaire $\phi_q$ prend en entrée un vecteur document $d \in E$ et renvoie une valeur numérique $\phi_q(d) = \langle q, d \rangle$.
    Cette valeur $\langle q, d \rangle$ représente le "score de pertinence" du document $d$ par rapport à la requête $q$. Plus ce score est élevé, plus le document est jugé pertinent.

    Si $q$ et $d$ sont normalisés (c'est-à-dire $q \in S(E)$ et $d \in S(E)$), alors leurs normes sont $\|q\|=1$ et $\|d\|=1$.
    Dans ce cas, la similarité cosinus est $\text{sim}_{\text{cos}}(q, d) = \frac{\langle q, d \rangle}{\|q\| \|d\|} = \frac{\langle q, d \rangle}{1 \cdot 1} = \langle q, d \rangle$.
    Le lien est donc direct : l'évaluation $\phi_q(d)$ de la forme linéaire $\phi_q$ sur le document normalisé $d$ est exactement la similarité cosinus entre $q$ et $d$.

**Partie III : Optimisation d'un Vecteur de Requête à partir d'Exemples**

1.  **Formulation du Problème d'Optimisation :**
    On rappelle la fonction objectif $J: S(E) \to \mathbb{R}$ :
    $$J(q) = \left( \frac{1}{k} \sum_{i=1}^k \langle q, p_i \rangle \right) - \left( \frac{1}{m} \sum_{j=1}^m \langle q, n_j \rangle \right)$$

    a.  **Simplification de $J(q)$ :**
        On a défini $c_P = \frac{1}{k} \sum_{i=1}^k p_i$ et $c_N = \frac{1}{m} \sum_{j=1}^m n_j$.
        En utilisant la linéarité du produit scalaire par rapport à son second argument :
        $$\frac{1}{k} \sum_{i=1}^k \langle q, p_i \rangle = \left\langle q, \frac{1}{k} \sum_{i=1}^k p_i \right\rangle = \langle q, c_P \rangle$$
        De même :
        $$\frac{1}{m} \sum_{j=1}^m \langle q, n_j \rangle = \left\langle q, \frac{1}{m} \sum_{j=1}^m n_j \right\rangle = \langle q, c_N \rangle$$
        Donc, $J(q)$ peut être réécrit comme :
        $$J(q) = \langle q, c_P \rangle - \langle q, c_N \rangle$$
        Par la linéarité du produit scalaire par rapport à son second argument (ou la distributivité) :
        $$J(q) = \langle q, c_P - c_N \rangle$$

    b.  **Existence et Unicité de $q_0$ :**
        On pose $v = c_P - c_N$. Nous cherchons à maximiser $J(q) = \langle q, v \rangle$ sous la contrainte $\|q\|=1$.
        On suppose $v \ne 0_E$.
        L'inégalité de Cauchy-Schwarz stipule que pour tout $q, v \in E$:
        $$|\langle q, v \rangle| \le \|q\| \|v\|$$
        Et l'égalité a lieu si et seulement si $q$ et $v$ sont colinéaires, c'est-à-dire s'il existe $\lambda \in \mathbb{R}$ tel que $q = \lambda v$.
        Nous cherchons à maximiser $\langle q, v \rangle$, donc nous voulons que $\langle q, v \rangle$ soit positif et aussi grand que possible.
        Ainsi, nous avons $\langle q, v \rangle \le \|q\| \|v\|$.
        Comme $\|q\|=1$, on a $\langle q, v \rangle \le \|v\|$.
        L'égalité $\langle q, v \rangle = \|v\|$ est atteinte lorsque $q$ est dans la même direction que $v$.
        Puisque $q$ doit être un vecteur unitaire, l'unique vecteur $q_0 \in S(E)$ qui satisfait cette condition est :
        $$q_0 = \frac{v}{\|v\|}$$
        L'existence et l'unicité de $q_0$ sont garanties car $v \ne 0_E$ par hypothèse, ce qui assure que $\|v\| \ne 0$.
        La valeur maximale de $J(q)$ est alors $J(q_0) = \left\langle \frac{v}{\|v\|}, v \right\rangle = \frac{1}{\|v\|} \langle v, v \rangle = \frac{\|v\|^2}{\|v\|} = \|v\|$.

    c.  **Cas $v = 0_E$ :**
        Si $v = 0_E$, cela signifie que $c_P - c_N = 0_E$, c'est-à-dire $c_P = c_N$. Les centroïdes des documents positifs et négatifs sont identiques.
        Dans ce cas, $J(q) = \langle q, 0_E \rangle = 0$ pour tout $q \in S(E)$.
        La fonction objectif $J(q)$ est constante et égale à $0$ sur $S(E)$.
        Par conséquent, tout vecteur $q \in S(E)$ est un optimum, car $J(q)=0$ pour tous les $q \in S(E)$.
        Le problème d'optimisation admet alors une infinité de solutions (tous les vecteurs sur la sphère unité $S(E)$), et l'optimum $q_0$ n'est pas unique. Cela indique que les ensembles $P$ et $N$ ne peuvent pas être distingués efficacement par cette méthode si leurs centroïdes coïncident.

2.  **Interprétation Géométrique et Sémantique :**
    Supposons que $v \ne 0_E$.

    a.  **Direction Optimale :**
        Le vecteur $q_0 = \frac{v}{\|v\|} = \frac{c_P - c_N}{\|c_P - c_N\|}$ pointe dans la direction du vecteur différence entre le centroïde des documents positifs et le centroïde des documents négatifs.
        Géométriquement, $q_0$ est le vecteur unitaire qui va de $c_N$ vers $c_P$, si l'on imagine ces centroïdes comme des points dans l'espace.
        Dans le contexte de la recherche sémantique, $q_0$ représente la "direction sémantique" qui discrimine le mieux les documents positifs des documents négatifs. Un document qui a une forte similarité cosinus avec $q_0$ (c'est-à-dire $\langle q_0, d \rangle$ élevé) sera sémantiquement proche de la tendance "positive" et éloigné de la tendance "négative". C'est un excellent candidat pour une requête sémantique qui cherche à retrouver des documents similaires aux exemples positifs tout en évitant ceux similaires aux exemples négatifs.

    b.  **Hyperplan de Séparation :**
        L'hyperplan $H = \{x \in E \mid \langle q_0, x \rangle = 0 \}$ est l'ensemble de tous les vecteurs orthogonaux à $q_0$. C'est un sous-espace vectoriel de dimension $n-1$.
        Pour un document $x \in S(E)$, la valeur $\langle q_0, x \rangle$ est la similarité cosinus entre $q_0$ et $x$. Géométriquement, c'est la projection orthogonale de $x$ sur la droite vectorielle engendrée par $q_0$. Cette valeur représente une "mesure de pertinence" signée par rapport à la requête $q_0$.
        *   Si $\langle q_0, x \rangle > 0$, le document $x$ est dans le même demi-espace que $q_0$ (et donc que $c_P$ relativement à $c_N$).
        *   Si $\langle q_0, x \rangle < 0$, le document $x$ est dans le demi-espace opposé à $q_0$.
        *   Si $\langle q_0, x \rangle = 0$, le document $x$ est sur l'hyperplan $H$.

        Concernant les centroïdes $c_P$ et $c_N$:
        Puisque $q_0 = \frac{c_P - c_N}{\|c_P - c_N\|}$, on a $c_P - c_N = \|c_P - c_N\| q_0$.
        Alors $\langle q_0, c_P - c_N \rangle = \langle q_0, \|c_P - c_N\| q_0 \rangle = \|c_P - c_N\| \langle q_0, q_0 \rangle = \|c_P - c_N\| \|q_0\|^2 = \|c_P - c_N\|$.
        Comme $\|c_P - c_N\| > 0$ (car $v \ne 0_E$), on a $\langle q_0, c_P - c_N \rangle > 0$.
        Ceci implique $\langle q_0, c_P \rangle - \langle q_0, c_N \rangle > 0$, ou $\langle q_0, c_P \rangle > \langle q_0, c_N \rangle$.
        Cela signifie que le centroïde $c_P$ se situe dans le demi-espace positif par rapport à $H$ (là où les valeurs $\langle q_0, x \rangle$ sont positives), et le centroïde $c_N$ se situe dans le demi-espace "moins positif" (potentiellement négatif) par rapport à $H$. L'hyperplan $H$ "sépare" ces deux centroïdes.

        Pour classer un nouveau document $d_{nouveau} \in S(E)$:
        On calcule le score $\text{score}(d_{nouveau}) = \langle q_0, d_{nouveau} \rangle$.
        *   Si $\text{score}(d_{nouveau}) > 0$ (ou un seuil positif), le document est classé comme "positif".
        *   Si $\text{score}(d_{nouveau}) < 0$ (ou un seuil négatif), le document est classé comme "négatif".
        *   Si $\text{score}(d_{nouveau}) = 0$, le document est sur l'hyperplan et est considéré comme "neutre" ou "ambigu" par rapport à cette requête.

    c.  **Lien avec la Dualité :**
        En utilisant l'isomorphisme de Riesz $\Phi: E \to E^*$, le vecteur de requête optimal $q_0 \in E$ correspond à la forme linéaire $\phi_{q_0} = \Phi(q_0) \in E^*$.
        Cette forme linéaire est définie par $\phi_{q_0}(x) = \langle q_0, x \rangle$ pour tout $x \in E$.
        L'évaluation $\phi_{q_0}(x)$ d'un document $x \in E$ peut être interprétée directement comme un "score de pertinence" par rapport à la requête optimale $q_0$. Un score positif élevé indique une forte pertinence (similaire aux documents positifs), un score négatif indique une faible pertinence (similaire aux documents négatifs), et un score proche de zéro indique une pertinence neutre ou ambiguë. C'est précisément la valeur qui est maximisée pour les documents positifs et minimisée pour les documents négatifs en moyenne. Cette forme linéaire incarne le critère de distinction sémantique appris des exemples $P$ et $N$.

---

Cet exercice a permis de solidifier votre compréhension des espaces vectoriels euclidiens, de la dualité, de la géométrie des hyperplans, et d'appliquer ces concepts à un problème concret d'optimisation en intelligence artificielle, montrant comment une requête sémantique peut être construite de manière rigoureuse.