---
uuid: "jalon-141"
title: "Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC"
year: 3
trimester: 12
tags:
  - math/fondations
  - ia/theorie
  - "[[Jalon-140.md]]"
  - "[[Jalon-142.md]]"
---
# Jalon 141 : Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC

## 1. Présentation du concept clé
*Chers étudiants, imaginez que vous êtes un explorateur dans un vaste pays inconnu. Vous ne pouvez pas visiter chaque recoin, mais vous voulez tout de même vous faire une idée très précise de la géographie, des populations, et des ressources de ce pays. Comment feriez-vous ?*

- **La Métaphore :** Imaginez que ce pays est une "distribution de données" infinie, et que chaque habitant est un "point de donnée". Vous ne pouvez observer qu'un petit échantillon d'habitants (votre "échantillon de données"). Votre objectif n'est pas seulement de connaître la taille moyenne des habitants, mais de comprendre la *répartition complète* de toutes leurs caractéristiques : combien sont grands, petits, aiment le café, possèdent une voiture rouge, etc.
    Les "Théorèmes de Glivenko-Cantelli" sont comme une promesse : si votre échantillon est suffisamment grand et que les caractéristiques que vous étudiez ne sont pas *trop compliquées* à définir, alors la répartition des caractéristiques que vous observez dans votre échantillon sera très, très proche de la vraie répartition dans tout le pays.
    La "classe de fonctions VC" est la clé de cette promesse. Elle nous dit ce que signifie "pas trop compliquée". Si les règles que vous utilisez pour classer les habitants (par exemple, "les habitants qui mesurent plus de 1m80 ET aiment le café ET ont un chien") sont d'une certaine complexité limitée (la "dimension VC"), alors cette promesse de convergence uniforme tient. C'est comme dire que si vos cartes ne sont pas trop détaillées au point de devenir illisibles, elles finiront par ressembler fidèlement au terrain.

- **Le "Pourquoi on a inventé ça" :** Dans le monde de l'Intelligence Artificielle et de l'apprentissage automatique, nous entraînons des modèles sur des données d'entraînement finies. Le rêve est que ces modèles fonctionnent aussi bien sur de nouvelles données, jamais vues auparavant. C'est le problème de la *généralisation*.
    Historiquement, les statisticiens et les informaticiens se sont heurtés à cette question : comment être sûr qu'un modèle appris sur un échantillon n'est pas juste "bon par hasard" sur cet échantillon, mais qu'il a réellement capturé une vérité sur la population sous-jacente ? Si nous voulons qu'un algorithme de classification, par exemple, apprenne à distinguer des chats des chiens, il doit le faire non seulement sur les images qu'on lui a montrées, mais aussi sur toutes les futures images de chats et de chiens.
    Les théorèmes de Glivenko-Cantelli généralisés, en particulier ceux liés à la dimension VC, ont été inventés pour fournir des garanties théoriques solides à ce problème. Ils nous disent que si la "capacité" ou la "complexité" de notre modèle (représentée par la classe de fonctions VC) est contrôlée, alors la performance observée sur l'échantillon d'entraînement sera un bon indicateur de la performance réelle sur l'ensemble des données possibles. C'est le fondement mathématique de la confiance que nous pouvons accorder à nos modèles d'IA.

