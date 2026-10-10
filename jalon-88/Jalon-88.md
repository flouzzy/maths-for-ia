---
uuid: "jalon-88"
title: "Indépendance d'événements et de variables aléatoires"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/fondations
prev: "[[Jalon 87 (Intégration des variables aléatoires).md]]"
next: "[[Jalon 89 (Lemmes de Borel-Cantelli).md]]"
---

# Jalon 88 : Indépendance d'événements et de variables aléatoires

## 1. Introduction historique et conceptuelle

Historiquement, la notion d'indépendance émerge des premiers travaux sur les jeux de hasard menés par Pascal et Fermat au XVIIe siècle, puis axiomatisée bien plus tard par Kolmogorov en 1933. L'intuition physique est fondamentale : si l'on lance deux dés à des années-lumière de distance, l'état de l'un ne contient aucune information sur l'état de l'autre. L'indépendance traduit l'absence de corrélation, l'absence d'influence causale, ou plus rigoureusement l'orthogonalité probabiliste.

C'est cette notion qui permet la décomposition des grands systèmes complexes. Si les particules d'un gaz idéal ne s'influencent pas à distance, on peut calculer l'entropie du système entier simplement comme la somme des entropies individuelles. En mathématiques, l'indépendance est la clé de voûte qui permet de remplacer les intersections d'événements par de simples multiplications de probabilités, rendant ainsi le calcul analytiquement possible.

## 2. Définitions, Théorèmes et Exemples

Nous nous plaçons dans un espace probabilisé ($\Omega, \mathcal{F}, \mathbb{P}$).

### 2.1 Indépendance de deux événements

**Définition 1 (Indépendance d'événements).** Deux événements $A, B \in \mathcal{F}$ sont dits indépendants si, et seulement si, on a l'égalité :
$$ \mathbb{P}(A \cap B) = \mathbb{P}(A) \mathbb{P}(B) $$

Si $\mathbb{P}(B) > 0$, cela équivaut à écrire que la probabilité conditionnelle $\mathbb{P}(A|B)$ est égale à $\mathbb{P}(A)$.

**Exemple concret 1 : Le jeu de dés**
Considérons le lancer d'un dé équilibré à 6 faces. $\Omega = \{1, 2, 3, 4, 5, 6\}$.
Soit $A = \text{« obtenir un nombre pair »} = \{2, 4, 6\}$ et $B = \text{« obtenir un multiple de 3 »} = \{3, 6\}$.
On calcule $\mathbb{P}(A) = \frac{3}{6} = \frac{1}{2}$ et $\mathbb{P}(B) = \frac{2}{6} = \frac{1}{3}$.
L'intersection est $A \cap B = \{6\}$, donc $\mathbb{P}(A \cap B) = \frac{1}{6}$.
On vérifie que $\mathbb{P}(A)\mathbb{P}(B) = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$.
Les événements $A$ et $B$ sont bien indépendants.

**Contre-exemple (Cas de dépendance) :**
Soit $C = \text{« obtenir un nombre premier »} = \{2, 3, 5\}$. $\mathbb{P}(C) = \frac{1}{2}$.
$A \cap C = \{2\}$, d'où $\mathbb{P}(A \cap C) = \frac{1}{6}$.
Cependant, $\mathbb{P}(A)\mathbb{P}(C) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} \neq \frac{1}{6}$.
$A$ et $C$ ne sont pas indépendants. Le fait de savoir que le résultat est pair diminue les chances qu'il soit premier.

### 2.2 Mutuelle indépendance

**Définition 2 (Indépendance mutuelle).** Une famille d'événements $(A_i)_{i \in I}$ est mutuellement indépendante si, pour tout sous-ensemble fini $J \subseteq I$, on a :
$$ \mathbb{P}\left(\bigcap_{j \in J} A_j\right) = \prod_{j \in J} \mathbb{P}(A_j) $$

