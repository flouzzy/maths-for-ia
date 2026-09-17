---
uuid: "jalon-73"
title: "Espaces Lp et passage au quotient"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 72 (Livrable IA).md]]"
next: "[[Jalon 74 (Inégalités fondamentales de l'analyse fonctionnelle).md]]"
---
# Jalon 73 : Espaces $L^p$ et passage au quotient

## 1. Genèse et Intuition Physique

L'intégration de Lebesgue permet de mesurer des ensembles de manière très générale, mais pour construire une théorie robuste de l'analyse fonctionnelle, nous avons besoin d'espaces vectoriels structurés (complets).
En physique du signal, on rencontre souvent deux signaux qui diffèrent uniquement sur un ensemble de points de mesure nulle (par exemple des bruits impulsionnels instantanés). Si on intègre leur différence, l'énergie de cette différence est nulle.
Pourtant, d'un point de vue strict des fonctions, ces signaux ne sont pas égaux. Le passage au quotient résout cette anomalie en identifiant les fonctions qui sont "presque partout" égales.

Les espaces $L^p$ classifient les fonctions selon la finitude de leurs moments d'ordre $p$. Par exemple, l'espace $L^1$ rassemble les fonctions d'aire absolue finie (stabilité moyenne), tandis que l'espace $L^2$ regroupe celles d'énergie finie.

## 2. Définitions, Théorèmes et Exemples

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Les espaces $\mathcal{L}^p$ (non quotientés)

**Définition 1 (Espace $\mathcal{L}^p$) :**
Pour $1 \le p < +\infty$, on définit l'ensemble des fonctions mesurables dont la puissance $p$-ième est intégrable :
$$\mathcal{L}^p(\mu) = \left\lbrace f : X \to \mathbb{K} \mid f \text{ est mesurable et } \int_X |f|^p d\mu < +\infty \right\rbrace$$
On définit également la semi-norme $\|f\|_p = \left( \int_X |f|^p d\mu \right)^{1/p}$.

**Définition 2 (Espace $\mathcal{L}^\infty$) :**
L'espace $\mathcal{L}^\infty(\mu)$ est l'ensemble des fonctions mesurables essentiellement bornées, c'est-à-dire bornées presque partout.
$\|f\|_\infty = \inf \{ C \ge 0 \mid |f(x)| \le C \text{ p.p.} \}$.

**Exemple 1 (Fonction indicatrice) :** Soit $X=[0,1]$ avec la mesure de Lebesgue $\lambda$. La fonction $f(x) = 1_{[0, 1/2]}(x)$ est dans tous les $\mathcal{L}^p([0,1])$. Son intégrale au carré est $1/2$, donc $\|f\|_2 = 1/\sqrt{2}$. Son intégrale à la puissance $p$ est $1/2$, donc $\|f\|_p = (1/2)^{1/p}$.

**Exemple 2 (Fonction puissance) :** Soit $f(x) = x^{-1/2}$ sur $X=]0, 1]$ avec la mesure de Lebesgue.
- $f \in \mathcal{L}^1$ car $\int_0^1 x^{-1/2} dx = [2x^{1/2}]_0^1 = 2 < +\infty$.
- $f \notin \mathcal{L}^2$ car $\int_0^1 (x^{-1/2})^2 dx = \int_0^1 \frac{1}{x} dx = [\ln(x)]_0^1 = +\infty$.

**Exemple 3 (Espace de suite) :** Si $X = \mathbb{N}$ avec la mesure de comptage, on note $\ell^p = \mathcal{L}^p(\mathbb{N})$. La suite $u_n = 1/n$ est dans $\ell^2$ (car $\sum 1/n^2 = \pi^2/6 < +\infty$) mais n'est pas dans $\ell^1$ (série harmonique divergente).

### La semi-norme et la relation d'équivalence

L'application $f \mapsto \|f\|_p$ n'est qu'une **semi-norme** sur $\mathcal{L}^p$ car $\|f\|_p = 0$ n'implique pas $f=0$ partout, seulement presque partout.

**Exemple 4 (Fonction nulle p.p.) :** Soit $X = \mathbb{R}$ et $f$ la fonction indicatrice des rationnels $1_{\mathbb{Q}}$.
Comme $\mathbb{Q}$ est dénombrable, sa mesure de Lebesgue est nulle. Ainsi $\int_{\mathbb{R}} |1_{\mathbb{Q}}|^p d\lambda = 0$. Donc $\|1_{\mathbb{Q}}\|_p = 0$, bien que $f(x)=1$ pour une infinité de points.