- **Visualisation :** Imaginez un nuage de points représentant toutes les données possibles (la vraie distribution $P$). Vous n'en voyez qu'un sous-ensemble fini, votre échantillon $X_1, \dots, X_n$. Maintenant, imaginez une famille de "séparateurs" ou de "classificateurs" possibles. Par exemple, si vos données sont en 2D, cette famille pourrait être l'ensemble de toutes les lignes droites, ou l'ensemble de tous les cercles, ou l'ensemble de toutes les courbes polynomiales d'un certain degré.
    Chacun de ces séparateurs définit une fonction qui attribue une étiquette (+1 ou -1) à chaque point. Un théorème de Glivenko-Cantelli généralisé nous dit que si la famille de séparateurs n'est pas "trop flexible" (sa dimension VC est finie), alors, à mesure que vous ajoutez des points à votre échantillon, l'erreur que chaque séparateur fait sur votre échantillon (l'erreur empirique) va converger uniformément vers l'erreur qu'il ferait sur l'ensemble du nuage de points (l'erreur vraie).
    Visuellement, cela signifie que si vous tracez l'erreur empirique pour *tous* les séparateurs de votre famille, et que vous tracez l'erreur vraie pour *tous* ces mêmes séparateurs, les deux courbes d'erreur vont se rapprocher de plus en plus, jusqu'à devenir presque indiscernables, et ce, pour *tous* les séparateurs simultanément. C'est une convergence "uniforme" sur toute la classe de fonctions.

## 2. Formalisation & Rigueur Académique
*Nous allons maintenant plonger dans la formalisation de ces concepts. Préparez-vous à une précision chirurgicale, car chaque terme et chaque notation sont cruciaux pour la compréhension des garanties théoriques.*

### A. Définitions Formelles

Soit $(\mathcal{X}, \mathcal{A})$ un espace mesurable, où $\mathcal{X}$ est un ensemble non vide (l'espace des caractéristiques) et $\mathcal{A}$ est une $\sigma$-algèbre sur $\mathcal{X}$ (l'ensemble des événements mesurables). Soit $P$ une mesure de probabilité sur $(\mathcal{X}, \mathcal{A})$.

1.  **Échantillon aléatoire i.i.d. :** Un échantillon $X_1, X_2, \dots, X_n$ est dit indépendant et identiquement distribué (i.i.d.) selon $P$ si chaque $X_i$ est une variable aléatoire définie sur un espace de probabilité $(\Omega, \Sigma, \mathbb{P})$ à valeurs dans $\mathcal{X}$, telle que pour tout $A \in \mathcal{A}$, $\mathbb{P}(X_i \in A) = P(A)$, et les variables $X_i$ sont mutuellement indépendantes.

2.  **Mesure empirique :** Pour un échantillon $X_1, \dots, X_n$ i.i.d. selon $P$, la mesure empirique $P_n$ est définie pour tout $A \in \mathcal{A}$ par :
    $$P_n(A) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{X_i \in A}$$
    où $\mathbf{1}_{X_i \in A}$ est la fonction indicatrice qui vaut 1 si $X_i \in A$ et 0 sinon.

3.  **Classe de fonctions :** Soit $\mathcal{F}$ une classe de fonctions $f: \mathcal{X} \to \mathbb{R}$. Pour toute fonction $f \in \mathcal{F}$, nous définissons :
    *   L'espérance vraie de $f$ sous $P$ : $P(f) = \mathbb{E}_P[f(X)] = \int_{\mathcal{X}} f(x) dP(x)$.
    *   L'espérance empirique de $f$ sur l'échantillon $X_1, \dots, X_n$ : $P_n(f) = \frac{1}{n} \sum_{i=1}^n f(X_i)$.

4.  **Processus empirique :** Le processus empirique indexé par $\mathcal{F}$ est la collection de variables aléatoires $(P_n(f) - P(f))_{f \in \mathcal{F}}$.

5.  **Classe de Glivenko-Cantelli (uniforme) :** Une classe de fonctions $\mathcal{F}$ est dite une classe de Glivenko-Cantelli (uniforme presque sûre) si :
    $$\sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \xrightarrow{a.s.} 0 \quad \text{quand } n \to \infty$$
    où $\xrightarrow{a.s.}$ désigne la convergence presque sûre.

6.  **Shattering (pour une classe de sets) :** Soit $\mathcal{C}$ une classe de sous-ensembles de $\mathcal{X}$ (c'est-à-dire $\mathcal{C} \subseteq \mathcal{A}$). Un ensemble fini de points $\{x_1, \dots, x_m\} \subset \mathcal{X}$ est dit *shattered* par $\mathcal{C}$ si pour tout sous-ensemble $S \subseteq \{x_1, \dots, x_m\}$, il existe un ensemble $C \in \mathcal{C}$ tel que $C \cap \{x_1, \dots, x_m\} = S$. En d'autres termes, $\mathcal{C}$ peut "isoler" n'importe quel sous-ensemble des $m$ points.

7.  **Dimension de Vapnik-Chervonenkis (VC) pour une classe de sets :** La dimension VC d'une classe de sets $\mathcal{C}$, notée $\text{VCdim}(\mathcal{C})$, est le plus grand entier $m$ tel qu'il existe un ensemble de $m$ points qui peut être shattered par $\mathcal{C}$. Si aucun ensemble de taille arbitrairement grande ne peut être shattered, la dimension VC est infinie.

8.  **Pseudo-dimension VC pour une classe de fonctions (à valeurs réelles) :** Soit $\mathcal{F}$ une classe de fonctions $f: \mathcal{X} \to \mathbb{R}$. La pseudo-dimension VC de $\mathcal{F}$ est la dimension VC de la classe de sets d'épigraphes $\mathcal{C}_{\mathcal{F}} = \{ \{(x, t) \in \mathcal{X} \times \mathbb{R} \mid f(x) \ge t \} \mid f \in \mathcal{F} \}$.
    Une définition équivalente et plus courante est la suivante : un ensemble de points $\{x_1, \dots, x_m\} \subset \mathcal{X}$ est *pseudo-shattered* par $\mathcal{F}$ s'il existe des "seuils" $t_1, \dots, t_m \in \mathbb{R}$ tels que pour tout sous-ensemble $S \subseteq \{x_1, \dots, x_m\}$, il existe une fonction $f \in \mathcal{F}$ vérifiant :
    *   $f(x_i) \ge t_i$ si $x_i \in S$
    *   $f(x_i) < t_i$ si $x_i \notin S$
    La pseudo-dimension VC de $\mathcal{F}$, notée $\text{VCdim}(\mathcal{F})$ ou $\text{Pdim}(\mathcal{F})$, est le plus grand entier $m$ tel qu'il existe un ensemble de $m$ points qui peut être pseudo-shattered par $\mathcal{F}$.

9.  **Variables de Rademacher :** Soit $\epsilon_1, \dots, \epsilon_n$ une suite de variables aléatoires i.i.d. telles que $\mathbb{P}(\epsilon_i = 1) = \mathbb{P}(\epsilon_i = -1) = 1/2$.

10. **Complexité de Rademacher empirique :** Pour une classe de fonctions $\mathcal{F}$ et un échantillon fixe $x_1, \dots, x_n \in \mathcal{X}$, la complexité de Rademacher empirique est définie par :
    $$\hat{\mathcal{R}}_n(\mathcal{F}) = \mathbb{E}_{\epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(x_i) \right| \right]$$
    où l'espérance est prise par rapport aux variables de Rademacher $\epsilon_i$.

11. **Complexité de Rademacher (vraie) :** La complexité de Rademacher (vraie) est $\mathcal{R}_n(\mathcal{F}) = \mathbb{E}_X[\hat{\mathcal{R}}_n(\mathcal{F})]$, où l'espérance est prise par rapport à l'échantillon $X_1, \dots, X_n$.

### B. Théorèmes, Propositions & Lemmes

> **Théorème de Glivenko-Cantelli (classique, 1933) :**
> Soit $P$ une mesure de probabilité sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ et $F(x) = P((-\infty, x])$ sa fonction de répartition. Soit $X_1, \dots, X_n$ un échantillon i.i.d. selon $P$, et $F_n(x) = P_n((-\infty, x]) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{X_i \le x}$ la fonction de répartition empirique. Alors :
> $$\sup_{x \in \mathbb{R}} |F_n(x) - F(x)| \xrightarrow{a.s.} 0 \quad \text{quand } n \to \infty$$

> **Théorème de Vapnik-Chervonenkis (VC) (pour classes de sets, 1971) :**
> Soit $\mathcal{C}$ une classe de sous-ensembles mesurables de $\mathcal{X}$. Alors $\mathcal{C}$ est une classe de Glivenko-Cantelli (uniforme presque sûre) si et seulement si sa dimension VC, $\text{VCdim}(\mathcal{C})$, est finie.

> **Théorème de Glivenko-Cantelli généralisé (pour classes de fonctions VC) :**
> Soit $\mathcal{F}$ une classe de fonctions $f: \mathcal{X} \to [0, B]$ pour une constante $B > 0$. Si la pseudo-dimension VC de $\mathcal{F}$, $\text{Pdim}(\mathcal{F})$, est finie, alors $\mathcal{F}$ est une classe de Glivenko-Cantelli (uniforme presque sûre) :
> $$\sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \xrightarrow{a.s.} 0 \quad \text{quand } n \to \infty$$
> *Note : Ce théorème peut être étendu à des fonctions non bornées sous certaines conditions d'intégrabilité, mais la version bornée est la plus courante et la plus simple à manipuler.*

> **Lemme de Symmetrisation (fondamental) :**
> Soit $\mathcal{F}$ une classe de fonctions $f: \mathcal{X} \to \mathbb{R}$. Soit $X_1, \dots, X_n$ un échantillon i.i.d. selon $P$. Soient $\epsilon_1, \dots, \epsilon_n$ des variables de Rademacher i.i.d. et indépendantes de $X_1, \dots, X_n$. Alors, pour toute fonction non décroissante $\phi: \mathbb{R}^+ \to \mathbb{R}^+$, nous avons :
> $$\mathbb{E}_X \left[ \phi\left( \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right) \right] \le \mathbb{E}_{X, \epsilon} \left[ \phi\left( 2 \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right) \right]$$
> Si $\mathcal{F}$ est une classe de fonctions indicatrices, $f: \mathcal{X} \to \{0,1\}$, alors :
> $$\mathbb{E}_X \left[ \phi\left( \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right) \right] \le \mathbb{E}_{X, \epsilon} \left[ \phi\left( 2 \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i (f(X_i) - P(f)) \right| \right) \right]$$
> Et plus simplement, pour l'espérance de la déviation elle-même ($\phi(t)=t$):
> $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] \le 2 \mathbb{E}_{X, \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right] = 2 \mathcal{R}_n(\mathcal{F})$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*La démonstration complète du Théorème de Glivenko-Cantelli généralisé est un parcours exigeant, impliquant plusieurs étapes complexes. Nous allons nous concentrer ici sur la démonstration du Lemme de Symmetrisation, qui est une étape pivotale et fondamentale dans la théorie des processus empiriques et des bornes de généralisation. Ce lemme permet de transformer la difficile tâche de borner la déviation par rapport à la vraie espérance (inconnue) en une tâche plus gérable de borner une somme de variables aléatoires signées (complexité de Rademacher).*

### Démonstration du Théorème Pivot : Lemme de Symmetrisation
1.  **Initialisation / Cadre :**
    Nous souhaitons démontrer que $\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] \le 2 \mathbb{E}_{X, \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right]$.
    Soit $X_1, \dots, X_n$ un échantillon i.i.d. de $P$.
    Soit $X'_1, \dots, X'_n$ un *échantillon fantôme* indépendant de $X_1, \dots, X_n$ mais ayant la même distribution $P$.
    Soient $\epsilon_1, \dots, \epsilon_n$ des variables de Rademacher i.i.d. et indépendantes de $X_1, \dots, X_n$ et $X'_1, \dots, X'_n$.
    La stratégie consiste à introduire l'échantillon fantôme pour "symmetriser" la différence $P_n(f) - P(f)$, puis à utiliser les variables de Rademacher pour relier cette expression à la complexité de Rademacher.

2.  **Étape 1 : Introduction de l'échantillon fantôme**
    Nous commençons par l'expression que nous voulons borner :
    $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right]$$
    Nous savons que $P(f) = \mathbb{E}_{X'}[f(X')]$ pour toute fonction $f \in \mathcal{F}$, où $X'$ est une variable aléatoire distribuée selon $P$.
    Puisque $X'_1, \dots, X'_n$ est un échantillon i.i.d. de $P$ et indépendant de $X_1, \dots, X_n$, nous pouvons remplacer $P(f)$ par une moyenne empirique sur l'échantillon fantôme, en prenant l'espérance sur cet échantillon fantôme.
    $$P(f) = \mathbb{E}_{X'} \left[ \frac{1}{n} \sum_{j=1}^n f(X'_j) \right]$$
    En substituant cette expression dans la déviation, nous obtenons :
    $$P_n(f) - P(f) = \frac{1}{n} \sum_{i=1}^n f(X_i) - \mathbb{E}_{X'} \left[ \frac{1}{n} \sum_{j=1}^n f(X'_j) \right]$$
    Nous pouvons intervertir l'espérance et le supremum (par le Lemme de Fatou généralisé ou simplement par la linéarité de l'espérance si le supremum est mesurable et borné, ce qui est le cas ici pour des classes de fonctions bien définies) :
    $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] = \mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n f(X_i) - \mathbb{E}_{X'} \left[ \frac{1}{n} \sum_{j=1}^n f(X'_j) \right] \right| \right]$$
    Maintenant, nous utilisons une propriété clé : pour toute variable aléatoire $Z$, $|Z| = |\mathbb{E}[Z] - Z + Z| \le |\mathbb{E}[Z] - Z| + |Z|$. Plus simplement, pour toute fonction $g$, $\mathbb{E}[g(X)] = \mathbb{E}_{X'}[\frac{1}{n}\sum_{j=1}^n g(X'_j)]$.
    Donc, nous pouvons écrire :
    $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] = \mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} \left| \mathbb{E}_{X'} \left[ \frac{1}{n} \sum_{j=1}^n f(X_j) - \frac{1}{n} \sum_{j=1}^n f(X'_j) \right] \right| \right]$$
    Par l'inégalité de Jensen (ou simplement le fait que $|\mathbb{E}[Z]| \le \mathbb{E}[|Z|]$), nous pouvons déplacer l'espérance sur $X'$ à l'extérieur de la valeur absolue :
    $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] \le \mathbb{E}_X \left[ \mathbb{E}_{X'} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{j=1}^n f(X_j) - \frac{1}{n} \sum_{j=1}^n f(X'_j) \right| \right] \right]$$
    Puisque les échantillons $X$ et $X'$ sont indépendants, nous pouvons combiner les espérances :
    $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] \le \mathbb{E}_{X, X'} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n (f(X_i) - f(X'_i)) \right| \right]$$

