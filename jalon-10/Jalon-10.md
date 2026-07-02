## 1. Présentation du concept clé

Imaginez un cartographe qui, pour la première fois, explore une région inconnue. Il pourrait commencer par établir un système de coordonnées simple, basé sur les points cardinaux : "tant de kilomètres au nord, tant à l'est". C'est une base de référence naturelle, intuitive. Cependant, si cette région est dominée par une chaîne de montagnes orientée obliquement par rapport à son axe nord-sud, ou traversée par un fleuve sinueux, décrire les caractéristiques géographiques importantes (les crêtes, les vallées, le cours du fleuve) dans ce système initial peut s'avérer laborieux. Les coordonnées seraient complexes, les équations des lignes de force de la topographie alambiquées.

Le cartographe avisé réaliserait bientôt qu'il serait bien plus efficace d'aligner son système de coordonnées principal le long de la chaîne de montagnes, ou de l'axe général du fleuve. Les descriptions des éléments clés deviendraient alors d'une simplicité déconcertante : "le sommet est à telle altitude le long de l'axe de la crête", "le fleuve suit l'axe principal avec de légères déviations". Le paysage n'a pas changé, mais la *manière* de le décrire a été transformée. Ce processus de réorientation du cadre de référence est l'essence du **changement de base**. La **matrice de passage** est l'instrument précis qui permet de traduire les coordonnées d'un point du système initial vers le nouveau système, et inversement. C'est un dictionnaire universel, une clé de voûte pour passer d'une langue descriptive à une autre, sans altérer la réalité sous-jacente.

Dans le même esprit, considérons une carte topographique d'une ampleur colossale, couvrant un continent entier. Tenter d'analyser cette carte comme une entité monolithique serait une tâche herculéenne. Il est plus judicieux de la subdiviser en régions distinctes : les plaines de l'ouest, les montagnes du centre, les côtes de l'est. Chaque région, bien que faisant partie du tout, peut être étudiée avec ses propres spécificités, ses propres outils d'analyse, avant que les résultats ne soient réintégrés dans une compréhension globale. Cette approche modulaire est la philosophie des **matrices par blocs**. Elle permet de décomposer un problème de grande dimension, représenté par une matrice massive, en une collection de sous-problèmes plus petits et plus gérables, chacun étant encapsulé dans un "bloc". Les interactions entre ces blocs sont alors étudiées, permettant de reconstruire la solution du problème original avec une efficacité et une clarté accrues.

L'invention de ces concepts n'est pas le fruit du hasard, mais une réponse directe à la nécessité de simplifier l'analyse et le calcul. Certaines transformations géométriques ou physiques, qui apparaissent complexes dans une base arbitraire, se révèlent triviales dans une base spécialement choisie. Les matrices par blocs, quant à elles, sont une manifestation de la stratégie "diviser pour régner", essentielle pour aborder les systèmes de grande taille, qu'ils soient numériques, physiques ou informatiques.

## 2. Formalisation

Le passage de l'intuition à la rigueur exige une définition précise des objets et des opérations.

### A. Définitions Formelles

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n$, où $\mathbb{K}$ désigne un corps commutatif (par exemple, $\mathbb{R}$ ou $\mathbb{C}$).

1.  **Matrice de passage ($P_{\mathcal{B} \to \mathcal{B}'}$) :**
    Soient $\mathcal{B} = (e_1, e_2, \dots, e_n)$ et $\mathcal{B}' = (e'_1, e'_2, \dots, e'_n)$ deux bases ordonnées de l'espace vectoriel $E$.
    La matrice de passage de la base $\mathcal{B}$ à la base $\mathcal{B}'$, notée $P_{\mathcal{B} \to \mathcal{B}'}$, est la matrice dont les colonnes sont les coordonnées des vecteurs de la nouvelle base $\mathcal{B}'$ exprimées dans l'ancienne base $\mathcal{B}$.
    Formellement, si pour tout $j \in \{1, \dots, n\}$, le vecteur $e'_j$ s'écrit comme une combinaison linéaire des vecteurs de $\mathcal{B}$ :
    $$e'_j = \sum_{i=1}^{n} p_{ij} e_i$$
    alors la matrice $P_{\mathcal{B} \to \mathcal{B}'}$ est donnée par $P_{\mathcal{B} \to \mathcal{B}'} = (p_{ij})_{1 \le i,j \le n}$.
    Cette matrice est également la matrice de l'application identité $Id_E: E \to E$ relativement aux bases $\mathcal{B}'$ au départ et $\mathcal{B}$ à l'arrivée :
    $$P_{\mathcal{B} \to \mathcal{B}'} = \text{Mat}_{\mathcal{B}', \mathcal{B}}(Id_E)$$
    Puisque $\mathcal{B}$ et $\mathcal{B}'$ sont des bases, la matrice $P_{\mathcal{B} \to \mathcal{B}'}$ est toujours inversible.

