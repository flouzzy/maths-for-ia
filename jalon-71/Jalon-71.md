---
uuid: "jalon-71"
title: "Théorèmes de Fubini-Tonelli"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 70 (Espaces mesurés produits).md]]"
next: "[[Jalon 72 (Livrable IA).md]]"
---

# Jalon 71 : Théorèmes de Fubini-Tonelli

## 1. Genèse et Intuition Physique

Le problème fondamental de l'intégration multiple consiste à évaluer le "volume" sous le graphe d'une fonction définie sur un espace de dimension supérieure, et plus généralement de calculer l'intégrale d'une fonction par rapport à une mesure produit sur un espace $X \times Y$. L'intuition physique, héritée d'Archimède et formalisée plus tard par Cavalieri avec sa méthode des indivisibles, suggère que le volume d'un solide peut être déterminé en sommant les aires de ses sections transversales parallèles. Cette idée séduisante de "couper en tranches" est le cœur des théorèmes d'interversion.

Historiquement, Cauchy et Riemann avaient déjà établi des théorèmes d'intégration successive pour des fonctions continues sur des rectangles de $\mathbb{R}^2$. Cependant, avec l'avènement de la théorie de la mesure de Lebesgue au début du XXe siècle, qui étendait drastiquement la classe des fonctions intégrables pour inclure des objets pathologiques, une question pressante s'est posée : sous quelles conditions rigoureuses peut-on affirmer que l'ordre dans lequel on intègre les variables n'affecte pas le résultat final ?

C'est Guido Fubini (1907) qui démontra que pour les fonctions Lebesgue-intégrables sur l'espace produit, l'intégrale double est toujours égale aux deux intégrales itérées. Leonida Tonelli (1909) compléta ce tableau en prouvant que pour des fonctions mesurables positives, le calcul d'une intégrale itérée finie garantit ipso facto l'intégrabilité sur l'espace produit. Ensemble, les théorèmes de Fubini-Tonelli constituent la pierre angulaire de l'analyse moderne, permettant des manipulations algébriques puissantes dans des domaines allant de la théorie des probabilités à l'analyse harmonique, en justifiant l'échange systématique de l'ordre d'intégration.

## 2. Définitions, Théorèmes et Exemples

### Définition 1 : Sections d'un ensemble et d'une fonction

Soient $(X, \mathcal{F})$ et $(Y, \mathcal{G})$ deux espaces mesurables. On munit l'espace produit $X \times Y$ de la tribu produit $\mathcal{F} \otimes \mathcal{G}$.

Pour un sous-ensemble $E \in \mathcal{F} \otimes \mathcal{G}$ et des points $x \in X$, $y \in Y$, on définit :
- La **$x$-section** de $E$ : $E_x = \{ y \in Y \mid (x, y) \in E \}$.
- La **$y$-section** de $E$ : $E^y = \{ x \in X \mid (x, y) \in E \}$.

Pour une fonction $f : X \times Y \to \mathbb{R}$ ou $\mathbb{C}$, on définit ses fonctions partielles (ou sections) :
- La **$x$-section** de $f$ : $f_x : Y \to \mathbb{R}$ définie par $f_x(y) = f(x, y)$.
- La **$y$-section** de $f$ : $f^y : X \to \mathbb{R}$ définie par $f^y(x) = f(x, y)$.

**Lemme de mesurabilité des sections :**
Si $E \in \mathcal{F} \otimes \mathcal{G}$, alors pour tout $x \in X$, $E_x \in \mathcal{G}$ et pour tout $y \in Y$, $E^y \in \mathcal{F}$.
Si $f$ est $\mathcal{F} \otimes \mathcal{G}$-mesurable, alors pour tout $x \in X$, la fonction $f_x$ est $\mathcal{G}$-mesurable et pour tout $y \in Y$, $f^y$ est $\mathcal{F}$-mesurable.

### Théorème de Tonelli (Cas des fonctions positives)

Soient $(X, \mathcal{F}, \mu)$ et $(Y, \mathcal{G}, \nu)$ deux espaces mesurés **$\sigma$-finis**.
Soit $f : X \times Y \to [0, +\infty]$ une fonction mesurable pour la tribu produit $\mathcal{F} \otimes \mathcal{G}$.

