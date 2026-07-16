---
titre: "Jalon 19 : Dérivabilité"
date: "2026-07-05"
statut: "Complet"
tags: ["analyse", "dérivabilité", "accroissements-finis", "rolle"]
---

# Jalon 19 : Dérivabilité, Théorème de Rolle et Accroissements Finis

## 1. Intuition et Genèse du Concept

La notion de dérivée émerge au carrefour de la cinématique (définir la vitesse instantanée d'un mobile) et de la géométrie (déterminer la tangente à une courbe en un point). Historiquement, Pierre de Fermat, puis Isaac Newton et Gottfried Wilhelm Leibniz, ont jeté les bases du calcul infinitésimal pour formaliser ces idées. Avant eux, la géométrie d'Euclide et d'Archimède permettait de tracer des tangentes à des cercles ou des paraboles, mais manquait d'un formalisme général.

L'intuition fondamentale de la dérivabilité est celle de l'approximation linéaire locale. Si l'on observe une courbe régulière (non fractale, sans point anguleux) au microscope en zoomant indéfiniment autour d'un point, celle-ci apparaît indiscernable d'une droite : sa tangente. La dérivée quantifie cette pente locale. C'est l'essence même du développement limité d'ordre 1 : exprimer une fonction complexe comme une fonction affine à l'ordre principal, perturbée par une erreur évanescente.

Ce changement de paradigme, consistant à passer du fini à l'infinitésimal, a nécessité des siècles de maturation pour être rendu rigoureux par Augustin-Louis Cauchy et Karl Weierstrass au XIXe siècle, à travers la formalisation des limites par la définition en $(\epsilon, \delta)$.

## 2. Formalisation et Structures Algébriques

### A. Énoncé Symbolique Strict (Définition de la dérivabilité)

Soit $I$ un intervalle de $\mathbb{R}$ d'intérieur non vide. Soit $f : I \to \mathbb{R}$ une application. Soit $a \in I$.
On dit que $f$ est dérivable en $a$ si la limite du taux d'accroissement de $f$ en $a$ existe et est finie. Formellement :
$$ \lim_{x \to a, x \neq a} \frac{f(x) - f(a)}{x - a} = \ell \in \mathbb{R} $$
Si cette limite existe, elle est notée $f'(a)$ et est appelée le nombre dérivé de $f$ en $a$.

De manière équivalente, par le changement de variable $h = x - a$, $f$ est dérivable en $a$ si et seulement si :
$$ \lim_{h \to 0, h \neq 0} \frac{f(a+h) - f(a)}{h} = f'(a) \in \mathbb{R} $$

**Développement Limité d'Ordre 1 (DL1) :**
La fonction $f$ est dérivable en $a$ si et seulement s'il existe un scalaire $L \in \mathbb{R}$ et une fonction $\epsilon : I \to \mathbb{R}$ tels que pour tout $x \in I$ :
$$ f(x) = f(a) + L(x - a) + (x - a)\epsilon(x) $$
avec $\lim_{x \to a} \epsilon(x) = 0$. Dans ce cas, $L = f'(a)$.

### B. Anatomie et Typage Chirurgical

- $I \subset \mathbb{R}$ : Un intervalle de la droite réelle. C'est la topologie usuelle induite par la valeur absolue qui est utilisée. Il garantit que le point $a$ n'est pas isolé.
- $f : I \to \mathbb{R}$ : L'application étudiée. L'espace d'arrivée est $\mathbb{R}$ muni de sa structure de corps complet.
- $a \in I$ : Le point d'évaluation. L'analyse est purement locale.
- $\tau_a(x) = \frac{f(x) - f(a)}{x - a}$ : Le taux d'accroissement, application définie sur $I \setminus \{a\}$.
- $f'(a) \in \mathbb{R}$ : Le scalaire réel représentant le coefficient directeur de l'approximation linéaire.
- $(x - a)\epsilon(x)$ : Le terme de reste (négligeable devant $x-a$, noté usuellement $o(x-a)$) qui mesure l'écart entre la fonction et son approximation affine.

### C. Exemples de Validation

**Exemple d'application trivial : La fonction affine**
Soit $f(x) = \alpha x + \beta$, avec $\alpha, \beta \in \mathbb{R}$.
Pour tout $a \in \mathbb{R}$ et $x \neq a$ :
$$ \frac{f(x) - f(a)}{x - a} = \frac{(\alpha x + \beta) - (\alpha a + \beta)}{x - a} = \frac{\alpha(x - a)}{x - a} = \alpha $$
La limite de ce rapport constant lorsque $x \to a$ est trivialement $\alpha$. Donc $f'(a) = \alpha$.

**Exemple de validation complexe : La fonction puissance**
Soit $f(x) = x^n$, avec $n \in \mathbb{N}^*$. Pour tout $a \in \mathbb{R}$ et $x \neq a$ :
$$ \frac{x^n - a^n}{x - a} = \frac{(x-a)\sum_{k=0}^{n-1} x^k a^{n-1-k}}{x-a} = \sum_{k=0}^{n-1} x^k a^{n-1-k} $$
Par continuité des fonctions polynomiales, la limite lorsque $x \to a$ du membre de droite s'obtient par substitution :
$$ \lim_{x \to a} \sum_{k=0}^{n-1} x^k a^{n-1-k} = \sum_{k=0}^{n-1} a^k a^{n-1-k} = \sum_{k=0}^{n-1} a^{n-1} = n a^{n-1} $$

### D. Cas Pathologiques et Contre-exemples

- **Point anguleux (Fonction valeur absolue) :** Soit $f(x) = |x|$. En $x = 0$, la limite du taux d'accroissement à droite est $\lim_{x \to 0^+} \frac{x - 0}{x} = 1$, tandis qu'à gauche elle est $\lim_{x \to 0^-} \frac{-x - 0}{x} = -1$. Les limites latérales diffèrent, donc la limite globale n'existe pas. $f$ n'est pas dérivable en $0$.
- **Tangente verticale (Fonction racine carrée) :** Soit $f(x) = \sqrt{x}$ définie sur $\mathbb{R}^+$. En $x = 0$, le taux d'accroissement $\frac{\sqrt{x} - 0}{x} = \frac{1}{\sqrt{x}}$ tend vers $+\infty$ lorsque $x \to 0^+$. La limite n'est pas finie, la fonction n'est pas dérivable en $0$.
- **Rupture complète (Fonction de Weierstrass) :** Il existe des fonctions continues sur tout $\mathbb{R}$ mais dérivables en aucun point, telles que $f(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x)$ avec $0 < a < 1$, $b$ entier impair et $ab > 1 + \frac{3}{2}\pi$.

## 3. Démonstrations Pas-à-Pas (Zéro Ellipse)

### Lemme Fondamental : Continuité induite
**Énoncé :** Si $f : I \to \mathbb{R}$ est dérivable en $a \in I$, alors $f$ est continue en $a$.

**Démonstration Exhaustive :**
1. Soit $f : I \to \mathbb{R}$ dérivable en $a \in I$.
2. Par définition de la dérivabilité, le réel $L = f'(a)$ existe et $\lim_{x \to a, x \neq a} \frac{f(x) - f(a)}{x - a} = L$.
3. Isolons $f(x)$. Pour tout $x \in I \setminus \{a\}$, nous pouvons écrire algébriquement :
   $$ f(x) = f(a) + \left( \frac{f(x) - f(a)}{x - a} \right) \cdot (x - a) $$
4. Considérons la limite de cette expression lorsque $x$ tend vers $a$.
5. Par les théorèmes d'opérations algébriques sur les limites (somme et produit), puisque la limite de chaque terme existe et est finie :
   $$ \lim_{x \to a} f(x) = \lim_{x \to a} f(a) + \left( \lim_{x \to a} \frac{f(x) - f(a)}{x - a} \right) \cdot \left( \lim_{x \to a} (x - a) \right) $$
6. En évaluant ces limites individuelles :
   $$ \lim_{x \to a} f(x) = f(a) + L \cdot 0 = f(a) $$
7. L'égalité $\lim_{x \to a} f(x) = f(a)$ constitue précisément l'axiome de continuité de la fonction $f$ au point $a$. La démonstration est achevée. $\blacksquare$

### Théorème de Rolle
**Énoncé :** Soient $a, b \in \mathbb{R}$ avec $a < b$. Soit $f : [a, b] \to \mathbb{R}$ une fonction telle que :
(i) $f$ est continue sur le segment fermé $[a, b]$,
(ii) $f$ est dérivable sur l'intervalle ouvert $]a, b[$,
(iii) $f(a) = f(b)$.
Alors, il existe au moins un point $c \in ]a, b[$ tel que $f'(c) = 0$.

**Démonstration Exhaustive :**
1. L'hypothèse (i) affirme que $f$ est continue sur le compact $[a, b]$. D'après le théorème des bornes atteintes (théorème de Weierstrass), l'image $f([a, b])$ est un segment fermé et borné. Par conséquent, $f$ admet un minimum global $m$ et un maximum global $M$ sur $[a, b]$, et ces extrema sont atteints. Il existe donc $x_m, x_M \in [a, b]$ tels que $f(x_m) = m$ et $f(x_M) = M$.
2. Discutons selon deux cas mutuellement exclusifs.
3. **Cas 1 :** Supposons que $m = M$. Dans ce cas, pour tout $x \in [a, b]$, $m \leq f(x) \leq M \implies f(x) = m$. La fonction $f$ est donc constante sur $[a, b]$. Sa dérivée est identiquement nulle sur $]a, b[$. Tout point $c \in ]a, b[$ satisfait $f'(c) = 0$. Le théorème est vérifié.
4. **Cas 2 :** Supposons que $m < M$. Par hypothèse (iii), $f(a) = f(b)$. Il est donc impossible que les deux extrema soient atteints uniquement aux bornes de l'intervalle (sinon on aurait $m = f(a) = f(b) = M$, contredisant $m < M$).
5. Par conséquent, au moins l'un des deux extrema, disons le maximum $M$, est atteint en un point $c \in ]a, b[$ strictement à l'intérieur de l'intervalle (c'est-à-dire $c = x_M \neq a$ et $c = x_M \neq b$).
6. Évaluons le comportement du taux d'accroissement de $f$ en ce point $c$. Puisque $c \in ]a, b[$, il existe un $\delta > 0$ tel que $]c-\delta, c+\delta[ \subset [a, b]$.
7. Par définition du maximum, pour tout $h$ tel que $c+h \in [a, b]$ (et en particulier pour $|h| < \delta$), on a $f(c+h) \leq f(c)$, ce qui implique $f(c+h) - f(c) \leq 0$.
8. Supposons $h > 0$. Alors le taux d'accroissement à droite vérifie :
   $$ \frac{f(c+h) - f(c)}{h} \leq 0 $$
   En passant à la limite quand $h \to 0^+$, la dérivée à droite $f'_d(c)$ vérifie $f'_d(c) \leq 0$.
