---
uuid: "jalon-38"
title: "Théorème fondamental de l'analyse"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/calcul-differentiel
prev: "[[Jalon-37.md]]"
next: "[[Jalon 39 (Intégrales généralisées sur un intervalle quelconque et critères de convergence.).md]]"
---

# Jalon 38 : Théorème fondamental de l'analyse

## 1. L'Échafaudage Cognitif & Traçabilité Historique

**Genèse et Motivation :**
La genèse du Théorème Fondamental de l'Analyse trouve ses racines dans l'une des quêtes les plus profondes de l'histoire des mathématiques : relier deux problèmes géométriques apparemment distincts. D'une part, le problème de la quadrature, c'est-à-dire le calcul de l'aire délimitée par une courbe, étudié depuis l'Antiquité par Archimède et Eudoxe via la méthode d'exhaustion. D'autre part, le problème des tangentes, visant à déterminer la pente d'une courbe en un point donné, exploré par Fermat, Descartes, et Barrow.

Avant le XVIIe siècle, ces deux champs d'étude progressaient de manière parallèle, sans que leur interdépendance intime ne soit perçue. Isaac Newton et Gottfried Wilhelm Leibniz, travaillant de manière indépendante, ont opéré une révolution conceptuelle majeure en réalisant que la dérivation (le calcul des taux de variation instantanés) et l'intégration (le calcul des accumulations continues) sont deux opérations réciproques. Leurs travaux, unifiant le calcul différentiel et intégral, ont donné naissance au calcul infinitésimal.

Le génie de ce théorème réside dans sa capacité à transformer un problème d'intégration ardu, défini par une limite de sommes de Riemann infinies, en une simple évaluation algébrique aux bornes, pour peu que l'on connaisse une primitive de la fonction. Cette unification n'est pas qu'une simple astuce de calcul ; elle traduit une profonde symétrie de la nature continue, liant indissolublement les variations locales aux propriétés globales. Augustin-Louis Cauchy et Bernhard Riemann viendront plus tard formaliser cette intuition avec une rigueur absolue, en définissant l'intégrale indépendamment de la notion de primitive, permettant ainsi au Théorème Fondamental de s'exprimer dans toute sa puissance sur des bases logiques irréprochables.

## 2. Le Protocole d'Exégèse Conceptuelle

### A. Primitives d'une Fonction

**A. Énoncé Symbolique Strict :**
Soit $I$ un intervalle de $\mathbb{R}$ non réduit à un point. Soit $f : I \to \mathbb{R}$ une fonction.
On dit qu'une fonction $F : I \to \mathbb{R}$ est une primitive de $f$ sur $I$ si et seulement si $F$ est dérivable sur $I$ et si, pour tout $x \in I$, on a :
$$ F'(x) = f(x) $$

**B. Anatomie et Typage Chirurgical :**
- $I$ désigne un intervalle réel arbitraire.
- $f$ est la fonction dont on cherche la primitive. Elle n'est soumise, a priori, à aucune condition de régularité pour cette définition, bien que l'existence d'une primitive en requière (comme la continuité).
- $F$ est la primitive candidate. L'exigence de dérivabilité sur l'ensemble de $I$ est inhérente à la définition.
- L'égalité $F'(x) = f(x)$ est universellement quantifiée sur l'intervalle $I$.

**C. Exemples de Validation :**
- *Exemple trivial :* La fonction $f : x \mapsto 2x$ définie sur $\mathbb{R}$ admet pour primitive la fonction $F : x \mapsto x^2$ sur $\mathbb{R}$, car la dérivée de $x \mapsto x^2$ est $x \mapsto 2x$ pour tout $x \in \mathbb{R}$.
- *Exemple complexe :* La fonction $f : \mathbb{R} \to \mathbb{R}$ définie par $f(x) = x \cos(x^2)$ admet pour primitive $F(x) = \frac{1}{2} \sin(x^2)$. En effet, par la règle de composition des dérivées, pour tout $x \in \mathbb{R}$, $F'(x) = \frac{1}{2} \cdot 2x \cdot \cos(x^2) = x \cos(x^2) = f(x)$.

