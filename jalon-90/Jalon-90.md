---
uuid: "jalon-90"
title: "Les modes de convergence en probabilités"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon-89.md]]"
next: "[[Jalon-91.md]]"
---

# Jalon 90 : Les modes de convergence en probabilités

## 1. Origines et intuitions asymptotiques

L'étude des phénomènes aléatoires, initialement circonscrite aux jeux de hasard, a pris une dimension analytique rigoureuse au tournant des XIXe et XXe siècles grâce aux travaux de mathématiciens russes tels que Pafnuty Chebyshev, Andrey Markov et Andrey Kolmogorov, ainsi que l'économiste et statisticien Eugen Slutsky. La question centrale qui animait ces chercheurs était de comprendre le comportement asymptotique des suites de variables aléatoires : lorsqu'une expérience est répétée une infinité de fois, de quelle manière la moyenne empirique converge-t-elle vers son espérance théorique ?

En mathématiques classiques, la convergence d'une suite de nombres réels est univoque et absolue. En probabilités, du fait de l'existence d'événements de mesure nulle (les fameux ensembles $\omega \in \Omega$ pour lesquels la propriété peut faire défaut sans affecter la probabilité globale), le concept de proximité entre variables aléatoires se décline sous plusieurs topologies distinctes. Il a fallu forger un arsenal d'outils analytiques pour mesurer si une suite de variables aléatoires $(X_n)$ s'approche d'une limite $X$ presque partout, en mesure, en moyenne ou seulement au niveau de ses répartitions (loi). Cette hiérarchie des modes de convergence permet d'isoler la nature exacte de la stabilité asymptotique d'un système.

Visuellement, on peut imaginer la convergence d'une suite de fonctions aléatoires. La convergence la plus forte exige que les trajectoires se superposent à la limite (sauf sur des cas rares invisibles). La convergence en probabilité accepte que les fonctions s'éloignent considérablement de la limite, pourvu que ces écarts deviennent de moins en moins fréquents. Enfin, la convergence en loi ne regarde même plus les trajectoires individuelles : elle compare uniquement la forme des histogrammes de répartition des valeurs, s'assurant que la cloche finale a la même allure, indépendamment de la trajectoire de chaque particule isolée.

## 2. Formalisation des modes de convergence et exemples

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires réelles et $X$ une variable aléatoire réelle, toutes définies sur ce même espace.

### A. Convergence Presque Sûre (p.s.)

La convergence presque sûre est l'analogue de la convergence ponctuelle presque partout en analyse fonctionnelle.

**Définition (Convergence Presque Sûre) :**
La suite $(X_n)$ converge presque sûrement vers $X$, ce que l'on note $X_n \xrightarrow{p.s.} X$, si l'événement sur lequel la convergence ponctuelle a lieu possède une probabilité égale à $1$ :
$$ \mathbb{P}\left(\left\{ \omega \in \Omega \mid \lim_{n \to \infty} X_n(\omega) = X(\omega) \right\}\right) = 1 $$

