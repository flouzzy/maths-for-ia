---
uuid: "jalon-94"
title: "Théorème central limite (TCL)"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon 93 (Fonctions caractéristiques).md]]"
next: "[[Jalon 95 (Vecteurs gaussiens).md]]"
---

# Jalon 94 : Théorème central limite (TCL)

## Introduction au comportement asymptotique

Le théorème central limite (TCL) est l'un des piliers des probabilités modernes. Il formalise le fait que la somme d'un grand nombre de variables aléatoires indépendantes et identiquement distribuées, convenablement normalisée, converge en loi vers une distribution normale standard, quelle que soit la loi d'origine de ces variables (pourvu qu'elles admettent une variance finie).

Ce résultat justifie l'ubiquité de la loi normale dans les sciences appliquées, les statistiques et l'intelligence artificielle, où les phénomènes complexes sont souvent modélisés comme l'accumulation de multiples petites perturbations indépendantes.

### Exemple Concret Immédiat : Moyenne des notes

Considérons une classe de 100 élèves passant un examen difficile noté sur 20. Les notes $X_1, \dots, X_{100}$ sont I.I.D. avec une espérance $\mu = 10$ et une variance $\sigma^2 = 9$.
La note moyenne de la classe est $\bar{X} = \frac{1}{100} \sum_{i=1}^{100} X_i$.
Bien que la répartition des notes individuelles puisse être asymétrique ou multimodale, le TCL garantit que la variable $\bar{X}$ suit approximativement une loi $\mathcal{N}(10, \frac{9}{100})$.
On a donc $\bar{X} \approx \mathcal{N}(10, 0.09)$. L'écart-type est $\sigma_{\bar{X}} = 0.3$.
La probabilité que la moyenne de la classe se situe entre $9.4$ et $10.6$ (soit à $\pm 2$ écarts-types) est d'environ $95\%$, indépendamment de la forme de la loi de $X_i$.

## Énoncé du Théorème Central Limite (Lindeberg-Lévy)

### Formalisation

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires réelles, indépendantes et identiquement distribuées (I.I.D.). On suppose que ces variables admettent un moment d'ordre deux fini, ce qui implique l'existence de leur espérance et de leur variance :
- Espérance : $\mathbb{E}[X_1] = \mu$
- Variance : $\text{Var}(X_1) = \sigma^2$, avec $0 < \sigma^2 < \infty$.

On définit la somme partielle $S_n = \sum_{i=1}^n X_i$ et la moyenne empirique $\bar{X}_n = \frac{S_n}{n}$.

> **Théorème (Théorème Central Limite) :**
> La variable aléatoire centrée et réduite $Z_n$ définie par :
> $$Z_n = \frac{S_n - n\mu}{\sigma \sqrt{n}} = \sqrt{n} \left( \frac{\bar{X}_n - \mu}{\sigma} \right)$$
> converge en loi vers la loi normale centrée réduite $\mathcal{N}(0, 1)$ lorsque $n \to \infty$.
>
> Autrement dit, pour tout couple de réels $a < b$ :
> $$\lim_{n \to \infty} \mathbb{P}(a \le Z_n \le b) = \int_a^b \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx$$

### Exemple Concret Immédiat : Somme de variables uniformes

Considérons $n=12$ variables aléatoires $X_1, \dots, X_{12}$ indépendantes, suivant toutes une loi uniforme continue sur l'intervalle $[0, 1]$.
- L'espérance est $\mu = \frac{1}{2}$.
- La variance est $\sigma^2 = \frac{1}{12}$.

On pose $S_{12} = \sum_{i=1}^{12} X_i$.
L'espérance de la somme est $\mathbb{E}[S_{12}] = 12 \times \frac{1}{2} = 6$.
La variance de la somme est $\text{Var}(S_{12}) = 12 \times \frac{1}{12} = 1$.

D'après le TCL, la variable $Z_{12} = \frac{S_{12} - 6}{1} = S_{12} - 6$ est approximativement de loi $\mathcal{N}(0, 1)$.
Par conséquent, la somme $S_{12}$ elle-même suit approximativement une loi $\mathcal{N}(6, 1)$.
C'est une méthode historiquement utilisée pour générer informatiquement des nombres pseudo-aléatoires de loi normale.

### Exemple Concret Immédiat : Lancer de pièces

Si on lance une pièce équilibrée $n=400$ fois, le nombre de Faces $S_{400}$ suit une loi binomiale $\mathcal{B}(400, 0.5)$.
$\mu = np = 200$, et $\sigma = \sqrt{np(1-p)} = \sqrt{100} = 10$.
Pour évaluer $\mathbb{P}(190 \le S_{400} \le 210)$, le TCL indique que $Z_{400} = \frac{S_{400} - 200}{10}$ est proche de $\mathcal{N}(0,1)$.
L'événement se réécrit $-1 \le Z_{400} \le 1$.
Par intégration de la loi normale, $\mathbb{P}(-1 \le Z \le 1) \approx 0.6826$.
La probabilité exacte est $0.683$, ce qui montre la puissance d'approximation du théorème.

