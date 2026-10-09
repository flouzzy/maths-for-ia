---
uuid: "jalon-87"
title: "Intégration et Espérance mathématique"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 86 (Variables aléatoires vues comme des applications mesurables).md]]"
next: "[[Jalon 88 (Indépendance d'événements).md]]"
---

# Jalon 87 : Intégration et Espérance Mathématique

## 1. Genèse et Intuition Physique

Historiquement, la notion d'espérance mathématique prend sa source dans les problèmes de jeux de hasard posés à Blaise Pascal et Pierre de Fermat au XVIIe siècle par le Chevalier de Méré, notamment le fameux « problème des partis ». Il s'agissait de répartir équitablement les mises lors de l'interruption prématurée d'une partie. Plus tard, Christian Huygens formalisa cette idée dans son traité *De ratiociniis in ludo aleae* (1657), définissant l'espérance comme la valeur que l'on devrait payer pour avoir le droit de jouer à un jeu, s'assurant ainsi que le jeu soit équitable sur le long terme.

D'un point de vue physique, l'espérance mathématique est directement analogue à la notion de centre de gravité (ou centre de masse) d'un système matériel en mécanique. Si l'on imagine la droite réelle comme une tige sans masse et que l'on place des masses ponctuelles (les probabilités) en différents points (les valeurs prises par la variable aléatoire), l'espérance correspond exactement au point d'équilibre de la tige. Cette vision géométrique permet de comprendre immédiatement que l'espérance se situe toujours entre les valeurs extrêmes prises par la variable.

Avec l'avènement de la théorie de la mesure par Andreï Kolmogorov dans les années 1930, l'espérance a trouvé son cadre formel définitif et rigoureux : elle n'est ni plus ni moins que l'intégrale de Lebesgue de la variable aléatoire (vue comme une fonction mesurable) par rapport à la mesure de probabilité sur l'espace d'états.

## 2. Définitions, Théorèmes et Exemples

### A. Intégration et Espérance Mathématique

Le cadre fondamental est un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$, où $\Omega$ est l'univers des possibles, $\mathcal{F}$ une tribu d'événements, et $\mathbb{P}$ une mesure de probabilité. Une variable aléatoire réelle $X$ est une application mesurable de $(\Omega, \mathcal{F})$ dans $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

