---
uuid: "jalon-18"
title: "Continuité des fonctions d'une variable réelle"
year: 1
trimester: 2
tags:
  - math/analyse
prev: "[[Jalon-17.md]]"
next: "[[Jalon-19.md]]"
---

### 1. Présentation du concept clé

La notion de continuité, intuitivement appréhendée comme la capacité de tracer une courbe sans lever le crayon, est l'une des pierres angulaires de l'analyse mathématique. Pourtant, cette intuition, si féconde soit-elle pour les fonctions "gentilles" de la géométrie euclidienne, s'est avérée être un piège conceptuel majeur au XIXe siècle, confrontée à l'émergence de fonctions aux comportements pathologiques.

Avant l'ère de la rigueur arithmétique, des mathématiciens comme Euler et Lagrange manipulaient des fonctions en s'appuyant sur une compréhension géométrique et souvent implicite de leur régularité. La "continuité" était alors synonyme de "formule unique" ou d'absence de "sauts". Cependant, les travaux sur les séries de Fourier, notamment ceux de Dirichlet et Riemann, révélèrent des fonctions définies par des séries infinies qui, bien que convergentes, ne se conformaient pas à cette vision simpliste. La limite d'une suite de fonctions continues n'était pas nécessairement continue, un fait déconcertant qui ébranla les fondements de l'analyse.

C'est Augustin-Louis Cauchy, au début du XIXe siècle, qui tenta de formaliser la continuité. Sa définition, souvent paraphrasée comme "une fonction est continue si une variation infiniment petite de la variable indépendante produit une variation infiniment petite de la variable dépendante", représentait un pas crucial vers l'arithmétisation. Cependant, le concept d'"infiniment petit" restait ambigu, hérité de Leibniz, et manquait de la précision nécessaire pour éviter les paradoxes. Cauchy lui-même commit des erreurs, affirmant par exemple que la limite ponctuelle d'une suite de fonctions continues était toujours continue, une assertion réfutée par des contre-exemples simples comme la suite $f_n(x) = x^n$ sur $[0,1]$.

L'impasse intellectuelle devint manifeste. La géométrie ne suffisait plus. Les "infiniment petits" devaient être quantifiés. C'est Karl Weierstrass, vers 1870, qui, avec une rigueur implacable, fournit la définition moderne, celle qui allait devenir le standard universel. Il remplaça l'intuition floue par une quantification précise des "petites variations", utilisant les célèbres quantificateurs $\epsilon$ et $\delta$. Cette définition, purement arithmétique, libéra l'analyse de ses dépendances géométriques et permit de distinguer clairement entre continuité ponctuelle, continuité uniforme, et d'autres formes de régularité. Elle ouvrit la voie à l'étude de fonctions aux propriétés contre-intuitives, comme la fonction de Weierstrass elle-même, continue partout mais nulle part différentiable, ou la fonction de Dirichlet, discontinue partout. La continuité, dès lors, n'était plus une évidence géométrique, mais une propriété structurelle rigoureusement définie, essentielle à la construction cohérente de l'édifice de l'analyse.

### 2. Formalisation

La continuité d'une fonction est une propriété locale, définie point par point, mais elle peut être étendue à un ensemble. La distinction entre continuité ponctuelle et continuité uniforme est fondamentale.

#### A. Énoncé Symbolique Strict

Soit $D$ un sous-ensemble de $\mathbb{R}$ et $f: D \to \mathbb{R}$ une fonction.

**Définition 2.1 (Continuité en un point)**
La fonction $f$ est dite continue en un point $x_0 \in D$ si :
$$ \forall \epsilon > 0, \exists \delta > 0, \forall x \in D, (|x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon) $$

**Définition 2.2 (Continuité sur un ensemble)**
La fonction $f$ est dite continue sur un ensemble $A \subseteq D$ si elle est continue en tout point $x_0 \in A$.

**Définition 2.3 (Continuité séquentielle en un point)**
La fonction $f$ est dite séquentiellement continue en un point $x_0 \in D$ si pour toute suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $D$ qui converge vers $x_0$, la suite des images $(f(x_n))_{n \in \mathbb{N}}$ converge vers $f(x_0)$.
$$ \forall (x_n)_{n \in \mathbb{N}} \subset D, (x_n \to x_0 \implies f(x_n) \to f(x_0)) $$

**Définition 2.4 (Continuité uniforme sur un ensemble)**
La fonction $f$ est dite uniformément continue sur un ensemble $A \subseteq D$ si :
$$ \forall \epsilon > 0, \exists \delta > 0, \forall x, y \in A, (|x - y| < \delta \implies |f(x) - f(y)| < \epsilon) $$

**Définition 2.5 (Compacité locale de $\mathbb{R}$)**
Un espace topologique $X$ est dit localement compact si tout point $x \in X$ possède un voisinage compact.
Pour $\mathbb{R}$ muni de sa topologie usuelle (induite par la métrique), cela signifie que pour tout $x \in \mathbb{R}$, il existe un ensemble $K$ compact tel que $x \in K^\circ \subseteq K$.

#### B. Anatomie et Typage Chirurgical

Dissectons la Définition 2.1 de la continuité en un point $x_0$:

*   $\forall \epsilon > 0$: Ce quantificateur universel exprime l'idée que la "proximité" des images peut être rendue arbitrairement petite. Il s'agit d'un défi : "Quel que soit le seuil de tolérance positif que vous me donnez pour la différence des images..."
*   $\exists \delta > 0$: Ce quantificateur existentiel est la réponse au défi. "...je peux trouver un rayon positif autour de $x_0$..." L'existence de ce $\delta$ dépend généralement de $\epsilon$ et de $x_0$.
*   $\forall x \in D$: "...pour tout point $x$ dans le domaine de la fonction..."
*   $(|x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon)$: C'est l'implication fondamentale. "...si $x$ est suffisamment proche de $x_0$ (à une distance inférieure à $\delta$), alors son image $f(x)$ est nécessairement proche de $f(x_0)$ (à une distance inférieure à $\epsilon$)."

La distinction avec la continuité uniforme (Définition 2.4) est cruciale :
Dans la continuité uniforme, le $\delta$ choisi ne dépend que de $\epsilon$, et non des points $x$ ou $y$ spécifiques. Il est "uniforme" sur tout l'ensemble $A$. Cela signifie qu'une même "fenêtre" de $\delta$ fonctionne pour tous les points de $A$. Pour la continuité ponctuelle, le $\delta$ peut varier d'un point $x_0$ à l'autre.

Concernant la compacité locale de $\mathbb{R}$:
*   $\mathbb{R}$ est localement compact car pour tout $x \in \mathbb{R}$, l'intervalle fermé $[x-1, x+1]$ est un voisinage compact de $x$. En effet, $[x-1, x+1]$ est fermé et borné, donc compact dans $\mathbb{R}$ par le théorème de Heine-Borel. L'intérieur de cet intervalle, $(x-1, x+1)$, contient $x$ et est inclus dans $[x-1, x+1]$.

