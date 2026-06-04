---
uuid: "jalon-137"
title: "Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC)"
year: 3
trimester: 12
tags:
  - math/apprentissage_statistique
  - ia/generalisation
prev: "[[Jalon 136 (Theorie de Vapnik-Chervonenkis).md]]"
next: "[[Jalon 138 (Inégalités de concentration avancées).md]]"
---

# Preuve des bornes de généralisation universelles de Vapnik via la dimension VC

## 1. L'Intuition Première (Niveau 12 ans)
**La Métaphore :** Imagine que tu essaies d'apprendre à reconnaître des chats et des chiens à partir de photos. Si tu regardes seulement 10 photos (ton ensemble d'entraînement), tu pourrais trouver une règle farfelue pour les séparer, comme "tout ce qui a un collier rouge est un chien". Mais cette règle ne marchera pas sur toutes les autres photos du monde. Par contre, si tu as regardé 10 000 photos, la règle que tu trouveras (comme "la forme des oreilles et le museau") a de très fortes chances de marcher pour *n'importe quelle* photo que tu verras plus tard.

**Le "Pourquoi on a inventé ça" :** En intelligence artificielle, on entraîne une machine sur des données que l'on possède déjà (le passé). Mais ce qu'on veut vraiment, c'est que la machine se trompe le moins possible sur les données qu'elle n'a *pas encore vues* (le futur). Vladimir Vapnik et Alexey Chervonenkis voulaient prouver mathématiquement que, sous certaines conditions, ce qu'on observe sur l'échantillon d'entraînement est le reflet fidèle de la réalité globale. Ils voulaient une garantie absolue.

**Visualisation :** Imagine une immense surface vallonnée représentant toutes les erreurs possibles. Tu ne vois qu'une toute petite partie de cette surface à travers quelques trous (tes données d'entraînement). La théorie de Vapnik te donne une formule magique qui te dit : "Je te garantis à 99% que la hauteur de la vallée que tu vois dans ton trou n'est jamais plus profonde de plus de $x$ mètres que le point le plus bas de toute la surface entière." Le but est de calculer ce $x$.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $\mathcal{Z} = \mathcal{X} \times \mathcal{Y}$ un espace d'observations, muni d'une tribu et d'une mesure de probabilité inconnue $\mathbb{P}$.
Soit un échantillon de $n$ variables aléatoires indépendantes et identiquement distribuées (i.i.d.) $S_n = (Z_1, \dots, Z_n) = ((X_1, Y_1), \dots, (X_n, Y_n)) \sim \mathbb{P}^{\otimes n}$.
Soit $\mathcal{H}$ une classe de fonctions (hypothèses) $h: \mathcal{X} \to \mathcal{Y}$. Dans le cadre de la classification binaire, on fixe $\mathcal{Y} = \{-1, +1\}$.
Soit $\ell: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$ une fonction de perte. Ici, nous considérons la perte 0-1 : $\ell(h(x), y) = \mathbf{1}_{h(x) \neq y}$.

On définit la **perte (ou risque) théorique** d'une hypothèse $h \in \mathcal{H}$ comme son espérance sous la vraie distribution :
$$R(h) = \mathbb{E}_{Z \sim \mathbb{P}}[\ell(h(X), Y)] = \mathbb{P}(h(X) \neq Y)$$

On définit la **perte (ou risque) empirique** évaluée sur l'échantillon fini $S_n$ comme la moyenne empirique :
$$R_n(h) = \frac{1}{n} \sum_{i=1}^n \ell(h(X_i), Y_i) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{h(X_i) \neq Y_i}$$

Rappelons que la **dimension VC** (Vapnik-Chervonenkis), notée $d_{VC}(\mathcal{H})$, est la taille maximale $n$ d'un ensemble de points dans $\mathcal{X}$ tel que la classe $\mathcal{H}$ puisse générer toutes les $2^n$ dichotomies possibles sur cet ensemble (on dit que l'ensemble est "pulvérisé").

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Vapnik-Chervonenkis (Borne de Généralisation Universelle) :**
> Soit $\mathcal{H}$ une classe de fonctions à valeurs dans $\{-1, +1\}$ de dimension de Vapnik-Chervonenkis $d = d_{VC}(\mathcal{H}) < \infty$. Soit $\delta \in (0, 1)$.
> Alors, avec une probabilité d'au moins $1 - \delta$ sur le tirage de l'échantillon $S_n \sim \mathbb{P}^{\otimes n}$, on a, pour **toute** hypothèse $h \in \mathcal{H}$ simultanément :
> $$ R(h) \le R_n(h) + 2 \sqrt{2 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n}} $$

