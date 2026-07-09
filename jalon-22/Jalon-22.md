---
uuid: "jalon-22"
title: "Séries de fonctions, convergence normale, théorèmes d'interversion limite-intégrale et limite-dérivée"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence-series
prev: "[[jalon-21/Jalon-21.md|Jalon 21 : Suites de fonctions]]"
next: "[[jalon-23/Jalon 23 (Séries entières).md|Jalon 23 : Séries entières]]"
---

# Jalon 22 : Séries de fonctions, convergence normale, théorèmes d'interversion limite-intégrale et limite-dérivée

## 1. L'Échafaudage Cognitif & Traçabilité Historique

L'étude des séries de fonctions trouve son origine dans le problème fondamental de la représentation de signaux et de fonctions complexes par des superpositions infinies d'éléments simples. Au début du XIXe siècle, les travaux de Joseph Fourier sur la propagation de la chaleur ont bousculé le monde mathématique. Fourier affirmait que toute fonction (même discontinue) pouvait s'écrire comme une somme infinie de sinus et cosinus.

Cette affirmation audacieuse a déclenché une crise de rigueur. Si l'on additionne une infinité de fonctions continues (comme des sinus et des cosinus), la limite de cette somme est-elle toujours continue ? Augustin-Louis Cauchy a d'abord cru que la réponse était "oui". Mais en 1826, Niels Henrik Abel a fourni des contre-exemples frappants (notamment avec les séries de Fourier de fonctions créneaux, qui présentent des sauts). L'erreur de Cauchy provenait d'une confusion entre la "convergence simple" (qui se vérifie point par point et ne préserve pas les propriétés globales comme la continuité) et la "convergence uniforme".

Karl Weierstrass, plus tard dans le siècle, a introduit la notion cruciale de **convergence normale**, un critère encore plus fort et souvent plus facile à manipuler en pratique. L'idée intuitive est la suivante : imaginez que chaque fonction de la somme soit une corde vibrante. La convergence normale signifie que l'amplitude maximale de chaque corde devient si petite, si rapidement, que la somme totale des amplitudes maximales est finie. Ainsi, la vibration globale reste "contrôlée" et lisse.

La nécessité d'intervertir des limites, des sommes, des intégrales et des dérivées est primordiale en analyse. Par exemple, si vous avez un signal représenté par une série infinie d'harmoniques, et que vous souhaitez mesurer l'énergie totale (intégrer) ou la vitesse de variation (dériver), vous voudriez idéalement le faire harmonique par harmonique. Les théorèmes d'interversion justifient quand nous avons le "droit" d'échanger l'ordre de ces opérations limites, évitant ainsi des paradoxes mathématiques où l'intégrale de la somme infinie diffère de la somme infinie des intégrales.

## 2. Protocole d'Exégèse Conceptuelle (Formalisation)

Soit $I \subset \mathbb{R}$ un intervalle, et $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions définies sur $I$ à valeurs dans $\mathbb{R}$ (ou $\mathbb{C}$).
On s'intéresse à la série de fonctions $\sum_{n=0}^\infty f_n$. On note $S_n(x) = \sum_{k=0}^n f_k(x)$ la somme partielle d'ordre $n$.

### 2.1. Convergence Simple (CS) et Uniforme (CU)

**A. Énoncé Symbolique Strict :**
1. La série $\sum f_n$ **converge simplement** sur $I$ si pour tout $x \in I$, la série numérique $\sum f_n(x)$ converge.
   On note alors $S(x) = \sum_{n=0}^\infty f_n(x)$ la fonction somme.
2. La série $\sum f_n$ **converge uniformément** sur $I$ si la suite de fonctions $(S_n)_{n \in \mathbb{N}}$ converge uniformément vers $S$ sur $I$. C'est-à-dire :
   $$ \forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in I, \left| \sum_{k=n+1}^\infty f_k(x) \right| \le \epsilon $$

**B. Anatomie et Typage Chirurgical :**
- $I$ est l'espace de base (typiquement un intervalle réel).
- $(f_n)$ est la suite de fonctions, la "matière première".
- $S_n : I \to \mathbb{R}$ est la fonction somme partielle.
- $S : I \to \mathbb{R}$ est la limite point par point.
- La définition de la convergence uniforme impose que le rang $N$ à partir duquel le reste de la série est petit soit le même pour **tous** les $x \in I$. L'ordre des quantificateurs $(\exists N, \forall x)$ est l'essence de la convergence uniforme.