#### C. Exemples de Validation

1.  **Fonction constante:** $f(x) = c$ pour tout $x \in \mathbb{R}$.
    Soit $x_0 \in \mathbb{R}$ et $\epsilon > 0$. Nous devons trouver $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
    Puisque $f(x) = c$ et $f(x_0) = c$, nous avons $|f(x) - f(x_0)| = |c - c| = 0$.
    Comme $0 < \epsilon$ pour tout $\epsilon > 0$, l'inégalité $|f(x) - f(x_0)| < \epsilon$ est toujours satisfaite, quelle que soit la valeur de $\delta$. Nous pouvons donc choisir n'importe quel $\delta > 0$ (par exemple $\delta = 1$).
    La fonction constante est continue sur $\mathbb{R}$.

2.  **Fonction identité:** $f(x) = x$ pour tout $x \in \mathbb{R}$.
    Soit $x_0 \in \mathbb{R}$ et $\epsilon > 0$. Nous cherchons $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
    Nous avons $|f(x) - f(x_0)| = |x - x_0|$.
    Si nous choisissons $\delta = \epsilon$, alors $|x - x_0| < \delta$ implique $|x - x_0| < \epsilon$, ce qui est exactement $|f(x) - f(x_0)| < \epsilon$.
    La fonction identité est continue sur $\mathbb{R}$.

3.  **Fonction quadratique:** $f(x) = x^2$ pour tout $x \in \mathbb{R}$.
    Soit $x_0 \in \mathbb{R}$ et $\epsilon > 0$. Nous voulons trouver $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|x^2 - x_0^2| < \epsilon$.
    Nous avons $|x^2 - x_0^2| = |(x - x_0)(x + x_0)| = |x - x_0| |x + x_0|$.
    Si nous imposons une condition initiale sur $\delta$, par exemple $\delta \le 1$, alors $|x - x_0| < \delta \le 1$.
    Ceci implique $x_0 - 1 < x < x_0 + 1$.
    Alors $|x + x_0| = |x - x_0 + 2x_0| \le |x - x_0| + |2x_0| < \delta + 2|x_0|$.
    Donc, $|x^2 - x_0^2| < \delta (\delta + 2|x_0|)$.
    Nous voulons que $\delta (\delta + 2|x_0|) < \epsilon$.
    Si nous choisissons $\delta \le 1$, alors $\delta + 2|x_0| \le 1 + 2|x_0|$.
    Donc, $|x^2 - x_0^2| < \delta (1 + 2|x_0|)$.
    Pour que cela soit inférieur à $\epsilon$, nous pouvons choisir $\delta = \min\left(1, \frac{\epsilon}{1 + 2|x_0|}\right)$.
    Avec ce choix de $\delta$, si $|x - x_0| < \delta$, alors $|x^2 - x_0^2| < \delta (1 + 2|x_0|) \le \frac{\epsilon}{1 + 2|x_0|} (1 + 2|x_0|) = \epsilon$.
    La fonction $f(x) = x^2$ est continue sur $\mathbb{R}$.

#### D. Cas Pathologiques et Contre-exemples

1.  **Fonction discontinue en un point (saut):**
    Soit $f: \mathbb{R} \to \mathbb{R}$ définie par :
    $$ f(x) = \begin{cases} 1 & \text{si } x \ge 0 \\ 0 & \text{si } x < 0 \end{cases} $$
    Montrons que $f$ n'est pas continue en $x_0 = 0$.
    Supposons par contradiction que $f$ est continue en $x_0 = 0$. Alors pour $\epsilon = 1/2$, il existerait $\delta > 0$ tel que si $|x - 0| < \delta$, alors $|f(x) - f(0)| < 1/2$.
    Nous avons $f(0) = 1$. Donc, nous devrions avoir $|f(x) - 1| < 1/2$, ce qui signifie $1/2 < f(x) < 3/2$.
    Cependant, pour tout $x \in (-\delta, 0)$, nous avons $x < 0$, donc $f(x) = 0$.
    Mais $0$ n'est pas dans l'intervalle $(1/2, 3/2)$.
    Ainsi, pour tout $x \in (-\delta, 0)$, la condition $|f(x) - f(0)| < 1/2$ n'est pas satisfaite.
    La fonction $f$ n'est pas continue en $x_0 = 0$.

2.  **Fonction de Dirichlet (discontinue partout):**
    Soit $D: \mathbb{R} \to \mathbb{R}$ définie par :
    $$ D(x) = \begin{cases} 1 & \text{si } x \in \mathbb{Q} \\ 0 & \text{si } x \notin \mathbb{Q} \end{cases} $$
    Montrons que $D$ est discontinue en tout point $x_0 \in \mathbb{R}$.
    *   **Cas 1: $x_0 \in \mathbb{Q}$.** Alors $D(x_0) = 1$.
        Pour tout $\delta > 0$, l'intervalle $(x_0 - \delta, x_0 + \delta)$ contient toujours des nombres irrationnels (densité des irrationnels dans $\mathbb{R}$).
        Soit $x \in (x_0 - \delta, x_0 + \delta)$ un nombre irrationnel. Alors $D(x) = 0$.
        La différence $|D(x) - D(x_0)| = |0 - 1| = 1$.
        Si nous choisissons $\epsilon = 1/2$, alors pour tout $\delta > 0$, il existe un $x$ tel que $|x - x_0| < \delta$ mais $|D(x) - D(x_0)| = 1 \not< 1/2$.
        Donc $D$ n'est pas continue en $x_0 \in \mathbb{Q}$.
    *   **Cas 2: $x_0 \notin \mathbb{Q}$.** Alors $D(x_0) = 0$.
        Pour tout $\delta > 0$, l'intervalle $(x_0 - \delta, x_0 + \delta)$ contient toujours des nombres rationnels (densité des rationnels dans $\mathbb{R}$).
        Soit $x \in (x_0 - \delta, x_0 + \delta)$ un nombre rationnel. Alors $D(x) = 1$.
        La différence $|D(x) - D(x_0)| = |1 - 0| = 1$.
        De même, pour $\epsilon = 1/2$, il existe un $x$ tel que $|x - x_0| < \delta$ mais $|D(x) - D(x_0)| = 1 \not< 1/2$.
        Donc $D$ n'est pas continue en $x_0 \notin \mathbb{Q}$.
    La fonction de Dirichlet est discontinue partout sur $\mathbb{R}$.