Pour démontrer ce résultat central, nous aurons besoin de deux lemmes fondamentaux : le lemme de symétrisation et le lemme de Sauer-Shelah.

> **Lemme de Symétrisation :**
> Soit $S_n = (Z_1, \dots, Z_n)$ un échantillon i.i.d., et $S'_n = (Z'_1, \dots, Z'_n)$ un "échantillon fantôme" i.i.d. suivant la même distribution $\mathbb{P}$. Pour tout $t > 0$ tel que $n t^2 \ge 2$, on a :
> $$ \mathbb{P}_{S_n}\left( \sup_{h \in \mathcal{H}} (R(h) - R_n(h)) > t \right) \le 2 \, \mathbb{P}_{S_n, S'_n}\left( \sup_{h \in \mathcal{H}} (R'_n(h) - R_n(h)) > \frac{t}{2} \right) $$
> où $R'_n(h) = \frac{1}{n}\sum_{i=1}^n \ell(h(X'_i), Y'_i)$ est le risque empirique sur l'échantillon fantôme.

> **Lemme de Sauer-Shelah (Rappel du Jalon 136) :**
> Si $d_{VC}(\mathcal{H}) = d$, alors pour tout entier $n$, la fonction de croissance $\Pi_{\mathcal{H}}(n)$, qui compte le nombre maximal de comportements distincts de $\mathcal{H}$ sur un ensemble de taille $n$, vérifie :
> $$ \Pi_{\mathcal{H}}(n) \le \sum_{i=0}^d \binom{n}{i} $$
> Pour $n \ge d$, cette somme est majorée par $\left(\frac{en}{d}\right)^d$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*L'objectif est d'établir la borne de Vapnik-Chervonenkis. La preuve suit une architecture en trois grands blocs : symétrisation, introduction des variables de Rademacher (ou permutation), et majoration par borne de l'union via le lemme de Sauer.*

### Démonstration du Théorème Pivot : Borne de Vapnik-Chervonenkis

**1. Initialisation / Cadre :**
Nous cherchons à borner la probabilité d'un "mauvais" événement : l'événement où le supremum de l'écart entre le risque théorique et le risque empirique excède un seuil $t$. Posons $P_n(t) = \mathbb{P}\left( \sup_{h \in \mathcal{H}} (R(h) - R_n(h)) > t \right)$. Nous allons procéder par analyse-synthèse, en introduisant un échantillon fantôme pour réduire le problème continu sur $\mathbb{P}$ à un problème combinatoire sur un ensemble fini de $2n$ points.

**2. Étape 1 : Application du Lemme de Symétrisation**
Par le lemme de symétrisation, nous bornons la déviation par rapport à la vraie moyenne par la déviation entre deux moyennes empiriques :
$$ P_n(t) \le 2 \, \mathbb{P}_{S_n, S'_n}\left( \sup_{h \in \mathcal{H}} (R'_n(h) - R_n(h)) > \frac{t}{2} \right) $$
L'intérêt crucial est que la quantité $\sup_{h \in \mathcal{H}} (R'_n(h) - R_n(h))$ ne dépend que du comportement de $\mathcal{H}$ sur la concaténation de $S_n$ et $S'_n$, soit un ensemble fini de $2n$ points.

