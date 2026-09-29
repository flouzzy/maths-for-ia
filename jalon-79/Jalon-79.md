---
uuid: "jalon-79"
title: "Convergence L2 et Identité de Parseval"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon-78.md]]"
next: "[[jalon-80/Jalon-80.md|Jalon 80 : Transformée de Fourier dans L1]]"
---

# Jalon 79 : Convergence $L^2$ et Identité de Parseval

## 1. Origine Physique et Géométrique

Le besoin de comprendre la convergence en moyenne quadratique (norme $L^2$) est intimement lié à la notion d'énergie physique. Au 19ème siècle, lorsque Joseph Fourier développe sa théorie de la chaleur, puis que Lord Rayleigh et Marc-Antoine Parseval formalisent la décomposition des signaux, une question fondamentale se pose : si l'on décompose un signal complexe (comme une onde sonore ou électromagnétique) en une somme infinie d'ondes sinusoïdales pures (ses composantes de Fourier), la somme des énergies de ces ondes pures est-elle exactement égale à l'énergie totale du signal d'origine ?

La réponse est oui, et cette conservation de l'énergie est le cœur de l'Identité de Parseval. Géométriquement, cela s'interprète comme une généralisation du Théorème de Pythagore en dimension infinie. Si l'on imagine l'espace des fonctions de carré intégrable $L^2$ comme un vaste espace vectoriel, les fonctions trigonométriques $e^{inx}$ forment une base orthogonale. Décomposer un signal en série de Fourier revient simplement à projeter ce signal sur chaque axe de cette base infinie. Le "carré de la longueur" (l'énergie) du vecteur-signal est alors exactement la somme des carrés de ses projections sur chaque axe, tout comme l'hypoténuse d'un triangle rectangle en 2D.

C'est une bascule majeure : on passe d'une convergence point par point (souvent difficile ou fausse avec les séries de Fourier à cause du phénomène de Gibbs) à une convergence "en énergie". Même si la série de Fourier ondule ou rate la fonction en quelques points de discontinuité, l'énergie totale de l'erreur tend vers zéro.

## 2. Définitions, Théorèmes et Exemples

### Théorème de Convergence en Moyenne Quadratique (Théorème de Riesz-Fischer)

**Théorème :**
Soit $f \in L^2([0, 2\pi], \mathbb{C})$ une fonction de carré intégrable sur $[0, 2\pi]$. Notons $c_n(f)$ ses coefficients de Fourier complexes définis par :
$$ c_n(f) = \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt $$
Et soit $S_N(f)(t) = \sum_{n=-N}^N c_n(f) e^{int}$ la somme partielle d'ordre $N$ de sa série de Fourier.
Alors, la suite des sommes partielles $(S_N(f))_{N \ge 0}$ converge vers $f$ en moyenne quadratique (pour la norme $L^2$) :
$$ \lim_{N \to +\infty} \| f - S_N(f) \|_{L^2}^2 = \lim_{N \to +\infty} \frac{1}{2\pi} \int_0^{2\pi} \left| f(t) - S_N(f)(t) \right|^2 dt = 0 $$