3.  **Fonction de Thomae (Popcorn function):**
    Soit $T: [0,1] \to \mathbb{R}$ définie par :
    $$ T(x) = \begin{cases} 1/q & \text{si } x = p/q \text{ est un rationnel irréductible, } q > 0 \\ 0 & \text{si } x \text{ est irrationnel ou } x=0 \end{cases} $$
    (Pour $x=0$, on peut le considérer comme $0/1$, donc $T(0)=0/1=0$ ou $T(0)=0$ par définition).
    *   **Continuité aux irrationnels:** Soit $x_0 \notin \mathbb{Q}$ et $x_0 \in (0,1)$. Alors $T(x_0) = 0$.
        Soit $\epsilon > 0$. Nous voulons trouver $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|T(x) - T(x_0)| < \epsilon$, c'est-à-dire $|T(x)| < \epsilon$.
        Il n'y a qu'un nombre fini de rationnels $p/q$ dans $[0,1]$ tels que $q \le 1/\epsilon$. (Par exemple, pour $q=1$, $0/1, 1/1$; pour $q=2$, $1/2$; pour $q=3$, $1/3, 2/3$, etc.).
        Soit $S_\epsilon = \{p/q \in [0,1] \mid q \le 1/\epsilon\}$. Cet ensemble est fini.
        Puisque $x_0$ est irrationnel, $x_0 \notin S_\epsilon$.
        Nous pouvons choisir $\delta$ suffisamment petit pour que l'intervalle $(x_0 - \delta, x_0 + \delta)$ ne contienne aucun point de $S_\epsilon$ (à l'exception possible de $x_0$ lui-même, mais $x_0$ n'est pas dans $S_\epsilon$). Par exemple, $\delta = \min_{r \in S_\epsilon} |x_0 - r|$.
        Si $x \in (x_0 - \delta, x_0 + \delta)$ et $x \ne x_0$:
        Si $x$ est irrationnel, $T(x) = 0 < \epsilon$.
        Si $x$ est rationnel, $x = p/q$. Alors $x \notin S_\epsilon$, ce qui signifie que $q > 1/\epsilon$.
        Dans ce cas, $T(x) = 1/q < \epsilon$.
        Donc, pour tout $x$ dans l'intervalle, $|T(x) - T(x_0)| = |T(x) - 0| = T(x) < \epsilon$.
        La fonction de Thomae est continue en tout point irrationnel.
    *   **Discontinuité aux rationnels:** Soit $x_0 = p/q \in \mathbb{Q} \cap (0,1)$ (irréductible). Alors $T(x_0) = 1/q > 0$.
        Pour tout $\delta > 0$, l'intervalle $(x_0 - \delta, x_0 + \delta)$ contient toujours des nombres irrationnels (densité des irrationnels).
        Soit $x \in (x_0 - \delta, x_0 + \delta)$ un nombre irrationnel. Alors $T(x) = 0$.
        La différence $|T(x) - T(x_0)| = |0 - 1/q| = 1/q$.
        Si nous choisissons $\epsilon = 1/(2q)$, alors pour tout $\delta > 0$, il existe un $x$ tel que $|x - x_0| < \delta$ mais $|T(x) - T(x_0)| = 1/q \not< 1/(2q)$.
        La fonction de Thomae est discontinue en tout point rationnel.

4.  **Non-uniforme continuité:** $f(x) = x^2$ sur $\mathbb{R}$.
    Nous avons montré que $f(x) = x^2$ est continue sur $\mathbb{R}$. Montrons qu'elle n'est pas uniformément continue.
    La négation de la continuité uniforme est :
    $\exists \epsilon_0 > 0, \forall \delta > 0, \exists x, y \in \mathbb{R}, (|x - y| < \delta \text{ et } |f(x) - f(y)| \ge \epsilon_0)$.
    Choisissons $\epsilon_0 = 1$.
    Soit $\delta > 0$ arbitraire. Nous devons trouver $x, y$ tels que $|x - y| < \delta$ mais $|x^2 - y^2| \ge 1$.
    Soit $x = 1/\delta$ et $y = 1/\delta + \delta/2$.
    Alors $|x - y| = |\delta/2| = \delta/2 < \delta$.
    Et $|x^2 - y^2| = |(x-y)(x+y)| = |\delta/2 (1/\delta + 1/\delta + \delta/2)| = |\delta/2 (2/\delta + \delta/2)| = |1 + \delta^2/4|$.
    Puisque $\delta > 0$, $1 + \delta^2/4 > 1$.
    Donc, $|f(x) - f(y)| = 1 + \delta^2/4 \ge 1 = \epsilon_0$.
    Ainsi, $f(x) = x^2$ n'est pas uniformément continue sur $\mathbb{R}$.

### 3. Démonstrations

#### A. Équivalence de la continuité $\epsilon-\delta$ et de la continuité séquentielle

**Théorème 3.1:** Soit $f: D \to \mathbb{R}$ une fonction et $x_0 \in D$. La fonction $f$ est continue en $x_0$ (au sens $\epsilon-\delta$) si et seulement si elle est séquentiellement continue en $x_0$.

**Démonstration:**

**Partie 1: ($\epsilon-\delta$ continuité $\implies$ continuité séquentielle)**
Supposons que $f$ est continue en $x_0$ au sens $\epsilon-\delta$.
Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments de $D$ telle que $x_n \to x_0$. Nous voulons montrer que $f(x_n) \to f(x_0)$.
Par définition de la convergence de suite, pour tout $\delta > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $|x_n - x_0| < \delta$.

Soit $\epsilon > 0$ arbitraire.
Puisque $f$ est continue en $x_0$, par la définition $\epsilon-\delta$, il existe un $\delta_0 > 0$ tel que pour tout $x \in D$, si $|x - x_0| < \delta_0$, alors $|f(x) - f(x_0)| < \epsilon$.

Maintenant, utilisons la convergence de la suite $(x_n)$. Pour ce $\delta_0$, il existe un entier $N_0 \in \mathbb{N}$ tel que pour tout $n \ge N_0$, nous avons $|x_n - x_0| < \delta_0$.
En combinant ces deux faits, pour tout $n \ge N_0$, nous avons $|x_n - x_0| < \delta_0$, ce qui implique $|f(x_n) - f(x_0)| < \epsilon$.
Ceci est précisément la définition de la convergence de la suite $(f(x_n))$ vers $f(x_0)$.
Donc, $f$ est séquentiellement continue en $x_0$.

**Partie 2: (Continuité séquentielle $\implies$ $\epsilon-\delta$ continuité)**
Nous allons démontrer cette partie par contraposition.
Supposons que $f$ n'est *pas* continue en $x_0$ au sens $\epsilon-\delta$.
Cela signifie que la négation de la définition $\epsilon-\delta$ est vraie :
$\exists \epsilon_0 > 0, \forall \delta > 0, \exists x \in D, (|x - x_0| < \delta \text{ et } |f(x) - f(x_0)| \ge \epsilon_0)$.