2.  **Matrices par blocs :**
    Une matrice $M \in \mathcal{M}_{m,p}(\mathbb{K})$ peut être décomposée en sous-matrices, appelées blocs, en partitionnant ses lignes et ses colonnes.
    Par exemple, une matrice $M$ peut être écrite sous la forme :
    $$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$$
    où $A \in \mathcal{M}_{m_1, p_1}(\mathbb{K})$, $B \in \mathcal{M}_{m_1, p_2}(\mathbb{K})$, $C \in \mathcal{M}_{m_2, p_1}(\mathbb{K})$, et $D \in \mathcal{M}_{m_2, p_2}(\mathbb{K})$, avec $m_1+m_2=m$ et $p_1+p_2=p$.
    Les opérations matricielles (somme, produit) peuvent être effectuées sur ces blocs comme s'ils étaient des scalaires, à condition que les dimensions des blocs soient compatibles pour les opérations correspondantes.

### B. Théorèmes, Propositions & Lemmes

**Théorème 1 (Formule du changement de base pour un vecteur) :**
Soit $u \in E$ un vecteur. Soit $X = \text{Coord}_{\mathcal{B}}(u)$ la colonne des coordonnées de $u$ dans la base $\mathcal{B}$, et $X' = \text{Coord}_{\mathcal{B}'}(u)$ la colonne des coordonnées de $u$ dans la base $\mathcal{B}'$. Alors la relation entre ces coordonnées est donnée par :
$$X = P_{\mathcal{B} \to \mathcal{B}'} X'$$
Ceci signifie que pour obtenir les coordonnées de $u$ dans l'ancienne base $\mathcal{B}$ à partir de ses coordonnées dans la nouvelle base $\mathcal{B}'$, on multiplie par la matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$.

**Théorème 2 (Formule du changement de base pour un endomorphisme) :**
Soit $f \in \mathcal{L}(E)$ un endomorphisme de $E$. Soit $M = \text{Mat}_{\mathcal{B}}(f)$ la matrice de $f$ dans la base $\mathcal{B}$, et $M' = \text{Mat}_{\mathcal{B}'}(f)$ la matrice de $f$ dans la base $\mathcal{B}'$. Soit $P = P_{\mathcal{B} \to \mathcal{B}'}$ la matrice de passage de $\mathcal{B}$ à $\mathcal{B}'$. Alors la relation entre $M$ et $M'$ est donnée par :
$$M' = P^{-1} M P$$
Les matrices $M$ et $M'$ sont dites **semblables**. La relation de similitude est une relation d'équivalence.

## 3. Démonstrations

Chaque assertion mathématique requiert une preuve rigoureuse, dénuée de toute ambiguïté ou raccourci.

### Démonstration du Théorème 2 : Formule du changement de base pour un endomorphisme

Nous souhaitons établir l'égalité $M' = P^{-1} M P$.