Alors :
1. La fonction $x \mapsto \int_Y f(x, y) \, d\nu(y)$ est $\mathcal{F}$-mesurable.
2. La fonction $y \mapsto \int_X f(x, y) \, d\mu(x)$ est $\mathcal{G}$-mesurable.
3. On a l'égalité des intégrales (qui peuvent valoir $+\infty$) :
   $$ \int_{X \times Y} f \, d(\mu \otimes \nu) = \int_X \left( \int_Y f(x, y) \, d\nu(y) \right) d\mu(x) = \int_Y \left( \int_X f(x, y) \, d\mu(x) \right) d\nu(y) $$

**Exemple 1 : Calcul direct avec Tonelli**
Soit $X = Y = [0, 1]$ munis de la mesure de Lebesgue et $f(x, y) = x^2 y$. La fonction $f$ est continue donc mesurable, et positive sur $X \times Y$.
D'après Tonelli :
$$ \int_{[0, 1]^2} x^2 y \, dx dy = \int_0^1 \left( \int_0^1 x^2 y \, dy \right) dx $$
L'intégrale intérieure est $\int_0^1 x^2 y \, dy = x^2 \left[ \frac{y^2}{2} \right]_0^1 = \frac{x^2}{2}$.
Puis, $\int_0^1 \frac{x^2}{2} \, dx = \left[ \frac{x^3}{6} \right]_0^1 = \frac{1}{6}$.
En inversant l'ordre, $\int_0^1 \left( \int_0^1 x^2 y \, dx \right) dy = \int_0^1 y \left[ \frac{x^3}{3} \right]_0^1 dy = \int_0^1 \frac{y}{3} \, dy = \left[ \frac{y^2}{6} \right]_0^1 = \frac{1}{6}$.

### Théorème de Fubini (Cas des fonctions intégrables)

Soient $(X, \mathcal{F}, \mu)$ et $(Y, \mathcal{G}, \nu)$ deux espaces mesurés **$\sigma$-finis**.
Soit $f : X \times Y \to \mathbb{R}$ ou $\mathbb{C}$ une fonction $\mathcal{F} \otimes \mathcal{G}$-mesurable.

Si l'une des intégrales itérées de la **valeur absolue** $|f|$ est finie, c'est-à-dire si :
$$ \int_X \left( \int_Y |f(x, y)| \, d\nu(y) \right) d\mu(x) < +\infty \quad \text{ou} \quad \int_Y \left( \int_X |f(x, y)| \, d\mu(x) \right) d\nu(y) < +\infty $$
(ou si $\int_{X \times Y} |f| \, d(\mu \otimes \nu) < +\infty$), alors :

1. $f$ est $\mu \otimes \nu$-intégrable.
2. Pour $\mu$-presque tout $x \in X$, la fonction $y \mapsto f(x, y)$ est $\nu$-intégrable.
3. Pour $\nu$-presque tout $y \in Y$, la fonction $x \mapsto f(x, y)$ est $\mu$-intégrable.
4. Les fonctions $x \mapsto \int_Y f(x, y) \, d\nu(y)$ (définie p.p.) et $y \mapsto \int_X f(x, y) \, d\mu(x)$ (définie p.p.) sont respectivement $\mu$-intégrable et $\nu$-intégrable.
5. On a l'égalité :
   $$ \int_{X \times Y} f \, d(\mu \otimes \nu) = \int_X \left( \int_Y f(x, y) \, d\nu(y) \right) d\mu(x) = \int_Y \left( \int_X f(x, y) \, d\mu(x) \right) d\nu(y) $$

