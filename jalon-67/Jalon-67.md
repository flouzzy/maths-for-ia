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

## 1. Naissance d'une vision nouvelle de l'intégration

La théorie de l'intégration développée par Bernhard Riemann au milieu du XIXe siècle représentait une avancée majeure pour formaliser le concept d'aire sous une courbe. Cependant, elle s'est rapidement heurtée à des limites structurelles incontournables face au comportement de certaines suites de fonctions. En particulier, l'espace des fonctions intégrables au sens de Riemann n'est pas complet : la limite d'une suite de fonctions intégrables n'est pas toujours intégrable.

Le mathématicien italien Beppo Levi, prolongeant les travaux révolutionnaires d'Henri Lebesgue, a formulé au début du XXe siècle un théorème qui constitue la pierre angulaire de l'intégration moderne. Face à l'impossibilité de garantir la stabilité des intégrales de Riemann lors de passages à la limite simples, Levi a identifié une condition d'une élégance absolue : la croissance de la suite. Géométriquement, si nous considérons une séquence de fonctions positives qui ne font que croître, approchant une fonction limite par le dessous, l'aire sous ces courbes approche nécessairement l'aire de la courbe limite. Ce résultat, profondément intuitif sur le plan visuel, exige une rigueur implacable pour être démontré dans le cadre abstrait de la théorie de la mesure. Il libère l'analyste des contraintes étouffantes de la convergence uniforme, permettant d'intervertir limite et intégrale sous la seule hypothèse de monotonie.

## 2. Définitions et Théorème de Beppo Levi

Avant d'énoncer le théorème principal, nous rappelons que nous travaillons dans un espace mesuré général $(X, \mathcal{F}, \mu)$, où $\mathcal{F}$ est une tribu sur $X$ et $\mu$ une mesure positive.

> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables définies sur un espace mesuré $(X, \mathcal{F}, \mu)$, à valeurs dans $\overline{\mathbb{R}}_+ = [0, +\infty]$.
> Si la suite $(f_n)_{n \in \mathbb{N}}$ est croissante presque partout (p.p.), c'est-à-dire :
> $$\forall n \in \mathbb{N}, \quad f_n(x) \leq f_{n+1}(x) \quad \text{pour } \mu\text{-presque tout } x \in X$$
> Alors, la fonction limite ponctuelle $f = \lim_{n \to +\infty} f_n = \sup_{n \in \mathbb{N}} f_n$ est mesurable et positive, et :
> $$\int_X f \, d\mu = \lim_{n \to +\infty} \int_X f_n \, d\mu = \sup_{n \in \mathbb{N}} \int_X f_n \, d\mu$$

