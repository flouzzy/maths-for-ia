---
uuid: "jalon-82"
title: "Introduction aux distributions de Schwartz"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-81.md]]"
next: "[[Jalon-83.md]]"
---

# Jalon 82 : Introduction aux distributions de Schwartz

## 1. Introduction : Genèse physique et mathématique

L'étude des phénomènes physiques impulsifs ou ponctuels a longtemps posé un défi majeur à l'analyse mathématique classique. Considérons, par exemple, le choc instantané d'un marteau sur une corde vibrante, ou encore la modélisation d'une charge électrique ponctuelle. Dans ces situations, on observe une quantité totale non nulle (comme une impulsion ou une charge) concentrée en un unique point de l'espace ou du temps.

Si l'on cherche à représenter une telle densité par une fonction classique $f(x)$, cette fonction devrait être nulle partout sauf en ce point précis (disons, l'origine $x=0$), où elle devrait tendre vers l'infini. Or, l'intégrale de Lebesgue d'une fonction nulle presque partout est nulle, ce qui contredit l'idée que l'intégrale totale représente la charge globale (qui vaut 1). Les ingénieurs et physiciens, tels que Paul Dirac au début du XXe siècle, utilisaient des objets formels comme la "fonction" $\delta$ (qui porte désormais son nom), la manipulant avec succès dans des calculs sans justification mathématique rigoureuse.

La théorie des distributions, développée par le mathématicien français Laurent Schwartz (médaille Fields 1950), apporte une solution élégante et définitive à ce paradoxe. L'idée fondatrice est de changer de perspective : au lieu de considérer une "fonction" ponctuellement, on l'étudie par son interaction (son intégrale) avec des fonctions dites "tests", très régulières. Les objets mathématiques ne sont plus étudiés par leurs valeurs ponctuelles, mais par la manière dont ils "mesurent" d'autres fonctions. Cette approche généralise la notion de fonction et donne un cadre rigoureux à la masse de Dirac et à ses dérivées.

\begin{center}
\begin{tikzpicture}[scale=1]
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};

  % Suite de fonctions approchant Dirac
  \draw[blue, thick] (-2,0) -- (-0.5,0) -- (-0.5, 1) -- (0.5, 1) -- (0.5, 0) -- (2,0);
  \node[blue] at (1, 1.2) {$f_1$};

  \draw[red, thick] (-2,0) -- (-0.25,0) -- (-0.25, 2) -- (0.25, 2) -- (0.25, 0) -- (2,0);
  \node[red] at (0.6, 2.2) {$f_2$};

  \draw[green!60!black, thick] (-2,0) -- (-0.125,0) -- (-0.125, 4) -- (0.125, 4) -- (0.125, 0) -- (2,0);
  \node[green!60!black] at (0.4, 3.8) {$f_3$};

  \node[below] at (0,0) {$0$};
