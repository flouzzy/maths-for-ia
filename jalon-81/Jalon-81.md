---
uuid: "jalon-81"
title: "Transformée de Fourier dans L2 et Plancherel"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 80 (Transformée de Fourier dans L1).md]]"
next: "[[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]]"
---

# Jalon 81 : Transformée de Fourier dans $L^2$ et Isométrie de Plancherel

## 1. Introduction à l'énergie spectrale

Dans le cadre du jalon précédent, nous avons bâti la transformée de Fourier sur l'espace $L^1(\mathbb{R})$, c'est-à-classiquement les signaux intégrables, pour lesquels l'intégrale définissant la transformée convergeait absolument. C'était une première victoire conceptuelle, mais physiquement insuffisante.

L'immense majorité des signaux d'intérêt physique, optique ou quantique (ondes électromagnétiques, signaux de télécommunication périodiques amortis, états quantiques) ne vivent pas naturellement dans $L^1$, mais dans $L^2(\mathbb{R})$, l'espace des fonctions de carré intégrable. Cet espace, un espace de Hilbert, encode une grandeur physique cardinale : **l'énergie totale** du signal, donnée par $\|f\|_2^2 = \int |f(t)|^2 dt$.

La quête fondatrice des mathématiciens (comme Plancherel et Parseval) fut de se demander si la décomposition spectrale conservait cette énergie. Autrement dit, si l'on éclate un faisceau de lumière en un spectre de couleurs, la somme des énergies de chaque couleur est-elle égale à l'énergie du faisceau incident ? La réponse est positive, et s'incarne mathématiquement par l'extension de l'opérateur de Fourier à $L^2$ via un argument profond de densité et de complétude. C'est le triomphe de l'analyse fonctionnelle qui permet de définir une transformée même lorsque l'intégrale classique de Fourier diverge.

## 2. Définitions, Théorèmes et Exemples

### Isométrie de Plancherel sur un sous-espace dense

L'approche de la théorie commence par l'observation de ce qui se passe sur un espace très régulier : l'espace de Schwartz $\mathcal{S}(\mathbb{R})$ (ou alternativement, $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$).