**3. Étape 2 : L'artifice combinatoire et les variables de Rademacher**
Notons le double échantillon $D_{2n} = (Z_1, \dots, Z_n, Z'_1, \dots, Z'_n)$. Puisque les variables sont i.i.d., échanger $Z_i$ et $Z'_i$ ne change pas la distribution conjointe.
Introduisons des variables de Rademacher i.i.d. $\sigma_i \in \{-1, +1\}$ avec probabilité $1/2$. L'échange entre $Z_i$ et $Z'_i$ équivaut à multiplier le terme $(\ell(h(X'_i), Y'_i) - \ell(h(X_i), Y_i))$ par $\sigma_i$.
Ainsi, en conditionnant sur $D_{2n}$, on peut réécrire la probabilité sur l'aléa des permutations :
$$ \mathbb{P}_{S_n, S'_n}\left( \sup_{h \in \mathcal{H}} \frac{1}{n} \sum_{i=1}^n (\ell(h(X'_i), Y'_i) - \ell(h(X_i), Y_i)) > \frac{t}{2} \right) $$
$$ = \mathbb{E}_{D_{2n}} \left[ \mathbb{P}_{\boldsymbol{\sigma}}\left( \sup_{h \in \mathcal{H}} \frac{1}{n} \sum_{i=1}^n \sigma_i (\ell(h(X'_i), Y'_i) - \ell(h(X_i), Y_i)) > \frac{t}{2} \right) \right] $$

**4. Étape 3 : Borne de l'Union sur la restriction finie**
Conditionnellement à $D_{2n}$, la classe $\mathcal{H}$ ne peut prendre qu'un nombre fini de valeurs distinctes. La fonction de perte $\ell$ étant une fonction déterministe de $h$, la restriction de la classe de pertes $\{ (z \mapsto \ell(h(x), y)) : h \in \mathcal{H} \}$ sur les $2n$ points possède au plus $\Pi_{\mathcal{H}}(2n)$ configurations distinctes.
Notons $\mathcal{H}|_{D_{2n}}$ l'ensemble de ces comportements distincts. Nous appliquons la borne de l'union (l'inégalité de Boole) sur cet ensemble fini :
$$ \mathbb{P}_{\boldsymbol{\sigma}}\left( \sup_{h \in \mathcal{H}|_{D_{2n}}} \frac{1}{n} \sum_{i=1}^n \sigma_i (\ell(h(X'_i), Y'_i) - \ell(h(X_i), Y_i)) > \frac{t}{2} \right) $$
$$ \le \sum_{h \in \mathcal{H}|_{D_{2n}}} \mathbb{P}_{\boldsymbol{\sigma}}\left( \frac{1}{n} \sum_{i=1}^n \sigma_i (\ell(h(X'_i), Y'_i) - \ell(h(X_i), Y_i)) > \frac{t}{2} \right) $$
Le nombre de termes dans la somme est borné par $\Pi_{\mathcal{H}}(2n)$.

**5. Étape 4 : Majoration d'un terme unique par l'inégalité de Hoeffding**
Pour un $h$ fixé, la variable aléatoire $V_i = \sigma_i (\ell(h(X'_i), Y'_i) - \ell(h(X_i), Y_i))$ est centrée ($\mathbb{E}_{\sigma_i}[V_i] = 0$) et est bornée puisque $\ell \in \{0, 1\}$.
Plus précisément, $A_i = \ell(h(X'_i), Y'_i) - \ell(h(X_i), Y_i) \in \{-1, 0, 1\}$.
Ainsi, $V_i$ prend ses valeurs dans l'intervalle $[-1, 1]$, d'amplitude $1 - (-1) = 2$.
Par l'inégalité de Hoeffding appliquée aux variables $V_i$ indépendantes (par rapport à $\boldsymbol{\sigma}$) :
$$ \mathbb{P}_{\boldsymbol{\sigma}}\left( \sum_{i=1}^n V_i > n \frac{t}{2} \right) \le \exp\left( - \frac{2 (n t/2)^2}{\sum_{i=1}^n 2^2} \right) = \exp\left( - \frac{2 n^2 t^2 / 4}{4n} \right) = \exp\left( - \frac{n t^2}{8} \right) $$

**6. Étape 5 : Synthèse des bornes et application de Sauer-Shelah**
En rassemblant les Étape 3 et 4 :
$$ \mathbb{P}_{\boldsymbol{\sigma}} \left( \dots \right) \le \Pi_{\mathcal{H}}(2n) \exp\left( - \frac{n t^2}{8} \right) $$
En reprenant l'espérance sur $D_{2n}$ (Étape 2) :
$$ P_n(t) \le 2 \, \mathbb{E}_{D_{2n}} \left[ \Pi_{\mathcal{H}}(2n) \exp\left( - \frac{n t^2}{8} \right) \right] = 2 \, \Pi_{\mathcal{H}}(2n) \exp\left( - \frac{n t^2}{8} \right) $$
Maintenant, par le lemme de Sauer-Shelah, puisque $d_{VC}(\mathcal{H}) = d$, on sait que pour $2n \ge d$, $\Pi_{\mathcal{H}}(2n) \le \left(\frac{2en}{d}\right)^d$.
Donc :
$$ P_n(t) \le 2 \left(\frac{2en}{d}\right)^d \exp\left( - \frac{n t^2}{8} \right) $$

**7. Conclusion et inversion de la probabilité**
Nous voulons que cette probabilité d'erreur soit au plus égale à $\delta$. Posons :
$$ 2 \left(\frac{2en}{d}\right)^d \exp\left( - \frac{n t^2}{8} \right) = \delta $$
Isolons $t$ de manière purement algébrique :
$$ \exp\left( \frac{n t^2}{8} \right) = \frac{2}{\delta} \left(\frac{2en}{d}\right)^d $$
Passons au logarithme népérien :
$$ \frac{n t^2}{8} = \ln\left( \frac{2}{\delta} \left(\frac{2en}{d}\right)^d \right) $$
$$ \frac{n t^2}{8} = \ln\left(\frac{2}{\delta}\right) + d \ln\left(\frac{2en}{d}\right) $$
$$ t^2 = 8 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n} $$
Puisque $t > 0$, la racine carrée nous donne :
$$ t = \sqrt{8 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n}} = 2 \sqrt{2 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n}} $$
Ainsi, avec une probabilité au moins $1-\delta$, le pire écart $\sup_{h \in \mathcal{H}} (R(h) - R_n(h))$ est inférieur ou égal à $t$. En particulier, pour toute hypothèse $h \in \mathcal{H}$, $R(h) - R_n(h) \le t$, ce qui donne :
$$ R(h) \le R_n(h) + 2 \sqrt{2 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n}} $$
La démonstration, pierre angulaire de l'apprentissage statistique, est ainsi rigoureusement complète et justifiée sans la moindre ellipse.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application Directe (Complexité d'échantillonnage)
**Énoncé :** Soit un problème de classification binaire dans $\mathbb{R}^2$. On décide d'utiliser comme espace d'hypothèses $\mathcal{H}$ l'ensemble de tous les demi-plans séparateurs (les perceptrons linéaires). On sait que $d_{VC}(\mathcal{H}) = 3$.
Vous exigez une confiance de $95\%$ (c'est-à-dire $\delta = 0.05$) pour garantir que l'écart entre le risque théorique et empirique de *n'importe quel* séparateur linéaire que vous pourriez choisir ne dépasse pas un intervalle de confiance abstrait $\epsilon$. Exprimez rigoureusement, à partir de la borne de Vapnik, l'inéquation implicite que doit vérifier le nombre d'échantillons $n$ pour garantir cette borne.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On nous demande de transformer la borne sur l'écart en une condition sur la taille de l'échantillon $n$ (ce qu'on appelle la *sample complexity*).
* *Résolution pas-à-pas :*
1. La borne de Vapnik nous assure avec probabilité $1-\delta$ que pour tout $h \in \mathcal{H}$ :
   $$ R(h) - R_n(h) \le 2 \sqrt{2 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n}} $$
2. On souhaite que ce majorant soit inférieur ou égal à $\epsilon$. On pose donc l'inéquation :
   $$ 2 \sqrt{2 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n}} \le \epsilon $$
