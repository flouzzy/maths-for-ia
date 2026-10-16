---
uuid: "jalon-91"
title: "Inégalités de concentration"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/theorie
prev: "[[Jalon 90 (Les modes de convergence).md]]"
next: "[[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]]"
---

# Jalon 91 : Inégalités de concentration

## 1. Introduction aux inégalités de concentration

Dans de nombreux domaines allant de la physique statistique à l'informatique théorique, il est fréquent de manipuler des systèmes complexes composés d'un très grand nombre de variables aléatoires (comme les particules d'un gaz, ou les échantillons de données en apprentissage automatique). La connaissance exacte de la distribution de probabilité globale de tels systèmes est généralement inaccessible. Néanmoins, on dispose souvent d'informations globales simples telles que l'espérance mathématique ou la variance.

C'est dans ce contexte que naissent les inégalités de concentration, dont les premiers jalons ont été posés par Andrey Markov et Pafnuty Chebyshev au XIXe siècle, avant d'être profondément développées par Herman Chernoff et Wassily Hoeffding au milieu du XXe siècle. Leur objet fondamental est de fournir des garanties mathématiques quantitatives sur la probabilité qu'une variable aléatoire s'écarte significativement de son espérance. En d'autres termes, ces inégalités expliquent comment, et à quelle vitesse, la mesure de probabilité "se concentre" autour de la moyenne.

L'intuition physique sous-jacente est simple : plus l'écart à la moyenne exigé est grand, plus la configuration du système qui produirait cet écart devient rare et contrainte, faisant s'effondrer sa probabilité de réalisation. La force de ces outils est d'être totalement agnostiques quant à la loi exacte sous-jacente, reposant uniquement sur quelques moments ou bornes de la variable aléatoire.

## 2. Définitions, Théorèmes & Exemples

### A. L'Inégalité de Markov

L'inégalité de Markov est la fondation sur laquelle reposent presque toutes les autres inégalités de concentration. Elle donne une majoration de la queue de distribution d'une variable positive en ne connaissant que son espérance.

**Théorème (Inégalité de Markov) :**
Soit $X$ une variable aléatoire réelle définie sur un espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$, telle que $X \ge 0$ presque sûrement. On suppose que son espérance $\mathbb{E}[X]$ est finie. Alors, pour tout réel $a > 0$ :
$$ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} $$

**Exemple concret 1 :**
Supposons que la durée de vie moyenne $T$ d'un composant électronique d'un cluster GPU soit de $\mathbb{E}[T] = 50 000$ heures. Sans connaître la loi exacte de $T$ (qui pourrait être exponentielle, de Weibull, etc.), on cherche à évaluer la probabilité que le composant fonctionne plus de $150 000$ heures.
Ici, $T \ge 0$. On applique l'inégalité de Markov avec $a = 150 000$ :
$$ \mathbb{P}(T \ge 150 000) \le \frac{50 000}{150 000} = \frac{1}{3} $$
La probabilité est donc inférieure ou égale à $33.33\%$.

### B. L'Inégalité de Bienaymé-Tchebychev

En exploitant l'ordre 2 (la variance), l'inégalité de Tchebychev permet d'obtenir une concentration beaucoup plus fine que celle de Markov, mesurant l'écart bilatéral autour de la moyenne.

**Théorème (Inégalité de Bienaymé-Tchebychev) :**
Soit $X$ une variable aléatoire réelle de carré intégrable, d'espérance $\mu = \mathbb{E}[X]$ et de variance $\sigma^2 = \text{Var}(X)$. Alors, pour tout réel $a > 0$ :
$$ \mathbb{P}(|X - \mu| \ge a) \le \frac{\sigma^2}{a^2} $$
Souvent, on pose $a = k\sigma$ avec $k > 0$, ce qui réécrit l'inégalité sous la forme :
$$ \mathbb{P}(|X - \mu| \ge k\sigma) \le \frac{1}{k^2} $$