## Démonstration via les fonctions caractéristiques

La démonstration classique repose sur l'outil des fonctions caractéristiques (transformée de Fourier des mesures de probabilité) et sur le théorème de continuité de Paul Lévy.

**Preuve pas à pas :**

Afin d'alléger les notations, on peut, sans perte de généralité, centrer et réduire préalablement les variables $X_i$.
Posons $Y_i = \frac{X_i - \mu}{\sigma}$.
Les variables $(Y_i)$ sont I.I.D., vérifient $\mathbb{E}[Y_1] = 0$ et $\mathbb{E}[Y_1^2] = \text{Var}(Y_1) = 1$.

La somme normalisée étudiée s'écrit alors :
$$Z_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n Y_i$$

Soit $\phi_Y(t) = \mathbb{E}[e^{itY_1}]$ la fonction caractéristique commune aux variables $Y_i$.
Puisque $Y_1$ admet des moments finis jusqu'à l'ordre 2, sa fonction caractéristique admet un développement limité à l'ordre 2 au voisinage de $0$ :
$$\phi_Y(t) = \phi_Y(0) + t \phi_Y'(0) + \frac{t^2}{2} \phi_Y''(0) + o(t^2)$$

Par les propriétés des fonctions caractéristiques :
- $\phi_Y(0) = 1$
- $\phi_Y'(0) = i\mathbb{E}[Y_1] = 0$
- $\phi_Y''(0) = i^2\mathbb{E}[Y_1^2] = -1 \times 1 = -1$

On obtient donc, au voisinage de $t=0$ :
$$\phi_Y(t) = 1 - \frac{t^2}{2} + o(t^2)$$

Calculons maintenant la fonction caractéristique de $Z_n$.
Par linéarité de l'argument de l'exponentielle complexe et par indépendance des variables $(Y_i)$ :
$$\phi_{Z_n}(t) = \mathbb{E}\left[ \exp\left( it \frac{1}{\sqrt{n}} \sum_{j=1}^n Y_j \right) \right]$$
$$\phi_{Z_n}(t) = \prod_{j=1}^n \mathbb{E}\left[ \exp\left( i \frac{t}{\sqrt{n}} Y_j \right) \right]$$
$$\phi_{Z_n}(t) = \left( \phi_Y\left( \frac{t}{\sqrt{n}} \right) \right)^n$$

Fixons $t \in \mathbb{R}$. Pour $n$ suffisamment grand, le terme $\frac{t}{\sqrt{n}}$ tend vers $0$. On peut donc utiliser le développement limité obtenu précédemment :
$$\phi_Y\left( \frac{t}{\sqrt{n}} \right) = 1 - \frac{1}{2} \left(\frac{t}{\sqrt{n}}\right)^2 + o\left( \frac{t^2}{n} \right) = 1 - \frac{t^2}{2n} + o\left( \frac{1}{n} \right)$$

Il s'ensuit que :
$$\phi_{Z_n}(t) = \left( 1 - \frac{t^2}{2n} + o\left( \frac{1}{n} \right) \right)^n$$

