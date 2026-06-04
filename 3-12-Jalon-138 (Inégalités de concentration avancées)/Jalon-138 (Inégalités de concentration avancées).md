---
uuid: "jalon-138"
title: "Inégalités de concentration avancées, inégalité de McDiarmid (différences bornées) et entropie de concentration"
year: 3
trimester: 12
tags:
  - math/probabilites
  - ia/generalisation
prev: "[[Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC).md]]"
next: "[[Jalon 139 (Notion de stabilité algorithmique).md]]"
---

# Inégalités de concentration avancées, inégalité de McDiarmid (différences bornées) et entropie de concentration

## 1. Présentation du concept clé (minimum 500 mots)

### La Métaphore
Imaginez que vous êtes le chef d'orchestre d'une immense cuisine comptant 100 cuisiniers préparant un banquet colossal. Chaque cuisinier travaille de manière largement indépendante sur sa propre tâche : l'un épluche des pommes de terre, un autre fouette une crème, un troisième assaisonne une sauce. À la fin de la journée, toutes leurs contributions individuelles sont combinées par une recette complexe (pas une simple addition) pour produire un score final : la note globale attribuée par les critiques gastronomiques à ce banquet.

L'inégalité de McDiarmid, ou méthode des différences bornées, repose sur une idée très intuitive : si chaque cuisinier, pris individuellement, ne peut modifier la qualité finale du repas que d'une quantité infime, alors la note globale du banquet sera extrêmement stable. Même si le cuisinier numéro 42 rate complètement sa crème ou si le cuisinier numéro 79 oublie de saler ses légumes, l'impact individuel sur le plat final reste borné. Bien que l'ensemble du processus culinaire soit chaotique et non linéaire (ce n'est pas une simple somme arithmétique de leurs efforts), le résultat final va se "concentrer" de manière quasi déterministe autour d'une valeur moyenne attendue. La probabilité d'observer un désastre complet ou un triomphe absolu (qui s'écarteraient significativement de la moyenne) est exponentiellement faible. C'est l'essence même de la concentration de la mesure dans les espaces de grande dimension.

### Le "Pourquoi on a inventé ça"
Historiquement, les probabilistes disposaient d'outils puissants comme la loi des grands nombres ou le théorème central limite, puis des inégalités de concentration classiques comme celles de Markov, de Bienaymé-Tchebychev, et enfin de Chernoff et de Hoeffding. Cependant, toutes ces inégalités traditionnelles partageaient une contrainte majeure : elles s'appliquaient presque exclusivement à des sommes de variables aléatoires indépendantes (de la forme $S_n = \sum_{i=1}^n X_i$). 

Or, dans les problèmes modernes de l'analyse des algorithmes, de la géométrie en grande dimension et surtout de l'apprentissage statistique (Machine Learning), nous manipulons des objets bien plus complexes qu'une simple somme. Par exemple, nous voulons analyser la concentration de la perte empirique minimale d'un classifieur, le supremum d'un processus empirique (comme la complexité de Rademacher), ou la longueur du chemin le plus court dans un graphe aléatoire. Ces variables sont des fonctions complexes, non linéaires et hautement couplées de $n$ variables aléatoires indépendantes.

Pour répondre à ce défi, Colin McDiarmid a introduit en 1989 une généralisation de l'inégalité de Hoeffding. Son but était de s'affranchir de la structure de somme linéaire. Il a prouvé que la seule propriété requise pour obtenir une concentration exponentielle d'une fonction générale de plusieurs variables aléatoires indépendantes est que cette fonction soit stable sous la perturbation d'une seule de ses coordonnées. C'est ce qu'on appelle la propriété des différences bornées ou propriété de Lipschitz par rapport à la métrique de Hamming.

Parallèlement, pour aller encore plus loin dans la finesse des bornes de concentration et étudier des fonctions n'ayant pas de bornes strictes sur leurs coordonnées, les mathématiciens (tels que Michel Ledoux, Pascal Massart et Stéphane Boucheron) ont développé l'approche entropique. Cette théorie cherche à quantifier la dispersion à travers l'entropie de Shannon des variables aléatoires et les inégalités log-soboléviennes, permettant d'obtenir des inégalités de concentration fonctionnelles d'une précision chirurgicale.

### Visualisation
Pour visualiser ce phénomène, imaginons la géométrie des espaces de dimension supérieure. Si l'on considère une sphère de dimension $n$ (où $n$ est de l'ordre de plusieurs milliers ou millions), un fait géométrique contre-intuitif et spectaculaire se produit : presque tout le volume de la sphère est concentré à proximité immédiate de son équateur. Si l'on trace une bande de largeur infinitésimale autour de n'importe quel équateur, cette bande contient plus de 99,99% du volume total de la sphère.

En transposant cette géométrie aux probabilités, si nous définissons une fonction continue (Lipschitz) sur un espace produit muni d'une mesure de probabilité, l'image de cet espace par la fonction va se concentrer sur un intervalle extrêmement étroit. Si vous mesurez cette fonction sur des points tirés au hasard, vous obtiendrez presque toujours exactement la même valeur (la moyenne). Les fluctuations hors de cette bande étroite sont confinées dans les "calottes polaires" de l'espace de grande dimension, dont le volume probabiliste décroît de façon exponentiellement rapide à mesure que la dimension $n$ augmente. L'entropie de concentration quantifie précisément cette vitesse de contraction géométrique de l'espace.

