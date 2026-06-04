---
uuid: "jalon-73"
title: "Espaces Lp et passage au quotient"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 72 (Livrable IA).md]]"
next: "[[Jalon 74 (Inégalités fondamentales de l'analyse fonctionnelle).md]]"
---

# Jalon 73 : Espaces $L^p$ et passage au quotient

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous enregistriez une chanson.
    - Il y a la chanson parfaite, mathématique ($f$).
    - Et il y a la chanson avec quelques parasites, des petits "clics" de poussière presque invisibles ($g$).
    - Pour vos oreilles (et pour la physique), si les deux chansons sont identiques partout sauf sur des points isolés qui ne durent rien du tout, ce sont **les mêmes chansons**.
    - Les **espaces $L^p$**, c'est une manière de regrouper les fonctions qui "chantent la même chose" presque tout le temps. On décide d'ignorer les différences qui ne pèsent rien (mesure nulle). On mesure la "force" de la chanson (son énergie $L^2$ ou son volume moyen $L^1$) pour les classer dans différents sacs.
- **Le "Pourquoi on a inventé ça" :** Pour transformer l'espace des fonctions en un véritable espace géométrique (un espace vectoriel normé). Sans le passage au quotient (ignorer le "presque partout"), on ne pourrait pas dire que $\|f\|=0 \implies f=0$, car une fonction peut avoir une aire nulle sans être nulle partout (ex: la fonction de Dirichlet).
- **Visualisation :** On prend toutes les fonctions possibles et on les jette dans des tiroirs. Dans le tiroir $L^1$, on met celles dont l'aire totale est finie. Dans le tiroir $L^2$, celles dont l'énergie est finie.

## 2. Formalisation & Rigueur Académique

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Définition des espaces $\mathcal{L}^p$

> **Définition 1 (Espace $\mathcal{L}^p$) :**
> Pour $1 \le p < +\infty$, on définit l'ensemble des fonctions mesurables dont la puissance $p$-ième est intégrable :
> $$\mathcal{L}^p(\mu) = \left\{ f : X \to \mathbb{K} \mid f \text{ est mesurable et } \int_X |f|^p d\mu < +\infty \right\}$$
> On définit également $\|f\|_p = \left( \int_X |f|^p d\mu \right)^{1/p}$.

> **Définition 2 (Espace $\mathcal{L}^\infty$) :**
> $\mathcal{L}^\infty(\mu)$ est l'ensemble des fonctions mesurables **essentiellement bornées**.
> $\|f\|_\infty = \inf \{ C \ge 0 \mid |f(x)| \le C \text{ p.p.} \}$.

### B. Le passage au quotient $L^p$

L'application $f \mapsto \|f\|_p$ n'est qu'une **semi-norme** sur $\mathcal{L}^p$ car $\|f\|_p = 0$ n'implique pas $f=0$ partout (seulement presque partout).

> **Définition 3 (Relation d'équivalence) :**
> On définit la relation $\sim$ par : $f \sim g \iff f = g \text{ presque partout}$.

> **Définition 4 (Espace quotient $L^p$) :**
> L'espace $L^p(\mu)$ est l'espace quotient de $\mathcal{L}^p(\mu)$ par la relation $\sim$. Ses éléments sont des **classes d'équivalence** de fonctions.
> Sur cet espace, $\| \cdot \|_p$ devient une véritable **norme**.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : $\|f\|_p = 0 \iff f = 0$ p.p.

1. **Sens ($\impliedby$) :** Si $f=0$ p.p., alors $|f|^p = 0$ p.p. L'intégrale d'une fonction nulle presque partout est nulle (voir Jalon 66). Donc $\|f\|_p = 0$.
2. **Sens ($\implies$) :** Supposons $\|f\|_p = 0$. Alors $\int_X |f|^p d\mu = 0$.
3. **Utilisation de la propriété de l'intégrale positive :** On a montré au Jalon 66 que si l'intégrale d'une fonction mesurable positive est nulle, alors la fonction est nulle presque partout.
4. **Application :** Ici $|f|^p \ge 0$. Donc $|f|^p = 0$ p.p., ce qui implique $f = 0$ p.p.

### Inégalité de Minkowski (Structure d'espace vectoriel)

Pour montrer que $L^p$ est un espace vectoriel, il faut montrer que $f, g \in L^p \implies f+g \in L^p$.
On utilise l'inégalité de convexité : $|f+g|^p \le ( |f| + |g| )^p \le 2^{p-1} ( |f|^p + |g|^p )$.
En intégrant, on voit que l'intégrale de $|f+g|^p$ est finie.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Comparaison des espaces $L^p$ sur un ensemble fini
**Énoncé :** Soit $\mu$ une mesure de probabilité ($\mu(X)=1$). Montrer que si $1 \le p \le q \le \infty$, alors $L^q(\mu) \subset L^p(\mu)$.
**Correction Détaillée :**
C'est une application directe de l'inégalité de Jensen ou de l'inégalité de Hölder (Jalon 74). Si une variable a un moment d'ordre 10 fini, elle a forcément un moment d'ordre 2 fini.
*Attention :* C'est faux si la mesure de l'espace est infinie (ex: sur $\mathbb{R}$). $f(x) = \frac{1}{1+x^2}$ est dans $L^2$ et $L^1$, mais $g(x) = \frac{1}{\sqrt{x}} \mathbf{1}_{]0, 1[}$ est dans $L^1$ mais pas dans $L^2$.

### Exercice 2 : Niveau Avancé (La norme $L^\infty$)
**Énoncé :** Soit $f(x) = x$ sur $[0, 1]$. Calculer $\|f\|_p$ et montrer que $\lim_{p \to \infty} \|f\|_p = \|f\|_\infty$.
**Correction Détaillée :**
1. $\|f\|_p = (\int_0^1 x^p dx)^{1/p} = (\frac{1}{p+1})^{1/p} = \exp( - \frac{1}{p} \ln(p+1) )$.
2. Quand $p \to \infty$, $\frac{\ln(p+1)}{p} \to 0$, donc $\|f\|_p \to e^0 = 1$.
3. Par ailleurs, $\sup |f| = 1$ sur $[0, 1]$, donc $\|f\|_\infty = 1$. L'égalité est vérifiée.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le choix de la fonction de perte en IA correspond exactement au choix de la norme $L^p$ dans laquelle on veut minimiser l'erreur.
- **Example Concret :**
    - **Régression $L^2$ (MSE) :** Minimiser $\mathbb{E}[(Y - f(X))^2]$. C'est minimiser la norme $L^2$ de l'erreur. Cela conduit à la moyenne conditionnelle.
    - **Régression $L^1$ (MAE) :** Minimiser $\mathbb{E}[|Y - f(X)|]$. C'est la norme $L^1$. C'est beaucoup plus robuste aux "outliers" (points aberrants) car on ne porte pas l'erreur au carré. Cela conduit à la médiane conditionnelle.
    - **Compression d'image :** Les métriques comme le PSNR sont basées sur la norme $L^2$. Des métriques plus récentes essaient de se rapprocher de la perception humaine, qui est une norme topologique beaucoup plus complexe sur l'espace des fonctions.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]
- **Concepts Futurs dépendants :** [[Jalon 75 (Preuve de la complétude des espaces Lp).md]], [[Jalon 81 (Transformée de Fourier dans L2).md]]
