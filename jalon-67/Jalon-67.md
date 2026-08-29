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

## 1. Fondements Historiques et Intuition Géométrique

Historiquement, l'intégrale de Riemann a montré des limites structurelles sévères face aux processus limites continus et aux séries de fonctions. Le mathématicien italien Beppo Levi (1875-1961), dans ses travaux sur l'intégration de Lebesgue en 1906, a formalisé un principe de convergence qui constitue la pierre angulaire de l'analyse fonctionnelle moderne : si une suite de fonctions mesurables positives croît vers une fonction limite, alors l'intégrale de la limite est la limite des intégrales.

Géométriquement, considérez une suite de surfaces sous des courbes de plus en plus hautes, toutes minorées par $0$. Si ces courbes s'élèvent monotonement pour épouser une courbe "plafond", l'aire sous les courbes successives tendra exactement vers l'aire sous la courbe plafond. Ce théorème libère l'analyste de l'obligation de vérifier la stricte uniformité de la convergence (comme c'était le cas chez Riemann) pour intervertir limite et intégrale.

## 2. Définitions et Structures Fondamentales

Considérons un espace mesuré $(X, \mathcal{A}, \mu)$.

**Théorème 1 (Théorème de Convergence Monotone ou de Beppo Levi) :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions à valeurs dans $[0, +\infty]$, mesurables sur $(X, \mathcal{A})$.
On suppose que la suite est croissante presque partout :
$$ \forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \mu\text{-p.p.} $$
Alors, la fonction limite $f = \sup_{n \in \mathbb{N}} f_n = \lim_{n \to \infty} f_n$ est mesurable et :
$$ \int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu $$

**Exemple Concret 1 : Progression sur l'intervalle unité**
Considérons l'espace mesuré $([0,1], \mathcal{B}([0,1]), \lambda)$, où $\lambda$ est la mesure de Lebesgue.
Soit $f_n(x) = 1 - (1-x)^n$.
Pour tout $x \in [0,1]$, $(1-x)^n$ est décroissante par rapport à $n$, donc $f_n(x)$ est croissante.
La limite ponctuelle est $f(x) = 1$ pour $x \in (0,1]$ et $f(0) = 0$.
Calculons les intégrales :
$$ \int_0^1 f_n(x) \, dx = \left[ x + \frac{(1-x)^{n+1}}{n+1} \right]_0^1 = 1 - \frac{1}{n+1} $$
La limite de ces intégrales est $\lim_{n \to \infty} \left(1 - \frac{1}{n+1}\right) = 1$.
D'autre part, l'intégrale de la limite $f$ (qui vaut $1$ presque partout) est $\int_0^1 1 \, dx = 1$.
Les deux valeurs coïncident parfaitement, illustrant le théorème.

**Théorème 2 (Corollaire : Sommation de séries de fonctions positives) :**
Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives. Alors :
$$ \int_X \left( \sum_{n=0}^{\infty} u_n \right) d\mu = \sum_{n=0}^{\infty} \int_X u_n \, d\mu $$

**Exemple Concret 2 : Évaluation d'une intégrale par développement en série**
Évaluons $\int_0^1 \frac{x}{1-x^2} \, dx$ de manière rigoureuse. On sait que pour $x \in [0,1)$, $\frac{1}{1-x^2} = \sum_{n=0}^\infty x^{2n}$.
Posons $u_n(x) = x^{2n+1}$, des fonctions mesurables positives sur $([0,1], \mathcal{B}, \lambda)$.
$$ \int_0^1 \left( \sum_{n=0}^\infty x^{2n+1} \right) dx = \sum_{n=0}^\infty \int_0^1 x^{2n+1} \, dx = \sum_{n=0}^\infty \frac{1}{2n+2} $$
La série de terme général $\frac{1}{2(n+1)}$ diverge (série harmonique modifiée). L'intégrale vaut donc $+\infty$.

## 3. Démonstration Rigoureuse du Théorème de Beppo Levi

Procédons à la démonstration ligne par ligne du Théorème 1.
Soit $f = \lim_{n \to \infty} f_n$. La mesurabilité de $f$ découle de la stabilité des fonctions mesurables par passage à la limite supérieure.

