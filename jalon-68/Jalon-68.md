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

# Jalon 68 : Lemme de Fatou et fonctions de signe quelconque

## Introduction

Le lemme de Fatou est une pierre angulaire de la théorie de l'intégration de Lebesgue. Son but principal est de fournir une borne inférieure sur l'intégrale de la limite inférieure d'une suite de fonctions mesurables positives. Historiquement, le passage à la limite sous le signe intégral posait des difficultés majeures, souvent insurmontables avec l'intégrale de Riemann, en particulier à cause des variations violentes ou de "masse" s'échappant vers l'infini. Pierre Fatou a montré que la "performance" limite ne peut excéder la limite des "performances".

Ensuite, l'extension aux fonctions de signe quelconque repose sur un principe comptable simple : séparer la fonction en une composante strictement positive et une composante strictement négative, intégrer chacune séparément avec les outils développés pour les fonctions positives, et faire le bilan.

## Définitions, Théorèmes et Exemples

### Le Lemme de Fatou

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables définies sur un espace mesuré $(X, \mathcal{A}, \mu)$ et à valeurs dans $[0, +\infty]$.

**Théorème (Lemme de Fatou) :**
$$ \int_X \left( \liminf_{n \to \infty} f_n \right) d\mu \le \liminf_{n \to \infty} \int_X f_n d\mu $$

**Typage des variables :**
- $X$ : l'espace de base (par exemple $\mathbb{R}$).
- $\mathcal{A}$ : une tribu sur $X$.
- $\mu$ : une mesure positive (par exemple la mesure de Lebesgue $\lambda$).
- $f_n$ : fonctions de $X$ vers $\overline{\mathbb{R}}_+$.

**Exemples concrets de validation :**
1. **Convergence simple sans perte :** Soit $f_n = \mathbf{1}_{[0, 1]}$. La limite est $\mathbf{1}_{[0, 1]}$. L'intégrale de la limite est $1$, et la limite des intégrales est $1$. L'inégalité est une égalité ($1 \le 1$).
2. **Masse fuyant à l'infini (droite) :** Soit $f_n = \mathbf{1}_{[n, n+1]}$. La suite tend simplement vers $0$ partout. $\int \liminf f_n = 0$. Mais $\int f_n = 1$ pour tout $n$, donc $\liminf \int f_n = 1$. On a bien $0 \le 1$.
3. **Masse se concentrant (Dirac) :** Soit $f_n = n \mathbf{1}_{]0, 1/n[}$. Pour $x > 0$, $f_n(x)$ s'annule à partir d'un certain rang, donc $\liminf f_n = 0$. $\int \liminf f_n = 0$. Mais $\int f_n = n \times (1/n) = 1$. L'inégalité est $0 \le 1$.
4. **Oscillations rapides :** $f_n(x) = \sin^2(nx)$ sur $[0, \pi]$. $\liminf f_n(x) = 0$ presque partout. $\int_0^\pi f_n = \pi/2$. On a $0 \le \pi/2$.
5. **Fonctions croissantes :** Si $f_n$ est croissante vers $f$, Beppo-Levi donne l'égalité. L'inégalité de Fatou reste vraie, mais n'est pas stricte.

**Cas pathologique (bordure) :**
Si les fonctions prennent des valeurs négatives, le lemme de Fatou peut être faux. Par exemple $f_n = -n \mathbf{1}_{[0, 1/n]}$. $\liminf f_n = 0$, donc $\int \liminf f_n = 0$. Mais $\int f_n = -1$, donc $\liminf \int f_n = -1$. On n'a pas $0 \le -1$. C'est pourquoi la positivité est requise ou, a minima, l'existence d'une fonction intégrable minorante (lemme de Fatou généralisé).

### Fonctions intégrables de signe quelconque

Soit $f : X \to \mathbb{R}$ ou $\overline{\mathbb{R}}$ mesurable.
On pose $f^+(x) = \max(f(x), 0)$ et $f^-(x) = \max(-f(x), 0)$.

**Définition :**
La fonction $f$ est dite $\mu$-intégrable si et seulement si $f^+$ et $f^-$ d'intégrales finies (i.e. $\int f^+ d\mu < \infty$ et $\int f^- d\mu < \infty$). L'intégrale de $f$ vaut alors :
$$ \int_X f d\mu = \int_X f^+ d\mu - \int_X f^- d\mu $$

**Typage des variables :**
- $f^+$ : Partie positive de $f$, à valeurs dans $\mathbb{R}_+$.
- $f^-$ : Partie négative de $f$, à valeurs dans $\mathbb{R}_+$.