**D. Cas Pathologiques et Contre-exemples :**
Toute fonction n'admet pas nécessairement de primitive. Par le théorème de Darboux, la fonction dérivée d'une fonction dérivable sur un intervalle satisfait obligatoirement la propriété des valeurs intermédiaires. Par conséquent, la fonction $f : \mathbb{R} \to \mathbb{R}$ définie par $f(x) = 1$ si $x \ge 0$ et $f(x) = -1$ si $x < 0$ n'admet aucune primitive sur $\mathbb{R}$, car elle ne vérifie pas la propriété des valeurs intermédiaires (elle ne prend pas la valeur $0$ qui est comprise entre $-1$ et $1$).

### B. Le Théorème Fondamental de l'Analyse (Première Forme)

**A. Énoncé Symbolique Strict :**
Soit $f : I \to \mathbb{R}$ une fonction continue sur un intervalle $I$ de $\mathbb{R}$. Soit $a \in I$.
La fonction $\Phi : I \to \mathbb{R}$ définie pour tout $x \in I$ par :
$$ \Phi(x) = \int_a^x f(t) \, dt $$
est l'unique primitive de $f$ sur $I$ qui s'annule en $a$. En particulier, $\Phi$ est dérivable (et même de classe $\mathcal{C}^1$ sur $I$) et on a :
$$ \forall x \in I, \quad \Phi'(x) = f(x) $$

**B. Anatomie et Typage Chirurgical :**
- L'hypothèse fondamentale est la **continuité** de $f$ sur $I$. Elle garantit l'intégrabilité de $f$ sur tout segment inclus dans $I$, et donc la bonne définition de la fonction $\Phi$.
- $a$ est un point d'ancrage arbitrairement choisi dans l'intervalle $I$.
- $\Phi$ est une fonction intégralement définie, parfois appelée intégrale indéfinie.
- Le résultat établit non seulement l'existence d'une primitive pour toute fonction continue, mais fournit également sa construction explicite via l'intégrale de Riemann.
- La variable d'intégration $t$ est une variable muette, strictement confinée à l'intérieur du symbole intégral, tandis que la borne supérieure $x$ est la variable de la fonction $\Phi$.