\end{tikzpicture}
\\ \textit{Figure 1 : Fonctions "portes" d'aire 1 dont la limite au sens des distributions est la distribution de Dirac $\delta_0$.}
\end{center}

## 2. Définitions, Théorèmes & Exemples

Pour définir le concept de distribution, il faut préalablement définir l'espace des fonctions sur lequel ces distributions vont agir. Ces fonctions doivent être suffisamment régulières pour absorber les irrégularités des objets qu'on étudie.

> **Définition 1 (Support d'une fonction) :**
> Soit $f : \mathbb{R}^n \to \mathbb{C}$ une fonction continue. Le support de $f$, noté $\text{supp}(f)$, est l'adhérence de l'ensemble des points où $f$ est non nulle :
> $$\text{supp}(f) = \overline{\{ x \in \mathbb{R}^n \mid f(x) \neq 0 \}}$$
> Une fonction est dite à **support compact** si son support est un sous-ensemble compact (fermé et borné) de $\mathbb{R}^n$.

**Exemple concret de calcul de support :**
Considérons la fonction en une dimension :
$f(x) = 1$ si $x \in ]-1, 1[$, et $f(x) = 0$ sinon.
L'ensemble des points où $f$ est non nulle est l'ouvert $]-1, 1[$.
L'adhérence de cet ouvert est le segment $[-1, 1]$.
Ainsi, $\text{supp}(f) = [-1, 1]$, qui est un compact (fermé et borné).

> **Définition 2 (Espace des fonctions tests $\mathcal{D}(\mathbb{R}^n)$) :**
> L'espace $\mathcal{D}(\mathbb{R}^n)$ (souvent noté $\mathcal{C}_c^\infty(\mathbb{R}^n)$) est l'espace vectoriel des fonctions $\phi : \mathbb{R}^n \to \mathbb{C}$ qui sont :
> 1. Infiniment dérivables (de classe $\mathcal{C}^\infty$).
> 2. À support compact.

Il n'est pas immédiat qu'il existe des fonctions non nulles dans $\mathcal{D}(\mathbb{R})$. Les polynômes, par exemple, sont $\mathcal{C}^\infty$ mais n'ont jamais un support compact (sauf le polynôme nul).

**Exemple fondamental de fonction test (la fonction plateau) :**
Soit $\phi(x) = \exp\left(-\frac{1}{1-x^2}\right)$ pour $|x| < 1$, et $\phi(x) = 0$ pour $|x| \ge 1$.
Cette fonction est infiniment dérivable sur tout $\mathbb{R}$ (en particulier en $-1$ et en $1$, car toutes ses dérivées tendent vers $0$) et son support est $[-1, 1]$, qui est compact. Ainsi, $\phi \in \mathcal{D}(\mathbb{R})$.

Avant de définir rigoureusement les distributions en tant que formes linéaires continues, nous devons définir la notion de convergence sur l'espace $\mathcal{D}(\mathbb{R}^n)$.

> **Définition 3 (Convergence dans $\mathcal{D}$) :**
> Une suite $(\phi_j)_{j \in \mathbb{N}}$ de fonctions de $\mathcal{D}(\mathbb{R}^n)$ converge vers une fonction $\phi \in \mathcal{D}(\mathbb{R}^n)$ si :
> 1. Il existe un compact fixe $K \subset \mathbb{R}^n$ tel que, pour tout $j \in \mathbb{N}$, $\text{supp}(\phi_j) \subset K$ et $\text{supp}(\phi) \subset K$.
> 2. Pour tout multi-indice $\alpha$, la suite des dérivées partielles $\left( \partial^\alpha \phi_j \right)$ converge uniformément vers $\partial^\alpha \phi$ sur $K$.

> **Définition 4 (Distribution de Schwartz) :**
> Une **distribution** sur $\mathbb{R}^n$ est une forme linéaire $T$ sur l'espace vectoriel $\mathcal{D}(\mathbb{R}^n)$, c'est-à-dire une application $T : \mathcal{D}(\mathbb{R}^n) \to \mathbb{C}$ telle que :
> 1. **Linéarité :** $\forall \phi, \psi \in \mathcal{D}$, $\forall \lambda, \mu \in \mathbb{C}$, $T(\lambda \phi + \mu \psi) = \lambda T(\phi) + \mu T(\psi)$.
> 2. **Continuité séquentielle :** Pour toute suite $(\phi_j)$ convergeant vers $0$ dans $\mathcal{D}$, on a $\lim_{j \to +\infty} T(\phi_j) = 0$.
> L'ensemble de toutes les distributions sur $\mathbb{R}^n$ est noté $\mathcal{D}'(\mathbb{R}^n)$. L'action d'une distribution $T$ sur une fonction test $\phi$ s'écrit souvent sous forme de crochet de dualité : $\langle T, \phi \rangle$.

**Exemple 1 : La distribution de Dirac (Distribution singulière)**
Soit $a \in \mathbb{R}^n$. On définit l'application $\delta_a : \mathcal{D}(\mathbb{R}^n) \to \mathbb{C}$ par :
$$\langle \delta_a, \phi \rangle = \phi(a)$$
Montrons que c'est une distribution.
- Linéarité : $\langle \delta_a, \lambda \phi + \mu \psi \rangle = (\lambda \phi + \mu \psi)(a) = \lambda \phi(a) + \mu \psi(a) = \lambda \langle \delta_a, \phi \rangle + \mu \langle \delta_a, \psi \rangle$.
- Continuité : Si $\phi_j \to 0$ dans $\mathcal{D}$, cela implique la convergence uniforme (en particulier ponctuelle) vers $0$, donc $\phi_j(a) \to 0$, d'où $\langle \delta_a, \phi_j \rangle \to 0$.
Ainsi, $\delta_a \in \mathcal{D}'(\mathbb{R}^n)$.

**Exemple 2 : Distributions régulières (généralisation des fonctions)**
Soit $f \in L^1_{loc}(\mathbb{R}^n)$, c'est-à-dire une fonction localement intégrable (son intégrale de Lebesgue est finie sur tout compact de $\mathbb{R}^n$). On lui associe $T_f$ par :
$$\langle T_f, \phi \rangle = \int_{\mathbb{R}^n} f(x) \phi(x) dx$$
- Linéarité : par la linéarité de l'intégrale.
- Continuité : Soit $\phi_j \to 0$ dans $\mathcal{D}$. Toutes les $\phi_j$ ont leur support inclus dans un compact $K$. Alors,
  $$\left| \langle T_f, \phi_j \rangle \right| \le \int_K |f(x)| |\phi_j(x)| dx \le \|\phi_j\|_{\infty, K} \int_K |f(x)| dx$$
  Or, la convergence uniforme implique $\|\phi_j\|_{\infty, K} \to 0$, et comme $f \in L^1_{loc}$, l'intégrale sur $K$ est finie. Donc $\langle T_f, \phi_j \rangle \to 0$.
Toute fonction (assez régulière) peut donc être identifiée à une distribution.

> **Définition 5 (Convergence au sens des distributions) :**
> Une suite de distributions $(T_j)_{j \in \mathbb{N}}$ de $\mathcal{D}'(\mathbb{R}^n)$ converge vers une distribution $T \in \mathcal{D}'(\mathbb{R}^n)$ si, pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R}^n)$ :
> $$\lim_{j \to +\infty} \langle T_j, \phi \rangle = \langle T, \phi \rangle$$
> C'est une convergence simple (dite convergence faible-*).