**Exemples concrets de validation :**
1. **Fonction simple :** $f(x) = x$ sur $[-1, 1]$. $f^+(x) = x$ sur $[0, 1]$, et $0$ ailleurs. $f^-(x) = -x$ sur $[-1, 0]$ et $0$ ailleurs. $\int f^+ = 1/2$, $\int f^- = 1/2$. Donc $\int f = 0$.
2. **Fonction non intégrable (compensation) :** $f(x) = 1/x$ sur $[1, \infty[ \cup ]-\infty, -1]$. On pourrait vouloir dire que par symétrie, l'intégrale est 0. Cependant, $f^+$ et $f^-$ ont des intégrales infinies. $f$ n'est pas intégrable au sens de Lebesgue.
3. **Fonction sinus amorti :** $f(x) = \frac{\sin(x)}{x^2}$ sur $[1, +\infty[$. $|f(x)| \le \frac{1}{x^2}$ qui est intégrable. Donc $f$ est intégrable.
4. **Valeur absolue :** $|f| = f^+ + f^-$. $f$ est intégrable si et seulement si $|f|$ l'est.
5. **Combinaison linéaire :** Si $f$ et $g$ sont intégrables, alors $2f - 3g$ l'est aussi.

## Demonstrations

### Démonstration du Lemme de Fatou

1. **Construction d'une suite auxiliaire :**
   Posons $g_k(x) = \inf_{n \ge k} f_n(x)$.
   Puisque les $f_n$ sont mesurables et positives, $g_k$ est mesurable et positive.
   De plus, pour tout $x \in X$, la suite $(g_k(x))_{k \in \mathbb{N}}$ est croissante car on prend l'infimum sur un ensemble d'indices de plus en plus petit.

2. **Identification de la limite :**
   Par définition de la limite inférieure, on a :
   $$ \lim_{k \to \infty} g_k(x) = \sup_{k \ge 0} \left( \inf_{n \ge k} f_n(x) \right) = \liminf_{n \to \infty} f_n(x) $$

3. **Application du Théorème de Convergence Monotone :**
   Puisque $(g_k)$ est une suite croissante de fonctions mesurables positives, le théorème de Beppo-Levi (Jalon 67) garantit que :
   $$ \int_X \left( \lim_{k \to \infty} g_k \right) d\mu = \lim_{k \to \infty} \int_X g_k d\mu $$
   Soit :
   $$ \int_X \left( \liminf_{n \to \infty} f_n \right) d\mu = \lim_{k \to \infty} \int_X g_k d\mu $$

4. **Majoration par la suite originale :**
   Pour tout $n \ge k$, on a $g_k(x) \le f_n(x)$.
   Par croissance de l'intégrale, on a $\int_X g_k d\mu \le \int_X f_n d\mu$ pour tout $n \ge k$.
   Ainsi, $\int_X g_k d\mu$ est un minorant de l'ensemble $\{ \int_X f_n d\mu \mid n \ge k \}$. Par conséquent :
   $$ \int_X g_k d\mu \le \inf_{n \ge k} \int_X f_n d\mu $$

5. **Passage à la limite fin :**
   On prend la limite quand $k \to \infty$ des deux côtés :
   $$ \lim_{k \to \infty} \int_X g_k d\mu \le \lim_{k \to \infty} \left( \inf_{n \ge k} \int_X f_n d\mu \right) = \liminf_{n \to \infty} \int_X f_n d\mu $$
   Ce qui achève la preuve :
   $$ \int_X \left( \liminf_{n \to \infty} f_n \right) d\mu \le \liminf_{n \to \infty} \int_X f_n d\mu $$

## Applications en Physique, Logique et AI

En Intelligence Artificielle, et particulièrement dans l'analyse théorique de l'apprentissage (Statistical Learning Theory), le lemme de Fatou est fondamental pour prouver des bornes sur le risque asymptotique (Expected Risk).

Si nous considérons une suite de modèles appris $h_n$ et leur perte sur une donnée $x$, $L(h_n(x), y)$, qui est positive. Si les modèles convergent vers un modèle $h$, le lemme de Fatou assure que le risque espéré du modèle limite est au plus la limite inférieure des risques espérés des modèles $h_n$. Cela signifie que passer à la limite dans l'espace des modèles ne peut pas empirer catastrophiquement notre garantie de performance.

Dans l'optimisation stochastique, lorsqu'on calcule la log-vraisemblance d'un modèle génératif, les variables prennent des valeurs de signe quelconque. La séparation en parties positives et négatives permet de garantir que l'entropie croisée est un objet mathématique bien défini avant de tenter de la minimiser via une descente de gradient.
