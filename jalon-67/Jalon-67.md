---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[jalon-66/Jalon-66.md]]"
next: "[[jalon-68/Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo-Levi)

## 1. Origines et intuitions physiques

À la fin du XIXe siècle, les mathématiciens, dont Henri Lebesgue, cherchent à dépasser les limites de l'intégrale de Riemann, qui échoue souvent face aux passages à la limite. Imaginez que vous accumuliez continuellement de l'énergie thermique dans un système, modélisée par une suite croissante de fonctions de densité d'énergie. Riemann ne peut garantir que l'énergie totale limite (l'intégrale de la limite) correspond à la limite des énergies calculées à chaque étape. Le mathématicien italien Beppo Levi (1906) formule alors un résultat fondamental qui constitue le cœur de la théorie de l'intégration moderne : si des grandeurs positives s'accumulent sans jamais décroître, l'intégrale "commute" avec la limite. Ce théorème est la pierre angulaire qui permet aux physiciens et aux statisticiens de manipuler des séries infinies avec une rigueur absolue.

## 2. Formalisation du théorème et exemples fondateurs

### A. Le Théorème de Convergence Monotone

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.

**Théorème (Beppo-Levi) :** Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
Si la suite est croissante presque partout, c'est-à-dire :
$$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \mu\text{-p.p.}$$
Alors, la fonction limite $f = \lim_{n \to +\infty} f_n$ (qui existe $\mu$-p.p. dans $[0, +\infty]$) est mesurable, et on a l'égalité fondamentale :
$$\int_X f \, d\mu = \lim_{n \to +\infty} \int_X f_n \, d\mu$$

**Typage des éléments :**
- $X$ : l'espace fondamental.
- $\mathcal{A}$ : une tribu (ou $\sigma$-algèbre) sur $X$.
- $\mu : \mathcal{A} \to [0, +\infty]$ : une mesure positive.
- $f_n : X \to [0, +\infty]$ : des fonctions prenant leurs valeurs dans les réels positifs étendus (incluant $+\infty$).

**Exemple de calcul : L'escalier vers l'infini**
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Soit $f_n(x) = \mathbf{1}_{[0, n]}(x) \cdot \left(1 - \frac{x}{n}\right)$ pour $n \ge 1$.
Pour tout $x \ge 0$, dès que $n$ est assez grand, $1 - \frac{x}{n}$ croît vers $1$. Ainsi, la suite $(f_n)$ est croissante et converge simplement vers $f(x) = \mathbf{1}_{[0, +\infty[}(x)$.
Calculons les intégrales :
$\int_\mathbb{R} f_n(x) d\lambda(x) = \int_0^n (1 - \frac{x}{n}) dx = \left[x - \frac{x^2}{2n}\right]_0^n = n - \frac{n}{2} = \frac{n}{2}$.
La limite de ces intégrales lorsque $n \to +\infty$ est $+\infty$.
Du côté de la limite : $\int_\mathbb{R} f(x) d\lambda(x) = \int_0^{+\infty} 1 dx = +\infty$.
L'égalité est vérifiée : $+\infty = +\infty$.

### B. Corollaire : Sommation terme à terme

**Théorème :** Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$. Alors :
$$\int_X \left( \sum_{n=0}^{+\infty} u_n \right) d\mu = \sum_{n=0}^{+\infty} \int_X u_n \, d\mu$$

**Exemple d'application immédiate :**
Évaluons $\int_{]0, 1[} \frac{1}{1-x} dx$.
On sait que pour $x \in ]0, 1[$, on a le développement en série entière : $\frac{1}{1-x} = \sum_{n=0}^{+\infty} x^n$.
Posons $u_n(x) = x^n$. Les $u_n$ sont positives et mesurables. On applique le corollaire :
$\int_0^1 \left(\sum_{n=0}^{+\infty} x^n\right) dx = \sum_{n=0}^{+\infty} \int_0^1 x^n dx = \sum_{n=0}^{+\infty} \frac{1}{n+1}$.
On reconnaît la série harmonique, qui diverge. Ainsi l'intégrale vaut $+\infty$.

### C. Contre-exemple si l'on retire l'hypothèse de positivité ou de monotonie

**Cas pathologique (Défaut de monotonie) :**
Soit $f_n(x) = n \mathbf{1}_{]0, 1/n]}(x)$ sur l'espace de Lebesgue.
Ici, $f_n \ge 0$, mais la suite n'est *pas* croissante. En effet, $f_n(x)$ converge vers $f(x) = 0$ pour tout $x > 0$.
L'intégrale de la limite est $\int f d\lambda = 0$.
Mais pour tout $n$, $\int f_n d\lambda = n \times \frac{1}{n} = 1$.
On a bien $\lim \int f_n \neq \int \lim f_n$. Ce phénomène est appelé "perte de masse vers l'infini local".

## 3. Démonstrations rigoureuses

### Preuve du Théorème de Convergence Monotone

Soit $(f_n)$ une suite croissante de fonctions mesurables positives. Notons $f = \lim_{n \to +\infty} f_n$.
Puisque pour tout $n$, $f_n \le f$, la monotonie de l'intégrale (établie au Jalon 66) implique que :
$$\int_X f_n \, d\mu \le \int_X f \, d\mu$$
En passant à la limite (qui existe car la suite des intégrales est croissante dans $[0, +\infty]$) :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \le \int_X f \, d\mu \quad \text{(Équation 1)}$$

Pour l'inégalité inverse, nous devons revenir à la définition de l'intégrale par les fonctions étagées.
Soit $s$ une fonction étagée mesurable telle que $0 \le s \le f$.
Soit un réel $c \in ]0, 1[$. Définissons les ensembles :
$$A_n = \{x \in X \mid f_n(x) \ge c \cdot s(x)\}$$
Les ensembles $A_n$ sont mesurables. Puisque $(f_n)$ est croissante, on a $A_n \subset A_{n+1}$.
De plus, si $s(x) = 0$, $x \in A_n$ trivialement. Si $s(x) > 0$, alors $c \cdot s(x) < s(x) \le f(x)$. Comme $f_n(x) \to f(x)$, il existe un rang $N$ tel que pour $n \ge N$, $f_n(x) \ge c \cdot s(x)$, donc $x \in A_n$.
Ainsi, $\bigcup_{n \in \mathbb{N}} A_n = X$.

Minorons l'intégrale de $f_n$ :
$$\int_X f_n \, d\mu \ge \int_{A_n} f_n \, d\mu \ge \int_{A_n} c \cdot s \, d\mu = c \int_{A_n} s \, d\mu$$
La fonction étagée s'écrit $s = \sum_{i=1}^k \alpha_i \mathbf{1}_{E_i}$.
Donc $\int_{A_n} s \, d\mu = \sum_{i=1}^k \alpha_i \mu(E_i \cap A_n)$.
Par la continuité croissante de la mesure $\mu$, puisque $E_i \cap A_n \nearrow E_i \cap X = E_i$, on a $\lim_{n \to +\infty} \mu(E_i \cap A_n) = \mu(E_i)$.
Ainsi, en passant à la limite quand $n \to +\infty$ :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \ge c \sum_{i=1}^k \alpha_i \mu(E_i) = c \int_X s \, d\mu$$
Puisque cette inégalité est vraie pour tout $c \in ]0, 1[$, on peut faire tendre $c \to 1$ :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X s \, d\mu$$
Cette minoration est vraie pour toute fonction étagée $s$ telle que $0 \le s \le f$. En passant au supremum sur toutes ces fonctions étagées $s$, par définition de l'intégrale de Lebesgue, on obtient :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X f \, d\mu \quad \text{(Équation 2)}$$

Les équations (1) et (2) prouvent que $\lim_{n \to +\infty} \int_X f_n \, d\mu = \int_X f \, d\mu$. $\blacksquare$

### Preuve du Corollaire (Séries)

Appliquons le TCM à la suite des sommes partielles $S_N = \sum_{n=0}^N u_n$.
Puisque les $u_n$ sont positives, la suite $(S_N)_N$ est croissante.
De plus, par linéarité de l'intégrale pour des sommes finies :
$$\int_X S_N \, d\mu = \sum_{n=0}^N \int_X u_n \, d\mu$$
La limite ponctuelle de $S_N$ est par définition la série $\sum_{n=0}^{+\infty} u_n$.
D'après le TCM :
$$\int_X \left( \sum_{n=0}^{+\infty} u_n \right) d\mu = \lim_{N \to +\infty} \int_X S_N \, d\mu = \lim_{N \to +\infty} \sum_{n=0}^N \int_X u_n \, d\mu = \sum_{n=0}^{+\infty} \int_X u_n \, d\mu$$
$\blacksquare$

## 4. Applications en Physique, Logique et IA

En Intelligence Artificielle et en Probabilités, le Théorème de Convergence Monotone est omniprésent.

- **Processus Stochastiques et Modèles Génératifs :** Lors du calcul de l'espérance mathématique d'une variable aléatoire définie comme un temps d'atteinte (par exemple, le nombre d'étapes de diffusion dans un Denoising Diffusion Probabilistic Model avant d'atteindre un niveau de bruit seuil), on est amené à évaluer l'espérance d'une somme infinie de variables de Bernoulli positives. Le TCM justifie l'inversion de l'espérance et de la série, assurant la convergence de l'algorithme d'entraînement.
- **Théorie de l'Information :** Dans l'étude des capacités de canaux (Théorème de Shannon), on manipule des entropies différentielles où l'on intègre des densités de probabilités développées en séries (via des polynômes orthogonaux). La stricte positivité des termes permet, par le corollaire de Beppo-Levi, de sommer les intégrales terme à terme pour trouver la borne supérieure théorique de la transmission.
- **Calcul des Variations et Réseaux de Neurones Physiques (PINNs) :** Lorsqu'on cherche à minimiser une fonctionnelle d'énergie (Loss function incluant des contraintes d'équations aux dérivées partielles), on utilise souvent des suites régularisantes. L'accumulation de termes de pénalisation positifs permet, via le TCM, de prouver la semi-continuité inférieure de la Loss totale, garantissant ainsi l'existence d'un minimiseur global (le réseau de neurones optimal).
