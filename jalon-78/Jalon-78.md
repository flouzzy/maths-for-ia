---
uuid: "jalon-78"
title: "Séries de Fourier"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 77 (Densité des fonctions simples).md]]"
next: "[[Jalon 79 (Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.).md]]"
---

# Séries de Fourier

## 1. Introduction (Génèse historique et physique)

L'étude des séries de Fourier trouve ses racines profondes dans la compréhension des phénomènes physiques périodiques. À l'aube du XIXe siècle, Joseph Fourier, alors préoccupé par l'équation de la chaleur, fait une conjecture audacieuse : toute fonction périodique, même discontinue ou présentant des "sauts", peut s'écrire comme une somme infinie de fonctions trigonométriques simples (sinus et cosinus).

Cette idée fondamentale opère un changement de paradigme. Au lieu de considérer une fonction dans le domaine temporel (ou spatial) $f(t)$, Fourier propose de la regarder dans le "domaine fréquentiel", en analysant le "poids" de chaque fréquence dans la composition de $f$. C'est le passage d'une vision globale à une analyse spectrale.

Mathématiquement, pour une fonction $T$-périodique, l'objectif est de trouver des coefficients $a_n$ et $b_n$ tels que :
$$ f(t) \sim \frac{a_0}{2} + \sum_{n=1}^{+\infty} \left( a_n \cos\left(n \frac{2\pi}{T} t\right) + b_n \sin\left(n \frac{2\pi}{T} t\right) \right) $$

Cette décomposition, d'abord rejetée par des mathématiciens de renom comme Lagrange pour son manque de rigueur (les notions de convergence n'étaient pas encore formellement établies), est devenue un des piliers de l'analyse moderne, jetant les bases de la théorie des espaces de Hilbert et de la théorie de la mesure.

## 2. Définitions, Théorèmes et Exemples

Dans tout ce qui suit, on s'intéresse aux fonctions $2\pi$-périodiques, à valeurs réelles ou complexes. On note $T = 2\pi$ la période, et $\omega = \frac{2\pi}{T} = 1$ la pulsation fondamentale.

On note $L^1_{loc}(\mathbb{R})$ l'espace des fonctions localement intégrables. Soit $f : \mathbb{R} \to \mathbb{C}$ une fonction $2\pi$-périodique et localement intégrable (donc intégrable sur tout intervalle de longueur $2\pi$).

### A. Coefficients de Fourier

**Définition 1 (Coefficients exponentiels) :**
Pour tout entier relatif $n \in \mathbb{Z}$, le $n$-ième coefficient de Fourier exponentiel de $f$, noté $c_n(f)$, est défini par :
$$ c_n(f) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) e^{-int} dt $$
L'intégrale peut être calculée sur n'importe quel intervalle de longueur $2\pi$, par exemple $[0, 2\pi]$ ou $[-\pi, \pi]$.

**Définition 2 (Coefficients trigonométriques) :**
Si $f$ est à valeurs réelles, on définit pour tout $n \in \mathbb{N}$ les coefficients trigonométriques :
$$ a_n(f) = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \cos(nt) dt \quad \text{pour } n \ge 0 $$
$$ b_n(f) = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) dt \quad \text{pour } n \ge 1 $$
On a alors la relation : $c_n(f) = \frac{a_n(f) - i b_n(f)}{2}$ et $c_{-n}(f) = \frac{a_n(f) + i b_n(f)}{2}$. Le coefficient $a_0(f)$ est particulier : $\frac{a_0(f)}{2} = c_0(f) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) dt$ représente la valeur moyenne de $f$.

**Exemple concret 1 : Le signal carré**
Soit $f$ la fonction $2\pi$-périodique définie sur $]-\pi, \pi]$ par $f(t) = -1$ si $t \in ]-\pi, 0]$ et $f(t) = 1$ si $t \in ]0, \pi]$.
Calculons ses coefficients de Fourier trigonométriques.
- $f$ est impaire, donc pour tout $n \ge 0$, $a_n(f) = 0$.
- Pour $n \ge 1$, calculons $b_n(f)$ :
  $$ b_n(f) = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) dt = \frac{2}{\pi} \int_{0}^{\pi} \sin(nt) dt = \frac{2}{\pi} \left[ -\frac{\cos(nt)}{n} \right]_0^\pi $$
  $$ b_n(f) = \frac{2}{\pi} \frac{1 - \cos(n\pi)}{n} = \frac{2}{\pi} \frac{1 - (-1)^n}{n} $$