**Exemple Numérique Immédiat :**
Soit $\Omega = [0, 1]$ muni de la tribu borélienne et de la mesure de Lebesgue $\mathbb{P}$. Considérons $X_n(\omega) = \omega^n$.
Pour tout $\omega \in [0, 1[$, on calcule :
$$ \lim_{n \to \infty} \omega^n = 0 $$
Pour $\omega = 1$, $X_n(1) = 1^n = 1$.
Posons $X(\omega) = 0$ pour tout $\omega \in \Omega$. L'ensemble des $\omega$ où $X_n(\omega)$ ne converge pas vers $X(\omega)$ est exactement $\{1\}$.
La probabilité de ce singleton pour la mesure de Lebesgue est :
$$ \mathbb{P}(\{1\}) = 0 $$
Ainsi, l'événement de convergence a pour probabilité $1 - 0 = 1$. On conclut que $X_n \xrightarrow{p.s.} 0$.

### B. Convergence en Probabilité

La convergence en probabilité requiert que la probabilité d'un écart significatif entre $X_n$ et $X$ tende vers zéro.

**Définition (Convergence en Probabilité) :**
La suite $(X_n)$ converge en probabilité vers $X$, noté $X_n \xrightarrow{\mathbb{P}} X$, si pour tout seuil $\epsilon > 0$ :
$$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 $$

**Exemple Numérique Immédiat :**
Considérons $\Omega = [0, 1]$ muni de la mesure de Lebesgue.
Soit l'intervalle $I_n = \left[ 0, \frac{1}{n} \right]$.
Définissons $X_n(\omega) = n \mathbf{1}_{I_n}(\omega)$.
Soit $\epsilon > 0$. Évaluons $\mathbb{P}(|X_n - 0| > \epsilon)$.
Dès que $n > \epsilon$, $X_n$ prend la valeur $n$ (qui est $> \epsilon$) sur l'intervalle $I_n$, et $0$ ailleurs.
$$ \mathbb{P}(|X_n| > \epsilon) = \mathbb{P}(\omega \in I_n) = \frac{1}{n} $$
Calculons la limite :
$$ \lim_{n \to \infty} \frac{1}{n} = 0 $$
Par conséquent, $X_n \xrightarrow{\mathbb{P}} 0$.

### C. Convergence dans $L^p$

La convergence dans $L^p$ traduit la convergence en moyenne, pondérée par la puissance $p$.

**Définition (Convergence $L^p$) :**
Pour $p \geq 1$, on suppose que $\mathbb{E}[|X_n|^p] < \infty$ et $\mathbb{E}[|X|^p] < \infty$. La suite $(X_n)$ converge dans $L^p$ vers $X$, noté $X_n \xrightarrow{L^p} X$, si :
$$ \lim_{n \to \infty} \mathbb{E}\left[|X_n - X|^p\right] = 0 $$

**Exemple Numérique Immédiat (Contre-exemple de la bosse glissante) :**
Reprenons $X_n(\omega) = n \mathbf{1}_{[0, 1/n]}(\omega)$ sur $[0, 1]$.
Nous avons vu que $X_n \xrightarrow{\mathbb{P}} 0$. Étudions la convergence dans $L^1$ ($p=1$).
Calculons l'espérance de la valeur absolue :
$$ \mathbb{E}\left[|X_n - 0|\right] = \int_{0}^{1} |n \mathbf{1}_{[0, 1/n]}(\omega)| \, d\omega = n \times \frac{1}{n} = 1 $$
La limite est :
$$ \lim_{n \to \infty} 1 = 1 \neq 0 $$
Ainsi, la suite $(X_n)$ ne converge pas vers $0$ dans $L^1$. L'aire de la fonction reste constante à $1$, bien que son support se réduise à un point de mesure nulle.

\begin{tikzpicture}
\draw[->] (-0.5,0) -- (5,0) node[right] {$\omega$};
\draw[->] (0,-0.5) -- (0,4) node[above] {$X_n(\omega)$};
\draw[blue, thick] (0, 0) -- (0, 2) -- (2, 2) -- (2, 0) -- (4, 0);
\draw[red, thick] (0, 0) -- (0, 3) -- (1.33, 3) -- (1.33, 0) -- (4, 0);
\node[below] at (2,0) {$1/n_1$};
\node[below] at (1.33,0) {$1/n_2$};
\node[left] at (0,2) {$n_1$};
\node[left] at (0,3) {$n_2$};
\node[above] at (2.5, 3) {L'aire (espérance) reste constante (1)};
\end{tikzpicture}

### D. Convergence en Loi (ou Convergence Étroite)

Ce mode de convergence ne requiert pas que les variables soient définies sur le même espace de probabilité. Il traduit la proximité des répartitions.

**Définition (Convergence en Loi) :**
La suite $(X_n)$ converge en loi vers $X$, noté $X_n \xrightarrow{\mathcal{L}} X$, si pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ continue et bornée :
$$ \lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)] $$
Ceci équivaut à $\lim_{n \to \infty} F_{X_n}(x) = F_X(x)$ en tout point de continuité de la fonction de répartition $F_X$.

**Exemple Numérique Immédiat :**
Soit $X \sim \mathcal{N}(0, 1)$. Définissons $X_n = -X$ pour tout $n$.
La densité de $X$ est paire, donc $-X$ suit exactement la même loi que $X$, c'est-à-dire $\mathcal{N}(0, 1)$.
Pour toute fonction $f$ continue et bornée :
$$ \mathbb{E}[f(X_n)] = \mathbb{E}[f(-X)] = \int_{-\infty}^{\infty} f(-x) \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx $$
Posons $y = -x$, $dy = -dx$ :
$$ \int_{+\infty}^{-\infty} f(y) \frac{1}{\sqrt{2\pi}} e^{-y^2/2} (-dy) = \int_{-\infty}^{\infty} f(y) \frac{1}{\sqrt{2\pi}} e^{-y^2/2} dy = \mathbb{E}[f(X)] $$
Ainsi $X_n \xrightarrow{\mathcal{L}} X$.
Cependant, l'écart $|X_n - X| = |-X - X| = 2|X|$ ne tend pas vers $0$. Il n'y a donc pas de convergence en probabilité.

## 3. Hiérarchie des Modes de Convergence : Démonstrations Pas-à-Pas

Le théorème suivant structure rigoureusement les relations d'implication entre les différents modes.

> **Théorème de Hiérarchie des Convergences :**
> Soit $(X_n)$ une suite de variables aléatoires et $X$ une variable aléatoire.
> 1. Si $X_n \xrightarrow{p.s.} X$, alors $X_n \xrightarrow{\mathbb{P}} X$.
> 2. Si $X_n \xrightarrow{L^p} X$ (pour $p \geq 1$), alors $X_n \xrightarrow{\mathbb{P}} X$.
> 3. Si $X_n \xrightarrow{\mathbb{P}} X$, alors $X_n \xrightarrow{\mathcal{L}} X$.

### Démonstration : $L^p \implies$ Convergence en Probabilité

1. **Initialisation / Cadre :**
   Nous supposons que $\lim_{n \to \infty} \mathbb{E}\left[|X_n - X|^p\right] = 0$. Nous voulons montrer que pour tout $\epsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0$.

2. **Étape 1 : Transformation de l'événement**
   Soit $\epsilon > 0$. Puisque $x \mapsto x^p$ est une fonction strictement croissante sur $\mathbb{R}^+$, les deux événements suivants sont strictement identiques :
   $$ \{ \omega \in \Omega \mid |X_n(\omega) - X(\omega)| > \epsilon \} = \{ \omega \in \Omega \mid |X_n(\omega) - X(\omega)|^p > \epsilon^p \} $$
   D'où :
   $$ \mathbb{P}(|X_n - X| > \epsilon) = \mathbb{P}\left(|X_n - X|^p > \epsilon^p\right) $$

3. **Étape 2 : Application de l'inégalité de Markov**
   Considérons la variable aléatoire positive $Y_n = |X_n - X|^p$.
   L'inégalité de Markov stipule que pour toute variable aléatoire $Z \geq 0$ et $a > 0$, $\mathbb{P}(Z \geq a) \leq \frac{\mathbb{E}[Z]}{a}$.
   Appliquons cette inégalité avec $Z = Y_n$ et $a = \epsilon^p$ :
   $$ \mathbb{P}\left(|X_n - X|^p > \epsilon^p\right) \leq \frac{\mathbb{E}\left[|X_n - X|^p\right]}{\epsilon^p} $$

4. **Conclusion : Passage à la limite**
   Par hypothèse de convergence dans $L^p$, on a :
   $$ \lim_{n \to \infty} \mathbb{E}\left[|X_n - X|^p\right] = 0 $$
   Puisque $\epsilon^p > 0$ est une constante fixée, le quotient tend vers $0$ :
   $$ \lim_{n \to \infty} \frac{\mathbb{E}\left[|X_n - X|^p\right]}{\epsilon^p} = 0 $$
   Puisque les probabilités sont toujours minorées par $0$, le théorème des gendarmes (encadrement) garantit que :
   $$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 $$
   La convergence en probabilité est rigoureusement établie.

### Démonstration : Convergence en Probabilité $\implies$ Convergence en Loi

1. **Initialisation / Cadre :**
   Nous supposons que pour tout $\epsilon > 0$, $\mathbb{P}(|X_n - X| > \epsilon) \to 0$. Nous voulons montrer que pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ continue et bornée, $\lim_{n \to \infty} \mathbb{E}[f(X_n)] = \mathbb{E}[f(X)]$.

2. **Étape 1 : Hypothèses sur la fonction $f$**
   Soit $f$ une fonction continue et bornée. Il existe un réel $M > 0$ tel que pour tout $x \in \mathbb{R}$, $|f(x)| \leq M$.
   Soit $\eta > 0$ un seuil de précision.
   Puisque $X$ est une variable aléatoire réelle, il existe un segment compact $K = [-A, A]$ suffisamment large tel que la masse de probabilité en dehors de $K$ soit petite :
   $$ \mathbb{P}(X \notin K) \leq \eta $$
   Sur le compact $K$, la fonction continue $f$ est uniformément continue (Théorème de Heine). Ainsi, il existe $\delta > 0$ tel que pour tout $x \in K$ et $y \in \mathbb{R}$ vérifiant $|x - y| \leq \delta$, on ait :
   $$ |f(x) - f(y)| \leq \eta $$

3. **Étape 2 : Partition de l'espace de probabilité**
   Nous voulons majorer l'écart des espérances :
   $$ |\mathbb{E}[f(X_n)] - \mathbb{E}[f(X)]| \leq \mathbb{E}\left[|f(X_n) - f(X)|\right] $$
   Partitionnons l'espace $\Omega$ en trois événements disjoints :
   - $E_1 = \{ \omega \in \Omega \mid |X_n(\omega) - X(\omega)| > \delta \}$
   - $E_2 = \{ \omega \in \Omega \mid |X_n(\omega) - X(\omega)| \leq \delta \} \cap \{ \omega \in \Omega \mid X(\omega) \notin K \}$
   - $E_3 = \{ \omega \in \Omega \mid |X_n(\omega) - X(\omega)| \leq \delta \} \cap \{ \omega \in \Omega \mid X(\omega) \in K \}$

   L'espérance se décompose en la somme des intégrales sur ces trois sous-ensembles :
   $$ \mathbb{E}\left[|f(X_n) - f(X)|\right] = \mathbb{E}\left[|f(X_n) - f(X)| \mathbf{1}_{E_1}\right] + \mathbb{E}\left[|f(X_n) - f(X)| \mathbf{1}_{E_2}\right] + \mathbb{E}\left[|f(X_n) - f(X)| \mathbf{1}_{E_3}\right] $$

4. **Étape 3 : Majoration terme à terme**
   - Sur l'événement $E_1$, on utilise la majoration globale induite par le fait que $f$ est bornée : $|f(X_n) - f(X)| \leq |f(X_n)| + |f(X)| \leq 2M$.
     $$ \mathbb{E}\left[|f(X_n) - f(X)| \mathbf{1}_{E_1}\right] \leq 2M \cdot \mathbb{P}(E_1) = 2M \cdot \mathbb{P}(|X_n - X| > \delta) $$
   - Sur l'événement $E_2$, on utilise encore la borne globale :
     $$ \mathbb{E}\left[|f(X_n) - f(X)| \mathbf{1}_{E_2}\right] \leq 2M \cdot \mathbb{P}(E_2) \leq 2M \cdot \mathbb{P}(X \notin K) \leq 2M \eta $$
   - Sur l'événement $E_3$, par définition de $\delta$ et de l'uniforme continuité sur $K$, on a $|f(X_n) - f(X)| \leq \eta$.
     $$ \mathbb{E}\left[|f(X_n) - f(X)| \mathbf{1}_{E_3}\right] \leq \eta \cdot \mathbb{P}(E_3) \leq \eta \cdot 1 = \eta $$

   L'inégalité totale devient :
   $$ \mathbb{E}\left[|f(X_n) - f(X)|\right] \leq 2M \cdot \mathbb{P}(|X_n - X| > \delta) + 2M \eta + \eta $$

5. **Conclusion : Passage à la limite**
   Par l'hypothèse de convergence en probabilité, nous savons que :
   $$ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \delta) = 0 $$
   En prenant la limite supérieure lorsque $n \to \infty$, le premier terme s'annule :
   $$ \limsup_{n \to \infty} \mathbb{E}\left[|f(X_n) - f(X)|\right] \leq 0 + 2M \eta + \eta = (2M + 1)\eta $$
   Puisque ce résultat est vrai pour tout $\eta > 0$ arbitrairement choisi, on peut faire tendre $\eta$ vers $0$ :
   $$ \limsup_{n \to \infty} \mathbb{E}\left[|f(X_n) - f(X)|\right] \leq 0 $$
   Comme la valeur absolue est positive, la limite est nécessairement $0$, achevant la preuve.