**Définition 3 (Relation d'équivalence) :**
On définit la relation d'équivalence $\sim$ sur l'ensemble des fonctions mesurables par :
$f \sim g \iff f = g \text{ presque partout}$ (c'est-à-dire $\mu(\{x \in X \mid f(x) \neq g(x)\}) = 0$).

### Le passage au quotient $L^p$

**Définition 4 (Espace quotient $L^p$) :**
L'espace $L^p(\mu)$ est l'espace quotient de $\mathcal{L}^p(\mu)$ par la relation $\sim$.
$L^p(\mu) = \mathcal{L}^p(\mu) / \sim$.
Ses éléments sont des **classes d'équivalence** de fonctions. Si $f \in \mathcal{L}^p(\mu)$, sa classe est $[f]$.
Sur cet espace, $\| \cdot \|_p$ devient une véritable **norme**. Par abus de notation, on identifie souvent la classe $[f]$ à un représentant $f$.

**Exemple 5 (Représentant continu) :** Soit $f : \mathbb{R} \to \mathbb{R}$ définie par $f(x) = \sin(x)$ si $x \neq 0$ et $f(0) = 42$. La fonction $f$ n'est pas continue. Cependant, dans $L^p$, $f \sim \sin$. La fonction $\sin$ est un représentant continu de la classe $[f]$.

**Exemple 6 (Égalité dans $L^p$) :** La fonction de Heaviside modifiée $H^*(x) = 1$ si $x > 0$, $0$ si $x \le 0$ et $1/2$ si $x=0$, et la fonction $H(x)=1$ si $x>0$, $0$ si $x<0$ sont exactement la même "fonction" dans l'espace $L^p(\mathbb{R})$, car elles diffèrent uniquement en $0$ qui est de mesure nulle.

**Théorème 1 (Structure d'espace vectoriel normé) :**
Pour $1 \le p \le \infty$, l'espace $(L^p(\mu), \|\cdot\|_p)$ est un espace vectoriel normé.
La stabilité par addition découle de l'inégalité $(a+b)^p \le 2^{p-1}(a^p + b^p)$ pour $a,b \ge 0$, et l'inégalité triangulaire s'appelle l'inégalité de Minkowski.

## 3. Démonstrations

### Démonstration : Séparation de la semi-norme au quotient

**Proposition :** Dans l'espace quotient $L^p(\mu)$, on a $\|[f]\|_p = 0 \iff [f] = [0]$.

*Preuve :*
1. **Sens ($\impliedby$) :** Supposons $[f] = [0]$. Alors $f \sim 0$, ce qui signifie que $f(x) = 0$ pour presque tout $x \in X$.
Ainsi, l'ensemble $A = \{x \in X \mid f(x) \neq 0\}$ est de mesure nulle : $\mu(A) = 0$.
La fonction $|f|^p$ est nulle en dehors de $A$. Par conséquent, $\int_X |f|^p d\mu = \int_A |f|^p d\mu + \int_{X \setminus A} 0 d\mu$.
Puisque $\mu(A) = 0$, l'intégrale sur $A$ est nulle. D'où $\|f\|_p = 0$.

2. **Sens ($\implies$) :** Supposons $\|f\|_p = 0$. Cela signifie que $\int_X |f|^p d\mu = 0$.
Soit $A_n = \{x \in X \mid |f(x)|^p \ge 1/n\}$.
D'après l'inégalité de Markov, $\mu(A_n) \le \frac{1}{1/n} \int_X |f|^p d\mu = n \times 0 = 0$.
Soit $A = \{x \in X \mid f(x) \neq 0\} = \{x \in X \mid |f(x)|^p > 0\}$.
On remarque que $A = \bigcup_{n=1}^\infty A_n$.
La sous-additivité de la mesure implique que $\mu(A) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0$.
Donc $f(x) = 0$ presque partout. Autrement dit $f \sim 0$, et par passage au quotient, $[f] = [0]$. $\blacksquare$

### Démonstration : Stabilité par combinaison linéaire

Montrons que si $f, g \in \mathcal{L}^p$, alors $f+g \in \mathcal{L}^p$.

*Preuve :*
Soient $f, g \in \mathcal{L}^p$. Par définition, $\int_X |f|^p d\mu < \infty$ et $\int_X |g|^p d\mu < \infty$.
Pour tout $x \in X$, on a $|f(x) + g(x)| \le |f(x)| + |g(x)|$.
Puisque la fonction $t \mapsto t^p$ est convexe croissante sur $\mathbb{R}^+$ pour $p \ge 1$, on a :
$$ \left( \frac{|f(x)| + |g(x)|}{2} \right)^p \le \frac{1}{2} |f(x)|^p + \frac{1}{2} |g(x)|^p $$
En multipliant par $2^p$, on obtient l'inégalité algébrique élémentaire :
$$ |f(x) + g(x)|^p \le 2^{p-1} \left( |f(x)|^p + |g(x)|^p \right) $$
En intégrant cette inégalité sur $X$, par linéarité de l'intégrale :
$$ \int_X |f+g|^p d\mu \le 2^{p-1} \left( \int_X |f|^p d\mu + \int_X |g|^p d\mu \right) < \infty $$
Donc $f+g \in \mathcal{L}^p$. $\blacksquare$

## 4. Applications en Physique, Logique et IA

### Intelligence Artificielle et Choix de la Fonction de Perte (Loss)

En apprentissage automatique, le choix de la métrique d'évaluation est intimement lié aux normes $L^p$. Supposons que l'on cherche à approcher une variable cible $Y$ par un estimateur $f(X)$. L'erreur est une fonction dans un espace $L^p$.
- **Régression $L^2$ (Mean Squared Error, MSE) :** On cherche à minimiser $\|Y - f(X)\|_2^2 = \mathbb{E}[(Y - f(X))^2]$. La norme $L^2$ pénalise fortement les grands écarts (à cause du carré). La solution théorique optimale est l'espérance conditionnelle $f(X) = \mathbb{E}[Y \mid X]$.
- **Régression $L^1$ (Mean Absolute Error, MAE) :** On cherche à minimiser $\|Y - f(X)\|_1 = \mathbb{E}[|Y - f(X)|]$. La norme $L^1$ accorde le même poids unitaire à toute erreur. Elle est particulièrement robuste aux points aberrants (outliers). La solution optimale est la médiane conditionnelle.

### Compression de signaux et quantification

La compression de données (par exemple JPEG pour les images ou MP3 pour l'audio) consiste à trouver une fonction "plus simple" qui approxime le signal de départ au sens d'une norme $L^p$.
- Pour un signal audio, l'oreille humaine est sensible à l'énergie, on cherche donc à approcher le signal en norme $L^2$.
- Pour un signal où les variations brusques (bords d'image) sont essentielles, des espaces dérivés basés sur des normes $L^1$ (espaces de Sobolev $W^{1,1}$ ou à variation bornée) sont privilégiés car la norme $L^2$ lisse trop le signal (phénomène de Gibbs).