**Remarque cruciale sur les cas limites :**
L'indépendance deux à deux n'implique **pas** l'indépendance mutuelle.
**Exemple 2 : Indépendance deux à deux $\nRightarrow$ mutuelle**
Soit $\Omega = \{1, 2, 3, 4\}$ muni de la probabilité uniforme.
Considérons $A = \{1, 2\}$, $B = \{1, 3\}$, et $C = \{1, 4\}$.
$\mathbb{P}(A) = \mathbb{P}(B) = \mathbb{P}(C) = \frac{1}{2}$.
$\mathbb{P}(A \cap B) = \mathbb{P}(\{1\}) = \frac{1}{4} = \mathbb{P}(A)\mathbb{P}(B)$. (Même chose pour $A,C$ et $B,C$). Les événements sont indépendants deux à deux.
Cependant, $\mathbb{P}(A \cap B \cap C) = \mathbb{P}(\{1\}) = \frac{1}{4}$.
Mais $\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C) = \frac{1}{8}$. Donc $\frac{1}{4} \neq \frac{1}{8}$, la famille n'est pas mutuellement indépendante.

### 2.3 Indépendance des tribus et variables aléatoires

**Définition 3 (Indépendance de tribus).** Deux sous-tribus $\mathcal{F}_1, \mathcal{F}_2 \subset \mathcal{F}$ sont indépendantes si pour tout $A \in \mathcal{F}_1$ et $B \in \mathcal{F}_2$, les événements $A$ et $B$ sont indépendants.

**Définition 4 (Indépendance de variables aléatoires).** Deux variables aléatoires réelles $X$ et $Y$ définies sur $(\Omega, \mathcal{F}, \mathbb{P})$ sont indépendantes si les tribus qu'elles engendrent $\sigma(X)$ et $\sigma(Y)$ sont indépendantes. Concrètement, pour tous boréliens $B_1, B_2 \in \mathcal{B}(\mathbb{R})$ :
$$ \mathbb{P}(X \in B_1 \cap Y \in B_2) = \mathbb{P}(X \in B_1) \mathbb{P}(Y \in B_2) $$

**Exemple concret 3 : Variables de Bernoulli indépendantes**
Soit $X \sim \mathcal{B}(p_1)$ et $Y \sim \mathcal{B}(p_2)$ représentant le succès de deux expériences distinctes. Si $X$ et $Y$ sont indépendantes, la probabilité d'avoir un double succès est $\mathbb{P}(X=1, Y=1) = \mathbb{P}(X=1)\mathbb{P}(Y=1) = p_1 p_2$.

**Théorème 1 (Espérance du produit).** Soient $X$ et $Y$ deux variables aléatoires réelles intégrables et indépendantes. Alors leur produit $XY$ est intégrable et :
$$ \mathbb{E}[XY] = \mathbb{E}[X] \mathbb{E}[Y] $$

**Exemple concret 4 : Covariance nulle**
Calculons la covariance : $\text{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.
Grâce au Théorème 1, si $X$ et $Y$ sont indépendantes, $\text{Cov}(X, Y) = 0$.
Toutefois, la réciproque est **fausse**.
Soit $X \sim \mathcal{U}(\{-1, 0, 1\})$. $\mathbb{E}[X] = 0$.
Posons $Y = X^2$. $Y$ prend les valeurs $0, 1$ avec $\mathbb{P}(Y=0)=1/3$ et $\mathbb{P}(Y=1)=2/3$.
Calculons $\mathbb{E}[XY] = \mathbb{E}[X^3]$. Puisque $X^3 = X$ (car $x \in \{-1,0,1\}$), $\mathbb{E}[XY] = \mathbb{E}[X] = 0$.
Ainsi, $\text{Cov}(X,Y) = 0 - 0 = 0$.
Mais $X$ et $Y$ ne sont pas indépendantes : $\mathbb{P}(X=0 \cap Y=1) = 0 \neq \mathbb{P}(X=0)\mathbb{P}(Y=1) = \frac{1}{3} \times \frac{2}{3}$.

**Théorème 2 (Variance de la somme).** Si $X$ et $Y$ sont des variables aléatoires de carré intégrable et indépendantes, alors :
$$ \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) $$
*Preuve directe :* $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$. Comme l'indépendance implique une covariance nulle, le terme croisé disparaît.