**C. Exemples de Validation :**
- **Trivial :** $f_n(x) = x^n / 2^n$ sur $I = [-1, 1]$. La série $\sum (x/2)^n$ est une série géométrique de raison $q = x/2 \in [-1/2, 1/2]$. Elle converge simplement vers $1 / (1 - x/2)$. De plus, on verra qu'elle converge uniformément.
- **Complexe :** La série $\sum \frac{\sin(nx)}{n^2}$ converge uniformément sur $\mathbb{R}$, car le terme général est majoré par $1/n^2$ indépendamment de $x$.

**D. Cas Pathologiques et Contre-exemples :**
- $f_n(x) = x^n(1-x)$ sur $I = [0, 1]$. La série télescopique $\sum_{k=0}^n x^k(1-x) = \sum (x^k - x^{k+1}) = 1 - x^{n+1}$ (si $x \neq 1$) et 0 si $x=1$. Bien qu'elle converge simplement vers une fonction (différente de 0 en 1), la convergence n'est pas uniforme au voisinage de 1.

### 2.2. Convergence Normale (CN)

**A. Énoncé Symbolique Strict :**
On dit que la série de fonctions $\sum f_n$ **converge normalement** sur l'intervalle $I$ si :
1. Chaque fonction $f_n$ est bornée sur $I$, ce qui permet de définir la norme de la convergence uniforme $\|f_n\|_{\infty, I} = \sup_{x \in I} |f_n(x)|$.
2. La série numérique à termes positifs $\sum_{n \ge 0} \|f_n\|_{\infty, I}$ est convergente.

**B. Anatomie et Typage Chirurgical :**
- $\|f_n\|_{\infty, I}$ est un nombre réel positif représentant l'amplitude maximale absolue de $f_n$ sur $I$.
- La convergence normale réduit l'étude d'une série de fonctions à l'étude d'une **série numérique à termes positifs** (la série des bornes supérieures).

**C. Exemples de Validation :**
- La série $\sum_{n \ge 1} \frac{\sin(nx)}{n^2}$ converge normalement sur $\mathbb{R}$ car $\| \frac{\sin(nx)}{n^2} \|_{\infty, \mathbb{R}} = \frac{1}{n^2}$, et la série de Riemann $\sum \frac{1}{n^2}$ converge.

