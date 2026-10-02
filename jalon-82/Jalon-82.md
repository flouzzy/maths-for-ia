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

# Introduction aux distributions de Schwartz

## Introduction historique et conceptuelle

La théorie des distributions a été formellement introduite par le mathématicien français Laurent Schwartz au milieu du vingtième siècle. Elle a été motivée par des problèmes physiques concrets que l'analyse classique peinait à formaliser rigoureusement. En particulier, la description d'une charge électrique ponctuelle, d'une force d'impact instantanée ou d'un dipôle nécessitait des objets mathématiques plus généraux que les fonctions classiques, qui associent à chaque point de l'espace une valeur finie.

L'approche de Schwartz, influencée par les travaux antérieurs de Sergueï Sobolev en Union Soviétique et de Paul Dirac en physique quantique, repose sur un changement de perspective fondamental : au lieu d'étudier un objet mathématique par ses valeurs ponctuelles (ce qui n'a pas toujours de sens), on l'étudie par son "effet" sur une classe de fonctions très régulières, appelées "fonctions tests". Cette idée de la dualité, issue de l'analyse fonctionnelle, permet d'étendre la notion de dérivée à des fonctions qui ne sont pas différentiables au sens usuel.

## L'espace des fonctions tests

Pour définir rigoureusement les distributions, nous devons d'abord construire l'espace des fonctions tests, qui serviront de "sondes" ou de "mesures" pour nos nouveaux objets.

**Définition (Support d'une fonction) :** Soit $\phi : \mathbb{R} \to \mathbb{C}$ une fonction continue. Le support de $\phi$, noté $\text{supp}(\phi)$, est l'adhérence de l'ensemble des points où $\phi$ ne s'annule pas :
$$\text{supp}(\phi) = \overline{\{ x \in \mathbb{R} \mid \phi(x) \neq 0 \}}$$

**Définition (Espace des fonctions tests $\mathcal{D}(\mathbb{R})$) :** L'espace $\mathcal{D}(\mathbb{R})$, également noté $C_c^\infty(\mathbb{R})$, est l'espace vectoriel des fonctions $\phi : \mathbb{R} \to \mathbb{C}$ indéfiniment dérivables ($C^\infty$) et à support compact.

**Exemple 1 : La fonction "bosse" (bump function) standard.**
Un exemple fondamental d'une fonction dans $\mathcal{D}(\mathbb{R})$ est la fonction $\phi_0$ définie par :
$$
\phi_0(x) =
\begin{cases}
e^{-\frac{1}{1-x^2}} & \text{si } |x| < 1 \\
0 & \text{si } |x| \ge 1
\end{cases}
$$
Vérifions que $\phi_0 \in \mathcal{D}(\mathbb{R})$.
1. Le support de $\phi_0$ est clairement l'intervalle compact $[-1, 1]$.
2. Pour $|x| < 1$, $\phi_0$ est la composée de fonctions $C^\infty$, donc elle est $C^\infty$.
3. Le seul point délicat est la régularité aux bords, en $x=1$ et $x=-1$. Montrons que toutes les dérivées à gauche en $x=1$ s'annulent.
   Posons $u = \frac{1}{1-x^2}$. Lorsque $x \to 1^-$, $u \to +\infty$.
   Pour $x \in (-1, 1)$, la dérivée de $\phi_0$ est :
   $\phi_0'(x) = e^{-u} \cdot \left(- \frac{-2x}{(1-x^2)^2}\right) = \frac{-2x}{(1-x^2)^2} e^{-\frac{1}{1-x^2}} = -2x u^2 e^{-u}$.
   Lorsque $x \to 1^-$, $u \to +\infty$, et par croissance comparée, $u^2 e^{-u} \to 0$. Donc $\lim_{x \to 1^-} \phi_0'(x) = 0$.
   Par une récurrence immédiate, on peut montrer que pour tout entier $k \ge 1$, la dérivée d'ordre $k$ est de la forme $\phi_0^{(k)}(x) = P_k(x, u) e^{-u}$ où $P_k$ est un polynôme. Ainsi, $\lim_{x \to 1^-} \phi_0^{(k)}(x) = 0$.
   Toutes les dérivées coïncident avec celles de la fonction identiquement nulle à droite de $x=1$. La fonction $\phi_0$ est donc de classe $C^\infty$ sur $\mathbb{R}$.

\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Axes
    \draw[->, thick] (-2, 0) -- (2, 0) node[right] {$x$};
    \draw[->, thick] (0, -0.2) -- (0, 1.2) node[above] {$y$};

    % Ticks
    \draw[thick] (-1, 0.05) -- (-1, -0.05) node[below] {$-1$};
    \draw[thick] (1, 0.05) -- (1, -0.05) node[below] {$1$};
    \draw[thick] (0.05, 1) -- (-0.05, 1) node[left] {$1$};

    % The bump function graph
    \draw[domain=-0.999:0.999, smooth, variable=\x, blue, thick] plot ({\x}, {exp(-1/(1-\x*\x))/exp(-1)});

    % Zero parts
    \draw[blue, thick] (-2, 0) -- (-1, 0);
    \draw[blue, thick] (1, 0) -- (2, 0);

    % Labels
    \node[blue] at (1.2, 0.5) {$\phi_0(x)$};
\end{tikzpicture}
\end{center}

## Notion de convergence dans $\mathcal{D}(\mathbb{R})$

Pour définir une distribution comme une forme linéaire continue, il faut préciser la topologie de $\mathcal{D}(\mathbb{R})$. Nous définirons ici la continuité de manière séquentielle.

**Définition (Convergence dans $\mathcal{D}(\mathbb{R})$) :** On dit qu'une suite $(\phi_n)_{n \in \mathbb{N}}$ de fonctions de $\mathcal{D}(\mathbb{R})$ converge vers $\phi \in \mathcal{D}(\mathbb{R})$ (et on note $\phi_n \xrightarrow{\mathcal{D}} \phi$) si les deux conditions suivantes sont vérifiées :
1. **Support commun borné :** Il existe un compact $K \subset \mathbb{R}$ tel que pour tout $n \in \mathbb{N}$, $\text{supp}(\phi_n) \subset K$ et $\text{supp}(\phi) \subset K$.
2. **Convergence uniforme de toutes les dérivées :** Pour tout entier $k \ge 0$, la suite des dérivées $(\phi_n^{(k)})_{n \in \mathbb{N}}$ converge uniformément vers $\phi^{(k)}$ sur $K$ :
   $$\lim_{n \to +\infty} \sup_{x \in K} |\phi_n^{(k)}(x) - \phi^{(k)}(x)| = 0$$

**Exemple 2 : Une suite convergente dans $\mathcal{D}(\mathbb{R})$.**
Soit $\phi_0$ la fonction bosse définie dans l'Exemple 1. Considérons la suite de fonctions $\phi_n(x) = \frac{1}{n} \phi_0(x)$.
1. Pour tout $n \ge 1$, $\text{supp}(\phi_n) = \text{supp}(\phi_0) = [-1, 1]$. La condition du support commun est vérifiée avec $K = [-1, 1]$.
2. Pour un entier $k \ge 0$ fixé, $\phi_n^{(k)}(x) = \frac{1}{n} \phi_0^{(k)}(x)$. Comme $\phi_0^{(k)}$ est continue sur le compact $[-1, 1]$, elle est bornée. Posons $M_k = \sup_{x \in [-1, 1]} |\phi_0^{(k)}(x)|$.
   Alors $\sup_{x \in [-1, 1]} |\phi_n^{(k)}(x) - 0| = \frac{M_k}{n}$, qui tend vers $0$ lorsque $n \to +\infty$.
Ainsi, $\phi_n \xrightarrow{\mathcal{D}} 0$.

**Exemple 3 : Une suite ne convergeant PAS dans $\mathcal{D}(\mathbb{R})$ malgré une convergence uniforme.**
Considérons $\phi_n(x) = \frac{1}{n} \phi_0\left(\frac{x}{n}\right)$.
La fonction $\phi_n$ tend uniformément vers $0$, ainsi que toutes ses dérivées.
Cependant, $\text{supp}(\phi_n) = [-n, n]$. Il n'existe aucun compact $K$ tel que tous les supports y soient inclus pour tout $n$.
Ainsi, la suite $(\phi_n)_{n \in \mathbb{N}}$ ne converge pas vers la fonction nulle au sens de la topologie de $\mathcal{D}(\mathbb{R})$.

## Définition des distributions

Nous sommes maintenant en mesure de définir rigoureusement ce qu'est une distribution.

**Définition (Distribution) :** Une distribution $T$ sur $\mathbb{R}$ est une forme linéaire continue sur l'espace des fonctions tests $\mathcal{D}(\mathbb{R})$.
L'ensemble des distributions sur $\mathbb{R}$ est noté $\mathcal{D}'(\mathbb{R})$.
Cela signifie que $T$ vérifie les deux conditions suivantes :
1. **Linéarité :** Pour tous $\alpha, \beta \in \mathbb{C}$ et pour toutes $\phi, \psi \in \mathcal{D}(\mathbb{R})$,
   $$T(\alpha \phi + \beta \psi) = \alpha T(\phi) + \beta T(\psi)$$
2. **Continuité séquentielle :** Si $(\phi_n)_{n \in \mathbb{N}}$ est une suite dans $\mathcal{D}(\mathbb{R})$ telle que $\phi_n \xrightarrow{\mathcal{D}} \phi$, alors
   $$\lim_{n \to +\infty} T(\phi_n) = T(\phi)$$

*Notation :* On utilise couramment la notation en crochet de dualité : $\langle T, \phi \rangle$ au lieu de $T(\phi)$.

## Distributions régulières associées aux fonctions

Le concept de distribution doit généraliser la notion de fonction. Nous allons voir comment "plonger" les fonctions classiques dans l'espace des distributions.

**Définition (Fonction localement intégrable) :** Une fonction $f : \mathbb{R} \to \mathbb{C}$ (mesurable) est dite localement intégrable si, pour tout compact $K \subset \mathbb{R}$, l'intégrale de Lebesgue $\int_K |f(x)| \, dx$ est finie.
L'espace de ces fonctions est noté $L^1_{\text{loc}}(\mathbb{R})$.

**Théorème 1 (Distribution régulière) :** Toute fonction $f \in L^1_{\text{loc}}(\mathbb{R})$ définit une distribution, notée $T_f$, par l'action suivante :
Pour toute $\phi \in \mathcal{D}(\mathbb{R})$,
$$\langle T_f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) \, dx$$

*Démonstration :*
Vérifions d'abord que l'intégrale est bien définie. Soit $\phi \in \mathcal{D}(\mathbb{R})$ et $K = \text{supp}(\phi)$. L'intégrale se réduit à $\int_K f(x) \phi(x) \, dx$.
La fonction $\phi$ est continue sur le compact $K$, donc elle est bornée par une constante $M$.
$$ \left| \int_K f(x) \phi(x) \, dx \right| \le \int_K |f(x)| |\phi(x)| \, dx \le M \int_K |f(x)| \, dx < +\infty $$
car $f \in L^1_{\text{loc}}(\mathbb{R})$. La forme $T_f$ est donc bien définie à valeurs dans $\mathbb{C}$.

1. **Linéarité :** Elle découle de la linéarité de l'intégrale.
   $$ \langle T_f, \alpha \phi + \beta \psi \rangle = \int_{\mathbb{R}} f(x) (\alpha \phi(x) + \beta \psi(x)) \, dx = \alpha \langle T_f, \phi \rangle + \beta \langle T_f, \psi \rangle $$
2. **Continuité :** Soit $(\phi_n)$ une suite convergeant vers $0$ dans $\mathcal{D}(\mathbb{R})$.
   Il existe un compact $K$ tel que $\text{supp}(\phi_n) \subset K$ pour tout $n$, et la suite converge uniformément vers $0$ sur $K$.
   $$ |\langle T_f, \phi_n \rangle| = \left| \int_K f(x) \phi_n(x) \, dx \right| \le \left( \sup_{x \in K} |\phi_n(x)| \right) \int_K |f(x)| \, dx $$
   Puisque $\phi_n$ tend uniformément vers $0$, $\sup_{x \in K} |\phi_n(x)|$ tend vers $0$.
   L'intégrale $\int_K |f(x)| \, dx$ est une constante finie. Donc $\lim_{n \to \infty} \langle T_f, \phi_n \rangle = 0$.
   $T_f$ est bien une distribution.
$\blacksquare$

**Remarque :** L'application $f \mapsto T_f$ est linéaire et injective (presque partout). Ainsi, on identifie souvent $f$ et $T_f$. On écrira alors $\langle f, \phi \rangle$ au lieu de $\langle T_f, \phi \rangle$.

**Exemple 4 : La distribution de Heaviside.**
La fonction de Heaviside $H$, définie par $H(x) = 1$ si $x \ge 0$ et $H(x) = 0$ si $x < 0$, est localement intégrable (car bornée).
Elle définit la distribution régulière $T_H$ :
$$ \langle T_H, \phi \rangle = \int_{-\infty}^{+\infty} H(x) \phi(x) \, dx = \int_0^{+\infty} \phi(x) \, dx $$
Calculons l'action de $T_H$ sur notre fonction bosse $\phi_0$ (Exemple 1) :
L'intégrale $\int_0^{+\infty} \phi_0(x) \, dx$ représente l'aire sous la moitié droite de la courbe, ce qui est un nombre réel positif bien défini, bien qu'il n'ait pas d'expression fermée simple à l'aide de fonctions élémentaires.

## Distributions singulières : l'exemple canonique de la masse de Dirac

Les distributions singulières sont des distributions qui ne peuvent pas s'écrire sous la forme d'une intégrale avec une fonction localement intégrable. L'exemple le plus fondamental est la masse de Dirac, notée $\delta_0$.

**Définition (Distribution de Dirac) :** La distribution de Dirac en un point $a \in \mathbb{R}$, notée $\delta_a$, est définie par son action sur une fonction test $\phi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle \delta_a, \phi \rangle = \phi(a) $$

**Exemple 5 : Preuve que $\delta_a$ est une distribution.**
1. L'application $\phi \mapsto \phi(a)$ est trivialement linéaire.
2. Pour la continuité, soit $(\phi_n)$ convergeant vers $0$ dans $\mathcal{D}(\mathbb{R})$.
   La convergence de $(\phi_n)$ vers $0$ implique la convergence uniforme (donc ponctuelle) vers $0$.
   Ainsi, $\langle \delta_a, \phi_n \rangle = \phi_n(a) \to 0$ lorsque $n \to +\infty$.
   $\delta_a$ est donc bien une distribution.

**Exemple 6 : Calculs avec des Diracs.**
Calculons l'action de différentes distributions sur une fonction test $\phi(x) = e^{-x^2} \sin(x)$ (remarquez que $\phi$ n'est pas à support compact, mais en physique on autorise souvent une plus grande classe de fonctions tests comme la classe de Schwartz $\mathcal{S}(\mathbb{R})$ ; pour cet exemple nous restreignons implicitement $\phi$ à un support compact très grand).
- Action de $\delta_0$ sur $\phi$ : $\langle \delta_0, \phi \rangle = \phi(0) = e^0 \sin(0) = 0$.
- Action de $\delta_{\pi/2}$ sur $\phi$ : $\langle \delta_{\pi/2}, \phi \rangle = \phi(\pi/2) = e^{-(\pi/2)^2} \sin(\pi/2) = e^{-\pi^2/4}$.
- Considérons $T = 3\delta_0 - 2\delta_\pi$. $T \in \mathcal{D}'(\mathbb{R})$ par combinaison linéaire.
  $\langle T, \phi \rangle = 3\langle \delta_0, \phi \rangle - 2\langle \delta_\pi, \phi \rangle = 3\phi(0) - 2\phi(\pi) = 3(0) - 2(0) = 0$.

