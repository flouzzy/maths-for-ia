Mes chers étudiants,

Bienvenue à cette séance avancée d'analyse mathématique. Aujourd'hui, nous allons nous pencher sur un résultat fondamental en théorie de l'apprentissage statistique et en processus empiriques : une version généralisée du Théorème de Glivenko-Cantelli pour les classes de fonctions de Vapnik-Chervonenkis (VC). Ce jalon, le 141ème de notre parcours, exige une compréhension solide des concepts de probabilité, de théorie de la mesure, des inégalités de concentration et, bien sûr, de la théorie VC.

Le théorème classique de Glivenko-Cantelli, que vous connaissez bien, affirme la convergence uniforme presque sûre de la fonction de répartition empirique vers la vraie fonction de répartition. Sa généralisation est cruciale car elle permet d'étendre cette convergence uniforme à des classes de fonctions bien plus riches, caractérisées par leur "complexité" mesurée par la dimension VC. C'est un pilier pour comprendre la généralisation des algorithmes d'apprentissage.

L'exercice que je vous propose est de difficulté 8/10. Il requiert non seulement l'application de théorèmes clés mais aussi une compréhension profonde de leurs interconnexions. Préparez-vous à une démonstration rigoureuse, sans la moindre ellipse mathématique.

---

## Jalon 141 - Exercice 8/10 : Théorèmes de Glivenko-Cantelli Généralisés pour les Classes de Fonctions VC

### Énoncé Rigoureux et Formel

Soit $(\Omega, \mathcal{A}_{\Omega}, \mathbb{P})$ un espace de probabilité.
Soit $(\mathcal{X}, \mathcal{B})$ un espace mesurable, où $\mathcal{X}$ est un ensemble non vide et $\mathcal{B}$ est une $\sigma$-algèbre sur $\mathcal{X}$.
Soit $P$ une mesure de probabilité sur $(\mathcal{X}, \mathcal{B})$.
Soient $X_1, X_2, \dots, X_n$ des variables aléatoires indépendantes et identiquement distribuées (i.i.d.) selon $P$, définies sur $(\Omega, \mathcal{A}_{\Omega}, \mathbb{P})$ et à valeurs dans $(\mathcal{X}, \mathcal{B})$.

Nous définissons la mesure empirique $P_n$ pour tout $B \in \mathcal{B}$ par :
$$ P_n(B) := \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{B}(X_i) $$
où $\mathbf{1}_{B}$ est la fonction indicatrice de l'ensemble $B$.

Soit $\mathcal{C}$ une classe de sous-ensembles mesurables de $\mathcal{X}$, c'est-à-dire $\mathcal{C} \subseteq \mathcal{B}$.
Nous supposons que $\mathcal{C}$ est une **classe VC de dimension $d$ finie**. Cela signifie qu'il existe un entier $d \in \mathbb{N}$ tel que $\mathcal{C}$ peut "briser" (shatter) un ensemble de $d$ points, mais ne peut pas briser un ensemble de $d+1$ points.

L'objectif de cet exercice est de démontrer la convergence en probabilité uniforme suivante :
$$ \sup_{C \in \mathcal{C}} |P_n(C) - P(C)| \xrightarrow{\mathbb{P}} 0 \quad \text{lorsque } n \to \infty $$

**Guidance pour la démonstration (étapes suggérées) :**