> **Théorème (Identité de Plancherel sur $L^1 \cap L^2$) :**
> Soit $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$. Alors sa transformée de Fourier $\mathcal{F}(f) = \hat{f}$, définie par la formule intégrale de Lebesgue $\hat{f}(\xi) = \int_{\mathbb{R}} f(t) e^{-i\xi t} dt$, appartient également à $L^2(\mathbb{R})$ (bien qu'elle ne soit pas toujours dans $L^1$).
> De plus, on a l'égalité stricte des énergies (à un facteur de normalisation près dépendant de la convention) :
> $$ \|\hat{f}\|_{L^2}^2 = 2\pi \|f\|_{L^2}^2 $$

**Exemple concret de vérification analytique :**
Considérons le signal "porte" (la fente rectangulaire en optique) : $f(t) = \mathbf{1}_{[-a, a]}(t)$ pour $a > 0$.
Clairement, $f \in L^1 \cap L^2$.
1. Calcul de l'énergie temporelle :
   $$ \|f\|_2^2 = \int_{-a}^{a} 1^2 dt = 2a $$
2. Calcul de la transformée de Fourier (vue au Jalon 80) :
   $$ \hat{f}(\xi) = \int_{-a}^{a} e^{-i\xi t} dt = \left[ \frac{e^{-i\xi t}}{-i\xi} \right]_{-a}^{a} = \frac{e^{ia\xi} - e^{-ia\xi}}{i\xi} = 2 \frac{\sin(a\xi)}{\xi} $$
3. Calcul de l'énergie spectrale :
   $$ \|\hat{f}\|_2^2 = \int_{-\infty}^{\infty} 4 \frac{\sin^2(a\xi)}{\xi^2} d\xi $$
   En posant le changement de variable $u = a\xi$, $d\xi = \frac{du}{a}$, on obtient :
   $$ \|\hat{f}\|_2^2 = \int_{-\infty}^{\infty} 4 \frac{\sin^2(u)}{(u/a)^2} \frac{du}{a} = 4a \int_{-\infty}^{\infty} \frac{\sin^2(u)}{u^2} du $$
   On sait (par l'analyse complexe ou l'identité de Parseval que l'on est en train de vérifier) que $\int_{-\infty}^{\infty} \frac{\sin^2(u)}{u^2} du = \pi$.
   Ainsi :
   $$ \|\hat{f}\|_2^2 = 4a \pi $$
   On vérifie exactement que $\|\hat{f}\|_2^2 = 2\pi (2a) = 2\pi \|f\|_2^2$. Le théorème est confirmé sur cet exemple.


### Prolongement à l'espace $L^2$ complet

Nous avons une application $\mathcal{F} : L^1 \cap L^2 \to L^2$ qui, divisée par $\sqrt{2\pi}$, préserve la norme $\|\cdot\|_2$. C'est une isométrie.

> **Théorème de Plancherel-Parseval (Global) :**
> L'opérateur de Fourier $\mathcal{F}$, défini sur le sous-espace dense $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, se prolonge de manière unique en un opérateur linéaire borné et bijectif de $L^2(\mathbb{R})$ dans $L^2(\mathbb{R})$.
> Ce prolongement continu, noté encore $\mathcal{F}$ (ou $\hat{f}$ pour l'image), vérifie pour tout $f, g \in L^2(\mathbb{R})$ :
> 1. L'isométrie : $\|\hat{f}\|_2 = \sqrt{2\pi} \|f\|_2$
> 2. La conservation du produit scalaire : $\langle \hat{f}, \hat{g} \rangle = 2\pi \langle f, g \rangle$
> 3. L'inversion : $f(t) = \frac{1}{2\pi} \mathcal{F}(\hat{f})(-t)$ au sens de $L^2$.

**Cas pathologique et subtilité absolue :**
Si $f \in L^2 \setminus L^1$, l'intégrale classique $\int_{\mathbb{R}} f(t) e^{-i\xi t} dt$ **ne converge pas** au sens de Lebesgue (puisque $\int |f(t)| dt = +\infty$). Par exemple $f(t) = \frac{\sin(t)}{t}$ est dans $L^2$ mais pas dans $L^1$.
La transformée de Fourier dans $L^2$ est alors définie **comme une limite** dans l'espace de Hilbert. On définit $\hat{f}$ comme la limite en norme $L^2$ de la suite $\hat{f}_n$ où $f_n(t) = f(t)\mathbf{1}_{[-n, n]}(t)$.
On écrit formellement : $\hat{f} = L^2\text{-}\lim_{n \to \infty} \int_{-n}^{n} f(t) e^{-i\xi t} dt$. On ne peut évaluer $\hat{f}(\xi)$ "point par point" de façon classique sans précautions.

**Exemple concret du Sinus Cardinal :**
Considérons $f(t) = \frac{\sin(t)}{t} = \text{sinc}(t)$.
Ce signal n'est pas dans $L^1$. Comment trouver sa transformée de Fourier ?
Nous utiliserons l'opérateur inverse de Plancherel. Prenons une fonction porte en fréquence : $\hat{g}(\xi) = \pi \mathbf{1}_{[-1, 1]}(\xi)$.
Clairement $\hat{g} \in L^1 \cap L^2$. Sa transformée inverse classique donne un signal temporel $g(t)$ :
$$ g(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \hat{g}(\xi) e^{i\xi t} d\xi = \frac{1}{2\pi} \int_{-1}^{1} \pi e^{i\xi t} d\xi = \frac{1}{2} \left[ \frac{e^{i\xi t}}{it} \right]_{-1}^{1} = \frac{\sin(t)}{t} $$
Donc $g(t) = f(t)$.
Puisque l'opérateur de Fourier est une bijection de $L^2$, si l'inverse donne $f$, cela implique catégoriquement que $\hat{f}(\xi) = \pi \mathbf{1}_{[-1, 1]}(\xi)$ au sens de $L^2$ (presque partout).

## 3. Démonstrations

### Démonstration rigoureuse du prolongement isométrique (Théorème de Plancherel)

Le but est d'établir l'existence et l'unicité de ce prolongement sur l'espace complet $L^2(\mathbb{R})$.

**Étape 1 : Hypothèse de densité**
Soit $E = L^1(\mathbb{R}) \cap L^2(\mathbb{R})$. L'espace $E$ est dense dans $L^2(\mathbb{R})$. En effet, pour toute fonction $f \in L^2(\mathbb{R})$, la suite tronquée $f_n = f \cdot \mathbf{1}_{[-n, n]}$ appartient à $E$ (car à support compact et de carré intégrable, donc intégrable) et $f_n \xrightarrow{L^2} f$ par le théorème de convergence dominée.

**Étape 2 : L'opérateur initial**
Définissons $\Phi : E \to L^2(\mathbb{R})$ par $\Phi(f) = \frac{1}{\sqrt{2\pi}} \mathcal{F}(f)$.
Nous admettons l'identité de Parseval sur l'espace de Schwartz (ou sur $E$ par régularisation), ce qui nous donne :
$$ \forall f \in E, \quad \|\Phi(f)\|_2 = \|f\|_2 $$
Ainsi, $\Phi$ est une application linéaire isométrique sur le sous-espace $E$. Une isométrie est nécessairement continue, et sa norme d'opérateur est $\|\Phi\|_{op} = 1$.

**Étape 3 : Construction de l'image pour $f \notin E$ via suites de Cauchy**
Soit $f \in L^2(\mathbb{R})$. Par la densité de $E$, il existe une suite $(f_n)_{n \in \mathbb{N}} \in E^{\mathbb{N}}$ telle que $f_n \xrightarrow{L^2} f$.
Puisque $(f_n)$ converge dans $L^2$, c'est une **suite de Cauchy** dans $L^2$ :
$$ \forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p,q \geq N, \quad \|f_p - f_q\|_2 < \varepsilon $$
Appliquons $\Phi$ aux éléments de cette suite pour former la suite $(\Phi(f_n))$.
Évaluons la distance entre deux termes de cette suite image :
$$ \|\Phi(f_p) - \Phi(f_q)\|_2 = \|\Phi(f_p - f_q)\|_2 $$
Par l'isométrie de $\Phi$ sur $E$ :
$$ \|\Phi(f_p - f_q)\|_2 = \|f_p - f_q\|_2 < \varepsilon \quad \text{pour } p,q \geq N $$
Ainsi, la suite $(\Phi(f_n))$ est elle-même une suite de Cauchy dans $L^2(\mathbb{R})$.

**Étape 4 : Utilisation de la complétude**
C'est ici qu'intervient la nature hilbertienne de l'espace. $L^2(\mathbb{R})$ est un espace **complet** (Théorème de Riesz-Fischer, Jalon 75).
Toute suite de Cauchy dans un espace complet converge vers une limite dans cet espace.
Donc, la suite $(\Phi(f_n))$ converge vers un élément $F \in L^2(\mathbb{R})$.
Nous posons par définition : $\widetilde{\Phi}(f) = F$.
Le prolongement de la transformée de Fourier de $f$ est alors $\hat{f} = \sqrt{2\pi} F$.

**Étape 5 : Indépendance vis-à-vis de la suite et unicité**
Supposons qu'il existe une autre suite $(g_n) \in E^{\mathbb{N}}$ convergeant vers $f$.
Considérons la suite combinée $(h_n)$ définie par $h_{2n} = f_n$ et $h_{2n+1} = g_n$.
La suite $(h_n)$ converge vers $f$. C'est une suite de Cauchy, donc $(\Phi(h_n))$ converge vers une limite unique $H$.
Les sous-suites $(\Phi(f_n))$ et $(\Phi(g_n))$ doivent converger vers la même limite $H = F$. La définition de $\widetilde{\Phi}(f)$ ne dépend donc pas du choix de la suite. L'unicité du prolongement continu d'une application uniformément continue d'un sous-espace dense dans un espace complet conclut la démonstration.

## 4. Applications en Physique, Logique & Intelligence Artificielle

### Analyse de densité spectrale (Spectral Norm) dans les GANs

Dans les réseaux génératifs adversariaux (GANs), le discriminateur doit mesurer la distance entre la vraie distribution de données et la distribution générée, souvent en utilisant la distance de Wasserstein. Pour que cette distance soit calculable, la fonction réseau neuronal (le discriminateur) doit être globalement Lipschitzienne (contrainte de gradient borné).
La **Normalisation Spectrale (Spectral Normalization)**, inventée par Miyato et al. (2018), consiste à diviser les poids de chaque couche convolutive par leur plus grande valeur singulière.
D'un point de vue continu, un noyau de convolution $k$ agit comme $f \mapsto k * f$. L'opérateur de Fourier transforme cette convolution en produit simple : $\mathcal{F}(k * f) = \mathcal{F}(k) \cdot \mathcal{F}(f)$.
La norme d'opérateur de cette convolution sur $L^2$ (qui borne la constante de Lipschitz globale) est exactement donnée par l'isométrie de Plancherel :
$$ \|k * f\|_2 \leq \sup_{\xi} |\hat{k}(\xi)| \cdot \|f\|_2 $$
La plus grande valeur singulière de l'opérateur de convolution correspond au maximum de l'amplitude de sa transformée de Fourier, $\|\hat{k}\|_\infty$. Plancherel établit ce pont fondamental entre le domaine spatial (les poids du filtre) et la borne de stabilité fréquentielle.

### Théorème de Nyquist-Shannon et compression de l'information (Audio/Image)

Lorsqu'une intelligence artificielle traite un signal brut (comme une seconde d'audio .wav à 44100 Hz), l'espace d'entrée est gigantesque.
Grâce à Plancherel, l'énergie du signal (ce qui importe perceptuellement et mathématiquement) est conservée si l'on bascule dans le domaine fréquentiel $L^2$.
Si le signal a un spectre concentré (c'est-à-dire que $\hat{f}$ est nulle en dehors de $[-\Omega, \Omega]$), Plancherel nous assure que le signal peut être reconstruit sans perte d'énergie à partir de points d'échantillons discrets espacés de $\pi / \Omega$.
Ceci permet de projeter la donnée sur un espace de dimension finie sans aucune fuite d'information avant de l'injecter dans un réseau de neurones. L'orthogonalité préservée permet de compresser la donnée sans altérer les produits scalaires (qui sont la base des similarités cosinus mesurées par l'IA).