Si $n$ est pair ($n=2p$), $b_{2p} = 0$.
Si $n$ est impair ($n=2p+1$), $b_{2p+1} = \frac{4}{\pi(2p+1)}$.

### B. Convergence des Séries de Fourier

La série de Fourier de $f$ est la série de fonctions définie par $S_N(f)(t) = \sum_{n=-N}^{N} c_n(f) e^{int} = \frac{a_0(f)}{2} + \sum_{n=1}^{N} \left( a_n(f) \cos(nt) + b_n(f) \sin(nt) \right)$. La question fondamentale est de savoir si cette suite de sommes partielles converge vers $f(t)$.

**Théorème 1 (Lemme de Riemann-Lebesgue) :**
Si $f$ est une fonction intégrable sur $[a,b]$, alors :
$$ \lim_{|n| \to +\infty} \int_a^b f(t) e^{int} dt = 0 $$
En particulier, $c_n(f) \xrightarrow{|n|\to+\infty} 0$, et de même pour $a_n(f)$ et $b_n(f)$.

**Exemple concret 2 : Application du lemme**
Pour la fonction porte valant $1$ sur $[-\pi/2, \pi/2]$ et $0$ ailleurs sur $[-\pi, \pi]$, $c_n(f) = \frac{1}{2\pi} \int_{-\pi/2}^{\pi/2} e^{-int} dt = \frac{\sin(n\pi/2)}{n\pi}$ pour $n \neq 0$. On observe bien que $\lim_{|n| \to +\infty} \frac{\sin(n\pi/2)}{n\pi} = 0$, illustrant le fait que les hautes fréquences ont une contribution qui s'évanouit.

**Théorème 2 (Théorème de Dirichlet) :**
Soit $f$ une fonction $2\pi$-périodique. Si $f$ est continue par morceaux et continûment dérivable par morceaux (de classe $C^1$ par morceaux) sur $\mathbb{R}$, alors en tout point $t \in \mathbb{R}$, la série de Fourier de $f$ converge, et sa somme vaut la moyenne des limites à gauche et à droite de $f$ en $t$ :
$$ \lim_{N \to +\infty} S_N(f)(t) = \frac{f(t^+) + f(t^-)}{2} $$
En particulier, si $f$ est continue au point $t$, alors la série converge vers $f(t)$.

