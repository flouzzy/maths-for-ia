# Les modes de convergence : presque sûre, en probabilité, dans $L^p$ et en loi

## 1. Introduction

La théorie des probabilités s'articule autour de la notion de limite. Contrairement à l'analyse classique où une suite de réels converge vers une valeur unique de manière déterministe, les variables aléatoires évoluent dans un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$. Il n'y a donc pas une seule façon de converger, mais plusieurs, selon la "force" avec laquelle on exige que la suite de variables aléatoires s'approche de sa limite. Historiquement, Andrey Kolmogorov (1933) a fondé la théorie moderne des probabilités en axiomatisant ces concepts à travers la théorie de la mesure. Des mathématiciens comme Pafnuty Chebyshev, son élève Andrey Markov, et plus tard Paul Lévy ont introduit et formalisé les différentes hiérarchies de convergence. Le besoin physique est évident : en mécanique statistique, on observe des macro-systèmes (comme un gaz) composés de milliards de micro-états aléatoires. Comment garantir que la moyenne de ces états se stabilise vers une valeur constante, malgré les fluctuations locales ? Les modes de convergence offrent les outils rigoureux pour répondre à cette question.

## 2. Formalisation : Les Hiérarchies de la Convergence

Nous nous plaçons sur un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$. Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires réelles et $X$ une variable aléatoire réelle définies sur cet espace.

### Convergence Presque Sûre (p.s.)

La convergence presque sûre est le mode de convergence le plus fort (avec la convergence dans $L^\infty$). Elle exige que, pour presque tout événement de l'univers, la suite numérique des réalisations converge.

**Définition (Convergence presque sûre) :**
On dit que la suite $(X_n)_{n \in \mathbb{N}}$ converge presque sûrement vers $X$, noté $X_n \xrightarrow{\text{p.s.}} X$, si :
$$\mathbb{P}\left(\left\{ \omega \in \Omega \mid \lim_{n \to +\infty} X_n(\omega) = X(\omega) \right\}\right) = 1$$
De manière équivalente, l'ensemble des $\omega$ pour lesquels $X_n(\omega)$ ne converge pas vers $X(\omega)$ est de mesure nulle.

**Exemple concret immédiat :**
Considérons l'espace de Lebesgue $(]0, 1], \mathcal{B}(]0, 1]), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Définissons $X_n(\omega) = \omega^n$.
Pour tout $\omega \in ]0, 1[$, on a $\lim_{n \to +\infty} \omega^n = 0$.
Pour $\omega = 1$, on a $\lim_{n \to +\infty} 1^n = 1$.
Donc, la limite simple $X(\omega)$ est $0$ si $\omega \in ]0, 1[$ et $1$ si $\omega = 1$.
L'ensemble de convergence vers $0$ est $]0, 1[$, dont la mesure de Lebesgue est $\lambda(]0, 1[) = 1$.
Ainsi, $\lambda(\{ \omega \in ]0, 1] \mid \lim_{n \to \infty} X_n(\omega) = 0 \}) = 1$.
On conclut que $X_n \xrightarrow{\text{p.s.}} 0$.

### Convergence en Probabilité

La convergence en probabilité est plus faible. Elle exige que la probabilité que $X_n$ s'éloigne de $X$ d'une distance donnée tende vers $0$.

**Définition (Convergence en probabilité) :**
On dit que la suite $(X_n)_{n \in \mathbb{N}}$ converge en probabilité vers $X$, noté $X_n \xrightarrow{\mathbb{P}} X$, si pour tout $\varepsilon > 0$ :
$$\lim_{n \to +\infty} \mathbb{P}(|X_n - X| > \varepsilon) = 0$$

**Théorème (Lien entre p.s. et probabilité) :**
Si $X_n \xrightarrow{\text{p.s.}} X$, alors $X_n \xrightarrow{\mathbb{P}} X$. La réciproque est fausse en général.

