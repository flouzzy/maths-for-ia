---
uuid: "jalon-37"
title: "Intégrale de Riemann sur un segment"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/calcul-integral
prev: "[[Jalon 36 (Livrable IA).md]]"
next: "[[Jalon 38 (Théorème fondamental de l'analyse).md]]"
---

# Jalon 37 : Intégrale de Riemann sur un segment

## 1. Genèse et Motivation Historique

La genèse du calcul intégral remonte à l'Antiquité, avec la méthode d'exhaustion d'Eudoxe et d'Archimède, visant à évaluer l'aire de figures complexes en les approximant par des polygones inscrits et circonscrits. Cependant, cette méthode exigeait une preuve d'ingéniosité spécifique pour chaque nouvelle courbe. Au XVIIe siècle, Newton et Leibniz ont uni le calcul des aires et le calcul des tangentes via le théorème fondamental du calcul différentiel et intégral. Toutefois, leur approche reposait sur des notions intuitives d'« infiniment petits », dont la rigueur fut vivement critiquée (notamment par l'évêque Berkeley qui les qualifiait de « fantômes de quantités défuntes »).

Ce n'est qu'au XIXe siècle, sous l'impulsion d'Augustin-Louis Cauchy puis de Bernhard Riemann, que l'intégrale acquiert une fondation rigoureuse. L'impasse intellectuelle était la suivante : comment définir de manière univoque l'aire sous une courbe pour des fonctions qui peuvent présenter des discontinuités denses ou des comportements pathologiques ? Cauchy avait défini l'intégrale pour les fonctions continues. Riemann (1854) élargit ce cadre en considérant les limites de sommes d'aires de rectangles pour toute fonction arbitraire, posant la question fondamentale : "quelles sont les fonctions qui admettent une telle limite ?".

Cette formalisation de Riemann a libéré l'analyse de son carcan purement géométrique. Elle a permis de traiter avec rigueur les séries de Fourier, d'étudier des fonctions hautement oscillantes, et constitue aujourd'hui la base de l'analyse fonctionnelle, des probabilités continues (via la théorie de la mesure de Lebesgue, qui la généralisera) et de la théorie de l'apprentissage statistique.

## 2. Formalisation Algébrique et Analytique

### A. Subdivisions d'un Segment

Soient $a, b \in \mathbb{R}$ tels que $a < b$. On considère le segment $[a, b]$.

**Définition 1 (Subdivision) :**
Une subdivision $\sigma$ de $[a, b]$ est une famille finie de points $\sigma = (x_0, x_1, \dots, x_n)$ de $[a, b]$ vérifiant :
$$ a = x_0 < x_1 < \dots < x_{n-1} < x_n = b $$
On note $\Sigma([a, b])$ l'ensemble de toutes les subdivisions de $[a, b]$.