**Exemple Concret : Le signal en dents de scie**
Considérons la fonction $2\pi$-périodique définie sur $[-\pi, \pi[$ par $f(t) = t$.
On a calculé (voir Jalon 78) ses coefficients de Fourier trigonométriques :
$a_n = 0$ et $b_n = \frac{2(-1)^{n+1}}{n}$ pour $n \ge 1$.
La série de Fourier est $S_N(f)(t) = \sum_{n=1}^N \frac{2(-1)^{n+1}}{n} \sin(nt)$.
La norme $L^2$ de $f$ est $\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi t^2 dt = \frac{1}{2\pi} \left[ \frac{t^3}{3} \right]_{-\pi}^\pi = \frac{1}{2\pi} \frac{2\pi^3}{3} = \frac{\pi^2}{3}$.
L'énergie de $S_N(f)$ est la somme des énergies des harmoniques. Pour la fonction sinus, l'énergie moyenne est $1/2$. Donc l'énergie de la n-ième harmonique est $\frac{1}{2} b_n^2 = \frac{1}{2} \left( \frac{2}{n} \right)^2 = \frac{2}{n^2}$.
L'énergie de l'erreur est $E_N = \|f - S_N(f)\|_{L^2}^2 = \frac{\pi^2}{3} - \sum_{n=1}^N \frac{2}{n^2}$.
On sait que $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$, donc la somme tend vers $2 \times \frac{\pi^2}{6} = \frac{\pi^2}{3}$. L'erreur $E_N$ tend bien vers 0. Par exemple, pour $N=10$, $\sum_{n=1}^{10} \frac{2}{n^2} \approx 3.099$, proche de $\pi^2/3 \approx 3.289$.

### Inégalité de Bessel

**Théorème :**
Pour toute fonction $f \in L^2([0, 2\pi])$, la série des carrés des modules des coefficients de Fourier converge, et l'on a :
$$ \sum_{n=-\infty}^{+\infty} |c_n(f)|^2 \le \frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt $$

**Exemple Concret : Un signal impulsionnel approché**
Considérons $f(t) = 1$ pour $t \in [0, a]$ et $f(t) = 0$ ailleurs sur $[0, 2\pi]$ (avec $0 < a < 2\pi$).
$\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_0^a 1^2 dt = \frac{a}{2\pi}$.
Les coefficients sont $c_0 = \frac{a}{2\pi}$, et pour $n \neq 0$, $c_n = \frac{1}{2\pi} \int_0^a e^{-int} dt = \frac{1-e^{-ina}}{2i\pi n}$.
Donc $|c_n|^2 = \frac{1 - \cos(na)}{2\pi^2 n^2} = \frac{\sin^2(na/2)}{\pi^2 n^2}$.
L'inégalité de Bessel affirme que $\left( \frac{a}{2\pi} \right)^2 + 2 \sum_{n=1}^\infty \frac{\sin^2(na/2)}{\pi^2 n^2} \le \frac{a}{2\pi}$.
Pour $a=\pi$, on a $\frac{1}{4} + \frac{2}{\pi^2} \sum_{k=0}^\infty \frac{1}{(2k+1)^2} \le \frac{1}{2}$. En fait, on verra avec Parseval que c'est une égalité stricte, prouvant au passage que la série vaut $\pi^2/8$.

### L'Identité de Parseval (Théorème Fondamental)

**Théorème :**
Pour toute fonction $f \in L^2([0, 2\pi], \mathbb{C})$, la série de Fourier associée vérifie **l'égalité de Parseval** :
$$ \frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt = \sum_{n=-\infty}^{+\infty} |c_n(f)|^2 $$
Si la fonction $f$ est à valeurs réelles, on peut utiliser les coefficients trigonométriques réels $a_n$ et $b_n$. L'identité devient :
$$ \frac{1}{2\pi} \int_0^{2\pi} (f(t))^2 dt = \frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^{+\infty} (a_n^2 + b_n^2) $$

**Exemple Concret : Le signal créneau et la série de Bâle modifiée**
Considérons le signal créneau pair $f(t) = 1$ sur $[-\pi/2, \pi/2]$ et $0$ sur $[-\pi, -\pi/2[ \cup ]\pi/2, \pi]$.
On a $\frac{1}{2\pi} \int_{-\pi}^\pi |f(t)|^2 dt = \frac{1}{2\pi} \times \pi = \frac{1}{2}$.
Ses coefficients réels : $a_0 = \frac{2}{2\pi} \int_{-\pi/2}^{\pi/2} 1 dt = 1$.
$a_n = \frac{1}{\pi} \int_{-\pi/2}^{\pi/2} \cos(nt) dt = \frac{2}{n\pi} \sin(n\pi/2)$. Ainsi $a_{2k} = 0$ pour $k \ge 1$ et $a_{2k+1} = \frac{2(-1)^k}{\pi(2k+1)}$. $b_n = 0$ (parité).
Appliquons l'identité de Parseval :
$$ \frac{1}{2} = \frac{1^2}{4} + \frac{1}{2} \sum_{k=0}^\infty \left( \frac{2(-1)^k}{\pi(2k+1)} \right)^2 $$
$$ \frac{1}{4} = \frac{1}{2} \frac{4}{\pi^2} \sum_{k=0}^\infty \frac{1}{(2k+1)^2} $$
$$ \frac{\pi^2}{8} = \sum_{k=0}^\infty \frac{1}{(2k+1)^2} $$
On retrouve instantanément une valeur célèbre par un simple calcul d'énergie !

\begin{tikzpicture}
\draw[->] (-3.5,0) -- (3.5,0) node[right] {Fréquences $\omega$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$|c_n|^2$ (Énergie)};
\draw[blue, thick] (0,2.5) -- (0,0) node[below] {$c_0$};
\draw[blue, thick] (1,1.5) -- (1,0) node[below] {$c_1$};
\draw[blue, thick] (-1,1.5) -- (-1,0) node[below] {$c_{-1}$};
\draw[blue, thick] (2,0.8) -- (2,0) node[below] {$c_2$};
\draw[blue, thick] (-2,0.8) -- (-2,0) node[below] {$c_{-2}$};
\draw[blue, thick] (3,0.3) -- (3,0) node[below] {$c_3$};
\draw[blue, thick] (-3,0.3) -- (-3,0) node[below] {$c_{-3}$};
\node at (2, 2.5) {$\sum |c_n|^2 = \|f\|_{L^2}^2$};
\end{tikzpicture}

## 3. Démonstrations

### Démonstration de l'Identité de Parseval via l'Inégalité de Bessel et l'Approximation

**Étape 1 : Projection orthogonale et Inégalité de Bessel**
Soit $H = L^2([0, 2\pi])$ l'espace de Hilbert pré-hilbertien muni du produit scalaire hermitien :
$$ \langle f, g \rangle = \frac{1}{2\pi} \int_0^{2\pi} f(t) \overline{g(t)} dt $$
La famille des exponentielles complexes $e_n(t) = e^{int}$ pour $n \in \mathbb{Z}$ forme une famille orthonormale.
En effet : $\langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)t} dt$. Si $n=m$, c'est $1$. Si $n \neq m$, la primitive de $e^{i(n-m)t}$ est $\frac{e^{i(n-m)t}}{i(n-m)}$ qui vaut $0$ entre $0$ et $2\pi$.
La somme partielle $S_N(f) = \sum_{n=-N}^N c_n(f) e_n$ est la projection orthogonale de $f$ sur le sous-espace de dimension finie $V_N = \text{Vect}(e_{-N}, \dots, e_N)$.
Par le théorème de Pythagore :
$$ \|f\|^2 = \|S_N(f)\|^2 + \|f - S_N(f)\|^2 $$
Puisque $e_n$ est orthonormale, $\|S_N(f)\|^2 = \sum_{n=-N}^N |c_n(f)|^2$.
On a donc $\sum_{n=-N}^N |c_n(f)|^2 \le \|f\|^2$. En faisant tendre $N$ vers $+\infty$, la série à termes positifs converge et l'on obtient l'Inégalité de Bessel.