**Exemple concret immédiat (Contre-exemple de la réciproque) :**
Le "typewriter sequence" (suite de la machine à écrire). Sur $(]0, 1], \mathcal{B}(]0, 1]), \lambda)$, on définit les intervalles $A_n$ de longueur décroissante qui "balayent" $]0, 1]$.
Pour tout entier $k \ge 1$ et $1 \le j \le 2^k$, posons $n = 2^k + j - 1$.
Définissons $A_n = \left] \frac{j-1}{2^k}, \frac{j}{2^k} \right]$.
Soit $X_n = \mathbb{1}_{A_n}$.
Pour tout $\varepsilon \in ]0, 1[$, $\mathbb{P}(|X_n - 0| > \varepsilon) = \mathbb{P}(A_n) = \frac{1}{2^k}$.
Comme $n \to +\infty \implies k \to +\infty$, $\lim_{n \to +\infty} \mathbb{P}(|X_n| > \varepsilon) = 0$, donc $X_n \xrightarrow{\mathbb{P}} 0$.
Cependant, pour tout $\omega \in ]0, 1]$, $\omega$ appartient à une infinité de $A_n$. Ainsi, la suite $(X_n(\omega))$ prend la valeur $1$ une infinité de fois et la valeur $0$ une infinité de fois.
Elle ne converge donc pour *aucun* $\omega$. Donc $X_n$ ne converge pas presque sûrement vers $0$.

### Convergence dans $L^p$

On exige ici que l'espérance de l'erreur à la puissance $p$ tende vers $0$.

**Définition (Convergence dans $L^p$) :**
Soit $p \ge 1$. Supposons que $\mathbb{E}[|X_n|^p] < +\infty$ et $\mathbb{E}[|X|^p] < +\infty$. On dit que $(X_n)_{n \in \mathbb{N}}$ converge vers $X$ dans $L^p$, noté $X_n \xrightarrow{L^p} X$, si :
$$\lim_{n \to +\infty} \mathbb{E}[|X_n - X|^p] = 0$$

**Théorème (Lien entre $L^p$ et probabilité) :**
Si $X_n \xrightarrow{L^p} X$, alors $X_n \xrightarrow{\mathbb{P}} X$.

**Exemple concret immédiat (Application de Markov) :**
Soit $p \ge 1$. Par l'inégalité de Markov, pour tout $\varepsilon > 0$ :
$$\mathbb{P}(|X_n - X| > \varepsilon) = \mathbb{P}(|X_n - X|^p > \varepsilon^p) \le \frac{\mathbb{E}[|X_n - X|^p]}{\varepsilon^p}$$
Si $X_n \xrightarrow{L^p} X$, alors le membre de droite tend vers $0$ quand $n \to +\infty$.
Ainsi, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \varepsilon) = 0$, soit $X_n \xrightarrow{\mathbb{P}} X$.

### Convergence en Loi (ou étroite)

C'est le mode le plus faible, concernant uniquement la répartition (la mesure) et non la variable aléatoire elle-même en tant que fonction.

**Définition (Convergence en loi) :**
On dit que la suite $(X_n)_{n \in \mathbb{N}}$ converge en loi vers $X$, noté $X_n \xrightarrow{\mathcal{L}} X$, si pour toute fonction continue et bornée $f : \mathbb{R} \to \mathbb{R}$ :
$$\lim_{n \to +\infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]$$
De manière équivalente (Théorème de Portmanteau), en notant $F_{X_n}$ et $F_X$ les fonctions de répartition respectives, $X_n \xrightarrow{\mathcal{L}} X$ ssi $\lim_{n \to +\infty} F_{X_n}(x) = F_X(x)$ pour tout point de continuité $x$ de $F_X$.

**Théorème (Lien entre probabilité et loi) :**
Si $X_n \xrightarrow{\mathbb{P}} X$, alors $X_n \xrightarrow{\mathcal{L}} X$.

