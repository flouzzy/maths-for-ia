---
uuid: "jalon-77"
title: "Densité dans Lp"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]"
next: "[[Jalon 78 (Séries de Fourier).md]]"
---

# Jalon 77 : Densité des fonctions simples dans $L^p$

## 1. Introduction à la Densité dans les Espaces de Lebesgue

L'analyse fonctionnelle moderne, particulièrement depuis les travaux fondateurs d'Henri Lebesgue et de Frigyes Riesz au début du XXe siècle, traite d'espaces de fonctions dont les éléments peuvent présenter des comportements extrêmement pathologiques : singularités, oscillations infinies, ou absences totales de continuité. L'espace $L^p(\mu)$, qui regroupe les fonctions dont la puissance $p$-ième est intégrable, est le cadre naturel de la physique quantique (avec $L^2$) et des probabilités. Cependant, manipuler directement de telles fonctions, qui ne sont définies que presque partout, s'avère souvent délicat.

C'est ici qu'intervient la notion de densité. L'idée est géométrique : tout comme n'importe quel nombre réel peut être approché d'aussi près que l'on veut par un nombre rationnel (densité de $\mathbb{Q}$ dans $\mathbb{R}$), toute fonction compliquée de $L^p$ peut être approximée par des fonctions "simples" ou "lisses". Ces fonctions régulières (fonctions étagées, continues, infiniment dérivables) forment une ossature sur laquelle on peut asseoir les démonstrations. On établit d'abord une propriété (une inégalité, une convergence) sur cet ensemble restreint, plus commode à manipuler, puis on l'étend à tout l'espace $L^p$ par passage à la limite, grâce à la densité. Ce principe d'extension continue est le moteur principal de l'analyse dans les espaces de Banach.

## 2. Définitions et Théorèmes de Densité

### Densité des Fonctions Étagées Intégrables

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $p \in [1, +\infty[$.
On note $\mathcal{E}$ l'espace vectoriel des fonctions étagées (ou simples), c'est-à-dire les fonctions de la forme $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}$ où les $\alpha_i \in \mathbb{R}$ (ou $\mathbb{C}$) et les $A_i \in \mathcal{A}$ sont deux à deux disjoints. On désigne par $\mathcal{E} \cap L^p(\mu)$ le sous-espace des fonctions étagées appartenant à $L^p(\mu)$ (ce qui équivaut à exiger que $\mu(A_i) < +\infty$ dès que $\alpha_i \neq 0$).

**Théorème 1 (Densité des fonctions étagées).**
Pour tout $p \in [1, +\infty[$, l'espace $\mathcal{E} \cap L^p(\mu)$ est dense dans $L^p(\mu)$.
Formellement :
$$ \forall f \in L^p(\mu), \forall \varepsilon > 0, \exists s \in \mathcal{E} \cap L^p(\mu) \text{ tel que } \|f - s\|_p < \varepsilon. $$

**Exemple Concret :**
Soit $f(x) = \frac{1}{\sqrt{x}}$ sur $]0, 1]$, et $f(0) = 0$. Montrons que $f \in L^1(]0, 1])$ et approchons-la par une fonction étagée.
L'intégrale vaut $\int_0^1 x^{-1/2} dx = [2\sqrt{x}]_0^1 = 2 < +\infty$.
Construisons une approximation $s$. Coupons $]0, 1]$ en deux : $A_1 = ]1/4, 1]$ et $A_2 = ]0, 1/4]$.
Sur $A_1$, $f(x)$ varie de $1$ à $2$. Posons $s(x) = 1$ sur $A_1$.
Sur $A_2$, $f(x)$ varie de $2$ à $+\infty$. Posons $s(x) = 2$ sur $A_2$.
$s = \mathbf{1}_{]1/4, 1]} + 2 \cdot \mathbf{1}_{]0, 1/4]}$.
L'erreur $L^1$ est :
$$ \|f - s\|_1 = \int_0^{1/4} \left|\frac{1}{\sqrt{x}} - 2\right| dx + \int_{1/4}^1 \left|\frac{1}{\sqrt{x}} - 1\right| dx $$
$$ = \left( [2\sqrt{x}]_0^{1/4} - 2(1/4) \right) + \left( [2\sqrt{x}]_{1/4}^1 - (1-1/4) \right) = (1 - 0.5) + (2 - 1 - 0.75) = 0.5 + 0.25 = 0.75 $$
En raffinant la partition, on peut rendre $\|f - s\|_1$ arbitrairement petit.

