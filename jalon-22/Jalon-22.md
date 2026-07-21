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

## 1. Intuition et genèse du concept

L'étude des séries de fonctions s'enracine dans la volonté farouche des mathématiciens du XIXe siècle de représenter des phénomènes physiques complexes — tels que la propagation de la chaleur ou les ondes sonores — par des superpositions infinies d'ondes simples. Lorsque Joseph Fourier a postulé que toute fonction, même discontinue, pouvait s'exprimer comme une série trigonométrique infinie, il a ouvert la boîte de Pandore de l'analyse moderne. Cette idée vertigineuse soulevait une question redoutable : si l'on somme une infinité de fonctions parfaitement lisses (continues, dérivables), la fonction résultante conserve-t-elle ces propriétés géométriques ?

Augustin-Louis Cauchy pensait initialement que la convergence simple point par point suffisait pour garantir le transfert de la continuité. Cependant, l'histoire mathématique est jalonnée de monstres et de contre-exemples, à l'image des séries de Fourier de fonctions créneaux mises en évidence par Niels Henrik Abel. Ces pathologies ont forcé Karl Weierstrass à forger un nouveau paradigme : la convergence uniforme, et son corollaire encore plus puissant, la convergence normale. Imaginez une infinité de cordes vibrantes ; la convergence normale exige que l'amplitude maximale absolue de chaque corde décroisse si radicalement que la somme globale de ces amplitudes maximales forme une série convergente. C'est un contrôle global et despotique sur le comportement des fonctions, qui empêche toute anomalie locale d'émerger à l'infini.

