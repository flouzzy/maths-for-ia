---
uuid: "jalon-82"
title: "Introduction aux distributions de Schwartz"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 81 (Transformée de Fourier dans L2).md]]"
next: "[[Jalon 83 (Dérivation au sens des distributions).md]]"
---

# Jalon 82 : Introduction à la théorie des distributions de Schwartz

## 1. Introduction historique et fondements conceptuels

L'analyse mathématique classique, forgée par Newton, Leibniz, Cauchy et Riemann, s'est construite sur le concept de fonction : une entité qui associe à chaque point de l'espace une valeur numérique bien définie. Ce paradigme a permis de décrire avec une précision remarquable une vaste gamme de phénomènes physiques, de la mécanique céleste à la propagation de la chaleur. Cependant, au tournant du XXe siècle, les physiciens et les ingénieurs se sont heurtés à des problèmes où ce cadre formel s'est révélé dramatiquement insuffisant.

L'exemple le plus paradigmatique est sans doute celui de la modélisation d'un choc instantané en mécanique ou d'une charge électrique ponctuelle en électromagnétisme. Paul Dirac, physicien théoricien britannique, a introduit dans les années 1920, pour les besoins de la mécanique quantique naissante, un objet mathématique étrange : la "fonction" $\delta$. Cette "fonction" devait avoir la propriété singulière d'être nulle partout sauf à l'origine où elle serait infinie, tout en ayant une intégrale sur l'espace entier exactement égale à 1. Formellement :
$$ \delta(x) = \begin{cases} +\infty & \text{si } x = 0 \\ 0 & \text{si } x \neq 0 \end{cases} \quad \text{et} \quad \int_{-\infty}^{+\infty} \delta(x) dx = 1 $$
Du point de vue de l'analyse classique (mesure de Lebesgue), un tel objet ne peut exister. Toute fonction valant zéro presque partout a une intégrale nulle. Le "Dirac" de la physique était donc une hérésie mathématique. Pourtant, les calculs réalisés avec cette fonction "interdite" donnaient des résultats physiques d'une exactitude stupéfiante.

C'est le mathématicien français Laurent Schwartz qui, dans les années 1940, a résolu ce paradoxe en créant la théorie des distributions. Son idée de génie fut d'opérer un renversement de perspective radical. Au lieu d'étudier une fonction de manière "absolue", c'est-à-dire en essayant de connaître sa valeur en chaque point $x$, Schwartz propose de la connaître de manière "relative", par ses interactions avec son environnement.