**Exemple concret immédiat :**
Soit $X \sim \mathcal{N}(0, 1)$. Définissons $X_n = -X$ pour tout $n$.
Les variables $X_n$ ont la même loi que $X$ (car la gaussienne centrée réduite est symétrique).
Donc $X_n \xrightarrow{\mathcal{L}} X$ (la suite des lois est constante).
Pourtant, $\mathbb{P}(|X_n - X| > 1) = \mathbb{P}(|-2X| > 1) = \mathbb{P}(|X| > 0.5) > 0$.
Cette probabilité ne tend pas vers $0$, donc $X_n$ ne converge pas en probabilité vers $X$.

## 3. Démonstrations

**Démonstration du théorème : $X_n \xrightarrow{\text{p.s.}} X \implies X_n \xrightarrow{\mathbb{P}} X$**

Soit $\varepsilon > 0$. Considérons les événements $A_n(\varepsilon) = \{ |X_n - X| > \varepsilon \}$.
Nous voulons montrer que $\lim_{n \to +\infty} \mathbb{P}(A_n(\varepsilon)) = 0$.
Posons $B_n(\varepsilon) = \bigcup_{k=n}^{+\infty} A_k(\varepsilon) = \bigcup_{k=n}^{+\infty} \{ |X_k - X| > \varepsilon \}$.
La suite d'ensembles $(B_n(\varepsilon))_{n \in \mathbb{N}}$ est décroissante : $B_{n+1}(\varepsilon) \subset B_n(\varepsilon)$.
Soit $B(\varepsilon) = \bigcap_{n=1}^{+\infty} B_n(\varepsilon) = \limsup_{n \to +\infty} A_n(\varepsilon)$.
$B(\varepsilon)$ est l'ensemble des $\omega$ pour lesquels $|X_k(\omega) - X(\omega)| > \varepsilon$ pour une infinité d'indices $k$.
Si $\omega \in B(\varepsilon)$, alors la suite $X_n(\omega)$ ne peut pas converger vers $X(\omega)$.
Ainsi, $B(\varepsilon) \subset \{ \omega \in \Omega \mid X_n(\omega) \text{ ne converge pas vers } X(\omega) \}$.
Par hypothèse de convergence presque sûre, ce dernier ensemble est de probabilité nulle.
Donc $\mathbb{P}(B(\varepsilon)) = 0$.
Puisque $(B_n(\varepsilon))$ est une suite décroissante d'événements, par le théorème de continuité décroissante pour les probabilités :
$$\lim_{n \to +\infty} \mathbb{P}(B_n(\varepsilon)) = \mathbb{P}\left( \bigcap_{n=1}^{+\infty} B_n(\varepsilon) \right) = \mathbb{P}(B(\varepsilon)) = 0$$
Or, pour tout $n$, $A_n(\varepsilon) \subset B_n(\varepsilon)$, donc $0 \le \mathbb{P}(A_n(\varepsilon)) \le \mathbb{P}(B_n(\varepsilon))$.
Par le théorème des gendarmes, $\lim_{n \to +\infty} \mathbb{P}(A_n(\varepsilon)) = 0$.
Ce qui conclut la preuve : $X_n \xrightarrow{\mathbb{P}} X$.

**Démonstration du théorème (partiel) : $X_n \xrightarrow{\mathbb{P}} X \implies X_n \xrightarrow{\mathcal{L}} X$**