**Exemple concret 2 :**
Un algorithme de routage réseau traite en moyenne $\mu = 10 000$ paquets par seconde, avec un écart-type $\sigma = 500$ paquets (soit une variance $\sigma^2 = 250 000$). Quelle est la probabilité que la charge réseau s'écarte de sa moyenne d'au moins $2 000$ paquets en un instant donné ?
On pose $a = 2 000$. D'après Bienaymé-Tchebychev :
$$ \mathbb{P}(|X - 10 000| \ge 2 000) \le \frac{250 000}{(2 000)^2} = \frac{250 000}{4 000 000} = \frac{1}{16} = 0.0625 $$
Ainsi, l'écart à la moyenne dépasse les $2 000$ paquets dans au plus $6.25\%$ des cas.

### C. La borne de Chernoff

Pour obtenir une décroissance exponentielle des probabilités des grandes déviations, il est nécessaire de faire appel à la fonction génératrice des moments (si elle existe). C'est le principe de la borne de Chernoff.

**Définition et Théorème (Borne de Chernoff) :**
Soit $X$ une variable aléatoire réelle telle que la fonction génératrice des moments $M_X(t) = \mathbb{E}[e^{tX}]$ est finie pour $t$ dans un voisinage de $0$. Pour tout réel $a$, en appliquant l'inégalité de Markov à $e^{tX}$ pour $t > 0$, on obtient la borne de Chernoff :
$$ \mathbb{P}(X \ge a) = \mathbb{P}(e^{tX} \ge e^{ta}) \le \frac{\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t) $$
Puisque cette majoration est vraie pour tout $t > 0$, on l'optimise sur $t$ :
$$ \mathbb{P}(X \ge a) \le \inf_{t > 0} e^{-ta} \mathbb{E}[e^{tX}] $$

**Exemple concret 3 :**
Soit $X \sim \mathcal{N}(\mu, \sigma^2)$. Sa fonction génératrice des moments est $M_X(t) = \exp(\mu t + \frac{1}{2}\sigma^2 t^2)$.
Majorons $\mathbb{P}(X \ge a)$ pour $a > \mu$. Pour $t > 0$ :
$$ \mathbb{P}(X \ge a) \le \exp(-ta + \mu t + \frac{1}{2}\sigma^2 t^2) $$
L'argument de l'exponentielle est une fonction dérivable en $t$ : $f(t) = \frac{1}{2}\sigma^2 t^2 - (a - \mu)t$.
Sa dérivée s'annule en $t^* = \frac{a - \mu}{\sigma^2}$. On vérifie que $t^* > 0$ puisque $a > \mu$.
En injectant $t^*$, on trouve :
$$ f(t^*) = \frac{1}{2}\sigma^2 \frac{(a - \mu)^2}{\sigma^4} - \frac{(a - \mu)^2}{\sigma^2} = -\frac{(a - \mu)^2}{2\sigma^2} $$
On en déduit la borne de queue gaussienne :
$$ \mathbb{P}(X \ge a) \le \exp\left( - \frac{(a - \mu)^2}{2\sigma^2} \right) $$
C'est une décroissance exponentielle, bien plus forte que la décroissance polynômiale en $1/a^2$ de Tchebychev.

### D. Le Lemme et l'Inégalité de Hoeffding

L'inégalité de Hoeffding spécifie la borne de Chernoff pour des sommes de variables aléatoires indépendantes et bornées. C'est l'outil roi en théorie de l'apprentissage statistique.

**Lemme de Hoeffding :**
Soit $X$ une variable aléatoire réelle d'espérance nulle ($\mathbb{E}[X] = 0$), bornée presque sûrement dans l'intervalle $[a, b]$. Alors pour tout $t \in \mathbb{R}$ :
$$ \mathbb{E}[e^{tX}] \le \exp\left( \frac{t^2 (b - a)^2}{8} \right) $$

**Théorème (Inégalité de Hoeffding) :**
Soit $X_1, \dots, X_n$ des variables aléatoires indépendantes telles que pour tout $i$, $X_i \in [a_i, b_i]$ presque sûrement. Soit $S_n = \sum_{i=1}^n X_i$. Alors pour tout $u > 0$ :
$$ \mathbb{P}(S_n - \mathbb{E}[S_n] \ge u) \le \exp\left( - \frac{2u^2}{\sum_{i=1}^n (b_i - a_i)^2} \right) $$
Et de manière symétrique pour l'écart absolu :
$$ \mathbb{P}(|S_n - \mathbb{E}[S_n]| \ge u) \le 2\exp\left( - \frac{2u^2}{\sum_{i=1}^n (b_i - a_i)^2} \right) $$