1.  **Initialisation et Cadre des Objets :**
    *   Soit $u$ un vecteur arbitraire de l'espace vectoriel $E$.
    *   Soit $v = f(u)$ l'image de $u$ par l'endomorphisme $f$.
    *   Soient $X \in \mathcal{M}_{n,1}(\mathbb{K})$ la colonne des coordonnées de $u$ dans la base $\mathcal{B}$.
    *   Soient $Y \in \mathcal{M}_{n,1}(\mathbb{K})$ la colonne des coordonnées de $v$ dans la base $\mathcal{B}$.
    *   Soient $X' \in \mathcal{M}_{n,1}(\mathbb{K})$ la colonne des coordonnées de $u$ dans la base $\mathcal{B}'$.
    *   Soient $Y' \in \mathcal{M}_{n,1}(\mathbb{K})$ la colonne des coordonnées de $v$ dans la base $\mathcal{B}'$.
    *   Par définition de la matrice d'un endomorphisme dans une base donnée, nous avons les relations suivantes :
        *   $Y = M X$ (1) : les coordonnées de $v$ dans $\mathcal{B}$ sont obtenues en appliquant $M$ aux coordonnées de $u$ dans $\mathcal{B}$.
        *   $Y' = M' X'$ (2) : les coordonnées de $v$ dans $\mathcal{B}'$ sont obtenues en appliquant $M'$ aux coordonnées de $u$ dans $\mathcal{B}'$.
    *   Par définition de la matrice de passage $P = P_{\mathcal{B} \to \mathcal{B}'}$ (Théorème 1), nous avons les relations suivantes :
        *   $X = P X'$ (3) : les coordonnées de $u$ dans $\mathcal{B}$ sont obtenues à partir de ses coordonnées dans $\mathcal{B}'$ par multiplication par $P$.
        *   $Y = P Y'$ (4) : les coordonnées de $v$ dans $\mathcal{B}$ sont obtenues à partir de ses coordonnées dans $\mathcal{B}'$ par multiplication par $P$.

2.  **Substitution des Coordonnées de $v$ :**
    Nous partons de l'équation (1) :
    $Y = M X$
    Nous substituons l'expression de $Y$ donnée par l'équation (4) dans cette égalité :
    $P Y' = M X$

3.  **Substitution des Coordonnées de $u$ :**
    Nous substituons ensuite l'expression de $X$ donnée par l'équation (3) dans l'égalité obtenue à l'étape précédente :
    $P Y' = M (P X')$
    Par associativité de la multiplication matricielle, nous pouvons écrire :
    $P Y' = (M P) X'$

4.  **Isolement de $Y'$ :**
    Puisque $P$ est une matrice de passage entre deux bases, elle est nécessairement inversible. Nous pouvons donc multiplier l'égalité à gauche par $P^{-1}$ :
    $P^{-1} (P Y') = P^{-1} (M P X')$
    En utilisant l'associativité de la multiplication matricielle et la propriété de l'inverse ($P^{-1} P = I_n$, où $I_n$ est la matrice identité de taille $n \times n$) :
    $(P^{-1} P) Y' = (P^{-1} M P) X'$
    $I_n Y' = (P^{-1} M P) X'$
    $Y' = (P^{-1} M P) X'$

5.  **Conclusion par Unicité :**
    Nous avons obtenu l'expression $Y' = (P^{-1} M P) X'$.
    Or, par définition de la matrice $M'$ de l'endomorphisme $f$ dans la base $\mathcal{B}'$, nous avons $Y' = M' X'$ (équation (2)).
    Puisque cette égalité $Y' = (P^{-1} M P) X'$ doit être vraie pour tout vecteur $u \in E$ (et donc pour toute colonne de coordonnées $X'$ dans $\mathcal{B}'$), et que la matrice associée à un endomorphisme dans une base donnée est unique, nous en déduisons par identification :
    $M' = P^{-1} M P$.
    La démonstration est achevée.

## 4. Exercices d'Application

La maîtrise des concepts s'acquiert par la pratique rigoureuse.

### Exercice 1 : Application Directe (Coordonnées dans une nouvelle base)

**Énoncé :**
Dans l'espace vectoriel $\mathbb{R}^2$ muni de la base canonique $\mathcal{B} = (e_1, e_2)$, où $e_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ et $e_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, on considère une nouvelle base $\mathcal{B}' = (e'_1, e'_2)$ définie par les vecteurs $e'_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ et $e'_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
Soit $u$ un vecteur de $\mathbb{R}^2$ dont les coordonnées dans la base canonique $\mathcal{B}$ sont $X = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$.
Calculer les coordonnées $X'$ du vecteur $u$ dans la base $\mathcal{B}'$.

**Correction Détaillée :**

