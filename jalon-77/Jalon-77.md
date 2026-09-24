---
uuid: "jalon-77"
title: "Densité dans Lp"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]"
next: "[[Jalon 78 (Séries de Fourier).md]]"
---

# Jalon 77 : Densité des Fonctions Simples et Régulières dans $L^p$

## 1. Introduction à l'Approximation dans les Espaces Mesurés

L'analyse fonctionnelle s'est heurtée à un défi de taille lors de la généralisation de l'intégration par Lebesgue. Les espaces $L^p(\mu)$, abritant des fonctions mesurables dont la puissance $p$-ième est intégrable, contiennent des objets mathématiques d'une grande pathologie, bien éloignés des fonctions lisses ou continues étudiées historiquement par Newton ou Cauchy. Comment alors démontrer des propriétés analytiques ou différentielles globales sur ces espaces ?

La réponse réside dans la notion de densité. L'idée fondatrice, développée par Fréchet, Riesz et Lebesgue, est d'approcher toute fonction mesurable, aussi singulière soit-elle, par une suite de fonctions "simples" ou "régulières" avec une erreur arbitrairement petite au sens de la norme $L^p$. On démontre alors une propriété sur un sous-espace dense (comme les fonctions étagées ou les fonctions infiniment dérivables à support compact), puis, par un argument de complétude (isométrie ou prolongement par continuité), on étend cette propriété à l'espace entier. C'est l'essence même de l'approximation dans les espaces de Lebesgue.

## 2. Définitions, Théorèmes & Exemples

### A. Densité des fonctions étagées

Considérons un espace mesuré $(X, \mathcal{A}, \mu)$ et soit $1 \le p < \infty$. On rappelle qu'une fonction étagée (ou simple) est une combinaison linéaire finie d'indicatrices d'ensembles mesurables : $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}$, où $A_i \in \mathcal{A}$ et $\mu(A_i) < \infty$.