3.  **Étape 2 (Transition micro-calculatoire) : Introduction des variables de Rademacher**
    Considérons la somme $\sum_{i=1}^n (f(X_i) - f(X'_i))$.
    Puisque $(X_i, X'_i)$ sont i.i.d. pour $i=1, \dots, n$, et que $X_i$ et $X'_i$ sont identiquement distribués, la distribution de $(X_i, X'_i)$ est la même que celle de $(X'_i, X_i)$.
    Soient $\epsilon_1, \dots, \epsilon_n$ des variables de Rademacher i.i.d. et indépendantes de $X$ et $X'$.
    Pour chaque $i$, la variable aléatoire $(f(X_i) - f(X'_i))$ a la même distribution que $\epsilon_i (f(X_i) - f(X'_i))$.
    Pour le voir, notons $Z_i = f(X_i) - f(X'_i)$. La distribution de $Z_i$ est symétrique autour de 0, car $f(X_i) - f(X'_i)$ a la même distribution que $-(f(X'_i) - f(X_i))$.
    Plus formellement, pour toute fonction mesurable $g$, $\mathbb{E}[g(f(X_i) - f(X'_i))] = \mathbb{E}[g(f(X'_i) - f(X_i))]$.
    De plus, $\epsilon_i$ est indépendante de $(X_i, X'_i)$.
    Donc, $\mathbb{E}[g(\epsilon_i (f(X_i) - f(X'_i)))] = \mathbb{E}_{\epsilon_i} \left[ \mathbb{E}_{X_i, X'_i} \left[ g(\epsilon_i (f(X_i) - f(X'_i))) \right] \right]$.
    Pour $\epsilon_i = 1$, on a $\mathbb{E}_{X_i, X'_i}[g(f(X_i) - f(X'_i))]$.
    Pour $\epsilon_i = -1$, on a $\mathbb{E}_{X_i, X'_i}[g(-(f(X_i) - f(X'_i)))] = \mathbb{E}_{X_i, X'_i}[g(f(X'_i) - f(X_i))]$.
    Puisque $X_i$ et $X'_i$ sont i.i.d., la distribution de $(X_i, X'_i)$ est la même que celle de $(X'_i, X_i)$. Donc, $\mathbb{E}_{X_i, X'_i}[g(f(X_i) - f(X'_i))] = \mathbb{E}_{X_i, X'_i}[g(f(X'_i) - f(X_i))]$.
    Par conséquent, $\mathbb{E}[g(\epsilon_i (f(X_i) - f(X'_i)))] = \frac{1}{2} \mathbb{E}_{X_i, X'_i}[g(f(X_i) - f(X'_i))] + \frac{1}{2} \mathbb{E}_{X_i, X'_i}[g(f(X'_i) - f(X_i))] = \mathbb{E}_{X_i, X'_i}[g(f(X_i) - f(X'_i))]$.
    Cela signifie que la distribution de $f(X_i) - f(X'_i)$ est la même que la distribution de $\epsilon_i (f(X_i) - f(X'_i))$.
    En utilisant cette propriété, nous pouvons introduire les variables de Rademacher. Puisque la fonction $\sup_{f \in \mathcal{F}} |\cdot|$ est convexe, nous pouvons appliquer l'inégalité de Jensen pour l'espérance conditionnelle.
    Plus simplement, nous pouvons remplacer la variable aléatoire $(f(X_i) - f(X'_i))$ par $\epsilon_i (f(X_i) - f(X'_i))$ sous l'espérance, car elles ont la même distribution.
    $$\mathbb{E}_{X, X'} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n (f(X_i) - f(X'_i)) \right| \right] = \mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i (f(X_i) - f(X'_i)) \right| \right]$$
    Maintenant, nous utilisons l'inégalité triangulaire : $|a-b| \le |a| + |b|$.
    $$\sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i (f(X_i) - f(X'_i)) \right| \le \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| + \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X'_i) \right|$$
    En prenant l'espérance des deux côtés :
    $$\mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i (f(X_i) - f(X'_i)) \right| \right] \le \mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right] + \mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X'_i) \right| \right]$$
    Considérons le premier terme du membre de droite : $\mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right]$. Puisque l'expression à l'intérieur du supremum ne dépend pas de $X'$, nous pouvons ignorer l'espérance sur $X'$.
    $$ \mathbb{E}_{X, \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right] $$
    Considérons le second terme du membre de droite : $\mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X'_i) \right| \right]$.
    Puisque $X_1, \dots, X_n$ et $X'_1, \dots, X'_n$ sont i.i.d. et ont la même distribution $P$, et que les variables de Rademacher $\epsilon_i$ sont indépendantes d'eux, l'espérance de la complexité de Rademacher calculée sur $X'$ est la même que celle calculée sur $X$.
    C'est-à-dire :
    $$\mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X'_i) \right| \right] = \mathbb{E}_{X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X'_i) \right| \right] = \mathbb{E}_{X, \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right]$$
    Donc, en combinant les deux termes :
    $$\mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i (f(X_i) - f(X'_i)) \right| \right] \le 2 \mathbb{E}_{X, \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right]$$

4.  **Conclusion :**
    En récapitulant les étapes, nous avons montré que :
    $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] \le \mathbb{E}_{X, X'} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n (f(X_i) - f(X'_i)) \right| \right]$$
    Et ensuite :
    $$\mathbb{E}_{X, X'} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n (f(X_i) - f(X'_i)) \right| \right] = \mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i (f(X_i) - f(X'_i)) \right| \right]$$
    Et enfin :
    $$\mathbb{E}_{X, X', \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i (f(X_i) - f(X'_i)) \right| \right] \le 2 \mathbb{E}_{X, \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right]$$
    En combinant ces inégalités, nous obtenons le résultat souhaité pour $\phi(t)=t$:
    $$\mathbb{E}_X \left[ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \right] \le 2 \mathbb{E}_{X, \epsilon} \left[ \sup_{f \in \mathcal{F}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i) \right| \right] = 2 \mathcal{R}_n(\mathcal{F})$$
    La démonstration pour la fonction $\phi$ non décroissante suit le même raisonnement en appliquant $\phi$ à l'intérieur de l'espérance et en utilisant la convexité de $\phi \circ |\cdot|$. Ce lemme est crucial car il relie la déviation par rapport à la vraie moyenne (inconnue) à la complexité de Rademacher, qui est une quantité mesurable et bornable. Le reste de la preuve du théorème de Glivenko-Cantelli généralisé s'appuie sur des bornes de la complexité de Rademacher en fonction de la dimension VC et des inégalités de concentration.

## 4. Exercices d'Application & Pratique de Concours
*Ces exercices sont conçus pour solidifier votre compréhension des concepts de dimension VC et de complexité de Rademacher, des outils essentiels pour la théorie de la généralisation.*

### Exercice 1 : Application Directe
**Énoncé :**
Soit $\mathcal{C}$ la classe de tous les intervalles $[a, b]$ sur $\mathbb{R}$, où $a, b \in \mathbb{R}$ et $a \le b$.
1.  Déterminez la dimension VC de la classe $\mathcal{C}$ des fonctions indicatrices $\mathbf{1}_{x \in [a,b]}$.
2.  En utilisant le théorème de VC pour les classes de sets, que pouvez-vous conclure sur la convergence uniforme de la fréquence empirique d'appartenance à un intervalle ?

**Correction Détaillée :**
*   *Analyse de l'énoncé :* Nous devons trouver le plus grand nombre de points que la classe $\mathcal{C}$ peut "shatter". Shatter signifie que pour tout sous-ensemble de ces points, il existe un intervalle dans $\mathcal{C}$ qui contient exactement ce sous-ensemble et aucun autre point de l'ensemble initial.

*   *Résolution pas-à-pas :*
    1.  **Recherche de la dimension VC de $\mathcal{C}$ :**
        *   **Peut-on shatter 1 point ?** Soit $\{x_1\}$ un ensemble de 1 point.
            *   Pour le sous-ensemble $\emptyset$ : L'intervalle $[x_1+1, x_1+2]$ ne contient pas $x_1$.
            *   Pour le sous-ensemble $\{x_1\}$ : L'intervalle $[x_1, x_1]$ (ou $[x_1-0.5, x_1+0.5]$) contient $x_1$.
            Donc, 1 point peut être shattered. La dimension VC est au moins 1.
        *   **Peut-on shatter 2 points ?** Soit $\{x_1, x_2\}$ avec $x_1 < x_2$.
            *   $\emptyset$: $[x_2+1, x_2+2]$
            *   $\{x_1\}$: $[x_1, x_1]$ (ou $[x_1-0.5, x_1+0.5]$)
            *   $\{x_2\}$: $[x_2, x_2]$ (ou $[x_2-0.5, x_2+0.5]$)
            *   $\{x_1, x_2\}$: $[x_1, x_2]$
            Donc, 2 points peuvent être shattered. La dimension VC est au moins 2.
        *   **Peut-on shatter 3 points ?** Soit $\{x_1, x_2, x_3\}$ avec $x_1 < x_2 < x_3$.
            Nous devons vérifier si tous les $2^3 = 8$ sous-ensembles peuvent être formés.
            Considérons le sous-ensemble $\{x_1, x_3\}$. Peut-on trouver un intervalle $[a, b]$ tel que $x_1 \in [a,b]$, $x_3 \in [a,b]$, et $x_2 \notin [a,b]$ ?
            Si $x_1 \in [a,b]$ et $x_3 \in [a,b]$, alors nécessairement, tout point entre $x_1$ et $x_3$ doit aussi être dans $[a,b]$. Puisque $x_1 < x_2 < x_3$, cela implique que $x_2$ doit être dans $[a,b]$.
            Par conséquent, il est impossible de former le sous-ensemble $\{x_1, x_3\}$ sans inclure $x_2$.
            Donc, 3 points ne peuvent pas être shattered par la classe des intervalles.
        *   **Conclusion pour la dimension VC :** Puisque 2 points peuvent être shattered mais 3 points ne le peuvent pas, la dimension VC de la classe des intervalles sur $\mathbb{R}$ est $\text{VCdim}(\mathcal{C}) = 2$.

    2.  **Conclusion sur la convergence uniforme :**
        Le théorème de Vapnik-Chervonenkis stipule qu'une classe de sets $\mathcal{C}$ est une classe de Glivenko-Cantelli (uniforme presque sûre) si et seulement si sa dimension VC est finie.
        Puisque nous avons trouvé que $\text{VCdim}(\mathcal{C}) = 2$, qui est une valeur finie, nous pouvons conclure que la classe des fonctions indicatrices d'intervalles sur $\mathbb{R}$ est une classe de Glivenko-Cantelli.
        Cela signifie que pour un échantillon i.i.d. $X_1, \dots, X_n$ tiré d'une distribution $P$ sur $\mathbb{R}$, la déviation maximale entre la fréquence empirique et la probabilité vraie d'appartenance à *n'importe quel* intervalle $[a,b]$ converge presque sûrement vers 0 lorsque $n \to \infty$:
        $$\sup_{[a,b] \in \mathcal{C}} \left| \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{X_i \in [a,b]} - P([a,b]) \right| \xrightarrow{a.s.} 0$$
        Ceci est une généralisation du théorème de Glivenko-Cantelli classique qui ne concerne que les intervalles $(-\infty, x]$.

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT)
**Énoncé :**
Soit $\mathcal{F}$ la classe des fonctions linéaires $f(x) = \mathbf{w}^\top \mathbf{x} + b$ sur $\mathbb{R}^d$, où $\mathbf{w} \in \mathbb{R}^d$, $b \in \mathbb{R}$. Nous considérons la classe de fonctions indicatrices $\mathcal{C} = \{ \mathbf{1}_{f(x) \ge 0} \mid f \in \mathcal{F} \}$. Cette classe représente les classificateurs linéaires (séparateurs par hyperplans).
1.  Démontrez que la dimension VC de $\mathcal{C}$ est au moins $d+1$.
2.  Expliquez intuitivement pourquoi la dimension VC de $\mathcal{C}$ est exactement $d+1$. (La preuve formelle que la dimension VC n'est pas $d+2$ est plus complexe et ne sera pas demandée ici, mais la compréhension intuitive est cruciale).
3.  En vous appuyant sur le Lemme de Symmetrisation et l'idée de la dimension VC, expliquez comment on peut borner la déviation uniforme $\mathbb{E}\left[ \sup_{h \in \mathcal{C}} |P_n(h) - P(h)| \right]$ pour cette classe de classificateurs.

**Correction Détaillée :**
*   *Analyse de l'énoncé :* Nous travaillons avec des classificateurs linéaires dans un espace de dimension $d$. Un classificateur linéaire sépare l'espace en deux demi-espaces. La dimension VC de cette classe est une mesure de sa capacité à "séparer" des points arbitrairement étiquetés.

*   *Résolution pas-à-pas :*
    1.  **Démonstration que $\text{VCdim}(\mathcal{C}) \ge d+1$ :**
        Nous devons trouver un ensemble de $d+1$ points dans $\mathbb{R}^d$ qui peut être shattered par la classe des hyperplans.
        Considérons l'ensemble de $d+1$ points suivants :
        $x_0 = \mathbf{0}$ (l'origine)
        $x_1 = \mathbf{e}_1$ (le premier vecteur de base canonique)
        ...
        $x_d = \mathbf{e}_d$ (le $d$-ième vecteur de base canonique)
        Ces $d+1$ points sont affinement indépendants. Cela signifie que si nous formons le vecteur $(x_i, 1)$ en ajoutant une dimension pour le terme de biais, ces $d+1$ vecteurs $(x_i, 1)$ sont linéairement indépendants dans $\mathbb{R}^{d+1}$.
        Soit $S \subseteq \{x_0, x_1, \dots, x_d\}$ un sous-ensemble arbitraire de ces points. Nous voulons montrer qu'il existe un hyperplan $f(x) = \mathbf{w}^\top \mathbf{x} + b = 0$ tel que $f(x_i) \ge 0$ si $x_i \in S$ et $f(x_i) < 0$ si $x_i \notin S$.
        Ceci revient à trouver $(\mathbf{w}, b)$ tel que :
        *   $\mathbf{w}^\top x_i + b \ge 0$ pour $x_i \in S$
        *   $\mathbf{w}^\top x_i + b < 0$ pour $x_i \notin S$
        Puisque les points $x_0, \dots, x_d$ sont affinement indépendants, pour toute assignation de labels binaires à ces $d+1$ points, il existe un hyperplan qui les sépare exactement. C'est un résultat standard de la géométrie des hyperplans.
        Plus formellement, nous pouvons construire un système d'équations linéaires. Pour chaque $x_i$, nous voulons assigner une valeur $y_i \in \{+1, -1\}$. Nous cherchons $(\mathbf{w}, b)$ tel que $y_i (\mathbf{w}^\top x_i + b) > 0$ pour tous $i$.
        Puisque les points $(x_i, 1)$ sont linéairement indépendants dans $\mathbb{R}^{d+1}$, la matrice $M$ dont les lignes sont $(x_i^\top, 1)$ a un rang de $d+1$. Cela garantit que nous pouvons trouver un vecteur $(\mathbf{w}^\top, b)^\top$ qui réalise n'importe quelle séparation linéaire des points.
        Par exemple, si nous voulons $f(x_i) = y_i$, nous pouvons résoudre le système linéaire. Pour le shattering, nous avons besoin de $f(x_i) \ge 0$ ou $f(x_i) < 0$. En choisissant des marges suffisamment petites, on peut toujours trouver un hyperplan.
        Donc, $d+1$ points peuvent être shattered. La dimension VC est au moins $d+1$.

    2.  **Explication intuitive de $\text{VCdim}(\mathcal{C}) = d+1$ :**
        La raison intuitive pour laquelle la dimension VC des hyperplans en $\mathbb{R}^d$ est exactement $d+1$ est liée à la notion de "degrés de liberté" d'un hyperplan. Un hyperplan en $\mathbb{R}^d$ est défini par $d+1$ paramètres (les $d$ composantes de $\mathbf{w}$ et le terme de biais $b$).
        Si nous avons $m$ points, et que $m \le d+1$, nous pouvons généralement trouver un hyperplan qui sépare ces points de n'importe quelle manière souhaitée. C'est parce que nous avons "suffisamment de degrés de liberté" dans la définition de l'hyperplan pour s'adapter à toutes les configurations de labels.
        Cependant, si nous avons $d+2$ points, ils ne peuvent plus être affinement indépendants. Cela signifie qu'il y aura toujours une relation linéaire entre eux. Cette relation impose des contraintes sur la façon dont ils peuvent être séparés. Par exemple, si $d=1$ (points sur une ligne), la dimension VC est $1+1=2$. On peut shatter 2 points (par exemple, $x_1=0, x_2=1$: $\{0\}$, $\{1\}$, $\{0,1\}$, $\emptyset$). Mais on ne peut pas shatter 3 points (par exemple, $x_1=0, x_2=1, x_3=2$). On ne peut pas avoir $\{0,2\}$ sans inclure $1$.
        En général, pour $d+2$ points en $\mathbb{R}^d$, il existe toujours une combinaison linéaire des points qui est nulle, ou une combinaison convexe qui inclut un point à l'intérieur de l'enveloppe convexe des autres. Cette structure géométrique limite la capacité de l'hyperplan à séparer arbitrairement les points. Il y aura toujours au moins une configuration de labels que l'hyperplan ne pourra pas réaliser.
        La preuve formelle de $\text{VCdim}(\mathcal{C}) \le d+1$ est plus technique et utilise le théorème de Radon ou des arguments de dualité, montrant qu'il existe toujours une configuration de $d+2$ points qui ne peut pas être shattered.

    3.  **Borne de la déviation uniforme en utilisant le Lemme de Symmetrisation et la dimension VC :**
        Le Lemme de Symmetrisation nous donne une borne sur l'espérance de la déviation uniforme :
        $$\mathbb{E}\left[ \sup_{h \in \mathcal{C}} |P_n(h) - P(h)| \right] \le 2 \mathbb{E}_{X, \epsilon} \left[ \sup_{h \in \mathcal{C}} \left| \frac{1}{n} \sum_{i=1}^n \epsilon_i h(X_i) \right| \right]$$
        Le terme de droite est $2 \mathcal{R}_n(\mathcal{C})$, la complexité de Rademacher (vraie) de la classe $\mathcal{C}$.
        Pour relier la complexité de Rademacher à la dimension VC, on utilise des bornes classiques comme le théorème de Massart ou le théorème de Dudley pour les nombres de recouvrement. Un résultat fondamental est que pour une classe de fonctions indicatrices $\mathcal{C}$ avec $\text{VCdim}(\mathcal{C}) = d_{VC}$, la complexité de Rademacher empirique est bornée par :
        $$\hat{\mathcal{R}}_n(\mathcal{C}) \le C \sqrt{\frac{d_{VC} \log(n/d_{VC})}{n}}$$
        où $C$ est une constante.
        En prenant l'espérance sur l'échantillon $X_1, \dots, X_n$, nous obtenons une borne pour la complexité de Rademacher vraie :
        $$\mathcal{R}_n(\mathcal{C}) = \mathbb{E}_X[\hat{\mathcal{R}}_n(\mathcal{C})] \le C \sqrt{\frac{d_{VC} \log(n/d_{VC})}{n}}$$
        En combinant avec le Lemme de Symmetrisation, nous obtenons une borne sur la déviation uniforme :
        $$\mathbb{E}\left[ \sup_{h \in \mathcal{C}} |P_n(h) - P(h)| \right] \le 2C \sqrt{\frac{d_{VC} \log(n/d_{VC})}{n}}$$
        Puisque pour notre classe de classificateurs linéaires, $d_{VC} = d+1$, nous avons :
        $$\mathbb{E}\left[ \sup_{h \in \mathcal{C}} |P_n(h) - P(h)| \right] \le 2C \sqrt{\frac{(d+1) \log(n/(d+1))}{n}}$$
        Cette borne montre que la déviation uniforme tend vers 0 lorsque $n \to \infty$, et la vitesse de convergence dépend de la dimension $d$ de l'espace (via $d_{VC}$). Plus la dimension VC est grande, plus la classe est complexe, et plus il faut de données $n$ pour garantir une bonne convergence uniforme. C'est le cœur des garanties de généralisation en apprentissage automatique.

## 5. Ancrage & Application en Intelligence Artificielle
*Les théorèmes de Glivenko-Cantelli généralisés et la théorie de la dimension VC ne sont pas de simples curiosités mathématiques ; ils sont les piliers fondamentaux sur lesquels repose une grande partie de la théorie de l'apprentissage automatique moderne.*

-   **Le Pont Théorique :** Ces théorèmes fournissent la justification mathématique de la *généralisation* en apprentissage automatique. En IA, nous entraînons un modèle (par exemple, un classificateur) sur un ensemble de données d'entraînement fini. Nous mesurons sa performance par l'erreur empirique (ou risque empirique) sur cet ensemble. Ce que nous voulons vraiment, c'est que le modèle soit performant sur des données *nouvelles et invisibles*, c'est-à-dire que son erreur vraie (ou risque vrai) soit faible.
    Les théorèmes de Glivenko-Cantelli généralisés nous disent que si la classe de fonctions que notre modèle peut apprendre (sa "capacité" ou "complexité", souvent mesurée par sa dimension VC) est finie, alors l'erreur empirique converge uniformément vers l'erreur vraie pour toute fonction de cette classe. Cela signifie que si nous trouvons un modèle dans cette classe qui a une faible erreur empirique, il est très probable qu'il aura aussi une faible erreur vraie. C'est la base du principe de minimisation du risque empirique (ERM) : choisir la fonction $f$ dans la classe $\mathcal{F}$ qui minimise $P_n(f)$ est une stratégie valide pour minimiser $P(f)$, à condition que $\mathcal{F}$ ait une dimension VC finie et que $n$ soit suffisamment grand.

-   **Exemple Concret :**
    *   **Support Vector Machines (SVM) :** Les SVMs linéaires sont des classificateurs qui trouvent un hyperplan optimal pour séparer les données. Comme nous l'avons vu dans l'exercice 2, la classe des hyperplans en $\mathbb{R}^d$ a une dimension VC de $d+1$. Cette dimension VC finie garantit que les SVMs linéaires ont de bonnes propriétés de généralisation. Si nous entraînons un SVM linéaire sur un grand ensemble de données, nous pouvons être confiants que son erreur sur de nouvelles données sera proche de son erreur sur l'entraînement. Pour les SVMs à noyau (kernel SVMs), la dimension VC peut être infinie dans l'espace de Hilbert des caractéristiques, mais la complexité effective est contrôlée par d'autres mesures (comme la marge ou la complexité de Rademacher du noyau), permettant toujours des garanties de généralisation.
    *   **Réseaux de Neurones :** Les réseaux de neurones, en particulier les réseaux profonds, sont des classes de fonctions extrêmement complexes. Leur dimension VC exacte est souvent très difficile à calculer et peut être très grande. Cependant, des bornes sur la dimension VC ou la pseudo-dimension VC des réseaux de neurones avec un nombre fini de neurones et des fonctions d'activation spécifiques existent. Ces bornes, bien que souvent lâches, nous rappellent que la capacité d'un réseau doit être contrôlée. C'est pourquoi des techniques de régularisation (comme le *dropout*, la régularisation L1/L2, l'arrêt précoce) sont cruciales en apprentissage profond. Elles visent à réduire la "capacité effective" du modèle pour éviter le surapprentissage (overfitting), même si la dimension VC théorique reste élevée. Les théorèmes de Glivenko-Cantelli généralisés nous disent que sans un contrôle de la complexité, la convergence uniforme n'est pas garantie, et donc la généralisation est compromise.

## 6. Liens Sémantiques & Maillage Obsidian
-   **Concepts Précédents requis :** [[Jalon-140.md]] (Probabilités et Mesures), [[Jalon-130.md]] (Inégalités de Concentration : Hoeffding, Bernstein), [[Jalon-135.md]] (Complexité de Rademacher et Nombres de Recouvrement).
-   **Concepts Futurs dépendants :** [[Jalon-142.md]] (Bornes de Généralisation pour l'Apprentissage Statistique), [[Jalon-150.md]] (Théorie de l'Apprentissage Statistique : ERM, PAC Learning), [[Jalon-155.md]] (Stabilité et Régularisation des Algorithmes d'Apprentissage).