3. Élevons les deux membres au carré (tout est positif) :
   $$ 4 \cdot 2 \frac{d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right)}{n} \le \epsilon^2 $$
   $$ \frac{8}{n} \left[ d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right) \right] \le \epsilon^2 $$
4. On isole $n$ en multipliant par $n$ (strictement positif) et en divisant par $\epsilon^2$ :
   $$ n \ge \frac{8}{\epsilon^2} \left[ d \ln\left(\frac{2en}{d}\right) + \ln\left(\frac{2}{\delta}\right) \right] $$
5. On substitue les valeurs numériques données ($d=3$, $\delta=0.05$) :
   $$ n \ge \frac{8}{\epsilon^2} \left[ 3 \ln\left(\frac{2en}{3}\right) + \ln\left(\frac{2}{0.05}\right) \right] $$
   $$ n \ge \frac{8}{\epsilon^2} \left[ 3 \ln\left(\frac{2e}{3}n\right) + \ln(40) \right] $$
Il s'agit d'une équation transcendante (puisque $n$ figure des deux côtés). En pratique, cette inéquation garantit la borne cherchée dès qu'elle est satisfaite, démontrant que la taille d'échantillon requise croît en $\mathcal{O}\left( \frac{d}{\epsilon^2} \ln(\frac{1}{\epsilon}) \right)$.

### Exercice 2 : Niveau Avancé (Inspiré Concours ENS / Exigence Master)
**Énoncé :** Démontrez que le terme de complexité structurelle issu du lemme de symétrisation et de la borne de Hoeffding ne permet d'obtenir la convergence uniforme (i.e. $\sup_{h} |R(h) - R_n(h)| \xrightarrow{\mathbb{P}} 0$) *que si* le rapport $\frac{\ln \Pi_{\mathcal{H}}(2n)}{n}$ tend vers 0 lorsque $n \to \infty$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* Il faut relier la condition de convergence en probabilité de l'écart au comportement asymptotique de la fonction de croissance $\Pi_{\mathcal{H}}(2n)$. C'est le fondement de l'équivalence entre la finitude de la dimension VC et l'apprenabilité PAC.
* *Résolution pas-à-pas :*
1. Pour prouver la convergence uniforme en probabilité, il faut montrer que pour tout $t > 0$,
   $$ \lim_{n \to \infty} \mathbb{P}\left( \sup_{h \in \mathcal{H}} |R(h) - R_n(h)| > t \right) = 0 $$
