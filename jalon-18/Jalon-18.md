---
uuid: "jalon-18"
title: "Continuité des fonctions d'une variable réelle, théorème des valeurs intermédiaires et compacité locale"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/surfaces-decision
prev: "[[Jalon-17.md]]"
next: "[[Jalon 19 (Dérivabilité).md]]"
---

# Jalon 18 : Continuité des fonctions d'une variable réelle, théorème des valeurs intermédiaires et compacité locale

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous dessiniez une courbe avec un crayon sur une feuille de papier. La **Continuité**, c'est simplement la règle d'or : vous n'avez pas le droit de lever le crayon. Si vous devez passer de la gauche à la droite de la feuille, votre trait doit être ininterrompu. Le **Théorème des Valeurs Intermédiaires (TVI)**, c'est comme dire que si vous commencez à dessiner en bas de la feuille et que vous finissez en haut, votre crayon a forcément dû traverser la ligne du milieu à un moment donné. Vous ne pouvez pas vous téléporter !
- **Le "Pourquoi on a inventé ça" :** Dans la nature, peu de choses changent instantanément. La température, la position d'une voiture, ou la croissance d'une plante sont des phénomènes continus. Les mathématiciens ont eu besoin de définir cette notion pour garantir que si on cherche une solution (un point où une fonction vaut zéro), elle existe vraiment. C'est fondamental pour modéliser des systèmes physiques et pour l'analyse numérique.
- **Visualisation :** Imaginez un élastique tendu. Si vous tirez sur un point, les points voisins suivent le mouvement. C'est la continuité : des causes proches produisent des effets proches. À l'inverse, une **discontinuité** serait une rupture nette de cet élastique, un "saut" ou un "trou" dans la courbe.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles

Soit $I$ un intervalle de $\mathbb{R}$ et $f : I \to \mathbb{R}$ une fonction.

1.  **Continuité en un point $x_0 \in I$ :**
    La fonction $f$ est dite **continue en $x_0$** si et seulement si :
    $$\forall \epsilon > 0, \exists \delta > 0, \forall x \in I, (|x - x_0| < \delta \Rightarrow |f(x) - f(x_0)| < \epsilon)$$
    *   **Typage chirurgical :** Cette définition est la définition de Cauchy (ou $\epsilon-\delta$). Elle exprime que pour toute "tolérance" $\epsilon$ sur l'image, il existe une "tolérance" $\delta$ sur l'antécédent telle que tous les points $x$ suffisamment proches de $x_0$ ont leurs images $f(x)$ suffisamment proches de $f(x_0)$. Le $\delta$ dépend de $\epsilon$ et de $x_0$.
    *   **Définition séquentielle (Heine) :** La fonction $f$ est continue en $x_0$ si et seulement si pour toute suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $I$ qui converge vers $x_0$, la suite des images $(f(x_n))_{n \in \mathbb{N}}$ converge vers $f(x_0)$.
        $$\forall (x_n)_{n \in \mathbb{N}} \subset I, (\lim_{n \to \infty} x_n = x_0 \Rightarrow \lim_{n \to \infty} f(x_n) = f(x_0))$$
    *   **Exemple :** La fonction $f(x) = x^2$ est continue en tout point $x_0 \in \mathbb{R}$. Pour un $\epsilon > 0$ donné, on cherche $\delta > 0$ tel que $|x - x_0| < \delta \Rightarrow |x^2 - x_0^2| < \epsilon$. On a $|x^2 - x_0^2| = |x - x_0||x + x_0|$. Si on suppose $\delta \le 1$, alors $|x - x_0| < 1 \Rightarrow x_0 - 1 < x < x_0 + 1 \Rightarrow |x + x_0| < |x_0 - 1 + x_0| + |x_0 + 1 + x_0| = |2x_0 - 1| + |2x_0 + 1|$. Plus simplement, si $|x-x_0|<1$, alors $|x|<|x_0|+1$, donc $|x+x_0| \le |x|+|x_0| < 2|x_0|+1$. Ainsi, $|x^2 - x_0^2| < \delta(2|x_0|+1)$. Pour que cela soit inférieur à $\epsilon$, on peut choisir $\delta = \min\left(1, \frac{\epsilon}{2|x_0|+1}\right)$.
    *   **Contre-exemple :** La fonction de Heaviside $H(x) = \begin{cases} 0 & \text{si } x < 0 \\ 1 & \text{si } x \ge 0 \end{cases}$ n'est pas continue en $x_0 = 0$.
        Pour $\epsilon = 1/2$, il n'existe aucun $\delta > 0$ tel que pour tout $x$ avec $|x - 0| < \delta$, on ait $|H(x) - H(0)| < 1/2$. En effet, si $x \in (-\delta, 0)$, alors $H(x) = 0$, donc $|H(x) - H(0)| = |0 - 1| = 1$, ce qui n'est pas inférieur à $1/2$.

2.  **Continuité à gauche et à droite en un point $x_0 \in I$ :**
    *   $f$ est **continue à droite en $x_0$** si :
        $$\forall \epsilon > 0, \exists \delta > 0, \forall x \in I, (x_0 \le x < x_0 + \delta \Rightarrow |f(x) - f(x_0)| < \epsilon)$$
    *   $f$ est **continue à gauche en $x_0$** si :
        $$\forall \epsilon > 0, \exists \delta > 0, \forall x \in I, (x_0 - \delta < x \le x_0 \Rightarrow |f(x) - f(x_0)| < \epsilon)$$
    *   **Proposition :** $f$ est continue en $x_0$ si et seulement si elle est continue à gauche et à droite en $x_0$.
    *   **Exemple :** La fonction $f(x) = \lfloor x \rfloor$ (partie entière) est continue à droite en tout $x_0 \in \mathbb{Z}$, mais pas continue à gauche.

3.  **Continuité sur un intervalle :**
    La fonction $f$ est dite **continue sur l'intervalle $I$** si elle est continue en tout point $x_0 \in I$. Si $I$ est un intervalle fermé $[a, b]$, la continuité en $a$ implique la continuité à droite en $a$, et la continuité en $b$ implique la continuité à gauche en $b$.

4.  **Types de discontinuités en un point $x_0$ :**
    *   **Discontinuité de première espèce (saut) :** Les limites à gauche et à droite existent et sont finies, mais différentes, ou l'une d'elles est différente de $f(x_0)$.
        $$\lim_{x \to x_0^-} f(x) \neq \lim_{x \to x_0^+} f(x)$$
        *   **Exemple :** La fonction $f(x) = \lfloor x \rfloor$ en $x_0 = 1$. $\lim_{x \to 1^-} f(x) = 0$ et $\lim_{x \to 1^+} f(x) = 1$.
    *   **Discontinuité de première espèce (éliminable ou "trou") :** Les limites à gauche et à droite existent et sont égales, mais différentes de $f(x_0)$, ou $f(x_0)$ n'est pas définie.
        *   **Exemple :** La fonction $f(x) = \frac{\sin(x)}{x}$ pour $x \neq 0$ et $f(0) = 0$. $\lim_{x \to 0} f(x) = 1 \neq f(0)$. On peut "recoller" la fonction en posant $f(0)=1$ pour la rendre continue.
    *   **Discontinuité de deuxième espèce (essentielle) :** Au moins une des limites à gauche ou à droite n'existe pas ou est infinie.
        *   **Exemple :** La fonction $f(x) = \sin(1/x)$ en $x_0 = 0$. La limite n'existe pas.

