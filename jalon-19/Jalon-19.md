---
titre: "Jalon 19 : Dérivabilité"
date: "2026-07-05"
statut: "Complet"
tags: ["analyse", "dérivabilité", "accroissements-finis", "rolle"]
---

# Jalon 19 : Dérivabilité, Théorème de Rolle, Accroissements Finis et Prolongement de la Dérivée

## 1. Présentation du concept clé (Échafaudage Cognitif)

L'étude de la continuité nous a permis de comprendre comment une fonction "ne saute pas", mais elle ne nous dit rien sur la "vitesse" à laquelle elle évolue. La dérivabilité naît du besoin historique et physique de mesurer des taux de variation instantanés : la vitesse d'un mobile (Newton, Leibniz) ou la pente de la tangente à une courbe (Fermat, Descartes).

Historiquement, la notion de tangente était géométrique et intuitive. Fermat fut l'un des premiers à formaliser cette idée en considérant des accroissements infiniment petits. Cependant, ce n'est qu'avec Cauchy et Weierstrass que la notion de dérivée a reçu une définition rigoureuse fondée sur la théorie des limites, balayant les paradoxes liés aux "infiniment petits". La dérivabilité d'une fonction en un point signifie localement que la fonction peut être approximée de manière optimale par une fonction affine : c'est la naissance de l'analyse locale.

Cette approximation linéaire locale est le cœur battant de l'optimisation moderne, y compris dans la rétropropagation du gradient (backpropagation) en intelligence artificielle, où l'on cherche à minimiser une fonction de coût en suivant la direction de sa plus forte pente.

## 2. Formalisation (Protocole d'Exégèse Conceptuelle)

### A. Énoncé Symbolique Strict