**Exemple concret 4 :**
Considérons $n = 100$ lancers indépendants d'une pièce déséquilibrée avec une probabilité $p$ de faire Pile (où l'on note $1$ pour Pile, $0$ pour Face). On a des variables de Bernoulli $X_i \in [0, 1]$. Posons $\overline{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$. L'espérance empirique est $\mathbb{E}[\overline{X}_n] = p$.
On veut estimer le risque que la moyenne empirique diffère de plus de $0.1$ de la vraie valeur $p$.
On pose $u = n \times 0.1 = 10$ pour la somme $S_n$. L'inégalité de Hoeffding donne :
$$ \mathbb{P}(|\overline{X}_n - p| \ge 0.1) = \mathbb{P}(|S_n - np| \ge 10) \le 2\exp\left( - \frac{2(10)^2}{100 \times (1 - 0)^2} \right) $$
$$ \mathbb{P}(|\overline{X}_n - p| \ge 0.1) \le 2\exp\left( - \frac{200}{100} \right) = 2e^{-2} \approx 2 \times 0.135 = 0.270 $$
La probabilité de s'écarter de $10\%$ est bornée par environ $27\%$. Si l'on augmente $n = 10 000$, la borne devient $2\exp(-200)$, ce qui est quasi nul.

## 3. Démonstrations

### A. Preuve de l'inégalité de Markov

Soit $X \ge 0$ presque sûrement. Soit $a > 0$. On introduit la fonction indicatrice $\mathbf{1}_{X \ge a}$.
Il est trivial de vérifier l'inégalité point par point sur $\Omega$ :
$$ X(\omega) \ge a \cdot \mathbf{1}_{X \ge a}(\omega) $$
En effet :
- Si $X(\omega) < a$, l'indicatrice vaut $0$, et $X(\omega) \ge 0$ est vrai.
- Si $X(\omega) \ge a$, l'indicatrice vaut $1$, et $X(\omega) \ge a$ est vrai par hypothèse.

L'opérateur espérance $\mathbb{E}[\cdot]$ préserve l'ordre (linéarité et positivité de l'intégrale). Par passage à l'espérance de chaque côté :
$$ \mathbb{E}[X] \ge \mathbb{E}[a \cdot \mathbf{1}_{X \ge a}] $$
Puisque $a$ est une constante, par linéarité :
$$ \mathbb{E}[X] \ge a \mathbb{E}[\mathbf{1}_{X \ge a}] $$
Or, l'espérance d'une variable indicatrice de l'événement $A$ est précisément la probabilité de l'événement $A$. Donc :
$$ \mathbb{E}[X] \ge a \mathbb{P}(X \ge a) $$
En divisant par $a > 0$, on obtient le résultat :
$$ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a} $$

### B. Preuve de l'inégalité de Bienaymé-Tchebychev

Posons la variable aléatoire $Y = (X - \mu)^2$. Puisque c'est un carré, $Y \ge 0$ presque sûrement.
On cherche à borner l'événement $\{|X - \mu| \ge a\}$. Or, cet événement est strictement équivalent à $\{ (X - \mu)^2 \ge a^2 \}$, car la fonction $x \mapsto x^2$ est strictement croissante sur $\mathbb{R}^+$.
Donc, on veut borner $\mathbb{P}(Y \ge a^2)$.
Puisque $Y \ge 0$, on applique directement l'inégalité de Markov à $Y$ pour la valeur $a^2$ :
$$ \mathbb{P}(Y \ge a^2) \le \frac{\mathbb{E}[Y]}{a^2} $$
En remplaçant $Y$ par sa définition :
$$ \mathbb{P}(|X - \mu| \ge a) \le \frac{\mathbb{E}[(X - \mu)^2]}{a^2} $$
Par définition de la variance, $\mathbb{E}[(X - \mu)^2] = \sigma^2$. On conclut :
$$ \mathbb{P}(|X - \mu| \ge a) \le \frac{\sigma^2}{a^2} $$

### C. Preuve du Lemme de Hoeffding

Soit $X$ une variable avec $\mathbb{E}[X] = 0$ et $X \in [a, b]$ presque sûrement.
Pour un $t$ fixé, par convexité de la fonction exponentielle sur l'intervalle $[a, b]$, on peut majorer $e^{tx}$ par la corde reliant les points $(a, e^{ta})$ et $(b, e^{tb})$.
Puisque $x \in [a, b]$, on peut écrire $x$ comme un barycentre :
$$ x = \alpha a + (1 - \alpha)b \quad \text{avec} \quad \alpha = \frac{b - x}{b - a} $$
Par l'inégalité de convexité pour la fonction $f(x) = e^{tx}$ :
$$ e^{tx} \le \alpha e^{ta} + (1 - \alpha)e^{tb} = \frac{b - x}{b - a} e^{ta} + \frac{x - a}{b - a} e^{tb} $$
On applique l'espérance $\mathbb{E}[\cdot]$ à cette inégalité. Puisque l'opérateur $\mathbb{E}$ est linéaire et que $\mathbb{E}[X] = 0$, les termes en $X$ disparaissent :
$$ \mathbb{E}[e^{tX}] \le \frac{b}{b - a} e^{ta} - \frac{a}{b - a} e^{tb} $$
Posons $\theta = -\frac{a}{b - a}$ et $u = t(b - a)$. Remarquons que $ta = -u\theta$ et $tb = u(1 - \theta)$. L'inégalité devient :
$$ \mathbb{E}[e^{tX}] \le (1 - \theta)e^{-u\theta} + \theta e^{u(1 - \theta)} = e^{-u\theta} (1 - \theta + \theta e^u) = \exp(-u\theta + \ln(1 - \theta + \theta e^u)) $$
Considérons la fonction $g(u) = -u\theta + \ln(1 - \theta + \theta e^u)$.
En étudiant les dérivées de $g$, on montre que $g(0) = g'(0) = 0$, et que la dérivée seconde vérifie $g''(u) \le \frac{1}{4}$ pour tout $u$.
Par la formule de Taylor-Lagrange autour de $u = 0$, il existe un $\xi \in (0, u)$ tel que :
$$ g(u) = g(0) + u g'(0) + \frac{u^2}{2} g''(\xi) \le 0 + 0 + \frac{u^2}{2} \cdot \frac{1}{4} = \frac{u^2}{8} $$
En remplaçant $u = t(b - a)$, on obtient bien :
$$ \mathbb{E}[e^{tX}] \le \exp\left( \frac{t^2 (b - a)^2}{8} \right) $$

## 4. Applications en Physique, Logique et Intelligence Artificielle

### A. Apprentissage Statistique et la borne PAC (Probably Approximately Correct)
En machine learning, le paradigme PAC cherche à borner la différence entre l'erreur empirique (le risque sur l'ensemble d'entraînement) $R_{emp}(h)$ et l'erreur de généralisation $R(h)$ d'un classifieur $h$. Par l'inégalité de Hoeffding sur $N$ données indépendantes, on démontre que la probabilité d'avoir $|R(h) - R_{emp}(h)| \ge \epsilon$ décroît comme $2e^{-2N\epsilon^2}$. C'est la fondation théorique de la complexité de Vapnik-Chervonenkis (VC) et des bornes de Rademacher qui garantissent qu'un algorithme d'IA généralise bien.

### B. Mécanique Statistique et Thermodynamique
Dans un gaz parfait, l'énergie cinétique totale est la somme des énergies cinétiques de $10^{23}$ molécules indépendantes. La borne de Chernoff assure que la probabilité que l'énergie totale fluctue macroscopiquement autour de sa valeur moyenne est exponentiellement supprimée par un facteur d'ordre $e^{-N}$. C'est ce qui légitime mathématiquement l'équivalence entre l'ensemble microcanonique (énergie fixée) et l'ensemble canonique (énergie fluctuante mais moyenne fixée) dans la limite thermodynamique.

### C. Algorithmes randomisés et cryptographie
En informatique quantique et en algorithmique randomisée (comme le test de primalité de Miller-Rabin), les algorithmes ont une probabilité d'erreur intrinsèque. L'inégalité de Chernoff prouve que si on exécute l'algorithme un nombre $k$ de fois indépendantes et qu'on prend le vote majoritaire, la probabilité que la majorité se trompe décroît exponentiellement avec $k$. Cela rend ces algorithmes probabilistes pratiquement infaillibles (probabilité d'erreur inférieure à la probabilité de dysfonctionnement du matériel) au bout de très peu de répétitions.