**Exemple concret 5 : Variables de Poisson**
Soit $X \sim \mathcal{P}(\lambda)$ et $Y \sim \mathcal{P}(\mu)$ indépendantes.
$\mathbb{E}[X] = \text{Var}(X) = \lambda$. $\mathbb{E}[Y] = \text{Var}(Y) = \mu$.
Alors la somme $Z = X+Y$ a pour variance $\text{Var}(Z) = \lambda + \mu$. (Nous verrons dans les démonstrations que $Z \sim \mathcal{P}(\lambda + \mu)$).

## 3. Démonstrations

### 3.1 Démonstration du Théorème 1 (Espérance du produit)

**Hypothèses :** $X$ et $Y$ sont indépendantes et intégrables.
**Objectif :** Montrer que $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.

1. **Par les fonctions étagées :**
   Soit $X = \sum_{i=1}^n x_i \mathbf{1}_{A_i}$ et $Y = \sum_{j=1}^m y_j \mathbf{1}_{B_j}$ deux variables aléatoires simples. Les $(A_i)$ forment une partition de $\Omega$, de même que les $(B_j)$.
   L'indépendance de $X$ et $Y$ signifie que $\mathbb{P}(A_i \cap B_j) = \mathbb{P}(A_i)\mathbb{P}(B_j)$ pour tout $i, j$.
2. **Calcul de l'espérance du produit :**
   Le produit s'écrit :
   $$ XY = \left( \sum_{i=1}^n x_i \mathbf{1}_{A_i} \right) \left( \sum_{j=1}^m y_j \mathbf{1}_{B_j} \right) = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbf{1}_{A_i \cap B_j} $$
   Par linéarité de l'espérance :
   $$ \mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{P}(A_i \cap B_j) $$
3. **Utilisation de l'indépendance :**
   $$ \mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{P}(A_i)\mathbb{P}(B_j) $$
4. **Factorisation :**
   $$ \mathbb{E}[XY] = \left( \sum_{i=1}^n x_i \mathbb{P}(A_i) \right) \left( \sum_{j=1}^m y_j \mathbb{P}(B_j) \right) = \mathbb{E}[X] \mathbb{E}[Y] $$
5. **Passage à la limite :**
   Pour des variables positives quelconques, on utilise une suite de variables étagées $(X_n)$ croissant vers $X$, et $(Y_n)$ croissant vers $Y$. Par le théorème de convergence monotone de Beppo-Levi, $\mathbb{E}[X_n Y_n]$ converge vers $\mathbb{E}[XY]$. Comme $\mathbb{E}[X_n Y_n] = \mathbb{E}[X_n]\mathbb{E}[Y_n]$, la limite donne bien $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.
   Enfin, on décompose pour $X = X^+ - X^-$ et $Y = Y^+ - Y^-$ pour étendre le résultat à toutes les variables intégrables.

### 3.2 Démonstration : Stabilité de la loi de Poisson par addition

**Hypothèses :** $X \sim \mathcal{P}(\lambda)$ et $Y \sim \mathcal{P}(\mu)$ sont indépendantes.
**Objectif :** Montrer que $X+Y \sim \mathcal{P}(\lambda + \mu)$.

1. **Expression de la probabilité :**
   Soit $n \in \mathbb{N}$. L'événement $\{X+Y = n\}$ peut se décomposer sur toutes les valeurs possibles de $X$, qui vont de $0$ à $n$.
   $$ \mathbb{P}(X+Y = n) = \sum_{k=0}^n \mathbb{P}(X=k, Y=n-k) $$
2. **Utilisation de l'indépendance :**
   $$ \mathbb{P}(X+Y = n) = \sum_{k=0}^n \mathbb{P}(X=k) \mathbb{P}(Y=n-k) $$
3. **Remplacement par les formules de Poisson :**
   $$ \mathbb{P}(X+Y = n) = \sum_{k=0}^n \left( e^{-\lambda} \frac{\lambda^k}{k!} \right) \left( e^{-\mu} \frac{\mu^{n-k}}{(n-k)!} \right) $$
