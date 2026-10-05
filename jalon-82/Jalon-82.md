---
uuid: "jalon-82"
title: "Introduction aux distributions de Schwartz"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 81 (Transformée de Fourier dans L2).md]]"
next: "[[Jalon 83 (Dérivation au sens des distributions).md]]"
---

# Jalon 82 : Introduction à la théorie des distributions de Schwartz

## 1. Introduction à la théorie des distributions

L'analyse réelle classique se heurte parfois à des limites sévères, notamment lorsqu'elle est confrontée à des phénomènes physiques idéalisés. En mécanique, comment modéliser un choc instantané ? En électromagnétisme, comment décrire la densité de charge d'une particule ponctuelle ? Ces objets, appelés communément "fonctions de Dirac" ou "impulsions", ne peuvent pas être définis rigoureusement en tant que fonctions classiques. En effet, une fonction $f$ qui vaudrait 0 partout sauf en un point et dont l'intégrale vaudrait 1 est une impossibilité dans le cadre de l'intégration de Lebesgue (car $\{0\}$ est de mesure nulle).

Dans les années 1940, le mathématicien français Laurent Schwartz a révolutionné l'analyse en introduisant la **théorie des distributions**. S'inspirant des travaux d'Oliver Heaviside et de Paul Dirac en physique, et de Sergei Sobolev en mathématiques, Schwartz a étendu la notion de fonction. Au lieu d'évaluer une fonction point par point, l'approche de Schwartz consiste à évaluer "l'effet" de l'objet sur une classe de fonctions très régulières, appelées **fonctions tests**. Cette idée est profondément physique : on ne mesure jamais l'état exact d'un système en un point précis, mais plutôt une moyenne locale pondérée par l'appareil de mesure (la fonction test).

La théorie des distributions permet de donner un sens rigoureux aux dérivées de fonctions non continues (comme la fonction échelon de Heaviside) et offre un cadre puissant pour la résolution des équations aux dérivées partielles.

## 2. Formalisation des distributions et de leur action sur les fonctions tests

Pour définir une distribution, nous devons d'abord préciser ce qu'est l'espace des fonctions tests.

### A. L'espace des fonctions tests $\mathcal{D}(\mathbb{R})$

> **Définition 1 (Espace des fonctions tests $\mathcal{D}(\mathbb{R})$) :**
> L'espace $\mathcal{D}(\mathbb{R})$ (ou $\mathcal{C}_c^\infty(\mathbb{R})$) est l'ensemble des fonctions $\phi : \mathbb{R} \to \mathbb{C}$ qui sont infiniment dérivables ($\mathcal{C}^\infty$) et à support compact. Le support d'une fonction $\phi$, noté $\text{Supp}(\phi)$, est l'adhérence de l'ensemble des points où $\phi$ ne s'annule pas : $\text{Supp}(\phi) = \overline{\{x \in \mathbb{R} \mid \phi(x) \neq 0\}}$.

