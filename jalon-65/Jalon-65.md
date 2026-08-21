---
uuid: "jalon-65"
title: "Fonctions mesurables"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/abstraction
prev: "[[jalon-64/Jalon-64.md|Jalon 64 (Construction pas à pas de la mesure de Lebesgue sur Rn via la mesure extérieure.)]]"
next: "[[jalon-66/Jalon-66.md|Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.)]]"
---

# Jalon 65 : Fonctions mesurables

## 1. Genèse et Nécessité Structurelle

Historiquement, l'intégrale de Riemann a montré ses limites lorsqu'elle fut confrontée à des fonctions fortement discontinues ou lors du passage à la limite dans les intégrales (convergence des suites de fonctions). L'intégrale de Lebesgue a été conçue pour intégrer une classe beaucoup plus vaste de fonctions, en changeant de perspective : au lieu de partitionner le domaine de départ, on partitionne l'espace d'arrivée.

Cependant, pour que cette construction soit rigoureuse et ne conduise pas à des contradictions logiques, on ne peut pas intégrer n'importe quelle fonction arbitraire. Il est impératif que les ensembles sur lesquels la fonction prend ses valeurs soient "mesurables" au sens de la théorie de la mesure. Une fonction est donc dite "mesurable" si, grosso modo, l'image réciproque de tout ensemble bien défini dans l'espace d'arrivée appartient à la tribu de l'espace de départ. C'est le prérequis fondamental de toute l'intégration moderne et de la théorie des probabilités de Kolmogorov.

## 2. Définitions et Théorèmes Fondamentaux

### Mesurabilité d'une Fonction

> **Définition 1 (Fonction mesurable) :**
> Soient $(E, \mathcal{A})$ et $(F, \mathcal{B})$ deux espaces mesurables. Une application $f : E \to F$ est dite **mesurable** (ou plus précisément $(\mathcal{A}, \mathcal{B})$-mesurable) si pour tout ensemble $B \in \mathcal{B}$, l'image réciproque $f^{-1}(B)$ appartient à la tribu $\mathcal{A}$ :
> $$ \forall B \in \mathcal{B}, \quad f^{-1}(B) \in \mathcal{A} $$

**Exemple Numérique Immédiat :**
Considérons l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ où $\mathcal{B}(\mathbb{R})$ est la tribu borélienne. Soit la fonction indicatrice d'un ensemble $A \subset \mathbb{R}$, définie par :
$$ \mathbb{1}_A(x) = \begin{cases} 1 & \text{si } x \in A \\ 0 & \text{si } x \notin A \end{cases} $$
Cette fonction prend ses valeurs dans $F = \{0, 1\}$. Munissons $F$ de la tribu $\mathcal{P}(F) = \{\emptyset, \{0\}, \{1\}, \{0, 1\}\}$.
Vérifions la mesurabilité pour chaque élément de $\mathcal{P}(F)$ :
- $\mathbb{1}_A^{-1}(\emptyset) = \emptyset \in \mathcal{B}(\mathbb{R})$
- $\mathbb{1}_A^{-1}(\{1\}) = A$. Pour que $\mathbb{1}_A$ soit mesurable, il faut donc impérativement que $A \in \mathcal{B}(\mathbb{R})$.
- $\mathbb{1}_A^{-1}(\{0\}) = A^c \in \mathcal{B}(\mathbb{R})$ (car la tribu est stable par passage au complémentaire).
- $\mathbb{1}_A^{-1}(\{0, 1\}) = \mathbb{R} \in \mathcal{B}(\mathbb{R})$.
Donc, $\mathbb{1}_A$ est mesurable si et seulement si $A$ est un borélien. Si $A$ est l'ensemble de Vitali (non mesurable), la fonction indicatrice correspondante n'est pas mesurable.