**D. Cas Pathologiques et Contre-exemples :**
- Une série peut converger uniformément sans converger normalement. Exemple célèbre : $f_n(x) = \frac{(-1)^n}{n+x}$ sur $I = [0, +\infty[$. Par le critère spécial des séries alternées, elle converge uniformément. Cependant, $\|f_n\|_{\infty, I} = \frac{1}{n}$, et la série harmonique $\sum \frac{1}{n}$ diverge, donc il n'y a pas convergence normale.

---

## 3. Démonstrations Zéro Ellipse

### Théorème 1 : Implications fondamentales des convergences

**Énoncé :** Si une série de fonctions $\sum f_n$ converge normalement sur $I$, alors elle converge uniformément sur $I$. Si elle converge uniformément sur $I$, alors elle converge simplement sur $I$. De plus, toute série normalement convergente est **absolument** convergente pour tout $x \in I$.

**Démonstration (CN $\implies$ CU) :**
Soit $\sum f_n$ une série de fonctions qui converge normalement sur $I$.
1. Soit $\epsilon > 0$.
2. Par hypothèse, la série numérique $\sum \|f_n\|_{\infty, I}$ converge.
3. Par le critère de Cauchy pour les séries numériques, il existe un entier $N \in \mathbb{N}$ tel que pour tout $q > p \ge N$,
   $$ \sum_{k=p+1}^q \|f_k\|_{\infty, I} \le \epsilon $$
4. Soit $x \in I$. Pour les mêmes indices $q > p \ge N$, on majore la valeur absolue de la tranche de Cauchy de la série de fonctions :
   $$ \left| \sum_{k=p+1}^q f_k(x) \right| \le \sum_{k=p+1}^q |f_k(x)| $$ (par l'inégalité triangulaire)
5. Par définition du supremum, pour tout $k$, on a $|f_k(x)| \le \|f_k\|_{\infty, I}$. Donc :
   $$ \sum_{k=p+1}^q |f_k(x)| \le \sum_{k=p+1}^q \|f_k\|_{\infty, I} \le \epsilon $$
6. On obtient ainsi que pour tout $x \in I$ et $q > p \ge N$, $\left| \sum_{k=p+1}^q f_k(x) \right| \le \epsilon$.
   La borne étant indépendante de $x$, la suite des sommes partielles vérifie le critère de Cauchy uniforme sur $I$.
7. L'espace des fonctions de $I$ dans $\mathbb{R}$ muni de la norme uniforme (sur l'espace des fonctions bornées) étant complet, ce critère de Cauchy uniforme implique la convergence uniforme de la série $\sum f_n$ sur $I$. $\blacksquare$

### Théorème 2 : Continuité de la fonction somme

**Énoncé :** Soit $\sum f_n$ une série de fonctions continues sur un intervalle $I$. Si la série $\sum f_n$ converge uniformément sur tout segment (ou uniformément sur $I$) vers une fonction $S$, alors $S$ est continue sur $I$.

**Démonstration :**
Il s'agit d'une application directe du théorème d'interversion des limites pour les suites de fonctions.
1. Fixons un point $a \in I$. Montrons que $S$ est continue en $a$.
2. On note $S_n(x) = \sum_{k=0}^n f_k(x)$. Comme somme finie de fonctions continues, $S_n$ est continue en $a$.
   Donc $\lim_{x \to a} S_n(x) = S_n(a)$.
3. Par hypothèse, la suite de fonctions $(S_n)$ converge uniformément vers $S$ sur un voisinage de $a$.
4. Le théorème d'interversion des doubles limites assure alors que :
   $$ \lim_{x \to a} S(x) = \lim_{x \to a} \left( \lim_{n \to \infty} S_n(x) \right) = \lim_{n \to \infty} \left( \lim_{x \to a} S_n(x) \right) = \lim_{n \to \infty} S_n(a) = S(a) $$
5. Donc $S$ est continue en $a$. Comme $a$ est arbitraire, $S$ est continue sur $I$. $\blacksquare$

### Théorème 3 : Interversion Limite-Intégrale (Théorème d'intégration terme à terme sur un segment)

**Énoncé :** Soit $(f_n)$ une suite de fonctions continues sur un segment $[a,b]$. Si la série $\sum f_n$ converge uniformément sur $[a,b]$ vers une fonction $S$, alors :
1. $S$ est continue (donc intégrable) sur $[a,b]$.
2. La série numérique $\sum \int_a^b f_n(t) \, dt$ converge.
3. L'intégrale de la somme est la somme des intégrales :
   $$ \int_a^b \left( \sum_{n=0}^\infty f_n(t) \right) \, dt = \sum_{n=0}^\infty \int_a^b f_n(t) \, dt $$

**Démonstration :**
1. La continuité de $S$ découle du Théorème 2. Ainsi l'intégrale $\int_a^b S(t) \, dt$ est bien définie.
2. Étudions la différence entre l'intégrale de la somme et la somme partielle des intégrales. Soit $S_n(t) = \sum_{k=0}^n f_k(t)$. Par linéarité de l'intégrale sur des sommes finies :
   $$ \sum_{k=0}^n \int_a^b f_k(t) \, dt = \int_a^b S_n(t) \, dt $$
3. Évaluons l'erreur :
   $$ \left| \int_a^b S(t) \, dt - \int_a^b S_n(t) \, dt \right| = \left| \int_a^b (S(t) - S_n(t)) \, dt \right| $$
4. Par la propriété de base de l'intégrale de Riemann, on majore l'intégrale de la valeur absolue :
   $$ \left| \int_a^b (S(t) - S_n(t)) \, dt \right| \le \int_a^b |S(t) - S_n(t)| \, dt $$
5. Or, par définition de la norme infinie, $|S(t) - S_n(t)| \le \|S - S_n\|_{\infty, [a,b]}$.
   Donc :
   $$ \int_a^b |S(t) - S_n(t)| \, dt \le \int_a^b \|S - S_n\|_{\infty, [a,b]} \, dt = \|S - S_n\|_{\infty, [a,b]} \cdot (b - a) $$
6. L'hypothèse de convergence uniforme de $\sum f_n$ signifie précisément que $\lim_{n \to \infty} \|S - S_n\|_{\infty, [a,b]} = 0$.
7. En passant à la limite quand $n \to \infty$ dans l'inégalité précédente, on obtient :
   $$ \lim_{n \to \infty} \left| \int_a^b S(t) \, dt - \sum_{k=0}^n \int_a^b f_k(t) \, dt \right| \le \lim_{n \to \infty} (b-a) \|S - S_n\|_{\infty, [a,b]} = 0 $$
8. Ce qui prouve exactement que la série numérique des intégrales converge et a pour limite l'intégrale de $S$. $\blacksquare$

### Théorème 4 : Interversion Limite-Dérivée (Théorème de dérivation terme à terme)

**Énoncé :** Soit $I$ un intervalle de $\mathbb{R}$. Soit $(f_n)$ une suite de fonctions de classe $\mathcal{C}^1$ sur $I$. Si :
1. Il existe un point $x_0 \in I$ tel que la série numérique $\sum f_n(x_0)$ converge.
2. La série des dérivées $\sum f_n'$ converge uniformément sur tout segment de $I$.
Alors, la série de fonctions $\sum f_n$ converge uniformément sur tout segment de $I$ vers une fonction $S$ qui est de classe $\mathcal{C}^1$ sur $I$, et on peut dériver terme à terme :
$$ \forall x \in I, \quad \left( \sum_{n=0}^\infty f_n \right)'(x) = \sum_{n=0}^\infty f_n'(x) $$

**Démonstration :**
1. La série $\sum f_n'$ est une série de fonctions continues (puisque les $f_n$ sont $\mathcal{C}^1$) qui converge uniformément sur tout segment. Soit $G(x) = \sum_{n=0}^\infty f_n'(x)$ sa fonction somme, qui est donc continue sur $I$ (par le Théorème 2).
2. Fixons $x \in I$. Appliquons le théorème fondamental de l'analyse (ou d'intégration terme à terme) sur le segment $[x_0, x]$ (ou $[x, x_0]$) aux sommes partielles. Pour chaque $n$, $f_n$ est $\mathcal{C}^1$, donc :
   $$ f_n(x) - f_n(x_0) = \int_{x_0}^x f_n'(t) \, dt $$
3. Par hypothèse (point 2), la série $\sum f_n'$ converge uniformément sur $[x_0, x]$. Par le théorème d'intégration terme à terme (Théorème 3), la série des intégrales converge et on peut sommer la relation :
   $$ \sum_{n=0}^\infty (f_n(x) - f_n(x_0)) = \int_{x_0}^x \left( \sum_{n=0}^\infty f_n'(t) \right) \, dt = \int_{x_0}^x G(t) \, dt $$
4. Or, par l'hypothèse (point 1), la série $\sum f_n(x_0)$ est convergente, disons vers une constante $C$.
   Donc, pour tout $x \in I$, la série $\sum f_n(x)$ converge. Notons $S(x)$ sa somme. On a :
   $$ S(x) - C = \int_{x_0}^x G(t) \, dt \implies S(x) = C + \int_{x_0}^x G(t) \, dt $$
5. $G$ étant une fonction continue sur $I$, le théorème fondamental de l'analyse implique que $x \mapsto \int_{x_0}^x G(t) \, dt$ est de classe $\mathcal{C}^1$ et a pour dérivée $G(x)$.
6. Ainsi, $S$ est de classe $\mathcal{C}^1$ sur $I$, et sa dérivée est :
   $$ S'(x) = G(x) = \sum_{n=0}^\infty f_n'(x) $$
   Ce qui démontre la relation. (La preuve de la convergence uniforme de $\sum f_n$ sur tout segment découle du fait que $f_n(x) = f_n(x_0) + \int_{x_0}^x f_n'(t) dt$ et de la majoration de l'intégrale par la norme infinie de $f_n'$, détail laissé sans ellipse en soulignant que $\| \int_{x_0}^x f_n'(t) dt \| \le |x-x_0| \|f_n'\|_\infty$, ce qui prouve la CU). $\blacksquare$