1.  **Symmetrisation :** Utiliser une technique de symétrisation impliquant des variables de Rademacher pour relier la quantité $\mathbb{P}\left(\sup_{C \in \mathcal{C}} |P_n(C) - P(C)| > \delta\right)$ à une quantité impliquant des sommes de Rademacher.
2.  **Conditionnement et Bornes de Concentration :** Conditionner sur les observations $X_1, \dots, X_n$ et appliquer une inégalité de concentration appropriée (par exemple, l'inégalité de Hoeffding) pour borner la probabilité conditionnelle.
3.  **Lemme de Sauer :** Utiliser le Lemme de Sauer pour borner le nombre de "motifs" (patterns) que la classe $\mathcal{C}$ peut induire sur un ensemble fini de $n$ points.
4.  **Borne Finale et Convergence :** Combiner les résultats précédents à l'aide d'une borne d'union (union bound) pour obtenir une borne explicite sur la probabilité de déviation uniforme, puis montrer que cette borne tend vers zéro lorsque $n \to \infty$.

---

### Analyse Détaillée

Cet exercice nous demande de prouver une forme de convergence uniforme pour la mesure empirique sur une classe de sets VC. C'est un résultat fondamental qui sous-tend de nombreux aspects de la théorie de l'apprentissage statistique, notamment les bornes de généralisation pour les classifieurs binaires.

La difficulté réside dans la gestion du supremum sur une classe infinie (potentiellement) de fonctions. Les techniques classiques pour des fonctions individuelles (comme la Loi des Grands Nombres) ne suffisent plus. Nous devons contrôler la "complexité" de la classe $\mathcal{C}$.

Voici la stratégie détaillée :

1.  **Le Problème du Supremum :** La quantité $\sup_{C \in \mathcal{C}} |P_n(C) - P(C)|$ est une variable aléatoire. Nous voulons montrer qu'elle converge en probabilité vers 0. Cela signifie que pour tout $\delta > 0$, $\mathbb{P}\left(\sup_{C \in \mathcal{C}} |P_n(C) - P(C)| > \delta\right) \to 0$ lorsque $n \to \infty$.

2.  **Symmetrisation (Étape 1) :**
    *   L'expression $P(C)$ est une espérance $\mathbb{E}[\mathbf{1}_C(X)]$. Il est souvent difficile de travailler avec des différences entre une moyenne empirique et une espérance.
    *   La technique de symétrisation remplace $P(C)$ par une autre moyenne empirique, $P_n'(C)$, calculée sur un "échantillon fantôme" $X_1', \dots, X_n'$ i.i.d. de $P$.
    *   Plus précisément, on utilise des variables de Rademacher $\epsilon_i$ (prenant les valeurs $+1$ ou $-1$ avec probabilité $1/2$) pour relier la déviation originale à une "complexité de Rademacher" de la classe. L'inégalité clé est :
        $$ \mathbb{P}\left(\sup_{C \in \mathcal{C}} |P_n(C) - P(C)| > \delta\right) \le 2 \mathbb{P}\left(\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| > \frac{\delta}{2}\right) $$
        Cette inégalité est fondamentale et évite de manipuler directement $P(C)$.

3.  **Conditionnement et Concentration (Étape 2) :**
    *   Après symétrisation, la probabilité dépend des variables $X_i$ et des variables de Rademacher $\epsilon_i$.
    *   Nous allons conditionner sur les observations $X_1, \dots, X_n$. Pour un ensemble fixe de $X_i$, la quantité $\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)$ est une somme de variables aléatoires de Rademacher pondérées.
    *   L'inégalité de Hoeffding est l'outil parfait pour borner la probabilité de déviation d'une telle somme. Pour une somme $\sum_{i=1}^n \epsilon_i a_i$ où $a_i \in [0,1]$, on a $\mathbb{P}\left(\left|\sum_{i=1}^n \epsilon_i a_i\right| > t\right) \le 2 \exp\left(-\frac{t^2}{2 \sum_{i=1}^n a_i^2}\right)$. Dans notre cas, $a_i = \mathbf{1}_C(X_i)$, donc $a_i \in \{0,1\}$, ce qui simplifie $\sum a_i^2 \le n$.

4.  **Lemme de Sauer (Étape 3) :**
    *   Le problème est que le supremum est pris sur une classe $\mathcal{C}$ potentiellement infinie. Cependant, pour un ensemble *fixe* de $n$ points $X_1, \dots, X_n$, la classe $\mathcal{C}$ ne peut induire qu'un nombre fini de "motifs" ou de "dichotomies" distincts.
    *   Soit $\mathcal{C}_{\mathbf{X}} = \{ (\mathbf{1}_C(X_1), \dots, \mathbf{1}_C(X_n)) : C \in \mathcal{C} \}$ l'ensemble des vecteurs binaires induits par $\mathcal{C}$ sur les points $X_1, \dots, X_n$.
    *   Le Lemme de Sauer (ou Sauer-Shelah) borne la taille de cet ensemble : $|\mathcal{C}_{\mathbf{X}}| \le \sum_{k=0}^d \binom{n}{k}$, où $d$ est la dimension VC de $\mathcal{C}$. Cette somme est souvent notée $\Phi_d(n)$.
    *   Une borne utile pour $\Phi_d(n)$ est $\Phi_d(n) \le (n+1)^d$ ou, plus précisément, $\Phi_d(n) \le (ne/d)^d$ pour $n \ge d$.