Soit $f : \mathbb{R} \to \mathbb{R}$ uniformément continue et bornée (le théorème de Portmanteau permet de se restreindre à ce sous-ensemble). Soit $M = \sup_{x \in \mathbb{R}} |f(x)|$.
Soit $\varepsilon > 0$. Comme $f$ est uniformément continue, il existe $\delta > 0$ tel que pour tout $x, y \in \mathbb{R}$, $|x - y| < \delta \implies |f(x) - f(y)| < \varepsilon$.
Évaluons la différence des espérances :
$$|\mathbb{E}[f(X_n)] - \mathbb{E}[f(X)]| \le \mathbb{E}[|f(X_n) - f(X)|]$$
Séparons l'espérance sur deux événements complémentaires, $\{ |X_n - X| \le \delta \}$ et $\{ |X_n - X| > \delta \}$ :
$$\mathbb{E}[|f(X_n) - f(X)|] = \mathbb{E}[|f(X_n) - f(X)| \mathbb{1}_{\{|X_n - X| \le \delta\}}] + \mathbb{E}[|f(X_n) - f(X)| \mathbb{1}_{\{|X_n - X| > \delta\}}]$$
Sur le premier événement, par définition de $\delta$, $|f(X_n) - f(X)| < \varepsilon$.
Sur le second événement, on majore grossièrement : $|f(X_n) - f(X)| \le |f(X_n)| + |f(X)| \le 2M$.
Ainsi :
$$\mathbb{E}[|f(X_n) - f(X)|] \le \mathbb{E}[\varepsilon \cdot \mathbb{1}_{\{|X_n - X| \le \delta\}}] + \mathbb{E}[2M \cdot \mathbb{1}_{\{|X_n - X| > \delta\}}]$$
$$\mathbb{E}[|f(X_n) - f(X)|] \le \varepsilon \mathbb{P}(|X_n - X| \le \delta) + 2M \mathbb{P}(|X_n - X| > \delta)$$
$$\mathbb{E}[|f(X_n) - f(X)|] \le \varepsilon \cdot 1 + 2M \mathbb{P}(|X_n - X| > \delta)$$
Puisque $X_n \xrightarrow{\mathbb{P}} X$, pour ce $\delta > 0$, on a $\lim_{n \to +\infty} \mathbb{P}(|X_n - X| > \delta) = 0$.
Donc $\limsup_{n \to +\infty} |\mathbb{E}[f(X_n)] - \mathbb{E}[f(X)]| \le \varepsilon$.
Ceci étant vrai pour tout $\varepsilon > 0$, la limite est nulle : $\lim_{n \to +\infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]$.

## 4. Applications en Physique, Logique & Intelligence Artificielle

En Intelligence Artificielle, et plus particulièrement en Machine Learning, la théorie de l'apprentissage statistique (Vapnik-Chervonenkis, PAC learning) repose fondamentalement sur ces modes de convergence.

1. **Convergence des risques empiriques (Loi des Grands Nombres) :**
   Lors de l'entraînement d'un modèle, on minimise le risque empirique $\hat{R}_n(\theta) = \frac{1}{n} \sum_{i=1}^n \ell(f_\theta(x_i), y_i)$ au lieu du risque vrai $R(\theta) = \mathbb{E}_{(X,Y)}[\ell(f_\theta(X), Y)]$. La convergence en probabilité (ou p.s. par la loi forte) de $\hat{R}_n(\theta)$ vers $R(\theta)$ garantit que l'apprentissage est possible (consistance du risque empirique).

2. **Descente de Gradient Stochastique (SGD) :**
   Dans l'optimisation des réseaux de neurones, on met à jour les poids $\theta_{t+1} = \theta_t - \eta_t \nabla \ell(\theta_t, z_t)$. Le théorème de Robbins-Monro prouve, sous certaines conditions sur les pas d'apprentissage $\eta_t$ ($\sum \eta_t = \infty, \sum \eta_t^2 < \infty$), la convergence presque sûre et dans $L^2$ de la suite des estimateurs $\theta_t$ vers l'optimum global (dans le cas convexe).

3. **Inférence Variationnelle et Modèles Génératifs (GAN, VAE) :**
   La convergence en loi est le fondement de la modélisation générative. On cherche à ce que la suite de mesures empiriques générées par le modèle converge faiblement vers la mesure des données réelles. L'utilisation de distances de probabilité (comme la distance de Wasserstein) permet de métriser cette convergence en loi.