1.  **Construction de la matrice de passage $P_{\mathcal{B} \to \mathcal{B}'}$ :**
    Par définition, les colonnes de la matrice de passage $P_{\mathcal{B} \to \mathcal{B}'}$ sont les coordonnées des vecteurs de la nouvelle base $\mathcal{B}'$ exprimées dans l'ancienne base $\mathcal{B}$.
    Les vecteurs $e'_1$ et $e'_2$ sont déjà donnés en coordonnées dans la base canonique $\mathcal{B}$.
    Ainsi, $e'_1 = 1 \cdot e_1 + 1 \cdot e_2$ et $e'_2 = 1 \cdot e_1 + (-1) \cdot e_2$.
    La matrice de passage est donc :
    $$P_{\mathcal{B} \to \mathcal{B}'} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

2.  **Formule de changement de coordonnées :**
    Le Théorème 1 établit la relation $X = P_{\mathcal{B} \to \mathcal{B}'} X'$.
    Pour trouver $X'$, nous devons inverser cette relation : $X' = (P_{\mathcal{B} \to \mathcal{B}'})^{-1} X$.

3.  **Calcul de l'inverse de la matrice de passage $(P_{\mathcal{B} \to \mathcal{B}'})^{-1}$ :**
    Pour une matrice $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, son déterminant est $\det(A) = ad - bc$. Si $\det(A) \ne 0$, alors $A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
    Calculons le déterminant de $P_{\mathcal{B} \to \mathcal{B}'}$ :
    $\det(P_{\mathcal{B} \to \mathcal{B}'}) = (1) \cdot (-1) - (1) \cdot (1) = -1 - 1 = -2$.
    Puisque $\det(P_{\mathcal{B} \to \mathcal{B}'}) = -2 \ne 0$, la matrice est inversible.
    Calculons son inverse :
    $$(P_{\mathcal{B} \to \mathcal{B}'})^{-1} = \frac{1}{-2} \begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{-1}{-2} & \frac{-1}{-2} \\ \frac{-1}{-2} & \frac{1}{-2} \end{pmatrix} = \begin{pmatrix} 0.5 & 0.5 \\ 0.5 & -0.5 \end{pmatrix}$$

4.  **Calcul des coordonnées $X'$ :**
    Nous appliquons la formule $X' = (P_{\mathcal{B} \to \mathcal{B}'})^{-1} X$ :
    $$X' = \begin{pmatrix} 0.5 & 0.5 \\ 0.5 & -0.5 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \end{pmatrix}$$
    Effectuons la multiplication matricielle :
    $$X' = \begin{pmatrix} (0.5 \cdot 4) + (0.5 \cdot 2) \\ (0.5 \cdot 4) + (-0.5 \cdot 2) \end{pmatrix} = \begin{pmatrix} 2 + 1 \\ 2 - 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$$

**Conclusion :**
Les coordonnées du vecteur $u$ dans la base $\mathcal{B}'$ sont $X' = \begin{pmatrix} 3 \\ 1 \end{pmatrix}$. Cela signifie que $u = 3e'_1 + 1e'_2$.
Vérification : $3e'_1 + 1e'_2 = 3 \begin{pmatrix} 1 \\ 1 \end{pmatrix} + 1 \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix} + \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 3+1 \\ 3-1 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$, ce qui correspond bien aux coordonnées de $u$ dans la base canonique.

### Exercice 2 : Niveau Avancé (Matrice par blocs et Inverse)

**Énoncé :**
Soit $M$ une matrice carrée de taille $(n+m) \times (n+m)$ sur le corps $\mathbb{K}$, décomposée en blocs de la manière suivante :
$$M = \begin{pmatrix} A & B \\ 0_{m,n} & D \end{pmatrix}$$
où $A \in \mathcal{M}_{n,n}(\mathbb{K})$ est une matrice carrée de taille $n$, $B \in \mathcal{M}_{n,m}(\mathbb{K})$ est une matrice rectangulaire de taille $n \times m$, $0_{m,n} \in \mathcal{M}_{m,n}(\mathbb{K})$ est la matrice nulle de taille $m \times n$, et $D \in \mathcal{M}_{m,m}(\mathbb{K})$ est une matrice carrée de taille $m$.
On suppose que les matrices $A$ et $D$ sont toutes deux inversibles.
Démontrer que la matrice $M$ est inversible et exprimer son inverse $M^{-1}$ sous forme de blocs.

**Correction Détaillée :**

1.  **Hypothèse d'inversibilité et forme de l'inverse :**
    Nous cherchons une matrice $M^{-1}$ de même taille que $M$, décomposée en blocs, telle que $M M^{-1} = I_{n+m}$, où $I_{n+m}$ est la matrice identité de taille $(n+m) \times (n+m)$.
    Soit $M^{-1}$ la matrice que nous cherchons, décomposée en blocs de dimensions compatibles :
    $$M^{-1} = \begin{pmatrix} X & Y \\ Z & W \end{pmatrix}$$
    où $X \in \mathcal{M}_{n,n}(\mathbb{K})$, $Y \in \mathcal{M}_{n,m}(\mathbb{K})$, $Z \in \mathcal{M}_{m,n}(\mathbb{K})$, et $W \in \mathcal{M}_{m,m}(\mathbb{K})$.
    La matrice identité $I_{n+m}$ peut également être décomposée en blocs :
    $$I_{n+m} = \begin{pmatrix} I_n & 0_{n,m} \\ 0_{m,n} & I_m \end{pmatrix}$$

2.  **Calcul du produit $M M^{-1}$ par blocs :**
    Nous effectuons la multiplication matricielle par blocs :
    $$\begin{pmatrix} A & B \\ 0_{m,n} & D \end{pmatrix} \begin{pmatrix} X & Y \\ Z & W \end{pmatrix} = \begin{pmatrix} (A X + B Z) & (A Y + B W) \\ (0_{m,n} X + D Z) & (0_{m,n} Y + D W) \end{pmatrix}$$
    Simplifions les termes impliquant la matrice nulle :
    $$M M^{-1} = \begin{pmatrix} A X + B Z & A Y + B W \\ D Z & D W \end{pmatrix}$$

3.  **Identification avec la matrice identité par blocs :**
    Nous égalons le résultat du produit $M M^{-1}$ à la matrice identité $I_{n+m}$ :
    $$\begin{pmatrix} A X + B Z & A Y + B W \\ D Z & D W \end{pmatrix} = \begin{pmatrix} I_n & 0_{n,m} \\ 0_{m,n} & I_m \end{pmatrix}$$
    Cette égalité matricielle par blocs conduit à un système de quatre équations matricielles :
    (a) $A X + B Z = I_n$
    (b) $A Y + B W = 0_{n,m}$
    (c) $D Z = 0_{m,n}$
    (d) $D W = I_m$

4.  **Résolution du système d'équations pour trouver $X, Y, Z, W$ :**

    *   **À partir de l'équation (c) :** $D Z = 0_{m,n}$
        Puisque $D$ est une matrice inversible (par hypothèse), nous pouvons multiplier cette équation à gauche par $D^{-1}$ :
        $D^{-1} (D Z) = D^{-1} 0_{m,n}$
        $(D^{-1} D) Z = 0_{m,n}$
        $I_m Z = 0_{m,n}$
        $Z = 0_{m,n}$

    *   **À partir de l'équation (d) :** $D W = I_m$
        Puisque $D$ est inversible, nous pouvons multiplier cette équation à gauche par $D^{-1}$ :
        $D^{-1} (D W) = D^{-1} I_m$
        $(D^{-1} D) W = D^{-1}$
        $I_m W = D^{-1}$
        $W = D^{-1}$

    *   **À partir de l'équation (a) :** $A X + B Z = I_n$
        Nous substituons la valeur de $Z = 0_{m,n}$ que nous venons de trouver :
        $A X + B (0_{m,n}) = I_n$
        $A X + 0_{n,n} = I_n$
        $A X = I_n$
        Puisque $A$ est une matrice inversible (par hypothèse), nous pouvons multiplier cette équation à gauche par $A^{-1}$ :
        $A^{-1} (A X) = A^{-1} I_n$
        $(A^{-1} A) X = A^{-1}$
        $I_n X = A^{-1}$
        $X = A^{-1}$

    *   **À partir de l'équation (b) :** $A Y + B W = 0_{n,m}$
        Nous substituons la valeur de $W = D^{-1}$ que nous avons trouvée :
        $A Y + B D^{-1} = 0_{n,m}$
        Nous isolons le terme $A Y$ :
        $A Y = -B D^{-1}$
        Puisque $A$ est une matrice inversible, nous pouvons multiplier cette équation à gauche par $A^{-1}$ :
        $A^{-1} (A Y) = A^{-1} (-B D^{-1})$
        $(A^{-1} A) Y = -A^{-1} B D^{-1}$
        $I_n Y = -A^{-1} B D^{-1}$
        $Y = -A^{-1} B D^{-1}$

5.  **Conclusion :**
    Nous avons trouvé des expressions uniques pour tous les blocs $X, Y, Z, W$. Cela démontre que la matrice $M$ est inversible, et son inverse $M^{-1}$ est donnée par :
    $$M^{-1} = \begin{pmatrix} A^{-1} & -A^{-1} B D^{-1} \\ 0_{m,n} & D^{-1} \end{pmatrix}$$

## 5. Application en Intelligence Artificielle

Les concepts de changement de base et de matrices par blocs ne sont pas de simples abstractions mathématiques ; ils constituent le socle de nombreuses techniques fondamentales en intelligence artificielle, permettant de transformer des données brutes en représentations plus significatives et plus efficaces pour l'apprentissage et l'analyse.

Le **changement de base** est au cœur de l'**extraction de caractéristiques (Feature Engineering)** et de la **réduction de dimensionnalité**. Dans de nombreux problèmes d'apprentissage automatique, les données initiales (par exemple, les valeurs de pixels d'une image, les mots d'un texte) résident dans un espace de très haute dimension, où les motifs pertinents sont souvent noyés dans le bruit ou exprimés de manière redondante. En changeant de base, on projette ces données dans un nouvel espace où les caractéristiques discriminantes sont amplifiées, les corrélations sont simplifiées, et la dimensionnalité peut être réduite sans perte significative d'information. C'est une transformation du "point de vue" sur les données pour en révéler la structure intrinsèque.

Un exemple emblématique de cette application est la **compression d'images JPEG**, qui repose sur la **Transformée en Cosinus Discrète (DCT)**. La DCT est un changement de base orthogonal qui transforme un signal (ici, les valeurs de pixels) du domaine spatial (où chaque pixel a une position) vers le domaine fréquentiel (où chaque coefficient représente l'amplitude d'une certaine fréquence spatiale).
Le processus se déroule comme suit :
1.  **Découpage par blocs :** L'image est d'abord divisée en petits blocs de pixels, généralement de taille $8 \times 8$. Cette étape illustre parfaitement l'utilisation des **matrices par blocs** : chaque bloc est traité indépendamment, ce qui permet de gérer la complexité d'une image entière en la décomposant en sous-problèmes.
2.  **Application de la DCT :** Pour chaque bloc $8 \times 8$, une transformation de base est appliquée. La base de la DCT est composée de fonctions cosinus de différentes fréquences et orientations. Dans cette nouvelle base, l'information visuelle est "compactée" : les coefficients correspondant aux basses fréquences (qui représentent les grandes structures et les couleurs générales) ont généralement des amplitudes élevées, tandis que les coefficients des hautes fréquences (qui représentent les détails fins et les textures) ont des amplitudes plus faibles.
3.  **Quantification et compression :** C'est là que la compression a lieu. Les coefficients de haute fréquence, qui contribuent moins à la perception visuelle humaine et sont souvent associés au bruit, sont quantifiés de manière plus grossière (c'est-à-dire que leur précision est réduite, voire qu'ils sont mis à zéro). Cette opération est possible et efficace précisément parce que le changement de base a regroupé l'information essentielle dans un petit nombre de coefficients.
4.  **Encodage :** Les coefficients quantifiés sont ensuite encodés de manière efficace.

Ainsi, la compression JPEG est une démonstration éloquente de la synergie entre le changement de base (DCT) et les matrices par blocs (traitement par $8 \times 8$ blocs). Elle permet de réduire drastiquement la taille des fichiers images en éliminant les informations redondantes ou moins perceptibles, tout en préservant une qualité visuelle acceptable, en exploitant la capacité des changements de base à révéler la structure essentielle des données.

## 6. Liens Sémantiques

Les concepts abordés ici s'inscrivent dans une progression logique de l'algèbre linéaire et sont des prérequis indispensables à des notions plus avancées.

*   **Concepts Précédents requis :**
    *   [[Jalon-7.md|Jalon 7 (Espaces vectoriels abstraits)]] : Compréhension des espaces vectoriels, des bases et des coordonnées.
    *   [[Jalon-9.md|Jalon 9 (Applications linéaires et matrices)]] : Maîtrise des applications linéaires, de leur représentation matricielle et des opérations matricielles.

*   **Concepts Futurs dépendants :**
    *   [[Jalon 29 (Éléments propres)]] : La diagonalisation des matrices, qui est un cas particulier de changement de base où la matrice de l'endomorphisme devient diagonale, est fondamentale pour l'étude des valeurs et vecteurs propres.
    *   [[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.)]] : Ces techniques visent à simplifier la matrice d'un endomorphisme par un changement de base, même lorsque la diagonalisation n'est pas possible.
    *   [[Jalon 80 (Transformée de Fourier dans L^1)]] : La transformée de Fourier est une généralisation du concept de changement de base à des espaces de fonctions, transformant un signal du domaine temporel au domaine fréquentiel, essentielle en traitement du signal et en physique.

## Genèse Narrative

Le concept de changement de base...

## Énoncé Symbolique Strict

Soit $E$ un espace vectoriel...