**Exemple concret 3 : Application de Dirichlet au signal carré**
Reprenons le signal carré $f$. $f$ est de classe $C^1$ par morceaux (dérivée nulle partout sauf aux points de discontinuité où elle n'est pas définie).
- En $t = \pi/2$, $f$ est continue et $f(\pi/2) = 1$. D'après Dirichlet :
  $$ 1 = \sum_{p=0}^{+\infty} b_{2p+1} \sin((2p+1)\frac{\pi}{2}) = \sum_{p=0}^{+\infty} \frac{4}{\pi(2p+1)} (-1)^p $$
  On retrouve ainsi la célèbre formule de Gregory-Leibniz : $\sum_{p=0}^{+\infty} \frac{(-1)^p}{2p+1} = \frac{\pi}{4}$.
- En $t = 0$, il y a discontinuité. La série converge vers $\frac{f(0^+) + f(0^-)}{2} = \frac{1 + (-1)}{2} = 0$, ce qui est cohérent car tous les termes en $\sin(0)$ sont nuls.

## 3. Démonstrations

### Démonstration du Lemme de Riemann-Lebesgue

**Étape 1 : Preuve pour les fonctions en escalier.**
Supposons d'abord que $f$ est l'indicatrice d'un intervalle $[\alpha, \beta] \subset [a,b]$.
$$ \int_a^b \mathbf{1}_{[\alpha, \beta]}(t) e^{int} dt = \int_\alpha^\beta e^{int} dt $$
Si $n \neq 0$, cette intégrale vaut :
$$ \left[ \frac{e^{int}}{in} \right]_\alpha^\beta = \frac{e^{in\beta} - e^{in\alpha}}{in} $$
En prenant le module, on a :
$$ \left| \int_a^b \mathbf{1}_{[\alpha, \beta]}(t) e^{int} dt \right| \le \frac{|e^{in\beta}| + |e^{in\alpha}|}{|n|} \le \frac{2}{|n|} $$
Cette quantité tend vers $0$ quand $|n| \to +\infty$.
Par linéarité de l'intégrale, ce résultat s'étend immédiatement à toute fonction en escalier sur $[a,b]$.

**Étape 2 : Extension par densité.**
Soit $f$ une fonction intégrable sur $[a,b]$. L'espace des fonctions en escalier est dense dans $L^1([a,b])$.
Ainsi, pour tout $\epsilon > 0$, il existe une fonction en escalier $\varphi$ telle que :
$$ \int_a^b |f(t) - \varphi(t)| dt < \frac{\epsilon}{2} $$
On écrit alors :
$$ \int_a^b f(t) e^{int} dt = \int_a^b (f(t) - \varphi(t)) e^{int} dt + \int_a^b \varphi(t) e^{int} dt $$
En passant aux valeurs absolues :
$$ \left| \int_a^b f(t) e^{int} dt \right| \le \int_a^b |f(t) - \varphi(t)| |e^{int}| dt + \left| \int_a^b \varphi(t) e^{int} dt \right| $$
Puisque $|e^{int}| = 1$ :
$$ \left| \int_a^b f(t) e^{int} dt \right| \le \frac{\epsilon}{2} + \left| \int_a^b \varphi(t) e^{int} dt \right| $$
D'après l'étape 1, puisque $\varphi$ est en escalier, il existe $N \in \mathbb{N}$ tel que pour tout $|n| \ge N$,
$$ \left| \int_a^b \varphi(t) e^{int} dt \right| < \frac{\epsilon}{2} $$
Pour tout $|n| \ge N$, on a donc $\left| \int_a^b f(t) e^{int} dt \right| < \epsilon$.
Ce qui achève la démonstration. $\blacksquare$

### Démonstration du Théorème de Dirichlet (Principe)

La démonstration complète s'appuie sur le noyau de Dirichlet.
**Étape 1 : Le noyau de Dirichlet.**
La somme partielle d'ordre $N$ s'écrit :
$$ S_N(f)(x) = \sum_{n=-N}^N c_n(f) e^{inx} = \sum_{n=-N}^N \left( \frac{1}{2\pi} \int_{-\pi}^\pi f(t) e^{-int} dt \right) e^{inx} $$
Par linéarité de l'intégrale :
$$ S_N(f)(x) = \frac{1}{2\pi} \int_{-\pi}^\pi f(t) \left( \sum_{n=-N}^N e^{in(x-t)} \right) dt $$
On pose $u = x-t$. Par périodicité, on peut intégrer sur $[-\pi, \pi]$ :
$$ S_N(f)(x) = \frac{1}{2\pi} \int_{-\pi}^\pi f(x-u) D_N(u) du $$
où $D_N(u) = \sum_{n=-N}^N e^{inu}$ est le noyau de Dirichlet.
En utilisant la somme d'une suite géométrique (pour $e^{iu} \neq 1$) :
$$ D_N(u) = e^{-iNu} \frac{1 - (e^{iu})^{2N+1}}{1 - e^{iu}} = \frac{e^{-iNu} - e^{i(N+1)u}}{e^{-iu/2} (e^{iu/2} - e^{-iu/2})} = \frac{e^{-i(N+1/2)u} - e^{i(N+1/2)u}}{e^{-iu/2} - e^{iu/2}} $$
$$ D_N(u) = \frac{\sin((N+\frac{1}{2})u)}{\sin(\frac{u}{2})} $$
On note également que $\frac{1}{2\pi} \int_{-\pi}^\pi D_N(u) du = \sum_{n=-N}^N \frac{1}{2\pi} \int_{-\pi}^\pi e^{inu} du = 1$.

**Étape 2 : L'expression de l'erreur.**
On veut montrer que $\lim_{N \to +\infty} \left( S_N(f)(x) - \frac{f(x^+) + f(x^-)}{2} \right) = 0$.
En séparant l'intégrale sur $[-\pi, 0]$ et $[0, \pi]$, et en utilisant l'intégrale valant 1 du noyau (et sa parité), on arrive à étudier l'intégrale :
$$ I_N = \frac{1}{2\pi} \int_0^\pi (f(x+u) - f(x^+)) \frac{\sin((N+1/2)u)}{\sin(u/2)} du $$
(et son analogue sur $[-\pi, 0]$ avec $f(x^-)$).
Puisque $f$ est $C^1$ par morceaux, le taux d'accroissement $\frac{f(x+u) - f(x^+)}{u}$ admet une limite finie quand $u \to 0^+$.
La fonction $g(u) = \frac{f(x+u) - f(x^+)}{\sin(u/2)}$ pour $u \in ]0, \pi]$ se prolonge continûment en $0$ car $\sin(u/2) \sim u/2$.
$g$ est donc continue par morceaux (et bornée) sur $]0, \pi]$, donc intégrable.
On applique alors le Lemme de Riemann-Lebesgue à la fonction intégrable $g$ sur $[0, \pi]$ :
$$ \lim_{N \to +\infty} \int_0^\pi g(u) \sin((N+1/2)u) du = 0 $$
Ainsi $I_N \to 0$. De même pour la partie gauche. Le théorème est démontré. $\blacksquare$



