---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[jalon-66/Jalon-66.md]]"
next: "[[jalon-68/Jalon-68.md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Genèse du concept et intuition géométrique

Avant l'avènement de l'intégrale de Lebesgue, la théorie de l'intégration (principalement dominée par l'approche de Riemann) se heurtait à un mur d'une rigidité absolue lors du passage à la limite. Si l'on considérait une suite de fonctions intégrables $f_n$ convergeant vers une fonction $f$, rien ne garantissait que $f$ fût elle-même intégrable, et encore moins que $\lim_{n \to \infty} \int f_n = \int \lim_{n \to \infty} f_n$. Les mathématiciens devaient exiger des conditions extrêmement fortes, comme la convergence uniforme, un luxe impensable dans les espaces fonctionnels rugueux de la physique mathématique moderne.

Le théorème de convergence monotone, formulé par Beppo Levi (1906), fait voler en éclats cette restriction. Il stipule que si une suite de fonctions mesurables positives "gonfle" (croît) vers une limite, alors l'intégrale suit le mouvement, sans aucune condition supplémentaire sur la limite elle-même ou sur la "vitesse" de la convergence. Géométriquement, imaginez un volume complexe que l'on remplit par des couches successives de plus en plus fines par le bas. L'aire sous la courbe limite est exactement la limite des aires des approximations par défaut. C'est l'essence même du constructivisme lebesguien : on contrôle le processus par l'ordre (la monotonie) plutôt que par la topologie fine.

## 2. Structures, Énoncés et Exemples Concrets

### A. Le Théorème de Convergence Monotone

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré abstrait.

**Théorème (Beppo Levi) :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables définies sur $X$ et à valeurs dans $[0, +\infty]$.
On suppose que pour presque tout $x \in X$, la suite $(f_n(x))_{n \in \mathbb{N}}$ est croissante :
$$ \forall n \in \mathbb{N}, \quad f_n(x) \le f_{n+1}(x) \quad \text{pour } \mu\text{-presque tout } x. $$
Alors, la fonction limite $f(x) = \lim_{n \to \infty} f_n(x)$ (qui existe dans $[0, +\infty]$) est mesurable, et on a l'égalité fondamentale :
$$ \int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu. $$

**Exemple Concret 1 (La pile de cylindres infinitésimaux) :**
Considérons $X = [0, 1]$ muni de la mesure de Lebesgue. Soit $f_n(x) = nx$ si $x \in [0, 1/n]$, et $f_n(x) = 1$ si $x \in ]1/n, 1]$.
Observons la monotonie : Pour un $x$ fixé, dès que $n > 1/x$, $f_n(x) = 1$. Donc la suite croît vers la fonction constante $f(x) = 1$ pour $x > 0$.
Calculons les intégrales des $f_n$ :
$\int_0^1 f_n(x) dx = \int_0^{1/n} nx \, dx + \int_{1/n}^1 1 \, dx = n \left[\frac{x^2}{2}\right]_0^{1/n} + (1 - 1/n) = \frac{1}{2n} + 1 - \frac{1}{n} = 1 - \frac{1}{2n}$.
La limite des intégrales est $\lim (1 - \frac{1}{2n}) = 1$.
Et l'intégrale de la limite est $\int_0^1 1 \, dx = 1$. L'égalité est parfaite, même si la limite ponctuelle présente une discontinuité en 0.