**Exemple 3 : Convergence vers le Dirac**
Posons la fonction porte (illustrée en Figure 1) : $f_j(x) = j$ si $x \in [-1/(2j), 1/(2j)]$ et $f_j(x) = 0$ sinon.
Calculons l'action de $T_{f_j}$ sur une fonction test $\phi \in \mathcal{D}(\mathbb{R})$ :
$$\langle T_{f_j}, \phi \rangle = \int_{\mathbb{R}} f_j(x)\phi(x) dx = j \int_{-1/(2j)}^{1/(2j)} \phi(x) dx$$
Par le théorème de la moyenne pour les intégrales, il existe $c_j \in [-1/(2j), 1/(2j)]$ tel que l'intégrale vaut la largeur du domaine $(1/j)$ multipliée par la valeur au point $c_j$.
$$\langle T_{f_j}, \phi \rangle = j \times \left( \frac{1}{j} \phi(c_j) \right) = \phi(c_j)$$
Lorsque $j \to +\infty$, l'intervalle se resserre vers $0$, donc $c_j \to 0$. Puisque $\phi$ est continue en $0$, $\phi(c_j) \to \phi(0) = \langle \delta_0, \phi \rangle$.
Ainsi, au sens des distributions, $\lim_{j \to +\infty} T_{f_j} = \delta_0$.

**Exemple 4 : La Valeur Principale de Cauchy**
La fonction $x \mapsto 1/x$ n'est pas localement intégrable autour de $0$, elle ne définit donc pas une distribution régulière. On peut définir une distribution singulière appelée "Valeur principale", notée $\text{vp}(1/x)$, par la limite d'intégrales évitant la singularité :
$$\langle \text{vp}\left(\frac{1}{x}\right), \phi \rangle = \lim_{\epsilon \to 0^+} \int_{|x| > \epsilon} \frac{\phi(x)}{x} dx$$

## 3. Démonstrations

### Proposition : Le Dirac n'est pas une distribution régulière
Nous allons démontrer de manière exhaustive, par l'absurde, qu'il n'existe aucune fonction $f \in L^1_{loc}(\mathbb{R})$ qui puisse représenter la distribution de Dirac $\delta_0$.

**Démonstration :**
Supposons par l'absurde qu'il existe une fonction $f \in L^1_{loc}(\mathbb{R})$ telle que $T_f = \delta_0$, ce qui signifie que pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$, nous avons :
$$\int_{-\infty}^{+\infty} f(x) \phi(x) dx = \phi(0)$$

Étape 1 : Construction d'une suite de fonctions tests appropriée.
Considérons une fonction test "bosse" standard, notée $\theta \in \mathcal{D}(\mathbb{R})$, possédant les propriétés suivantes :
- $0 \le \theta(x) \le 1$ pour tout $x \in \mathbb{R}$.
- $\theta(0) = 1$.
- $\text{supp}(\theta) \subset [-1, 1]$.
À partir de $\theta$, nous construisons une suite de fonctions tests concentrées autour de $0$ :
$$\phi_j(x) = \theta(jx)$$
Vérifions les propriétés de $\phi_j$ :
- $\phi_j \in \mathcal{D}(\mathbb{R})$ car la composition par une dilatation conserve le caractère $\mathcal{C}^\infty$ et le support compact.
- $\phi_j(0) = \theta(0) = 1$ pour tout $j$.
- Le support de $\phi_j$ est l'ensemble des points $x$ tels que $jx \in [-1, 1]$, soit $x \in [-1/j, 1/j]$.