**C. Exemples de Validation :**
- *Exemple trivial :* Soit $f(t) = 1$ sur $\mathbb{R}$. Fixons $a = 0$. $\Phi(x) = \int_0^x 1 \, dt = x$. On vérifie bien que $\Phi'(x) = 1 = f(x)$ et $\Phi(0) = 0$.
- *Exemple complexe :* Soit $f(t) = e^{-t^2}$. La fonction $\Phi(x) = \int_0^x e^{-t^2} \, dt$ (qui est proportionnelle à la fonction d'erreur $\text{erf}$) est une primitive de $t \mapsto e^{-t^2}$. Bien qu'elle ne s'exprime pas à l'aide des fonctions usuelles (fonctions élémentaires), le théorème garantit son existence, sa dérivabilité et affirme que $\Phi'(x) = e^{-x^2}$.

**D. Cas Pathologiques et Contre-exemples :**
La continuité de $f$ est cruciale. Si $f$ n'est pas continue, $\Phi$ peut exister (être bien définie) mais ne pas être dérivable en certains points. Considérons $f(t) = \text{sgn}(t)$ (le signe de $t$) sur $[-1, 1]$. On a $\Phi(x) = \int_0^x \text{sgn}(t) \, dt = |x|$. La fonction $\Phi$ est continue sur $[-1, 1]$, mais n'est pas dérivable en $x = 0$, et par suite, n'est pas une primitive de $f$ sur l'intervalle tout entier.

### C. Le Théorème Fondamental de l'Analyse (Seconde Forme)

**A. Énoncé Symbolique Strict :**
Soit $f : [a, b] \to \mathbb{R}$ une fonction continue. Si $F : [a, b] \to \mathbb{R}$ est une primitive quelconque de $f$ sur $[a, b]$, alors :
$$ \int_a^b f(t) \, dt = F(b) - F(a) $$
On utilise souvent la notation crochets : $[F(t)]_a^b = F(b) - F(a)$.

**B. Anatomie et Typage Chirurgical :**
- $f$ est une fonction continue sur le segment $[a, b]$.
- $F$ désigne n'importe quelle primitive de $f$.
- Le théorème stipule que le calcul d'une intégrale définie, processus analytique complexe reposant sur des limites de subdivisions, se réduit à l'évaluation algébrique d'une primitive aux bornes de l'intervalle.

**C. Exemples de Validation :**
- *Exemple trivial :* Calculons $\int_0^2 3x^2 \, dt$. Une primitive de $f(x) = 3x^2$ est $F(x) = x^3$. L'intégrale vaut $[x^3]_0^2 = 2^3 - 0^3 = 8$.
- *Exemple complexe :* Évaluons $\int_1^e \frac{\ln(x)}{x} \, dx$. En remarquant que $\frac{\ln(x)}{x} = \frac{1}{x} \ln(x)$, c'est de la forme $u'(x)u(x)$ avec $u(x) = \ln(x)$. Une primitive est $F(x) = \frac{1}{2}(\ln(x))^2$. Ainsi, l'intégrale vaut $\frac{1}{2}(\ln(e))^2 - \frac{1}{2}(\ln(1))^2 = \frac{1}{2} \cdot 1^2 - 0 = \frac{1}{2}$.

**D. Cas Pathologiques et Contre-exemples :**
L'application aveugle de ce théorème sans vérifier la continuité sur l'ensemble du segment d'intégration conduit à des absurdités. Considérons l'intégrale $\int_{-1}^1 \frac{1}{x^2} \, dx$. Si l'on choisit brutalement $F(x) = -\frac{1}{x}$, on obtiendrait $\left[-\frac{1}{x}\right]_{-1}^1 = -1 - (1) = -2$. Or la fonction $x \mapsto \frac{1}{x^2}$ est strictement positive, son aire sous la courbe ne peut être négative. L'erreur vient du fait que la fonction n'est pas continue, ni même définie en $0 \in [-1, 1]$. Le théorème ne s'applique pas.

### D. Techniques d'Intégration Fondamentales

#### 1. L'Intégration par Parties (IPP)

**A. Énoncé Symbolique Strict :**
Soient $u, v : [a, b] \to \mathbb{R}$ deux fonctions de classe $\mathcal{C}^1$ sur $[a, b]$. On a :
$$ \int_a^b u'(t) v(t) \, dt = [u(t)v(t)]_a^b - \int_a^b u(t) v'(t) \, dt $$

**B. Anatomie et Typage Chirurgical :**
- $u$ et $v$ sont dérivables sur $[a, b]$, et leurs dérivées $u'$ et $v'$ sont continues (hypothèse $\mathcal{C}^1$). Cette hypothèse assure que les fonctions intégrées $u'v$ et $uv'$ sont continues, et donc intégrables au sens de Riemann.
- La formule découle directement de la règle de dérivation du produit $(uv)' = u'v + uv'$ intégrée grâce au Théorème Fondamental.

#### 2. Le Changement de Variable

**A. Énoncé Symbolique Strict :**
Soit $\varphi : [\alpha, \beta] \to \mathbb{R}$ une fonction de classe $\mathcal{C}^1$. Soit $f : I \to \mathbb{R}$ une fonction continue sur un intervalle $I$ tel que $\varphi([\alpha, \beta]) \subset I$. Alors :
$$ \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x) \, dx = \int_\alpha^\beta f(\varphi(t)) \varphi'(t) \, dt $$

**B. Anatomie et Typage Chirurgical :**
- $\varphi$ est la fonction de changement de variable. Sa régularité $\mathcal{C}^1$ est requise. Contrairement à une idée reçue, il n'est **pas** nécessaire que $\varphi$ soit bijective pour appliquer la formule dans le sens direct.
- L'intervalle image $\varphi([\alpha, \beta])$ doit être strictement inclus dans le domaine de définition (et de continuité) de $f$.
- Cette formule traduit la règle de dérivation des fonctions composées $(F \circ \varphi)' = (F' \circ \varphi) \cdot \varphi'$ transposée au calcul intégral.

## 3. Zéro Ellipse dans les Démonstrations à Blanc

### Démonstration de l'unicité des primitives à une constante près
Soit un intervalle $I$ de $\mathbb{R}$. Soit $f : I \to \mathbb{R}$. Supposons que $F_1$ et $F_2$ soient deux primitives de $f$ sur $I$.
Nous allons démontrer qu'il existe une constante réelle $C$ telle que pour tout $x \in I$, $F_1(x) - F_2(x) = C$.