**Exemple Concret 1 (La fonction "bosse" ou "bump function") :**
Considérons la fonction $\phi : \mathbb{R} \to \mathbb{R}$ définie par :
$$ \phi(x) = \begin{cases} \exp\left(-\frac{1}{1-x^2}\right) & \text{si } |x| < 1 \\ 0 & \text{si } |x| \ge 1 \end{cases} $$
- Le support de $\phi$ est l'intervalle fermé $[-1, 1]$, qui est compact.
- La fonction est clairement $\mathcal{C}^\infty$ sur $]-1, 1[$ et sur $]-\infty, -1[ \cup ]1, +\infty[$.
- En $x=1$ (et $x=-1$), on peut montrer par récurrence que toutes les dérivées à gauche tendent vers 0, assurant le raccordement $\mathcal{C}^\infty$ avec la partie identiquement nulle. Ainsi, $\phi \in \mathcal{D}(\mathbb{R})$.

Nous devons munir $\mathcal{D}(\mathbb{R})$ d'une topologie particulière, définie via la notion de convergence d'une suite de fonctions tests.

> **Définition 2 (Convergence dans $\mathcal{D}(\mathbb{R})$) :**
> Une suite $(\phi_n)_{n \in \mathbb{N}}$ de fonctions de $\mathcal{D}(\mathbb{R})$ converge vers $0$ dans $\mathcal{D}(\mathbb{R})$ si et seulement si :
> 1. Il existe un compact $K \subset \mathbb{R}$ tel que pour tout $n \in \mathbb{N}$, $\text{Supp}(\phi_n) \subset K$.
> 2. Pour tout entier $k \ge 0$, la suite des dérivées $(\phi_n^{(k)})_{n \in \mathbb{N}}$ converge uniformément vers $0$ sur $K$.

### B. Définition et exemples de distributions

> **Définition 3 (Distribution) :**
> Une **distribution** $T$ sur $\mathbb{R}$ est une forme linéaire continue sur $\mathcal{D}(\mathbb{R})$.
> - **Linéarité :** $\forall \phi, \psi \in \mathcal{D}(\mathbb{R}), \forall \lambda, \mu \in \mathbb{C}, \langle T, \lambda\phi + \mu\psi \rangle = \lambda\langle T, \phi \rangle + \mu\langle T, \psi \rangle$.
> - **Continuité :** Pour toute suite $(\phi_n)$ convergeant vers $0$ dans $\mathcal{D}(\mathbb{R})$, la suite de nombres complexes $\langle T, \phi_n \rangle$ converge vers $0$.
> L'ensemble des distributions sur $\mathbb{R}$ est noté $\mathcal{D}'(\mathbb{R})$.

**Exemple Concret 2 (Distribution de Dirac) :**
Fixons $a \in \mathbb{R}$. La distribution de Dirac au point $a$, notée $\delta_a$, est définie pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$ par :
$$ \langle \delta_a, \phi \rangle = \phi(a) $$
- **Linéarité :** $\langle \delta_a, \lambda\phi + \mu\psi \rangle = (\lambda\phi + \mu\psi)(a) = \lambda\phi(a) + \mu\psi(a) = \lambda\langle \delta_a, \phi \rangle + \mu\langle \delta_a, \psi \rangle$.
- **Continuité :** Si $(\phi_n)$ converge vers $0$ dans $\mathcal{D}(\mathbb{R})$, la convergence de $\phi_n$ vers 0 est en particulier uniforme, donc simple. Ainsi, $\phi_n(a) \to 0$, soit $\langle \delta_a, \phi_n \rangle \to 0$.
$\delta_a$ est bien une distribution. C'est l'exemple paradigmatique d'une distribution singulière.

> **Théorème 1 (Distributions régulières) :**
> Soit $f : \mathbb{R} \to \mathbb{C}$ une fonction localement intégrable (c'est-à-dire que pour tout segment $[a,b]$, $\int_a^b |f(x)|dx < \infty$). Alors l'application $T_f$ définie sur $\mathcal{D}(\mathbb{R})$ par :
> $$ \langle T_f, \phi \rangle = \int_{-\infty}^{+\infty} f(x)\phi(x)dx $$
> est une distribution, appelée distribution régulière associée à $f$.

**Exemple Concret 3 (Fonction de Heaviside) :**
La fonction de Heaviside $H$ est définie par $H(x) = 1$ si $x \ge 0$, et $H(x) = 0$ si $x < 0$. $H$ est localement intégrable (bornée). La distribution associée $T_H$ s'évalue par :
$$ \langle T_H, \phi \rangle = \int_{-\infty}^{+\infty} H(x)\phi(x)dx = \int_0^{+\infty} \phi(x)dx $$
Cette intégrale est bien définie car $\phi$ est à support compact.

## 3. Démonstrations

Dans cette section, nous démontrons le Théorème 1 concernant les distributions régulières.

**Démonstration du Théorème 1 (Régularité de $T_f$) :**
Soit $f \in L^1_{loc}(\mathbb{R})$. Définissons pour tout $\phi \in \mathcal{D}(\mathbb{R})$, $T_f(\phi) = \langle T_f, \phi \rangle = \int_{\mathbb{R}} f(x)\phi(x)dx$.

1.  **Linéarité :**
    Soient $\phi, \psi \in \mathcal{D}(\mathbb{R})$ et $\lambda, \mu \in \mathbb{C}$.
    $$ \langle T_f, \lambda\phi + \mu\psi \rangle = \int_{\mathbb{R}} f(x)(\lambda\phi(x) + \mu\psi(x))dx $$
    L'intégrale porte sur un domaine borné (l'union des supports de $\phi$ et $\psi$). Par linéarité de l'intégrale :
    $$ \langle T_f, \lambda\phi + \mu\psi \rangle = \lambda \int_{\mathbb{R}} f(x)\phi(x)dx + \mu \int_{\mathbb{R}} f(x)\psi(x)dx = \lambda\langle T_f, \phi \rangle + \mu\langle T_f, \psi \rangle $$
    La forme est bien linéaire.

2.  **Continuité :**
    Soit $(\phi_n)_{n \in \mathbb{N}}$ une suite de $\mathcal{D}(\mathbb{R})$ convergeant vers $0$.
    Par définition, il existe un compact $K = [a, b]$ tel que $\forall n \in \mathbb{N}, \text{Supp}(\phi_n) \subset K$, et la suite $(\phi_n)$ converge uniformément vers $0$ sur $K$. Notons $\|\phi_n\|_\infty = \sup_{x \in K} |\phi_n(x)|$, avec $\lim_{n \to \infty} \|\phi_n\|_\infty = 0$.
    Évaluons $T_f(\phi_n)$ :
    $$ \langle T_f, \phi_n \rangle = \int_{\mathbb{R}} f(x)\phi_n(x)dx = \int_K f(x)\phi_n(x)dx $$
    Majorons le module de cette valeur :
    $$ |\langle T_f, \phi_n \rangle| = \left| \int_K f(x)\phi_n(x)dx \right| \le \int_K |f(x)| \cdot |\phi_n(x)| dx $$
    Comme $\forall x \in K, |\phi_n(x)| \le \|\phi_n\|_\infty$, on a :
    $$ |\langle T_f, \phi_n \rangle| \le \|\phi_n\|_\infty \int_K |f(x)|dx $$
    Puisque $f \in L^1_{loc}(\mathbb{R})$, l'intégrale $\int_K |f(x)|dx$ est une constante finie, que nous noterons $C_K$. Ainsi :
    $$ |\langle T_f, \phi_n \rangle| \le C_K \|\phi_n\|_\infty $$
    Comme $\lim_{n \to \infty} \|\phi_n\|_\infty = 0$, on obtient par le théorème des gendarmes :
    $$ \lim_{n \to \infty} \langle T_f, \phi_n \rangle = 0 $$
    La forme linéaire $T_f$ est donc continue sur $\mathcal{D}(\mathbb{R})$, ce qui prouve que $T_f \in \mathcal{D}'(\mathbb{R})$. $\blacksquare$

## 4. Applications en Physique, Logique & Intelligence Artificielle

### A. Modélisation physique des phénomènes impulsionnels
La distribution de Dirac $\delta_a$ permet de modéliser avec précision des sources ponctuelles (charges électriques, masses ponctuelles) ou des phénomènes instantanés (un choc mécanique à $t=a$). L'utilisation des distributions justifie les calculs symboliques effectués par les ingénieurs (notamment dans la résolution de circuits RLC ou l'étude des réponses impulsionnelles de filtres).