5.  **Borne Finale et Convergence (Étape 4) :**
    *   En utilisant le Lemme de Sauer, nous pouvons remplacer le supremum sur $\mathcal{C}$ par un maximum sur l'ensemble fini $\mathcal{C}_{\mathbf{X}}$.
    *   Ensuite, nous appliquons une borne d'union (union bound) : $\mathbb{P}(\max_j A_j) \le \sum_j \mathbb{P}(A_j)$.
    *   Chaque terme de la somme sera borné par l'inégalité de Hoeffding.
    *   Le résultat final sera une borne qui dépend de $n$, $d$, et $\delta$. Il faudra montrer que cette borne tend vers 0 lorsque $n \to \infty$. L'exponentielle dans l'inégalité de Hoeffding dominera le terme polynomial issu du Lemme de Sauer.

La démonstration est un exemple classique de la façon dont la complexité combinatoire (dimension VC) est utilisée pour contrôler la convergence stochastique dans des espaces fonctionnels.

---

### Correction Pas-à-Pas (Zéro Ellipse Mathématique)

Soit $\delta \in \mathbb{R}_{>0}$ arbitrairement fixé. Nous voulons montrer que $\lim_{n \to \infty} \mathbb{P}\left(\sup_{C \in \mathcal{C}} |P_n(C) - P(C)| > \delta\right) = 0$.

#### Étape 1 : Symmetrisation

Nous introduisons un échantillon "fantôme" $X_1', \dots, X_n'$ de variables aléatoires i.i.d. selon $P$, indépendantes de $X_1, \dots, X_n$.
Nous définissons la mesure empirique fantôme $P_n'(C) := \frac{1}{n} \sum_{i=1}^n \mathbf{1}_C(X_i')$.