---

## 2. Formalisation & Rigueur Académique (minimum 500 mots)

### A. Définitions Formelles
Commençons par définir rigoureusement le cadre probabiliste dans lequel s'énoncent ces inégalités.

Soient $(\mathcal{X}_1, \Sigma_1), (\mathcal{X}_2, \Sigma_2), \dots, (\mathcal{X}_n, \Sigma_n)$ des espaces mesurables.
Soit $\mathcal{X} = \prod_{i=1}^n \mathcal{X}_i$ leur espace produit, muni de la tribu produit $\Sigma = \bigotimes_{i=1}^n \Sigma_i$.
Soient $X_1, X_2, \dots, X_n$ des variables aléatoires indépendantes définies sur un espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$ et prenant leurs valeurs respectivement dans $\mathcal{X}_i$. La loi conjointe du vecteur aléatoire $X = (X_1, \dots, X_n)$ est la mesure de probabilité produit $\mathbb{P}_X = \bigotimes_{i=1}^n \mathbb{P}_{X_i}$ sur $(\mathcal{X}, \Sigma)$.

#### Propriété des Différences Bornées (Bounded Differences Property)
Soit $f : \mathcal{X} \to \mathbb{R}$ une fonction mesurable. On dit que $f$ satisfait la **propriété des différences bornées** s'il existe des constantes positives $c_1, c_2, \dots, c_n$ telles que pour tout $i \in \{1, \dots, n\}$, et pour tous points $x_1, \dots, x_n \in \mathcal{X}$ et $x'_i \in \mathcal{X}_i$ :
$$|f(x_1, \dots, x_{i-1}, x_i, x_{i+1}, \dots, x_n) - f(x_1, \dots, x_{i-1}, x'_i, x_{i+1}, \dots, x_n)| \le c_i$$

Géométriquement, cela signifie que si l'on remplace la $i$-ème coordonnée du vecteur $x$ par une autre valeur $x'_i$, la valeur de la fonction $f$ ne varie pas de plus de $c_i$. Cette condition s'interprète comme une forme de continuité de Lipschitz de la fonction $f$ par rapport à la métrique de Hamming pondérée sur l'espace produit $\mathcal{X}$.

#### Entropie d'une Variable Aléatoire
Soit $Z$ une variable aléatoire réelle positive ou nulle ($Z \ge 0$ presque sûrement) telle que $\mathbb{E}[Z \ln_+ Z] < \infty$. L'**entropie** de $Z$, notée $\text{Ent}(Z)$, est définie par :
$$\text{Ent}(Z) = \mathbb{E}[Z \ln Z] - \mathbb{E}[Z] \ln \mathbb{E}[Z]$$
avec la convention habituelle $0 \ln 0 = 0$.

Par l'inégalité de Jensen appliquée à la fonction strictement convexe $x \mapsto x \ln x$ sur $\mathbb{R}_+$, on garantit que pour toute variable aléatoire $Z$ non constante, $\text{Ent}(Z) \ge 0$, avec égalité si et seulement si $Z$ est presque sûrement constante.

#### Inégalité Log-Sobolev de Maurer / Méthode de l'Entropie
Dans le cadre de l'entropie de concentration, pour une fonction $f(X_1, \dots, X_n)$, on introduit les opérateurs d'espérance conditionnelle. Notons $\mathbb{E}_i$ l'espérance conditionnelle par rapport à toutes les variables sauf $X_i$ :
$$\mathbb{E}_i[Z] = \mathbb{E}[Z \mid X_1, \dots, X_{i-1}, X_{i+1}, \dots, X_n]$$
De même, on définit l'entropie conditionnelle $\text{Ent}_i(Z)$ comme :
$$\text{Ent}_i(Z) = \mathbb{E}_i[Z \ln Z] - \mathbb{E}_i[Z] \ln \mathbb{E}_i[Z]$$

L'une des propriétés fondamentales de l'entropie (connue sous le nom de sous-additivité de l'entropie, ou théorème de Han-Massart) stipule que :
$$\text{Ent}(Z) \le \mathbb{E}\left[ \sum_{i=1}^n \text{Ent}_i(Z) \right]$$

### B. Théorèmes, Propositions & Lemmes

> **Théorème 1 : Inégalité de McDiarmid (Colin McDiarmid, 1989) :**
> Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes à valeurs dans des ensembles $\mathcal{X}_1, \dots, \mathcal{X}_n$. 
> Soit $f : \prod_{i=1}^n \mathcal{X}_i \to \mathbb{R}$ une fonction satisfaisant la propriété des différences bornées avec les constantes $c_1, \dots, c_n$.
> Alors, pour tout $t > 0$ :
> $$\mathbb{P}\Big(f(X_1, \dots, X_n) - \mathbb{E}[f(X_1, \dots, X_n)] \ge t\Big) \le \exp\left( - \frac{2 t^2}{\sum_{i=1}^n c_i^2} \right)$$
> et de même pour la déviation inférieure :
> $$\mathbb{P}\Big(f(X_1, \dots, X_n) - \mathbb{E}[f(X_1, \dots, X_n)] \le -t\Big) \le \exp\left( - \frac{2 t^2}{\sum_{i=1}^n c_i^2} \right)$$
> ce qui implique par la borne de l'union la version bilatérale :
> $$\mathbb{P}\Big(|f(X) - \mathbb{E}[f(X)]| \ge t\Big) \le 2 \exp\left( - \frac{2 t^2}{\sum_{i=1}^n c_i^2} \right)$$

Ce théorème est extrêmement puissant car il ne formule aucune hypothèse sur la loi des variables $X_i$ (qui peuvent être discrètes, continues, ou définies sur des espaces de dimension infinie). La seule exigence est l'indépendance mutuelle des variables et la régularité Lipschitzienne locale de la fonction $f$.

> **Théorème 2 : Lemme de Herbst (Lien entre Log-Sobolev et Concentration) :**
> Soit $Y$ une variable aléatoire réelle. Supposons qu'il existe une constante $v > 0$ telle que pour tout $\lambda \ge 0$, l'entropie de la variable transformée $e^{\lambda Y}$ vérifie l'inégalité log-sobolévienne suivante :
> $$\text{Ent}(e^{\lambda Y}) \le \frac{\lambda^2 v}{2} \mathbb{E}[e^{\lambda Y}]$$
> Alors, pour tout $t > 0$, on a :
> $$\mathbb{P}(Y - \mathbb{E}[Y] \ge t) \le \exp\left( - \frac{t^2}{2 v} \right)$$

Le Lemme de Herbst montre que le contrôle de l'entropie permet d'obtenir un contrôle immédiat sur la transformée de Laplace de la variable aléatoire, et donc sur ses queues de distribution. C'est le fondement de la méthode moderne de l'entropie pour la concentration.

---

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas (minimum 500 mots)

### Démonstration du Théorème Pivot : Inégalité de McDiarmid

La stratégie de preuve repose sur la construction d'une martingale de Doob associée à la fonction $f$, suivie de l'application de l'inégalité d'Azuma-Hoeffding pour les martingales à accroissements bornés.

#### 1. Initialisation / Cadre
Soit $Y = f(X_1, \dots, X_n)$. Nous voulons borner la probabilité des grandes déviations de $Y$ par rapport à sa moyenne $\mathbb{E}[Y]$.
Introduisons la filtration naturelle $\mathcal{F}_0, \mathcal{F}_1, \dots, \mathcal{F}_n$ définie par :
- $\mathcal{F}_0 = \{\emptyset, \Omega\}$ (la tribu triviale)
- $\mathcal{F}_k = \sigma(X_1, \dots, X_k)$ pour tout $k \in \{1, \dots, n\}$.

Définissons la suite de variables aléatoires $Z_k$ par espérance conditionnelle successive (Martingale de Doob) :
$$Z_k = \mathbb{E}[Y \mid \mathcal{F}_k] = \mathbb{E}[f(X_1, \dots, X_n) \mid X_1, \dots, X_k]$$

Par construction :
- $Z_0 = \mathbb{E}[Y \mid \mathcal{F}_0] = \mathbb{E}[Y]$
- $Z_n = \mathbb{E}[Y \mid \mathcal{F}_n] = Y$ car le vecteur $X$ est entièrement déterminé par $X_1, \dots, X_n$.
La suite $(Z_k)_{k=0}^n$ est par définition une martingale par rapport à la filtration $(\mathcal{F}_k)_{k=0}^n$. En effet, par la propriété de projection de l'espérance conditionnelle (loi des attentes totales) :
$$\mathbb{E}[Z_k \mid \mathcal{F}_{k-1}] = \mathbb{E}[\mathbb{E}[Y \mid \mathcal{F}_k] \mid \mathcal{F}_{k-1}] = \mathbb{E}[Y \mid \mathcal{F}_{k-1}] = Z_{k-1}$$

Posons la suite des différences de martingale $D_k = Z_k - Z_{k-1}$ pour $k \in \{1, \dots, n\}$, de sorte que :
$$Y - \mathbb{E}[Y] = Z_n - Z_0 = \sum_{k=1}^n (Z_k - Z_{k-1}) = \sum_{k=1}^n D_k$$

#### 2. Étape 1 : Majoration uniforme des accroissements de la martingale
Pour appliquer l'inégalité de Hoeffding, nous devons prouver que chaque différence de martingale $D_k$ est presque sûrement bornée par un intervalle dont la longueur est reliée à la constante de McDiarmid $c_k$.

Soient $x_1, \dots, x_k$ les réalisations des variables $X_1, \dots, X_k$. Écrivons explicitement $Z_k$ et $Z_{k-1}$ sous forme d'intégrales par rapport aux lois des variables indépendantes restantes :
$$Z_k = \int f(x_1, \dots, x_k, x_{k+1}, \dots, x_n) d\mathbb{P}_{X_{k+1}} \dots d\mathbb{P}_{X_n}$$
$$Z_{k-1} = \int f(x_1, \dots, x_{k-1}, x'_k, x_{k+1}, \dots, x_n) d\mathbb{P}_{X_k}(x'_k) d\mathbb{P}_{X_{k+1}} \dots d\mathbb{P}_{X_n}$$

Définissons les bornes conditionnelles inférieure $L_k$ et supérieure $U_k$ sur la valeur de la variable $X_k$ en gelant les autres variables $X_1, \dots, X_{k-1}$ :
$$L_k(X_1, \dots, X_{k-1}) = \inf_{x \in \mathcal{X}_k} \mathbb{E}[f(X_1, \dots, X_{k-1}, x, X_{k+1}, \dots, X_n) \mid X_1, \dots, X_{k-1}]$$
$$U_k(X_1, \dots, X_{k-1}) = \sup_{y \in \mathcal{X}_k} \mathbb{E}[f(X_1, \dots, X_{k-1}, y, X_{k+1}, \dots, X_n) \mid X_1, \dots, X_{k-1}]$$

Puisque les variables aléatoires $X_i$ sont mutuellement indépendantes, l'infimum et le supremum ci-dessus ne dépendent pas des lois de probabilité de $X_{k+1}, \dots, X_n$. De plus, pour tous choix de $x, y \in \mathcal{X}_k$, la propriété des différences bornées appliquée à la coordonnée $k$ nous donne :
$$f(x_1, \dots, x_{k-1}, y, x_{k+1}, \dots, x_n) - f(x_1, \dots, x_{k-1}, x, x_{k+1}, \dots, x_n) \le c_k$$
En prenant l'espérance par rapport aux variables indépendantes $X_{k+1}, \dots, X_n$ de chaque côté de cette inégalité, nous obtenons :
$$\mathbb{E}[f(x_1, \dots, x_{k-1}, y, X_{k+1}, \dots, X_n)] - \mathbb{E}[f(x_1, \dots, x_{k-1}, x, X_{k+1}, \dots, X_n)] \le c_k$$
Comme cela est vrai pour tous $x, y \in \mathcal{X}_k$, nous en déduisons en passant au supremum sur $y$ et à l'infimum sur $x$ :
$$U_k(X_1, \dots, X_{k-1}) - L_k(X_1, \dots, X_{k-1}) \le c_k \quad \text{presque sûrement.}$$

#### 3. Étape 2 : Encadrement conditionnel de $D_k$
Remarquons maintenant que $Z_k$ est une valeur intermédiaire particulière de l'espérance où $X_k$ a été fixé à sa valeur aléatoire réalisée. Par conséquent, pour tout tirage, nous avons :
$$L_k(X_1, \dots, X_{k-1}) \le Z_k \le U_k(X_1, \dots, X_{k-1})$$
Puisque $Z_{k-1} = \mathbb{E}[Z_k \mid \mathcal{F}_{k-1}]$ est une espérance par rapport à la loi de $X_k$, cette quantité respecte également les mêmes bornes :
$$L_k(X_1, \dots, X_{k-1}) \le Z_{k-1} \le U_k(X_1, \dots, X_{k-1})$$

En soustrayant $Z_{k-1}$, nous obtenons les bornes suivantes pour la différence de martingale $D_k = Z_k - Z_{k-1}$ :
$$A_k \le D_k \le B_k$$
où nous posons :
$$A_k = L_k(X_1, \dots, X_{k-1}) - Z_{k-1}$$
$$B_k = U_k(X_1, \dots, X_{k-1}) - Z_{k-1}$$
Ces variables aléatoires $A_k$ et $B_k$ sont mesurables par rapport à la tribu $\mathcal{F}_{k-1}$.
L'amplitude de cet intervalle vérifie :
$$B_k - A_k = U_k(X_1, \dots, X_{k-1}) - L_k(X_1, \dots, X_{k-1}) \le c_k \quad \text{presque sûrement.}$$

#### 4. Étape 3 : Application du Lemme de Hoeffding Conditionnel
Le Lemme de Hoeffding classique affirme que si une variable aléatoire réelle $V$ est centrée et à valeurs dans $[a, b]$, alors pour tout $\lambda \in \mathbb{R}$, $\mathbb{E}[e^{\lambda V}] \le \exp(\frac{\lambda^2 (b-a)^2}{8})$.
Appliquons la version conditionnelle de ce lemme à la différence de martingale $D_k$. 
Puisque $\mathbb{E}[D_k \mid \mathcal{F}_{k-1}] = 0$ et que $A_k \le D_k \le B_k$ avec $B_k - A_k \le c_k$, nous avons pour tout $\lambda \ge 0$ :
$$\mathbb{E}[e^{\lambda D_k} \mid \mathcal{F}_{k-1}] \le \exp\left( \frac{\lambda^2 (B_k - A_k)^2}{8} \right) \le \exp\left( \frac{\lambda^2 c_k^2}{8} \right) \quad \text{presque sûrement.}$$

#### 5. Étape 4 : Majoration de la transformée de Laplace globale
Par la méthode de Chernoff, étudions la transformée de Laplace de $Y - \mathbb{E}[Y]$. Pour tout $\lambda \ge 0$ :
$$\mathbb{E}\left[ e^{\lambda (Y - \mathbb{E}[Y])} \right] = \mathbb{E}\left[ e^{\lambda \sum_{i=1}^n D_i} \right]$$

Conditionnons successivement par rapport aux tribus $\mathcal{F}_{n-1}, \mathcal{F}_{n-2}, \dots$ en utilisant la propriété d'espérance conditionnelle itérée :
$$\mathbb{E}\left[ e^{\lambda \sum_{i=1}^n D_i} \right] = \mathbb{E}\left[ \mathbb{E}\left[ e^{\lambda \sum_{i=1}^n D_i} \;\middle|\; \mathcal{F}_{n-1} \right] \right]$$
$$\mathbb{E}\left[ \mathbb{E}\left[ e^{\lambda \sum_{i=1}^n D_i} \;\middle|\; \mathcal{F}_{n-1} \right] \right] = \mathbb{E}\left[ e^{\lambda \sum_{i=1}^{n-1} D_i} \, \mathbb{E}\left[ e^{\lambda D_n} \;\middle|\; \mathcal{F}_{n-1} \right] \right]$$

Par l'inégalité obtenue à l'Étape 3 pour $k=n$ :
$$\mathbb{E}\left[ e^{\lambda \sum_{i=1}^n D_i} \right] \le \mathbb{E}\left[ e^{\lambda \sum_{i=1}^{n-1} D_i} \right] \exp\left( \frac{\lambda^2 c_n^2}{8} \right)$$

Par une récurrence descendante immédiate (appliquée de $k=n-1$ jusqu'à $k=1$) :
$$\mathbb{E}\left[ e^{\lambda (Y - \mathbb{E}[Y])} \right] \le \prod_{k=1}^n \exp\left( \frac{\lambda^2 c_k^2}{8} \right) = \exp\left( \frac{\lambda^2 \sum_{k=1}^n c_k^2}{8} \right)$$

#### 6. Étape 5 : Optimisation du paramètre de Chernoff (Synthèse)
En appliquant l'inégalité de Markov pour tout $\lambda \ge 0$ :
$$\mathbb{P}(Y - \mathbb{E}[Y] \ge t) = \mathbb{P}\left( e^{\lambda (Y - \mathbb{E}[Y])} \ge e^{\lambda t} \right) \le e^{-\lambda t} \mathbb{E}\left[ e^{\lambda (Y - \mathbb{E}[Y])} \right]$$
$$\mathbb{P}(Y - \mathbb{E}[Y] \ge t) \le e^{-\lambda t} \exp\left( \frac{\lambda^2 \sum_{k=1}^n c_k^2}{8} \right) = \exp\left( -\lambda t + \frac{\lambda^2 \sum_{k=1}^n c_k^2}{8} \right)$$

Cette inégalité est valable pour tout $\lambda \ge 0$. Minimisons l'exposant par rapport à $\lambda$. La fonction quadratique $g(\lambda) = -\lambda t + \frac{\lambda^2 \sum_{k=1}^n c_k^2}{8}$ atteint son minimum global au point d'annulation de sa dérivée :
$$-t + \frac{\lambda \sum_{k=1}^n c_k^2}{4} = 0 \implies \lambda^* = \frac{4 t}{\sum_{k=1}^n c_k^2} > 0$$

En injectant cette valeur optimale $\lambda^*$ dans l'inégalité :
$$\mathbb{P}(Y - \mathbb{E}[Y] \ge t) \le \exp\left( - \frac{4 t^2}{\sum_{k=1}^n c_k^2} + \frac{16 t^2 \sum_{k=1}^n c_k^2}{8 \left(\sum_{k=1}^n c_k^2\right)^2} \right) = \exp\left( - \frac{2 t^2}{\sum_{k=1}^n c_k^2} \right)$$

La démonstration est identique pour la déviation inférieure en considérant la variable $-Y$. Par symétrie, l'inégalité bilatérale est prouvée sans aucune ellipse.

---

## 4. Exercices d'Application & Pratique de Concours (minimum 500 mots)

### Exercice 1 : Concentration du Risque Empirique Généralisé en Apprentissage

**Énoncé :**
Soit $\mathcal{H}$ une classe de fonctions d'apprentissage de $\mathcal{X}$ dans $[0, 1]$.
On dispose d'un échantillon $S_n = (X_1, \dots, X_n)$ de variables indépendantes et identiquement distribuées (i.i.d.) selon une distribution inconnue $\mathbb{P}$.
Pour toute fonction $h \in \mathcal{H}$, on note $R(h) = \mathbb{E}_{X \sim \mathbb{P}}[h(X)]$ le risque théorique et $R_n(h) = \frac{1}{n} \sum_{i=1}^n h(X_i)$ le risque empirique.
Définissons la variable aléatoire représentant l'écart de généralisation maximal sur la classe :
$$\Phi(S_n) = \sup_{h \in \mathcal{H}} \big( R(h) - R_n(h) \big)$$
Démontrer que $\Phi(S_n)$ vérifie une inégalité de concentration de type McDiarmid et expliciter la borne de déviation pour tout $t > 0$.

**Correction Détaillée :**

* *Analyse de l'énoncé :*
L'objectif est d'étudier la concentration de la variable aléatoire $\Phi(S_n)$ qui dépend de l'échantillon aléatoire $S_n \in \mathcal{X}^n$. Nous devons vérifier si la fonction $\Phi : \mathcal{X}^n \to \mathbb{R}$ satisfait la condition des différences bornées de McDiarmid. L'aléa réside dans le choix de l'échantillon $S_n$.

* *Résolution pas-à-pas :*
Soient $s = (x_1, \dots, x_n)$ et $s^{(i)} = (x_1, \dots, x_{i-1}, x'_i, x_{i+1}, \dots, x_n)$ deux échantillons qui ne diffèrent que par leur $i$-ème coordonnée.
Développons la différence $\Phi(s) - \Phi(s^{(i)})$ :
$$\Phi(s) - \Phi(s^{(i)}) = \sup_{h \in \mathcal{H}} \left( R(h) - \frac{1}{n} \sum_{j=1}^n h(x_j) \right) - \sup_{h \in \mathcal{H}} \left( R(h) - \frac{1}{n} \sum_{j \neq i} h(x_j) - \frac{1}{n} h(x'_i) \right)$$

Utilisons la propriété sous-additive classique du supremum : pour toutes fonctions réelles $u$ et $v$, $\sup_h u(h) - \sup_h v(h) \le \sup_h (u(h) - v(h))$.
Posons $u(h) = R(h) - \frac{1}{n} \sum_{j=1}^n h(x_j)$ et $v(h) = R(h) - \frac{1}{n} \sum_{j \neq i} h(x_j) - \frac{1}{n} h(x'_i)$.
Alors :
$$\Phi(s) - \Phi(s^{(i)}) \le \sup_{h \in \mathcal{H}} \left( R(h) - \frac{1}{n} \sum_{j=1}^n h(x_j) - \left( R(h) - \frac{1}{n} \sum_{j \neq i} h(x_j) - \frac{1}{n} h(x'_i) \right) \right)$$
$$\Phi(s) - \Phi(s^{(i)}) \le \sup_{h \in \mathcal{H}} \left( \frac{1}{n} h(x'_i) - \frac{1}{n} h(x_i) \right) = \frac{1}{n} \sup_{h \in \mathcal{H}} \big( h(x'_i) - h(x_i) \big)$$

Puisque les fonctions de la classe $\mathcal{H}$ sont à valeurs dans $[0, 1]$, pour tout $h \in \mathcal{H}$, nous avons la borne $0 \le h(x) \le 1$. D'où :
$$h(x'_i) - h(x_i) \le 1 - 0 = 1$$
Ce qui implique :
$$\Phi(s) - \Phi(s^{(i)}) \le \frac{1}{n}$$

Par symétrie des rôles joués par $s$ et $s^{(i)}$ (en inversant simplement l'inégalité et en appliquant le même raisonnement), on obtient également :
$$\Phi(s^{(i)}) - \Phi(s) \le \frac{1}{n}$$
D'où l'inégalité absolue sur la perturbation d'une coordonnée :
$$|\Phi(s) - \Phi(s^{(i)})| \le \frac{1}{n}$$

La fonction $\Phi$ satisfait la propriété des différences bornées avec les constantes uniformes $c_i = \frac{1}{n}$ pour tout $i \in \{1, \dots, n\}$.
Calculons le dénominateur de l'exposant de McDiarmid :
$$\sum_{i=1}^n c_i^2 = \sum_{i=1}^n \left(\frac{1}{n}\right)^2 = n \times \frac{1}{n^2} = \frac{1}{n}$$

Par application directe du Théorème de McDiarmid, nous concluons que pour tout $t > 0$ :
$$\mathbb{P}\Big(\Phi(S_n) - \mathbb{E}[\Phi(S_n)] \ge t\Big) \le \exp\left( - \frac{2 t^2}{1/n} \right) = \exp\big( - 2 n t^2 \big)$$
et
$$\mathbb{P}\Big(\big|\Phi(S_n) - \mathbb{E}[\Phi(S_n)]\big| \ge t\Big) \le 2 \exp\big( - 2 n t^2 \big)$$
L'exercice est résolu de manière complète et rigoureuse.

---

### Exercice 2 : Concentration de la Plus Longue Sous-Suite Croissante (Niveau ENS)

**Énoncé :**
Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes distribuées de manière uniforme sur l'intervalle $[0, 1]$.
Soit $L_n = L(X_1, \dots, X_n)$ la longueur de la plus longue sous-suite strictement croissante de la suite $(X_1, \dots, X_n)$.
1. Montrer que $L$ vérifie la propriété des différences bornées avec des constantes $c_i$ que l'on déterminera.
2. En déduire une borne supérieure pour la probabilité de déviation de $L_n$ par rapport à sa moyenne $\mathbb{E}[L_n]$.

**Correction Détaillée :**

* *Analyse de l'énoncé :*
La fonction $L(X_1, \dots, X_n)$ recherche le cardinal maximal d'un sous-ensemble d'indices $I \subseteq \{1, \dots, n\}$ tel que pour tous $i, j \in I$ avec $i < j$, on ait $X_i < X_j$. Nous devons analyser comment la modification d'une seule valeur $X_k$ influe sur la longueur de cette sous-suite.

* *Résolution pas-à-pas :*
1. Soit $x = (x_1, \dots, x_n)$ une suite de nombres réels distincts. Soit $x'_k$ une valeur réelle alternative remplaçant $x_k$. Notons $x^{(k)} = (x_1, \dots, x_{k-1}, x'_k, x_{k+1}, \dots, x_n)$.
Soit $S$ la plus longue sous-suite croissante de $x$, de longueur $L(x)$.
- Si la coordonnée $x_k$ n'appartient pas à la sous-suite optimale $S$, alors $S$ reste une sous-suite croissante valide pour le vecteur modifié $x^{(k)}$. Donc $L(x^{(k)}) \ge L(x)$.
- Si la coordonnée $x_k$ appartient à la sous-suite optimale $S$, alors en retirant $x_k$ de cette suite, on obtient une sous-suite croissante de longueur $L(x) - 1$ qui ne fait intervenir que les coordonnées $x_j$ pour $j \neq k$. Cette sous-suite amputée reste une sous-suite croissante valide pour le vecteur modifié $x^{(k)}$, quelle que soit la nouvelle valeur $x'_k$. Donc $L(x^{(k)}) \ge L(x) - 1$.
Dans tous les cas, nous venons d'établir que :
$$L(x^{(k)}) \ge L(x) - 1 \implies L(x) - L(x^{(k)}) \le 1$$

Par symétrie mathématique rigoureuse, en échangeant les rôles de $x$ et $x^{(k)}$ (ce qui revient à remplacer $x'_k$ par $x_k$), nous obtenons l'inégalité inverse :
$$L(x) \ge L(x^{(k)}) - 1 \implies L(x^{(k)}) - L(x) \le 1$$

En combinant ces deux inégalités unilatérales, nous prouvons que pour tout $k \in \{1, \dots, n\}$ :
$$|L(x) - L(x^{(k)})| \le 1$$
La fonction de longueur $L$ vérifie donc la propriété des différences bornées de McDiarmid avec les constantes uniformes $c_k = 1$ pour tout $k \in \{1, \dots, n\}$.

2. Calculons la somme des constantes au carré :
$$\sum_{k=1}^n c_k^2 = \sum_{k=1}^n 1^2 = n$$

En appliquant le théorème de McDiarmid, nous obtenons immédiatement la borne de concentration pour tout $t > 0$ :
$$\mathbb{P}\Big(|L_n - \mathbb{E}[L_n]| \ge t\Big) \le 2 \exp\left( - \frac{2 t^2}{n} \right)$$

*Remarque d'excellence :* Bien que la moyenne $\mathbb{E}[L_n]$ croisse comme $2\sqrt{n}$ quand $n \to \infty$ (théorème de Vershik-Kerov-Logan-Shepp), l'inégalité de McDiarmid nous montre que les fluctuations autour de cette moyenne sont d'un ordre de grandeur au plus $\sqrt{n}$. (En réalité, des analyses plus poussées via l'entropie montrent que les fluctuations sont d'ordre $n^{1/6}$ selon la loi de Tracy-Widom, mais McDiarmid fournit déjà une borne non asymptotique très puissante).

---

## 5. Ancrage & Application en Intelligence Artificielle (minimum 500 mots)

### Le Pont Théorique
Dans la théorie de l'apprentissage statistique (Statistical Learning Theory), l'objectif principal est de garantir qu'un modèle entraîné sur un jeu de données fini présentera des performances similaires sur de nouvelles données futures. Ce problème se formalise par l'étude de la convergence uniforme du risque empirique vers le risque réel sur l'ensemble de la classe d'hypothèses $\mathcal{H}$.

Pour démontrer ces garanties, on utilise la complexité de Rademacher ou la dimension VC. Cependant, la complexité de Rademacher empirique $\widehat{\mathcal{R}}_S(\mathcal{H})$ est elle-même une variable aléatoire qui dépend du choix de l'échantillon $S$. Pour que cette borne soit exploitable en pratique, il est nécessaire de prouver que la complexité de Rademacher empirique se concentre fortement autour de son espérance théorique $\mathcal{R}_n(\mathcal{H}) = \mathbb{E}[\widehat{\mathcal{R}}_S(\mathcal{H})]$.

C'est ici que l'inégalité de McDiarmid intervient comme le pivot mathématique incontournable. En montrant que la fonction qui associe à un échantillon $S$ sa complexité de Rademacher empirique respecte la propriété des différences bornées, on garantit que pour presque tout échantillon tiré, la complexité empirique calculée est un estimateur fiable de la complexité théorique. Sans cette concentration, les bornes de généralisation ne tiendraient pas, car l'écart entre théorie et pratique fluctuerait de manière incontrôlable d'un échantillon à un autre.

### Exemple Concret : Concentration de la Complexité de Rademacher Empirique

Soit $\mathcal{H}$ une classe de fonctions définies sur $\mathcal{X}$ à valeurs dans $[-B, B]$ avec $B > 0$.
Soit $S = (X_1, \dots, X_n)$ un échantillon de variables aléatoires i.i.d. suivant une distribution $\mathbb{P}$.
La complexité de Rademacher empirique de la classe $\mathcal{H}$ sur l'échantillon $S$ est définie par :
$$\widehat{\mathcal{R}}_S(\mathcal{H}) = \mathbb{E}_{\boldsymbol{\sigma}}\left[ \sup_{h \in \mathcal{H}} \frac{1}{n} \sum_{i=1}^n \sigma_i h(X_i) \right]$$
où $\boldsymbol{\sigma} = (\sigma_1, \dots, \sigma_n)$ est un vecteur de variables de Rademacher indépendantes ($\mathbb{P}(\sigma_i = 1) = \mathbb{P}(\sigma_i = -1) = 1/2$), indépendantes des $X_i$.

Analysons la sensibilité de la fonction $g(S) = \widehat{\mathcal{R}}_S(\mathcal{H})$ par rapport au remplacement d'un point $X_k$ par $X'_k$.
Soit $S^{(k)} = (X_1, \dots, X_{k-1}, X'_k, X_{k+1}, \dots, X_n)$.
$$g(S) - g(S^{(k)}) = \mathbb{E}_{\boldsymbol{\sigma}}\left[ \sup_{h \in \mathcal{H}} \frac{1}{n} \sum_{i=1}^n \sigma_i h(X_i) \right] - \mathbb{E}_{\boldsymbol{\sigma}}\left[ \sup_{h \in \mathcal{H}} \frac{1}{n} \left( \sum_{i \neq k} \sigma_i h(X_i) + \sigma_k h(X'_k) \right) \right]$$

Par linéarité de l'espérance et sous-additivité du supremum :
$$g(S) - g(S^{(k)}) \le \mathbb{E}_{\boldsymbol{\sigma}}\left[ \sup_{h \in \mathcal{H}} \left( \frac{1}{n} \sum_{i=1}^n \sigma_i h(X_i) - \frac{1}{n} \left( \sum_{i \neq k} \sigma_i h(X_i) + \sigma_k h(X'_k) \right) \right) \right]$$
$$g(S) - g(S^{(k)}) \le \mathbb{E}_{\boldsymbol{\sigma}}\left[ \sup_{h \in \mathcal{H}} \frac{\sigma_k \big( h(X_k) - h(X'_k) \big)}{n} \right]$$

Puisque $\sigma_k \in \{-1, +1\}$ et $|h(x)| \le B$, la quantité $\sigma_k \big( h(X_k) - h(X'_k) \big)$ est bornée supérieurement par $2B$ (que $\sigma_k$ vaille $1$ ou $-1$, il suffit de choisir le signe correspondant pour maximiser la différence). 
D'où :
$$g(S) - g(S^{(k)}) \le \mathbb{E}_{\boldsymbol{\sigma}}\left[ \frac{2B}{n} \right] = \frac{2B}{n}$$

Par symétrie, nous obtenons également $g(S^{(k)}) - g(S) \le \frac{2B}{n}$.
Ainsi, la complexité de Rademacher empirique vérifie la propriété des différences bornées de McDiarmid avec les constantes uniformes :
$$c_i = \frac{2B}{n} \quad \forall i \in \{1, \dots, n\}$$

Calculons la somme de ces constantes au carré :
$$\sum_{i=1}^n c_i^2 = n \times \left(\frac{2B}{n}\right)^2 = \frac{4 B^2}{n}$$

En appliquant l'inégalité de McDiarmid, nous pouvons affirmer que pour tout $t > 0$ :
$$\mathbb{P}\left( \widehat{\mathcal{R}}_S(\mathcal{H}) - \mathbb{E}[\widehat{\mathcal{R}}_S(\mathcal{H})] \ge t \right) \le \exp\left( - \frac{2 t^2}{4 B^2 / n} \right) = \exp\left( - \frac{n t^2}{2 B^2} \right)$$
et de même pour la déviation bilatérale :
$$\mathbb{P}\left( \big|\widehat{\mathcal{R}}_S(\mathcal{H}) - \mathbb{E}[\widehat{\mathcal{R}}_S(\mathcal{H})]\big| \ge t \right) \le 2 \exp\left( - \frac{n t^2}{2 B^2} \right)$$

Ce résultat démontre de manière rigoureuse que la complexité de Rademacher calculée sur un échantillon empirique est extrêmement proche de sa valeur théorique attendue dès que $n$ devient grand. C'est le théorème clé qui valide l'utilisation pratique des bornes de généralisation dans l'apprentissage automatique moderne.

---

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 91 (Inégalités de concentration)]], [[Jalon 135 (Complexite de Rademacher)]], [[Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC)]]
- **Concepts Futurs dépendants :** [[Jalon 139 (Notion de stabilité algorithmique)]], [[Jalon 141 (Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC.)]]