Pensez à un instrument de mesure physique, comme une balance ou un capteur de température. Ce capteur n'est jamais parfait ; il a une certaine inertie, une certaine fenêtre de résolution. Il ne donne pas la valeur exacte d'une grandeur en un point mathématique infiniment précis, mais plutôt une moyenne locale de cette grandeur, pondérée par la sensibilité de l'instrument.
Mathématiquement, ces "instruments de mesure parfaits" seront appelés les **fonctions tests**, des fonctions infiniment lisses et à support compact, que l'on notera $\varphi$. Un objet mathématique (une "distribution" $T$) sera alors entièrement défini, non pas par ses valeurs ponctuelles $T(x)$, mais par la collection de toutes les mesures que l'on peut faire avec tous les capteurs possibles, c'est-à-dire par le résultat de l'interaction (qui s'écrira comme une intégrale généralisée $\langle T, \varphi \rangle$) entre $T$ et chaque fonction test $\varphi$.

Cette approche de dualité, d'une élégance conceptuelle inouïe, permet de donner un sens rigoureux non seulement à la masse de Dirac, mais à une infinité d'autres objets singuliers. Plus fondamentalement, elle permet de dériver n'importe quelle fonction continue (même si elle présente des angles vifs), et de donner un cadre unifié à la résolution des équations aux dérivées partielles linéaires.

## 2. Définitions et structures fondamentales

### 2.1 L'espace des fonctions tests $\mathcal{D}(\mathbb{R})$

Pour définir correctement une distribution en tant qu'opérateur agissant sur des fonctions, il faut d'abord choisir avec soin l'espace de ces "fonctions sondes". Nous voulons qu'elles soient aussi régulières et "gentilles" que possible, afin que les distributions puissent, en retour, être aussi singulières et "sauvages" qu'elles le souhaitent.

**Définition 1 (Espace des fonctions tests).** On note $\mathcal{D}(\mathbb{R})$ (ou $C_c^\infty(\mathbb{R})$) l'espace vectoriel des fonctions $\varphi : \mathbb{R} \to \mathbb{C}$ vérifiant les deux propriétés suivantes :
1. $\varphi$ est indéfiniment dérivable sur $\mathbb{R}$ ($\varphi \in C^\infty(\mathbb{R})$).
2. Le **support** de $\varphi$, noté $\text{supp}(\varphi)$ et défini par $\text{supp}(\varphi) = \overline{\{ x \in \mathbb{R} \mid \varphi(x) \neq 0 \}}$, est un ensemble compact (fermé et borné dans $\mathbb{R}$). On dit que $\varphi$ est à support compact.

**Remarque géométrique :** Une fonction test est une cloche lisse qui s'annule identiquement (elle vaut exactement zéro) en dehors d'un certain intervalle fermé $[a,b]$. Cela garantit que toute intégrale impliquant une fonction test se réduit à une intégrale sur un intervalle borné, évitant ainsi les problèmes de convergence à l'infini.

**Exemple concret 1 : La "fonction cloche" standard**
Pour s'assurer que l'espace $\mathcal{D}(\mathbb{R})$ n'est pas réduit à la fonction nulle (ce qui ruinerait la théorie avant même qu'elle ne commence), construisons explicitement une fonction test non triviale.
Considérons la fonction $f : \mathbb{R} \to \mathbb{R}$ définie par :
$$ f(x) = \begin{cases} \exp\left(-\frac{1}{1-x^2}\right) & \text{si } |x| < 1 \\ 0 & \text{si } |x| \ge 1 \end{cases} $$
- **Support :** Il est clair que $\text{supp}(f) = [-1, 1]$, qui est compact.
- **Régularité :** Sur $]-1, 1[$, $f$ est une composée de fonctions lisses, donc elle est $C^\infty$. Le point délicat est le raccordement en $x = \pm 1$.
Calculons la dérivée première pour $x \in ]-1, 1[$ :
$$ f'(x) = -\frac{2x}{(1-x^2)^2} \exp\left(-\frac{1}{1-x^2}\right) $$
Lorsque $x \to 1^-$, posons $t = \frac{1}{1-x^2}$. On a $t \to +\infty$. Alors $f'(x)$ se comporte comme un polynôme en $t$ multiplié par $e^{-t}$. Par croissances comparées, la limite est nulle.
Par une récurrence immédiate, on montre que pour tout entier $n$, la dérivée $n$-ième $f^{(n)}(x)$ est de la forme $P_n(x)/(1-x^2)^{2n} \exp(-1/(1-x^2))$ pour $|x| < 1$, et tend vers 0 lorsque $|x| \to 1$.
Ainsi, toutes les dérivées à gauche de 1 (et à droite de -1) sont nulles, raccordant parfaitement avec la valeur nulle à l'extérieur. $f$ est bien dans $\mathcal{D}(\mathbb{R})$.

Pour munir $\mathcal{D}(\mathbb{R})$ d'une structure topologique permettant de définir la continuité, on introduit la notion de convergence pour les suites de fonctions tests.

**Définition 2 (Convergence dans $\mathcal{D}(\mathbb{R})$).** Une suite de fonctions $(\varphi_n)_{n \in \mathbb{N}}$ de $\mathcal{D}(\mathbb{R})$ converge vers une fonction $\varphi \in \mathcal{D}(\mathbb{R})$ au sens de $\mathcal{D}$ si et seulement si :
1. **Il existe un compact commun $K \subset \mathbb{R}$** tel que pour tout entier $n$, $\text{supp}(\varphi_n) \subset K$.
2. Pour tout entier $k \in \mathbb{N}$ (incluant $k=0$ pour la fonction elle-même), la suite des dérivées $(\varphi_n^{(k)})_{n \in \mathbb{N}}$ converge **uniformément** vers la dérivée $\varphi^{(k)}$ sur le compact $K$ (et donc sur $\mathbb{R}$ entier).

### 2.2 Définition de l'espace des distributions $\mathcal{D}'(\mathbb{R})$

Nous pouvons maintenant définir rigoureusement le concept central.

**Définition 3 (Distribution).** Une distribution $T$ sur $\mathbb{R}$ est une forme linéaire **continue** sur l'espace vectoriel topologique $\mathcal{D}(\mathbb{R})$. L'ensemble de toutes les distributions est noté $\mathcal{D}'(\mathbb{R})$ (c'est le dual topologique de $\mathcal{D}(\mathbb{R})$).
Si $T \in \mathcal{D}'(\mathbb{R})$ et $\varphi \in \mathcal{D}(\mathbb{R})$, la valeur complexe que $T$ associe à $\varphi$ est notée, par analogie avec le produit scalaire, par le crochet de dualité : $\langle T, \varphi \rangle$.