> **Théorème de densité des fonctions étagées :**
> Soit $p \in [1, \infty[$. L'espace vectoriel des fonctions étagées intégrables, noté $\mathcal{E} \cap L^p(X, \mu)$, est dense dans l'espace de Banach $L^p(X, \mu)$.
> Formellement :
> $$ \forall f \in L^p(X, \mu), \forall \varepsilon > 0, \exists s \in \mathcal{E}, \quad \|f - s\|_p = \left( \int_X |f - s|^p \, d\mu \right)^{\frac{1}{p}} < \varepsilon $$

**Exemple :**
Soit $f(x) = x^{-1/4}$ définie sur $X = (0, 1]$ munie de la mesure de Lebesgue $\lambda$. Montrons que $f \in L^2((0, 1])$.
On a $\|f\|_2^2 = \int_0^1 (x^{-1/4})^2 \, dx = \int_0^1 x^{-1/2} \, dx = \left[ 2x^{1/2} \right]_0^1 = 2 < \infty$.
Construisons une approximation étagée $s$. Divisons $(0, 1]$ en deux intervalles $I_1 = (0, 1/4]$ et $I_2 = (1/4, 1]$.
Posons $s(x) = 2 \cdot \mathbf{1}_{(0, 1/4]} + 1 \cdot \mathbf{1}_{(1/4, 1]}$. (Les valeurs $2$ et $1$ approchent $f(x)$ sur ces sous-intervalles).
Calculons l'erreur $L^2$ sur $I_2$ par exemple :
$\int_{1/4}^1 |x^{-1/4} - 1|^2 \, dx = \int_{1/4}^1 (x^{-1/2} - 2x^{-1/4} + 1) \, dx = \left[ 2x^{1/2} - \frac{8}{3}x^{3/4} + x \right]_{1/4}^1$.
En $1$ : $2 - \frac{8}{3} + 1 = \frac{1}{3}$.
En $1/4$ : $2(1/2) - \frac{8}{3}(1/4)^{3/4} + 1/4 = 1 - \frac{8}{3} (2^{-2})^{3/4} + 1/4 = 5/4 - \frac{8}{3} 2^{-3/2} = 5/4 - \frac{8}{3} \frac{1}{2\sqrt{2}} = 5/4 - \frac{4}{3\sqrt{2}} \approx 1.25 - 0.942 = 0.308$.
L'intégrale sur $I_2$ vaut $0.333 - 0.308 = 0.025$. En raffinant la subdivision, l'erreur globale $\|f - s\|_2$ tendra vers $0$.

### B. Densité des fonctions continues à support compact

Soit $\Omega$ un ouvert de $\mathbb{R}^n$, muni de la tribu borélienne et de la mesure de Lebesgue. On note $C_c(\Omega)$ l'espace des fonctions continues de $\Omega$ dans $\mathbb{R}$ dont le support est un compact inclus dans $\Omega$.

> **Théorème de régularité et densité :**
> Pour $1 \le p < \infty$, l'espace $C_c(\Omega)$ est dense dans $L^p(\Omega)$.
> $$ \forall f \in L^p(\Omega), \forall \varepsilon > 0, \exists \varphi \in C_c(\Omega), \quad \|f - \varphi\|_p < \varepsilon $$

**Exemple :**
Approchons la fonction indicatrice de l'intervalle $f = \mathbf{1}_{[-1, 1]} \in L^1(\mathbb{R})$ par une fonction continue à support compact.
Soit $\delta > 0$. Définissons $\varphi_\delta \in C_c(\mathbb{R})$ par :
$\varphi_\delta(x) = 1$ si $x \in [-1, 1]$.
$\varphi_\delta(x) = \frac{1+\delta-x}{\delta}$ si $x \in (1, 1+\delta]$.
$\varphi_\delta(x) = \frac{x+1+\delta}{\delta}$ si $x \in [-1-\delta, -1)$.
$\varphi_\delta(x) = 0$ si $|x| > 1+\delta$.
Calculons $\|f - \varphi_\delta\|_1$ :
$\|f - \varphi_\delta\|_1 = \int_{\mathbb{R}} |f(x) - \varphi_\delta(x)| \, dx = \int_{-1-\delta}^{-1} |\varphi_\delta(x)| \, dx + \int_{1}^{1+\delta} |\varphi_\delta(x)| \, dx$.
$\int_{1}^{1+\delta} \frac{1+\delta-x}{\delta} \, dx = \left[ -\frac{(1+\delta-x)^2}{2\delta} \right]_1^{1+\delta} = 0 - \left( -\frac{\delta^2}{2\delta} \right) = \frac{\delta}{2}$.
Par symétrie, la deuxième intégrale vaut aussi $\frac{\delta}{2}$.
Donc $\|f - \varphi_\delta\|_1 = \delta$.
En choisissant $\delta < \varepsilon$, on a bien approché l'indicatrice $f$ par une fonction continue $\varphi_\delta$ à $\varepsilon$ près en norme $L^1$.

### C. Densité des fonctions lisses à support compact

On note $C_c^\infty(\Omega) = \mathcal{D}(\Omega)$ l'espace des fonctions infiniment différentiables à support compact dans $\Omega$ (les fonctions tests).

> **Théorème de densité des fonctions lisses :**
> Pour $1 \le p < \infty$, l'espace $C_c^\infty(\Omega)$ est dense dans $L^p(\Omega)$.

*Remarque sur le cas limite :* Si $p = \infty$, les théorèmes de densité précédents tombent en défaut. L'adhérence de $C_c(\Omega)$ pour la norme $\|\cdot\|_\infty$ est l'espace $C_0(\Omega)$ des fonctions continues tendant vers $0$ à l'infini, qui est un sous-espace strict et très petit de $L^\infty(\Omega)$.

\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->] (-2.5,0) -- (2.5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,1.5) node[above] {$y$};
\draw[thick, blue] (-1,0) -- (-1,1) -- (1,1) -- (1,0);
\draw[thick, red] (-1.2,0) -- (-1,1) -- (1,1) -- (1.2,0);
\node[blue, above] at (0,1.1) {$f = \mathbf{1}_{[-1, 1]}$};
\node[red, above right] at (1.1,0.5) {$\varphi_\delta$};
\draw[dashed] (-1,0) node[below] {$-1$};
\draw[dashed] (1,0) node[below] {$1$};
\draw[dashed] (-1.2,0) node[below] {$-1-\delta$};
\draw[dashed] (1.2,0) node[below] {$1+\delta$};
\end{tikzpicture}
\end{center}

## 3. Démonstrations

### Preuve du Théorème de densité des fonctions étagées

Nous allons démontrer ce théorème ligne par ligne pour $f \in L^p(X, \mu)$.

**Étape 1 : Réduction au cas des fonctions positives.**
Toute fonction mesurable $f$ à valeurs réelles se décompose canoniquement en ses parties positive et négative : $f = f^+ - f^-$, où $f^+ = \max(f, 0) \ge 0$ et $f^- = \max(-f, 0) \ge 0$.
Si $f \in L^p(X, \mu)$, alors $|f|^p \in L^1(X, \mu)$. Comme $0 \le f^+ \le |f|$, on a $(f^+)^p \le |f|^p$, d'où $f^+ \in L^p(X, \mu)$ et de même $f^- \in L^p(X, \mu)$.
Si l'on montre que toute fonction positive de $L^p$ peut être approchée par des fonctions étagées positives de $L^p$, alors par linéarité, pour $\varepsilon > 0$, on trouvera $s_1$ et $s_2$ étagées positives telles que $\|f^+ - s_1\|_p < \varepsilon/2$ et $\|f^- - s_2\|_p < \varepsilon/2$. En posant $s = s_1 - s_2$ (qui est étagée), on aura, par l'inégalité triangulaire (Minkowski) :
$\|f - s\|_p = \|(f^+ - s_1) - (f^- - s_2)\|_p \le \|f^+ - s_1\|_p + \|f^- - s_2\|_p < \varepsilon$.
Supposons donc $f \ge 0$.

**Étape 2 : Construction de la suite d'approximation.**
D'après la théorie de l'intégration (Jalon 65), puisqu'on a $f \ge 0$ mesurable, il existe une suite croissante $(s_n)_{n \in \mathbb{N}}$ de fonctions étagées positives telles que pour tout $x \in X$, $s_n(x) \to f(x)$ lorsque $n \to \infty$.

**Étape 3 : Application du Théorème de Convergence Dominée (TCD).**
Nous voulons montrer que $\|f - s_n\|_p \to 0$.
Considérons la suite de fonctions $g_n = |f - s_n|^p$.
1. **Convergence simple :** Pour tout $x \in X$, $s_n(x) \to f(x)$, donc $g_n(x) = |f(x) - s_n(x)|^p \to 0$.
2. **Domination :** Comme $0 \le s_n(x) \le f(x)$ pour tout $n$, on a $0 \le f(x) - s_n(x) \le f(x)$.
Donc $g_n(x) = (f(x) - s_n(x))^p \le (f(x))^p$.
La fonction majorante est $(f)^p$, qui est intégrable par hypothèse puisque $f \in L^p(X, \mu)$.
Par le Théorème de Convergence Dominée de Lebesgue,
$$ \lim_{n \to \infty} \int_X g_n \, d\mu = \int_X \lim_{n \to \infty} g_n \, d\mu = \int_X 0 \, d\mu = 0 $$
Ainsi, $\lim_{n \to \infty} \|f - s_n\|_p^p = 0$, soit $\lim_{n \to \infty} \|f - s_n\|_p = 0$.

**Étape 4 : Intégrabilité des fonctions étagées de la suite.**
Puisque $0 \le s_n \le f$, on a $s_n^p \le f^p$, donc $\int_X s_n^p d\mu \le \int_X f^p d\mu < \infty$. Les fonctions $s_n$ sont donc bien des fonctions étagées dans $L^p(X, \mu)$. La démonstration est complète. $\blacksquare$

### Preuve partielle : Régularité de la mesure de Lebesgue et densité de $C_c(\Omega)$

Pour passer des fonctions étagées aux fonctions continues dans $L^p(\mathbb{R}^n)$, on procède en deux temps.
1. Les fonctions étagées sont combinaisons linéaires d'indicatrices d'ensembles mesurables $A$ avec $\lambda(A) < \infty$.
2. Par le théorème de régularité de la mesure de Lebesgue, tout ensemble mesurable de mesure finie peut être approché par des ouverts de l'extérieur et des compacts de l'intérieur. De plus, on peut approcher la mesure d'un ouvert par la réunion finie de pavés (produits d'intervalles).
Ainsi, l'indicatrice $\mathbf{1}_A$ peut être approchée dans $L^p$ par $\mathbf{1}_{P}$ où $P$ est une réunion finie de pavés fermés bornés.
3. Chaque indicatrice de pavé $\mathbf{1}_{[-a, a]}$ peut être approchée par des fonctions continues à support compact (la fonction "trapèze" $\varphi_\delta$ vue dans l'exemple, généralisée en dimension $n$). Par l'inégalité triangulaire, ces approximations composées garantissent la densité de $C_c(\mathbb{R}^n)$.

## 4. Applications en Physique, Logique & Intelligence Artificielle

**1. Transformée de Fourier et Traitement du Signal (Physique & IA) :**
La densité de $\mathcal{D}(\mathbb{R})$ dans $L^2(\mathbb{R})$ est cruciale pour étendre la transformée de Fourier. Initialement bien définie sur $L^1(\mathbb{R})$ ou $\mathcal{D}(\mathbb{R})$ (où elle produit des fonctions lisses à décroissance rapide), l'isométrie de Plancherel permet de prolonger uniquement par continuité la transformée de Fourier à tout l'espace $L^2(\mathbb{R})$. L'espace des signaux d'énergie finie est ainsi traité spectralement. En intelligence artificielle, le traitement des signaux audio via l'algorithme STFT (Short-Time Fourier Transform) s'appuie formellement sur ces prolongements dans les espaces $L^2$.

**2. Analyse par Convolution et Régularisation (IA) :**
Une technique courante pour approcher une fonction $f \in L^p$ par une fonction de $C_c^\infty$ est la convolution par une suite régularisante $(\rho_n)$ (fonctions lisses, d'intégrale 1, à support concentré autour de 0). La suite $f * \rho_n$ converge vers $f$ dans $L^p$. En apprentissage profond, les opérateurs de flou (blur pooling) ou les noyaux gaussiens dans les réseaux convolutifs (CNN) effectuent empiriquement des lissages de représentations discrètes.

**3. Théorème d'Approximation Universelle (Réseaux de Neurones) :**
Bien que formulé classiquement pour des fonctions continues sur des compacts via le théorème de Stone-Weierstrass, l'approximation universelle s'étend à $L^p(\mu)$. Cybenko et Hornik ont montré que l'ensemble des réseaux de neurones à une couche cachée $F(x) = \sum_i c_i \sigma(w_i^T x + b_i)$ est dense dans $L^p(\mathbb{R}^n, \mu)$ (pour toute mesure de probabilité $\mu$). Le processus d'entraînement (descente de gradient stochastique) recherche itérativement la meilleure configuration pour se rapprocher de la fonction cible, justifié fondamentalement par cette garantie topologique de densité.
