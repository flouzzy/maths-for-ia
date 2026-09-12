---
uuid: "jalon-68"
title: "Lemme de Fatou et fonctions de signe quelconque"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[jalon-67/Jalon-67.md|Jalon 67 (Démonstration du théorème de convergence monotone)]]"
next: "[[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]"
---

# Jalon 68 : Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque

## 1. Origines et nécessité de l'intégration des fonctions signées

La construction de l'intégrale de Lebesgue, initiée par les fonctions mesurables positives, trouve rapidement une limite lorsqu'il s'agit d'analyser des phénomènes physiques ou probabilistes réels où les grandeurs étudiées (charges électriques, flux thermiques, gains et pertes) peuvent s'annuler et changer de signe. L'enjeu géométrique et analytique est de définir un cadre rigoureux permettant de sommer de telles quantités sans risquer d'obtenir des indéterminations du type $\infty - \infty$.

Historiquement, Henri Lebesgue, au début du XXe siècle, surmonte cette difficulté par un procédé de décomposition canonique. Plutôt que d'intégrer directement la fonction oscillante, il propose de la scinder en deux composantes strictement positives : sa partie positive (ce qui dépasse l'axe des abscisses) et sa partie négative (la profondeur sous l'axe, rendue positive). Ce traitement symétrique et absolu garantit la stabilité des théorèmes de passage à la limite, dont le Lemme de Fatou, introduit par Pierre Fatou en 1906, constitue la pierre angulaire permettant de gérer la semi-continuité inférieure des intégrales.

## 2. Définition de l'intégrale et théorèmes fondamentaux

### Décomposition canonique d'une fonction mesurable

Pour toute fonction $f : X \to \overline{\mathbb{R}}$ définie sur un espace mesuré $(X, \mathcal{A}, \mu)$, on définit la **partie positive** $f^+$ et la **partie négative** $f^-$ par :
$$f^+(x) = \max(f(x), 0) \quad \text{et} \quad f^-(x) = \max(-f(x), 0)$$

On obtient ainsi les identités fondamentales :
$$f = f^+ - f^- \quad \text{et} \quad |f| = f^+ + f^-$$

**Exemple d'application immédiat :**
Soit $f(x) = \sin(x)$ sur $X = [0, 2\pi]$ muni de la mesure de Lebesgue $\lambda$.
- $f^+(x) = \sin(x)$ si $x \in [0, \pi]$ et $0$ si $x \in [\pi, 2\pi]$.
- $f^-(x) = 0$ si $x \in [0, \pi]$ et $-\sin(x)$ si $x \in [\pi, 2\pi]$.
On vérifie bien que $|f(x)| = |\sin(x)| = f^+(x) + f^-(x)$.

**Illustration (TikZ) de la décomposition $f = f^+ - f^-$ :**
```tikz
\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->,thick] (-2,0) -- (3,0) node[right] {$x$};
  \draw[->,thick] (0,-1.5) -- (0,1.5) node[above] {$y$};

  % Fonction originale en gris
  \draw[domain=-1.5:2.5, smooth, variable=\x, gray, dashed, thick] plot ({\x}, {sin(\x r * 1.5)});

  % f^+ en bleu
  \draw[domain=-1.5:0, smooth, variable=\x, blue, ultra thick] plot ({\x}, {0});
  \draw[domain=0:2.094, smooth, variable=\x, blue, ultra thick] plot ({\x}, {sin(\x r * 1.5)});
  \draw[domain=2.094:2.5, smooth, variable=\x, blue, ultra thick] plot ({\x}, {0});
  \node[blue] at (1, 1.2) {$f^+$};

  % f^- en rouge
  \draw[domain=-1.5:0, smooth, variable=\x, red, thick] plot ({\x}, {-sin(\x r * 1.5)});
  \draw[domain=0:2.094, smooth, variable=\x, red, thick] plot ({\x}, {0});
  \draw[domain=2.094:2.5, smooth, variable=\x, red, thick] plot ({\x}, {-sin(\x r * 1.5)});
  \node[red] at (-0.7, 1.2) {$f^-$};

  \node at (2.5, -0.5) {$f(x) = \sin(\frac{3}{2}x)$};
\end{tikzpicture}
```


### Intégrabilité selon Lebesgue

**Définition (Fonction Lebesgue-intégrable) :**
Une fonction mesurable $f : X \to \overline{\mathbb{R}}$ est dite **intégrable** (ou Lebesgue-intégrable) par rapport à la mesure $\mu$ si et seulement si ses deux parties $f^+$ et $f^-$ ont une intégrale finie :
$$\int_X f^+ d\mu < +\infty \quad \text{et} \quad \int_X f^- d\mu < +\infty$$
L'espace vectoriel des fonctions intégrables est noté $\mathcal{L}^1(X, \mathcal{A}, \mu)$.
Dans ce cas, l'intégrale de $f$ est définie par :
$$\int_X f d\mu = \int_X f^+ d\mu - \int_X f^- d\mu$$

**Remarque fondamentale :** $f$ est intégrable si et seulement si $|f|$ l'est, puisque $\int |f| d\mu = \int f^+ d\mu + \int f^- d\mu$. C'est une différence majeure avec l'intégrale de Riemann pour les intégrales généralisées (ex: $\int_0^\infty \frac{\sin x}{x} dx$ converge au sens de Riemann mais pas de Lebesgue).

### Le Lemme de Fatou

Le Lemme de Fatou est le premier grand théorème de passage à la limite pour l'intégrale de Lebesgue.

**Théorème (Lemme de Fatou) :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables **positives** sur $(X, \mathcal{A}, \mu)$. Alors :
$$\int_X \left( \liminf_{n \to \infty} f_n \right) d\mu \leq \liminf_{n \to \infty} \int_X f_n d\mu$$

**Exemple de stricte inégalité (perte de masse à l'infini) :**
Sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, posons $f_n = \mathbf{1}_{[n, n+1]}$.
- Pour tout $x \in \mathbb{R}$, il existe $N$ tel que pour tout $n \geq N$, $f_n(x) = 0$. Donc $\liminf_{n \to \infty} f_n(x) = 0$.
- D'où $\int_{\mathbb{R}} (\liminf f_n) d\lambda = 0$.
- Or, pour tout $n$, $\int_{\mathbb{R}} f_n d\lambda = 1$, donc $\liminf_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda = 1$.
On a bien $0 \leq 1$, avec une inégalité stricte causée par la fuite du support vers l'infini.

**Contre-exemple (cas non positif) :**
Si les fonctions ne sont pas positives, le lemme peut être faux. Prenons $f_n = -\mathbf{1}_{[n, n+1]}$.
$\liminf f_n = 0 \implies \int (\liminf f_n) = 0$.
Mais $\int f_n = -1 \implies \liminf \int f_n = -1$. L'inégalité $0 \leq -1$ est fausse. L'hypothèse de positivité (ou de minoration par une fonction intégrable) est donc cruciale.

## 3. Démonstrations rigoureuses

### Démonstration du Lemme de Fatou

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives.
Posons, pour tout $n \in \mathbb{N}$, la fonction $g_n = \inf_{k \geq n} f_k$.
1. **Mesurabilité et positivité :** Les $f_k$ étant mesurables et positives, chaque $g_n$ est mesurable et positive.
2. **Monotonie :** Pour tout $x \in X$, la suite $(g_n(x))_{n \in \mathbb{N}}$ est croissante. En effet, l'infimum est pris sur un ensemble d'indices de plus en plus restreint : $\{k \ge n+1\} \subset \{k \ge n\} \implies \inf_{k \ge n+1} f_k(x) \ge \inf_{k \ge n} f_k(x)$.
3. **Limite :** Par définition de la limite inférieure, on a pour tout $x \in X$ :
   $$\lim_{n \to \infty} g_n(x) = \sup_{n \ge 0} \inf_{k \ge n} f_k(x) = \liminf_{n \to \infty} f_n(x)$$
4. **Application de Beppo-Levi (Convergence Monotone) :**
   La suite $(g_n)$ est une suite croissante de fonctions mesurables positives qui converge simplement vers $\liminf f_n$. Par le théorème de convergence monotone, on a :
   $$\int_X \left( \lim_{n \to \infty} g_n \right) d\mu = \lim_{n \to \infty} \int_X g_n d\mu$$
   Ce qui s'écrit :
   $$\int_X \left( \liminf_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X g_n d\mu$$
5. **Majoration :** Pour tout $k \geq n$, on a par définition $g_n \leq f_k$.
   En intégrant cette inégalité (croissance de l'intégrale), il vient :
   $$\int_X g_n d\mu \leq \int_X f_k d\mu \quad \forall k \geq n$$
   En passant à l'infimum sur $k \geq n$ dans le membre de droite :
   $$\int_X g_n d\mu \leq \inf_{k \geq n} \int_X f_k d\mu$$
6. **Conclusion :** En prenant la limite (qui existe puisque la suite est croissante) quand $n \to \infty$ :
   $$\lim_{n \to \infty} \int_X g_n d\mu \leq \lim_{n \to \infty} \left( \inf_{k \geq n} \int_X f_k d\mu \right) = \liminf_{n \to \infty} \int_X f_n d\mu$$
   En combinant avec le point 4, on obtient exactement :
   $$\int_X \left( \liminf_{n \to \infty} f_n \right) d\mu \leq \liminf_{n \to \infty} \int_X f_n d\mu$$
   $\blacksquare$

## 4. Applications en Théorie de l'Information et Intelligence Artificielle

### Preuve de la semi-continuité inférieure de la divergence de Kullback-Leibler

En apprentissage automatique, on cherche souvent à minimiser la divergence de Kullback-Leibler (KL) entre une distribution vraie $P$ et une distribution approchée $Q_\theta$.
Si $P$ et $Q_\theta$ admettent des densités $p$ et $q_\theta$ par rapport à une mesure de Lebesgue,
$$D_{KL}(P || Q_\theta) = \int p(x) \log\left(\frac{p(x)}{q_\theta(x)}\right) dx$$

Si l'on considère une suite de paramètres $\theta_n \to \theta^*$ telle que $q_{\theta_n}(x) \to q_{\theta^*}(x)$ ponctuellement, la divergence est-elle continue ?
En général non, mais grâce au Lemme de Fatou, on peut prouver sa **semi-continuité inférieure**.
On remarque que la fonction à intégrer n'est pas forcément positive. Toutefois, la fonction $f(u) = u \log(u) - u + 1$ est toujours positive pour $u \ge 0$.
Par le Lemme de Fatou sur des transformations adéquates de la log-vraisemblance, on garantit que :
$$\liminf_{n \to \infty} D_{KL}(P || Q_{\theta_n}) \geq D_{KL}(P || Q_{\theta^*})$$
Cela assure mathématiquement que la limite d'une suite de modèles approchés ne peut pas être "meilleure" (avoir une divergence KL plus faible) que ce que la convergence ponctuelle des densités laisse supposer, sécurisant ainsi les preuves de convergence des algorithmes d'optimisation variationnelle (Variational Inference).
