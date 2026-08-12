---
uuid: "jalon-57"
title: "Théorème du point fixe de Banach"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/convergence
prev: "[[Jalon 56 (Espaces métriques complets).md]]"
next: "[[Jalon 58 (Théorème de Baire).md]]"
---

# Jalon 57 : Théorème du point fixe de Banach

## 1. Genèse du Théorème du Point Fixe

L'étude des équations de la forme $f(x) = x$ est au cœur de l'analyse mathématique. De nombreuses équations différentielles, intégrales ou algébriques peuvent se reformuler en la recherche d'un point fixe pour un opérateur approprié. L'intuition fondamentale derrière le théorème du point fixe de Banach, formulé par Stefan Banach en 1922 dans sa thèse de doctorat, repose sur un principe géométrique simple : si une transformation réduit systématiquement les distances entre les points d'un espace complet, l'itération répétée de cette transformation finira par "piéger" l'espace en un unique point immuable.

Historiquement, cette idée systématise la méthode des approximations successives introduite par Émile Picard et Charles Émile Augustin Liouville pour prouver l'existence et l'unicité des solutions d'équations différentielles (le célèbre théorème de Cauchy-Lipschitz). Banach a distillé ce principe en l'extrayant de son contexte différentiel pour l'énoncer dans le cadre pur et abstrait des espaces métriques, marquant ainsi une étape fondatrice dans le développement de l'analyse fonctionnelle moderne.

## 2. Définitions, Théorèmes et Exemples

### A. Applications Contractantes

Soit $(X, d)$ un espace métrique.

**Définition (Application Contractante) :**
Une application $f : X \to X$ est dite strictement contractante, ou plus simplement contractante, s'il existe une constante $k \in [0, 1[$ (appelée rapport de contraction) telle que pour tout couple de points $(x, y) \in X^2$ :
$$d(f(x), f(y)) \leq k \, d(x, y)$$

**Exemple Concret Immédiat 1 (Fonction réelle affine) :**
Considérons l'espace métrique usuel $(\mathbb{R}, |\cdot|)$ et l'application $f(x) = \frac{1}{2}x + 3$.
Calculons la distance entre les images :
$$|f(x) - f(y)| = \left|\left(\frac{1}{2}x + 3\right) - \left(\frac{1}{2}y + 3\right)\right| = \frac{1}{2}|x - y|$$
L'application $f$ est donc contractante avec un rapport de contraction $k = \frac{1}{2} < 1$.

**Exemple Concret Immédiat 2 (Fonction réelle non linéaire) :**
Soit l'espace métrique $X = [1, +\infty[$ muni de la distance usuelle, et $f(x) = x + \frac{1}{x}$.
Regardons la dérivée : $f'(x) = 1 - \frac{1}{x^2}$. Sur $[1, +\infty[$, on a $0 \leq f'(x) < 1$.
Cependant, le supremum de $|f'(x)|$ sur cet intervalle est $1$ (atteint asymptotiquement lorsque $x \to +\infty$). L'application $f$ satisfait $d(f(x), f(y)) < d(x, y)$ pour $x \neq y$, mais n'admet aucun $k < 1$ global. Elle n'est **pas** contractante au sens strict (elle est seulement faiblement contractante ou non-expansive). D'ailleurs, l'équation $x + \frac{1}{x} = x$ n'a aucune solution réelle (elle impliquerait $1/x = 0$).

### B. Le Théorème Fondamental de Banach