**Exemple Concret 2 (La série géométrique comme intégrale) :**
Sur l'espace $\mathbb{N}$ muni de la mesure de comptage $\mu$, intégrer une fonction équivaut à sommer la série de ses valeurs.
Soit $f_n(k) = r^k \mathbf{1}_{\{k \le n\}}$, pour $r \in ]0, 1[$.
La suite $(f_n)$ est trivialement positive et croissante vers $f(k) = r^k$ pour tout $k \in \mathbb{N}$.
On a $\int_{\mathbb{N}} f_n \, d\mu = \sum_{k=0}^n r^k = \frac{1 - r^{n+1}}{1 - r}$.
Par Beppo Levi, $\lim \int f_n = \frac{1}{1-r}$. Et l'intégrale de la limite est bien $\int_{\mathbb{N}} f \, d\mu = \sum_{k=0}^\infty r^k = \frac{1}{1-r}$.

**Exemple Concret 3 (Explosion de la masse) :**
Prenons $f_n(x) = n \mathbf{1}_{]0, 1/n[}(x)$ sur $X = \mathbb{R}$.
Ici, $f_n(x)$ converge vers $0$ partout (pour tout $x>0$, dès que $n>1/x$, $f_n(x)=0$).
Cependant, $f_n$ n'est pas croissante ! Le théorème ne s'applique pas.
En effet, $\int f_n = n \times (1/n) = 1$. Donc $\lim \int f_n = 1$, mais $\int \lim f_n = \int 0 = 0$. Le théorème exige impérativement la croissance pour éviter que la "masse" ne s'échappe vers des singularités.

### B. Le Corollaire d'Intégration des Séries

Une conséquence vertigineuse de Beppo Levi est la manipulation des séries de fonctions positives.

**Théorème (Sommation terme à terme de Lebesgue) :**
Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables **positives**. Alors :
$$ \int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n \, d\mu. $$

**Exemple Concret 4 (L'intégrale de Gauss-Poisson) :**
On veut évaluer $I = \int_{]0, 1[} \sum_{n=1}^\infty \frac{x^n}{n} dx$.
Les fonctions $u_n(x) = \frac{x^n}{n}$ sont strictement positives sur $]0, 1[$.
Par le théorème d'intégration des séries :
$I = \sum_{n=1}^\infty \int_0^1 \frac{x^n}{n} dx = \sum_{n=1}^\infty \frac{1}{n} \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \sum_{n=1}^\infty \frac{1}{n(n+1)}$.
Par décomposition en éléments simples : $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$.
La série est télescopique : $I = \lim_{N \to \infty} \sum_{n=1}^N \left( \frac{1}{n} - \frac{1}{n+1} \right) = \lim_{N \to \infty} \left( 1 - \frac{1}{N+1} \right) = 1$.
Le passage de l'intégrale complexe à la série élémentaire est rendu licite, d'un coup de scalpel, par Beppo Levi.

**Exemple Concret 5 (L'intégrale exponentielle) :**
Considérons $\int_0^\infty e^{-x} x^{z-1} dx$ pour $z > 0$ (la fonction Gamma d'Euler).
Utilisons le développement en série : $e^{-x} = \sum_{n=0}^\infty \frac{(-1)^n x^n}{n!}$.
Attention, ici la série **n'est pas à termes positifs** ! On ne peut pas appliquer le corollaire directement pour intervertir somme et intégrale sur tout l'intervalle $[0, +\infty[$. C'est un cas limite classique. Il faudra utiliser le théorème de convergence dominée (Jalon suivant) pour traiter le cas des signes alternés.

## 3. Démonstration Fondamentale du Théorème de Beppo Levi

Nous procédons par une démonstration en trois temps, rigoureuse et exhaustive.

**Étape 1 : Monotonie de l'intégrale et première inégalité.**
Puisque $f_n(x) \le f_{n+1}(x) \le f(x)$ pour tout $n$ (presque partout), on a par croissance de l'intégrale (établie pour les fonctions mesurables positives) :
$$ \int_X f_n \, d\mu \le \int_X f_{n+1} \, d\mu \le \int_X f \, d\mu. $$
La suite réelle des intégrales est donc croissante et majorée par $\int f \, d\mu$. Elle admet une limite (éventuellement $+\infty$), et on obtient immédiatement la majoration :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \le \int_X f \, d\mu. $$

**Étape 2 : L'approximation par le bas (le coeur de Lebesgue).**
Il nous faut prouver l'inégalité inverse. C'est ici qu'intervient l'idée géniale de Lebesgue : approcher la fonction limite $f$ par le bas avec une fonction étagée simple $s$ telle que $0 \le s \le f$.
Fixons une constante arbitraire $\alpha \in ]0, 1[$.
Définissons les ensembles :
$$ A_n = \{ x \in X \mid f_n(x) \ge \alpha s(x) \}. $$
Puisque $f_n \le f_{n+1}$, il est immédiat que $A_n \subset A_{n+1}$. Les $A_n$ forment une suite croissante de sous-ensembles mesurables.
De plus, si on prend un $x \in X$ tel que $s(x) > 0$, alors $\alpha s(x) < s(x) \le f(x)$. Comme $f_n(x) \to f(x)$, il existera forcément un rang $N$ à partir duquel $f_N(x) \ge \alpha s(x)$. Donc $x \in A_N$.
Si $s(x) = 0$, $x \in A_1$ trivialement.
Ainsi, l'union des $A_n$ couvre l'espace tout entier : $\bigcup_{n \in \mathbb{N}} A_n = X$.

**Étape 3 : Passage à la limite sur la mesure.**
On a la minoration suivante sur l'espace total $X$ :
$$ \int_X f_n \, d\mu \ge \int_{A_n} f_n \, d\mu \ge \int_{A_n} \alpha s \, d\mu = \alpha \int_{A_n} s \, d\mu. $$
Rappelons que l'intégrale d'une fonction étagée sur un ensemble $A_n$ est la somme finie $\sum_{i} c_i \mu(E_i \cap A_n)$.
Puisque $A_n \uparrow X$, par continuité croissante de la mesure $\mu$, $\mu(E_i \cap A_n) \uparrow \mu(E_i \cap X) = \mu(E_i)$.
Donc :
$$ \lim_{n \to \infty} \int_{A_n} s \, d\mu = \int_X s \, d\mu. $$
En passant à la limite dans l'inégalité de l'Étape 3, on obtient :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \alpha \int_X s \, d\mu. $$
Cette relation est vraie pour tout $\alpha < 1$. En faisant tendre $\alpha \to 1$, il vient :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \int_X s \, d\mu. $$
Enfin, cette inégalité est vraie pour *toute* fonction étagée $s \le f$. Par définition même de l'intégrale de Lebesgue pour $f$ (qui est le suprémum des intégrales des fonctions étagées la minorant), on a :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \sup_{0 \le s \le f} \int_X s \, d\mu = \int_X f \, d\mu. $$
Les deux inégalités (Étape 1 et Étape 3) forcent l'égalité. La démonstration est achevée.

## 4. Rôle dans l'Ingénierie de l'IA et de l'Apprentissage Machine

Dans les fondations théoriques du Deep Learning, Beppo Levi est le garant silencieux de nos opérations sur les espérances mathématiques.

1.  **Fonctions de perte et Espérance (Risk Minimization) :**
    Le risque théorique d'un modèle est $\mathcal{R}(\theta) = \mathbb{E}_{(x,y)}[\mathcal{L}(f_\theta(x), y)]$. Souvent, on approche ce risque par des sommes (Risque empirique). Si la fonction de perte est positive (comme la Cross-Entropy), Beppo Levi justifie que la limite d'une suite de modèles approchant de mieux en mieux un processus complexe convergera en espérance vers la perte de la limite.
2.  **Apprentissage par renforcement (MDP à horizon infini) :**
    La valeur d'état $V(s) = \mathbb{E}[\sum_{t=0}^\infty \gamma^t R_{t+1} | S_0=s]$ implique l'espérance d'une somme infinie. C'est exactement le corollaire d'intégration des séries de Beppo Levi (puisque les récompenses escomptées $R$ pour les problèmes standards de contrôle positif forment une série positive) qui permet de manipuler les équations de Bellman avec une rigueur absolue.
3.  **Théorie de l'Information (Divergence KL) :**
    La divergence de Kullback-Leibler $D_{KL}(P || Q) = \int p(x) \log \frac{p(x)}{q(x)} dx$. Lors de l'entraînement d'Autoencodeurs Variationnels (VAE), on approxime cette intégrale. La justification que l'optimisation limite des approximations variationnelles converge bien vers la KL vraie repose sur la topologie mesurable dont Beppo Levi est la clé de voûte.
