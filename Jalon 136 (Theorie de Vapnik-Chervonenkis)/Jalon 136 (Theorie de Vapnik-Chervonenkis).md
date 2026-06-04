---
uuid: "jalon-136"
title: "Jalon 136 : Theorie de Vapnik-Chervonenkis"
year: 3
trimester: 12
tags:
  - math/statistiques
  - ia/machine_learning
  - ia/theorie_apprentissage
prev: "[[Jalon 135 (Complexite de Rademacher).md]]"
next: "[[Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC).md]]"
---

# Théorie de Vapnik-Chervonenkis et Lemme de Sauer

## 1. L'Intuition Première (Niveau 12 ans)

**La Métaphore : Le Jeu du Devin et des Points Colorés**

Imagine que tu es un devin et que l'on te donne une feuille blanche. Ton ami dessine quelques points sur cette feuille et les colorie en rouge ou en bleu, au hasard. Ton objectif est de tracer une seule ligne droite qui sépare parfaitement tous les points rouges des points bleus.

Si ton ami dessine 2 points (un rouge et un bleu), tu pourras toujours tracer une ligne entre eux. Même avec 3 points (disons 2 rouges et 1 bleu, disposés en triangle), tu peux toujours trouver une ligne qui isole le point bleu. Par contre, s'il dessine 4 points formant un carré (avec les couleurs alternées sur les diagonales), aucune ligne droite ne pourra séparer les rouges des bleus !

Dans ce jeu, la "ligne droite" est ce qu'on appelle ton *hypothèse*. Le fait que tu puisses séparer n'importe quelle coloration de 3 points, mais pas de 4, mesure la "puissance" ou la "flexibilité" de ta ligne droite. Si tu avais le droit d'utiliser un cercle au lieu d'une ligne, tu pourrais séparer des configurations bien plus compliquées !

**Le "Pourquoi on a inventé ça" :**
En Intelligence Artificielle, une machine essaie d'apprendre une règle (comme notre ligne droite) pour séparer des données (comme des images de chats et de chiens). Si le modèle est trop simple (une ligne), il risque de ne pas y arriver. S'il est trop complexe (une courbe qui serpente dans tous les sens), il risque d'apprendre par cœur chaque exemple sans comprendre la logique générale (c'est l'overfitting). Les mathématiciens Vladimir Vapnik et Alexey Chervonenkis ont inventé une théorie pour mesurer exactement cette "complexité". Ils voulaient savoir jusqu'à quel point on peut faire confiance à une machine qui a trouvé une règle qui marche sur ses exemples d'entraînement.

**Visualisation :**
Imagine un plan $\mathbb{R}^2$. Pour 3 points non alignés, on peut générer $2^3 = 8$ façons de les colorier (rouge/bleu). Pour chacune de ces 8 configurations, on peut trouver un demi-plan (délimité par une droite) qui englobe exactement les points bleus. On dit que la famille des demi-plans "pulvérise" (ou *shatter*) ces 3 points.

## 2. Formalisation & Rigueur Académique

### A. Définitions Formelles

Soit $\mathcal{X}$ un espace d'entrée mesurable (par exemple $\mathcal{X} \subset \mathbb{R}^d$) et $\mathcal{Y} = \{0, 1\}$ (ou $\{-1, 1\}$) l'espace des étiquettes. Soit $\mathcal{H}$ un espace d'hypothèses, c'est-à-dire un ensemble de fonctions $h : \mathcal{X} \to \mathcal{Y}$.

**Définition 1 (Dichotomie) :**
Pour un ensemble fini de $n$ points $S = \{x_1, \dots, x_n\} \subset \mathcal{X}$, la restriction de $\mathcal{H}$ à $S$, notée $\mathcal{H}_S$, est l'ensemble de tous les comportements possibles des hypothèses de $\mathcal{H}$ sur $S$ :
$$ \mathcal{H}_S = \{(h(x_1), \dots, h(x_n)) \in \{0, 1\}^n \mid h \in \mathcal{H}\} $$