### B. Machine Learning et Mesures empiriques
En Intelligence Artificielle et en statistiques, on dispose souvent d'un ensemble fini de données $\mathcal{X} = \{x_1, \ldots, x_N\}$. La loi empirique associée à ces données est modélisée mathématiquement par la distribution de Dirac empirique :
$$ \hat{p}(x) = \frac{1}{N}\sum_{i=1}^N \delta_{x_i}(x) $$
Lorsqu'un modèle d'apprentissage automatique cherche à minimiser une perte espérée $\mathbb{E}_{x \sim P}[\ell(x)]$, cette intégrale par rapport à la vraie distribution inconnue $P$ est approchée par l'intégrale par rapport à la distribution empirique $\hat{p}$. Le calcul de l'intégrale contre cette somme de Diracs donne exactement la perte moyenne empirique (ERM) :
$$ \frac{1}{N}\sum_{i=1}^N \ell(x_i) $$
La théorie des distributions (ainsi que la théorie de la mesure) fournit le cadre rigoureux pour étudier la convergence de $\hat{p}$ vers $P$ (par exemple via la distance de Wasserstein ou les bornes PAC).

### C. Réseaux de Neurones à Impulsions (Spiking Neural Networks)
Les SNNs s'inspirent plus fidèlement de la biologie en modélisant les neurones non pas par des valeurs d'activation continues, mais par des trains de potentiels d'action (spikes). Un train de spikes d'un neurone $i$ peut être décrit mathématiquement par une somme de distributions de Dirac $\sum_k \delta(t - t_k^{(i)})$. L'étude de la propagation du signal et de la plasticité synaptique (STDP) dans ces réseaux nécessite l'usage des distributions pour traiter les dérivées temporelles.
