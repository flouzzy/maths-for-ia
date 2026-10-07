---
uuid: "jalon-83"
title: "Dérivation au sens des distributions"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]]"
next: "[[Jalon 84 (Livrable IA).md]]"
---

# Jalon 83 : Dérivation au sens des distributions

## 1. Introduction et Genèse Physique

Historiquement, le besoin de dériver des fonctions non différentiables ou discontinues s'est fait sentir en physique, notamment avec les travaux de Paul Dirac en mécanique quantique et d'Oliver Heaviside en ingénierie électrique. Lorsqu'on étudie un signal qui s'allume instantanément (un interrupteur parfait), le signal est modélisé par la fonction de Heaviside. La dérivée de ce signal, représentant par exemple une intensité transitoire infinie sur un temps nul, ne peut pas être décrite par une fonction classique.

La théorie des distributions de Laurent Schwartz offre un cadre rigoureux (celui de l'analyse fonctionnelle) pour justifier et étendre ces manipulations formelles. L'idée fondatrice est de transférer la dérivation du "signal" (l'objet rugueux) vers une "fonction test" (un objet infiniment lisse et à support compact) via une intégration par parties formelle.

Ainsi, on ne regarde plus la fonction point par point, mais on l'observe à travers son action (intégrale) sur des fonctions tests de la classe $\mathcal{D}(\mathbb{R})$. Cela permet de définir une dérivée pour tout objet localement intégrable, et plus généralement pour toute distribution, prolongeant ainsi l'opérateur de dérivation de manière universelle et continue.

## 2. Définitions, Théorèmes & Exemples

### A. Dérivée d'une distribution

Soit $\mathcal{D}(\mathbb{R})$ l'espace des fonctions tests (fonctions $C^\infty$ à support compact) et $\mathcal{D}'(\mathbb{R})$ l'espace des distributions (formes linéaires continues sur $\mathcal{D}(\mathbb{R})$).

**Définition (Dérivée au sens des distributions) :**
Soit $T \in \mathcal{D}'(\mathbb{R})$. On définit la dérivée de $T$, notée $T'$ (ou $\frac{dT}{dx}$), comme la distribution agissant sur toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$ par la formule :
$$ \langle T', \phi \rangle = - \langle T, \phi' \rangle $$

Par récurrence, on définit la dérivée $k$-ième $T^{(k)}$ par :
$$ \langle T^{(k)}, \phi \rangle = (-1)^k \langle T, \phi^{(k)} \rangle $$

**Exemple Concret 1 : Dérivation d'une fonction $C^1$.**
Soit $f \in C^1(\mathbb{R})$. Identifions $f$ à la distribution régulière $T_f$. Pour $\phi \in \mathcal{D}(\mathbb{R})$, on a :
$$ \langle (T_f)', \phi \rangle = - \langle T_f, \phi' \rangle = - \int_{\mathbb{R}} f(x) \phi'(x) dx $$
Par intégration par parties, sachant que $\phi$ est à support compact (donc le terme de bord $[f(x)\phi(x)]_{-\infty}^{+\infty}$ est nul) :
$$ \langle (T_f)', \phi \rangle = \int_{\mathbb{R}} f'(x) \phi(x) dx = \langle T_{f'}, \phi \rangle $$
On retrouve bien la dérivée usuelle.

### B. Formule des sauts

La formule des sauts permet de calculer la dérivée distributionnelle d'une fonction continue par morceaux.

**Théorème (Formule des sauts en dimension 1) :**
Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction de classe $C^1$ par morceaux, présentant des discontinuités de première espèce (des sauts) aux points isolés $a_1, a_2, \dots, a_n$.
Notons $\{f'\}$ la dérivée de $f$ au sens usuel (définie presque partout sur $\mathbb{R} \setminus \{a_1, \dots, a_n\}$).
Si $\{f'\}$ est localement intégrable sur $\mathbb{R}$, alors la dérivée de $f$ au sens des distributions est donnée par :
$$ T_f' = T_{\{f'\}} + \sum_{i=1}^n \sigma_{a_i} \delta_{a_i} $$
où $\sigma_{a_i} = f(a_i^+) - f(a_i^-)$ est le saut de la fonction $f$ au point $a_i$, et $\delta_{a_i}$ est la distribution de Dirac centrée en $a_i$.

**Exemple Concret 2 : Application à la fonction signe.**
Considérons la fonction signe définie par $f(x) = 1$ si $x > 0$ et $f(x) = -1$ si $x < 0$.
- La dérivée usuelle $\{f'\}$ est nulle partout où elle est définie ($x \neq 0$).
- En $x = 0$, $f$ présente un saut de $\sigma_0 = f(0^+) - f(0^-) = 1 - (-1) = 2$.
D'après la formule des sauts, la dérivée au sens des distributions est :
$$ f' = 0 + 2\delta_0 = 2\delta_0 $$

### C. Espaces de Sobolev $H^1(\mathbb{R})$

La dérivation distributionnelle permet d'introduire des espaces fonctionnels adaptés à l'étude des équations aux dérivées partielles.

**Définition (Espace de Sobolev $H^1$) :**
L'espace de Sobolev $H^1(\mathbb{R})$ (ou $W^{1,2}(\mathbb{R})$) est défini comme l'espace des fonctions $f \in L^2(\mathbb{R})$ dont la dérivée première au sens des distributions $f'$ appartient également à $L^2(\mathbb{R})$.
$$ H^1(\mathbb{R}) = \left\{ f \in L^2(\mathbb{R}) \mid f' \in L^2(\mathbb{R}) \right\} $$
Cet espace est muni du produit scalaire :
$$ \langle f, g \rangle_{H^1} = \int_{\mathbb{R}} f(x)g(x) dx + \int_{\mathbb{R}} f'(x)g'(x) dx $$

**Exemple Concret 3 : Inappartenance de la fonction échelon à $H^1$.**
Considérons la fonction $f(x) = e^{-|x|}$.
Elle est continue, son intégrale $\int e^{-2|x|}dx$ est finie donc $f \in L^2(\mathbb{R})$.
Sa dérivée distributionnelle est $f'(x) = -\text{sgn}(x)e^{-|x|}$. On a $f' \in L^2(\mathbb{R})$. Ainsi, $f \in H^1(\mathbb{R})$.
En revanche, la fonction $g(x) = \mathbf{1}_{[0,1]}(x)$ est dans $L^2(\mathbb{R})$, mais sa dérivée est $g' = \delta_0 - \delta_1$. Les distributions de Dirac n'appartenant pas à $L^2(\mathbb{R})$, on conclut que $g \notin H^1(\mathbb{R})$.

**Exemple Concret 4 : Dérivée de la valeur absolue.**
La fonction $f(x) = |x|$ est continue partout, et continûment dérivable sur $\mathbb{R}^*$ de dérivée $f'(x) = \text{sgn}(x)$.
En $x=0$, $f$ est continue ($f(0^+) = f(0^-) = 0$), donc le saut est nul ($\sigma_0 = 0$).
D'après la formule des sauts :
$$ f' = \text{sgn}(x) + 0 \cdot \delta_0 = \text{sgn}(x) $$

**Exemple Concret 5 : Dérivée d'un Dirac translaté.**
Soit $T = \delta_a$. Calculons sa dérivée $T'$.
Pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle \delta_a', \phi \rangle = - \langle \delta_a, \phi' \rangle = - \phi'(a) $$
La dérivée d'un Dirac en $a$ évalue l'opposé de la dérivée de la fonction test en $a$.

**Exemple Concret 6 : L'équation $x T = 1$.**
On cherche les distributions $T$ vérifiant $xT = 1$. L'une des solutions est la valeur principale de Cauchy, notée $\text{vp}(\frac{1}{x})$, définie par :
$$ \langle \text{vp}\left(\frac{1}{x}\right), \phi \rangle = \lim_{\epsilon \to 0^+} \int_{|x|>\epsilon} \frac{\phi(x)}{x} dx $$
Une propriété remarquable est que la dérivée distributionnelle du logarithme donne cette distribution :
$$ (\ln|x|)' = \text{vp}\left(\frac{1}{x}\right) $$


## 3. Démonstrations

### Démonstration 1 : Dérivée de la fonction de Heaviside

La fonction de Heaviside est définie par $H(x) = 1$ pour $x > 0$ et $H(x) = 0$ pour $x \le 0$.
Montrons rigoureusement que $H' = \delta_0$.

**Preuve :**
Soit $\phi \in \mathcal{D}(\mathbb{R})$ une fonction test. Par définition de la dérivée distributionnelle :
$$ \langle H', \phi \rangle = - \langle H, \phi' \rangle $$
En identifiant $H$ à son action intégrale :
$$ \langle H', \phi \rangle = - \int_{\mathbb{R}} H(x) \phi'(x) dx = - \int_0^{+\infty} 1 \cdot \phi'(x) dx $$
Par le théorème fondamental de l'analyse :
$$ \int_0^{+\infty} \phi'(x) dx = \lim_{R \to +\infty} \phi(R) - \phi(0) $$
Puisque $\phi$ est à support compact, elle s'annule en dehors d'un intervalle $[-A, A]$, donc pour $R > A$, $\phi(R) = 0$.
Ainsi, l'intégrale vaut $-\phi(0)$.
En substituant :
$$ \langle H', \phi \rangle = - ( - \phi(0) ) = \phi(0) $$
Or, par définition de la distribution de Dirac en 0, on a $\langle \delta_0, \phi \rangle = \phi(0)$.
Par conséquent, pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$, $\langle H', \phi \rangle = \langle \delta_0, \phi \rangle$.
Ce qui prouve que $H' = \delta_0$ au sens des distributions. $\blacksquare$

### Démonstration 2 : Formule des sauts avec un unique point de saut

Soit $f$ de classe $C^1$ sur $\mathbb{R}^*$, continue à gauche et à droite en 0, et dont la dérivée usuelle $\{f'\}$ est localement intégrable. Montrons que $T_f' = T_{\{f'\}} + \sigma_0 \delta_0$.

**Preuve :**
Soit $\phi \in \mathcal{D}(\mathbb{R})$. Le support de $\phi$ est inclus dans un segment $[-A, A]$.
$$ \langle f', \phi \rangle = - \langle f, \phi' \rangle = - \int_{-\infty}^{+\infty} f(x) \phi'(x) dx $$
On découpe l'intégrale en $x=0$ :
$$ \langle f', \phi \rangle = - \int_{-\infty}^{0} f(x) \phi'(x) dx - \int_{0}^{+\infty} f(x) \phi'(x) dx $$
Appliquons une intégration par parties sur $]-\infty, 0[$ et sur $]0, +\infty[$ :
Pour $]-\infty, 0[$ :
$$ \int_{-\infty}^{0} f(x) \phi'(x) dx = [f(x)\phi(x)]_{-\infty}^{0^-} - \int_{-\infty}^{0} f'(x) \phi(x) dx $$
$$ = f(0^-)\phi(0) - 0 - \int_{-\infty}^{0} f'(x) \phi(x) dx $$
Pour $]0, +\infty[$ :
$$ \int_{0}^{+\infty} f(x) \phi'(x) dx = [f(x)\phi(x)]_{0^+}^{+\infty} - \int_{0}^{+\infty} f'(x) \phi(x) dx $$
$$ = 0 - f(0^+)\phi(0) - \int_{0}^{+\infty} f'(x) \phi(x) dx $$
En sommant ces deux expressions :
$$ \langle f', \phi \rangle = - \left( f(0^-)\phi(0) - \int_{-\infty}^{0} f'(x) \phi(x) dx - f(0^+)\phi(0) - \int_{0}^{+\infty} f'(x) \phi(x) dx \right) $$
$$ \langle f', \phi \rangle = \left( f(0^+) - f(0^-) \right)\phi(0) + \int_{-\infty}^{+\infty} \{f'\}(x) \phi(x) dx $$
Soit :
$$ \langle f', \phi \rangle = \sigma_0 \langle \delta_0, \phi \rangle + \langle T_{\{f'\}}, \phi \rangle $$
On a bien démontré que $f' = \{f'\} + \sigma_0 \delta_0$. $\blacksquare$

## 4. Applications en Physique, Logique, & IA

La dérivation au sens des distributions possède un impact majeur en Intelligence Artificielle et en Physique Computationnelle.

- **Fonctions d'activation non-lisses (Deep Learning) :**
L'une des fonctions d'activation les plus utilisées est la ReLU ($f(x) = \max(0,x)$). Bien qu'elle soit continue, elle n'est pas dérivable classiquement en $x=0$. Au sens des distributions, sa dérivée est la fonction de Heaviside $H(x)$. Sa dérivée seconde est la distribution de Dirac $\delta_0$. Cette formalisation justifie mathématiquement les algorithmes de rétro-propagation du gradient (backpropagation) qui traitent des points de non-différentiabilité. En informatique, on choisit conventionnellement $H(0)=0$ ou $H(0)=0.5$, ce qui correspond en réalité à la notion de sous-différentiel (lié aux distributions).

- **Traitement d'Image et Détection de Contours :**
En vision par ordinateur, une image est un signal 2D discontinu. Un contour correspond à un saut brutal d'intensité. L'application d'un opérateur de dérivation spatiale (comme le filtre de Sobel, approximation discrète du gradient) fait ressortir ces discontinuités sous forme de pics élevés. C'est l'incarnation visuelle et algorithmique de la formule des sauts : la composante impulsionnelle $\sigma \delta$ domine le signal dérivé.

- **Physics-Informed Neural Networks (PINNs) :**
Dans la modélisation de phénomènes physiques complexes par réseaux de neurones (mécanique des fluides, propagation d'ondes avec chocs), la solution présente fréquemment des discontinuités. La fonction de perte associée à l'Équation aux Dérivées Partielles doit donc évaluer des dérivées d'ordre supérieur. L'utilisation d'une formulation faible, s'appuyant sur la dérivation distributionnelle (intégration contre des fonctions tests ou utilisation d'espaces de Sobolev $H^s$), permet d'optimiser le réseau même en présence de chocs réguliers.