Posons $H : I \to \mathbb{R}$ définie par $H(x) = F_1(x) - F_2(x)$ pour tout $x \in I$.
Par hypothèse, $F_1$ et $F_2$ sont dérivables sur $I$. Par linéarité de la dérivation, $H$ est dérivable sur $I$.
Pour tout $x \in I$, nous avons $H'(x) = F_1'(x) - F_2'(x)$.
Or, $F_1$ et $F_2$ étant des primitives de $f$, on a $F_1'(x) = f(x)$ et $F_2'(x) = f(x)$.
Donc, pour tout $x \in I$, $H'(x) = f(x) - f(x) = 0$.

Soient $a$ et $b$ deux points quelconques de l'intervalle $I$, avec $a < b$.
La fonction $H$ est dérivable (donc continue) sur $[a, b]$, et dérivable sur $]a, b[$.
D'après le Théorème des Accroissements Finis appliqué à $H$ sur l'intervalle $[a, b]$, il existe un réel $c \in ]a, b[$ tel que :
$$ H(b) - H(a) = H'(c)(b - a) $$
Or, nous avons établi que la dérivée de $H$ est identiquement nulle sur $I$. Par conséquent, $H'(c) = 0$.
Ainsi, $H(b) - H(a) = 0 \cdot (b - a) = 0$, ce qui implique $H(b) = H(a)$.
Ceci étant valable pour tout couple $(a, b) \in I^2$, la fonction $H$ est constante sur $I$.
Il existe donc une constante $C \in \mathbb{R}$ telle que pour tout $x \in I$, $F_1(x) - F_2(x) = C$. $\blacksquare$

### Démonstration du Théorème Fondamental (Première Forme)
Soit $f$ une fonction continue sur un intervalle $I$. Soit $a \in I$. Soit $\Phi(x) = \int_a^x f(t) \, dt$.
Démontrons que $\Phi$ est dérivable sur $I$ et que pour tout $x \in I$, $\Phi'(x) = f(x)$.

Soit $x_0 \in I$. Montrons que $\Phi$ est dérivable en $x_0$.
Soit $h \in \mathbb{R}^*$ tel que $x_0 + h \in I$.
Étudions le taux d'accroissement de $\Phi$ en $x_0$ :
$$ \frac{\Phi(x_0+h) - \Phi(x_0)}{h} = \frac{1}{h} \left( \int_a^{x_0+h} f(t) \, dt - \int_a^{x_0} f(t) \, dt \right) $$
Par la relation de Chasles pour l'intégrale de Riemann, on a $\int_a^{x_0+h} f(t) \, dt = \int_a^{x_0} f(t) \, dt + \int_{x_0}^{x_0+h} f(t) \, dt$.
En soustrayant $\int_a^{x_0} f(t) \, dt$, on obtient :
$$ \Phi(x_0+h) - \Phi(x_0) = \int_{x_0}^{x_0+h} f(t) \, dt $$
Ce qui nous donne le taux d'accroissement :
$$ \frac{\Phi(x_0+h) - \Phi(x_0)}{h} = \frac{1}{h} \int_{x_0}^{x_0+h} f(t) \, dt $$
Pour démontrer que la limite de ce taux d'accroissement quand $h$ tend vers 0 est $f(x_0)$, nous allons évaluer la valeur absolue de la différence :
$$ D_h = \left| \frac{\Phi(x_0+h) - \Phi(x_0)}{h} - f(x_0) \right| $$
Remarquons que la constante $f(x_0)$ peut s'écrire sous forme intégrale : $f(x_0) = \frac{1}{h} \int_{x_0}^{x_0+h} f(x_0) \, dt$, puisque l'intégrale d'une constante sur un intervalle de longueur $h$ est égale au produit de cette constante par $h$.
Ainsi, en utilisant la linéarité de l'intégrale, on a :
$$ D_h = \left| \frac{1}{h} \int_{x_0}^{x_0+h} f(t) \, dt - \frac{1}{h} \int_{x_0}^{x_0+h} f(x_0) \, dt \right| = \left| \frac{1}{h} \int_{x_0}^{x_0+h} (f(t) - f(x_0)) \, dt \right| $$
Par l'inégalité triangulaire intégrale, $\left| \int_\alpha^\beta g(t) \, dt \right| \le \left| \int_\alpha^\beta |g(t)| \, dt \right|$ (en conservant l'ordre naturel des bornes si $h > 0$ et en inversant les bornes si $h < 0$, ce qui est absorbé par le $|h|$ au dénominateur) :
$$ D_h \le \frac{1}{|h|} \left| \int_{x_0}^{x_0+h} |f(t) - f(x_0)| \, dt \right| $$