**Étape 2 : Densité des polynômes trigonométriques**
Pour obtenir l'égalité, il faut prouver que $\|f - S_N(f)\|^2 \to 0$, ce qui équivaut à montrer que la famille $(e_n)_{n \in \mathbb{Z}}$ est une famille **totale** dans $L^2$.
D'après le théorème d'approximation de Weierstrass trigonométrique, pour toute fonction continue $2\pi$-périodique $g$, il existe une suite de polynômes trigonométriques $P_k$ convergeant uniformément vers $g$.
La convergence uniforme sur le compact $[0, 2\pi]$ implique la convergence en norme $L^2$ :
$$ \|g - P_k\|_{L^2} \le \sup_{t} |g(t) - P_k(t)| \to 0 $$

**Étape 3 : Densité des fonctions continues dans $L^2$**
Toute fonction $f \in L^2$ peut être approchée d'aussi près que l'on veut (en norme $L^2$) par une fonction continue périodique $g$.
Ainsi, pour un $\epsilon > 0$ fixé :
Il existe $g$ continue telle que $\|f - g\| \le \epsilon/2$.
Il existe un polynôme trigonométrique $P \in V_M$ (pour un certain $M$) tel que $\|g - P\| \le \epsilon/2$.
Par l'inégalité triangulaire, $\|f - P\| \le \epsilon$.

**Étape 4 : Conclusion par la propriété de la projection orthogonale**
La projection orthogonale $S_M(f)$ est l'élément de $V_M$ qui minimise la distance à $f$.
Donc $\|f - S_M(f)\| \le \|f - P\| \le \epsilon$.
Comme la suite des distances à des sous-espaces emboîtés est décroissante, pour tout $N \ge M$, $\|f - S_N(f)\| \le \epsilon$.
Ceci prouve que $\lim_{N \to +\infty} \|f - S_N(f)\| = 0$.
Par Pythagore (Étape 1), on déduit que $\lim_{N \to \infty} \sum_{n=-N}^N |c_n(f)|^2 = \|f\|^2$, achevant la preuve de l'Identité de Parseval.

## 4. Applications en Physique et Intelligence Artificielle

### En Physique : La conservation de l'Énergie
En électromagnétisme et traitement du signal, si $V(t)$ est un signal de tension périodique aux bornes d'une résistance $1\ \Omega$, la puissance moyenne dissipée (l'énergie par période) est donnée par $\frac{1}{T} \int_0^T V(t)^2 dt$.
L'Identité de Parseval stipule que cette puissance totale est la somme des puissances dissipées indépendamment par chaque harmonique (chaque onde sinus). C'est le fondement de l'analyse spectrale moderne avec des analyseurs de spectre.

### En Intelligence Artificielle : Les Réseaux de Neurones Informés par la Physique (PINNs) et les S-Transformées
Dans les architectures d'apprentissage profond travaillant sur le son ou l'image, il est souvent mathématiquement équivalent, grâce à Parseval, de minimiser une fonction de coût (Loss) dans le domaine spatial/temporel et dans le domaine fréquentiel.
- **Régularisation Spectrale :** Lors de l'entraînement d'un Auto-Encoder pour la compression d'image, imposer une perte quadratique $\|x - \hat{x}\|^2$ sur les pixels revient à imposer une perte $\sum |c_n(x) - c_n(\hat{x})|^2$ sur les composantes fréquentielles (via SVD ou DCT). Parseval garantit que les deux espaces géométriques sont parfaitement isométriques.
- **Opérateurs de Convolution Neuronaux (Neural Operators, FNO) :** Dans la résolution d'équations aux dérivées partielles (Navier-Stokes) par des réseaux FNO (Fourier Neural Operators), le modèle apprend les filtres dans le domaine spectral, car l'opération de dérivation s'y transforme en multiplication. La convergence de l'apprentissage est formellement garantie par l'équivalence $L^2$ de Parseval.