> **Théorème 1 (Critère de mesurabilité sur un système générateur) :**
> Soit $\mathcal{C}$ une classe de parties de $F$ qui engendre la tribu $\mathcal{B}$, c'est-à-dire $\sigma(\mathcal{C}) = \mathcal{B}$.
> L'application $f : (E, \mathcal{A}) \to (F, \mathcal{B})$ est mesurable si et seulement si :
> $$ \forall C \in \mathcal{C}, \quad f^{-1}(C) \in \mathcal{A} $$

**Exemple de validation géométrique :**
Pour prouver qu'une fonction $f : \mathbb{R} \to \mathbb{R}$ est borélienne, on n'a pas besoin de tester tous les boréliens (ce qui est impossible). Il suffit de vérifier la mesurabilité sur les générateurs, par exemple les intervalles du type $]-\infty, a]$. Ainsi, $f$ est borélienne si et seulement si :
$$ \forall a \in \mathbb{R}, \quad \{ x \in \mathbb{R} \mid f(x) \leq a \} \in \mathcal{B}(\mathbb{R}) $$

### Opérations sur les Fonctions Mesurables

> **Théorème 2 (Stabilité des fonctions mesurables réelles) :**
> Soient $f$ et $g$ deux fonctions mesurables de $(E, \mathcal{A})$ dans $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$, et soit $\lambda \in \mathbb{R}$.
> Alors les fonctions suivantes sont mesurables :
> 1. $\lambda f$
> 2. $f + g$
> 3. $f \cdot g$
> 4. $\max(f, g)$ et $\min(f, g)$
> 5. $|f|$

### Suites de Fonctions Mesurables

> **Théorème 3 (Stabilité par passage à la limite) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $(E, \mathcal{A})$ dans $(\overline{\mathbb{R}}, \mathcal{B}(\overline{\mathbb{R}}))$.
> Alors les fonctions suivantes sont mesurables :
> 1. $\sup_{n \in \mathbb{N}} f_n$
> 2. $\inf_{n \in \mathbb{N}} f_n$
> 3. $\limsup_{n \to \infty} f_n$
> 4. $\liminf_{n \to \infty} f_n$
> De plus, si la suite $(f_n)_{n \in \mathbb{N}}$ converge ponctuellement vers une fonction $f$, alors la fonction limite $f$ est mesurable.

**Cas limite :** Ce théorème est crucial. Il indique que l'espace des fonctions mesurables est fermé pour la convergence ponctuelle, ce qui n'est pas le cas pour les fonctions continues (la limite d'une suite de fonctions continues n'est pas nécessairement continue).

### Fonctions Étagées