**Théorème 2 :** La distribution de Dirac $\delta_0$ n'est pas une distribution régulière. Autrement dit, il n'existe aucune fonction localement intégrable $f$ telle que pour toute $\phi \in \mathcal{D}(\mathbb{R})$, $\int_{-\infty}^{+\infty} f(x)\phi(x) \, dx = \phi(0)$.

*Démonstration :*
Supposons par l'absurde qu'une telle fonction $f \in L^1_{\text{loc}}(\mathbb{R})$ existe.
Considérons une fonction test $\psi \in \mathcal{D}(\mathbb{R})$ telle que $\psi(x) = 1$ pour $|x| \le 1$, $\psi(x) = 0$ pour $|x| \ge 2$, et $0 \le \psi(x) \le 1$ partout.
Pour $n \ge 1$, définissons la suite de fonctions tests $\phi_n(x) = \psi(nx)$.
Le support de $\phi_n$ est $\left[-\frac{2}{n}, \frac{2}{n}\right]$. De plus, $\phi_n(0) = \psi(0) = 1$.
Par hypothèse, nous aurions :
$$ \phi_n(0) = \int_{-\infty}^{+\infty} f(x) \phi_n(x) \, dx $$
Donc :
$$ 1 = \int_{-\frac{2}{n}}^{\frac{2}{n}} f(x) \phi_n(x) \, dx $$
En prenant la valeur absolue :
$$ 1 = \left| \int_{-\frac{2}{n}}^{\frac{2}{n}} f(x) \phi_n(x) \, dx \right| \le \int_{-\frac{2}{n}}^{\frac{2}{n}} |f(x)| |\phi_n(x)| \, dx \le \int_{-\frac{2}{n}}^{\frac{2}{n}} |f(x)| \, dx $$
car $0 \le \phi_n(x) \le 1$.
Puisque $f \in L^1_{\text{loc}}(\mathbb{R})$, $f$ est intégrable sur le segment $[-2, 2]$.
La mesure de Lebesgue de l'intervalle $\left[-\frac{2}{n}, \frac{2}{n}\right]$ tend vers 0 lorsque $n \to +\infty$.
Par le théorème de convergence dominée (ou la continuité absolue de l'intégrale de Lebesgue), on a :
$$ \lim_{n \to +\infty} \int_{-\frac{2}{n}}^{\frac{2}{n}} |f(x)| \, dx = 0 $$
Nous obtenons alors $1 \le 0$, ce qui est une contradiction manifeste.
Par conséquent, une telle fonction $f$ n'existe pas. La masse de Dirac $\delta_0$ est véritablement une distribution singulière.
$\blacksquare$

\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Axes
    \draw[->, thick] (-2, 0) -- (2, 0) node[right] {$x$};
    \draw[->, thick] (0, -0.2) -- (0, 2) node[above] {$\phi_n(x)$};

    % The function psi for n=1
    \draw[domain=1:2, smooth, variable=\x, blue, thick] plot ({\x}, {cos((\x-1)*90)^2});
    \draw[domain=-2:-1, smooth, variable=\x, blue, thick] plot ({\x}, {cos((-\x-1)*90)^2});
    \draw[blue, thick] (-1, 1) -- (1, 1);
    \draw[blue, thick] (-2.5, 0) -- (-2, 0);
    \draw[blue, thick] (2, 0) -- (2.5, 0);

    % The function phi_n for n=2
    \draw[domain=0.5:1, smooth, variable=\x, red, thick] plot ({\x}, {cos((\x*2-1)*90)^2});
    \draw[domain=-1:-0.5, smooth, variable=\x, red, thick] plot ({\x}, {cos((-\x*2-1)*90)^2});
    \draw[red, thick] (-0.5, 1) -- (0.5, 1);

    % The function phi_n for n=4
    \draw[domain=0.25:0.5, smooth, variable=\x, green!70!black, thick] plot ({\x}, {cos((\x*4-1)*90)^2});
    \draw[domain=-0.5:-0.25, smooth, variable=\x, green!70!black, thick] plot ({\x}, {cos((-\x*4-1)*90)^2});
    \draw[green!70!black, thick] (-0.25, 1) -- (0.25, 1);

    % Labels
    \node[blue] at (1.5, 1.2) {$n=1$};
    \node[red] at (0.7, 1.2) {$n=2$};
    \node[green!70!black] at (0.3, 1.2) {$n=4$};

    \node[below] at (2,0) {$2$};
    \node[below] at (-2,0) {$-2$};
\end{tikzpicture}
\end{center}

## Ordre d'une distribution

Les distributions sont des formes linéaires continues sur $\mathcal{D}(\mathbb{R})$. On peut quantifier cette continuité à travers la notion d'ordre.

**Définition (Distribution d'ordre $k$) :** Soit $T \in \mathcal{D}'(\mathbb{R})$. On dit que $T$ est d'ordre $k$ (où $k \in \mathbb{N}$) si pour tout compact $K \subset \mathbb{R}$, il existe une constante $C_K \ge 0$ telle que pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$ dont le support est inclus dans $K$ :
$$ |\langle T, \phi \rangle| \le C_K \sum_{j=0}^k \sup_{x \in K} |\phi^{(j)}(x)| $$
L'ordre d'une distribution $T$ est le plus petit entier $k$ vérifiant cette propriété. Si aucun tel entier n'existe, la distribution est dite d'ordre infini.

**Exemple 7 : Ordre de $T_f$ pour $f \in L^1_{\text{loc}}$.**
Pour une distribution régulière $T_f$, si le support de $\phi$ est dans $K$ :
$$ |\langle T_f, \phi \rangle| = \left| \int_K f(x) \phi(x) \, dx \right| \le \left( \sup_{x \in K} |\phi(x)| \right) \int_K |f(x)| \, dx = C_K \sup_{x \in K} |\phi(x)| $$
avec $C_K = \int_K |f(x)| \, dx$.
Ici $k=0$. Toute distribution régulière associée à une fonction localement intégrable est d'ordre $0$.

**Exemple 8 : Ordre de la distribution de Dirac $\delta_a$.**
Pour $\phi$ à support dans $K$ :
$$ |\langle \delta_a, \phi \rangle| = |\phi(a)| $$
Si $a \in K$, on a $|\phi(a)| \le \sup_{x \in K} |\phi(x)|$. La constante est $C_K = 1$.
Si $a \notin K$, $\phi(a) = 0$ et l'inégalité est trivialement vérifiée avec $C_K = 0$.
Ainsi, l'inégalité est vérifiée pour $k=0$. La distribution de Dirac est donc d'ordre $0$.

**Exemple 9 : Une distribution d'ordre 1.**
La forme linéaire définie par $T(\phi) = \phi'(0)$ (la dérivée évaluée en 0) est une distribution.
Elle est d'ordre 1, car on a besoin de contrôler la norme infini de la première dérivée : $|\langle T, \phi \rangle| = |\phi'(0)| \le \sup_{x \in K} |\phi'(x)|$.
On ne peut pas borner $|\phi'(0)|$ uniquement en utilisant $\sup_{x \in K} |\phi(x)|$ car une fonction peut être très petite mais avoir une pente très raide en 0 (pensez à $\frac{1}{n}\sin(n^2 x)$). L'ordre est donc exactement 1.

## Applications en Intelligence Artificielle et Analyse de données

En modélisation et en apprentissage automatique, le formalisme des distributions intervient de façon sous-jacente dès qu'on manipule des probabilités discrètes ou continues dans un cadre unifié.

1. **Mesures empiriques :**
Lors de l'entraînement d'un réseau de neurones, on observe un ensemble fini de données d'apprentissage $\{x_1, \dots, x_N\}$. La véritable loi générative des données est inconnue. L'approximation naturelle est la mesure empirique, qui est une distribution :
$$ \hat{\mathbb{P}}_N = \frac{1}{N} \sum_{i=1}^N \delta_{x_i} $$
Cette distribution, somme de Diracs, s'intègre parfaitement dans le formalisme. Le risque empirique d'un modèle (la perte moyenne) est alors l'action de cette distribution sur la fonction de perte $L$ (vue comme fonction test sur l'espace des paramètres fixés) :
$$ \mathcal{R}_{\text{emp}} = \langle \hat{\mathbb{P}}_N, L \rangle = \frac{1}{N} \sum_{i=1}^N L(x_i) $$

2. **Densités non régulières en Probabilité :**
Les variables aléatoires discrètes n'ont pas de fonction de densité classique (au sens de Lebesgue). En utilisant la théorie des distributions, toute variable aléatoire $X$, qu'elle soit continue ou discrète, possède une densité "généralisée". Par exemple, une variable de Bernoulli $B \sim \mathcal{B}(p)$ possède la "densité" au sens des distributions $p \delta_1 + (1-p) \delta_0$. Cela permet d'unifier le calcul des espérances sous forme d'intégrales pour tous les types de variables aléatoires.