Pour tout $C \in \mathcal{C}$, nous avons $\mathbb{E}[\mathbf{1}_C(X_i')] = P(C)$.
Ainsi, $P(C) = \mathbb{E}[P_n'(C) | X_1, \dots, X_n]$.
Nous pouvons écrire :
$$ P_n(C) - P(C) = P_n(C) - \mathbb{E}[P_n'(C) | X_1, \dots, X_n] = \mathbb{E}[P_n(C) - P_n'(C) | X_1, \dots, X_n] $$
Ceci n'est pas directement utile pour la borne de probabilité. Nous utilisons plutôt le lemme de symétrisation standard.

**Lemme de Symmetrisation :** Pour toute classe de fonctions $\mathcal{F}$ et pour tout $\delta > 0$,
$$ \mathbb{P}\left(\sup_{f \in \mathcal{F}} \left|\frac{1}{n} \sum_{i=1}^n (f(X_i) - \mathbb{E}[f(X)])\right| > \delta\right) \le 2 \mathbb{P}\left(\sup_{f \in \mathcal{F}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i f(X_i)\right| > \frac{\delta}{2}\right) $$
où $\epsilon_1, \dots, \epsilon_n$ sont des variables de Rademacher i.i.d. (c'est-à-dire $\mathbb{P}(\epsilon_i = 1) = \mathbb{P}(\epsilon_i = -1) = 1/2$), indépendantes des $X_i$.

Dans notre cas, la classe de fonctions est $\mathcal{F} = \{ \mathbf{1}_C : C \in \mathcal{C} \}$.
En appliquant ce lemme, nous obtenons :
$$ \mathbb{P}\left(\sup_{C \in \mathcal{C}} |P_n(C) - P(C)| > \delta\right) \le 2 \mathbb{P}\left(\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| > \frac{\delta}{2}\right) \quad (*)$$

#### Étape 2 : Conditionnement et Bornes de Concentration

Soit $\mathbf{X} = (X_1, \dots, X_n)$ la séquence des $n$ observations. Nous allons conditionner sur $\mathbf{X}$.
La probabilité du membre de droite de $(*)$ peut s'écrire comme $\mathbb{E}_{\mathbf{X}}\left[\mathbb{P}_{\epsilon}\left(\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| > \frac{\delta}{2} \Big| \mathbf{X}\right)\right]$.

Pour un $\mathbf{X}$ fixé, considérons la quantité $\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right|$.
Soit $\mathcal{C}_{\mathbf{X}}$ l'ensemble des vecteurs binaires induits par $\mathcal{C}$ sur les points $X_1, \dots, X_n$ :
$$ \mathcal{C}_{\mathbf{X}} := \left\{ (\mathbf{1}_C(X_1), \dots, \mathbf{1}_C(X_n)) \in \{0,1\}^n : C \in \mathcal{C} \right\} $$
Le supremum sur $C \in \mathcal{C}$ peut être remplacé par un maximum sur les vecteurs $v \in \mathcal{C}_{\mathbf{X}}$ :
$$ \sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| = \max_{v \in \mathcal{C}_{\mathbf{X}}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i v_i\right| $$
Nous utilisons l'inégalité d'union (union bound) :
$$ \mathbb{P}_{\epsilon}\left(\max_{v \in \mathcal{C}_{\mathbf{X}}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i v_i\right| > \frac{\delta}{2} \Big| \mathbf{X}\right) \le \sum_{v \in \mathcal{C}_{\mathbf{X}}} \mathbb{P}_{\epsilon}\left(\left|\frac{1}{n} \sum_{i=1}^n \epsilon_i v_i\right| > \frac{\delta}{2} \Big| \mathbf{X}\right) $$
Pour chaque $v = (v_1, \dots, v_n) \in \mathcal{C}_{\mathbf{X}}$, la somme $\sum_{i=1}^n \epsilon_i v_i$ est une somme de variables aléatoires indépendantes $\epsilon_i v_i$. Puisque $v_i \in \{0,1\}$, chaque terme $\epsilon_i v_i$ est soit $0$ (si $v_i=0$) soit $\epsilon_i \in \{-1,1\}$ (si $v_i=1$). Ainsi, chaque terme $\epsilon_i v_i$ est borné en valeur absolue par $1$.
Nous appliquons l'**Inégalité de Hoeffding** pour les sommes de variables de Rademacher pondérées :
Pour des constantes $a_1, \dots, a_n \in \mathbb{R}$ et des variables de Rademacher $\epsilon_1, \dots, \epsilon_n$,
$$ \mathbb{P}\left(\left|\sum_{i=1}^n \epsilon_i a_i\right| > t\right) \le 2 \exp\left(-\frac{t^2}{2 \sum_{i=1}^n a_i^2}\right) $$
Dans notre cas, $a_i = v_i$. Donc $\sum_{i=1}^n a_i^2 = \sum_{i=1}^n v_i^2$. Puisque $v_i \in \{0,1\}$, $v_i^2 = v_i$.
Donc $\sum_{i=1}^n v_i^2 = \sum_{i=1}^n v_i$. Soit $k_v = \sum_{i=1}^n v_i$ le nombre de $X_i$ pour lesquels $v_i=1$.
L'inégalité de Hoeffding donne :
$$ \mathbb{P}_{\epsilon}\left(\left|\frac{1}{n} \sum_{i=1}^n \epsilon_i v_i\right| > \frac{\delta}{2} \Big| \mathbf{X}\right) \le 2 \exp\left(-\frac{n^2 (\delta/2)^2}{2 \sum_{i=1}^n v_i^2}\right) = 2 \exp\left(-\frac{n^2 \delta^2}{8 k_v}\right) $$
Cependant, $k_v$ peut être petit, ce qui rend la borne lâche. Une borne plus générale et plus robuste pour $\sum_{i=1}^n \epsilon_i a_i$ où $a_i \in [0,1]$ est d'utiliser $\sum a_i^2 \le \sum 1^2 = n$.
Donc, pour $v_i \in \{0,1\}$, $\sum_{i=1}^n v_i^2 \le n$.
$$ \mathbb{P}_{\epsilon}\left(\left|\frac{1}{n} \sum_{i=1}^n \epsilon_i v_i\right| > \frac{\delta}{2} \Big| \mathbf{X}\right) \le 2 \exp\left(-\frac{n^2 (\delta/2)^2}{2 n}\right) = 2 \exp\left(-\frac{n \delta^2}{8}\right) $$
Cette borne est uniforme pour tous les $v \in \mathcal{C}_{\mathbf{X}}$.

#### Étape 3 : Lemme de Sauer

Le nombre de vecteurs distincts dans $\mathcal{C}_{\mathbf{X}}$ est borné par le Lemme de Sauer.
**Lemme de Sauer (ou Sauer-Shelah) :** Si $\mathcal{C}$ est une classe VC de dimension $d$, alors pour tout ensemble de $n$ points $X_1, \dots, X_n \in \mathcal{X}$, le nombre de motifs distincts induits par $\mathcal{C}$ sur ces points est borné par :
$$ |\mathcal{C}_{\mathbf{X}}| \le \Phi_d(n) := \sum_{k=0}^d \binom{n}{k} $$
Une borne supérieure utile pour $\Phi_d(n)$ est $\Phi_d(n) \le (n+1)^d$ pour $n \ge d$. Une borne plus précise est $\Phi_d(n) \le \left(\frac{ne}{d}\right)^d$ pour $n \ge d$. Nous utiliserons la borne $\Phi_d(n) \le (n+1)^d$ pour la simplicité, mais la conclusion reste la même avec la borne plus précise.

En combinant la borne d'union avec le Lemme de Sauer :
$$ \mathbb{P}_{\epsilon}\left(\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| > \frac{\delta}{2} \Big| \mathbf{X}\right) \le |\mathcal{C}_{\mathbf{X}}| \cdot 2 \exp\left(-\frac{n \delta^2}{8}\right) $$
$$ \mathbb{P}_{\epsilon}\left(\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| > \frac{\delta}{2} \Big| \mathbf{X}\right) \le \Phi_d(n) \cdot 2 \exp\left(-\frac{n \delta^2}{8}\right) $$
$$ \mathbb{P}_{\epsilon}\left(\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| > \frac{\delta}{2} \Big| \mathbf{X}\right) \le 2 (n+1)^d \exp\left(-\frac{n \delta^2}{8}\right) $$
Cette borne ne dépend pas de $\mathbf{X}$.

#### Étape 4 : Borne Finale et Convergence

Nous prenons l'espérance sur $\mathbf{X}$ de l'expression précédente :
$$ \mathbb{E}_{\mathbf{X}}\left[\mathbb{P}_{\epsilon}\left(\sup_{C \in \mathcal{C}} \left|\frac{1}{n} \sum_{i=1}^n \epsilon_i \mathbf{1}_C(X_i)\right| > \frac{\delta}{2} \Big| \mathbf{X}\right)\right] = 2 (n+1)^d \exp\left(-\frac{n \delta^2}{8}\right) $$
En substituant ce résultat dans l'inégalité de symétrisation $(*)$ :
$$ \mathbb{P}\left(\sup_{C \in \mathcal{C}} |P_n(C) - P(C)| > \delta\right) \le 2 \left[ 2 (n+1)^d \exp\left(-\frac{n \delta^2}{8}\right) \right] $$
$$ \mathbb{P}\left(\sup_{C \in \mathcal{C}} |P_n(C) - P(C)| > \delta\right) \le 4 (n+1)^d \exp\left(-\frac{n \delta^2}{8}\right) $$
Pour montrer la convergence en probabilité, nous devons vérifier que cette borne tend vers 0 lorsque $n \to \infty$.
Considérons la limite :
$$ \lim_{n \to \infty} 4 (n+1)^d \exp\left(-\frac{n \delta^2}{8}\right) $$
Pour tout $d \in \mathbb{N}$ et tout $\delta > 0$, le terme exponentiel $\exp\left(-\frac{n \delta^2}{8}\right)$ décroît beaucoup plus rapidement que le terme polynomial $(n+1)^d$ ne croît.
Formellement, pour tout polynôme $Q(n)$ et toute constante $c > 0$, $\lim_{n \to \infty} Q(n) e^{-cn} = 0$.
Ici, $Q(n) = 4(n+1)^d$ et $c = \frac{\delta^2}{8}$. Puisque $d$ est fini et $\delta > 0$, $c > 0$.
Donc,
$$ \lim_{n \to \infty} 4 (n+1)^d \exp\left(-\frac{n \delta^2}{8}\right) = 0 $$
Puisque $\delta$ était un réel strictement positif arbitraire, nous avons démontré que :
$$ \sup_{C \in \mathcal{C}} |P_n(C) - P(C)| \xrightarrow{\mathbb{P}} 0 \quad \text{lorsque } n \to \infty $$

Ceci conclut la démonstration de la convergence en probabilité uniforme pour les classes de sets VC.

---

J'espère que cette démonstration pas-à-pas, sans aucune ellipse, vous a permis de saisir la puissance des outils combinatoires (dimension VC, Lemme de Sauer) et probabilistes (symétrisation, inégalités de concentration) pour établir des résultats de convergence uniforme dans des contextes complexes. C'est un résultat fondamental qui ouvre la voie à la compréhension des bornes de généralisation en apprentissage automatique.

N'hésitez pas à poser des questions si des points restent obscurs. La rigueur est la clé de la compréhension profonde en mathématiques.