4. **Réarrangement algébrique :**
   On sort les constantes de la somme :
   $$ \mathbb{P}(X+Y = n) = e^{-(\lambda + \mu)} \sum_{k=0}^n \frac{\lambda^k \mu^{n-k}}{k! (n-k)!} $$
5. **Reconnaissance du Binôme de Newton :**
   On multiplie et on divise par $n!$ pour faire apparaître les coefficients binomiaux :
   $$ \mathbb{P}(X+Y = n) = \frac{e^{-(\lambda + \mu)}}{n!} \sum_{k=0}^n \frac{n!}{k! (n-k)!} \lambda^k \mu^{n-k} $$
   $$ \mathbb{P}(X+Y = n) = \frac{e^{-(\lambda + \mu)}}{n!} \sum_{k=0}^n \binom{n}{k} \lambda^k \mu^{n-k} $$
   D'après la formule du binôme de Newton, la somme vaut $(\lambda + \mu)^n$.
   $$ \mathbb{P}(X+Y = n) = e^{-(\lambda + \mu)} \frac{(\lambda + \mu)^n}{n!} $$
6. **Conclusion :** On reconnaît exactement la formule de la loi de Poisson de paramètre $\lambda + \mu$.

## 4. Applications en Physique, Logique et Intelligence Artificielle

### Mécanique Statistique et Physique Quantique
En physique statistique de Maxwell-Boltzmann, l'hypothèse d'indépendance des chocs entre particules (le Stosszahlansatz) est nécessaire pour dériver l'équation de Boltzmann. Sans cette hypothèse, le théorème H prouvant l'augmentation de l'entropie s'effondre. En physique quantique, l'intrication représente précisément la violation pure de l'indépendance probabiliste classique, prouvée par la violation des inégalités de Bell.

### Intelligence Artificielle : Hypothèse i.i.d. et Vraisemblance
L'ensemble de l'apprentissage automatique repose sur l'hypothèse que les données d'entraînement $(x_1, y_1), \dots, (x_N, y_N)$ sont i.i.d. (Indépendantes et Identiquement Distribuées).
Si l'on cherche les paramètres $\theta$ qui maximisent la vraisemblance des données $\mathbb{P}(X | \theta)$, l'indépendance permet d'écrire la probabilité conjointe du dataset comme un simple produit :
$$ \mathcal{L}(\theta) = \prod_{i=1}^N \mathbb{P}(x_i | \theta) $$
Le calcul analytique des gradients d'un produit est numériquement instable (underflow). On utilise donc le logarithme, qui transforme le produit en somme (la log-vraisemblance) :
$$ \log \mathcal{L}(\theta) = \sum_{i=1}^N \log \mathbb{P}(x_i | \theta) $$
C'est la fondation de la fonction de perte Cross-Entropy.

### Intelligence Artificielle : Naive Bayes
Le classifieur de Bayes Naïf prend un vecteur d'entrée $x = (x_1, x_2, \dots, x_d)$ et veut prédire une classe $C$. Par le théorème de Bayes :
$$ \mathbb{P}(C | x) \propto \mathbb{P}(C) \mathbb{P}(x_1, \dots, x_d | C) $$
L'algorithme fait l'hypothèse très forte (naïve) que les composantes $x_j$ sont conditionnellement indépendantes sachant $C$ :
$$ \mathbb{P}(C | x) \propto \mathbb{P}(C) \prod_{j=1}^d \mathbb{P}(x_j | C) $$
Cette approximation drastique transforme un problème insoluble en un calcul très rapide, et reste paradoxalement très efficace pour la classification de textes.

### Intelligence Artificielle : Dropout dans les Réseaux de Neurones
Durant la rétropropagation (Backpropagation), pour éviter le sur-apprentissage (overfitting), le Dropout "éteint" certains neurones avec une probabilité $p$, de manière totalement indépendante les uns des autres. Cette injection d'indépendance artificielle force le réseau à apprendre des caractéristiques redondantes et brise la co-adaptation (dépendance) excessive entre les neurones.