**Exemple concret 5 : Théorème de Parseval intuitif (Énergie)**
Bien que le théorème soit détaillé plus tard, illustrons-le : l'énergie totale d'un signal (intégrale de son carré) est la somme de l'énergie de ses harmoniques.
Pour le signal carré $f$, l'énergie moyenne est $\frac{1}{2\pi} \int_{-\pi}^\pi |f(t)|^2 dt = \frac{1}{2\pi} \int_{-\pi}^\pi 1 dt = 1$.
Les composantes sont $b_{2p+1} = \frac{4}{\pi(2p+1)}$. L'énergie des harmoniques est $\frac{1}{2} \sum b_n^2$.
Donc $\frac{1}{2} \sum_{p=0}^{+\infty} \frac{16}{\pi^2 (2p+1)^2} = 1 \implies \sum_{p=0}^{+\infty} \frac{1}{(2p+1)^2} = \frac{\pi^2}{8}$.
C'est la même valeur qu'on retrouve dans les exercices pour la fonction valeur absolue.


## 4. Applications en Physique, Logique et IA

### A. Traitement du Signal et IA (Feature Extraction)

Dans les architectures neuronales traitant le son ou les séries temporelles (comme certains Transformers ou CNN 1D), les séries de Fourier sous-tendent les transformations initiales. Les réseaux n'analysent pas toujours le signal brut temporel, mais plutôt son spectrogramme (qui est une série de transformées de Fourier à court terme successives).

L'idée de base est qu'une onde sonore très complexe (la voix humaine) n'est qu'une superposition de fréquences pures. En décomposant le signal via ses coefficients $c_n(f)$, l'algorithme "isole" les caractéristiques : les basses fréquences (le timbre global) des hautes fréquences (les transitoires, les consonnes).

**Exemple concret 4 : Compression d'une vibration**
Imaginons qu'un capteur vibratoire industriel capte un signal $f(t) = 3\cos(t) + 0.1\sin(50t) + \mathcal{N}(t)$ où $\mathcal{N}$ est un bruit blanc.
Le calcul des coefficients de Fourier révélera un immense pic d'amplitude pour $n=\pm 1$ ($a_1 = 3$), et un petit pic pour $n=\pm 50$ ($b_{50} = 0.1$). Le reste sera proche de zéro.
Pour stocker le signal ou l'envoyer à un modèle de Machine Learning, il suffit de ne transmettre que le tuple `(frequence=1, amplitude=3)` et `(frequence=50, amplitude=0.1)`. C'est l'essence même de l'ingénierie des caractéristiques (feature engineering) dans l'IA embarquée.

### B. Illustration géométrique : Synthèse Additive

\begin{tikzpicture}[scale=1.5]
    % Axes
    \draw[->] (-3.5,0) -- (3.5,0) node[right] {$t$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$f(t)$};

    % Signal Carré (True function)
    \draw[thick, blue] (-3.14,-1) -- (0,-1);
    \draw[thick, blue] (0,1) -- (3.14,1);
    \draw[dashed, blue] (0,-1) -- (0,1);

    % Fundamental (sin(t))
    \draw[red, domain=-3.14:3.14, smooth, samples=100] plot (\x, {4/3.14 * sin(\x r)});

    % N=3 Sum (sin(t) + sin(3t)/3)
    \draw[green!60!black, domain=-3.14:3.14, smooth, samples=150] plot (\x, {4/3.14 * (sin(\x r) + 1/3*sin(3*\x r))});

    % N=5 Sum
    \draw[orange, domain=-3.14:3.14, smooth, samples=200] plot (\x, {4/3.14 * (sin(\x r) + 1/3*sin(3*\x r) + 1/5*sin(5*\x r))});

    % Légende
    \node[blue] at (2, 1.2) {Signal Carré};
    \node[red] at (2, 0.7) {$N=1$};
    \node[green!60!black] at (2, -0.2) {$N=3$};
    \node[orange] at (2, -0.6) {$N=5$};
\end{tikzpicture}