La définition implique deux propriétés fondamentales que l'on doit vérifier à chaque fois que l'on manipule une distribution :
1. **Linéarité :** $\forall \varphi_1, \varphi_2 \in \mathcal{D}(\mathbb{R}), \forall \lambda, \mu \in \mathbb{C}, \quad \langle T, \lambda\varphi_1 + \mu\varphi_2 \rangle = \lambda\langle T, \varphi_1 \rangle + \mu\langle T, \varphi_2 \rangle$
2. **Continuité séquentielle :** Pour toute suite $(\varphi_n)_{n \in \mathbb{N}}$ convergeant vers $\varphi$ dans $\mathcal{D}(\mathbb{R})$, on a :
   $$ \lim_{n \to +\infty} \langle T, \varphi_n \rangle = \langle T, \varphi \rangle $$

**Théorème 1 (Critère pratique de continuité).** Une forme linéaire $T$ sur $\mathcal{D}(\mathbb{R})$ est continue (et donc est une distribution) si et seulement si, pour tout compact $K \subset \mathbb{R}$, il existe un entier $m \ge 0$ et une constante $C > 0$ tels que pour toute fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ avec $\text{supp}(\varphi) \subset K$, on ait :
$$ |\langle T, \varphi \rangle| \le C \max_{0 \le k \le m} \sup_{x \in K} |\varphi^{(k)}(x)| $$
L'entier minimal $m$ qui fonctionne pour tout compact (s'il en existe un global) est appelé l'**ordre** de la distribution.

### 2.3 Distributions régulières

Le premier test de cohérence pour toute théorie généralisant un concept existant est de vérifier qu'elle inclut bien l'ancien concept comme un cas particulier. Les "anciennes" fonctions doivent pouvoir être vues comme des distributions particulières.

