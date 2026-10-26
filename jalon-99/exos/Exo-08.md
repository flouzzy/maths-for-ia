# Exercice 8
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Ce problème montre comment la séparation des convexes permet de prouver l'existence d'équilibres dans les matrices de gains (Théorème du Minimax de von Neumann).
Soit $A$ une matrice $n \times m$ représentant les gains d'un jeu à somme nulle.
On note $S_n$ le simplexe des stratégies mixtes du joueur 1 (les vecteurs de probabilités dans $\mathbb{R}^n$) et $S_m$ celui du joueur 2.
Le gain espéré si le joueur 1 joue $x \in S_n$ et le joueur 2 joue $y \in S_m$ est $x^T A y$.
Si l'on définit la valeur "garantie" par le joueur 1 comme $v_1 = \max_{x \in S_n} \min_{y \in S_m} x^T A y$ et celle du joueur 2 comme $v_2 = \min_{y \in S_m} \max_{x \in S_n} x^T A y$.
Il est toujours vrai que $v_1 \le v_2$. L'objectif est de montrer, via Hahn-Banach sur des convexes, que $v_1 = v_2$ pour un jeu sans valeur connue a priori (supposons $v_1 < v_2$ par l'absurde).
On admet que si $v_1 = 0$, la condition $\forall x \in S_n, \exists y \in S_m, x^T A y < 0$ (déduite de $v_1 < 0$) implique que l'image de $S_n$ par $A^T$ et le quadrant positif de $\mathbb{R}^m$ sont séparables géométriquement.
Prouver que $v_1 < v_2$ mène à une contradiction par séparation d'ensembles convexes appropriés.

**Correction :**
1. **Simplification et traduction géométrique :**
   Quitte à ajouter une constante à tous les éléments de $A$ (ce qui ne change pas la dynamique du jeu), on peut supposer $v_1 < 0 < v_2$.
   L'hypothèse $v_1 < 0$ signifie : pour toute stratégie mixte $x \in S_n$, le vecteur des gains anticipés du joueur 1 contre les stratégies pures du joueur 2, noté $u = A^T x \in \mathbb{R}^m$, possède au moins une coordonnée strictement négative.
   Définissons l'ensemble de ces gains possibles pour le joueur 1 : $C_1 = \{ A^T x \in \mathbb{R}^m \mid x \in S_n \}$.
   $S_n$ étant l'enveloppe convexe canonique des vecteurs de la base canonique, c'est un convexe compact. L'image de ce convexe par l'application linéaire $x \mapsto A^T x$ est donc $C_1$, qui est un convexe compact de $\mathbb{R}^m$.
2. **Construction de l'ensemble adverse :**
   Considérons l'orthant positif fermé $C_2 = \mathbb{R}^m_+ = \{ u \in \mathbb{R}^m \mid u_i \ge 0 \text{ pour tout } i \}$.
   C'est un ensemble convexe, fermé (mais non compact).
   La condition "pour tout $x \in S_n$, $u = A^T x$ a au moins une composante strictement négative" se traduit géométriquement de manière très simple : aucun vecteur de $C_1$ ne se trouve entièrement dans le quadrant positif.
   Donc $C_1 \cap C_2 = \emptyset$.
3. **Application du théorème de Hahn-Banach géométrique :**
   Nous avons $C_1$ convexe compact, et $C_2$ convexe fermé, disjoints dans $\mathbb{R}^m$.
   Par la deuxième forme de Hahn-Banach, il existe un hyperplan séparant strictement $C_1$ et $C_2$.
   En dimension finie, cela signifie qu'il existe un vecteur $w \in \mathbb{R}^m$, $w \ne 0$, et un scalaire $\alpha$ tels que :
   $\forall u \in C_2, \, w^T u > \alpha$
   $\forall v \in C_1, \, w^T v < \alpha$
4. **Exploitation de la nature de l'orthant :**
   Puisque l'orthant $C_2$ est un cône (il contient $0$ et si $u \in C_2$, $\lambda u \in C_2$ pour $\lambda > 0$), la condition $w^T u > \alpha$ pour tout $\lambda u$ (avec $\lambda \to \infty$) exige que $w^T u \ge 0$ pour tout $u \in C_2$.
   En prenant $u$ égal aux vecteurs de la base canonique, on déduit que toutes les composantes de $w$ sont positives : $w_i \ge 0$ pour tout $i$.
   Comme $0 \in C_2$, on a $w^T 0 = 0 > \alpha$, donc $\alpha < 0$.
5. **Normalisation en stratégie de jeu :**
   Puisque $w \ne 0$ et $w_i \ge 0$, la somme de ses composantes est strictement positive : $S = \sum w_i > 0$.
   Définissons $y = \frac{1}{S} w$. Par construction, $y \in S_m$ (c'est une stratégie mixte valide pour le joueur 2).
   L'inégalité stricte pour $C_1$ donne : pour tout $v \in C_1$, $w^T v < \alpha < 0$.
   Comme $y = \frac{1}{S} w$ avec $S > 0$, l'inégalité reste vraie : $y^T v < 0$ pour tout $v \in C_1$.
6. **Obtention de la contradiction finale :**
   Revenons à la définition de $C_1$. Pour tout $x \in S_n$, le vecteur $v = A^T x$ est dans $C_1$.
   L'inégalité $y^T v < 0$ se traduit par $y^T (A^T x) < 0$, soit en transposant le scalaire : $(A y)^T x = x^T A y < 0$.
   Nous venons de prouver qu'il existe une stratégie $y \in S_m$ telle que, pour toute stratégie $x \in S_n$, $x^T A y < 0$.
   Mais cela contredit directement l'hypothèse de départ sur le joueur 2 : on avait supposé $v_2 > 0$, ce qui signifie que $\min_{y \in S_m} \max_{x \in S_n} x^T A y > 0$, donc que pour n'importe quelle stratégie $y$ du joueur 2, le joueur 1 pouvait trouver un $x$ tel que le gain $x^T A y$ soit strictement positif.
   L'absurdité prouve que $v_1$ ne peut être strictement inférieur à $v_2$. Le théorème du Minimax (et par là même, l'existence de l'équilibre de Nash pour les jeux à somme nulle) est une conséquence spectaculaire et directe du théorème de Hahn-Banach géométrique en dimension finie.