**Exemple 2 : Calcul de l'intégrale de Gauss**
Évaluons $I = \int_0^{+\infty} e^{-x^2} \, dx$.
On a $I^2 = \left( \int_0^{+\infty} e^{-x^2} \, dx \right) \left( \int_0^{+\infty} e^{-y^2} \, dy \right) = \int_0^{+\infty} \int_0^{+\infty} e^{-(x^2+y^2)} \, dx dy$.
La fonction $(x,y) \mapsto e^{-(x^2+y^2)}$ est positive et continue sur $\mathbb{R}_+^2$, on peut appliquer Tonelli pour justifier l'écriture sous forme d'intégrale double.
Un changement de variables en coordonnées polaires (qui nécessite la formule du changement de variable, s'appuyant sur les mêmes fondations) donne :
$x = r \cos \theta, y = r \sin \theta$. Le domaine $[0, +\infty[ \times [0, +\infty[$ correspond à $r \in [0, +\infty[$ et $\theta \in [0, \pi/2]$. Le jacobien est $r$.
$$ I^2 = \int_0^{\pi/2} \int_0^{+\infty} e^{-r^2} r \, dr d\theta $$
Par Tonelli, on peut séparer les intégrales :
$$ I^2 = \left( \int_0^{\pi/2} d\theta \right) \left( \int_0^{+\infty} r e^{-r^2} \, dr \right) = \left( \frac{\pi}{2} \right) \left[ -\frac{1}{2} e^{-r^2} \right]_0^{+\infty} = \frac{\pi}{2} \times \frac{1}{2} = \frac{\pi}{4} $$
Ainsi, $I = \frac{\sqrt{\pi}}{2}$.

**Exemple 3 : Cas pathologique, la condition d'intégrabilité absolue est nécessaire**
Considérons l'espace $X = Y = \mathbb{N} \setminus \{0\}$ avec la mesure de comptage. L'intégrale est une série.
Soit la suite double $a_{i,j}$ définie par :
- $a_{i,i} = 1$ pour $i \ge 1$
- $a_{i,i+1} = -1$ pour $i \ge 1$
- $a_{i,j} = 0$ sinon.

La matrice associée est :
$$ \begin{pmatrix} 1 & -1 & 0 & 0 & \dots \\ 0 & 1 & -1 & 0 & \dots \\ 0 & 0 & 1 & -1 & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix} $$
Calculons les sommes itérées :
Sommation par lignes : $\sum_{i=1}^\infty \left( \sum_{j=1}^\infty a_{i,j} \right) = \sum_{i=1}^\infty (1 - 1) = \sum_{i=1}^\infty 0 = 0$.
Sommation par colonnes : $\sum_{j=1}^\infty \left( \sum_{i=1}^\infty a_{i,j} \right) = 1 + \sum_{j=2}^\infty (-1 + 1) = 1 + 0 = 1$.
Les deux intégrales itérées existent mais sont distinctes ($0 \neq 1$).
Pourquoi le théorème de Fubini échoue-t-il ? Vérifions la condition de Fubini sur la valeur absolue :
$\sum_{i=1}^\infty \sum_{j=1}^\infty |a_{i,j}| = \sum_{i=1}^\infty (1 + 1) = \sum_{i=1}^\infty 2 = +\infty$.
La condition d'intégrabilité absolue (Tonelli sur la valeur absolue) n'est pas remplie, interdisant l'interversion.

## 3. Démonstrations

La démonstration complète s'appuie sur la théorie des classes monotones, permettant de passer de propriétés vraies sur des rectangles mesurables à toute la tribu produit.

**Lemme des classes monotones (Théorème $\pi-\lambda$ de Dynkin) :**
Soit $\Omega$ un ensemble. Une classe $\mathcal{P}$ de sous-ensembles de $\Omega$ stable par intersection finie (un $\pi$-système) et $\mathcal{L}$ un $\lambda$-système (contenant $\Omega$, stable par complémentaire et réunion dénombrable disjointe). Si $\mathcal{P} \subset \mathcal{L}$, alors la tribu engendrée $\sigma(\mathcal{P}) \subset \mathcal{L}$.

**Preuve du Théorème de Tonelli (Esquisse pour les ensembles) :**
On commence par prouver le résultat pour les fonctions indicatrices $f = \mathbf{1}_E$ où $E \in \mathcal{F} \otimes \mathcal{G}$.
Considérons $\mathcal{L} = \{ E \in \mathcal{F} \otimes \mathcal{G} \mid \text{le théorème est vrai pour } \mathbf{1}_E \}$.
Pour un rectangle $E = A \times B$ avec $A \in \mathcal{F}, B \in \mathcal{G}$.
$f(x, y) = \mathbf{1}_{A \times B}(x, y) = \mathbf{1}_A(x) \mathbf{1}_B(y)$.
$\int_Y \mathbf{1}_A(x) \mathbf{1}_B(y) d\nu(y) = \mathbf{1}_A(x) \nu(B)$.
Puis $\int_X \mathbf{1}_A(x) \nu(B) d\mu(x) = \mu(A)\nu(B) = (\mu \otimes \nu)(A \times B)$.
Le théorème est vrai pour la classe $\mathcal{P}$ des rectangles mesurables, qui est un $\pi$-système engendrant $\mathcal{F} \otimes \mathcal{G}$.
On montre ensuite que $\mathcal{L}$ est un $\lambda$-système (en utilisant les propriétés de l'intégrale et le théorème de convergence monotone pour les réunions croissantes). Par le théorème des classes monotones, $\mathcal{L} = \mathcal{F} \otimes \mathcal{G}$.

On étend ensuite le résultat des indicatrices aux fonctions étagées positives par linéarité.
Enfin, pour $f \ge 0$ mesurable quelconque, il existe une suite croissante de fonctions étagées positives $(s_n)$ convergeant simplement vers $f$. Par le théorème de convergence monotone de Lebesgue (Jalon 67), l'interversion de la limite et des intégrales successives permet de conclure pour $f$.

**Preuve du Théorème de Fubini :**
Soit $f$ mesurable telle que $\int_X (\int_Y |f| d\nu) d\mu < +\infty$.
On décompose $f = f^+ - f^-$, avec $f^+, f^- \ge 0$.
On sait que $|f| = f^+ + f^-$.
En appliquant Tonelli à $|f|$, on obtient que $\int_{X \times Y} |f| d(\mu \otimes \nu) = \int_X (\int_Y |f| d\nu) d\mu < +\infty$, donc $f$ est intégrable pour la mesure produit.
Les fonctions $f^+$ et $f^-$ sont positives et dominées par $|f|$, elles sont donc intégrables.
On applique Tonelli séparément à $f^+$ et $f^-$ :
$\int_Y f d\nu = \int_Y f^+ d\nu - \int_Y f^- d\nu$ (cette écriture est justifiée presque partout car les intégrales sont finies p.p.).
En intégrant par rapport à $\mu$ :
$$ \int_X \left( \int_Y f d\nu \right) d\mu = \int_X \left( \int_Y f^+ d\nu \right) d\mu - \int_X \left( \int_Y f^- d\nu \right) d\mu $$
Par Tonelli sur $f^+$ et $f^-$, ceci est égal à $\int_{X \times Y} f^+ d(\mu \otimes \nu) - \int_{X \times Y} f^- d(\mu \otimes \nu) = \int_{X \times Y} f d(\mu \otimes \nu)$.
Le même raisonnement vaut pour l'intégration dans l'autre ordre. La condition $\sigma$-finie assure qu'il n'y a pas d'ambiguïté sur les domaines de mesure infinie.

## 4. Applications en Physique, Logique et AI

**1. Calcul des Lois Marginales en Probabilités :**
En statistiques et en apprentissage automatique probabiliste, la densité conjointe de deux variables aléatoires continues $X$ et $Y$ est $f_{X,Y}(x, y)$.
Pour trouver la densité marginale de $X$, on intègre sur toutes les valeurs possibles de $Y$ :
$$ f_X(x) = \int_{\mathbb{R}} f_{X,Y}(x, y) \, dy $$
Pour que la probabilité totale reste de $1$ : $\int f_X(x) dx = \int \int f_{X,Y}(x, y) dy dx = 1$. C'est le théorème de Fubini qui garantit de manière formelle que cette double sommation continue est valide et donne toujours $1$.

**2. Optimisation et Fonctions de Perte dans l'IA :**
Dans les modèles génératifs comme les Variational Autoencoders (VAE) ou les modèles de diffusion, la fonction d'objectif implique souvent l'espérance d'une intégrale par rapport à des variables latentes.
Le calcul du gradient d'une espérance :
$$ \nabla_\theta \mathbb{E}_{z \sim p_\theta}[f(z)] = \nabla_\theta \int f(z) p_\theta(z) dz $$
L'interversion de la dérivée (qui est une limite) et de l'intégrale requiert la convergence dominée, mais les réarrangements des variables dans les bornes (le "Reparameterization Trick") s'appuient fondamentalement sur les structures d'espaces produits justifiées par Fubini.

**3. Traitement du Signal et Convolution :**
La transformée de Fourier et le produit de convolution de signaux continus s'appuient sur Fubini.
Pour deux fonctions $f, g \in L^1(\mathbb{R})$, leur produit de convolution $(f * g)(x) = \int_{\mathbb{R}} f(t) g(x-t) dt$ est bien défini presque partout et est dans $L^1(\mathbb{R})$.
La démonstration repose sur l'intégration de la fonction $(x,t) \mapsto |f(t)g(x-t)|$ sur $\mathbb{R}^2$ via Tonelli.
Dans les Réseaux de Neurones Convolutifs (CNN), une convolution 2D stricte (filtre $k \times k$) peut être séparée en deux convolutions 1D (séparabilité spatiale, souvent exploitée avec des filtres gaussiens), ce qui est une application discrète du principe de Fubini réduisant la complexité algorithmique de $O(k^2)$ à $O(2k)$.