**Définition 4 (Fonction localement intégrable).** On note $L^1_{\text{loc}}(\mathbb{R})$ l'espace des fonctions $f : \mathbb{R} \to \mathbb{C}$ mesurables au sens de Lebesgue et dont la restriction à tout segment compact $[a,b]$ est intégrable (i.e. $\int_a^b |f(x)|dx < +\infty$).
Les fonctions continues, les fonctions continues par morceaux, les polynômes, etc., sont toutes localement intégrables. La fonction $x \mapsto 1/x$ sur $]0,1[$ ne l'est pas (au voisinage de 0).

**Théorème 2 (Injection canonique).** Toute fonction $f \in L^1_{\text{loc}}(\mathbb{R})$ définit une distribution unique, notée $T_f$, agissant de la manière suivante pour toute $\varphi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle T_f, \varphi \rangle = \int_{-\infty}^{+\infty} f(x)\varphi(x) dx $$
Une distribution qui peut s'écrire sous cette forme est appelée **distribution régulière**.

**Exemple concret 2 : La distribution associée à une fonction constante.**
Considérons la fonction $f(x) = 1$ pour tout $x$. Elle est localement intégrable. La distribution $T_1$ correspondante est donnée par :
$\langle T_1, \varphi \rangle = \int_{\mathbb{R}} 1 \cdot \varphi(x) dx = \int_{\text{supp}(\varphi)} \varphi(x) dx$.
Vérifions le critère de continuité. Soit $K$ un compact et $\text{supp}(\varphi) \subset K$.
$|\langle T_1, \varphi \rangle| \le \int_K |\varphi(x)| dx \le \text{longueur}(K) \sup_{x \in K}|\varphi(x)|$.
Ici, on voit que l'entier $m=0$ suffit. La constante est $C = \text{longueur}(K)$. C'est donc bien une distribution d'ordre 0.

### 2.4 Distributions singulières

Une distribution singulière est une distribution qui n'est pas régulière, c'est-à-dire qui ne peut s'écrire comme l'intégrale d'une fonction localement intégrable contre une fonction test.

**Théorème 3 (La masse de Dirac est une distribution).** L'application $\delta_0 : \mathcal{D}(\mathbb{R}) \to \mathbb{C}$ définie, pour un point $a \in \mathbb{R}$, par :
$$ \langle \delta_a, \varphi \rangle = \varphi(a) $$
est une distribution singulière d'ordre 0, appelée masse de Dirac au point $a$.

**Exemple concret 3 : Masse de Dirac et combinaison linéaire.**
Soit $T = 3\delta_{-1} - 2\delta_{5}$. C'est une combinaison linéaire de deux masses de Dirac. Quelle est son action sur une fonction test $\varphi(x) = \cos(\pi x) e^{-x^2}$ (en supposant cette fonction tronquée proprement pour être à support compact, ou on étend la définition aux distributions tempérées plus tard) ?
$$ \langle T, \varphi \rangle = 3 \langle \delta_{-1}, \varphi \rangle - 2 \langle \delta_{5}, \varphi \rangle = 3\varphi(-1) - 2\varphi(5) $$
Calcul : $\varphi(-1) = \cos(-\pi)e^{-(-1)^2} = -e^{-1}$ et $\varphi(5) = \cos(5\pi)e^{-(5)^2} = -e^{-25}$.
Donc $\langle T, \varphi \rangle = -3e^{-1} + 2e^{-25}$.

## 3. Démonstrations

### Démonstration de la continuité de la masse de Dirac (Théorème 3, partie 1)

**Objectif :** Démontrer formellement que l'application définie par $\langle \delta_a, \varphi \rangle = \varphi(a)$ est bien une forme linéaire continue sur $\mathcal{D}(\mathbb{R})$.

1.  **Linéarité :** Soient $\varphi, \psi \in \mathcal{D}(\mathbb{R})$ et $\lambda, \mu \in \mathbb{C}$.
    $$ \langle \delta_a, \lambda\varphi + \mu\psi \rangle = (\lambda\varphi + \mu\psi)(a) $$
    Par définition des opérations sur les fonctions, on a :
    $$ (\lambda\varphi + \mu\psi)(a) = \lambda\varphi(a) + \mu\psi(a) = \lambda\langle \delta_a, \varphi \rangle + \mu\langle \delta_a, \psi \rangle $$
    L'application est donc une forme linéaire.

2.  **Continuité (critère séquentiel) :** Soit $(\varphi_n)_{n \in \mathbb{N}}$ une suite de fonctions tests convergeant vers $\varphi$ dans $\mathcal{D}(\mathbb{R})$. Par définition de cette convergence, il existe un compact commun et la suite $(\varphi_n)$ converge uniformément vers $\varphi$ sur ce compact (et donc ponctuellement partout).
    Donc, en particulier au point $x=a$ :
    $$ \lim_{n \to +\infty} \varphi_n(a) = \varphi(a) $$
    Ce qui se réécrit en termes de crochets de dualité :
    $$ \lim_{n \to +\infty} \langle \delta_a, \varphi_n \rangle = \langle \delta_a, \varphi \rangle $$
    La forme linéaire est donc continue.

3.  **Ordre :** Pour tout compact $K$, si $\text{supp}(\varphi) \subset K$, alors on a la majoration triviale :
    $$ |\langle \delta_a, \varphi \rangle| = |\varphi(a)| \le \sup_{x \in K} |\varphi(x)| $$
    Ceci correspond au critère du Théorème 1 avec la constante $C=1$ et l'entier $m=0$. La distribution de Dirac est donc d'ordre 0. $\blacksquare$

### Démonstration : Singularité de la masse de Dirac (Théorème 3, partie 2)

**Objectif :** Montrer par l'absurde qu'il n'existe aucune fonction localement intégrable $f \in L^1_{\text{loc}}(\mathbb{R})$ telle que pour toute $\varphi \in \mathcal{D}(\mathbb{R})$, on ait $\varphi(0) = \int_{\mathbb{R}} f(x)\varphi(x) dx$.

1.  **Hypothèse par l'absurde :** Supposons qu'une telle fonction $f$ existe. Alors pour toute $\varphi \in \mathcal{D}(\mathbb{R})$, $\langle \delta_0, \varphi \rangle = \int_{-\infty}^{+\infty} f(x)\varphi(x) dx = \varphi(0)$.

2.  **Construction d'une suite test "pathologique" :** Nous allons utiliser une suite de fonctions "plateaux" qui se rétrécissent autour de zéro tout en restant bornées par 1.
    Prenons une fonction test de base $\psi \in \mathcal{D}(\mathbb{R})$ telle que $0 \le \psi(x) \le 1$, $\psi(0) = 1$ et $\text{supp}(\psi) \subset [-1, 1]$.
    Définissons une suite de fonctions par changement d'échelle :
    $$ \varphi_n(x) = \psi(nx) $$
    Pour chaque $n \ge 1$ :
    *   $\varphi_n \in \mathcal{D}(\mathbb{R})$ car la composition avec une homothétie conserve la régularité lisse.
    *   Le support de $\varphi_n$ est inclus dans $[-1/n, 1/n]$. En effet, si $x \notin [-1/n, 1/n]$, alors $|nx| > 1$, donc $\psi(nx) = 0$.
    *   $\varphi_n(0) = \psi(0) = 1$.
    *   $0 \le \varphi_n(x) \le 1$ pour tout $x \in \mathbb{R}$.

3.  **Évaluation de l'égalité sous l'hypothèse :** Puisque $\varphi_n(0) = 1$, notre hypothèse implique que pour tout $n \ge 1$ :
    $$ 1 = \int_{-\infty}^{+\infty} f(x)\varphi_n(x) dx = \int_{-1/n}^{1/n} f(x)\varphi_n(x) dx $$
    La deuxième égalité vient du fait que $\varphi_n$ est nulle en dehors de $[-1/n, 1/n]$.

4.  **Majoration :** On peut majorer la valeur absolue de l'intégrale :
    $$ 1 = \left| \int_{-1/n}^{1/n} f(x)\varphi_n(x) dx \right| \le \int_{-1/n}^{1/n} |f(x)||\varphi_n(x)| dx $$
    Comme $|\varphi_n(x)| \le 1$ partout, on obtient la majoration stricte :
    $$ 1 \le \int_{-1/n}^{1/n} |f(x)| dx $$

5.  **Utilisation de l'intégrabilité locale et conclusion :**
    La fonction $f$ est supposée appartenir à $L^1_{\text{loc}}(\mathbb{R})$. Donc la fonction $x \mapsto |f(x)|$ est intégrable sur le voisinage de l'origine $[-1, 1]$.
    Posons la fonction indicatrice $\mathbf{1}_{[-1/n, 1/n]}(x)$. Pour tout $x \neq 0$, cette indicatrice tend vers 0 quand $n \to +\infty$. De plus, on a la domination ponctuelle :
    $|f(x)| \mathbf{1}_{[-1/n, 1/n]}(x) \le |f(x)| \mathbf{1}_{[-1, 1]}(x)$, et le membre de droite est intégrable.
    Par le théorème de convergence dominée de Lebesgue, on peut passer à la limite dans l'intégrale :
    $$ \lim_{n \to +\infty} \int_{-1/n}^{1/n} |f(x)| dx = \int_{\mathbb{R}} \lim_{n \to +\infty} \left( |f(x)| \mathbf{1}_{[-1/n, 1/n]}(x) \right) dx = \int_{\mathbb{R}} 0 \, dx = 0 $$
    (On rappelle qu'un point isolé, $\{0\}$, a une mesure de Lebesgue nulle, donc ce qui se passe en $x=0$ ne change pas l'intégrale).
    Nous aboutissons donc à la contradiction évidente :
    $$ 1 \le \lim_{n \to +\infty} \int_{-1/n}^{1/n} |f(x)| dx = 0 \implies 1 \le 0 $$
    L'hypothèse de départ est fausse. La distribution $\delta_0$ ne peut pas s'écrire comme l'intégrale d'une fonction $L^1_{\text{loc}}$. $\blacksquare$

## 4. Applications en Physique, Logique & Intelligence Artificielle

L'introduction du formalisme des distributions n'a pas seulement pacifié les mathématiciens scrupuleux, elle a fourni un outil d'une puissance redoutable pour modéliser des phénomènes extrêmes et discrétisés dans un monde continu.

**En Physique classique et quantique :**
En mécanique classique, un choc est un échange de quantité de mouvement sur un temps infiniment court. Si l'on essaie de modéliser la force (qui est la dérivée de la quantité de mouvement), on obtient une entité infinie pendant un instant de durée nulle. C'est exactement un multiple de la masse de Dirac. De même en électrostatique, la densité volumique de charge associée à un électron ponctuel n'est pas une fonction, c'est une distribution proportionnelle à un Dirac tridimensionnel $\delta(\mathbf{r} - \mathbf{r}_0)$. L'équation de Poisson $\Delta V = -\frac{\rho}{\varepsilon_0}$ ne prend tout son sens mathématique que si l'on admet que $\rho$ peut être une distribution. Les solutions fondamentales (ou fonctions de Green) de ces équations sont précisément les champs créés par ces sources ponctuelles de type Dirac.

**En Théorie du Signal et Probabilités :**
La transformée de Fourier, qui nécessitait historiquement des fonctions qui décroissent à l'infini (fonctions $L^1$ ou $L^2$), s'étend naturellement aux distributions tempérées. Cela permet de donner un sens rigoureux à la "densité spectrale" d'un signal périodique (qui devient une somme de Diracs dans le domaine fréquentiel). En probabilités, la loi d'une variable aléatoire discrète n'a pas de densité de probabilité au sens classique, mais sa distribution empirique s'écrit parfaitement comme une somme pondérée de masses de Dirac, unifiant ainsi le traitement formel des variables continues et discrètes sous le chapeau unique de l'intégration par rapport à des mesures de Radon (qui sont des distributions d'ordre 0 particulières).