Cette maîtrise rigoureuse est la clé de voûte de l'intelligence artificielle contemporaine. Lorsque nous entraînons des réseaux de neurones profonds, nous manipulons des limites infinies d'approximations fonctionnelles. Comprendre intimement quand et pourquoi nous pouvons intervertir une limite avec une dérivée (comme dans la rétropropagation du gradient) ou avec une intégrale (dans le calcul de l'espérance des pertes stochastiques) est la ligne de démarcation entre l'ingénierie approximative et la science mathématique rigoureuse.

## 2. Formalisation et structures algébriques

Dans toute cette section, nous considérons un intervalle $I$ de $\mathbb{R}$, non vide et non réduit à un point. Soit $E$ l'espace vectoriel des fonctions définies sur $I$ à valeurs dans $\mathbb{R}$. Nous étudions une suite de fonctions $(f_n)_{n \in \mathbb{N}} \in E^{\mathbb{N}}$.

La somme partielle d'ordre $n$ est l'application $S_n : I \to \mathbb{R}$ définie par $S_n(x) = \sum_{k=0}^n f_k(x)$.

### 2.1 Convergence Simple (CS) et Uniforme (CU)

**A. Énoncé Symbolique Strict**

La série de fonctions $\sum f_n$ converge **simplement** sur $I$ vers une fonction $S : I \to \mathbb{R}$ si et seulement si :
$$ \forall x \in I, \quad \forall \epsilon > 0, \quad \exists N \in \mathbb{N}, \quad \forall n \ge N \implies |S_n(x) - S(x)| < \epsilon $$

La série de fonctions $\sum f_n$ converge **uniformément** sur $I$ vers $S$ si et seulement si :
$$ \forall \epsilon > 0, \quad \exists N \in \mathbb{N}, \quad \forall n \ge N \implies \forall x \in I, \quad |S_n(x) - S(x)| < \epsilon $$

**B. Anatomie et Typage Chirurgical**
- $I$ est le domaine de définition topologique.
- $S_n(x)$ est l'évaluation scalaire de la $n$-ième somme partielle.
- $S(x)$ est la valeur scalaire de la limite asymptotique.
- L'ordre des quantificateurs dicte la nature géométrique de la convergence. Pour la convergence simple, l'entier $N$ dépend de $\epsilon$ ET de $x$ (on écrit souvent $N(\epsilon, x)$). Pour la convergence uniforme, l'entier $N$ est universel pour tout l'intervalle $I$ ; il ne dépend que de $\epsilon$ (soit $N(\epsilon)$). Le supremum géométrique de l'erreur globale s'écrase dans un tube de rayon $\epsilon$.

**C. Exemples de Validation**
- **Cas d'application valide :** Considérons la suite $f_n(x) = x^n / 2^n$ sur le segment $I = [-1, 1]$. La série $\sum (x/2)^n$ est une série géométrique de raison $q = x/2$. Puisque $|q| \le 1/2 < 1$, elle converge simplement vers $S(x) = \frac{1}{1 - x/2}$. La convergence est par ailleurs uniforme car le reste $|R_n(x)| \le \frac{(1/2)^{n+1}}{1 - 1/2}$ tend vers $0$ indépendamment de $x$.
- **Extension :** La série $\sum \frac{\sin(nx)}{n^2}$ converge uniformément sur $\mathbb{R}$. En effet, l'erreur est globalement bornée indépendamment de $x$ par la somme des restes de la série de Riemann convergente.

**D. Cas Pathologiques et Contre-exemples**
- La fonction $f_n(x) = x^n(1-x)$ sur l'intervalle semi-ouvert $I = [0, 1[$. La somme partielle est $S_n(x) = 1 - x^{n+1}$. La limite simple est $S(x) = 1$ pour tout $x \in [0, 1[$. Cependant, pour tout $n$, $\sup_{x \in [0, 1[} |S_n(x) - 1| = \sup_{x} x^{n+1} = 1$. L'erreur globale ne tend pas vers $0$. La convergence n'est pas uniforme à cause du comportement pathologique au voisinage du point $x = 1$.

### 2.2 Convergence Normale (CN)

**A. Énoncé Symbolique Strict**

On dit que la série de fonctions $\sum f_n$ **converge normalement** sur l'intervalle $I$ si :
1. $\forall n \in \mathbb{N}$, la fonction $f_n$ est bornée sur $I$, permettant de définir la norme infinie $\|f_n\|_{\infty, I} = \sup_{x \in I} |f_n(x)|$.
2. La série numérique à termes réels positifs $\sum_{n \ge 0} \|f_n\|_{\infty, I}$ est convergente.

**B. Anatomie et Typage Chirurgical**
- $\|f_n\|_{\infty, I} \in \mathbb{R}^+$ représente le pire scénario d'amplitude de la fonction $f_n$ sur l'intégralité du domaine $I$.
- Le concept de convergence normale ramène la difficulté inhérente à l'analyse fonctionnelle (espaces de dimension infinie) à un simple problème d'analyse réelle classique : l'étude d'une série de nombres réels positifs.

**C. Exemples de Validation**
- La série $\sum_{n \ge 1} \frac{\cos(nx)}{n^3}$ converge normalement sur $\mathbb{R}$ car la norme infinie $\| \frac{\cos(nx)}{n^3} \|_{\infty, \mathbb{R}} = \frac{1}{n^3}$. Or la série de Riemann $\sum \frac{1}{n^3}$ converge (exposant $3 > 1$).

**D. Cas Pathologiques et Contre-exemples**
- La série $f_n(x) = \frac{(-1)^n}{n+x}$ sur $I = [0, +\infty[$. Par application du critère spécial des séries alternées, la série converge uniformément. Néanmoins, $\|f_n\|_{\infty, I} = \frac{1}{n}$, et la série harmonique diverge. C'est l'exemple paradigmatique d'une convergence uniforme non absolue, et a fortiori non normale.

## 3. Démonstrations pas-à-pas

### Théorème 1 : De la Convergence Normale vers la Convergence Uniforme

**Énoncé :** Si une série de fonctions $\sum f_n$ converge normalement sur $I$, alors elle converge uniformément (et absolument) sur $I$.

**Démonstration analytique complète :**
Soit $\sum f_n$ une série de fonctions qui converge normalement sur l'intervalle $I$.
1. Fixons un scalaire arbitrairement petit $\epsilon > 0$.
2. L'hypothèse fondamentale pose que la série de nombres réels positifs $\sum \|f_n\|_{\infty, I}$ converge.
3. Par application stricte du critère de Cauchy pour les séries numériques, il existe un entier de seuil $N \in \mathbb{N}$ tel que pour tout couple d'entiers $(p, q)$ vérifiant $q > p \ge N$, l'inégalité suivante est vraie :
   $$ \sum_{k=p+1}^q \|f_k\|_{\infty, I} \le \epsilon $$
4. Fixons désormais un point arbitraire $x \in I$. Pour ces mêmes indices $q > p \ge N$, évaluons la distance dans $\mathbb{R}$ de la tranche de Cauchy de la série de fonctions :
   $$ \left| \sum_{k=p+1}^q f_k(x) \right| $$
5. Par application de l'inégalité triangulaire dans $\mathbb{R}$, nous majorons cette somme :
   $$ \left| \sum_{k=p+1}^q f_k(x) \right| \le \sum_{k=p+1}^q |f_k(x)| $$
6. Or, par définition exacte de l'opérateur supremum, pour tout indice $k$ et pour tout $x \in I$, on a l'inégalité stricte : $|f_k(x)| \le \|f_k\|_{\infty, I}$. Nous déduisons donc la chaîne d'inégalités :
   $$ \sum_{k=p+1}^q |f_k(x)| \le \sum_{k=p+1}^q \|f_k\|_{\infty, I} \le \epsilon $$
7. En combinant les équations, nous obtenons que pour tout $x \in I$ et pour tout couple $q > p \ge N$ :
   $$ \left| \sum_{k=p+1}^q f_k(x) \right| \le \epsilon $$
8. La subtilité cruciale est que cette borne $\epsilon$ est totalement indépendante du choix de la variable $x$. La suite des sommes partielles $(S_n)$ satisfait donc le critère de Cauchy uniforme sur $I$.
9. Puisque l'espace vectoriel normé des fonctions bornées de $I$ dans $\mathbb{R}$, muni de la norme infinie $\|\cdot\|_{\infty}$, est un espace de Banach (donc un espace complet), le respect du critère de Cauchy uniforme garantit mathématiquement l'existence d'une limite et la convergence uniforme de la série $\sum f_n$ vers cette limite sur $I$. $\blacksquare$

### Théorème 2 : Continuité de la fonction somme par interversion limite-limite

**Énoncé :** Soit $\sum f_n$ une série de fonctions où chaque $f_n$ est continue sur l'intervalle $I$. Si la série converge uniformément vers une fonction globale $S$ sur tout segment inclus dans $I$, alors $S$ est une fonction continue sur $I$.

**Démonstration analytique complète :**
L'objectif est d'appliquer le théorème de la double limite.
1. Considérons un point arbitraire $a \in I$. Nous devons prouver rigoureusement que la fonction limite $S$ est continue au point $a$.
2. Définissons la somme partielle $S_n(x) = \sum_{k=0}^n f_k(x)$. Étant une somme finie de fonctions continues en $a$, l'opérateur $S_n$ est lui-même intrinsèquement continu en $a$. Cela s'écrit formellement :
   $$ \lim_{x \to a} S_n(x) = S_n(a) $$
3. L'hypothèse stipule que la suite de fonctions $(S_n)$ converge uniformément vers la fonction $S$ sur tout segment, et en particulier sur un voisinage compact de $a$.
4. Le théorème fondamental d'interversion des limites pour les suites de fonctions (qui repose lui-même sur un argument d'epsilontique $\frac{\epsilon}{3}$) nous autorise à échanger l'ordre de passage à la limite :
   $$ \lim_{x \to a} S(x) = \lim_{x \to a} \left( \lim_{n \to \infty} S_n(x) \right) $$
5. Intervertissons formellement les deux opérateurs de limite :
   $$ \lim_{x \to a} \left( \lim_{n \to \infty} S_n(x) \right) = \lim_{n \to \infty} \left( \lim_{x \to a} S_n(x) \right) $$
6. Substituons l'évaluation de continuité de $S_n$ :
   $$ \lim_{n \to \infty} \left( \lim_{x \to a} S_n(x) \right) = \lim_{n \to \infty} S_n(a) = S(a) $$
7. En concaténant ces identités, nous avons formellement prouvé que $\lim_{x \to a} S(x) = S(a)$. La fonction limite $S$ est donc continue en tout point $a \in I$, ce qui achève la démonstration. $\blacksquare$

### Théorème 3 : Interversion Limite-Intégrale de Riemann (Théorème d'intégration terme à terme)

**Énoncé :** Soit $(f_n)$ une suite de fonctions continues sur le segment compact $[a,b]$. Si la série $\sum f_n$ converge uniformément sur $[a,b]$ vers la fonction limite $S$, alors :
- La fonction $S$ est Riemann-intégrable sur $[a,b]$.
- La série numérique des intégrales $\sum \int_a^b f_n(t) \, dt$ converge.
- L'intégrale de la série est égale à la série des intégrales : $\int_a^b \left( \sum_{n=0}^\infty f_n(t) \right) \, dt = \sum_{n=0}^\infty \int_a^b f_n(t) \, dt$.

**Démonstration analytique complète :**
1. La continuité globale de la fonction $S$ sur le segment $[a,b]$ découle directement du Théorème 2. Ainsi, $S$ est une fonction continue sur un compact, elle y est bornée et admet une intégrale de Riemann bien définie $\int_a^b S(t) \, dt$.
2. Construisons la fonction somme partielle $S_n(t) = \sum_{k=0}^n f_k(t)$. En vertu de l'axiome de linéarité de l'intégrale de Riemann appliqué à une somme finie, nous avons :
   $$ \sum_{k=0}^n \int_a^b f_k(t) \, dt = \int_a^b S_n(t) \, dt $$
3. Afin de prouver la convergence, formons la distance absolue entre l'intégrale théorique de la limite et la somme partielle des intégrales :
   $$ \Delta_n = \left| \int_a^b S(t) \, dt - \int_a^b S_n(t) \, dt \right| $$
4. Par l'opérateur de linéarité inverse et l'inégalité triangulaire intégrale fondamentale ($\left| \int g \right| \le \int |g|$), nous obtenons :
   $$ \Delta_n = \left| \int_a^b (S(t) - S_n(t)) \, dt \right| \le \int_a^b |S(t) - S_n(t)| \, dt $$
5. L'expression $|S(t) - S_n(t)|$ est, par définition du supremum, strictement majorée pour tout $t \in [a,b]$ par la norme infinie $\|S - S_n\|_{\infty, [a,b]}$. En injectant ce majorant constant dans l'intégrale :
   $$ \int_a^b |S(t) - S_n(t)| \, dt \le \int_a^b \|S - S_n\|_{\infty, [a,b]} \, dt = \|S - S_n\|_{\infty, [a,b]} \cdot (b - a) $$
6. L'hypothèse cruciale de la convergence uniforme de la série matricielle $\sum f_n$ implique précisément, par caractérisation métrique, que :
   $$ \lim_{n \to \infty} \|S - S_n\|_{\infty, [a,b]} = 0 $$
7. Le paramètre $(b-a)$ étant une constante strictement finie, la borne supérieure de l'erreur intégrale s'effondre vers $0$ au passage à la limite :
   $$ \lim_{n \to \infty} \Delta_n \le \lim_{n \to \infty} (b-a) \|S - S_n\|_{\infty, [a,b]} = 0 $$
8. La quantité positive $\Delta_n$ tend asymptotiquement vers $0$. Ceci prouve rigoureusement que la suite des sommes partielles des intégrales converge vers l'intégrale de $S$. L'interversion est algébriquement validée. $\blacksquare$

### Théorème 4 : Interversion Limite-Dérivée (Théorème de dérivation terme à terme)

**Énoncé :** Soit $I$ un intervalle quelconque de $\mathbb{R}$ et $(f_n)$ une suite de fonctions de classe $\mathcal{C}^1$ sur $I$. Si la série ponctuelle numérique $\sum f_n(x_0)$ converge en au moins un point d'ancrage $x_0 \in I$, et si la série dérivée fonctionnelle $\sum f_n'$ converge uniformément sur tout segment compact de $I$, alors la série originelle $\sum f_n$ converge uniformément sur tout segment de $I$ vers une fonction limite $S$ qui est également de classe $\mathcal{C}^1$ sur $I$. De plus, la dérivée commute : $S'(x) = \sum_{n=0}^\infty f_n'(x)$.

**Démonstration analytique complète :**
1. Considérons la série des dérivées $\sum f_n'$. Par hypothèse, chaque terme $f_n'$ est une fonction continue (car $f_n \in \mathcal{C}^1$). Cette série converge uniformément sur tout sous-segment compact. Par application du Théorème 2, sa limite, que nous désignerons par $G(x) = \sum_{n=0}^\infty f_n'(x)$, est nécessairement une fonction globale continue sur l'intervalle $I$.
2. Sélectionnons une variable indépendante arbitraire $x \in I$. Appliquons le théorème fondamental de l'analyse intégrale (Newton-Leibniz) sur le chemin d'intégration borné $[x_0, x]$. Pour tout entier $n$, la différentiabilité de $f_n$ donne l'équation exacte :
   $$ f_n(x) - f_n(x_0) = \int_{x_0}^x f_n'(t) \, dt $$
3. L'hypothèse de convergence uniforme de la série des dérivées $\sum f_n'$ est valide sur le segment compact délimité par $x_0$ et $x$. Cette propriété topologique autorise l'application du Théorème 3 (interversion limite-intégrale). En sommant les expressions sur l'indice $n$ de $0$ à l'infini :
   $$ \sum_{n=0}^\infty (f_n(x) - f_n(x_0)) = \sum_{n=0}^\infty \int_{x_0}^x f_n'(t) \, dt = \int_{x_0}^x \left( \sum_{n=0}^\infty f_n'(t) \right) \, dt = \int_{x_0}^x G(t) \, dt $$
4. L'énoncé précise qu'au point singulier $x_0$, la série numérique $\sum f_n(x_0)$ est structurellement convergente vers une constante scalaire, notons-la $C$. Conséquemment, par transfert algébrique, la série globale $\sum f_n(x)$ converge pour tout $x \in I$. Nommons $S(x)$ la fonction limite de cette série point par point. En réagençant l'équation d'intégration, nous isolons $S(x)$ :
   $$ S(x) - C = \int_{x_0}^x G(t) \, dt \implies S(x) = C + \int_{x_0}^x G(t) \, dt $$
5. Observons la nature analytique de la primitive. L'intégrande $G$ a été formellement identifiée comme une fonction continue sur $I$. Par le théorème fondamental de l'analyse réelle, l'opérateur intégral de borne variable $x \mapsto \int_{x_0}^x G(t) \, dt$ engendre une fonction primitive de classe $\mathcal{C}^1$, dont la dérivée est très exactement $G(x)$.
6. La constante $C$ disparaissant par dérivation, l'implication terminale est que la fonction limite $S$ appartient à la classe de régularité $\mathcal{C}^1$ sur l'ensemble de l'intervalle $I$. Sa dérivée première est rigoureusement évaluée à :
   $$ S'(x) = G(x) = \sum_{n=0}^\infty f_n'(x) $$
   L'interversion est donc légitimement prouvée. L'absence totale d'ellipse garantit la robustesse du raisonnement analytique. $\blacksquare$