5.  **Continuité Uniforme :**
    La fonction $f$ est dite **uniformément continue sur $I$** si :
    $$\forall \epsilon > 0, \exists \delta > 0, \forall (x, y) \in I^2, (|x - y| < \delta \Rightarrow |f(x) - f(y)| < \epsilon)$$
    *   **Typage chirurgical :** La différence cruciale avec la continuité simple est que le $\delta$ ne dépend *que* de $\epsilon$, et non du point $x_0$ (ou $x, y$) choisi dans l'intervalle $I$. Cela signifie que la "vitesse" à laquelle la fonction varie est bornée sur tout l'intervalle.
    *   **Exemple :** La fonction $f(x) = x$ est uniformément continue sur $\mathbb{R}$. Pour tout $\epsilon > 0$, on peut choisir $\delta = \epsilon$. Alors $|x-y| < \delta \Rightarrow |f(x)-f(y)| = |x-y| < \epsilon$.
    *   **Contre-exemple :** La fonction $f(x) = x^2$ est continue sur $[0, +\infty[$ mais n'est pas uniformément continue sur cet intervalle.
        Pour le prouver, nous devons montrer qu'il existe un $\epsilon_0 > 0$ tel que pour tout $\delta > 0$, il existe $x, y \in [0, +\infty[$ avec $|x-y| < \delta$ et $|f(x)-f(y)| \ge \epsilon_0$.
        Prenons $\epsilon_0 = 1$. Soit $\delta > 0$ arbitraire.
        Choisissons $x = \frac{1}{\delta}$ et $y = \frac{1}{\delta} + \frac{\delta}{2}$.
        Alors $|x-y| = \left|\frac{1}{\delta} - \left(\frac{1}{\delta} + \frac{\delta}{2}\right)\right| = \frac{\delta}{2}$. Puisque $\delta > 0$, on a $\frac{\delta}{2} < \delta$.
        Calculons $|f(x)-f(y)| = |x^2 - y^2| = \left|\left(\frac{1}{\delta}\right)^2 - \left(\frac{1}{\delta} + \frac{\delta}{2}\right)^2\right|$.
        $|x^2 - y^2| = \left|\frac{1}{\delta^2} - \left(\frac{1}{\delta^2} + 1 + \frac{\delta^2}{4}\right)\right| = \left|-1 - \frac{\delta^2}{4}\right| = 1 + \frac{\delta^2}{4}$.
        Puisque $1 + \frac{\delta^2}{4} \ge 1 = \epsilon_0$, nous avons trouvé $x, y$ tels que $|x-y| < \delta$ mais $|f(x)-f(y)| \ge \epsilon_0$.
        Donc $f(x) = x^2$ n'est pas uniformément continue sur $[0, +\infty[$.

6.  **Fonction Lipschitzienne :**
    La fonction $f$ est dite **Lipschitzienne sur $I$** s'il existe une constante $L \ge 0$ (appelée constante de Lipschitz) telle que :
    $$\forall (x, y) \in I^2, |f(x) - f(y)| \le L|x - y|$$
    *   **Typage chirurgical :** Une fonction Lipschitzienne est toujours uniformément continue. Pour un $\epsilon > 0$ donné, on choisit $\delta = \epsilon/L$ (si $L>0$). Alors $|x-y| < \delta \Rightarrow |f(x)-f(y)| \le L|x-y| < L(\epsilon/L) = \epsilon$. Si $L=0$, $f$ est constante, donc uniformément continue.
    *   **Exemple :** $f(x) = \sin(x)$ est Lipschitzienne sur $\mathbb{R}$ avec $L=1$, car $|\sin(x) - \sin(y)| \le |x-y|$ (d'après l'inégalité des accroissements finis, ou directement par la formule de soustraction des sinus).

### B. Théorèmes, Propositions & Lemmes

1.  **Propriétés algébriques des fonctions continues :**
    Soient $f, g : I \to \mathbb{R}$ deux fonctions continues en $x_0 \in I$.
    *   La somme $f+g$ est continue en $x_0$.
    *   Le produit $f \cdot g$ est continue en $x_0$.
    *   Pour tout réel $\lambda$, la fonction $\lambda f$ est continue en $x_0$.
    *   Si $g(x_0) \neq 0$, alors le quotient $f/g$ est continue en $x_0$.
    *   **Proposition :** Les fonctions polynomiales sont continues sur $\mathbb{R}$. Les fonctions rationnelles sont continues sur leur domaine de définition.

2.  **Composition de fonctions continues :**
    Soient $f : I \to J$ et $g : J \to \mathbb{R}$ deux fonctions. Si $f$ est continue en $x_0 \in I$ et $g$ est continue en $f(x_0) \in J$, alors la fonction composée $g \circ f : I \to \mathbb{R}$ est continue en $x_0$.

3.  **Théorème des Valeurs Intermédiaires (TVI) :**
    Soit $f$ une fonction continue sur un intervalle $[a, b]$. Alors pour tout réel $y$ compris entre $f(a)$ et $f(b)$ (c'est-à-dire $y \in [\min(f(a), f(b)), \max(f(a), f(b))]$), il existe au moins un réel $c \in [a, b]$ tel que $f(c) = y$.
    *   **Corollaire (Théorème de Bolzano) :** Si $f$ est continue sur $[a, b]$ et $f(a)f(b) < 0$ (i.e., $f(a)$ et $f(b)$ sont de signes opposés), alors il existe au moins un $c \in ]a, b[$ tel que $f(c) = 0$.

4.  **Théorème de Heine (ou Théorème de la continuité uniforme sur un segment) :**
    Toute fonction continue sur un segment $[a, b]$ (c'est-à-dire un intervalle fermé et borné) est uniformément continue sur ce segment.
    *   **Typage chirurgical :** Ce théorème est fondamental car il établit un lien fort entre la continuité simple et la continuité uniforme sur des ensembles compacts (les segments de $\mathbb{R}$). Il n'est pas vrai sur des intervalles ouverts ou non bornés.

5.  **Théorème des Bornes Atteintes (ou Théorème de Weierstrass) :**
    L'image d'un segment $[a, b]$ par une fonction continue $f$ est un segment $[m, M]$. Autrement dit, $f([a, b]) = [\min_{x \in [a,b]} f(x), \max_{x \in [a,b]} f(x)]$. La fonction $f$ est donc bornée sur $[a, b]$ et atteint ses bornes (il existe $x_m, x_M \in [a, b]$ tels que $f(x_m) = m$ et $f(x_M) = M$).
    *   **Typage chirurgical :** Ce théorème garantit l'existence d'un minimum et d'un maximum globaux pour une fonction continue sur un segment. C'est une propriété cruciale pour l'optimisation.

6.  **Théorème de la fonction inverse continue :**
    Soit $f : I \to \mathbb{R}$ une fonction continue et strictement monotone sur un intervalle $I$. Alors $f$ est une bijection de $I$ sur $J = f(I)$, et sa fonction réciproque $f^{-1} : J \to I$ est continue et strictement monotone sur $J$.
    *   **Typage chirurgical :** L'image $J$ est également un intervalle.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Théorème des Valeurs Intermédiaires (par dichotomie)
Nous allons démontrer le cas particulier du TVI où $f(a) < 0 < f(b)$, et montrer qu'il existe $c \in [a, b]$ tel que $f(c) = 0$. Le cas général du TVI s'en déduit facilement.

**Énoncé :** Soit $f : [a, b] \to \mathbb{R}$ une fonction continue sur le segment $[a, b]$ telle que $f(a) < 0$ et $f(b) > 0$. Alors il existe au moins un réel $c \in ]a, b[$ tel que $f(c) = 0$.

**Démonstration :**

1.  **Initialisation / Cadre :**
    *   Nous définissons deux suites $(a_n)_{n \in \mathbb{N}}$ et $(b_n)_{n \in \mathbb{N}}$ par récurrence, qui vont encadrer la racine $c$.
    *   Posons $a_0 = a$ et $b_0 = b$.
    *   Par hypothèse, nous avons $f(a_0) < 0$ et $f(b_0) > 0$.

2.  **Étape 1 : Construction des suites par dichotomie**
    Supposons que pour un certain $n \in \mathbb{N}$, les termes $a_n$ et $b_n$ sont définis et vérifient les propriétés suivantes :
    (i) $a_n \in [a, b]$ et $b_n \in [a, b]$
    (ii) $a_n \le b_n$
    (iii) $f(a_n) < 0$
    (iv) $f(b_n) > 0$

    Nous construisons $a_{n+1}$ et $b_{n+1}$ comme suit :
    *   Calculons le milieu du segment $[a_n, b_n]$ : $m_n = \frac{a_n + b_n}{2}$.
    *   **Cas 1 :** Si $f(m_n) = 0$.
        Alors $c = m_n$ est une racine de $f$. La démonstration est terminée.
    *   **Cas 2 :** Si $f(m_n) < 0$.
        Dans ce cas, la racine doit se trouver dans l'intervalle $[m_n, b_n]$.
        Nous posons $a_{n+1} = m_n$ et $b_{n+1} = b_n$.
        Vérifions les propriétés pour $n+1$:
        (i) $a_{n+1} = m_n \in [a_n, b_n] \subset [a, b]$ et $b_{n+1} = b_n \in [a, b]$.
        (ii) $a_{n+1} = m_n = \frac{a_n+b_n}{2} \le b_n = b_{n+1}$.
        (iii) $f(a_{n+1}) = f(m_n) < 0$ par hypothèse de ce cas.
        (iv) $f(b_{n+1}) = f(b_n) > 0$ par hypothèse de récurrence.
    *   **Cas 3 :** Si $f(m_n) > 0$.
        Dans ce cas, la racine doit se trouver dans l'intervalle $[a_n, m_n]$.
        Nous posons $a_{n+1} = a_n$ et $b_{n+1} = m_n$.
        Vérifions les propriétés pour $n+1$:
        (i) $a_{n+1} = a_n \in [a, b]$ et $b_{n+1} = m_n \in [a_n, b_n] \subset [a, b]$.
        (ii) $a_{n+1} = a_n \le \frac{a_n+b_n}{2} = m_n = b_{n+1}$.
        (iii) $f(a_{n+1}) = f(a_n) < 0$ par hypothèse de récurrence.
        (iv) $f(b_{n+1}) = f(m_n) > 0$ par hypothèse de ce cas.

    Dans tous les cas (sauf si $f(m_n)=0$ et la preuve est finie), nous avons construit des suites $(a_n)$ et $(b_n)$ telles que $a_n \le a_{n+1}$, $b_{n+1} \le b_n$, $f(a_n) < 0$, $f(b_n) > 0$ et $b_{n+1} - a_{n+1} = \frac{b_n - a_n}{2}$.

3.  **Étape 2 : Convergence des suites**
    *   La suite $(a_n)_{n \in \mathbb{N}}$ est croissante par construction ($a_{n+1} \ge a_n$).
    *   La suite $(b_n)_{n \in \mathbb{N}}$ est décroissante par construction ($b_{n+1} \le b_n$).
    *   De plus, pour tout $n$, $a_n \le b_n$.
    *   Les suites sont bornées : $a \le a_n \le b_n \le b$.
    *   Par le théorème de convergence monotone, $(a_n)$ converge vers une limite $c_1 \in [a, b]$ et $(b_n)$ converge vers une limite $c_2 \in [a, b]$.
    *   Calculons la différence entre les termes des suites :
        $b_n - a_n = \frac{b_{n-1} - a_{n-1}}{2} = \frac{b_{n-2} - a_{n-2}}{2^2} = \dots = \frac{b_0 - a_0}{2^n} = \frac{b - a}{2^n}$.
    *   Puisque $\lim_{n \to \infty} \frac{b - a}{2^n} = 0$, nous avons $\lim_{n \to \infty} (b_n - a_n) = 0$.
    *   Par conséquent, $c_1 = c_2$. Nous appelons cette limite commune $c$.
    *   Puisque $a_n \le c \le b_n$ pour tout $n$, et $a_0 = a$, $b_0 = b$, on a $c \in [a, b]$.
    *   De plus, comme $f(a) < 0$ et $f(b) > 0$, $c$ ne peut être ni $a$ ni $b$ (sauf si $f(a)=0$ ou $f(b)=0$, ce qui est exclu par l'hypothèse stricte $f(a)<0<f(b)$). Donc $c \in ]a, b[$.

4.  **Étape 3 : Utilisation de la continuité**
    *   La fonction $f$ est continue sur $[a, b]$, et donc en particulier en $c$.
    *   Par la définition séquentielle de la continuité (Heine), puisque $\lim_{n \to \infty} a_n = c$, nous avons $\lim_{n \to \infty} f(a_n) = f(c)$.
    *   De même, puisque $\lim_{n \to \infty} b_n = c$, nous avons $\lim_{n \to \infty} f(b_n) = f(c)$.
    *   Par construction, pour tout $n \in \mathbb{N}$, nous avons $f(a_n) < 0$.
    *   Par passage à la limite dans les inégalités larges (si une suite $(u_n)$ converge vers $L$ et $u_n \le K$ pour tout $n$, alors $L \le K$), nous obtenons $f(c) \le 0$.
    *   De même, pour tout $n \in \mathbb{N}$, nous avons $f(b_n) > 0$.
    *   Par passage à la limite dans les inégalités larges, nous obtenons $f(c) \ge 0$.

5.  **Conclusion :**
    *   Nous avons établi que $f(c) \le 0$ et $f(c) \ge 0$.
    *   La seule valeur possible pour $f(c)$ qui satisfait ces deux inégalités est $f(c) = 0$.
    *   Le point $c \in ]a, b[$ tel que $f(c) = 0$ existe bien. Le théorème est démontré pour le cas $f(a) < 0 < f(b)$.

**Démonstration du cas général du TVI :**
Soit $f$ continue sur $[a, b]$. Soit $y$ un réel compris entre $f(a)$ et $f(b)$.
Sans perte de généralité, supposons $f(a) \le y \le f(b)$.
Considérons la fonction auxiliaire $g(x) = f(x) - y$.
*   $g$ est continue sur $[a, b]$ car $f$ est continue et $x \mapsto y$ est continue.
*   $g(a) = f(a) - y \le 0$ (par hypothèse $f(a) \le y$).
*   $g(b) = f(b) - y \ge 0$ (par hypothèse $y \le f(b)$).
Si $g(a)=0$ ou $g(b)=0$, alors $a$ ou $b$ est le $c$ recherché.
Sinon, $g(a) < 0$ et $g(b) > 0$. D'après la démonstration précédente (cas particulier du TVI), il existe $c \in ]a, b[$ tel que $g(c) = 0$.
Ceci implique $f(c) - y = 0$, soit $f(c) = y$.
Le théorème des valeurs intermédiaires est ainsi démontré dans sa généralité.

### Démonstration des propriétés algébriques de la continuité (pour la somme)
**Énoncé :** Soient $f, g : I \to \mathbb{R}$ deux fonctions continues en $x_0 \in I$. Alors la fonction $h = f+g$ est continue en $x_0$.

**Démonstration :**
Nous voulons montrer que pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour tout $x \in I$, si $|x - x_0| < \delta$, alors $|h(x) - h(x_0)| < \epsilon$.

1.  Soit $\epsilon > 0$ arbitrairement choisi.
2.  Puisque $f$ est continue en $x_0$, par définition, il existe $\delta_1 > 0$ tel que pour tout $x \in I$, si $|x - x_0| < \delta_1$, alors $|f(x) - f(x_0)| < \frac{\epsilon}{2}$.
3.  Puisque $g$ est continue en $x_0$, par définition, il existe $\delta_2 > 0$ tel que pour tout $x \in I$, si $|x - x_0| < \delta_2$, alors $|g(x) - g(x_0)| < \frac{\epsilon}{2}$.
4.  Choisissons $\delta = \min(\delta_1, \delta_2)$. Puisque $\delta_1 > 0$ et $\delta_2 > 0$, $\delta$ est bien un nombre réel strictement positif.
5.  Maintenant, considérons un $x \in I$ tel que $|x - x_0| < \delta$.
    *   Puisque $\delta \le \delta_1$, nous avons $|x - x_0| < \delta_1$, ce qui implique $|f(x) - f(x_0)| < \frac{\epsilon}{2}$.
    *   Puisque $\delta \le \delta_2$, nous avons $|x - x_0| < \delta_2$, ce qui implique $|g(x) - g(x_0)| < \frac{\epsilon}{2}$.
6.  Nous voulons majorer $|h(x) - h(x_0)|$:
    $|h(x) - h(x_0)| = |(f(x) + g(x)) - (f(x_0) + g(x_0))|$
    $|h(x) - h(x_0)| = |(f(x) - f(x_0)) + (g(x) - g(x_0))|$
7.  Par l'inégalité triangulaire, nous avons :
    $|(f(x) - f(x_0)) + (g(x) - g(x_0))| \le |f(x) - f(x_0)| + |g(x) - g(x_0)|$
8.  En utilisant les majorations obtenues aux étapes 5 :
    $|f(x) - f(x_0)| + |g(x) - g(x_0)| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
9.  Donc, pour tout $x \in I$ tel que $|x - x_0| < \delta$, nous avons $|h(x) - h(x_0)| < \epsilon$.
10. Puisque $\epsilon$ était arbitraire, $h = f+g$ est continue en $x_0$.

### Démonstration du Théorème de Weierstrass (Théorème des Bornes Atteintes)
**Énoncé :** Soit $f : [a, b] \to \mathbb{R}$ une fonction continue sur le segment $[a, b]$. Alors $f$ est bornée sur $[a, b]$ et atteint ses bornes. C'est-à-dire, il existe $x_m, x_M \in [a, b]$ tels que $f(x_m) = \min_{x \in [a,b]} f(x)$ et $f(x_M) = \max_{x \in [a,b]} f(x)$.

**Démonstration :**

**Partie 1 : $f$ est bornée sur $[a, b]$.**
Nous allons démontrer que $f$ est bornée supérieurement. La démonstration pour la borne inférieure est similaire.
Supposons par l'absurde que $f$ n'est pas bornée supérieurement sur $[a, b]$.
1.  Alors, pour tout $n \in \mathbb{N}^*$, il existe un $x_n \in [a, b]$ tel que $f(x_n) > n$.
2.  La suite $(x_n)_{n \in \mathbb{N}^*}$ est une suite d'éléments du segment $[a, b]$.
3.  Puisque $[a, b]$ est un segment (fermé et borné), il est compact. D'après le théorème de Bolzano-Weierstrass, toute suite bornée admet une sous-suite convergente.
4.  Il existe donc une sous-suite $(x_{\phi(n)})_{n \in \mathbb{N}^*}$ qui converge vers un point $c \in [a, b]$ (car $[a, b]$ est fermé).
5.  Puisque $f$ est continue en $c$, par la définition séquentielle de la continuité, nous avons $\lim_{n \to \infty} f(x_{\phi(n)}) = f(c)$.
6.  Cependant, par construction de la suite $(x_n)$, nous avons $f(x_{\phi(n)}) > \phi(n)$.
7.  Comme $\phi(n)$ est une suite strictement croissante d'entiers, $\lim_{n \to \infty} \phi(n) = +\infty$.
8.  Donc, $\lim_{n \to \infty} f(x_{\phi(n)}) = +\infty$.
9.  Ceci contredit le fait que $\lim_{n \to \infty} f(x_{\phi(n)}) = f(c)$, car $f(c)$ est un nombre réel fini.
10. Par conséquent, l'hypothèse de départ est fausse : $f$ doit être bornée supérieurement sur $[a, b]$.
11. De manière analogue, en considérant $f(x_n) < -n$, on montre que $f$ est bornée inférieurement.
12. Donc, $f$ est bornée sur $[a, b]$.

**Partie 2 : $f$ atteint ses bornes.**
Puisque $f$ est bornée sur $[a, b]$, l'ensemble image $f([a, b])$ est borné.
1.  Soit $M = \sup_{x \in [a,b]} f(x)$. Puisque $f([a, b])$ est non vide et borné supérieurement, $M$ existe et est fini.
2.  Nous voulons montrer qu'il existe $x_M \in [a, b]$ tel que $f(x_M) = M$.
3.  Par la définition de la borne supérieure, pour tout $n \in \mathbb{N}^*$, il existe un $x_n \in [a, b]$ tel que $M - \frac{1}{n} < f(x_n) \le M$.
4.  La suite $(x_n)_{n \in \mathbb{N}^*}$ est une suite d'éléments du segment $[a, b]$.
5.  D'après le théorème de Bolzano-Weierstrass, il existe une sous-suite $(x_{\phi(n)})_{n \in \mathbb{N}^*}$ qui converge vers un point $x_M \in [a, b]$.
6.  Puisque $f$ est continue en $x_M$, par la définition séquentielle de la continuité, nous avons $\lim_{n \to \infty} f(x_{\phi(n)}) = f(x_M)$.
7.  D'autre part, pour la sous-suite, nous avons $M - \frac{1}{\phi(n)} < f(x_{\phi(n)}) \le M$.
8.  Par le théorème des gendarmes, puisque $\lim_{n \to \infty} (M - \frac{1}{\phi(n)}) = M$ et $\lim_{n \to \infty} M = M$, nous avons $\lim_{n \to \infty} f(x_{\phi(n)}) = M$.
9.  Par unicité de la limite, $f(x_M) = M$.
10. Donc, $f$ atteint sa borne supérieure sur $[a, b]$.
11. De manière analogue, en considérant la borne inférieure $m = \inf_{x \in [a,b]} f(x)$, on montre qu'il existe $x_m \in [a, b]$ tel que $f(x_m) = m$.
12. Le théorème de Weierstrass est démontré.

### Démonstration du Théorème de Heine (Théorème de la continuité uniforme sur un segment)
**Énoncé :** Toute fonction continue sur un segment $[a, b]$ est uniformément continue sur ce segment.

**Démonstration :**
Supposons par l'absurde que $f$ est continue sur $[a, b]$ mais n'est pas uniformément continue sur $[a, b]$.
1.  Si $f$ n'est pas uniformément continue, alors la négation de la définition de la continuité uniforme est vraie :
    Il existe un $\epsilon_0 > 0$ tel que pour tout $\delta > 0$, il existe $x, y \in [a, b]$ tels que $|x - y| < \delta$ et $|f(x) - f(y)| \ge \epsilon_0$.
2.  En particulier, pour chaque $n \in \mathbb{N}^*$, en prenant $\delta = \frac{1}{n}$, il existe une paire de points $(x_n, y_n)$ dans $[a, b]^2$ telle que :
    (i) $|x_n - y_n| < \frac{1}{n}$
    (ii) $|f(x_n) - f(y_n)| \ge \epsilon_0$
3.  Les suites $(x_n)_{n \in \mathbb{N}^*}$ et $(y_n)_{n \in \mathbb{N}^*}$ sont des suites d'éléments du segment $[a, b]$.
4.  Puisque $[a, b]$ est un segment (fermé et borné), il est compact. D'après le théorème de Bolzano-Weierstrass, la suite $(x_n)$ admet une sous-suite convergente $(x_{\phi(n)})_{n \in \mathbb{N}^*}$.
5.  Soit $c = \lim_{n \to \infty} x_{\phi(n)}$. Puisque $[a, b]$ est fermé, $c \in [a, b]$.
6.  Considérons maintenant la sous-suite correspondante $(y_{\phi(n)})_{n \in \mathbb{N}^*}$.
    Nous avons $|x_{\phi(n)} - y_{\phi(n)}| < \frac{1}{\phi(n)}$.
    Puisque $\phi(n) \to \infty$ quand $n \to \infty$, nous avons $\frac{1}{\phi(n)} \to 0$ quand $n \to \infty$.
    Par le théorème des gendarmes, $\lim_{n \to \infty} |x_{\phi(n)} - y_{\phi(n)}| = 0$.
7.  Puisque $\lim_{n \to \infty} x_{\phi(n)} = c$ et $\lim_{n \to \infty} (x_{\phi(n)} - y_{\phi(n)}) = 0$, nous pouvons déduire la limite de $y_{\phi(n)}$:
    $\lim_{n \to \infty} y_{\phi(n)} = \lim_{n \to \infty} (x_{\phi(n)} - (x_{\phi(n)} - y_{\phi(n)})) = \lim_{n \to \infty} x_{\phi(n)} - \lim_{n \to \infty} (x_{\phi(n)} - y_{\phi(n)}) = c - 0 = c$.
    Donc, la sous-suite $(y_{\phi(n)})$ converge également vers $c$.
8.  Puisque $f$ est continue sur $[a, b]$, elle est continue en $c$.
    Par la définition séquentielle de la continuité :
    *   $\lim_{n \to \infty} f(x_{\phi(n)}) = f(c)$.
    *   $\lim_{n \to \infty} f(y_{\phi(n)}) = f(c)$.
9.  Par conséquent, $\lim_{n \to \infty} (f(x_{\phi(n)}) - f(y_{\phi(n)})) = f(c) - f(c) = 0$.
10. Cependant, par construction de la sous-suite, nous avons $|f(x_{\phi(n)}) - f(y_{\phi(n)})| \ge \epsilon_0$ pour tout $n$.
11. Par passage à la limite dans les inégalités larges, nous obtenons $|0| \ge \epsilon_0$, ce qui signifie $0 \ge \epsilon_0$.
12. Ceci contredit notre hypothèse initiale que $\epsilon_0 > 0$.
13. Par conséquent, l'hypothèse de départ est fausse : $f$ doit être uniformément continue sur $[a, b]$.
14. Le théorème de Heine est démontré.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Point Fixe (Application du TVI)
**Énoncé :** Soit $f : [0, 1] \to [0, 1]$ une fonction continue. Démontrer qu'il existe au moins un réel $c \in [0, 1]$ tel que $f(c) = c$. Un tel $c$ est appelé un point fixe de $f$.

**Correction Détaillée :**

1.  **Définition de la fonction auxiliaire :**
    Considérons la fonction auxiliaire $g(x)$ définie sur l'intervalle $[0, 1]$ par $g(x) = f(x) - x$.
2.  **Continuité de la fonction auxiliaire :**
    *   La fonction $f$ est continue sur $[0, 1]$ par hypothèse.
    *   La fonction $h(x) = x$ (fonction identité) est continue sur $[0, 1]$ (c'est une fonction polynomiale).
    *   Puisque la différence de deux fonctions continues est continue, la fonction $g(x) = f(x) - x$ est continue sur l'intervalle $[0, 1]$.
3.  **Évaluation aux bornes de l'intervalle :**
    *   Calculons la valeur de $g$ en $x=0$:
        $g(0) = f(0) - 0 = f(0)$.
        Puisque $f : [0, 1] \to [0, 1]$, l'image $f(0)$ doit appartenir à l'intervalle $[0, 1]$.
        Par conséquent, $f(0) \ge 0$. Donc, $g(0) \ge 0$.
    *   Calculons la valeur de $g$ en $x=1$:
        $g(1) = f(1) - 1$.
        Puisque $f : [0, 1] \to [0, 1]$, l'image $f(1)$ doit appartenir à l'intervalle $[0, 1]$.
        Par conséquent, $f(1) \le 1$. Donc, $f(1) - 1 \le 0$. Donc, $g(1) \le 0$.
4.  **Application du Théorème des Valeurs Intermédiaires (TVI) :**
    Nous avons deux cas possibles :
    *   **Cas 1 :** Si $g(0) = 0$.
        Alors $f(0) - 0 = 0$, ce qui signifie $f(0) = 0$. Dans ce cas, $c=0$ est un point fixe.
    *   **Cas 2 :** Si $g(1) = 0$.
        Alors $f(1) - 1 = 0$, ce qui signifie $f(1) = 1$. Dans ce cas, $c=1$ est un point fixe.
    *   **Cas 3 :** Si $g(0) > 0$ et $g(1) < 0$.
        Dans ce cas, nous avons $g(1) < 0 < g(0)$.
        La fonction $g$ est continue sur le segment $[0, 1]$.
        D'après le Théorème des Valeurs Intermédiaires (TVI), pour toute valeur $y$ comprise entre $g(1)$ et $g(0)$, il existe un $c \in [0, 1]$ tel que $g(c) = y$.
        En particulier, puisque $0$ est compris entre $g(1)$ et $g(0)$, il existe au moins un réel $c \in ]0, 1[$ tel que $g(c) = 0$.
5.  **Conclusion :**
    Dans tous les cas, il existe un réel $c \in [0, 1]$ tel que $g(c) = 0$.
    Par définition de $g(x)$, cela signifie $f(c) - c = 0$, ce qui équivaut à $f(c) = c$.
    Ainsi, toute fonction continue d'un segment dans lui-même admet au moins un point fixe.

### Exercice 2 : Continuité Uniforme de $\sqrt{x}$
**Énoncé :** Démontrer que la fonction $f(x) = \sqrt{x}$ est uniformément continue sur $[0, +\infty[$.

**Correction Détaillée :**
Pour démontrer l'uniforme continuité sur $[0, +\infty[$, nous allons diviser l'intervalle en deux parties : un segment $[0, M]$ et un intervalle non borné $[M, +\infty[$, puis recoller les résultats.

1.  **Uniforme continuité sur un segment $[0, 1]$ :**
    *   La fonction $f(x) = \sqrt{x}$ est continue sur l'intervalle $[0, 1]$.
    *   L'intervalle $[0, 1]$ est un segment (fermé et borné).
    *   D'après le Théorème de Heine, toute fonction continue sur un segment est uniformément continue sur ce segment.
    *   Donc, $f(x) = \sqrt{x}$ est uniformément continue sur $[0, 1]$.
    *   Cela signifie que pour tout $\epsilon > 0$, il existe $\delta_1 > 0$ tel que pour tout $(x, y) \in [0, 1]^2$, si $|x - y| < \delta_1$, alors $|f(x) - f(y)| < \epsilon$.

2.  **Uniforme continuité sur un intervalle non borné $[1, +\infty[$ :**
    *   Considérons $x, y \in [1, +\infty[$.
    *   Nous voulons majorer $|f(x) - f(y)| = |\sqrt{x} - \sqrt{y}|$.
    *   Pour éviter les racines au dénominateur, nous multiplions par l'expression conjuguée :
        $|\sqrt{x} - \sqrt{y}| = \left|\frac{(\sqrt{x} - \sqrt{y})(\sqrt{x} + \sqrt{y})}{\sqrt{x} + \sqrt{y}}\right| = \left|\frac{x - y}{\sqrt{x} + \sqrt{y}}\right| = \frac{|x - y|}{\sqrt{x} + \sqrt{y}}$.
    *   Puisque $x \ge 1$ et $y \ge 1$, nous avons $\sqrt{x} \ge 1$ et $\sqrt{y} \ge 1$.
    *   Par conséquent, $\sqrt{x} + \sqrt{y} \ge 1 + 1 = 2$.
    *   Donc, $\frac{1}{\sqrt{x} + \sqrt{y}} \le \frac{1}{2}$.
    *   En substituant cette inégalité, nous obtenons :
        $|\sqrt{x} - \sqrt{y}| \le \frac{1}{2} |x - y|$.
    *   Cette inégalité montre que $f(x) = \sqrt{x}$ est une fonction **Lipschitzienne** sur $[1, +\infty[$ avec une constante de Lipschitz $L = 1/2$.
    *   Toute fonction Lipschitzienne est uniformément continue.
    *   Pour un $\epsilon > 0$ donné, nous pouvons choisir $\delta_2 = 2\epsilon$.
    *   Alors, si $|x - y| < \delta_2 = 2\epsilon$, nous avons $|\sqrt{x} - \sqrt{y}| \le \frac{1}{2} |x - y| < \frac{1}{2} (2\epsilon) = \epsilon$.
    *   Donc, $f(x) = \sqrt{x}$ est uniformément continue sur $[1, +\infty[$.

3.  **Recollement des continuités uniformes sur $[0, +\infty[$ :**
    Nous avons montré que $f$ est uniformément continue sur $[0, 1]$ (avec $\delta_1$) et sur $[1, +\infty[$ (avec $\delta_2$). Nous voulons montrer qu'elle l'est sur l'union $[0, +\infty[$.
    Soit $\epsilon > 0$ donné.
    *   D'après le point 1, il existe $\delta_1 > 0$ tel que pour tout $(x, y) \in [0, 1]^2$, si $|x - y| < \delta_1$, alors $|f(x) - f(y)| < \epsilon$.
    *   D'après le point 2, il existe $\delta_2 > 0$ tel que pour tout $(x, y) \in [1, +\infty[^2$, si $|x - y| < \delta_2$, alors $|f(x) - f(y)| < \epsilon$.
    *   Choisissons $\delta = \min(\delta_1, \delta_2, 1)$. (Le choix de 1 est pour s'assurer que si $x$ et $y$ sont "proches" et de part et d'autre de 1, ils ne sont pas trop éloignés de 1).
    *   Soient $x, y \in [0, +\infty[$ tels que $|x - y| < \delta$.
    *   **Cas A :** $x, y \in [0, 1]$.
        Puisque $|x - y| < \delta \le \delta_1$, nous avons $|f(x) - f(y)| < \epsilon$.
    *   **Cas B :** $x, y \in [1, +\infty[$.
        Puisque $|x - y| < \delta \le \delta_2$, nous avons $|f(x) - f(y)| < \epsilon$.
    *   **Cas C :** $x \in [0, 1]$ et $y \in [1, +\infty[$ (ou inversement, par symétrie).
        Puisque $|x - y| < \delta \le 1$, nous avons $y - x < 1$.
        Comme $x \le 1$ et $y \ge 1$, on a $y-x \ge 0$.
        Considérons le point $1$. Nous pouvons écrire :
        $|f(x) - f(y)| = |f(x) - f(1) + f(1) - f(y)| \le |f(x) - f(1)| + |f(1) - f(y)|$ (par inégalité triangulaire).
        *   Pour le terme $|f(x) - f(1)|$: $x \in [0, 1]$ et $1 \in [0, 1]$. De plus, $|x - 1| \le |x - y| < \delta \le \delta_1$.
            Donc, $|f(x) - f(1)| < \epsilon$.
        *   Pour le terme $|f(1) - f(y)|$: $1 \in [1, +\infty[$ et $y \in [1, +\infty[$. De plus, $|1 - y| \le |x - y| < \delta \le \delta_2$.
            Donc, $|f(1) - f(y)| < \epsilon$.
        *   En combinant, $|f(x) - f(y)| < \epsilon + \epsilon = 2\epsilon$.
        *   Pour que cela soit inférieur à $\epsilon$, nous devons ajuster notre choix initial de $\delta_1$ et $\delta_2$. Si nous avions choisi $\delta_1'$ et $\delta_2'$ pour $\epsilon/2$, alors le recollement donnerait $\epsilon/2 + \epsilon/2 = \epsilon$.
        *   Reprenons : Pour $\epsilon > 0$, il existe $\delta_1'$ tel que pour $(x,y) \in [0,1]^2$, $|x-y|<\delta_1' \Rightarrow |f(x)-f(y)| < \epsilon/2$.
        *   Il existe $\delta_2'$ tel que pour $(x,y) \in [1,+\infty[^2$, $|x-y|<\delta_2' \Rightarrow |f(x)-f(y)| < \epsilon/2$.
        *   Choisissons $\delta = \min(\delta_1', \delta_2', 1)$.
        *   Si $x \in [0,1]$ et $y \in [1,+\infty[$ avec $|x-y|<\delta$:
            $|f(x)-f(y)| \le |f(x)-f(1)| + |f(1)-f(y)|$.
            Comme $|x-1| \le |x-y| < \delta \le \delta_1'$, alors $|f(x)-f(1)| < \epsilon/2$.
            Comme $|1-y| \le |x-y| < \delta \le \delta_2'$, alors $|f(1)-f(y)| < \epsilon/2$.
            Donc, $|f(x)-f(y)| < \epsilon/2 + \epsilon/2 = \epsilon$.

    Dans tous les cas, pour tout $\epsilon > 0$, nous avons trouvé un $\delta > 0$ tel que si $|x - y| < \delta$, alors $|f(x) - f(y)| < \epsilon$.
**Conclusion :** La fonction $f(x) = \sqrt{x}$ est bien uniformément continue sur $[0, +\infty[$.

### Exercice 3 : Fonction continue mais non uniformément continue
**Énoncé :** Démontrer que la fonction $f(x) = \frac{1}{x}$ est continue sur $]0, 1]$ mais n'est pas uniformément continue sur cet intervalle.

**Correction Détaillée :**

**Partie 1 : Continuité sur $]0, 1]$**
1.  Soit $x_0 \in ]0, 1]$. Nous voulons montrer que $f$ est continue en $x_0$.
2.  Soit $\epsilon > 0$ arbitrairement choisi.
3.  Nous cherchons $\delta > 0$ tel que pour tout $x \in ]0, 1]$, si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
4.  $|f(x) - f(x_0)| = \left|\frac{1}{x} - \frac{1}{x_0}\right| = \left|\frac{x_0 - x}{x x_0}\right| = \frac{|x - x_0|}{|x x_0|}$.
5.  Pour majorer cette expression, nous devons minorer $|x x_0|$.
    Puisque $x_0 \in ]0, 1]$, $x_0 > 0$.
    Choisissons $\delta$ tel que $\delta \le \frac{x_0}{2}$.
    Alors, si $|x - x_0| < \delta$, nous avons $x_0 - \delta < x < x_0 + \delta$.
    Puisque $\delta \le \frac{x_0}{2}$, on a $x_0 - \delta \ge x_0 - \frac{x_0}{2} = \frac{x_0}{2}$.
    Donc, $x > \frac{x_0}{2}$.
    Par conséquent, $x x_0 > \frac{x_0}{2} \cdot x_0 = \frac{x_0^2}{2}$.
    Donc, $\frac{1}{|x x_0|} < \frac{2}{x_0^2}$.
6.  En substituant dans l'expression de $|f(x) - f(x_0)|$:
    $|f(x) - f(x_0)| < |x - x_0| \cdot \frac{2}{x_0^2}$.
7.  Nous voulons que cette expression soit inférieure à $\epsilon$. Donc, nous voulons $|x - x_0| \cdot \frac{2}{x_0^2} < \epsilon$.
    Cela implique $|x - x_0| < \frac{\epsilon x_0^2}{2}$.
8.  Nous choisissons $\delta = \min\left(\frac{x_0}{2}, \frac{\epsilon x_0^2}{2}\right)$.
9.  Avec ce choix de $\delta$, pour tout $x \in ]0, 1]$ tel que $|x - x_0| < \delta$, nous avons :
    $|f(x) - f(x_0)| < \frac{\epsilon x_0^2}{2} \cdot \frac{2}{x_0^2} = \epsilon$.
10. Donc, $f(x) = \frac{1}{x}$ est continue en tout point $x_0 \in ]0, 1]$. Par conséquent, elle est continue sur $]0, 1]$.

**Partie 2 : Non-uniforme continuité sur $]0, 1]$**
Nous devons montrer qu'il existe un $\epsilon_0 > 0$ tel que pour tout $\delta > 0$, il existe $x, y \in ]0, 1]$ avec $|x - y| < \delta$ et $|f(x) - f(y)| \ge \epsilon_0$.

1.  Choisissons $\epsilon_0 = 1$.
2.  Soit $\delta > 0$ arbitrairement choisi.
3.  Nous devons trouver $x, y \in ]0, 1]$ tels que $|x - y| < \delta$ et $\left|\frac{1}{x} - \frac{1}{y}\right| \ge 1$.
4.  Considérons des points $x$ et $y$ très proches de $0$.
    Soit $y = \min\left(1, \frac{\delta}{2}\right)$. (Pour s'assurer que $y \in ]0, 1]$ et que $y$ est petit).
    Soit $x = \frac{y}{2}$.
    Alors $x \in ]0, 1]$ et $y \in ]0, 1]$.
5.  Calculons la distance entre $x$ et $y$:
    $|x - y| = \left|\frac{y}{2} - y\right| = \left|-\frac{y}{2}\right| = \frac{y}{2}$.
    Puisque $y \le \frac{\delta}{2}$, on a $\frac{y}{2} \le \frac{\delta}{4}$.
    Donc, $|x - y| < \delta$.
6.  Calculons la différence des images :
    $|f(x) - f(y)| = \left|\frac{1}{x} - \frac{1}{y}\right| = \left|\frac{1}{y/2} - \frac{1}{y}\right| = \left|\frac{2}{y} - \frac{1}{y}\right| = \left|\frac{1}{y}\right| = \frac{1}{y}$.
7.  Puisque $y = \min\left(1, \frac{\delta}{2}\right)$, nous avons $y \le 1$ et $y \le \frac{\delta}{2}$.
    Donc, $\frac{1}{y} \ge \frac{1}{\delta/2} = \frac{2}{\delta}$.
    Et $\frac{1}{y} \ge \frac{1}{1} = 1$.
    En particulier, $\frac{1}{y} \ge 1 = \epsilon_0$.
8.  Nous avons trouvé $x, y \in ]0, 1]$ tels que $|x - y| < \delta$ et $|f(x) - f(y)| \ge \epsilon_0$.
9.  Puisque ce raisonnement est valable pour tout $\delta > 0$, la fonction $f(x) = \frac{1}{x}$ n'est pas uniformément continue sur $]0, 1]$.

**Conclusion :** La fonction $f(x) = \frac{1}{x}$ est continue sur $]0, 1]$ mais n'est pas uniformément continue sur cet intervalle. L'intuition est que la pente de la fonction devient arbitrairement grande à l'approche de 0, ce qui empêche de trouver un $\delta$ unique pour toutes les paires de points.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*

-   **Le Pont Théorique :** En Intelligence Artificielle, et plus particulièrement dans les réseaux de neurones profonds, les fonctions de transformation (activations, couches linéaires, convolutions) sont souvent choisies pour être continues, voire différentiables. La continuité garantit que de petites modifications des données d'entrée (par exemple, un léger bruit sur une image, une petite variation dans un texte) n'entraînent pas de changements brutaux et imprévisibles dans la prédiction ou la sortie du modèle. C'est la base de la **Robustesse** des modèles d'IA. Sans continuité, un modèle pourrait donner des résultats complètement différents pour des entrées presque identiques, le rendant inutilisable dans des applications critiques.

-   **Exemple Concret 1 : Robustesse et Adversarial Examples :**
    Dans la classification d'images, un réseau de neurones apprend une fonction $f: \mathbb{R}^d \to \mathbb{R}^k$ (où $d$ est la dimension de l'image et $k$ le nombre de classes). Si $f$ est continue, on s'attend à ce que $f(x)$ soit proche de $f(x')$ si $x$ est proche de $x'$. Cependant, les fonctions apprises par les réseaux de neurones sont souvent très complexes et peuvent être "localement non-Lipschitziennes" ou avoir des régions où la pente est extrêmement raide. Cela conduit au phénomène des **exemples adversariaux** : une perturbation infime et imperceptible à l'œil humain sur une image $x$ (créant $x'$) peut faire en sorte que le modèle classifie $x'$ dans une classe complètement différente de $x$. Bien que la fonction soit globalement continue, l'absence de continuité uniforme ou de bornes de Lipschitz globales peut rendre le modèle vulnérable. La recherche vise à rendre ces fonctions plus "lisses" ou plus robustes, souvent en imposant des contraintes de régularisation qui favorisent la continuité uniforme ou la Lipschitzianité.

-   **Exemple Concret 2 : Génération d'images et Espace Latent :**
    Dans la génération d'images par des modèles comme les **GAN (Generative Adversarial Networks)** ou les **Auto-encodeurs variationnels (VAE)**, on manipule un "Espace Latent" (un espace de vecteurs de faible dimension). Le générateur (ou décodeur) est une fonction $G: \mathbb{R}^m \to \mathbb{R}^d$ qui transforme un vecteur latent $z$ en une image $G(z)$. On veut que cet espace latent soit continu : si on se déplace doucement entre le vecteur latent $z_1$ d'un "Chien" et le vecteur latent $z_2$ d'un "Chat", le décodeur doit générer une suite d'images qui se transforment graduellement de l'un à l'autre sans sauter d'une image à une autre sans transition logique. Si la fonction $G$ apprise par le réseau n'était pas continue, le modèle "hallucinerait" des images incohérentes ou des transitions abruptes au moindre petit changement de paramètre dans l'espace latent. La continuité du générateur est essentielle pour l'exploration fluide et l'interpolation dans l'espace des images.

-   **Exemple Concret 3 : Optimisation et Convergence :**
    Les algorithmes d'apprentissage automatique reposent souvent sur l'optimisation de fonctions de coût. La continuité de ces fonctions de coût (et de leurs dérivées, si elles existent) est une propriété fondamentale qui garantit que les algorithmes d'optimisation (comme la descente de gradient) peuvent converger vers un minimum local. Si la fonction de coût présentait des discontinuités, l'algorithme pourrait "sauter" des minima ou ne jamais trouver de direction de descente stable.

## 6. Liens Sémantiques
-   **Concepts Précédents requis :**
    *   [[Jalon 13 (Structure de R)]] : Compréhension des propriétés de $\mathbb{R}$ (ordre, complétude, intervalles, segments), qui sont fondamentales pour les définitions et théorèmes de continuité.
    *   [[Jalon 14 (Suites réelles et complexes)]] : Maîtrise des notions de convergence de suites, de suites adjacentes, de suites de Cauchy, et du théorème de Bolzano-Weierstrass, qui sont utilisées dans les démonstrations de la continuité et des théorèmes associés (TVI, Weierstrass, Heine).
-   **Concepts Futurs dépendants :**
    *   [[Jalon 19 (Dérivabilité)]] : La dérivabilité est une condition plus forte que la continuité. Toute fonction dérivable est continue, mais la réciproque est fausse. La continuité est un prérequis essentiel à la notion de dérivabilité.
    *   [[Jalon 44 (Fonctions de plusieurs variables)]] : Les concepts de continuité s'étendent aux fonctions de plusieurs variables, nécessitant l'introduction de topologies plus générales (normes, métriques).
    *   [[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.)]] : La continuité est un concept central en topologie générale. La définition $\epsilon-\delta$ est une instanciation de la continuité dans les espaces métriques. Ce jalon généralisera la notion à des espaces topologiques arbitraires via les ouverts et les voisinages, et introduira les homéomorphismes comme bijections continues dont la réciproque est continue.
    *   **Intégration (Théorème fondamental de l'analyse) :** La continuité est une condition suffisante pour l'intégrabilité au sens de Riemann.
    *   **Équations Différentielles :** L'existence et l'unicité des solutions d'équations différentielles dépendent souvent de la continuité (et de la Lipschitzianité) des fonctions impliquées (Théorème de Cauchy-Lipschitz).
