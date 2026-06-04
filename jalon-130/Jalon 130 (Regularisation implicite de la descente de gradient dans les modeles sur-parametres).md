---
uuid: "jalon-130"
title: "Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés"
year: 3
trimester: 11
tags:
  - math/optimisation
  - math/analyse_fonctionnelle
  - ia/deep_learning
  - ia/generalisation
prev: "[[Jalon 129 (Optimisation stochastique)]]"
next: "[[Jalon 131 (Algorithmes d'optimisation de second ordre en grande dimension)]]"
---

# Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imagine que tu sois un sculpteur face à un immense bloc d'argile. Ton objectif est de façonner un visage précis (c'est l'objectif de ton modèle IA : apprendre à reconnaître des données). Le problème, c'est que tu as tellement d'argile (le modèle est "sur-paramétré") qu'il existe une infinité de façons de sculpter ce visage. Tu pourrais faire un visage avec un énorme nez, ou avec des oreilles pointues, tant que les traits principaux sont là. Mais toi, tu utilises un outil très simple, un petit burin qui enlève l'argile petit à petit (c'est la descente de gradient). Le fait d'utiliser cet outil t'oblige, sans que tu t'en rendes compte, à sculpter le visage le plus "lisse", le plus simple et le plus naturel possible, sans rajouter de détails farfelus.
- **Le "Pourquoi on a inventé ça" :** En Intelligence Artificielle, on s'est aperçu d'un phénomène très étrange : les réseaux de neurones gigantesques ont des milliards de paramètres. Mathématiquement, ils pourraient apprendre "par cœur" toutes les données (avec du bruit) et échouer lamentablement sur de nouvelles données (ce qu'on appelle le "surapprentissage" ou *overfitting*). Pourtant, ils généralisent très bien. Les mathématiciens ont dû inventer une théorie pour comprendre pourquoi : c'est parce que l'algorithme d'apprentissage lui-même (la descente de gradient) choisit *naturellement* la solution la plus "simple" parmi l'infinité de solutions possibles. L'algorithme a une préférence cachée, une "régularisation implicite".
- **Visualisation :** Imagine une feuille de papier posée sur une table, avec plein de points dessinés dessus. Tu cherches à relier tous les points. Il y a une infinité de gribouillis possibles qui passent par tous les points. Mais si tu tends un élastique pour relier ces points, l'élastique va prendre la forme la plus tendue, la plus courte possible. La descente de gradient agit exactement comme la tension de cet élastique.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles

**1. Cadre de l'apprentissage sur-paramétré linéaire :**
Soit $n \in \mathbb{N}^*$ le nombre de données et $d \in \mathbb{N}^*$ la dimension de l'espace des caractéristiques, avec le régime fortement sur-paramétré défini par $d > n$.
Soit $X \in \mathcal{M}_{n,d}(\mathbb{R})$ la matrice de conception (*design matrix*) où chaque ligne $x_i^\top \in \mathbb{R}^d$ ($i \in \{1, \dots, n\}$) représente une observation. Nous supposerons que la matrice $X$ est de rang plein en lignes, c'est-à-dire $\text{rg}(X) = n$.
Soit $y \in \mathbb{R}^n$ le vecteur des étiquettes (labels).
L'objectif est d'apprendre un vecteur de paramètres $w \in \mathbb{R}^d$ via un modèle linéaire $f_w(x) = \langle w, x \rangle = x^\top w$.

**2. Le problème d'optimisation :**
La fonction de perte empirique (moindres carrés) est définie par l'application :
$$ \mathcal{L} : \mathbb{R}^d \to \mathbb{R}_+ $$
$$ w \mapsto \mathcal{L}(w) = \frac{1}{2n} \|Xw - y\|_2^2 = \frac{1}{2n} \sum_{i=1}^n (x_i^\top w - y_i)^2 $$
Puisque $d > n$ et que $\text{rg}(X) = n$, le système linéaire $Xw = y$ est sous-déterminé. L'ensemble des minimiseurs globaux de $\mathcal{L}$, noté $\mathcal{M}$, est un espace affine de dimension $d - n > 0$ :
$$ \mathcal{M} = \{ w \in \mathbb{R}^d \mid Xw = y \} $$
Il existe donc une infinité de vecteurs $w$ qui annulent parfaitement la perte empirique ($\mathcal{L}(w) = 0$).

**3. Algorithme de descente de gradient (Gradient Descent) :**
La descente de gradient continue (flot de gradient, voir [[Jalon 128 (Flots de gradient)]]) est régie par l'équation différentielle ordinaire :
$$ \frac{dw(t)}{dt} = -\nabla \mathcal{L}(w(t)) $$
avec une condition initiale $w(0) = w_0 \in \mathbb{R}^d$.
Le gradient de $\mathcal{L}$ est donné analytiquement par :
$$ \nabla \mathcal{L}(w) = \frac{1}{n} X^\top (Xw - y) $$

### B. Théorèmes, Propositions & Lemmes

> **Théorème de la Régularisation Implicite pour le Flot de Gradient Linéaire :**
> Soit le problème des moindres carrés sur-paramétré défini ci-dessus ($d > n$, $\text{rg}(X)=n$).
> Considérons la dynamique du flot de gradient $\frac{dw(t)}{dt} = -\frac{1}{n}X^\top(Xw(t) - y)$ avec une initialisation à l'origine $w(0) = 0_{\mathbb{R}^d}$.
> Alors, la trajectoire $w(t)$ converge de manière exponentiellement rapide, lorsque $t \to +\infty$, vers une limite $w_\infty$ qui est l'unique solution du problème d'optimisation sous contrainte suivant :
> $$ w_\infty = \underset{w \in \mathbb{R}^d}{\text{argmin}} \frac{1}{2} \|w\|_2^2 \quad \text{sous la contrainte} \quad Xw = y $$
> Ce point limite correspond précisément à la projection orthogonale de l'origine sur l'espace affine des solutions $\mathcal{M}$, ou de manière équivalente, à l'estimateur de norme minimale (minimum norm interpolator).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème de la Régularisation Implicite

1. **Initialisation / Cadre :**
Nous allons démontrer ce théorème en deux temps. D'abord (Analyse de la trajectoire), nous allons caractériser l'espace vectoriel dans lequel évolue la dynamique $w(t)$ pour toute condition initiale $w(0)$. Ensuite (Convergence), nous allons résoudre explicitement l'équation différentielle, puis appliquer la condition initiale $w(0)=0$ pour prouver que le point fixe atteint minimise la norme euclidienne.

2. **Étape 1 : Analyse du sous-espace d'évolution (Invariance de l'espace colonne).**
L'équation différentielle du flot de gradient est :
$$ \frac{dw(t)}{dt} = -\frac{1}{n} X^\top (X w(t) - y) $$
Posons le vecteur des résidus à l'instant $t$ :
$$ r(t) = -(X w(t) - y) \in \mathbb{R}^n $$
L'équation différentielle se réécrit donc :
$$ \frac{dw(t)}{dt} = \frac{1}{n} X^\top r(t) $$
Puisque $X \in \mathcal{M}_{n,d}(\mathbb{R})$, l'opérateur $X^\top$ est une application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}^d$.
Nous observons que pour tout $t \ge 0$, la dérivée temporelle $\frac{dw(t)}{dt}$ appartient à l'image de $X^\top$, notée $\text{Im}(X^\top)$.
En intégrant cette équation différentielle entre $0$ et $t$, par linéarité de l'intégrale (au sens de Bochner, mais ici en dimension finie), nous obtenons :
$$ w(t) - w(0) = \int_0^t \frac{dw(s)}{ds} ds = \int_0^t \frac{1}{n} X^\top r(s) ds $$
$$ w(t) = w(0) + X^\top \left( \frac{1}{n} \int_0^t r(s) ds \right) $$
Posons le vecteur $v(t) = \frac{1}{n} \int_0^t r(s) ds \in \mathbb{R}^n$.
Nous obtenons la caractérisation fondamentale de la trajectoire :
$$ w(t) = w(0) + X^\top v(t) $$
Ceci implique que pour tout $t \ge 0$, le vecteur des poids $w(t)$ reste confiné dans le sous-espace affine $w(0) + \text{Im}(X^\top)$.