**Définition 1 (Espérance d'une variable aléatoire positive) :**
Soit $X : \Omega \to \mathbb{R}^+$ une variable aléatoire positive. L'espérance de $X$, notée $\mathbb{E}[X]$, est définie par l'intégrale de Lebesgue de $X$ par rapport à $\mathbb{P}$ :
$$ \mathbb{E}[X] = \int_{\Omega} X(\omega) \, \mathrm{d}\mathbb{P}(\omega) $$
Cette valeur appartient à $[0, +\infty]$.

**Définition 2 (Variables aléatoires intégrables) :**
Une variable aléatoire réelle $X$ quelconque (pouvant prendre des valeurs négatives) s'écrit $X = X^+ - X^-$, où $X^+ = \max(X, 0)$ et $X^- = \max(-X, 0)$.
On dit que $X$ est intégrable si $\mathbb{E}[X^+] < +\infty$ et $\mathbb{E}[X^-] < +\infty$, ce qui équivaut à $\mathbb{E}[|X|] < +\infty$.
Dans ce cas, on définit l'espérance de $X$ par :
$$ \mathbb{E}[X] = \mathbb{E}[X^+] - \mathbb{E}[X^-] = \int_{\Omega} X \, \mathrm{d}\mathbb{P} $$
L'espace des variables aléatoires réelles intégrables est noté $\mathcal{L}^1(\Omega, \mathcal{F}, \mathbb{P})$.

**Exemple concret immédiat :**
Considérons le lancement d'un dé équilibré à $6$ faces. L'univers est $\Omega = \{1, 2, 3, 4, 5, 6\}$, muni de la tribu $\mathcal{F} = \mathcal{P}(\Omega)$ et de la probabilité uniforme $\mathbb{P}(\{\omega\}) = \frac{1}{6}$ pour tout $\omega \in \Omega$.
Soit $X$ la variable aléatoire représentant le résultat du dé : $X(\omega) = \omega$.
La loi de probabilité est discrète. L'intégrale de Lebesgue par rapport à une mesure discrète se réduit à une somme discrète :
$$ \mathbb{E}[X] = \sum_{\omega \in \Omega} X(\omega) \mathbb{P}(\{\omega\}) = 1\left(\frac{1}{6}\right) + 2\left(\frac{1}{6}\right) + 3\left(\frac{1}{6}\right) + 4\left(\frac{1}{6}\right) + 5\left(\frac{1}{6}\right) + 6\left(\frac{1}{6}\right) $$
$$ \mathbb{E}[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5 $$
C'est le centre de masse des valeurs $1$ à $6$ pondérées uniformément.

### B. Théorème de Transfert

Dans la pratique, on ne calcule presque jamais l'intégrale sur l'univers abstrait $\Omega$. On utilise la loi (la mesure image) de $X$ sur $\mathbb{R}$, notée $\mathbb{P}_X$.

**Théorème 1 (Théorème de Transfert) :**
Soit $X$ une variable aléatoire de loi $\mathbb{P}_X$, et $\varphi : \mathbb{R} \to \mathbb{R}$ une fonction mesurable.
Alors $\varphi(X)$ est intégrable si et seulement si $\int_{\mathbb{R}} |\varphi(x)| \, \mathrm{d}\mathbb{P}_X(x) < +\infty$.
Dans ce cas, on a :
$$ \mathbb{E}[\varphi(X)] = \int_{\mathbb{R}} \varphi(x) \, \mathrm{d}\mathbb{P}_X(x) $$

**Conséquences calculatoires :**
1. Si $X$ est discrète prenant les valeurs $(x_i)_{i \in I}$ :
   $$ \mathbb{E}[\varphi(X)] = \sum_{i \in I} \varphi(x_i) \mathbb{P}(X = x_i) $$
2. Si $X$ admet une densité $f_X$ par rapport à la mesure de Lebesgue sur $\mathbb{R}$ :
   $$ \mathbb{E}[\varphi(X)] = \int_{-\infty}^{+\infty} \varphi(x) f_X(x) \, \mathrm{d}x $$

**Exemple concret immédiat :**
Soit $X$ une variable aléatoire continue suivant une loi exponentielle de paramètre $\lambda > 0$. Sa densité de probabilité est $f_X(x) = \lambda e^{-\lambda x} \mathbf{1}_{\mathbb{R}^+}(x)$.
Calculons l'espérance de la variable $Y = X^2$, qui correspond au moment d'ordre $2$ de $X$.
D'après le théorème de transfert (avec $\varphi(x) = x^2$) :
$$ \mathbb{E}[X^2] = \int_{-\infty}^{+\infty} x^2 \lambda e^{-\lambda x} \mathbf{1}_{\mathbb{R}^+}(x) \, \mathrm{d}x = \int_{0}^{+\infty} x^2 \lambda e^{-\lambda x} \, \mathrm{d}x $$
Nous effectuons une première intégration par parties avec $u = x^2 \implies \mathrm{d}u = 2x \, \mathrm{d}x$ et $\mathrm{d}v = \lambda e^{-\lambda x} \, \mathrm{d}x \implies v = -e^{-\lambda x}$ :
$$ \mathbb{E}[X^2] = \left[ -x^2 e^{-\lambda x} \right]_0^{+\infty} - \int_0^{+\infty} -2x e^{-\lambda x} \, \mathrm{d}x $$
Le terme de bord $\lim_{x \to +\infty} -x^2 e^{-\lambda x}$ est nul par croissance comparée. Ainsi :
$$ \mathbb{E}[X^2] = 0 + \frac{2}{\lambda} \int_0^{+\infty} x \lambda e^{-\lambda x} \, \mathrm{d}x = \frac{2}{\lambda} \mathbb{E}[X] $$
L'espérance de $X$ (moment d'ordre 1) se calcule par une autre intégration par parties (similaire) et vaut $\frac{1}{\lambda}$.
Donc $\mathbb{E}[X^2] = \frac{2}{\lambda} \cdot \frac{1}{\lambda} = \frac{2}{\lambda^2}$.

### C. Linéarité, Monotonie et Inégalités Fondamentales

**Théorème 2 (Linéarité de l'Espérance) :**
Si $X, Y \in \mathcal{L}^1$ et $a, b \in \mathbb{R}$, alors $aX + bY \in \mathcal{L}^1$ et :
$$ \mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y] $$

**Théorème 3 (Croissance de l'Espérance) :**
Soient $X, Y \in \mathcal{L}^1$. Si $\mathbb{P}(X \le Y) = 1$ (c'est-à-dire que $X \le Y$ presque sûrement), alors :
$$ \mathbb{E}[X] \le \mathbb{E}[Y] $$

**Théorème 4 (Inégalité de Markov) :**
Soit $X$ une variable aléatoire positive ou nulle et $a > 0$. Alors :
$$ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} $$

**Exemple concret de l'inégalité de Markov :**
Supposons que la durée de vie moyenne d'un composant électronique est $\mathbb{E}[X] = 5$ ans (où $X \ge 0$).
Quelle est la probabilité que ce composant fonctionne plus de $20$ ans ?
En appliquant Markov avec $a = 20$ :
$$ \mathbb{P}(X \ge 20) \le \frac{\mathbb{E}[X]}{20} = \frac{5}{20} = 0.25 $$
La probabilité est donc inférieure ou égale à $25\%$.

### D. Variance et Écart-Type

**Définition 3 (Variance) :**
Si $X \in \mathcal{L}^2$ (c'est-à-dire si $\mathbb{E}[X^2] < +\infty$), la variance de $X$, notée $\mathrm{Var}(X)$, est définie comme l'espérance du carré de l'écart à la moyenne :
$$ \mathrm{Var}(X) = \mathbb{E}\left[ (X - \mathbb{E}[X])^2 \right] $$
L'écart-type est défini par $\sigma(X) = \sqrt{\mathrm{Var}(X)}$. Il donne une mesure de la dispersion des valeurs autour de l'espérance, exprimée dans les mêmes unités que la variable d'origine.

**Théorème 5 (Formule de Koenig-Huygens) :**
$$ \mathrm{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 $$

**Cas pathologique :**
Toutes les variables aléatoires n'ont pas une espérance finie. Prenons la loi de Cauchy standard, dont la densité sur $\mathbb{R}$ est $f(x) = \frac{1}{\pi(1+x^2)}$.
Pour calculer $\mathbb{E}[|X|]$, nous devons évaluer l'intégrale $\int_{-\infty}^{+\infty} |x| \frac{1}{\pi(1+x^2)} \, \mathrm{d}x$.
Comme $\frac{|x|}{1+x^2} \sim \frac{1}{|x|}$ lorsque $|x| \to +\infty$, l'intégrale diverge. Par conséquent, la variable aléatoire de Cauchy n'a pas d'espérance (elle n'est pas dans $\mathcal{L}^1$). Il est physiquement impossible de définir un "centre de gravité" moyen, les valeurs extrêmes tirant la moyenne à l'infini avec des probabilités non négligeables.

## 3. Démonstrations

### Démonstration de l'inégalité de Markov

Soit $X$ une variable aléatoire positive et $a > 0$.
Posons l'ensemble $A = \{ \omega \in \Omega \mid X(\omega) \ge a \}$.
La fonction indicatrice de l'événement $A$, notée $\mathbf{1}_{A}$, vaut $1$ si $\omega \in A$ et $0$ sinon.
Pour tout $\omega \in \Omega$, on peut écrire l'inégalité suivante :
$$ a \mathbf{1}_{A}(\omega) \le X(\omega) $$
Justifions précisément cette étape :
- Si $\omega \in A$, alors $X(\omega) \ge a$, et $a \mathbf{1}_{A}(\omega) = a \cdot 1 = a$. L'inégalité $a \le X(\omega)$ est trivialement vérifiée par définition de l'ensemble $A$.
- Si $\omega \notin A$, alors $X(\omega) < a$, et $a \mathbf{1}_{A}(\omega) = a \cdot 0 = 0$. Comme $X$ est une variable aléatoire positive par hypothèse, $0 \le X(\omega)$, donc l'inégalité est également vérifiée.

On intègre alors cette inégalité sur $\Omega$ par rapport à la mesure de probabilité $\mathbb{P}$. Par croissance (monotonie) de l'intégrale de Lebesgue (Théorème 3) :
$$ \int_{\Omega} a \mathbf{1}_{A}(\omega) \, \mathrm{d}\mathbb{P}(\omega) \le \int_{\Omega} X(\omega) \, \mathrm{d}\mathbb{P}(\omega) $$
La partie droite est exactement l'espérance de $X$, $\mathbb{E}[X]$.
Pour la partie gauche, on utilise la linéarité de l'intégrale pour sortir la constante $a$ :
$$ a \int_{\Omega} \mathbf{1}_{A}(\omega) \, \mathrm{d}\mathbb{P}(\omega) \le \mathbb{E}[X] $$
Par définition, l'intégrale de la fonction indicatrice d'un événement correspond à la mesure (ici la probabilité) de cet événement :
$$ \int_{\Omega} \mathbf{1}_{A} \, \mathrm{d}\mathbb{P} = \mathbb{P}(A) = \mathbb{P}(X \ge a) $$
On obtient donc :
$$ a \mathbb{P}(X \ge a) \le \mathbb{E}[X] $$
En divisant les deux côtés par la constante strictement positive $a$, il vient :
$$ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} $$
Ce qui achève rigoureusement la démonstration.

### Démonstration de la formule de Koenig-Huygens

Soit $X \in \mathcal{L}^2$. Par l'inégalité de Cauchy-Schwarz (ou le fait que $\mathcal{L}^2 \subset \mathcal{L}^1$ sur un espace de mesure finie), on sait que $X$ admet une espérance finie.
Posons $\mu = \mathbb{E}[X]$. Par définition de la variance :
$$ \mathrm{Var}(X) = \mathbb{E}\left[ (X - \mu)^2 \right] $$
On développe le polynôme à l'intérieur de l'espérance :
$$ (X - \mu)^2 = X^2 - 2\mu X + \mu^2 $$
On applique alors la linéarité de l'espérance, sachant que $\mu$ est une simple constante réelle :
$$ \mathbb{E}\left[ X^2 - 2\mu X + \mu^2 \right] = \mathbb{E}[X^2] - \mathbb{E}[2\mu X] + \mathbb{E}[\mu^2] $$
On sort la constante $2\mu$ de la deuxième espérance, et la constante $\mu^2$ de la troisième espérance (l'espérance d'une constante est la constante elle-même) :
$$ \mathbb{E}[X^2] - 2\mu \mathbb{E}[X] + \mu^2 $$
Or, nous savons que $\mathbb{E}[X] = \mu$, on remplace :
$$ \mathbb{E}[X^2] - 2\mu(\mu) + \mu^2 = \mathbb{E}[X^2] - 2\mu^2 + \mu^2 $$
$$ = \mathbb{E}[X^2] - \mu^2 = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 $$
Ce qui termine la preuve de la formule.

## 4. Applications en Physique, Logique et Intelligence Artificielle

### En Physique Statistique (Mécanique Statistique)
L'espérance est le pilier de la mécanique statistique développée par Boltzmann et Gibbs. L'état d'un système à l'équilibre thermique est distribué selon la distribution de Boltzmann : la probabilité qu'un système soit dans un micro-état d'énergie $E_i$ est proportionnelle à $e^{-E_i / k_B T}$. L'énergie macroscopique mesurable (l'énergie interne $U$) n'est rien d'autre que l'espérance de l'énergie :
$$ U = \langle E \rangle = \mathbb{E}[E] = \frac{\sum_i E_i e^{-E_i / k_B T}}{\sum_i e^{-E_i / k_B T}} $$
Toutes les grandeurs thermodynamiques dérivent d'une approche par intégration sur l'espace des phases (espace abstrait de dimension $6N$).

### En Apprentissage Automatique (Machine Learning)
Le problème fondamental de l'apprentissage supervisé s'énonce comme la minimisation du risque théorique, ou risque attendu.
Si on cherche un modèle de prédiction $f_{\theta}$ pour estimer une variable $Y$ à partir de $X$, et que $\mathcal{L}(\hat{y}, y)$ est une fonction de perte évaluant l'erreur de prédiction, le risque se définit formellement par :
$$ R(\theta) = \mathbb{E}_{(X,Y)\sim P}[\mathcal{L}(f_{\theta}(X), Y)] = \int_{\mathcal{X} \times \mathcal{Y}} \mathcal{L}(f_{\theta}(x), y) \, \mathrm{d}\mathbb{P}_{X,Y}(x, y) $$
Comme la véritable mesure de probabilité jointe $\mathbb{P}_{X,Y}$ de la nature est toujours inconnue en pratique, on approxime l'espérance par une moyenne empirique sur un jeu de données $\{ (x_i, y_i) \}_{i=1}^N$ (Risque Empirique). La Loi Forte des Grands Nombres garantit que ce risque empirique converge vers l'espérance mathématique théorique.

### En Logique et IA probabiliste (Théorie de la Décision)
L'espérance permet de prendre des décisions optimales sous incertitude (Processus de Décision Markoviens - MDP, Apprentissage par Renforcement). Dans l'algorithme Q-Learning, la fonction valeur (Q-value) d'un état $s$ et d'une action $a$ est l'espérance de la somme actualisée des récompenses futures :
$$ Q^{\pi}(s,a) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t R_t \mid S_0 = s, A_0 = a \right] $$
L'agent d'IA résout le jeu en cherchant à maximiser cette intégrale dans le temps.