**Définition 2 (Pas d'une subdivision) :**
Le pas d'une subdivision $\sigma = (x_i)_{0 \le i \le n}$, noté $\delta(\sigma)$, est la plus grande des longueurs des sous-intervalles $[x_{i-1}, x_i]$ :
$$ \delta(\sigma) = \max_{1 \le i \le n} (x_i - x_{i-1}) $$

**Définition 3 (Subdivision plus fine) :**
Soient $\sigma_1, \sigma_2 \in \Sigma([a, b])$. On dit que $\sigma_2$ est plus fine que $\sigma_1$ si tous les points de $\sigma_1$ appartiennent à $\sigma_2$ (i.e. $\sigma_1 \subset \sigma_2$).
On note que si $\sigma_1, \sigma_2 \in \Sigma([a, b])$, leur union $\sigma_1 \cup \sigma_2$ est une subdivision plus fine que $\sigma_1$ et que $\sigma_2$.

### B. Fonctions en Escalier

**Définition 4 (Fonction en escalier) :**
Une fonction $\varphi : [a, b] \to \mathbb{R}$ est dite en escalier s'il existe une subdivision $\sigma = (x_0, \dots, x_n) \in \Sigma([a, b])$ telle que $\varphi$ soit constante sur chaque intervalle ouvert $]x_{i-1}, x_i[$.
On note $\mathcal{E}([a, b])$ l'ensemble des fonctions en escalier sur $[a, b]$.
Si $\varphi(t) = c_i$ pour $t \in ]x_{i-1}, x_i[$, on note que les valeurs de $\varphi(x_i)$ aux points de subdivision sont quelconques et n'affectent pas le caractère "en escalier".

**Définition 5 (Intégrale d'une fonction en escalier) :**
Soit $\varphi \in \mathcal{E}([a, b])$ associée à une subdivision $\sigma = (x_i)_{0 \le i \le n}$ sur laquelle elle prend les valeurs constantes $c_i$ sur $]x_{i-1}, x_i[$.
L'intégrale de Riemann de $\varphi$ sur $[a, b]$ est définie par la somme finie :
$$ \int_a^b \varphi(t) \, dt = \sum_{i=1}^n c_i (x_i - x_{i-1}) $$
*Remarque :* On démontre que cette valeur est indépendante du choix de la subdivision adaptée à $\varphi$.

### C. L'Intégrale de Riemann

Soit $f : [a, b] \to \mathbb{R}$ une fonction **bornée** sur $[a, b]$.
Étant donné que $f$ est bornée, on peut définir les ensembles suivants pour toute subdivision $\sigma$ :
$m_i = \inf_{t \in [x_{i-1}, x_i]} f(t)$ et $M_i = \sup_{t \in [x_{i-1}, x_i]} f(t)$.

**Définition 6 (Sommes de Darboux) :**
La somme de Darboux inférieure de $f$ pour $\sigma$ est :
$$ S_-(\sigma, f) = \sum_{i=1}^n m_i (x_i - x_{i-1}) $$
La somme de Darboux supérieure de $f$ pour $\sigma$ est :
$$ S_+(\sigma, f) = \sum_{i=1}^n M_i (x_i - x_{i-1}) $$

**Définition 7 (Intégrabilité au sens de Riemann) :**
L'intégrale inférieure de Riemann de $f$ est $I_-(f) = \sup_{\sigma \in \Sigma} S_-(\sigma, f)$.
L'intégrale supérieure de Riemann de $f$ est $I_+(f) = \inf_{\sigma \in \Sigma} S_+(\sigma, f)$.
La fonction $f$ est dite Riemann-intégrable sur $[a, b]$ si $I_-(f) = I_+(f)$.
Dans ce cas, cette valeur commune est appelée l'intégrale de Riemann de $f$ sur $[a, b]$ et est notée $\int_a^b f(t) \, dt$.
On note $\mathcal{R}([a, b])$ l'espace vectoriel des fonctions Riemann-intégrables sur $[a, b]$.

**Exemples de Validation :**
- Fonction constante $f(t) = C$ : toute somme de Darboux vaut $C(b-a)$, donc $I_- = I_+ = C(b-a)$.
- Fonction de Dirichlet (cas pathologique) : $f(t) = 1$ si $t \in \mathbb{Q}$, $0$ sinon.
Pour tout intervalle $[x_{i-1}, x_i]$, il contient des rationnels et des irrationnels (densité). Donc $m_i = 0$ et $M_i = 1$.
Ainsi, $S_-(\sigma, f) = 0$ et $S_+(\sigma, f) = b-a$. Par suite $I_-(f) = 0 \neq I_+(f) = b-a$.
La fonction de Dirichlet n'est **pas** Riemann-intégrable.

## 3. Démonstrations et Preuves Étape par Étape

### Théorème : Les fonctions continues sur un segment sont Riemann-intégrables.

**Énoncé :**
Soit $f : [a, b] \to \mathbb{R}$ une fonction continue. Alors $f \in \mathcal{R}([a, b])$.

**Démonstration :**
1. Soit $\epsilon > 0$ un réel fixé arbitrairement.
2. La fonction $f$ est continue sur le segment $[a, b]$. D'après le théorème de Heine-Borel (compacité des segments dans $\mathbb{R}$), $f$ est uniformément continue sur $[a, b]$.
3. Il existe donc un $\delta > 0$ tel que pour tout $x, y \in [a, b]$ vérifiant $|x - y| < \delta$, on ait $|f(x) - f(y)| < \frac{\epsilon}{b - a}$.
4. Soit $\sigma = (x_0, \dots, x_n)$ une subdivision de $[a, b]$ telle que son pas $\delta(\sigma)$ soit strictement inférieur à $\delta$.
5. Considérons un sous-intervalle quelconque $[x_{i-1}, x_i]$ de la subdivision. Comme $f$ y est continue, par le théorème des bornes atteintes, $f$ atteint son minimum $m_i$ en un point $u_i \in [x_{i-1}, x_i]$ et son maximum $M_i$ en un point $v_i \in [x_{i-1}, x_i]$.
6. Puisque $u_i, v_i \in [x_{i-1}, x_i]$, la distance qui les sépare est majorée par la longueur de l'intervalle : $|u_i - v_i| \le x_i - x_{i-1} \le \delta(\sigma) < \delta$.
7. Par l'uniforme continuité (étape 3), on en déduit que :
$$ M_i - m_i = f(v_i) - f(u_i) = |f(v_i) - f(u_i)| < \frac{\epsilon}{b - a} $$
8. Évaluons maintenant la différence entre la somme de Darboux supérieure et la somme de Darboux inférieure pour cette subdivision $\sigma$ :
$$ S_+(\sigma, f) - S_-(\sigma, f) = \sum_{i=1}^n (M_i - m_i)(x_i - x_{i-1}) $$
9. En injectant la majoration obtenue à l'étape 7 :
$$ S_+(\sigma, f) - S_-(\sigma, f) < \sum_{i=1}^n \frac{\epsilon}{b - a} (x_i - x_{i-1}) = \frac{\epsilon}{b - a} \sum_{i=1}^n (x_i - x_{i-1}) $$
10. La somme télescopique $\sum_{i=1}^n (x_i - x_{i-1})$ vaut précisément $x_n - x_0 = b - a$.
11. D'où :
$$ S_+(\sigma, f) - S_-(\sigma, f) < \frac{\epsilon}{b - a} (b - a) = \epsilon $$
12. Par définition, $I_+(f) \le S_+(\sigma, f)$ et $S_-(\sigma, f) \le I_-(f)$. Donc :
$$ 0 \le I_+(f) - I_-(f) \le S_+(\sigma, f) - S_-(\sigma, f) < \epsilon $$
13. Cette inégalité stricte $0 \le I_+(f) - I_-(f) < \epsilon$ est vraie pour tout $\epsilon > 0$. L'unique possibilité est donc que $I_+(f) - I_-(f) = 0$.
14. Par conséquent, $I_+(f) = I_-(f)$, ce qui signifie que $f$ est Riemann-intégrable sur $[a, b]$. $\blacksquare$

### Théorème (Sommes de Riemann)

**Énoncé :**
Si $f \in \mathcal{R}([a, b])$, pour toute suite de subdivisions pointées $(\sigma_n, \xi_n)$ telle que $\lim_{n \to \infty} \delta(\sigma_n) = 0$, la somme de Riemann :
$$ S(\sigma_n, f) = \sum_{i=1}^n f(\xi_{i,n}) (x_{i,n} - x_{i-1,n}) $$
converge vers $\int_a^b f(t) \, dt$.

**Preuve abrégée :**
Cela découle directement du fait que pour toute subdivision pointée, $S_-(\sigma_n, f) \le S(\sigma_n, f) \le S_+(\sigma_n, f)$, et l'intégrabilité assure que les sommes de Darboux encadrantes convergent vers la même limite lorsque le pas tend vers 0.