> **Définition 2 (Fonction étagée) :**
> Une fonction mesurable $s : (E, \mathcal{A}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ est dite **étagée** si elle ne prend qu'un nombre fini de valeurs réelles.
> Toute fonction étagée s'écrit sous la forme canonique :
> $$ s(x) = \sum_{i=1}^n \alpha_i \mathbb{1}_{A_i}(x) $$
> où $\alpha_1, \dots, \alpha_n$ sont des réels distincts et $A_1, \dots, A_n$ forment une partition mesurable de $E$ ($A_i \in \mathcal{A}$).

> **Théorème 4 (Approximation par des fonctions étagées) :**
> 1. Soit $f : E \to [0, +\infty]$ une fonction mesurable positive. Il existe une suite croissante $(s_n)_{n \in \mathbb{N}}$ de fonctions étagées positives qui converge ponctuellement vers $f$.
> 2. Si de plus $f$ est bornée, la convergence de cette suite est uniforme.

## 3. Démonstrations

**Démonstration du Théorème 1 (Critère sur les générateurs) :**
L'implication directe est triviale puisque $\mathcal{C} \subset \mathcal{B}$.
Montrons la réciproque. Supposons que $\forall C \in \mathcal{C}, f^{-1}(C) \in \mathcal{A}$.
Posons $\mathcal{T} = \{ B \in \mathcal{P}(F) \mid f^{-1}(B) \in \mathcal{A} \}$.
L'objectif est de montrer que $\mathcal{B} \subset \mathcal{T}$.
1. $f^{-1}(F) = E \in \mathcal{A}$, donc $F \in \mathcal{T}$.
2. Soit $B \in \mathcal{T}$. $f^{-1}(B^c) = (f^{-1}(B))^c$. Or $f^{-1}(B) \in \mathcal{A}$ et $\mathcal{A}$ est une tribu, donc $(f^{-1}(B))^c \in \mathcal{A}$. D'où $B^c \in \mathcal{T}$.
3. Soit $(B_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{T}$. $f^{-1}(\bigcup_{n \in \mathbb{N}} B_n) = \bigcup_{n \in \mathbb{N}} f^{-1}(B_n)$. Or $\forall n, f^{-1}(B_n) \in \mathcal{A}$ et $\mathcal{A}$ est une tribu, donc la réunion dénombrable appartient à $\mathcal{A}$. D'où $\bigcup_{n \in \mathbb{N}} B_n \in \mathcal{T}$.
Par conséquent, $\mathcal{T}$ est une tribu sur $F$.
Puisque par hypothèse $\mathcal{C} \subset \mathcal{T}$ et que $\mathcal{T}$ est une tribu, $\mathcal{T}$ contient nécessairement la plus petite tribu contenant $\mathcal{C}$, soit $\sigma(\mathcal{C})$. Or $\mathcal{B} = \sigma(\mathcal{C})$, donc $\mathcal{B} \subset \mathcal{T}$.
Ainsi, $\forall B \in \mathcal{B}, f^{-1}(B) \in \mathcal{A}$, ce qui prouve la mesurabilité de $f$. $\blacksquare$

**Démonstration du Théorème 4.1 (Approximation canonique) :**
Pour tout entier $n \ge 1$ et pour tout $x \in E$, on pose :
$$ s_n(x) = \sum_{k=0}^{n2^n - 1} \frac{k}{2^n} \mathbb{1}_{\{ x \in E \mid \frac{k}{2^n} \le f(x) < \frac{k+1}{2^n} \}}(x) + n \mathbb{1}_{\{ x \in E \mid f(x) \ge n \}}(x) $$
Par définition de la mesurabilité de $f$, les ensembles de niveau $A_{n,k} = f^{-1}([\frac{k}{2^n}, \frac{k+1}{2^n}[)$ et $B_n = f^{-1}([n, +\infty])$ sont dans $\mathcal{A}$.
Donc $s_n$ est bien une fonction étagée mesurable positive.
De plus, par construction :
- Si $f(x) < n$, on a $\frac{k}{2^n} \le f(x) < \frac{k+1}{2^n}$ pour un certain $k$, d'où $s_n(x) = \frac{k}{2^n} \le f(x)$ et $f(x) - s_n(x) < \frac{1}{2^n}$.
- Si $f(x) \ge n$, alors $s_n(x) = n \le f(x)$.
On a donc bien $s_n \le s_{n+1} \le f$ pour tout $n$.
Si $x \in E$ est tel que $f(x) = +\infty$, alors $s_n(x) = n \to +\infty = f(x)$.
Si $f(x) \in \mathbb{R}$, pour $n > f(x)$, la différence $0 \le f(x) - s_n(x) < \frac{1}{2^n}$ tend vers 0. Donc la suite converge ponctuellement vers $f$. $\blacksquare$

## 4. Applications en Physique, Logique & Intelligence Artificielle

Dans la théorie moderne des probabilités (Axiomatique de Kolmogorov), une **variable aléatoire** réelle $X$ définie sur un espace de probabilité $(\Omega, \mathcal{A}, \mathbb{P})$ n'est rien d'autre qu'une **fonction mesurable** de $(\Omega, \mathcal{A})$ dans $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

En Machine Learning, les espaces d'observation (pixels, ondes sonores) sont munis de tribus. L'existence même d'une loi de probabilité pour les variables et de l'espérance mathématique (la fonction de perte empirique ou théorique) repose intégralement sur la mesurabilité des fonctions considérées, comme les réseaux de neurones (les fonctions continues ou de classe $C^1$ par morceaux composant les couches denses et d'activation étant par essence boréliennes).