### Densité des Fonctions Continues à Support Compact (Cas de la mesure de Lebesgue)

Plaçons-nous maintenant dans l'espace $\mathbb{R}^d$ muni de la tribu borélienne et de la mesure de Lebesgue $\lambda$. Soit $\mathcal{C}_c(\mathbb{R}^d)$ l'espace des fonctions continues à support compact.

**Théorème 2 (Densité des fonctions continues).**
Pour tout $p \in [1, +\infty[$, l'espace $\mathcal{C}_c(\mathbb{R}^d)$ est dense dans $L^p(\mathbb{R}^d)$.

**Exemple Concret :**
Soit $f = \mathbf{1}_{[0, 1]}$. C'est une fonction de $L^1(\mathbb{R})$. Elle n'est pas continue (sauts en $0$ et $1$).
Approchons-la par $g_n \in \mathcal{C}_c(\mathbb{R})$ définie par :
$g_n(x) = 1$ si $x \in [0, 1]$.
$g_n(x) = 1 + n x$ si $x \in [-1/n, 0]$.
$g_n(x) = 1 - n (x-1)$ si $x \in [1, 1+1/n]$.
$g_n(x) = 0$ ailleurs.
$g_n$ est un "trapèze" qui encadre l'indicatrice.
L'erreur $L^1$ est la surface des deux petits triangles ajoutés :
$$ \|f - g_n\|_1 = \int_{-1/n}^0 (1+nx) dx + \int_1^{1+1/n} (1-n(x-1)) dx = \frac{1}{2n} + \frac{1}{2n} = \frac{1}{n} $$
Pour $\varepsilon > 0$, il suffit de choisir $n > 1/\varepsilon$ pour obtenir $\|f - g_n\|_1 < \varepsilon$.

**Contre-exemple (Cas pathologique $p = \infty$) :**
Le théorème est **faux** pour $p = \infty$.
Soit $f = \mathbf{1}_{[0, 1]}$. Si $\mathcal{C}_c$ était dense dans $L^\infty$, il existerait $g \in \mathcal{C}_c$ telle que $\|f - g\|_\infty < 1/3$.
Cela impliquerait $|g(x) - 1| < 1/3$ presque partout sur $[0, 1]$ et $|g(x)| < 1/3$ presque partout sur $\mathbb{R} \setminus [0, 1]$.
Par continuité de $g$, $g(0)$ devrait satisfaire à la fois $|g(0) - 1| \le 1/3$ (donc $g(0) \ge 2/3$) et $|g(0)| \le 1/3$. C'est une contradiction. Donc l'indicatrice ne peut être approchée uniformément par une fonction continue. L'adhérence de $\mathcal{C}_c$ dans $L^\infty$ est l'espace $\mathcal{C}_0$ des fonctions continues qui tendent vers $0$ à l'infini, qui est strictement inclus dans $L^\infty$.

## 3. Démonstrations Complètes

### Démonstration du Théorème 1 : Densité des fonctions étagées

On procède par étapes pour montrer la densité dans $L^p(\mu)$.

**Étape 1 : Le cas des fonctions positives mesurables**
Soit $f \in L^p(\mu)$ telle que $f(x) \ge 0$ pour presque tout $x$.
Par le théorème d'approximation mesurable (Jalon 65), il existe une suite croissante $(s_n)_{n \in \mathbb{N}}$ de fonctions étagées positives convergeant simplement vers $f$ :
$$ \forall x \in X, \quad 0 \le s_1(x) \le s_2(x) \le \dots \le f(x) \quad \text{et} \quad \lim_{n \to \infty} s_n(x) = f(x). $$
Puisque $0 \le s_n \le f$ et $f \in L^p$, on a $s_n^p \le f^p$. En intégrant, $\int s_n^p d\mu \le \int f^p d\mu < +\infty$, donc chaque $s_n$ appartient à $\mathcal{E} \cap L^p(\mu)$.

**Étape 2 : Convergence dans $L^p$ par le TCD**
On souhaite montrer que $\|f - s_n\|_p \to 0$.
Considérons la suite de fonctions $g_n = (f - s_n)^p$.
- Convergence ponctuelle : $\lim_{n \to \infty} g_n(x) = (f(x) - f(x))^p = 0$ partout.
- Domination : On a $0 \le s_n \le f$, donc $0 \le f - s_n \le f$.
  Ainsi, $|g_n| = (f - s_n)^p \le f^p$.
  La fonction dominante $f^p$ est intégrable car $f \in L^p(\mu)$.
D'après le Théorème de Convergence Dominée (TCD), on peut intervertir la limite et l'intégrale :
$$ \lim_{n \to \infty} \int_X (f - s_n)^p d\mu = \int_X 0 \, d\mu = 0. $$
Ce qui signifie exactement que $\|f - s_n\|_p \to 0$.

**Étape 3 : Cas général d'une fonction à valeurs réelles**
Soit $f \in L^p(\mu)$. On décompose $f$ en ses parties positive et négative : $f = f^+ - f^-$, où $f^+ = \max(f, 0)$ et $f^- = \max(-f, 0)$.
Comme $|f^+| \le |f|$ et $|f^-| \le |f|$, on a $f^+, f^- \in L^p(\mu)$.
D'après l'Étape 2, il existe des suites d'étagées $s_n^{(+)}$ et $s_n^{(-)}$ telles que $\|f^+ - s_n^{(+)}\|_p \to 0$ et $\|f^- - s_n^{(-)}\|_p \to 0$.
Posons $s_n = s_n^{(+)} - s_n^{(-)}$. La fonction $s_n$ est étagée et appartient à $L^p$.
Par l'inégalité de Minkowski (inégalité triangulaire de la norme $L^p$) :
$$ \|f - s_n\|_p = \|(f^+ - f^-) - (s_n^{(+)} - s_n^{(-)})\|_p \le \|f^+ - s_n^{(+)}\|_p + \|f^- - s_n^{(-)}\|_p. $$
Cette somme tend vers $0$ quand $n \to \infty$.

**Étape 4 : Cas complexe**
Si $f$ est à valeurs complexes, on applique le même raisonnement aux parties réelle et imaginaire $f = \text{Re}(f) + i\text{Im}(f)$.
La densité de $\mathcal{E} \cap L^p$ est donc démontrée en toute généralité. $\blacksquare$

### Démonstration du Théorème 2 : Densité des fonctions continues

La preuve procède par approximations successives, justifiées rigoureusement.

**Étape 1 : Réduction à une fonction indicatrice d'un ensemble de mesure finie**
Par le Théorème 1, les fonctions étagées intégrables sont denses dans $L^p(\mathbb{R}^d)$.
Ainsi, pour $f \in L^p(\mathbb{R}^d)$ et $\varepsilon > 0$, il existe une fonction étagée $s = \sum_{k=1}^m \alpha_k \mathbf{1}_{A_k}$ (où les $A_k$ sont disjoints et de mesure finie) telle que $\|f - s\|_p \le \frac{\varepsilon}{3}$.
Par l'inégalité triangulaire de la norme $L^p$ (Minkowski), si nous pouvons approcher chaque indicatrice $\mathbf{1}_{A_k}$ par une fonction continue à support compact $g_k$ telle que $\|\mathbf{1}_{A_k} - g_k\|_p \le \frac{\varepsilon}{3m|\alpha_k|}$, alors la fonction $g = \sum_{k=1}^m \alpha_k g_k$ sera continue à support compact et vérifiera $\|s - g\|_p \le \sum_{k=1}^m |\alpha_k| \|\mathbf{1}_{A_k} - g_k\|_p \le \frac{\varepsilon}{3}$.
Finalement, $\|f - g\|_p \le \|f - s\|_p + \|s - g\|_p \le \frac{2\varepsilon}{3} < \varepsilon$.
Il suffit donc de prouver le théorème pour $f = \mathbf{1}_A$ avec $\lambda(A) < +\infty$.

**Étape 2 : Régularité de la mesure de Lebesgue et approximation par un ouvert et un compact**
La mesure de Lebesgue sur $\mathbb{R}^d$ est régulière. Pour tout ensemble mesurable $A$ tel que $\lambda(A) < +\infty$, et pour tout $\eta > 0$, il existe un compact $K$ et un ouvert $U$ tels que $K \subset A \subset U$ et $\lambda(U \setminus K) < \eta$.
Choisissons $\eta = \left( \frac{\varepsilon}{3m|\alpha_k|} \right)^p$. Nous avons donc $K \subset A \subset U$ avec $\lambda(U \setminus K) < \eta$.

**Étape 3 : Construction de la fonction continue (Lemme d'Urysohn pour $\mathbb{R}^d$)**
Puisque $K$ est compact et $U$ est ouvert (donc $U^c$ est fermé), et que $K \cap U^c = \emptyset$, la distance entre $K$ et $U^c$, définie par $d(K, U^c) = \inf_{x \in K, y \in U^c} \|x - y\|$, est strictement positive car $K$ est compact.
Définissons la fonction $g(x)$ par :
$$ g(x) = \frac{d(x, U^c)}{d(x, K) + d(x, U^c)} $$
Cette fonction est continue car la fonction distance à un ensemble est lipschitzienne (donc continue).
Évaluons ses valeurs :
- Si $x \in K$, $d(x, K) = 0$, donc $g(x) = 1$.
- Si $x \in U^c$, $d(x, U^c) = 0$, donc $g(x) = 0$.
- Pour tout $x \in \mathbb{R}^d$, $0 \le g(x) \le 1$.
Le support de $g$ est inclus dans l'adhérence de $U$. Puisque $K$ est compact, on peut choisir $U$ borné, de sorte que $\bar{U}$ est compact. Ainsi, $g$ est continue à support compact : $g \in \mathcal{C}_c(\mathbb{R}^d)$.

**Étape 4 : Calcul de l'erreur d'approximation $L^p$**
Nous devons évaluer $\|\mathbf{1}_A - g\|_p$.
Observons que :
- Sur $K$, $\mathbf{1}_A(x) = 1$ et $g(x) = 1$, donc $\mathbf{1}_A(x) - g(x) = 0$.
- Sur $U^c$, $\mathbf{1}_A(x) = 0$ (car $A \subset U$) et $g(x) = 0$, donc $\mathbf{1}_A(x) - g(x) = 0$.
Ainsi, la fonction $\mathbf{1}_A - g$ est non nulle uniquement sur l'ensemble $U \setminus K$.
De plus, $|\mathbf{1}_A(x) - g(x)| \le 1$ pour tout $x$.
Par conséquent,
$$ \|\mathbf{1}_A - g\|_p^p = \int_{\mathbb{R}^d} |\mathbf{1}_A(x) - g(x)|^p dx = \int_{U \setminus K} |\mathbf{1}_A(x) - g(x)|^p dx \le \int_{U \setminus K} 1^p dx = \lambda(U \setminus K). $$
Comme nous avons choisi $\lambda(U \setminus K) < \eta$, il s'ensuit que $\|\mathbf{1}_A - g\|_p < \eta^{1/p} = \frac{\varepsilon}{3m|\alpha_k|}$.
Ceci achève la démonstration rigoureuse de la densité de $\mathcal{C}_c(\mathbb{R}^d)$ dans $L^p(\mathbb{R}^d)$. $\blacksquare$

## 4. Applications en Physique, Logique et Intelligence Artificielle

### Convolution et Régularisation
En physique du signal, on convolutionne souvent un signal bruité $f \in L^p$ avec une famille de fonctions "molles" (mollifiers) infiniment dérivables, comme une gaussienne $G_\sigma$.
On montre que le produit de convolution $f * G_\sigma$ est une fonction de classe $\mathcal{C}^\infty$, et par un théorème fondamental de densité, $\|f - f * G_\sigma\|_p \to 0$ lorsque $\sigma \to 0$. Cela permet de lisser n'importe quelle fonction $L^p$, ce qui est crucial pour la résolution des EDP (Équations aux Dérivées Partielles) comme l'équation de la chaleur.

### Intelligence Artificielle et Théorème d'Approximation Universelle
Le célèbre théorème d'approximation universelle stipule qu'un réseau de neurones avec une seule couche cachée, utilisant des fonctions d'activation non polynomiales (comme ReLU ou Sigmoïde), peut approximer n'importe quelle fonction continue sur un compact avec une erreur arbitrairement petite (dans l'espace des fonctions continues).
Puisque les fonctions continues sont elles-mêmes denses dans $L^p(\mathbb{R}^d)$ par rapport aux mesures de probabilité régulières, un réseau de neurones est en réalité un approximateur universel pour **toute fonction mesurable de $L^p$**. C'est le fondement théorique absolu justifiant pourquoi l'apprentissage profond (Deep Learning) est capable d'apprendre des mappings complexes comme la classification d'images ou la traduction linguistique.

### Méthode des Éléments Finis (FEM)
En mécanique des fluides ou en calcul de structure, la méthode de Galerkin consiste à chercher la solution faible d'une équation différentielle non pas dans un vaste espace infini-dimensionnel (un espace de Sobolev), mais dans un sous-espace de dimension finie, souvent engendré par des fonctions polynomiales par morceaux (qui sont continues ou simples). L'erreur commise entre la solution exacte et la solution approchée tend vers zéro à mesure que l'on raffine le maillage, ce qui est une conséquence géométrique directe des théorèmes de densité dans les espaces $L^p$ et les espaces de Sobolev.