**Définition 2 (Pulvérisation / Shattering) :**
On dit que l'espace d'hypothèses $\mathcal{H}$ *pulvérise* l'ensemble $S$ si $\mathcal{H}$ est capable de réaliser toutes les dichotomies possibles sur $S$, c'est-à-dire si le cardinal de $\mathcal{H}_S$ est maximal :
$$ |\mathcal{H}_S| = 2^n $$

**Définition 3 (Fonction de Croissance / Growth Function) :**
La fonction de croissance de $\mathcal{H}$, notée $\tau_{\mathcal{H}} : \mathbb{N} \to \mathbb{N}$, est définie comme le nombre maximal de dichotomies que $\mathcal{H}$ peut générer sur n'importe quel ensemble de taille $n$ :
$$ \tau_{\mathcal{H}}(n) = \max_{S \subset \mathcal{X}, |S|=n} |\mathcal{H}_S| $$
Par définition, $\forall n \in \mathbb{N}, \tau_{\mathcal{H}}(n) \le 2^n$.

**Définition 4 (Dimension de Vapnik-Chervonenkis / VC Dimension) :**
La dimension VC de $\mathcal{H}$, notée $VC(\mathcal{H})$, est le cardinal du plus grand ensemble $S \subset \mathcal{X}$ pouvant être pulvérisé par $\mathcal{H}$ :
$$ VC(\mathcal{H}) = \max \{ n \in \mathbb{N} \mid \tau_{\mathcal{H}}(n) = 2^n \} $$
S'il existe des ensembles de taille arbitrairement grande qui peuvent être pulvérisés, on pose $VC(\mathcal{H}) = \infty$.

### B. Théorèmes, Propositions & Lemmes

> **Théorème (Lemme de Sauer-Shelah-Perles) :**
> Soit $\mathcal{H}$ un espace d'hypothèses de dimension VC finie $d = VC(\mathcal{H}) < \infty$. Alors, pour tout $n \in \mathbb{N}$ :
> $$ \tau_{\mathcal{H}}(n) \le \sum_{i=0}^{d} \binom{n}{i} $$
> En particulier, pour $n \ge d$, on a la majoration polynomiale :
> $$ \tau_{\mathcal{H}}(n) \le \left( \frac{en}{d} \right)^d $$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème Pivot : Lemme de Sauer-Shelah-Perles