**Exemple Calculatoire Immédiat :**
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$ où $\lambda$ est la mesure de Lebesgue.
Soit la suite de fonctions $f_n(x) = \chi_{[0, n]}(x) \left(1 - \frac{x}{n}\right)^n$, où $\chi_{[0, n]}$ est la fonction indicatrice de l'intervalle $[0, n]$.
Pour tout $x \ge 0$ fixé, la suite $\left(1 - \frac{x}{n}\right)^n$ est croissante pour $n > x$ et converge ponctuellement vers $e^{-x}$. Ainsi, $(f_n)$ est une suite croissante de fonctions mesurables positives convergeant ponctuellement vers $f(x) = e^{-x} \chi_{[0, +\infty[}(x)$.
Le théorème de Beppo Levi garantit que l'intégrale de la limite est la limite des intégrales :
$$\int_{\mathbb{R}} f(x) \, d\lambda(x) = \lim_{n \to +\infty} \int_{\mathbb{R}} f_n(x) \, d\lambda(x)$$
Calculons l'intégrale de $f_n$ :
$$\int_{\mathbb{R}} f_n(x) \, d\lambda(x) = \int_0^n \left(1 - \frac{x}{n}\right)^n dx$$
Effectuons le changement de variable affine $u = 1 - \frac{x}{n}$, donc $dx = -n \, du$. Les bornes deviennent $u=1$ pour $x=0$, et $u=0$ pour $x=n$.
$$\int_0^n \left(1 - \frac{x}{n}\right)^n dx = \int_1^0 u^n (-n \, du) = n \int_0^1 u^n \, du = n \left[ \frac{u^{n+1}}{n+1} \right]_0^1 = \frac{n}{n+1}$$
La limite lorsque $n \to +\infty$ de cette intégrale est $1$.
D'autre part, calculons l'intégrale de la limite :
$$\int_0^{+\infty} e^{-x} dx = \left[ -e^{-x} \right]_0^{+\infty} = 1$$
Le résultat est parfaitement cohérent, et le passage à la limite sous le signe intégral est ici rigoureusement validé par la monotonie de la suite.

**Corollaire : Sommation de séries à termes positifs**
> Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives sur $X$. Alors :
> $$\int_X \left( \sum_{n=0}^{+\infty} u_n \right) d\mu = \sum_{n=0}^{+\infty} \int_X u_n \, d\mu$$
Ce résultat fondamental permet d'intervertir sans condition série et intégrale dès lors que les termes sont de signe constant (positif).

**Cas limites et configurations pathologiques :**
Si l'hypothèse de positivité ou de croissance n'est pas respectée, le théorème tombe en défaut.
Considérons $f_n(x) = \frac{1}{n} \chi_{[0, n]}(x)$. Cette suite converge ponctuellement vers $f(x) = 0$ pour tout $x \in \mathbb{R}$.
Cependant, $\int_{\mathbb{R}} f_n \, d\lambda = \int_0^n \frac{1}{n} dx = 1$ pour tout $n$, donc $\lim_{n \to +\infty} \int f_n = 1$.
Mais $\int_{\mathbb{R}} f \, d\lambda = \int_{\mathbb{R}} 0 \, d\lambda = 0$.
L'égalité n'est pas vérifiée car la suite $(f_n)$ n'est pas croissante (par exemple pour $x \in [0, 1]$, $f_1(x) = 1$, $f_2(x) = 1/2$, donc $f_2 \le f_1$). Ce contre-exemple justifie l'introduction future du Lemme de Fatou et du Théorème de Convergence Dominée.

## 3. Démonstration Rigoureuse

Nous allons démontrer le Théorème de Convergence Monotone dans le cas où l'inégalité de croissance est vraie partout (la généralisation au cas "presque partout" se fait aisément en restreignant l'espace au sous-ensemble de mesure pleine où la croissance est vraie).

Soit $(f_n)$ une suite de fonctions mesurables positives telles que $f_n \le f_{n+1}$ pour tout $n$.
Posons $f(x) = \sup_n f_n(x) = \lim_{n \to \infty} f_n(x)$. Comme borne supérieure d'une suite de fonctions mesurables, $f$ est mesurable.

**Étape 1 : Inégalité évidente**
Puisque $f_n \le f_{n+1}$ pour tout $n$, la suite numérique $\left( \int_X f_n \, d\mu \right)$ est croissante dans $[0, +\infty]$. Elle admet donc une limite.
De plus, pour tout $n$, nous avons $f_n \le f$. Par croissance de l'intégrale de Lebesgue :
$$\int_X f_n \, d\mu \le \int_X f \, d\mu$$
En passant à la limite (ou au supremum) sur $n$ :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \le \int_X f \, d\mu$$

**Étape 2 : Inégalité inverse (l'argument central)**
Il nous faut prouver que $\int_X f \, d\mu \le \lim_{n \to +\infty} \int_X f_n \, d\mu$.
Rappelons la définition de l'intégrale d'une fonction positive $f$ :
$$\int_X f \, d\mu = \sup \left\{ \int_X s \, d\mu \;\middle|\; s \text{ est une fonction étagée mesurable, et } 0 \le s \le f \right\}$$
Soit $s$ une telle fonction étagée vérifiant $0 \le s(x) \le f(x)$ pour tout $x \in X$.
Soit une constante $c \in ]0, 1[$. Nous considérons l'ensemble :
$$A_n = \{ x \in X \mid f_n(x) \ge c \cdot s(x) \}$$
Puisque $(f_n)$ est croissante, il est clair que $A_n \subset A_{n+1}$ pour tout $n$.
De plus, nous affirmons que $\bigcup_{n=1}^\infty A_n = X$.
En effet, soit $x \in X$.
- Si $f(x) = 0$, alors $s(x) = 0$, donc $c \cdot s(x) = 0$. Puisque $f_n(x) \ge 0$, on a $f_n(x) \ge c \cdot s(x)$ pour tout $n$, donc $x \in A_1$.
- Si $f(x) > 0$, alors puisque $c < 1$, nous avons strictement $c \cdot s(x) < f(x)$. Comme $f_n(x) \to f(x)$, par définition de la limite, il existe un rang $N$ tel que pour tout $n \ge N$, $f_n(x) \ge c \cdot s(x)$. Donc $x \in A_N$.

Maintenant, évaluons l'intégrale de $f_n$ :
$$\int_X f_n \, d\mu \ge \int_{A_n} f_n \, d\mu \ge \int_{A_n} c \cdot s \, d\mu = c \int_{A_n} s \, d\mu$$
La fonction $s$ est étagée, elle s'écrit $s = \sum_{i=1}^k \alpha_i \chi_{E_i}$. Donc :
$$\int_{A_n} s \, d\mu = \sum_{i=1}^k \alpha_i \mu(E_i \cap A_n)$$
La suite d'ensembles $(E_i \cap A_n)_{n \in \mathbb{N}}$ est une suite croissante d'ensembles dont l'union est $E_i \cap X = E_i$.
Par la propriété de continuité séquentielle croissante de la mesure $\mu$, nous avons :
$$\lim_{n \to +\infty} \mu(E_i \cap A_n) = \mu\left(\bigcup_{n=1}^\infty (E_i \cap A_n)\right) = \mu(E_i)$$
Par conséquent, en passant à la limite quand $n \to +\infty$ dans notre inégalité :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \ge c \lim_{n \to +\infty} \int_{A_n} s \, d\mu = c \sum_{i=1}^k \alpha_i \mu(E_i) = c \int_X s \, d\mu$$
Nous avons donc $\lim_{n} \int_X f_n \, d\mu \ge c \int_X s \, d\mu$ pour tout $c \in ]0, 1[$.
En faisant tendre $c$ vers $1$ (par valeurs inférieures), nous obtenons :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X s \, d\mu$$
Cette inégalité est valide pour toute fonction étagée $s$ telle que $0 \le s \le f$.
En prenant le supremum sur l'ensemble de ces fonctions $s$, par définition de l'intégrale de $f$ :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X f \, d\mu$$
Les deux inégalités démontrent l'égalité recherchée. $\blacksquare$

## 4. Applications en Théorie de l'Information et Intelligence Artificielle

Le Théorème de Convergence Monotone ne se contente pas de consolider les fondations de l'analyse, il s'avère être un outil analytique omniprésent dans la modélisation statistique avancée et les théories d'apprentissage automatique.

1. **Calcul des Espérances Inconditionnelles (Expectation-Maximization) :**
Dans les algorithmes à variables latentes, tels que les modèles de mélange gaussien (GMM) optimisés par l'algorithme EM, nous sommes amenés à marginaliser sur un espace d'états potentiellement infini. L'espérance d'une fonction de vraisemblance décomposée en série de composantes positives repose fondamentalement sur le TCM. Il justifie rigoureusement la permutation entre l'opérateur d'espérance intégrale et la sommation infinie, assurant que l'accumulation des probabilités converge de manière cohérente vers la vraisemblance marginale du modèle.

2. **Divergence de Kullback-Leibler et Séries Entropiques :**
En théorie de l'information, l'entropie croisée (Cross-Entropy) et la divergence de Kullback-Leibler $D_{KL}(P || Q) = \int p(x) \log\left(\frac{p(x)}{q(x)}\right) dx$ jouent un rôle central dans l'apprentissage des modèles génératifs et discriminatifs profonds. Lorsque les densités de probabilité sont développées sous forme de limites de fonctions d'approximation (par exemple lors de l'estimation de densité par noyaux - KDE), le TCM, ou ses corollaires pour les séries, permet de justifier la convergence de la fonction de perte empirique vers la divergence théorique exacte sous des hypothèses de monotonie de l'approximation de densité.

3. **Inférence Variationnelle Bayésienne (Variational Inference) :**
Pour contourner les intégrales intraitables du théorème de Bayes en très grande dimension (typiques des réseaux de neurones bayésiens), l'inférence variationnelle transforme le problème d'intégration en un problème d'optimisation (maximisation de l'ELBO - Evidence Lower Bound). Les garanties théoriques de convergence des suites d'approximations variationnelles vers la borne optimale utilisent les propriétés de convergence des intégrales de Lebesgue, où les suites de limites successives, souvent monotones dans la réduction de l'écart KL, invoquent implicitement le TCM pour assurer la stabilité mathématique de la limite entropique.