**Étape 1 : Inégalité facile ($\int f \ge \lim \int f_n$)**
Pour tout $n \in \mathbb{N}$, par hypothèse de croissance, $f_n \le f$ presque partout.
La monotonie de l'intégrale de Lebesgue implique :
$$ \int_X f_n \, d\mu \le \int_X f \, d\mu $$
En passant à la limite (la suite des intégrales est croissante et admet une limite dans $\overline{\mathbb{R}}$) :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \le \int_X f \, d\mu $$

**Étape 2 : Inégalité fine ($\int f \le \lim \int f_n$)**
Soit $\varphi$ une fonction étagée positive telle que $0 \le \varphi \le f$.
Fixons un réel $\alpha \in (0, 1)$.
Définissons les ensembles mesurables pour chaque $n$ :
$$ A_n = \{ x \in X \mid f_n(x) \ge \alpha \varphi(x) \} $$
Puisque $(f_n)$ est croissante, la suite d'ensembles $(A_n)$ est une suite croissante pour l'inclusion : $A_n \subset A_{n+1}$.
De plus, si $x$ est tel que $\varphi(x) > 0$, alors $\alpha \varphi(x) < \varphi(x) \le f(x)$.
Comme $f_n(x) \to f(x)$, il existe $N$ tel que pour $n \ge N$, $f_n(x) \ge \alpha \varphi(x)$, donc $x \in A_n$.
Si $\varphi(x) = 0$, $x \in A_1$ trivialement.
Ainsi, $\bigcup_{n \in \mathbb{N}} A_n = X$.

Sur l'ensemble $A_n$, nous avons :
$$ \int_X f_n \, d\mu \ge \int_{A_n} f_n \, d\mu \ge \int_{A_n} \alpha \varphi \, d\mu = \alpha \int_{A_n} \varphi \, d\mu $$
Rappelons que pour une fonction étagée $\varphi = \sum_{i=1}^k c_i \mathbf{1}_{E_i}$, son intégrale sur $A_n$ s'écrit $\sum_{i=1}^k c_i \mu(E_i \cap A_n)$.
Par continuité séquentielle croissante de la mesure $\mu$, $\lim_{n \to \infty} \mu(E_i \cap A_n) = \mu(E_i \cap X) = \mu(E_i)$.
En passant à la limite quand $n \to \infty$ dans notre inégalité :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \alpha \int_X \varphi \, d\mu $$
Cette relation étant vraie pour tout $\alpha < 1$, en faisant tendre $\alpha \to 1$, nous obtenons :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \int_X \varphi \, d\mu $$
Par définition de l'intégrale pour les fonctions mesurables positives (le supremum sur toutes les fonctions étagées minorantes) :
$$ \lim_{n \to \infty} \int_X f_n \, d\mu \ge \sup_{0 \le \varphi \le f} \int_X \varphi \, d\mu = \int_X f \, d\mu $$

**Conclusion :**
Les deux inégalités établissent l'égalité : $\int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu$.

## 4. Applications en Analyse Fonctionnelle, Probabilités et IA

Le théorème de Beppo Levi transcende le simple cadre de l'intégration pour s'imposer en théorie de la mesure appliquée :
- **Probabilités :** Pour un espace probabilisé $(\Omega, \mathcal{F}, P)$, toute suite de variables aléatoires positives croissante $(X_n)$ vérifie $\mathbb{E}[\lim X_n] = \lim \mathbb{E}[X_n]$.
- **Intelligence Artificielle et PAC Learning :** En théorie de l'apprentissage statistique, le calcul de l'espérance de la perte (risque empirique vs risque vrai) s'appuie souvent sur des sommations infinies ou des limites de séquences de fonctions de coût. Pour garantir que l'approximation (somme finie) converge vers l'erreur globale théorique, le théorème de Beppo Levi garantit l'interversion de l'intégrale sur la distribution des données $\mathcal{D}$ et la limite.
- **Théorie de l'Information :** Dans l'analyse de l'entropie croisée, des suites de densités approchant une vraie distribution nécessitent une intégration de logarithmes et de densités. La convergence monotone assure la stabilité de ces métriques limites lors du processus d'optimisation par Descente de Gradient Stochastique.