Étape 2 : Évaluation des deux membres de notre égalité hypothétique pour $\phi_j$.
D'une part, puisque $T_f = \delta_0$, on a par définition de l'action de $\delta_0$ sur $\phi_j$ :
$$\langle \delta_0, \phi_j \rangle = \phi_j(0) = 1$$
Et ceci est strictement égal à 1 pour tout entier $j \ge 1$.

D'autre part, en utilisant la forme intégrale avec notre fonction $f \in L^1_{loc}(\mathbb{R})$ :
$$\langle T_f, \phi_j \rangle = \int_{-\infty}^{+\infty} f(x) \phi_j(x) dx = \int_{-1/j}^{1/j} f(x) \phi_j(x) dx$$
(Puisque $\phi_j(x) = 0$ en dehors de $[-1/j, 1/j]$).

Prenons la valeur absolue de cette intégrale et majorons-la :
$$\left| \int_{-1/j}^{1/j} f(x) \phi_j(x) dx \right| \le \int_{-1/j}^{1/j} |f(x)| |\phi_j(x)| dx$$
Étant donné que $0 \le \phi_j(x) \le 1$ pour tout $x$, on peut majorer par :
$$\left| \langle T_f, \phi_j \rangle \right| \le \int_{-1/j}^{1/j} |f(x)| dx$$

Étape 3 : Passage à la limite quand $j \to +\infty$.
La fonction $f$ étant localement intégrable, la fonction $|f|$ est une fonction positive dont l'intégrale sur le compact $[-1, 1]$ est finie.
Par le théorème de continuité absolue de l'intégrale de Lebesgue, si on intègre une telle fonction sur un domaine dont la mesure de Lebesgue tend vers $0$, la valeur de l'intégrale tend vers $0$.
Ici, l'intervalle d'intégration est $[-1/j, 1/j]$, dont la mesure (la longueur) est $2/j$, qui tend rigoureusement vers $0$ lorsque $j \to +\infty$.
Par conséquent :
$$\lim_{j \to +\infty} \int_{-1/j}^{1/j} |f(x)| dx = 0$$
Ce qui implique :
$$\lim_{j \to +\infty} \langle T_f, \phi_j \rangle = 0$$

Étape 4 : Conclusion.
Nous avons obtenu, par la représentation intégrale, une limite valant $0$. Mais par définition de l'égalité supposée avec $\delta_0$, cette même quantité devait valoir exactement $1$ pour tout $j$. Nous obtenons $0 = 1$, ce qui est une contradiction manifeste. L'hypothèse de départ est fausse : la masse de Dirac ne peut pas être représentée par une fonction localement intégrable. C'est un objet mathématique intrinsèquement différent, une "distribution singulière". $\blacksquare$

## 4. Applications en Intelligence Artificielle

En intelligence artificielle, et plus particulièrement en apprentissage statistique (Machine Learning), la théorie des distributions intervient de manière structurelle, bien que souvent implicite dans l'écriture des équations au quotidien.

**Modélisation des densités de probabilité empiriques :**
Lorsqu'un réseau de neurones est entraîné par apprentissage supervisé, le jeu de données d'entraînement est constitué d'un ensemble fini de couples $(x_i, y_i)$. La distribution sous-jacente des données génératrices n'est pas connue. L'algorithme d'optimisation (par exemple la descente de gradient stochastique) tente de minimiser l'espérance de la perte (le risque réel) définie formellement par rapport à une mesure de probabilité $P$ :
$$R(w) = \int \mathcal{L}(f_w(x), y) dP(x,y)$$
Mais $P$ étant inconnue, on approxime cette intégrale par l'espérance sur une mesure empirique $\hat{P}$, qui est une combinaison convexe de distributions de Dirac centrées sur les points d'entraînement :
$$\hat{P} = \frac{1}{N} \sum_{i=1}^N \delta_{(x_i, y_i)}$$
La mesure de probabilité empirique est donc une distribution au sens de Schwartz. Son action sur la fonction de perte $\mathcal{L}$ (agissant comme la "fonction test" dans ce contexte d'intégration de Lebesgue généralisée) redonne bien la moyenne arithmétique de la perte sur l'échantillon, le risque empirique que l'on minimise effectivement.

**Calcul des gradients aux singularités :**
Les fonctions d'activation modernes, telles que le ReLU ($f(x) = \max(0, x)$), présentent des points de non-dérivabilité classique (en $0$). Les algorithmes de rétropropagation calculent implicitement des dérivées au sens des distributions. La dérivée d'une fonction échelon (de Heaviside) est rigoureusement définie dans le cadre des distributions comme étant la distribution de Dirac. L'élargissement de l'espace des fonctions aux distributions est la fondation théorique autorisant le succès massif des réseaux profonds non lisses optimisés par sous-gradients.