3. **Étape 2 : Résolution explicite de la dynamique et convergence.**
Intéressons-nous à l'évolution temporelle des prédictions du modèle sur les données d'entraînement.
Notons $\hat{y}(t) = X w(t) \in \mathbb{R}^n$.
Dérivons $\hat{y}(t)$ par rapport au temps :
$$ \frac{d\hat{y}(t)}{dt} = X \frac{dw(t)}{dt} $$
En remplaçant $\frac{dw(t)}{dt}$ par l'expression du flot de gradient :
$$ \frac{d\hat{y}(t)}{dt} = X \left( -\frac{1}{n} X^\top (X w(t) - y) \right) $$
$$ \frac{d\hat{y}(t)}{dt} = -\frac{1}{n} X X^\top (\hat{y}(t) - y) $$
Posons la matrice de covariance empirique non centrée des données (aussi appelée matrice de Gram ou noyau neural tangent linéaire), $K = X X^\top \in \mathcal{M}_{n,n}(\mathbb{R})$.
Puisque nous avons supposé $\text{rg}(X) = n$, la matrice $K$ est définie positive. En effet, pour tout vecteur non nul $u \in \mathbb{R}^n$ :
$$ u^\top K u = u^\top (X X^\top) u = (X^\top u)^\top (X^\top u) = \|X^\top u\|_2^2 \ge 0 $$
Et l'égalité à $0$ n'est possible que si $X^\top u = 0_{\mathbb{R}^d}$. Or, par le théorème du rang, $\dim(\text{Ker}(X^\top)) + \text{rg}(X^\top) = n$. Comme $\text{rg}(X^\top) = \text{rg}(X) = n$, alors $\dim(\text{Ker}(X^\top)) = 0$, donc $X^\top u = 0 \implies u = 0_{\mathbb{R}^n}$. Ainsi $K$ est strictement définie positive, et ses valeurs propres sont toutes strictement positives (la plus petite est notée $\lambda_{\text{min}}(K) > 0$).
L'équation différentielle pour les prédictions devient un système d'EDO linéaires à coefficients constants :
$$ \frac{d}{dt} (\hat{y}(t) - y) = -\frac{1}{n} K (\hat{y}(t) - y) $$
La solution analytique de cette EDO matricielle est obtenue via l'exponentielle de matrice :
$$ \hat{y}(t) - y = \exp\left( -\frac{t}{n} K \right) (\hat{y}(0) - y) $$
Puisque toutes les valeurs propres de $K$ sont strictement positives, l'opérateur $\exp\left(-\frac{t}{n} K\right)$ est une contraction.
Prenons la norme euclidienne de part et d'autre :
$$ \|\hat{y}(t) - y\|_2 \le \exp\left( -\frac{t \cdot \lambda_{\text{min}}(K)}{n} \right) \|\hat{y}(0) - y\|_2 $$
Lorsque $t \to +\infty$, $\|\hat{y}(t) - y\|_2 \to 0$, ce qui démontre que $\lim_{t \to +\infty} X w(t) = y$. Le système converge donc asymptotiquement vers une solution interpolatrice globale (la perte empirique s'annule).
Notons $w_\infty = \lim_{t \to +\infty} w(t)$. Ce point fixe appartient à l'espace des solutions $\mathcal{M} = \{ w \mid Xw = y \}$.

4. **Étape 3 : Caractérisation de l'optimum par la condition initiale et conclusion.**
Reprenons le résultat de l'Étape 1. Nous avons prouvé que pour tout $t$, $w(t) \in w(0) + \text{Im}(X^\top)$.
Par passage à la limite (l'espace affine étant fermé), la limite $w_\infty$ vérifie :
$$ w_\infty \in w(0) + \text{Im}(X^\top) $$
Appliquons maintenant l'hypothèse de l'initialisation du théorème : $w(0) = 0_{\mathbb{R}^d}$.
Alors :
$$ w_\infty \in \text{Im}(X^\top) $$
Il existe donc un vecteur $\alpha \in \mathbb{R}^n$ tel que $w_\infty = X^\top \alpha$.
De plus, $w_\infty$ est une solution du problème d'interpolation, donc :
$$ X w_\infty = y $$
En substituant $w_\infty$ par $X^\top \alpha$ dans cette contrainte, nous obtenons :
$$ X (X^\top \alpha) = y $$
$$ (X X^\top) \alpha = y $$
$$ K \alpha = y $$
Comme nous l'avons démontré à l'Étape 2, $K$ est inversible (définie positive). Nous pouvons donc isoler $\alpha$ de manière unique :
$$ \alpha = K^{-1} y = (X X^\top)^{-1} y $$
En réinjectant cette expression dans l'équation de $w_\infty$, nous obtenons la forme explicite (pseudo-inverse de Moore-Penrose pour les matrices larges) :
$$ w_\infty = X^\top (X X^\top)^{-1} y $$
Il reste à prouver que ce $w_\infty$ précis est le minimiseur global de la norme euclidienne parmi toutes les solutions interpolatrices.
Considérons le problème d'optimisation sous contrainte :
$$ \min_{w \in \mathbb{R}^d} \frac{1}{2} \|w\|_2^2 \quad \text{s.c.} \quad Xw = y $$
Le Lagrangien associé s'écrit, en introduisant un vecteur de multiplicateurs de Lagrange $\lambda \in \mathbb{R}^n$ :
$$ \mathcal{L}(w, \lambda) = \frac{1}{2} \|w\|_2^2 + \lambda^\top (y - Xw) $$
Les conditions d'optimalité de premier ordre (KKT, voir [[Jalon 124 (Conditions de Karush-Kuhn-Tucker)]]) imposent l'annulation du gradient par rapport à $w$ :
$$ \nabla_w \mathcal{L}(w^*, \lambda^*) = w^* - X^\top \lambda^* = 0_{\mathbb{R}^d} \implies w^* = X^\top \lambda^* $$
Cette condition KKT exige que la solution optimale $w^*$ appartienne à l'image de $X^\top$ ($\text{Im}(X^\top)$).
Nous savons que toute solution appartenant à l'intersection de l'espace affine des contraintes $\{ w \mid Xw=y \}$ et du sous-espace vectoriel orthogonal au noyau $\text{Im}(X^\top) = (\text{Ker}(X))^\bot$ est l'unique projection orthogonale de l'origine sur la variété affine, et minimise donc la norme euclidienne.
Or, nous avons trouvé exactement que notre limite du flot de gradient $w_\infty$ vérifie simultanément $X w_\infty = y$ et $w_\infty \in \text{Im}(X^\top)$.
Conclusion finale : La dynamique de la descente de gradient, lorsqu'elle est initialisée à zéro, sélectionne implicitement l'unique solution interpolatrice de norme minimale euclidienne $\ell_2$. L'algorithme d'optimisation induit donc une régularisation invisible, en pénalisant la norme des poids sans qu'aucun terme de type $\|w\|_2^2$ (Ridge) n'ait été ajouté à la fonction de perte empirique.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application Directe : Régularisation implicite avec une initialisation non nulle
**Énoncé :**
On se place dans le cadre du théorème précédent ($d>n$, $X$ de plein rang), mais l'initialisation du flot de gradient n'est plus à l'origine : on pose $w(0) = w_0 \neq 0_{\mathbb{R}^d}$.
Démontrer, en déroulant l'intégralité du raisonnement formel, que le point fixe asymptotique $w_\infty$ atteint par le flot de gradient correspond à la solution du problème d'optimisation suivant :
$$ w_\infty = \underset{w \in \mathbb{R}^d}{\text{argmin}} \frac{1}{2} \|w - w_0\|_2^2 \quad \text{sous la contrainte} \quad Xw = y $$

**Correction Détaillée :**
* *Analyse de l'énoncé :* Le flot de gradient reste inchangé, son équation différentielle est la même. Seule la condition initiale est perturbée. L'objectif est de montrer que l'algorithme cherche l'interpolateur le plus proche, au sens euclidien, du point de départ.
* *Résolution pas-à-pas :*
1. Reprenons l'Étape 1 de la démonstration du cours. Nous avons prouvé, par intégration stricte, que la trajectoire obéit à la contrainte géométrique invariante :
   $$ w(t) = w_0 + X^\top v(t) $$
   où $v(t) = \frac{1}{n} \int_0^t r(s) ds$.
   Ceci implique que pour tout $t$, $w(t) - w_0 \in \text{Im}(X^\top)$.
2. La convergence de la dynamique est préservée. L'analyse de l'Étape 2 (qui utilise $K = XX^\top$) est indépendante de $w_0$. Le résidu $\|\hat{y}(t) - y\|_2 \to 0$, donc $X w_\infty = y$.
3. À la limite $t \to +\infty$, nous obtenons deux conditions simultanées pour le point fixe :
   (Condition 1 d'interpolation) : $X w_\infty = y$
   (Condition 2 d'invariance géométrique) : $\exists \alpha \in \mathbb{R}^n$ tel que $w_\infty - w_0 = X^\top \alpha$.
4. Résolvons le problème d'optimisation sous contrainte proposé :
   Soit le programme $(P) : \min_{w} \frac{1}{2} \|w - w_0\|_2^2$ s.c. $Xw = y$.
   Le Lagrangien est :
   $$ \mathcal{L}(w, \lambda) = \frac{1}{2} \|w - w_0\|_2^2 + \lambda^\top (y - Xw) $$
   Dérivons par rapport à $w$ pour les conditions KKT du premier ordre :
   $$ \nabla_w \mathcal{L}(w^*, \lambda^*) = (w^* - w_0) - X^\top \lambda^* = 0_{\mathbb{R}^d} $$
   $$ w^* - w_0 = X^\top \lambda^* $$
   Nous constatons que la condition d'optimalité stipule que la direction $(w^* - w_0)$ doit appartenir à $\text{Im}(X^\top)$.
   De plus, pour satisfaire la contrainte primale, il faut $X w^* = y$.
5. Identifions les systèmes. Notre limite $w_\infty$ vérifie précisément les conditions KKT du problème d'optimisation $(P)$. Comme $(P)$ est un problème de minimisation strictement convexe sur un espace affine, les conditions KKT sont nécessaires et suffisantes.
   Donc $w_\infty$ est l'unique solution du problème $(P)$.
   *Conclusion finale* : Une initialisation arbitraire $w_0$ induit une régularisation implicite qui pénalise la distance euclidienne entre la solution finale et l'initialisation.

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT) : Perte Logistique et Marge Maximale
**Énoncé :**
Soit un problème de classification binaire linéairement séparable où les données sont représentées par $\{(x_i, y_i)\}_{i=1}^n$ avec $x_i \in \mathbb{R}^d$ et $y_i \in \{-1, +1\}$.
On utilise un modèle linéaire $f_w(x) = \langle w, x \rangle$ et on entraîne le modèle en minimisant la perte logistique (sans aucune régularisation explicite) par descente de gradient (GD) à pas discret ou flot de gradient.
La perte empirique est :
$$ \mathcal{L}(w) = \frac{1}{n} \sum_{i=1}^n \log(1 + \exp(-y_i \langle w, x_i \rangle)) $$
Dans un régime fortement sur-paramétré (données linéairement séparables, il existe une infinité d'hyperplans séparateurs), démontrer conceptuellement (et esquisser la preuve mathématique rigoureuse) vers quel type de séparateur la trajectoire $\frac{w(t)}{\|w(t)\|_2}$ converge asymptotiquement lorsque $t \to +\infty$. Quel est le lien avec les Machines à Vecteurs de Support (SVM) ?

**Correction Détaillée :**
* *Analyse de l'énoncé :* Contrairement aux moindres carrés qui pénalisent la norme $\ell_2$ des poids (régularisation Ridge implicite), la perte logistique couplée à l'exponentielle asymptotique pousse les normes des poids vers l'infini ($\|w(t)\|_2 \to \infty$) pour obtenir des prédictions infiniment confiantes. Le mystère réside dans l'évolution de la *direction* du vecteur.
* *Résolution pas-à-pas (Esquisse de la preuve de Soudry et al., 2018) :*
1. **Divergence de la norme :** Les données sont séparables, donc il existe $w^*$ tel que pour tout $i$, $y_i \langle w^*, x_i \rangle > 0$. Si on pose $w = \alpha w^*$ avec $\alpha \to +\infty$, les marges $y_i \langle w, x_i \rangle \to +\infty$. L'argument de l'exponentielle tend vers $-\infty$, et $\log(1 + e^{-\infty}) \to 0$. L'infimum de la perte est $0$, mais il n'est jamais atteint à distance finie. Le flot de gradient pousse inexorablement vers $\|w(t)\|_2 \to +\infty$.
2. **Dynamique directionnelle :** Le gradient de la perte est :
   $$ \nabla \mathcal{L}(w) = -\frac{1}{n} \sum_{i=1}^n \frac{1}{1 + \exp(y_i \langle w, x_i \rangle)} y_i x_i $$
   À mesure que $t \to +\infty$ et que les marges grandissent, le terme logistique $\frac{1}{1 + e^z}$ se comporte asymptotiquement comme $e^{-z}$.
   Le flot se rapproche d'une dynamique dominée par les exemples $x_i$ ayant la *plus petite* marge (les points les plus proches de l'hyperplan de décision), car ils maximisent le terme $e^{-y_i \langle w, x_i \rangle}$ et dominent la somme du gradient. Ce sont les "Vecteurs de Support".
3. **Alignement KKT (Le Lemme Fondamental) :**
   Si l'on change le repère temporel pour observer l'évolution de la direction unitaire $\tilde{w}(t) = \frac{w(t)}{\|w(t)\|_2}$, les mathématiciens démontrent que $\tilde{w}(t)$ converge vers une direction limite $\bar{w}$.
   On prouve que cette direction correspond au vecteur normal de l'hyperplan de *marge maximale* (Hard-Margin SVM).
   Le problème de marge maximale $L_2$ est défini par :
   $$ \bar{w}_{\text{SVM}} = \underset{w \in \mathbb{R}^d}{\text{argmin}} \frac{1}{2} \|w\|_2^2 \quad \text{s.c.} \quad y_i \langle w, x_i \rangle \ge 1 \quad \forall i $$
   La direction limite $\bar{w}$ s'aligne exactement avec $\frac{\bar{w}_{\text{SVM}}}{\|\bar{w}_{\text{SVM}}\|_2}$.
4. *Conclusion :*
   Bien que l'on n'ait codé aucun terme pénalisant la norme ou imposant une marge complexe dans la perte logistique, l'algorithme d'optimisation par flot de gradient sur une perte exponentielle agit comme un solveur SVM de marge maximale. C'est l'essence même de la **régularisation implicite** : le biais inductif profond de l'optimiseur sélectionne un modèle géométriquement maximalement robuste parmi une infinité d'hyperplans qui séparent parfaitement (à $100\%$ d'accuracy d'entraînement) les données.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le phénomène de double descente (abordé au [[Jalon 144 (Le phénomène de double descente)]]) et la généralisation hors-norme des réseaux de neurones profonds (Deep Learning) défient la théorie classique de l'apprentissage statistique de Vapnik-Chervonenkis (voir [[Jalon 136 (Theorie de Vapnik-Chervonenkis)]]). Dans le régime sur-paramétré des LLMs (Large Language Models) ou des CNNs massifs, les modèles ont la capacité de mémoriser n'importe quel bruit aléatoire. S'ils ne le font pas en pratique, c'est grâce au biais inductif de la descente de gradient stochastique (SGD). La SGD agit comme un rasoir d'Ockham mathématique implicite, cherchant activement la variété de dimension minimale ou la fonction la plus régulière qui interpole les données, évitant ainsi les fluctuations violentes (hautes fréquences) caractéristiques de l'overfitting pur.
- **Exemple Concret :** Lors du pré-entraînement (Pre-training) d'un Transformer doté de 175 milliards de paramètres comme GPT-3. La dimension des poids $d$ est monstrueusement supérieure au nombre d'exemples d'un mini-batch $n$. Le problème local est infini-sous-déterminé. Si un optimiseur abstrait générique cherchait les racines, il pourrait exploser les normes des poids et créer un modèle hautement instable (qui prédirait des tokens absurdes à la moindre variation de prompt). Or l'usage de l'optimiseur Adam ou de la SGD force les matrices de poids (les matrices Query, Key, Value de l'Attention) à maintenir de faibles normes spectrales et un faible rang de manière organique. Le réseau apprend des représentations lisses, douces et généralisables *uniquement* parce que le trajet que parcourt l'algorithme d'optimisation pénalise implicitement la complexité.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 128 (Flots de gradient)]], [[Jalon 124 (Conditions de Karush-Kuhn-Tucker)]], [[Jalon 7 (Espaces vectoriels abstraits)]]
- **Concepts Futurs dépendants :** [[Jalon 144 (Le phénomène de double descente)]], [[Jalon 130 (Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés.)]], [[Jalon 140 (Classifieur de Bayes optimal)]]