**En Intelligence Artificielle et Machine Learning :**
Le formalisme variationnel des distributions est au cœur de la conception moderne des algorithmes d'apprentissage profond.
1.  **Fonction de perte sur des échantillons empiriques :** Lors de l'entraînement d'un réseau de neurones, on cherche à minimiser l'espérance d'une perte (Loss) sur la vraie distribution des données $p_{data}(\mathbf{x})$. Comme on ne possède qu'un ensemble fini d'échantillons $\{\mathbf{x}_1, \dots, \mathbf{x}_N\}$, on remplace $p_{data}$ par la distribution empirique $\hat{p}(\mathbf{x}) = \frac{1}{N}\sum_{i=1}^N \delta(\mathbf{x} - \mathbf{x}_i)$. L'intégrale de perte $\int L(\mathbf{x}, \theta) p_{data}(\mathbf{x}) d\mathbf{x}$ devient alors formellement $\langle \hat{p}, L(\cdot, \theta) \rangle = \frac{1}{N}\sum L(\mathbf{x}_i, \theta)$. Le cadre des distributions valide rigoureusement cette manipulation.
2.  **Réseaux de neurones à impulsions (Spiking Neural Networks - SNN) :** Inspirés du cerveau humain, ces réseaux communiquent via des "spikes" ou potentiels d'action, qui sont des impulsions brèves modélisables par des trains de Dirac temporels $S(t) = \sum_k \delta(t - t_k)$. Le traitement mathématique de ces réseaux, notamment pour adapter l'algorithme de rétropropagation du gradient (qui exige de dériver le signal), repose sur des approximations de la masse de Dirac (surrogate gradients) fondées sur la théorie des distributions.