Utilisons maintenant l'hypothèse de continuité de $f$ en $x_0$.
Soit $\epsilon > 0$. Il existe $\delta > 0$ tel que pour tout $t \in I$, $|t - x_0| \le \delta \implies |f(t) - f(x_0)| \le \epsilon$.
Supposons que $0 < |h| \le \delta$. Alors, pour tout $t$ compris entre $x_0$ et $x_0+h$, la distance $|t - x_0|$ est inférieure ou égale à $|h|$, donc $|t - x_0| \le \delta$.
Par conséquent, pour tout $t$ entre $x_0$ et $x_0+h$, on a l'inégalité $|f(t) - f(x_0)| \le \epsilon$.
En intégrant cette inégalité sur l'intervalle de bornes $x_0$ et $x_0+h$ (dont la longueur est $|h|$) :
$$ \left| \int_{x_0}^{x_0+h} |f(t) - f(x_0)| \, dt \right| \le \left| \int_{x_0}^{x_0+h} \epsilon \, dt \right| = \epsilon |h| $$
En réinjectant cette majoration dans l'inégalité pour $D_h$ :
$$ D_h \le \frac{1}{|h|} ( \epsilon |h| ) = \epsilon $$
Nous avons ainsi démontré : pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour tout $h$ vérifiant $0 < |h| \le \delta$, on a :
$$ \left| \frac{\Phi(x_0+h) - \Phi(x_0)}{h} - f(x_0) \right| \le \epsilon $$
Cela constitue précisément la définition formelle de la limite :
$$ \lim_{h \to 0} \frac{\Phi(x_0+h) - \Phi(x_0)}{h} = f(x_0) $$
La fonction $\Phi$ est donc dérivable en $x_0$, et sa dérivée en ce point est $f(x_0)$.
Ceci étant vrai pour tout $x_0 \in I$, on a bien $\forall x \in I, \Phi'(x) = f(x)$. $\Phi$ est bien une primitive de $f$.
Enfin, l'unicité découle du fait que si $\Phi_1$ est une autre primitive s'annulant en $a$, alors $\Phi - \Phi_1$ est une constante. Or $(\Phi - \Phi_1)(a) = 0 - 0 = 0$, donc la constante est nulle et $\Phi = \Phi_1$. $\blacksquare$

### Démonstration de l'Intégration Par Parties
Soient $u$ et $v$ deux fonctions de classe $\mathcal{C}^1$ sur le segment $[a, b]$.
La fonction produit $uv$ est dérivable sur $[a, b]$, et par la formule de Leibniz, sa dérivée est $(uv)' = u'v + uv'$.
Les fonctions $u', v, u, v'$ étant continues sur $[a, b]$, les fonctions $u'v$, $uv'$ et $(uv)'$ le sont également, et sont donc Riemann-intégrables sur $[a, b]$.
En intégrant cette égalité sur $[a, b]$ :
$$ \int_a^b (uv)'(t) \, dt = \int_a^b (u'(t)v(t) + u(t)v'(t)) \, dt $$
Par linéarité de l'intégrale de Riemann :
$$ \int_a^b (uv)'(t) \, dt = \int_a^b u'(t)v(t) \, dt + \int_a^b u(t)v'(t) \, dt $$
Or, par le second Théorème Fondamental de l'Analyse, comme la fonction $uv$ est une primitive de $(uv)'$ sur $[a, b]$, on a :
$$ \int_a^b (uv)'(t) \, dt = [u(t)v(t)]_a^b $$
En combinant les deux équations :
$$ [u(t)v(t)]_a^b = \int_a^b u'(t)v(t) \, dt + \int_a^b u(t)v'(t) \, dt $$
Ce qui, par un simple réarrangement algébrique (soustraction du second terme de l'intégrale des deux côtés), donne la formule recherchée :
$$ \int_a^b u'(t)v(t) \, dt = [u(t)v(t)]_a^b - \int_a^b u(t)v'(t) \, dt $$
$\blacksquare$