**Définition (Dérivabilité en un point) :**
Soit $I$ un intervalle de $\mathbb{R}$ d'intérieur non vide. Soit $f : I \to \mathbb{R}$ une fonction et $a \in I$.
On dit que $f$ est dérivable en $a$ si la limite suivante existe dans $\mathbb{R}$ (c'est-à-dire si elle est finie) :
$$ \lim_{x \to a, x \neq a} \frac{f(x) - f(a)}{x - a} $$
ou, de manière équivalente en posant $x = a + h$ :
$$ \lim_{h \to 0, h \neq 0} \frac{f(a+h) - f(a)}{h} $$
Si cette limite existe, elle est notée $f'(a)$ et est appelée le nombre dérivé de $f$ en $a$.

**Développement limité d'ordre 1 (DL1) :**
$f$ est dérivable en $a$ si et seulement s'il existe un réel $L$ et une fonction $\epsilon : I \to \mathbb{R}$ tels que pour tout $x \in I$ :
$$ f(x) = f(a) + L(x - a) + (x - a)\epsilon(x) $$
avec $\lim_{x \to a} \epsilon(x) = 0$. Dans ce cas, $L = f'(a)$.

### B. Anatomie et Typage Chirurgical

- $I \subset \mathbb{R}$ : Un intervalle qui garantit que l'on peut s'approcher de $a$ par des points de l'ensemble de définition.
- $f : I \to \mathbb{R}$ : La fonction étudiée, à valeurs réelles.
- $a \in I$ : Le point où l'on étudie le comportement local. Si $a$ est une borne de l'intervalle $I$ (par exemple $I=[a, b[$), la limite est une limite à droite (dérivabilité à droite).
- Le rapport $\frac{f(x) - f(a)}{x - a}$ : Appelé taux d'accroissement de $f$ entre $a$ et $x$. Il représente la pente de la sécante passant par les points $(a, f(a))$ et $(x, f(x))$.
- $f'(a) \in \mathbb{R}$ : Le nombre dérivé. C'est un scalaire réel pur.
- $L(x - a)$ : La partie linéaire de l'accroissement.
- $(x - a)\epsilon(x)$ : Le reste, qui est négligeable devant $(x - a)$ au voisinage de $a$ (noté $o(x-a)$).

### C. Exemples de Validation

**Exemple trivial :** $f(x) = c$ (constante).
$\forall x \neq a, \frac{f(x) - f(a)}{x - a} = \frac{c - c}{x - a} = 0$. Donc $f'(a) = \lim_{x \to a} 0 = 0$.

**Exemple complexe :** $f(x) = x^n$ ($n \in \mathbb{N}^*$).
Le taux d'accroissement en $a$ est :
$$ \frac{x^n - a^n}{x - a} = \frac{(x-a)\sum_{k=0}^{n-1} x^k a^{n-1-k}}{x-a} = \sum_{k=0}^{n-1} x^k a^{n-1-k} $$
En passant à la limite quand $x \to a$, chaque terme $x^k a^{n-1-k}$ tend vers $a^k a^{n-1-k} = a^{n-1}$. Comme il y a $n$ termes, $\lim_{x \to a} \frac{x^n - a^n}{x - a} = n a^{n-1}$.

### D. Cas Pathologiques et Contre-exemples

- **La fonction valeur absolue $f(x) = |x|$ en $0$.**
  - Limite à droite ($x > 0$) : $\frac{|x| - |0|}{x - 0} = \frac{x}{x} = 1 \xrightarrow{x \to 0^+} 1$.
  - Limite à gauche ($x < 0$) : $\frac{|x| - |0|}{x - 0} = \frac{-x}{x} = -1 \xrightarrow{x \to 0^-} -1$.
  Les limites à droite et à gauche diffèrent. La fonction n'est pas dérivable en $0$ (point anguleux).
- **La fonction $f(x) = \sqrt{x}$ en $0$ sur $\mathbb{R}_+$.**
  $\frac{\sqrt{x} - 0}{x - 0} = \frac{1}{\sqrt{x}}$. La limite quand $x \to 0^+$ est $+\infty$. La limite n'est pas finie, la fonction n'est pas dérivable en 0 (tangente verticale).
- **La fonction de Weierstrass.** Il existe des fonctions continues partout sur $\mathbb{R}$ mais dérivables nulle part. (Contre-exemple historique détruisant l'intuition que "continu implique dérivable sauf en des points isolés").

## 3. Démonstrations (Zéro Ellipse)

### Théorème (Continuité implique par la dérivabilité)
Si $f$ est dérivable en $a$, alors $f$ est continue en $a$.

**Démonstration :**
1. Soit $f : I \to \mathbb{R}$ dérivable en $a \in I$.
2. Par définition, il existe $L = f'(a) \in \mathbb{R}$ tel que $\lim_{x \to a, x \neq a} \frac{f(x) - f(a)}{x - a} = L$.
3. Pour $x \in I \setminus \{a\}$, nous pouvons écrire :
   $$ f(x) - f(a) = \frac{f(x) - f(a)}{x - a} \cdot (x - a) $$
4. Calculons la limite de cette expression lorsque $x$ tend vers $a$ :
   $$ \lim_{x \to a} (f(x) - f(a)) = \left( \lim_{x \to a} \frac{f(x) - f(a)}{x - a} \right) \cdot \left( \lim_{x \to a} (x - a) \right) $$
5. Les deux limites du membre de droite existent et sont finies. Ainsi :
   $$ \lim_{x \to a} (f(x) - f(a)) = f'(a) \cdot 0 = 0 $$
6. On en déduit immédiatement que $\lim_{x \to a} f(x) = f(a)$.
7. Cette égalité est exactement la définition de la continuity de $f$ en $a$. $\blacksquare$

### Théorème de Rolle
Soient $a, b \in \mathbb{R}$ avec $a < b$. Soit $f : [a, b] \to \mathbb{R}$ une fonction vérifiant :
- $f$ est continue sur le segment $[a, b]$,
- $f$ est dérivable sur l'intervalle ouvert $]a, b[$,
- $f(a) = f(b)$.
Alors, il existe $c \in ]a, b[$ tel que $f'(c) = 0$.

**Démonstration :**
1. La fonction $f$ est continue sur le segment $[a, b]$. D'après le théorème des bornes atteintes (théorème de Weierstrass), $f$ est bornée et atteint ses bornes. Il existe donc $x_m, x_M \in [a, b]$ tels que $f(x_m) = \inf_{x \in [a, b]} f(x)$ et $f(x_M) = \sup_{x \in [a, b]} f(x)$.
2. **Premier cas :** Si $f(x_m) = f(x_M)$. Alors le minimum et le maximum de la fonction sont égaux. La fonction $f$ est donc constante sur $[a, b]$. Par conséquent, sa dérivée est nulle en tout point de $]a, b[$. N'importe quel $c \in ]a, b[$ convient.
3. **Second cas :** Si $f(x_m) \neq f(x_M)$. Comme $f(a) = f(b)$, au moins l'une des deux bornes $f(x_m)$ ou $f(x_M)$ est différente de $f(a)$ (et donc de $f(b)$). Supposons par exemple que $f(x_M) > f(a)$.
4. Puisque $f(x_M) \neq f(a)$ et $f(x_M) \neq f(b)$, le point $x_M$ où le maximum est atteint ne peut être ni $a$ ni $b$. Donc $x_M \in ]a, b[$.
5. Posons $c = x_M$. Étudions le taux d'accroissement de $f$ en $c$. Pour tout $h$ tel que $c+h \in [a, b]$ :
   $$ f(c+h) \leq f(c) $$ car $f(c)$ est le maximum global sur $[a,b]$.
   Donc $f(c+h) - f(c) \leq 0$.
6. Si $h > 0$, alors $\frac{f(c+h) - f(c)}{h} \leq 0$. Par passage à la limite, la dérivée à droite $f'_d(c) \leq 0$.
7. Si $h < 0$, alors $\frac{f(c+h) - f(c)}{h} \geq 0$ (car le dénominateur est strictement négatif). Par passage à la limite, la dérivée à gauche $f'_g(c) \geq 0$.
8. Puisque $f$ est dérivable sur $]a, b[$, et que $c \in ]a, b[$, $f$ est dérivable en $c$. Donc la dérivée à gauche et la dérivée à droite existent et sont égales à $f'(c)$.
9. Ainsi, $f'(c) = f'_d(c) \leq 0$ et $f'(c) = f'_g(c) \geq 0$. La seule possibilité est $f'(c) = 0$. $\blacksquare$

### Théorème des Accroissements Finis (TAF)
Soient $a, b \in \mathbb{R}$ avec $a < b$. Soit $f : [a, b] \to \mathbb{R}$ une fonction vérifiant :
- $f$ est continue sur $[a, b]$,
- $f$ est dérivable sur $]a, b[$.
Alors il existe au moins un point $c \in ]a, b[$ tel que $f(b) - f(a) = f'(c)(b - a)$.

**Démonstration :**
1. L'idée est de se ramener au théorème de Rolle en soustrayant à $f$ l'équation de la droite sécante passant par $(a, f(a))$ et $(b, f(b))$.
2. Introduisons la fonction auxiliaire $\varphi : [a, b] \to \mathbb{R}$ définie par :
   $$ \varphi(x) = f(x) - \left( f(a) + \frac{f(b) - f(a)}{b - a}(x - a) \right) $$
3. Vérifions les hypothèses de Rolle pour $\varphi$.
   - $\varphi$ est continue sur $[a, b]$ comme somme de fonctions continues.
   - $\varphi$ est dérivable sur $]a, b[$ comme somme de fonctions dérivables, et pour tout $x \in ]a, b[$,
     $$ \varphi'(x) = f'(x) - \frac{f(b) - f(a)}{b - a} $$
   - Calculons $\varphi(a)$ et $\varphi(b)$ :
     $$ \varphi(a) = f(a) - \left( f(a) + \frac{f(b) - f(a)}{b - a}(a - a) \right) = f(a) - f(a) = 0 $$
     $$ \varphi(b) = f(b) - \left( f(a) + \frac{f(b) - f(a)}{b - a}(b - a) \right) = f(b) - (f(a) + f(b) - f(a)) = 0 $$
4. Ainsi, $\varphi(a) = \varphi(b) = 0$.
5. D'après le théorème de Rolle appliqué à $\varphi$, il existe $c \in ]a, b[$ tel que $\varphi'(c) = 0$.
6. Or $\varphi'(c) = f'(c) - \frac{f(b) - f(a)}{b - a}$. Donc :
   $$ f'(c) - \frac{f(b) - f(a)}{b - a} = 0 \iff f'(c) = \frac{f(b) - f(a)}{b - a} $$
7. En multipliant par $(b-a)$, on obtient bien $f(b) - f(a) = f'(c)(b-a)$. $\blacksquare$

### Théorème de Prolongement de la Dérivée
Soit $f : I \to \mathbb{R}$ continue sur $I$ et $a \in I$. Si $f$ est dérivable sur $I \setminus \{a\}$ et si la limite $\lim_{x \to a, x \neq a} f'(x) = \ell$ existe (avec $\ell \in \mathbb{R}$), alors $f$ est dérivable en $a$ et $f'(a) = \ell$.

**Démonstration :**
1. Soit $x \in I \setminus \{a\}$. Plaçons-nous par exemple dans le cas $x > a$ (le cas $x < a$ est identique par symétrie de l'intervalle de travail).
2. Considérons l'intervalle $[a, x]$. $f$ est continue sur $[a, x]$ (car continue sur $I$) et dérivable sur $]a, x[$ (car dérivable sur $I \setminus \{a\}$).
3. D'après le Théorème des Accroissements Finis appliqué à $f$ sur $[a, x]$, il existe un réel $c_x \in ]a, x[$ tel que :
   $$ f(x) - f(a) = f'(c_x)(x - a) \iff \frac{f(x) - f(a)}{x - a} = f'(c_x) $$
4. Étudions la limite quand $x \to a$. Par le théorème d'encadrement (gendarmes), comme $a < c_x < x$, lorsque $x \to a^+$, on a nécessairement $c_x \to a^+$.
5. Or l'hypothèse indique que $\lim_{t \to a} f'(t) = \ell$. Donc, en composant les limites, $\lim_{x \to a^+} f'(c_x) = \ell$.
6. Par suite :
   $$ \lim_{x \to a^+} \frac{f(x) - f(a)}{x - a} = \lim_{x \to a^+} f'(c_x) = \ell $$
7. Le même raisonnement s'applique pour $x \to a^-$ (avec $c_x \in ]x, a[$), donnant $\lim_{x \to a^-} \frac{f(x) - f(a)}{x - a} = \ell$.
8. La limite du taux d'accroissement en $a$ existe, est finie et vaut $\ell$. Donc $f$ est dérivable en $a$ et $f'(a) = \ell$. $\blacksquare$

## 4. Exercices d'Application
L'étudiant est invité à résoudre intégralement, avec une rigueur inébranlable, les 10 exercices présents dans le dossier `exos/`, triés par difficulté.

## 5. Application en Intelligence Artificielle

La dérivabilité est le fondement incontestable de l'optimisation continue, moteur de tout l'apprentissage profond (Deep Learning).
Lorsqu'un réseau de neurones cherche à ajuster ses poids $W$ pour minimiser une fonction de coût $L(W)$ (par exemple, l'entropie croisée), il utilise l'algorithme de descente de gradient. Le gradient $\nabla L(W)$ est la généralisation en dimension supérieure de la dérivée.
L'existence de cette dérivée (garantie presque partout grâce aux fonctions d'activation comme ReLU $f(x)=\max(0,x)$ qui sont Lipschitz continues) permet d'approximer localement le comportement de la perte :
$$ L(W - \eta \nabla L(W)) \approx L(W) - \eta \|\nabla L(W)\|^2 < L(W) $$
pour un pas d'apprentissage $\eta > 0$ suffisamment petit. C'est l'application directe du DL1.

## 6. Liens Sémantiques
- Continuité (Jalon 18) - Pré-requis de la dérivabilité.
- Fonctions d'une variable - Cadre d'application.
- Calcul différentiel multidimensionnel - Extension au gradient et à la matrice jacobienne.