Nous devons construire une suite $(x_n)$ qui converge vers $x_0$ mais telle que $(f(x_n))$ ne converge pas vers $f(x_0)$.
Pour l'$\epsilon_0$ qui existe, appliquons la négation de la définition $\epsilon-\delta$ pour une suite de $\delta$ décroissante.
Pour chaque entier $n \ge 1$, choisissons $\delta_n = 1/n$.
Alors, pour ce $\delta_n$, il existe un $x_n \in D$ tel que :
1. $|x_n - x_0| < \delta_n = 1/n$
2. $|f(x_n) - f(x_0)| \ge \epsilon_0$

Considérons la suite $(x_n)_{n \in \mathbb{N}}$.
De la condition (1), puisque $0 \le |x_n - x_0| < 1/n$ et $1/n \to 0$ quand $n \to \infty$, par le théorème des gendarmes, nous avons $x_n \to x_0$.
Cependant, de la condition (2), pour tout $n \ge 1$, la distance entre $f(x_n)$ et $f(x_0)$ est toujours supérieure ou égale à $\epsilon_0$.
Ceci signifie que la suite $(f(x_n))$ ne peut pas converger vers $f(x_0)$, car elle ne peut pas être rendue arbitrairement proche de $f(x_0)$ (elle reste toujours à une distance d'au moins $\epsilon_0$).
Donc, $f$ n'est pas séquentiellement continue en $x_0$.
Par contraposition, si $f$ est séquentiellement continue en $x_0$, alors elle est continue en $x_0$ au sens $\epsilon-\delta$.

#### B. Propriétés des fonctions continues

**Théorème 3.2 (Opérations algébriques sur les fonctions continues):**
Soient $f: D \to \mathbb{R}$ et $g: D \to \mathbb{R}$ deux fonctions continues en un point $x_0 \in D$.
Alors :
1.  $f+g$ est continue en $x_0$.
2.  $f \cdot g$ est continue en $x_0$.
3.  Si $g(x_0) \ne 0$, alors $f/g$ est continue en $x_0$.

**Démonstration (pour $f+g$):**
Soit $\epsilon > 0$.
Puisque $f$ est continue en $x_0$, il existe $\delta_1 > 0$ tel que si $|x - x_0| < \delta_1$, alors $|f(x) - f(x_0)| < \epsilon/2$.
Puisque $g$ est continue en $x_0$, il existe $\delta_2 > 0$ tel que si $|x - x_0| < \delta_2$, alors $|g(x) - g(x_0)| < \epsilon/2$.
Soit $\delta = \min(\delta_1, \delta_2)$. Si $|x - x_0| < \delta$, alors les deux inégalités précédentes sont valides.
Alors, pour $|x - x_0| < \delta$:
$|(f+g)(x) - (f+g)(x_0)| = |f(x) + g(x) - f(x_0) - g(x_0)|$
$= |(f(x) - f(x_0)) + (g(x) - g(x_0))|$
$\le |f(x) - f(x_0)| + |g(x) - g(x_0)|$ (par l'inégalité triangulaire)
$< \epsilon/2 + \epsilon/2 = \epsilon$.
Donc, $f+g$ est continue en $x_0$.

**Démonstration (pour $f \cdot g$):**
Soit $\epsilon > 0$.
Nous voulons montrer que $|f(x)g(x) - f(x_0)g(x_0)| < \epsilon$.
$|f(x)g(x) - f(x_0)g(x_0)| = |f(x)g(x) - f(x_0)g(x) + f(x_0)g(x) - f(x_0)g(x_0)|$
$= |(f(x) - f(x_0))g(x) + f(x_0)(g(x) - g(x_0))|$
$\le |f(x) - f(x_0)||g(x)| + |f(x_0)||g(x) - g(x_0)|$.

Puisque $g$ est continue en $x_0$, pour $\delta_g=1$, il existe $\delta_1 > 0$ tel que si $|x - x_0| < \delta_1$, alors $|g(x) - g(x_0)| < 1$.
Ceci implique $|g(x)| < |g(x_0)| + 1$. Soit $M = |g(x_0)| + 1$.
Puisque $f$ est continue en $x_0$, il existe $\delta_2 > 0$ tel que si $|x - x_0| < \delta_2$, alors $|f(x) - f(x_0)| < \frac{\epsilon}{2M}$.
Puisque $g$ est continue en $x_0$, il existe $\delta_3 > 0$ tel que si $|x - x_0| < \delta_3$, alors $|g(x) - g(x_0)| < \frac{\epsilon}{2(|f(x_0)|+1)}$ (pour éviter la division par zéro si $f(x_0)=0$).
Soit $\delta = \min(\delta_1, \delta_2, \delta_3)$. Si $|x - x_0| < \delta$:
$|f(x)g(x) - f(x_0)g(x_0)| \le |f(x) - f(x_0)||g(x)| + |f(x_0)||g(x) - g(x_0)|$
$< \frac{\epsilon}{2M} \cdot M + |f(x_0)| \cdot \frac{\epsilon}{2(|f(x_0)|+1)}$
$= \frac{\epsilon}{2} + \frac{|f(x_0)|}{|f(x_0)|+1} \frac{\epsilon}{2}$
$\le \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
Donc, $f \cdot g$ est continue en $x_0$.

**Théorème 3.3 (Composition de fonctions continues):**
Soient $f: D_f \to \mathbb{R}$ et $g: D_g \to \mathbb{R}$ deux fonctions telles que $f(D_f) \subseteq D_g$.
Si $f$ est continue en $x_0 \in D_f$ et $g$ est continue en $y_0 = f(x_0) \in D_g$, alors la fonction composée $g \circ f: D_f \to \mathbb{R}$ est continue en $x_0$.

**Démonstration:**
Soit $\epsilon > 0$. Nous voulons montrer que $\exists \delta > 0$ tel que si $|x - x_0| < \delta$, alors $|(g \circ f)(x) - (g \circ f)(x_0)| < \epsilon$.
C'est-à-dire $|g(f(x)) - g(f(x_0))| < \epsilon$.

Puisque $g$ est continue en $y_0 = f(x_0)$, pour cet $\epsilon$, il existe un $\delta_g > 0$ tel que pour tout $y \in D_g$, si $|y - y_0| < \delta_g$, alors $|g(y) - g(y_0)| < \epsilon$.

Maintenant, utilisons la continuité de $f$ en $x_0$. Pour ce $\delta_g$ (qui joue le rôle d'un $\epsilon$ pour $f$), il existe un $\delta_f > 0$ tel que pour tout $x \in D_f$, si $|x - x_0| < \delta_f$, alors $|f(x) - f(x_0)| < \delta_g$.

Soit $\delta = \delta_f$.
Si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \delta_g$.
Posons $y = f(x)$. Alors $|y - y_0| < \delta_g$.
Puisque $y \in D_g$ (car $f(D_f) \subseteq D_g$), nous pouvons appliquer la continuité de $g$:
$|g(y) - g(y_0)| < \epsilon$.
C'est-à-dire $|g(f(x)) - g(f(x_0))| < \epsilon$.
Donc, $g \circ f$ est continue en $x_0$.

#### C. Théorème des Valeurs Intermédiaires (TVI)

**Théorème 3.4 (Théorème des Valeurs Intermédiaires):**
Soit $f: [a,b] \to \mathbb{R}$ une fonction continue sur l'intervalle fermé et borné $[a,b]$.
Si $y$ est un nombre réel compris entre $f(a)$ et $f(b)$ (c'est-à-dire $f(a) \le y \le f(b)$ ou $f(b) \le y \le f(a)$), alors il existe au moins un $c \in [a,b]$ tel que $f(c) = y$.

**Démonstration (par dichotomie):**
Sans perte de généralité, supposons $f(a) < y < f(b)$. (Si $f(a) = y$ ou $f(b) = y$, le théorème est trivialement vrai en prenant $c=a$ ou $c=b$. Si $f(b) < y < f(a)$, on peut considérer la fonction $-f$).

Nous allons construire une suite d'intervalles emboîtés $[a_n, b_n]$ tels que $f(a_n) \le y \le f(b_n)$ pour tout $n$, et la longueur de ces intervalles tend vers zéro.

1.  **Initialisation:** Posons $a_0 = a$ et $b_0 = b$. Nous avons $f(a_0) < y < f(b_0)$.

2.  **Itération:** Pour $n \ge 0$, supposons que nous avons un intervalle $[a_n, b_n]$ tel que $f(a_n) < y < f(b_n)$.
    Calculons le milieu $m_n = (a_n + b_n)/2$.
    *   Si $f(m_n) < y$: Alors la valeur $y$ se trouve dans l'intervalle $(f(m_n), f(b_n)]$. Nous posons $a_{n+1} = m_n$ et $b_{n+1} = b_n$.
    *   Si $f(m_n) > y$: Alors la valeur $y$ se trouve dans l'intervalle $[f(a_n), f(m_n))$. Nous posons $a_{n+1} = a_n$ et $b_{n+1} = m_n$.
    *   Si $f(m_n) = y$: Nous avons trouvé notre $c = m_n$. La démonstration est terminée.

3.  **Propriétés des suites:** Si le processus ne s'arrête pas (c'est-à-dire si $f(m_n) \ne y$ pour tout $n$), nous obtenons deux suites $(a_n)$ et $(b_n)$ avec les propriétés suivantes :
    *   $(a_n)$ est croissante et bornée supérieurement par $b$.
    *   $(b_n)$ est décroissante et bornée inférieurement par $a$.
    *   $a_n \le b_n$ pour tout $n$.
    *   $f(a_n) < y < f(b_n)$ pour tout $n$.
    *   La longueur de l'intervalle $[a_n, b_n]$ est $b_n - a_n = (b - a)/2^n$.

4.  **Convergence:** Puisque $(a_n)$ est croissante et bornée, elle converge vers une limite $c_1$. Puisque $(b_n)$ est décroissante et bornée, elle converge vers une limite $c_2$.
    De plus, $b_n - a_n = (b - a)/2^n \to 0$ quand $n \to \infty$.
    Donc, $c_1 = c_2$. Appelons cette limite $c$.
    Par construction, $a \le a_n \le c \le b_n \le b$ pour tout $n$, donc $c \in [a,b]$.

5.  **Conclusion par continuité:** Puisque $f$ est continue sur $[a,b]$, et $a_n \to c$ et $b_n \to c$, nous avons par continuité séquentielle (Théorème 3.1) :
    $\lim_{n \to \infty} f(a_n) = f(c)$
    $\lim_{n \to \infty} f(b_n) = f(c)$

    Nous savons que $f(a_n) < y$ pour tout $n$. En passant à la limite, $f(c) \le y$.
    Nous savons que $f(b_n) > y$ pour tout $n$. En passant à la limite, $f(c) \ge y$.
    Les deux inégalités $f(c) \le y$ et $f(c) \ge y$ impliquent $f(c) = y$.
    Ainsi, il existe bien un $c \in [a,b]$ tel que $f(c) = y$.

#### D. Continuité sur un compact (Heine-Weierstrass)

**Théorème 3.5 (Théorème de Heine-Cantor):**
Toute fonction continue sur un intervalle fermé et borné (donc compact) $[a,b]$ est uniformément continue sur cet intervalle.

**Démonstration:**
Supposons par contradiction que $f$ est continue sur $[a,b]$ mais n'est pas uniformément continue sur $[a,b]$.
La négation de la continuité uniforme (Définition 2.4) est :
$\exists \epsilon_0 > 0, \forall \delta > 0, \exists x, y \in [a,b], (|x - y| < \delta \text{ et } |f(x) - f(y)| \ge \epsilon_0)$.

Pour cet $\epsilon_0$, et pour chaque $n \in \mathbb{N}^*$, choisissons $\delta_n = 1/n$.
Alors, pour chaque $\delta_n$, il existe des points $x_n, y_n \in [a,b]$ tels que :
1.  $|x_n - y_n| < 1/n$
2.  $|f(x_n) - f(y_n)| \ge \epsilon_0$

Les suites $(x_n)$ et $(y_n)$ sont des suites d'éléments de l'intervalle compact $[a,b]$.
Puisque $[a,b]$ est compact, par le théorème de Bolzano-Weierstrass, il existe une sous-suite $(x_{n_k})$ de $(x_n)$ qui converge vers un point $x^* \in [a,b]$.

Maintenant, considérons la sous-suite $(y_{n_k})$.
Nous avons $|y_{n_k} - x^*| = |y_{n_k} - x_{n_k} + x_{n_k} - x^*| \le |y_{n_k} - x_{n_k}| + |x_{n_k} - x^*|$.
Puisque $|y_{n_k} - x_{n_k}| < 1/n_k$ et $n_k \to \infty$ (donc $1/n_k \to 0$), et $x_{n_k} \to x^*$, nous avons $\lim_{k \to \infty} |y_{n_k} - x^*| = 0 + 0 = 0$.
Donc, la sous-suite $(y_{n_k})$ converge également vers $x^*$.

Puisque $f$ est continue sur $[a,b]$, elle est continue en $x^*$. Par la continuité séquentielle (Théorème 3.1) :
$\lim_{k \to \infty} f(x_{n_k}) = f(x^*)$
$\lim_{k \to \infty} f(y_{n_k}) = f(x^*)$

Par conséquent, $\lim_{k \to \infty} (f(x_{n_k}) - f(y_{n_k})) = f(x^*) - f(x^*) = 0$.
Ceci implique que pour tout $\epsilon' > 0$, il existe $K \in \mathbb{N}$ tel que pour tout $k \ge K$, $|f(x_{n_k}) - f(y_{n_k})| < \epsilon'$.

Cependant, par construction de nos suites, nous avons $|f(x_{n_k}) - f(y_{n_k})| \ge \epsilon_0$ pour tout $k$.
Ceci est une contradiction. La limite de termes supérieurs ou égaux à $\epsilon_0$ ne peut pas être 0 (sauf si $\epsilon_0=0$, ce qui n'est pas le cas).
Notre supposition initiale que $f$ n'est pas uniformément continue doit être fausse.
Donc, $f$ est uniformément continue sur $[a,b]$.

**Théorème 3.6 (Théorème des bornes atteintes / Extreme Value Theorem):**
Toute fonction continue sur un intervalle fermé et borné $[a,b]$ atteint ses bornes, c'est-à-dire qu'il existe $c_1, c_2 \in [a,b]$ tels que $f(c_1) = \min_{x \in [a,b]} f(x)$ et $f(c_2) = \max_{x \in [a,b]} f(x)$.

**Démonstration:**
Considérons l'ensemble image $f([a,b]) = \{f(x) \mid x \in [a,b]\}$.
Nous allons montrer que $f([a,b])$ est un ensemble compact dans $\mathbb{R}$.
Puisque $[a,b]$ est un ensemble compact et $f$ est continue, l'image continue d'un compact est un compact.
Un ensemble compact dans $\mathbb{R}$ est un ensemble fermé et borné (Théorème de Heine-Borel).
Puisque $f([a,b])$ est borné, il possède un supremum $M = \sup_{x \in [a,b]} f(x)$ et un infimum $m = \inf_{x \in [a,b]} f(x)$.
Puisque $f([a,b])$ est fermé, il contient ses points d'accumulation, et en particulier ses bornes supérieure et inférieure.
Donc, $M \in f([a,b])$ et $m \in f([a,b])$.
Par définition de l'image, cela signifie qu'il existe $c_1 \in [a,b]$ tel que $f(c_1) = m$ et il existe $c_2 \in [a,b]$ tel que $f(c_2) = M$.
Ainsi, $f$ atteint son minimum et son maximum sur $[a,b]$.

#### E. Compacité locale de $\mathbb{R}$

Comme mentionné précédemment, $\mathbb{R}$ est localement compact.
**Démonstration:**
Soit $x \in \mathbb{R}$. Nous devons montrer qu'il existe un voisinage $V$ de $x$ tel que $V$ est compact.
Considérons l'intervalle fermé $[x-1, x+1]$.
1.  **Voisinage:** L'intervalle $(x-1, x+1)$ est un ensemble ouvert contenant $x$. Puisque $(x-1, x+1) \subset [x-1, x+1]$, l'intervalle $[x-1, x+1]$ est un voisinage de $x$.
2.  **Compacité:** L'intervalle $[x-1, x+1]$ est un sous-ensemble de $\mathbb{R}$ qui est fermé (par définition d'un intervalle fermé) et borné (il est contenu dans $[-M, M]$ pour $M = \max(|x-1|, |x+1|)$).
    D'après le théorème de Heine-Borel, un sous-ensemble de $\mathbb{R}$ est compact si et seulement s'il est fermé et borné.
    Par conséquent, $[x-1, x+1]$ est un voisinage compact de $x$.
Puisque ceci est vrai pour tout $x \in \mathbb{R}$, l'espace $\mathbb{R}$ est localement compact.

### 4. Exercices d'Application

**Exercice 1:**
Montrer que la fonction $f(x) = x^3$ est continue sur $\mathbb{R}$ en utilisant la définition $\epsilon-\delta$.

**Solution:**
Soit $x_0 \in \mathbb{R}$ et $\epsilon > 0$. Nous cherchons $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|x^3 - x_0^3| < \epsilon$.
Nous avons $|x^3 - x_0^3| = |(x - x_0)(x^2 + x x_0 + x_0^2)| = |x - x_0| |x^2 + x x_0 + x_0^2|$.
Imposons $\delta \le 1$. Si $|x - x_0| < \delta \le 1$, alors $x_0 - 1 < x < x_0 + 1$.
Alors $|x| \le |x_0| + 1$.
Donc, $|x^2 + x x_0 + x_0^2| \le |x|^2 + |x||x_0| + |x_0|^2 \le (|x_0| + 1)^2 + (|x_0| + 1)|x_0| + |x_0|^2$.
Soit $M = (|x_0| + 1)^2 + (|x_0| + 1)|x_0| + |x_0|^2$. $M$ est une constante positive qui dépend de $x_0$.
Alors $|x^3 - x_0^3| < \delta M$.
Pour que $\delta M < \epsilon$, nous choisissons $\delta = \min\left(1, \frac{\epsilon}{M}\right)$.
Avec ce choix de $\delta$, si $|x - x_0| < \delta$, alors $|x^3 - x_0^3| < \delta M \le \frac{\epsilon}{M} M = \epsilon$.
Donc, $f(x) = x^3$ est continue sur $\mathbb{R}$.

**Exercice 2:**
Soit $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = \sin(1/x)$ pour $x \ne 0$ et $f(0) = 0$. Montrer que $f$ n'est pas continue en $x=0$.

**Solution:**
Nous allons utiliser la définition séquentielle de la continuité.
Pour que $f$ soit continue en $x=0$, il faudrait que pour toute suite $(x_n)$ convergeant vers $0$, la suite $(f(x_n))$ converge vers $f(0)=0$.
Considérons la suite $x_n = \frac{1}{n\pi + \pi/2}$ pour $n \in \mathbb{N}$.
Alors $x_n \to 0$ lorsque $n \to \infty$.
Calculons $f(x_n) = \sin\left(\frac{1}{1/(n\pi + \pi/2)}\right) = \sin(n\pi + \pi/2)$.
Pour $n$ pair, $n=2k$, $f(x_{2k}) = \sin(2k\pi + \pi/2) = \sin(\pi/2) = 1$.
Pour $n$ impair, $n=2k+1$, $f(x_{2k+1}) = \sin((2k+1)\pi + \pi/2) = \sin(\pi + \pi/2) = -1$.
La suite $(f(x_n))$ alterne entre $1$ et $-1$. Elle ne converge pas vers $0$.
Puisque nous avons trouvé une suite $(x_n)$ convergeant vers $0$ telle que $(f(x_n))$ ne converge pas vers $f(0)$, la fonction $f$ n'est pas continue en $x=0$.

**Exercice 3:**
Soit $f: [0,1] \to [0,1]$ une fonction continue. Montrer qu'il existe un point fixe $c \in [0,1]$ tel que $f(c) = c$. (Application du TVI).

**Solution:**
Considérons la fonction auxiliaire $g: [0,1] \to \mathbb{R}$ définie par $g(x) = f(x) - x$.
Puisque $f$ est continue sur $[0,1]$ et la fonction $h(x) = x$ est continue sur $[0,1]$, leur différence $g(x)$ est continue sur $[0,1]$.
Calculons les valeurs de $g$ aux bornes de l'intervalle :
$g(0) = f(0) - 0 = f(0)$. Puisque $f: [0,1] \to [0,1]$, nous avons $f(0) \ge 0$. Donc $g(0) \ge 0$.
$g(1) = f(1) - 1$. Puisque $f: [0,1] \to [0,1]$, nous avons $f(1) \le 1$. Donc $g(1) \le 0$.

Nous avons deux cas :
1.  Si $g(0) = 0$ ou $g(1) = 0$, alors $f(0) = 0$ ou $f(1) = 1$. Dans ce cas, $0$ ou $1$ est un point fixe, et le théorème est prouvé.
2.  Si $g(0) > 0$ et $g(1) < 0$. Alors $g(1) < 0 < g(0)$.
    Puisque $g$ est continue sur $[0,1]$ et $0$ est une valeur entre $g(1)$ et $g(0)$, par le Théorème des Valeurs Intermédiaires (Théorème 3.4), il existe un $c \in [0,1]$ tel que $g(c) = 0$.
    Par définition de $g$, $f(c) - c = 0$, ce qui signifie $f(c) = c$.
Dans tous les cas, il existe un point fixe $c \in [0,1]$ tel que $f(c) = c$.

**Exercice 4:**
La fonction $f(x) = x^2$ est-elle uniformément continue sur $\mathbb{R}$ ? Sur $[0,M]$ pour $M>0$ ?

**Solution:**
1.  **Sur $\mathbb{R}$:**
    Non, $f(x) = x^2$ n'est pas uniformément continue sur $\mathbb{R}$. La démonstration a été faite dans la section 2.D. (Cas Pathologiques et Contre-exemples). En résumé, pour $\epsilon_0=1$, on peut trouver $x_n = 1/\delta$ et $y_n = 1/\delta + \delta/2$ tels que $|x_n - y_n| < \delta$ mais $|f(x_n) - f(y_n)| \ge 1$.

2.  **Sur $[0,M]$ pour $M>0$ :**
    Oui, $f(x) = x^2$ est uniformément continue sur $[0,M]$.
    L'intervalle $[0,M]$ est un intervalle fermé et borné, donc un compact de $\mathbb{R}$.
    La fonction $f(x) = x^2$ est continue sur $\mathbb{R}$ (comme montré en 2.C), donc elle est continue sur le sous-intervalle $[0,M]$.
    D'après le Théorème de Heine-Cantor (Théorème 3.5), toute fonction continue sur un compact est uniformément continue sur ce compact.
    Par conséquent, $f(x) = x^2$ est uniformément continue sur $[0,M]$.

**Exercice 5:**
Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction continue telle que $\lim_{x \to -\infty} f(x) = L_1$ et $\lim_{x \to +\infty} f(x) = L_2$.
1.  Montrer que $f$ est bornée.
2.  Si $L_1 \ne L_2$, montrer que $f$ prend toutes les valeurs entre $L_1$ et $L_2$.

**Solution:**
1.  **$f$ est bornée :**
    Puisque $\lim_{x \to -\infty} f(x) = L_1$, pour $\epsilon = 1$, il existe $A < 0$ tel que pour tout $x < A$, $|f(x) - L_1| < 1$.
    Ceci implique $L_1 - 1 < f(x) < L_1 + 1$ pour $x < A$. Donc $f$ est bornée sur $(-\infty, A)$.
    Puisque $\lim_{x \to +\infty} f(x) = L_2$, pour $\epsilon = 1$, il existe $B > 0$ tel que pour tout $x > B$, $|f(x) - L_2| < 1$.
    Ceci implique $L_2 - 1 < f(x) < L_2 + 1$ pour $x > B$. Donc $f$ est bornée sur $(B, +\infty)$.
    Considérons l'intervalle $[A,B]$. Puisque $f$ est continue sur $\mathbb{R}$, elle est continue sur l'intervalle fermé et borné $[A,B]$.
    D'après le Théorème des bornes atteintes (Théorème 3.6), $f$ est bornée sur $[A,B]$.
    Soit $M_A = \sup_{x \in (-\infty, A)} f(x)$, $m_A = \inf_{x \in (-\infty, A)} f(x)$.
    Soit $M_B = \sup_{x \in (B, +\infty)} f(x)$, $m_B = \inf_{x \in (B, +\infty)} f(x)$.
    Soit $M_{[A,B]} = \max_{x \in [A,B]} f(x)$, $m_{[A,B]} = \min_{x \in [A,B]} f(x)$.
    Alors $f$ est bornée sur $\mathbb{R}$ par $\max(L_1+1, L_2+1, M_{[A,B]})$ et $\min(L_1-1, L_2-1, m_{[A,B]})$.
    Donc $f$ est bornée sur $\mathbb{R}$.

2.  **Si $L_1 \ne L_2$, $f$ prend toutes les valeurs entre $L_1$ et $L_2$ :**
    Sans perte de généralité, supposons $L_1 < L_2$.
    Soit $y$ une valeur telle que $L_1 < y < L_2$.
    Puisque $\lim_{x \to -\infty} f(x) = L_1$, et $y > L_1$, il existe $A < 0$ tel que pour tout $x < A$, $f(x) < y$. (En prenant $\epsilon = y - L_1 > 0$, il existe $A$ tel que pour $x<A$, $f(x) < L_1 + (y-L_1) = y$).
    Puisque $\lim_{x \to +\infty} f(x) = L_2$, et $y < L_2$, il existe $B > 0$ tel que pour tout $x > B$, $f(x) > y$. (En prenant $\epsilon = L_2 - y > 0$, il existe $B$ tel que pour $x>B$, $f(x) > L_2 - (L_2-y) = y$).
    Maintenant, considérons l'intervalle $[A,B]$. La fonction $f$ est continue sur $[A,B]$.
    Nous avons $f(A) < y$ et $f(B) > y$.
    Par le Théorème des Valeurs Intermédiaires (Théorème 3.4), il existe un $c \in [A,B]$ tel que $f(c) = y$.
    Donc, $f$ prend toutes les valeurs entre $L_1$ et $L_2$.

### 5. Application en Intelligence Artificielle

La continuité est une propriété fondamentale qui sous-tend de nombreux aspects théoriques et pratiques de l'Intelligence Artificielle, en particulier dans le domaine de l'apprentissage automatique et des réseaux de neurones.

1.  **Fonctions d'activation :** Les fonctions d'activation dans les réseaux de neurones (Sigmoid, Tanh, ReLU, Leaky ReLU, ELU, etc.) sont des exemples primordiaux de fonctions dont la continuité est cruciale.
    *   **Sigmoid et Tanh :** Ces fonctions sont continues et différentiables partout. Leur continuité assure que de petites variations dans l'entrée d'un neurone entraînent de petites variations dans sa sortie, ce qui est essentiel pour la stabilité de l'apprentissage. Leur différentiabilité permet l'application directe des algorithmes de descente de gradient (rétropropagation).
    *   **ReLU (Rectified Linear Unit) :** $f(x) = \max(0, x)$. La fonction ReLU est continue sur $\mathbb{R}$. Cependant, elle n'est pas différentiable en $x=0$. Pour l'optimisation, on utilise le concept de sous-gradient en $x=0$, ou on ignore simplement le point de non-différentiabilité, car il s'agit d'un ensemble de mesure nulle. Sa continuité garantit que le comportement de la fonction ne "saute" pas brusquement, ce qui serait problématique pour la convergence des algorithmes.

2.  **Fonctions de perte (Loss Functions) :** Les fonctions de perte (par exemple, l'erreur quadratique moyenne (MSE) pour la régression, l'entropie croisée pour la classification) mesurent l'écart entre les prédictions du modèle et les vraies valeurs. La continuité de ces fonctions est une exigence quasi universelle pour les algorithmes d'optimisation basés sur le gradient.
    *   Si une fonction de perte n'était pas continue, de très petites modifications des paramètres du modèle pourraient entraîner des changements arbitrairement grands dans la perte, rendant la recherche d'un minimum difficile, voire impossible, pour des méthodes comme la descente de gradient. La continuité assure que le paysage de la perte est "lisse" à une échelle locale, permettant aux algorithmes de se déplacer progressivement vers des minima.

3.  **Algorithmes d'optimisation :** La plupart des algorithmes d'optimisation en apprentissage automatique (descente de gradient, Adam, RMSprop, etc.) reposent sur le calcul de gradients ou de sous-gradients. Ces calculs présupposent la continuité (et souvent la différentiabilité) de la fonction objectif (la fonction de perte). La continuité garantit que la direction du gradient est une indication fiable de la direction de la plus forte augmentation (ou diminution) locale de la fonction.

4.  **Robustesse et stabilité des modèles :** Un modèle d'IA est considéré comme robuste si de petites perturbations de ses entrées n'entraînent pas de changements drastiques dans ses sorties. Cette propriété est directement liée à la continuité des fonctions qui composent le modèle. Si un modèle est une fonction continue, alors pour un $\epsilon$ donné (tolérance sur la sortie), il existe un $\delta$ (tolérance sur l'entrée) tel que toute entrée dans la boule de rayon $\delta$ autour d'une entrée donnée produira une sortie dans la boule de rayon $\epsilon$ autour de la sortie correspondante. Les attaques adversariales, qui visent à tromper les modèles en introduisant de minuscules perturbations imperceptibles, exploitent souvent les régions où la fonction du modèle est "moins continue" ou a une constante de Lipschitz élevée.

5.  **Théorème d'approximation universelle :** Ce théorème fondamental en théorie des réseaux de neurones stipule qu'un réseau de neurones à une seule couche cachée avec un nombre suffisant de neurones et une fonction d'activation continue, non constante et bornée (comme la sigmoïde ou la tanh) peut approximer n'importe quelle fonction continue sur un sous-ensemble compact de $\mathbb{R}^n$ avec une précision arbitraire. La continuité de la fonction à approximer et de la fonction d'activation est une condition essentielle pour ce théorème, soulignant le rôle central de la continuité dans la capacité d'apprentissage des réseaux de neurones.

### 6. Liens Sémantiques

La continuité est un concept fondamental qui tisse des liens profonds avec de nombreuses autres branches des mathématiques, servant de pont entre l'analyse classique et des domaines plus abstraits.

1.  **Topologie Générale :** La définition $\epsilon-\delta$ de la continuité est une spécification pour les espaces métriques. En topologie générale, la continuité est définie de manière plus abstraite : une fonction $f: X \to Y$ entre deux espaces topologiques est continue si l'image réciproque de tout ensemble ouvert de $Y$ est un ensemble ouvert de $X$. Pour les espaces métriques, cette définition est équivalente à la définition $\epsilon-\delta$. La continuité est donc une propriété topologique, préservant la "proximité" des points.

2.  **Différentiabilité :** La différentiabilité est une condition plus forte que la continuité. Toute fonction différentiable en un point est continue en ce point, mais la réciproque est fausse (par exemple, la fonction valeur absolue $f(x) = |x|$ est continue en $0$ mais non différentiable en $0$; la fonction de Weierstrass est continue partout mais nulle part différentiable). La différentiabilité implique une "lisséité" locale, permettant une approximation linéaire de la fonction.

3.  **Intégration (Riemann et Lebesgue) :** Les fonctions continues sur un intervalle fermé et borné sont toujours Riemann-intégrables. La continuité uniforme joue un rôle crucial dans la démonstration de l'intégrabilité de Riemann. Pour l'intégrale de Lebesgue, la notion de fonction mesurable est une généralisation de la continuité, mais toutes les fonctions continues sont mesurables.

4.  **Séries de Fonctions et Convergence :** La continuité est étroitement liée à la convergence des suites et séries de fonctions. Le théorème de la limite uniforme stipule que si une suite de fonctions continues $(f_n)$ converge uniformément vers une fonction $f$ sur un ensemble, alors $f$ est également continue sur cet ensemble. Ce n'est pas le cas pour la convergence simple (ponctuelle), comme le montrent les séries de Fourier qui peuvent converger vers des fonctions discontinues.

5.  **Analyse Fonctionnelle :** Dans les espaces vectoriels normés, la continuité des opérateurs linéaires est un concept central. Un opérateur linéaire entre deux espaces normés est continu si et seulement s'il est borné. Cette équivalence est fondamentale pour l'étude des opérateurs et des fonctionnelles linéaires.

6.  **Théorie de la Mesure :** Les fonctions continues sont des exemples prototypiques de fonctions mesurables. La mesurabilité est une propriété plus faible que la continuité mais essentielle pour définir l'intégrale de Lebesgue et pour travailler avec des espaces de fonctions plus généraux.

7.  **Compacité :** La compacité est une propriété topologique qui généralise la notion d'intervalle fermé et borné dans $\mathbb{R}$. Le théorème de Heine-Cantor et le théorème des bornes atteintes (Théorème 3.5 et 3.6) illustrent le lien profond entre continuité et compacité : les fonctions continues "préservent" la compacité (l'image continue d'un compact est un compact) et acquièrent des propriétés supplémentaires (uniforme continuité, existence d'extrema) sur des domaines compacts. La compacité locale de $\mathbb{R}$ est une propriété intrinsèque de l'espace qui permet à de nombreux résultats locaux de s'étendre.