**Théorème du point fixe de Banach (ou Théorème de l'application contractante) :**
Soit $(X, d)$ un espace métrique complet et non vide. Si $f : X \to X$ est une application contractante de rapport $k \in [0, 1[$, alors :
1. $f$ admet un unique point fixe $x^* \in X$, c'est-à-dire un unique élément vérifiant $f(x^*) = x^*$.
2. Pour tout point initial $x_0 \in X$, la suite $(x_n)_{n \in \mathbb{N}}$ définie par récurrence par $x_{n+1} = f(x_n)$ converge vers $x^*$.
3. La vitesse de convergence (erreur d'approximation) vérifie la majoration *a priori* :
$$d(x_n, x^*) \leq \frac{k^n}{1 - k} d(x_1, x_0)$$
Et la majoration *a posteriori* :
$$d(x_{n+1}, x^*) \leq \frac{k}{1 - k} d(x_{n+1}, x_n)$$

**Exemple Concret Immédiat 3 (Convergence d'une suite itérative) :**
Prenons l'équation $x = \cos(x)$ sur $X = [0, 1]$ muni de $d(x, y) = |x - y|$.
La fonction $f(x) = \cos(x)$ est dérivable, et $|f'(x)| = |-\sin(x)| = \sin(x)$.
Sur $[0, 1]$, la fonction sinus est croissante et son maximum est $\sin(1) \approx 0.841 < 1$.
Ainsi, $f$ est contractante avec $k = \sin(1)$. L'intervalle fermé $[0, 1]$ est un sous-ensemble fermé de $\mathbb{R}$ (complet), donc c'est un espace métrique complet.
Le théorème garantit l'existence d'un unique point fixe dans $[0, 1]$.
Si l'on part de $x_0 = 0$ :
$x_1 = \cos(0) = 1$
$x_2 = \cos(1) \approx 0.5403$
$x_3 = \cos(0.5403) \approx 0.8575$
$x_4 = \cos(0.8575) \approx 0.6543$
La suite $(x_n)$ oscille et converge rapidement vers l'unique solution $x^* \approx 0.739085$.

### C. Cas Limites et Configurations Pathologiques

Le théorème repose sur deux hypothèses cruciales qui ne peuvent être relâchées simultanément.

**Pathologie 1 : Espace non complet.**
Considérons l'espace métrique $X = ]0, 1]$ (qui n'est pas complet avec la distance usuelle) et $f(x) = \frac{x}{2}$.
$f$ est contractante ($k = 1/2$). Or l'équation $f(x) = x$ implique $x = 0$, qui n'appartient pas à $X$. L'absence de complétude empêche la suite $x_n = x_0 / 2^n$ de trouver sa limite dans $X$.

**Pathologie 2 : Application faiblement contractante (mais pas strictement).**
Comme vu dans l'exemple 2 avec $f(x) = x + 1/x$ sur $[1, +\infty[$. L'espace est fermé dans $\mathbb{R}$, donc complet. On a $|f(x) - f(y)| < |x - y|$ (inégalité stricte), mais la constante $k < 1$ fait défaut. L'application ne possède aucun point fixe.

## 3. Démonstrations Explicites

Nous allons démontrer en détail le théorème du point fixe de Banach.

**Étape 1 : Unicité du point fixe.**
Supposons que $f$ admette deux points fixes, $x^*$ et $y^*$. Par définition, $f(x^*) = x^*$ et $f(y^*) = y^*$.
Évaluons la distance entre ces deux points :
$$d(x^*, y^*) = d(f(x^*), f(y^*)) \leq k \, d(x^*, y^*)$$
Ceci s'écrit :
$$(1 - k) d(x^*, y^*) \leq 0$$
Puisque $k < 1$, on a $1 - k > 0$. La distance étant toujours positive ou nulle, la seule solution possible est $d(x^*, y^*) = 0$, ce qui implique, par l'axiome de séparation de la distance, que $x^* = y^*$. L'unicité est prouvée.

**Étape 2 : Construction d'une suite de Cauchy.**
Soit $x_0 \in X$ un point quelconque. Définissons la suite des itérés $x_{n+1} = f(x_n)$.
Calculons la distance entre deux termes consécutifs :
$$d(x_{n+1}, x_n) = d(f(x_n), f(x_{n-1})) \leq k \, d(x_n, x_{n-1})$$
Par récurrence immédiate, on obtient :
$$d(x_{n+1}, x_n) \leq k^n \, d(x_1, x_0)$$
Maintenant, pour $p > n \geq 0$, évaluons la distance $d(x_p, x_n)$ en utilisant l'inégalité triangulaire de manière répétée :
$$d(x_p, x_n) \leq d(x_p, x_{p-1}) + d(x_{p-1}, x_{p-2}) + \dots + d(x_{n+1}, x_n)$$
$$d(x_p, x_n) \leq \sum_{i=n}^{p-1} d(x_{i+1}, x_i)$$
En utilisant la majoration précédente :
$$d(x_p, x_n) \leq \sum_{i=n}^{p-1} k^i \, d(x_1, x_0) = k^n \, d(x_1, x_0) \sum_{j=0}^{p-n-1} k^j$$
On reconnaît la somme des termes d'une suite géométrique de raison $k < 1$ :
$$\sum_{j=0}^{p-n-1} k^j = \frac{1 - k^{p-n}}{1 - k} \leq \frac{1}{1 - k}$$
D'où l'inégalité fondamentale :
$$d(x_p, x_n) \leq \frac{k^n}{1 - k} d(x_1, x_0)$$
Puisque $k < 1$, $\lim_{n \to +\infty} k^n = 0$. Par conséquent, pour tout $\epsilon > 0$, il existe un rang $N$ tel que pour tout $p > n \geq N$, $d(x_p, x_n) < \epsilon$.
La suite $(x_n)_{n \in \mathbb{N}}$ est donc une suite de Cauchy dans l'espace $(X, d)$.

**Étape 3 : Convergence et existence du point fixe.**
Puisque l'espace métrique $(X, d)$ est complet par hypothèse, toute suite de Cauchy y converge. Il existe donc un élément $x^* \in X$ tel que $\lim_{n \to +\infty} x_n = x^*$.
Montrons que $x^*$ est un point fixe de $f$.
L'application $f$ est contractante, elle est donc uniformément continue (c'est une application lipschitzienne). La continuité implique que la limite commute avec l'application :
$$f(x^*) = f\left(\lim_{n \to +\infty} x_n\right) = \lim_{n \to +\infty} f(x_n) = \lim_{n \to +\infty} x_{n+1} = x^*$$
Ainsi, $x^*$ est bien un point fixe de $f$.

**Étape 4 : Majoration de l'erreur.**
En reprenant l'inégalité fondamentale $d(x_p, x_n) \leq \frac{k^n}{1 - k} d(x_1, x_0)$ et en faisant tendre $p$ vers l'infini (la distance $d(\cdot, x_n)$ étant continue par rapport à son premier argument), on obtient directement la majoration *a priori* :
$$d(x^*, x_n) \leq \frac{k^n}{1 - k} d(x_1, x_0)$$
La preuve est achevée.

## 4. Applications en Physique, Logique et Intelligence Artificielle

### A. Équations Différentielles (Théorème de Cauchy-Lipschitz)
Le théorème de Banach est la clé de voûte de la théorie des équations différentielles ordinaires. Pour une équation différentielle du premier ordre $y'(t) = F(t, y(t))$ avec condition initiale $y(t_0) = y_0$, on peut la formuler comme une équation intégrale de Volterra :
$$y(t) = y_0 + \int_{t_0}^t F(s, y(s)) \, ds$$
On définit l'opérateur intégral $T$ opérant sur un espace de fonctions continues, muni de la norme de la convergence uniforme, par $(T(y))(t) = y_0 + \int_{t_0}^t F(s, y(s)) \, ds$.
Si $F$ est localement lipschitzienne par rapport à $y$, on montre qu'en restreignant l'intervalle de temps $[t_0 - \alpha, t_0 + \alpha]$, l'opérateur $T$ devient strictement contractant. Son unique point fixe est l'unique solution locale de l'équation différentielle (Théorème de Picard-Lindelöf).

### B. Apprentissage par Renforcement (Reinforcement Learning)
Dans les processus de décision markoviens (MDP), l'objectif est de trouver la fonction de valeur optimale $V^*(s)$, qui représente le gain espéré maximal à partir d'un état $s$. Cette fonction est définie implicitement par l'**équation d'optimalité de Bellman** :
$$V^*(s) = \max_{a} \sum_{s', r} p(s', r | s, a) [r + \gamma V^*(s')]$$
On définit l'opérateur de Bellman optimal $\mathcal{B}$ opérant sur l'espace des fonctions de valeur $V : \mathcal{S} \to \mathbb{R}$ (qui, pour un espace d'états fini, est isomorphe à $\mathbb{R}^{|\mathcal{S}|}$ muni de la norme $\|\cdot\|_\infty$) par :
$$(\mathcal{B}V)(s) = \max_{a} \sum_{s', r} p(s', r | s, a) [r + \gamma V(s')]$$
Grâce au facteur de dépréciation (discount factor) $\gamma \in [0, 1[$, on démontre que l'opérateur $\mathcal{B}$ est une $\gamma$-contraction pour la norme infinie :
$$\|\mathcal{B}V_1 - \mathcal{B}V_2\|_\infty \leq \gamma \|V_1 - V_2\|_\infty$$
Puisque l'espace $\mathbb{R}^{|\mathcal{S}|}$ muni de la norme uniforme est un espace de Banach (donc complet), le théorème du point fixe garantit que :
1. L'équation de Bellman admet une **unique** solution $V^*$.
2. L'algorithme **Value Iteration**, qui consiste simplement à calculer itérativement $V_{k+1} = \mathcal{B}V_k$ à partir d'une estimation arbitraire $V_0$, converge uniformément vers la vraie fonction de valeur $V^*$. L'erreur décroît de manière exponentielle en $\gamma^k$.

### C. Réseaux de Neurones à Équilibre Profond (Deep Equilibrium Models - DEQ)
L'architecture standard d'un réseau de neurones profond compose $L$ fonctions paramétrées $h_{i+1} = \sigma(W_i h_i + b_i)$. Dans un modèle DEQ, l'idée est de lier les poids à travers une infinité de couches (récurrentes), cherchant à atteindre un état stable (ou état stationnaire) de la représentation :
$$h^* = \sigma(W h^* + U x + b)$$
où $x$ est l'entrée, et $h^*$ la représentation cachée d'équilibre.
Ce modèle correspond à la recherche d'un point fixe de l'application $f_x(h) = \sigma(W h + U x + b)$. Si la norme spectrale de la matrice de poids satisfait $\|W\| < \frac{1}{L_\sigma}$ (où $L_\sigma$ est la constante de Lipschitz de la fonction d'activation, souvent 1 pour ReLU), alors $f_x$ est une contraction stricte. Le théorème de Banach assure que peu importe l'état initial du réseau, la propagation avant convergera de manière garantie et géométrique vers le même état d'équilibre $h^*$. La rétropropagation peut ensuite se faire analytiquement via le théorème des fonctions implicites sur l'état d'équilibre, libérant une quantité massive de mémoire car il n'est plus nécessaire de stocker les activations des itérations intermédiaires.