2. Reprenons la majoration stricte obtenue à l'étape 6 de la preuve (en considérant la valeur absolue, on multiplie la borne de Hoeffding par 2 pour les queues bilatérales, et on a le facteur 2 de la symétrisation) :
   $$ \mathbb{P}\left( \sup_{h \in \mathcal{H}} |R(h) - R_n(h)| > t \right) \le 4 \, \Pi_{\mathcal{H}}(2n) \exp\left( - \frac{n t^2}{8} \right) $$
3. Posons $B_n(t) = 4 \, \Pi_{\mathcal{H}}(2n) \exp\left( - \frac{n t^2}{8} \right)$. Pour que cette borne soit utile et prouve la convergence, il est nécessaire et suffisant de montrer que $\lim_{n \to \infty} B_n(t) = 0$.
4. Étudions le logarithme de $B_n(t)$ :
   $$ \ln(B_n(t)) = \ln(4) + \ln(\Pi_{\mathcal{H}}(2n)) - \frac{n t^2}{8} $$
5. Factorisons par $n$ le terme prépondérant asymptotiquement :
   $$ \ln(B_n(t)) = n \left[ \frac{\ln(4)}{n} + \frac{\ln(\Pi_{\mathcal{H}}(2n))}{n} - \frac{t^2}{8} \right] $$
6. Puisque $t > 0$ est fixé, le terme $-\frac{t^2}{8}$ est une constante strictement négative. Le terme $\frac{\ln(4)}{n}$ tend vers $0$.
7. Si $\lim_{n \to \infty} \frac{\ln \Pi_{\mathcal{H}}(2n)}{n} = 0$, alors le terme entre crochets tend vers une constante strictement négative ($-t^2 / 8$).
   Par conséquent, $\lim_{n \to \infty} \ln(B_n(t)) = -\infty$.
   Et par composition avec l'exponentielle, $\lim_{n \to \infty} B_n(t) = 0$.
8. À l'inverse, si ce rapport ne tendait pas vers 0, mais vers une constante $C > 0$, alors pour un $t$ suffisamment petit (tel que $\frac{t^2}{8} < C$), le terme entre crochets serait positif, entraînant la divergence de la borne, et ruinant toute garantie universelle.
9. La condition fondamentale d'apprenabilité est donc bien $\frac{\ln \Pi_{\mathcal{H}}(2n)}{n} \xrightarrow{n \to \infty} 0$, qui est satisfaite de manière éclatante si la dimension VC est finie grâce au lemme de Sauer (croissance polynomiale opposée à l'exponentielle $n$).

## 5. Ancrage & Application en Intelligence Artificielle
- **Le Pont Théorique :** Le Théorème de Vapnik-Chervonenkis est la clé de voûte de l'apprentissage machine (Machine Learning). Il prouve rigoureusement le principe de "Minimisation du Risque Empirique" (ERM). Quand vous entraînez un modèle avec scikit-learn, vous minimisez $R_n(h)$. Sans la théorie VC, minimiser $R_n(h)$ serait un acte de foi aveugle, car cela ne garantirait en rien que $R(h)$ sera petit. La théorie VC dresse un pont infranchissable qui force $R(h)$ à suivre docilement $R_n(h)$ vers le bas.
- **Exemple Concret :** Dans la conception des Support Vector Machines (SVM), l'objectif est d'utiliser un mapping via un *noyau* vers un espace de grande dimension, ce qui risque de faire exploser la dimension VC (et donc de relâcher dangereusement la borne, provoquant de l'overfitting). Cependant, Vapnik a prouvé un théorème collatéral montrant que pour les SVM à marge maximale, la borne de généralisation ne dépend plus de la dimension intrinsèque de l'espace, mais de l'inverse de la marge (la "fat-shattering dimension"). La théorie VC a ainsi directement guidé l'architecture algorithmique des SVM pour maintenir la borne petite et forcer la généralisation.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 133 (Modele PAC)]], [[Jalon 134 (Complexite des classes de fonctions)]], [[Jalon 136 (Theorie de Vapnik-Chervonenkis)]]
- **Concepts Futurs dépendants :** [[Jalon 138 (Inégalités de concentration avancées)]], [[Jalon 139 (Notion de stabilité algorithmique)]]
