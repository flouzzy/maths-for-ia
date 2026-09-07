---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]"
next: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Genèse du concept et intuition fondamentale

Le passage à la limite sous le signe intégral est l'un des problèmes les plus profonds et historiques de l'analyse mathématique. Au XIXe siècle, l'intégrale de Riemann a montré ses limites intrinsèques : une suite de fonctions Riemann-intégrables $(f_n)_{n \in \mathbb{N}}$ convergeant simplement vers une fonction $f$ ne garantit nullement que $f$ soit Riemann-intégrable, ni que la limite des intégrales soit l'intégrale de la limite. L'exemple classique de l'indicatrice des rationnels, limite de fonctions étagées sur des ensembles finis, montre l'effondrement de la théorie de Riemann face aux limites simples.

L'invention de la théorie de la mesure par Henri Lebesgue, et son corollaire immédiat par l'école italienne avec Beppo Levi en 1906, change radicalement de paradigme. Au lieu de découper l'axe des abscisses (la source), on découpe l'axe des ordonnées (la cible). Cette approche permet de capturer avec une robustesse absolue le comportement limite des fonctions positives qui croissent.

Imaginez une suite de fonctions positives $f_n$ qui ne font que croître : $f_n(x) \le f_{n+1}(x)$. L'aire sous la courbe (qui peut être un volume, une probabilité, une énergie) ne fait qu'augmenter. Le théorème de convergence monotone affirme un principe de continuité géométrique fondamental : l'aire sous la courbe limite est **exactement** la limite des aires. Ce théorème est le pilier sur lequel repose toute la construction de l'intégration abstraite et des probabilités modernes (notamment l'espérance).

## 2. Définitions et Théorèmes de Convergence Monotone

### Le Théorème Fondamental de Beppo Levi

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré, où $X$ est un ensemble, $\mathcal{A}$ une tribu sur $X$, et $\mu$ une mesure positive.

> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
> Si la suite est **croissante** presque partout, c'est-à-dire :
> $$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \mu\text{-presque partout}$$
> Alors la fonction limite simple $f = \lim_{n \to \infty} f_n$ (qui existe dans $[0, +\infty]$) est mesurable et :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

#### Analyse du Théorème :
- **Variables et Typage :** Les $f_n : X \to [0, +\infty]$ sont à valeurs dans la droite achevée positive. C'est crucial : une fonction peut valoir $+\infty$ et la limite peut valoir $+\infty$. L'intégrale prend donc ses valeurs dans $[0, +\infty]$.
- **Condition de monotonie :** La positivité et la croissance sont indissociables ici. Si la suite n'est pas positive, ou n'est pas croissante, le théorème tombe en défaut (comme on le verra avec le Lemme de Fatou).

### Exemple Concret Immédiat 1 : Construction d'un escalier infini

Prenons l'espace mesuré classique $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Considérons la suite de fonctions définies sur $[0, 1[$ par :
$$f_n(x) = \sum_{k=1}^n k \cdot \mathbf{1}_{\left[1 - \frac{1}{k}, 1 - \frac{1}{k+1}\right[}(x)$$

**1. Croissance et limite :**
Pour tout $x \in [0, 1[$, il existe un unique entier $k_0 \ge 1$ tel que $x \in \left[1 - \frac{1}{k_0}, 1 - \frac{1}{k_0+1}\right[$.
Pour $n \ge k_0$, on a $f_n(x) = k_0$. Ainsi, la suite $f_n(x)$ est croissante et stationne à $k_0$. La fonction limite $f(x)$ prend la valeur $k_0$ sur l'intervalle correspondant.

**2. Calcul de l'intégrale des $f_n$ :**
Les fonctions $f_n$ sont des fonctions étagées. Leur intégrale est la somme des aires des rectangles :
$$\int_{[0,1[} f_n d\lambda = \sum_{k=1}^n k \cdot \lambda\left(\left[1 - \frac{1}{k}, 1 - \frac{1}{k+1}\right[\right) = \sum_{k=1}^n k \left( \left(1 - \frac{1}{k+1}\right) - \left(1 - \frac{1}{k}\right) \right)$$
$$= \sum_{k=1}^n k \left( \frac{1}{k} - \frac{1}{k+1} \right) = \sum_{k=1}^n k \frac{1}{k(k+1)} = \sum_{k=1}^n \frac{1}{k+1}$$

**3. Application du Théorème de Beppo Levi :**
La suite $\left(\int_{[0,1[} f_n d\lambda\right)$ est une série harmonique tronquée, qui tend vers $+\infty$ quand $n \to \infty$.
D'après Beppo Levi, la limite des $f_n$, notée $f$, est intégrable (au sens large) et :
$$\int_{[0,1[} f d\lambda = \lim_{n \to \infty} \sum_{k=1}^n \frac{1}{k+1} = +\infty$$
L'aire sous cet escalier infini est infinie, et l'interversion limite-intégrale est pleinement valide (dans $[0, +\infty]$).

### Corollaire Fondamental : L'Intégration Terme à Terme (Séries à termes positifs)

> **Théorème :**
> Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables **positives** (à valeurs dans $[0, +\infty]$).
> Alors :
> $$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$

Ce corollaire est une application directe du TCM appliqué à la suite des sommes partielles $S_N = \sum_{n=0}^N u_n$, qui est trivialement croissante puisque les $u_n$ sont positives.

### Cas limites et contre-exemples

Le théorème tombe formellement en défaut si l'une des hypothèses (positivité, croissance) manque.

**Contre-exemple (Manque de croissance) : La bosse glissante**
Sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, soit $f_n(x) = \mathbf{1}_{[n, n+1]}(x)$.
- $f_n \ge 0$ (positivité).
- $f_n(x) \to 0$ simplement pour tout $x \in \mathbb{R}$. Donc $f = 0$.
- Mais $\int_{\mathbb{R}} f_n d\lambda = 1$ pour tout $n$.
- Ainsi : $\lim_{n \to \infty} \int f_n = 1 \neq \int \lim f_n = \int 0 = 0$.
Pourquoi le théorème échoue-t-il ? Car la suite $(f_n)$ **n'est pas croissante**. En un point $x$, la fonction prend la valeur 1, puis retombe à 0.

## 3. Démonstration du Théorème de Convergence Monotone

La démonstration est un modèle de rigueur constructiviste. Nous devons montrer deux inégalités : $\int f \le \lim \int f_n$ et $\int f \ge \lim \int f_n$.

**Étape 1 : Inégalité évidente ($\ge$)**
Puisque $(f_n)$ est croissante et tend vers $f$, on a $f_n \le f$ pour tout $n$.
Par monotonie de l'intégrale, on a pour tout $n \in \mathbb{N}$ :
$$\int_X f_n d\mu \le \int_X f d\mu$$
La suite $\left(\int_X f_n d\mu\right)$ est une suite croissante de réels (ou $+\infty$). Elle admet donc une limite dans $[0, +\infty]$. En passant à la limite :
$$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu$$

**Étape 2 : Inégalité subtile ($\le$)**
L'idée de génie de Lebesgue est d'approcher $f$ non pas par en haut, mais par en bas avec des fonctions simples (étagées).
Rappelons que par définition, $\int_X f d\mu = \sup \left\{ \int_X s d\mu \mid s \text{ fonction simple mesurable, } 0 \le s \le f \right\}$.

Soit $s$ une fonction simple mesurable telle que $0 \le s \le f$.
Soit une constante $\alpha \in ]0, 1[$.
Considérons les ensembles de niveau définis par :
$$A_n = \{ x \in X \mid f_n(x) \ge \alpha s(x) \}$$

- Puisque $(f_n)$ est croissante, la suite d'ensembles $(A_n)$ est une **suite croissante d'ensembles** ($A_n \subset A_{n+1}$).
- Puisque $\lim f_n(x) = f(x) \ge s(x)$, pour tout $x$ tel que $s(x) > 0$, on aura pour $n$ assez grand $f_n(x) \ge \alpha s(x)$ (car $\alpha < 1$).
- Si $s(x) = 0$, $x \in A_n$ pour tout $n$.
- Donc, $\bigcup_{n \in \mathbb{N}} A_n = X$.

Maintenant, évaluons l'intégrale de $f_n$ :
$$\int_X f_n d\mu \ge \int_{A_n} f_n d\mu \ge \int_{A_n} \alpha s d\mu = \alpha \int_{A_n} s d\mu$$
(où $\int_{A_n} s d\mu = \int_X s \cdot \mathbf{1}_{A_n} d\mu$).

Puisque $s$ est simple, elle s'écrit $s = \sum_{i=1}^k c_i \mathbf{1}_{E_i}$. Alors :
$$\int_{A_n} s d\mu = \sum_{i=1}^k c_i \mu(E_i \cap A_n)$$
Comme $(A_n)$ croît vers $X$, la suite d'ensembles $(E_i \cap A_n)$ croît vers $E_i \cap X = E_i$.
Par **continuité séquentielle monotone croissante de la mesure** $\mu$, on a :
$$\lim_{n \to \infty} \mu(E_i \cap A_n) = \mu(E_i)$$
Donc :
$$\lim_{n \to \infty} \int_{A_n} s d\mu = \sum_{i=1}^k c_i \mu(E_i) = \int_X s d\mu$$

En passant à la limite dans notre inégalité précédente :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \alpha \int_X s d\mu$$

Cette inégalité est vraie pour tout $\alpha \in ]0, 1[$. En faisant tendre $\alpha \to 1$ par valeurs inférieures :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu$$

Enfin, cette inégalité est vraie pour *toute* fonction simple $s$ telle que $0 \le s \le f$.
En prenant le supremum sur toutes ces fonctions simples $s$, on obtient par définition de l'intégrale de $f$ :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \sup_s \int_X s d\mu = \int_X f d\mu$$

**Étape 3 : Conclusion**
Les deux inégalités montrent que $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$. La démonstration est complète, sans aucune ellipse.

## 4. Applications en Théorie des Probabilités et en Intelligence Artificielle

### Probabilités : Espérance de variables aléatoires

En probabilités, l'espace mesuré est $(\Omega, \mathcal{F}, \mathbb{P})$, l'intégrale devient l'espérance mathématique $\mathbb{E}[X] = \int_\Omega X d\mathbb{P}$. Le théorème de Beppo Levi garantit que si l'on a une suite de variables aléatoires positives croissantes $X_n \le X_{n+1}$ presque sûrement, alors l'espérance de la limite (même infinie) est la limite des espérances.

### Fonctions de Coût et Risque Empirique en Machine Learning

Dans les modèles d'apprentissage profond, la fonction de risque théorique est définie comme $R(w) = \mathbb{E}_{(x,y) \sim P}[L(f_w(x), y)]$ où $L$ est une fonction de perte positive.
Si l'on construit une architecture complexe par des blocs d'approximation successifs (par exemple une série de réseaux de neurones résiduels) telle que la perte de l'approximation croît vers la perte d'un modèle abstrait limite idéal, le TCM garantit que le risque converge.

### Optimisation et Processus Discrets (Méthodes de Monte-Carlo)

Le corollaire d'intégration terme à terme est au cœur de l'analyse des algorithmes MCMC (Markov Chain Monte Carlo). Lorsqu'on cherche à évaluer une distribution invariante complexe, on exprime souvent la densité limite comme une série infinie de noyaux de transition. Le TCM (pour les noyaux positifs) autorise formellement à intervertir la série (la somme des étapes temporelles) avec l'intégration (l'espérance spatiale sur l'espace d'état). Sans Beppo Levi, les garanties mathématiques de l'échantillonnage de Gibbs (Gibbs Sampling) ou de l'algorithme Metropolis-Hastings seraient impossibles à asseoir rigoureusement en dimension infinie.

---