1. **Initialisation / Cadre :**
   La preuve se fait par une récurrence double sur $n$ (la taille de l'échantillon $S$) et sur $d$ (la dimension VC). On note $\Phi(n, d) = \sum_{i=0}^{d} \binom{n}{i}$. L'objectif est de montrer que pour tout ensemble $S$ de taille $n$, si $VC(\mathcal{H}) \le d$, alors $|\mathcal{H}_S| \le \Phi(n, d)$.

2. **Étape 1 : Cas de base de la récurrence :**
   - Si $n = 0$ : $\mathcal{H}_\emptyset = \{\emptyset\}$, donc $|\mathcal{H}_\emptyset| = 1$. Et $\Phi(0, d) = \binom{0}{0} = 1$. L'inégalité est vérifiée.
   - Si $d = 0$ : Cela signifie qu'aucun point ne peut être pulvérisé. Donc pour tout $x \in \mathcal{X}$, toutes les hypothèses donnent la même étiquette. Ainsi, $|\mathcal{H}_S| = 1$. Et $\Phi(n, 0) = \binom{n}{0} = 1$. L'inégalité est vérifiée.

3. **Étape 2 (Hérédité) :**
   Supposons la propriété vraie pour $(n-1, d)$ et $(n-1, d-1)$.
   Soit $S = \{x_1, \dots, x_n\}$ un ensemble de taille $n$, et posons $S' = S \setminus \{x_n\}$.
   L'ensemble de dichotomies $\mathcal{H}_S$ induit un ensemble de dichotomies sur $S'$, noté $\mathcal{H}_{S'}$. En restreignant $\mathcal{H}_S$ à $S'$, certains couples de dichotomies (qui différaient uniquement sur $x_n$) vont "fusionner".
   Définissons l'ensemble des dichotomies sur $S'$ qui admettaient deux extensions dans $\mathcal{H}_S$ (une avec $h(x_n)=0$ et une avec $h(x_n)=1$) :
   $$ \mathcal{D} = \{ y' \in \{0, 1\}^{n-1} \mid (y', 0) \in \mathcal{H}_S \text{ et } (y', 1) \in \mathcal{H}_S \} $$

   Par construction, nous avons l'égalité exacte :
   $$ |\mathcal{H}_S| = |\mathcal{H}_{S'}| + |\mathcal{D}| $$
   *(Chaque élément de $\mathcal{H}_{S'}$ provient d'au moins un élément de $\mathcal{H}_S$. Si un élément provient de deux éléments de $\mathcal{H}_S$, il est compté une fois dans $|\mathcal{H}_{S'}|$ et il appartient à $\mathcal{D}$, ajoutant exactement la contribution manquante).*

4. **Étape 3 (Majoration des termes) :**
   - Pour $|\mathcal{H}_{S'}|$ : L'espace d'hypothèses $\mathcal{H}$ restreint à $S'$ a toujours une dimension VC au plus $d$. Donc, par hypothèse de récurrence :
     $$ |\mathcal{H}_{S'}| \le \Phi(n-1, d) $$
   - Pour $|\mathcal{D}|$ : $\mathcal{D}$ représente l'ensemble des dichotomies sur $S'$ telles que $\mathcal{H}$ peut leur adjoindre n'importe quelle valeur (0 ou 1) pour $x_n$. Cela implique qu'un sous-ensemble $A \subset S'$ est pulvérisé par $\mathcal{D}$ si et seulement si l'ensemble $A \cup \{x_n\} \subset S$ est pulvérisé par $\mathcal{H}$.
     Puisque $VC(\mathcal{H}) \le d$, le plus grand ensemble pulvérisable par $\mathcal{H}$ a pour taille $d$. Donc le plus grand ensemble $A \subset S'$ pulvérisable par $\mathcal{D}$ a une taille maximale de $d-1$. Ainsi, la dimension VC de l'espace d'hypothèses induisant $\mathcal{D}$ est au plus $d-1$.
     En appliquant l'hypothèse de récurrence à $\mathcal{D}$ (qui porte sur les $n-1$ points de $S'$) avec une dimension VC de $d-1$ :
     $$ |\mathcal{D}| \le \Phi(n-1, d-1) $$

5. **Conclusion de la récurrence :**
   En combinant les deux majorations :
   $$ |\mathcal{H}_S| = |\mathcal{H}_{S'}| + |\mathcal{D}| \le \Phi(n-1, d) + \Phi(n-1, d-1) $$
   Or, en utilisant la formule d'addition de Pascal $\binom{n-1}{i} + \binom{n-1}{i-1} = \binom{n}{i}$ :
   $$ \Phi(n-1, d) + \Phi(n-1, d-1) = \sum_{i=0}^{d} \binom{n-1}{i} + \sum_{i=1}^{d} \binom{n-1}{i-1} $$
   *(Notons que $\Phi(n-1, d-1)$ somme de $j=0$ à $d-1$, on pose $i=j+1$, d'où la somme de $i=1$ à $d$. Pour $i=0$, on a $\binom{n-1}{0} = 1 = \binom{n}{0}$)*.
   $$ = \binom{n-1}{0} + \sum_{i=1}^{d} \left( \binom{n-1}{i} + \binom{n-1}{i-1} \right) $$
   $$ = \binom{n}{0} + \sum_{i=1}^{d} \binom{n}{i} = \sum_{i=0}^{d} \binom{n}{i} = \Phi(n, d) $$
   Ce qui démontre le lemme de Sauer de manière formelle et exhaustive.

*(La majoration $(en/d)^d$ découle d'une majoration analytique standard de la somme des coefficients binomiaux pour $n \ge d$.)*

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application Directe : Intervalles sur la droite réelle
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}$. Considérons l'espace d'hypothèses $\mathcal{H}$ constitué des fonctions indicatrices d'intervalles fermés : $\mathcal{H} = \{ \mathbb{I}_{[a, b]} \mid a \le b \in \mathbb{R} \}$. Déterminer la dimension VC de $\mathcal{H}$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On demande d'évaluer le maximum de points $n$ que $\mathcal{H}$ peut pulvériser. Il faut donc montrer qu'il existe un ensemble de taille $d$ pulvérisable, et qu'aucun ensemble de taille $d+1$ n'est pulvérisable.
* *Résolution pas-à-pas :*
  1. *Minoration ($VC(\mathcal{H}) \ge 2$) :* Considérons $S = \{1, 2\}$. Les dichotomies possibles sont $\{(0,0), (1,0), (0,1), (1,1)\}$.
     - $(0,0)$ est réalisé par $[3, 4]$.
     - $(1,0)$ est réalisé par $[0.5, 1.5]$.
     - $(0,1)$ est réalisé par $[1.5, 2.5]$.
     - $(1,1)$ est réalisé par $[0.5, 2.5]$.
     Toutes les $2^2=4$ dichotomies sont réalisables. Donc $\mathcal{H}$ pulvérise $S$, d'où $VC(\mathcal{H}) \ge 2$.
  2. *Majoration ($VC(\mathcal{H}) < 3$) :* Soit $S = \{x_1, x_2, x_3\}$ un ensemble quelconque de 3 points. Quitte à les réordonner, on suppose sans perte de généralité $x_1 < x_2 < x_3$.
     Considérons la dichotomie alternée : attribuer $1$ à $x_1$ et $x_3$, et $0$ à $x_2$.
     Si une telle hypothèse $h = \mathbb{I}_{[a, b]}$ existe, elle doit vérifier :
     $a \le x_1 \le b$ et $a \le x_3 \le b$.
     Par convexité de l'intervalle $[a,b]$, tout point compris entre $x_1$ et $x_3$ doit appartenir à l'intervalle. Puisque $x_1 < x_2 < x_3$, on a nécessairement $x_2 \in [a, b]$, ce qui contredit l'exigence d'avoir $0$ en $x_2$.
     Cette dichotomie est impossible. Ainsi, aucun ensemble de 3 points ne peut être pulvérisé.
  3. *Conclusion :* La dimension VC des intervalles de $\mathbb{R}$ est exactement 2.

### Exercice 2 : Niveau Avancé (Inspiré Concours ENS) : Les demi-espaces de $\mathbb{R}^d$
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}^d$. Considérons $\mathcal{H}$ la classe des demi-espaces linéaires homogènes (passant par l'origine), définis par $\mathcal{H} = \{ x \mapsto \text{sign}(\langle w, x \rangle) \mid w \in \mathbb{R}^d \}$, avec la convention $\text{sign}(0) = 1$. Démontrer rigoureusement que $VC(\mathcal{H}) = d$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* La classe correspond aux classifieurs linéaires purs (sans biais). Nous devons montrer que $d$ points peuvent être pulvérisés (minoration), mais que tout ensemble de $d+1$ points ne le peut pas (majoration par le théorème de Radon).
* *Résolution pas-à-pas :*
  1. *Minoration ($VC \ge d$) :* Considérons la base canonique $S = \{e_1, \dots, e_d\}$ de $\mathbb{R}^d$. Pour toute dichotomie $(y_1, \dots, y_d) \in \{-1, 1\}^d$, choisissons le vecteur de poids $w = \sum_{i=1}^{d} y_i e_i$.
     Alors pour tout $k \in \{1, \dots, d\}$, on évalue :
     $$ \text{sign}(\langle w, e_k \rangle) = \text{sign}(y_k \langle e_k, e_k \rangle) = \text{sign}(y_k) = y_k $$
     Toutes les $2^d$ dichotomies sont réalisables. Donc $\mathcal{H}$ pulvérise $S$, et $VC(\mathcal{H}) \ge d$.
  2. *Majoration ($VC < d+1$) :* Soit $S = \{x_1, \dots, x_{d+1}\}$ un ensemble de $d+1$ points dans $\mathbb{R}^d$.
     Puisqu'il y a $d+1$ vecteurs dans un espace de dimension $d$, la famille $S$ est linéairement liée.
     Il existe donc des scalaires $\alpha_1, \dots, \alpha_{d+1}$ non tous nuls tels que :
     $$ \sum_{i=1}^{d+1} \alpha_i x_i = 0 $$
     Séparons les indices en deux ensembles disjoints selon le signe des coefficients :
     $$ I = \{ i \mid \alpha_i > 0 \} \quad \text{et} \quad J = \{ i \mid \alpha_i \le 0 \} $$
     Au moins l'un des deux ensembles est non vide, et comme les coefficients ne sont pas tous nuls, l'autre n'est pas "absorbant", réécrivons l'égalité vectorielle :
     $$ \sum_{i \in I} \alpha_i x_i = \sum_{j \in J} (-\alpha_j) x_j $$
     Considérons la dichotomie qui associe l'étiquette $+1$ aux points indicés par $I$, et $-1$ à ceux indicés par $J$.
     S'il existait $w \in \mathbb{R}^d$ réalisant cette dichotomie, alors $\forall i \in I, \langle w, x_i \rangle > 0$ et $\forall j \in J, \langle w, x_j \rangle < 0$.
     Prenons le produit scalaire avec le vecteur combinaison linéaire :
     $$ \langle w, \sum_{i \in I} \alpha_i x_i \rangle = \sum_{i \in I} \alpha_i \langle w, x_i \rangle > 0 $$ (car $\alpha_i > 0$ et $\langle w, x_i \rangle > 0$).
     D'autre part :
     $$ \langle w, \sum_{j \in J} (-\alpha_j) x_j \rangle = \sum_{j \in J} (-\alpha_j) \langle w, x_j \rangle \le 0 $$ (car $(-\alpha_j) \ge 0$ et $\langle w, x_j \rangle < 0$).
     Ceci implique que $A > 0$ et $A \le 0$ avec $A$ la valeur des deux sommes égales. C'est une contradiction absolue.
     Cette dichotomie spécifique est irréalisable pour tout ensemble de $d+1$ points.
  3. *Conclusion :* Aucun ensemble de $d+1$ points ne peut être pulvérisé, donc $VC(\mathcal{H}) = d$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le Lemme de Sauer est la clé de voûte du Modèle PAC (Probably Approximately Correct). Il permet de passer d'un espace d'hypothèses potentiellement infini continu (où des bornes naïves par l'union (Union Bound) exploseraient vers l'infini) à une mesure de complexité effective finie. La fonction de croissance remplace la taille de l'espace dans les bornes de généralisation. Si la dimension VC d'un modèle est finie, la différence entre l'erreur d'entraînement (Risque Empirique) et l'erreur réelle (Risque Réel) décroît de l'ordre de $\sqrt{VC(\mathcal{H}) / n}$. Le modèle apprend et généralise !
- **Exemple Concret :** Dans la classification d'images via un réseau de neurones multicouche avec des activations ReLU (Multilayer Perceptron), des théorèmes majeurs (ex: Bartlett et al.) lient la dimension VC au nombre de paramètres $W$ et de couches $L$. Le fait que ces réseaux aient une dimension VC finie est la preuve formelle fondamentale que l'apprentissage du perceptron n'est pas qu'une mémorisation aléatoire, mais obéit aux lois universelles de la théorie statistique. Le Lemme de Sauer assure que, malgré une infinité de valeurs possibles pour les poids du réseau, le comportement effectif sur un dataset de taille $n$ ne croît que de manière polynomiale par rapport à $n$, ce qui sauve l'apprentissage.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 133 (Modele PAC)]], [[Jalon 134 (Complexite des classes de fonctions)]], [[Jalon 135 (Complexite de Rademacher)]]
- **Concepts Futurs dépendants :** [[Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC)]], [[Jalon 144 (Le phénomène de double descente)]]