En passant au logarithme (pour $n$ assez grand afin que l'argument soit positif) :
$$\ln \phi_{Z_n}(t) = n \ln\left( 1 - \frac{t^2}{2n} + o\left( \frac{1}{n} \right) \right)$$

Puisque $\ln(1 + x) \sim x$ quand $x \to 0$ :
$$\ln \phi_{Z_n}(t) \sim n \left( - \frac{t^2}{2n} \right) = - \frac{t^2}{2}$$

En composant par la fonction exponentielle (qui est continue), on obtient la limite ponctuelle :
$$\lim_{n \to \infty} \phi_{Z_n}(t) = e^{-t^2/2}$$

Or, la fonction $t \mapsto e^{-t^2/2}$ est précisément la fonction caractéristique de la loi normale centrée réduite $\mathcal{N}(0, 1)$.
D'après le théorème de continuité de Lévy, la convergence ponctuelle des fonctions caractéristiques vers une fonction continue en $0$ implique la convergence en loi des variables aléatoires associées :
$$Z_n \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$

Ce qui achève la démonstration du Théorème Central Limite.

### Exemple Concret Immédiat : Vérification du DL avec Poisson

Si on considère des variables $X_i$ de loi de Poisson $\mathcal{P}(1)$ (donc $\mu=1, \sigma^2=1$).
La fonction caractéristique de $X$ centrée (donc $Y = X-1$) est :
$\phi_Y(t) = \mathbb{E}[e^{it(X-1)}] = e^{-it} \exp(e^{it} - 1) = \exp(e^{it} - 1 - it)$.
Le développement de $e^{it} = 1 + it - t^2/2 + o(t^2)$ donne :
$e^{it} - 1 - it = -t^2/2 + o(t^2)$.
D'où $\phi_Y(t) = \exp(-t^2/2 + o(t^2)) = 1 - t^2/2 + o(t^2)$.
On retrouve bien la structure quadratique $(-t^2/2)$ requise par le théorème.

### Exemple Concret Immédiat : Cas Gaussien

Si $X_1 \sim \mathcal{N}(0, 1)$, alors sa fonction caractéristique est exactement $\phi_X(t) = e^{-t^2/2}$.
Dans ce cas, $\phi_X(t/\sqrt{n})^n = (e^{-t^2/(2n)})^n = e^{-t^2/2}$.
La limite est atteinte instantanément pour tout $n$, car la somme de variables normales indépendantes reste normale.

## Vitesse de convergence : Théorème de Berry-Esseen

Le TCL assure la convergence asymptotique. Pour quantifier l'erreur d'approximation à $n$ fini, on fait appel au théorème de Berry-Esseen.

> **Théorème de Berry-Esseen :**
> Si, en plus des hypothèses du TCL, le moment d'ordre 3 est fini, c'est-à-dire $\mathbb{E}[|X_1|^3] = \rho < \infty$, alors il existe une constante universelle $C$ (telle que $0.4 \le C \le 0.4748$) telle que pour tout $x \in \mathbb{R}$ et tout $n \in \mathbb{N}^*$ :
> $$\left| \mathbb{P}(Z_n \le x) - \Phi(x) \right| \le \frac{C \rho}{\sigma^3 \sqrt{n}}$$
> où $\Phi$ désigne la fonction de répartition de la loi $\mathcal{N}(0, 1)$.

Cela démontre que l'erreur d'approximation uniforme décroît en $\mathcal{O}\left(\frac{1}{\sqrt{n}}\right)$.

### Exemple Concret Immédiat : Calcul d'erreur

Reprenons l'exemple d'une variable de Bernoulli modélisant un pile ou face biaisé avec $p=0.2$.
$\mu = 0.2$, $\sigma^2 = 0.16$, et $\sigma = 0.4$.
Calculons $\rho = \mathbb{E}[|X - 0.2|^3]$.
$X = 1$ avec probabilité $0.2$, et $X = 0$ avec probabilité $0.8$.
$\rho = 0.2 \times |1 - 0.2|^3 + 0.8 \times |0 - 0.2|^3 = 0.2 \times 0.512 + 0.8 \times 0.008 = 0.1024 + 0.0064 = 0.1088$.
L'erreur de l'approximation normale est bornée par $\frac{0.4748 \times 0.1088}{(0.4)^3 \sqrt{n}} \approx \frac{0.0516}{0.064 \sqrt{n}} \approx \frac{0.807}{\sqrt{n}}$.
Pour $n=100$ lancers, l'erreur est inférieure à $8\%$. Pour $n=10000$, l'erreur chute sous les $0.8\%$.

## Applications en Intelligence Artificielle et Statistique

La puissance du TCL se manifeste particulièrement en apprentissage automatique et en théorie de l'information.

### Initialisation des réseaux de neurones (Xavier/He)

Dans un réseau de neurones profond, l'activation d'un neurone correspond à une somme pondérée d'entrées $z = \sum_{i=1}^d w_i x_i$.
Sous des hypothèses raisonnables (indépendance des $w_i$ et des $x_i$, centrés), cette somme agit comme l'addition d'un grand nombre de variables aléatoires indépendantes.
D'après le TCL, la pré-activation $z$ tend vers une loi normale. Le contrôle rigoureux de la variance de cette loi normale limite l'explosion ou la disparition des gradients. C'est le fondement de l'initialisation de Xavier Glorot et Kaiming He, où les variances des poids sont choisies proportionnellement à $1/d$.

### Modèles de diffusion (Diffusion Models)

Les modèles génératifs de diffusion, tels que ceux utilisés pour la synthèse d'images, consistent à injecter progressivement un bruit gaussien de faible amplitude à une donnée initiale.
Le TCL (ou plus rigoureusement le théorème de Donsker, son extension aux processus stochastiques) explique pourquoi l'accumulation d'un très grand nombre de petites perturbations additives et indépendantes conduit inexorablement à une distribution marginale parfaitement gaussienne au bout du processus de corruption (Forward Process). L'inversion de ce processus (Reverse Diffusion) s'appuie alors intégralement sur les propriétés analytiques du noyau gaussien.