9. Supposons $h < 0$. Alors le taux d'accroissement à gauche vérifie (puisque le dénominateur est négatif) :
   $$ \frac{f(c+h) - f(c)}{h} \geq 0 $$
   En passant à la limite quand $h \to 0^-$, la dérivée à gauche $f'_g(c)$ vérifie $f'_g(c) \geq 0$.
10. Par hypothèse (ii), $f$ est dérivable sur $]a, b[$. Puisque $c \in ]a, b[$, $f$ est dérivable au point $c$. Cela implique l'existence de la limite globale, et donc l'égalité des dérivées latérales : $f'(c) = f'_d(c) = f'_g(c)$.
11. Les inégalités $f'(c) \leq 0$ et $f'(c) \geq 0$ imposent inéluctablement $f'(c) = 0$. La démonstration est achevée. $\blacksquare$

### Théorème des Accroissements Finis (Égalité de Lagrange)
**Énoncé :** Soient $a, b \in \mathbb{R}$ avec $a < b$. Soit $f : [a, b] \to \mathbb{R}$ une fonction continue sur $[a, b]$ et dérivable sur $]a, b[$. Alors il existe un point $c \in ]a, b[$ tel que $f(b) - f(a) = f'(c)(b - a)$.

**Démonstration Exhaustive :**
1. L'objectif est d'appliquer le théorème de Rolle. Pour cela, nous construisons une fonction auxiliaire $\varphi$ mesurant l'écart entre la fonction $f$ et la corde reliant les points $(a, f(a))$ et $(b, f(b))$.
2. La droite sécante passant par ces deux points a pour équation $y(x) = f(a) + \frac{f(b) - f(a)}{b - a}(x - a)$.
3. Définissons la fonction $\varphi : [a, b] \to \mathbb{R}$ par :
   $$ \varphi(x) = f(x) - \left( f(a) + \frac{f(b) - f(a)}{b - a}(x - a) \right) $$
4. Vérifions scrupuleusement les trois hypothèses du théorème de Rolle pour $\varphi$ :
   - (i) $\varphi$ est continue sur $[a, b]$ en tant que somme de la fonction $f$ (continue par hypothèse) et d'un polynôme de degré 1 (continu sur $\mathbb{R}$).
   - (ii) $\varphi$ est dérivable sur $]a, b[$ en tant que somme de fonctions dérivables. Sa dérivée s'exprime par :
     $$ \forall x \in ]a, b[, \quad \varphi'(x) = f'(x) - \frac{f(b) - f(a)}{b - a} $$
   - (iii) Évaluons $\varphi$ aux bornes de l'intervalle :
     $$ \varphi(a) = f(a) - \left( f(a) + \frac{f(b) - f(a)}{b - a}(a - a) \right) = f(a) - f(a) = 0 $$
     $$ \varphi(b) = f(b) - \left( f(a) + \frac{f(b) - f(a)}{b - a}(b - a) \right) = f(b) - \left( f(a) + f(b) - f(a) \right) = 0 $$
     Ainsi, $\varphi(a) = \varphi(b) = 0$.
5. Les trois prémisses du théorème de Rolle étant satisfaites, il existe au moins un point $c \in ]a, b[$ tel que $\varphi'(c) = 0$.
6. Substituons cette condition dans l'expression de la dérivée de $\varphi$ :
   $$ \varphi'(c) = f'(c) - \frac{f(b) - f(a)}{b - a} = 0 $$
7. L'équivalence algébrique mène immédiatement à :
   $$ f'(c) = \frac{f(b) - f(a)}{b - a} \implies f(b) - f(a) = f'(c)(b - a) $$
   La démonstration est achevée. $\blacksquare$