## 4. Applications en Physique Statistique, Logique et Apprentissage Automatique

La rigueur des modes de convergence offre une architecture sémantique essentielle pour qualifier le comportement asymptotique des algorithmes d'IA.

### A. Consistance des Estimateurs (Machine Learning PAC)
En théorie de l'apprentissage statistique (Probably Approximately Correct Learning), un modèle cherche à inférer les paramètres d'une loi génératrice à partir de $n$ échantillons. Un estimateur $\hat{\theta}_n$ est dit **consistant** s'il converge en probabilité vers la vraie valeur des paramètres $\theta^*$, soit $\hat{\theta}_n \xrightarrow{\mathbb{P}} \theta^*$. Cela signifie que la probabilité que l'algorithme se trompe de plus de $\epsilon$ tend vers $0$ avec l'accumulation des données.

**Exemple Calculatoire (Estimateur de la moyenne) :**
Soit un jeu de données de variables indépendantes et identiquement distribuées $Y_1, \dots, Y_n$ d'espérance $\mu$ et de variance $\sigma^2$. L'estimateur moyenne empirique est $\hat{\mu}_n = \frac{1}{n} \sum_{i=1}^n Y_i$.
L'espérance est $\mathbb{E}[\hat{\mu}_n] = \mu$ et la variance $\text{Var}(\hat{\mu}_n) = \frac{\sigma^2}{n}$.
Par l'inégalité de Bienaymé-Chebyshev :
$$ \mathbb{P}(|\hat{\mu}_n - \mu| \geq \epsilon) \leq \frac{\text{Var}(\hat{\mu}_n)}{\epsilon^2} = \frac{\sigma^2}{n \epsilon^2} $$
En prenant la limite, $\frac{\sigma^2}{n \epsilon^2} \to 0$, démontrant la consistance en probabilité de l'estimateur.

### B. Dynamique de la Descente de Gradient Stochastique (SGD)
Dans l'entraînement des réseaux de neurones profonds, la fonction de perte n'est pas calculée sur l'ensemble du jeu de données, mais estimée stochastiquement sur des mini-lots. Cette estimation introduit un bruit. Les travaux d'approximation stochastique (Robbins-Monro) s'appuient sur la théorie des martingales pour démontrer que, si le taux d'apprentissage $\alpha_n$ satisfait $\sum \alpha_n = \infty$ et $\sum \alpha_n^2 < \infty$, alors la suite des poids paramétriques $\theta_n$ converge **presque sûrement** vers un optimum local.

### C. Théorème Central Limite et Théorie de l'Information
Le passage des lois microscopiques déterministes aux lois macroscopiques continues repose sur la convergence en loi. Le Théorème Central Limite stipule que la somme normalisée de variables indépendantes converge **en loi** vers une distribution Gaussienne $\mathcal{N}(0, 1)$. En IA générative, notamment dans les modèles de diffusion, cette convergence justifie la modélisation du bruit asymptotique comme un processus d'Ornstein-Uhlenbeck convergeant vers une loi normale isotrope.
