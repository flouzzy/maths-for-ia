---
uuid: "jalon-98"
title: "Théorème de Hahn-Banach (forme analytique)"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/fondations
prev: "[[Jalon 97 (Espaces de Banach et Opérateurs Linéaires).md]]"
next: "[[Jalon 99 (Théorème de Hahn-Banach).md]]"
---

# Jalon 98 : Théorème de Hahn-Banach (forme analytique)

## 1. Introduction historique et conceptuelle

La naissance de l'analyse fonctionnelle au début du XXe siècle, sous l'impulsion de mathématiciens tels que Stefan Banach, Hans Hahn, et Norbert Wiener, a été motivée par le besoin de comprendre des espaces de dimension infinie, comme les espaces de fonctions. Dans ces espaces vastes, une question fondamentale se pose : dispose-t-on de suffisamment de "scanners" linéaires pour explorer et séparer les éléments de l'espace ? En dimension finie, l'existence de formes linéaires est garantie par la construction de bases. En dimension infinie, la situation est beaucoup plus délicate.

Le théorème de Hahn-Banach, formulé indépendamment par Hahn (1927) et Banach (1929), apporte une réponse magistrale à cette question. Il stipule que toute forme linéaire définie sur un sous-espace, et dominée par une certaine jauge (une fonctionnelle sous-linéaire), peut être prolongée à l'espace tout entier tout en respectant cette domination. Ce résultat non-constructif, qui repose fondamentalement sur le lemme de Zorn (et donc l'axiome du choix), est le pilier central de l'analyse fonctionnelle moderne. Il permet de garantir l'existence d'un dual topologique suffisamment riche, ouvrant la voie à l'optimisation convexe, à la théorie des distributions de Schwartz, et aux fondations mathématiques du Machine Learning.

## 2. Fonctionnelles sous-linéaires et jauges

Avant d'énoncer le théorème principal, nous devons définir la structure mathématique qui servira de "plafond" ou de contrainte lors du prolongement.

> **Définition 1 (Fonctionnelle sous-linéaire) :** Soit $E$ un espace vectoriel sur $\mathbb{R}$. Une application $p : E \to \mathbb{R}$ est dite **sous-linéaire** si elle vérifie les deux axiomes suivants :
> 1. **Sous-additivité :** $\forall x, y \in E, \quad p(x+y) \le p(x) + p(y)$.
> 2. **Homogénéité positive :** $\forall \lambda \ge 0, \forall x \in E, \quad p(\lambda x) = \lambda p(x)$.

**Exemple concret calculatoire 1 :**
Soit $E = \mathbb{R}^2$ et $p(x) = p(x_1, x_2) = \max(|x_1|, |x_2|) + 2\max(x_1, 0)$.
Vérifions que $p$ est sous-linéaire.
Soient $x = (x_1, x_2)$ et $y = (y_1, y_2)$ dans $E$.
L'application $(x_1, x_2) \mapsto \max(|x_1|, |x_2|)$ est la norme infinie $\|\cdot\|_\infty$, qui est sous-linéaire.
Pour la partie $q(x) = 2\max(x_1, 0)$ :
$q(x+y) = 2\max(x_1+y_1, 0) \le 2(\max(x_1, 0) + \max(y_1, 0)) = q(x) + q(y)$.
Pour $\lambda \ge 0$, $q(\lambda x) = 2\max(\lambda x_1, 0) = 2\lambda\max(x_1, 0) = \lambda q(x)$.
La somme de deux fonctionnelles sous-linéaires est sous-linéaire, donc $p$ est bien sous-linéaire.
Calculons $p$ au point $v = (-3, 4)$ :
$p(-3, 4) = \max(|-3|, |4|) + 2\max(-3, 0) = 4 + 2(0) = 4$.
Calculons $p$ au point $w = (3, -1)$ :
$p(3, -1) = \max(|3|, |-1|) + 2\max(3, 0) = 3 + 2(3) = 9$.

> **Définition 2 (Jauge d'un convexe) :** Soit $C$ un sous-ensemble convexe de $E$, absorbant (pour tout $x \in E$, il existe $t>0$ tel que $x \in tC$) et contenant l'origine. La **jauge** ou **fonctionnelle de Minkowski** associée à $C$ est définie par :
> $$ p_C(x) = \inf \{ \lambda > 0 \mid x \in \lambda C \} $$

**Propriété immédiate :** La jauge $p_C$ d'un tel convexe $C$ est toujours une fonctionnelle sous-linéaire.

## 3. Le Théorème de Hahn-Banach (Forme Analytique)

Nous formulons ici le théorème dans toute sa généralité algébrique sur le corps des réels.

> **Théorème de Hahn-Banach (Analytique réel) :**
> Soit $E$ un espace vectoriel sur $\mathbb{R}$.
> Soit $p : E \to \mathbb{R}$ une fonctionnelle sous-linéaire.
> Soit $M$ un sous-espace vectoriel de $E$, et $f : M \to \mathbb{R}$ une forme linéaire telle que :
> $$ \forall x \in M, \quad f(x) \le p(x) $$
> Alors, il existe une forme linéaire $F : E \to \mathbb{R}$ prolongeant $f$ (c'est-à-dire $F|_M = f$) et telle que :
> $$ \forall x \in E, \quad F(x) \le p(x) $$

**Exemple concret calculatoire 2 :**
Considérons $E = \mathbb{R}^2$ muni de la fonctionnelle sous-linéaire $p(x_1, x_2) = \sqrt{x_1^2 + x_2^2}$ (la norme euclidienne).
Soit le sous-espace $M = \text{Vect}((1, 1))$ et la forme linéaire $f$ définie sur $M$ par $f(\lambda(1, 1)) = \lambda$.
Vérifions la condition de domination sur $M$ :
Pour $x = (\lambda, \lambda) \in M$, on a $f(x) = \lambda$.
Par ailleurs, $p(x) = \sqrt{\lambda^2 + \lambda^2} = |\lambda|\sqrt{2}$.
Puisque $\lambda \le |\lambda| \le |\lambda|\sqrt{2}$, on a bien $f(x) \le p(x)$ pour tout $x \in M$.
Le théorème de Hahn-Banach garantit l'existence d'une forme linéaire $F(x_1, x_2) = a x_1 + b x_2$ sur $\mathbb{R}^2$ telle que $F(1, 1) = a+b = 1$ et $F(x_1, x_2) \le \sqrt{x_1^2+x_2^2}$ pour tout $(x_1, x_2)$.
Un choix évident est $a = \frac{1}{2}, b = \frac{1}{2}$. La forme $F(x_1, x_2) = \frac{1}{2}x_1 + \frac{1}{2}x_2$ vérifie :
$F(1,1) = 1$ et par l'inégalité de Cauchy-Schwarz : $F(x_1, x_2) = \langle (\frac{1}{2}, \frac{1}{2}), (x_1, x_2) \rangle \le \sqrt{\frac{1}{4}+\frac{1}{4}} \sqrt{x_1^2+x_2^2} = \frac{1}{\sqrt{2}} p(x) \le p(x)$.

## 4. Démonstration exhaustive

La démonstration s'effectue en deux temps : on montre d'abord qu'on peut prolonger la forme linéaire à une dimension supplémentaire de manière cohérente, puis on utilise le lemme de Zorn pour conclure sur l'existence d'un prolongement maximal.

### Étape 1 : Prolongement d'une dimension

Supposons que $M \neq E$. Choisissons un vecteur $x_0 \in E \setminus M$. Nous allons prolonger $f$ au sous-espace $M_1 = M \oplus \mathbb{R}x_0$.
Tout élément $z \in M_1$ s'écrit de manière unique $z = x + t x_0$ avec $x \in M$ et $t \in \mathbb{R}$.
Pour que notre prolongement $F_1$ soit linéaire, il doit s'écrire :
$$ F_1(x + t x_0) = f(x) + t F_1(x_0) $$
Posons $\alpha = F_1(x_0)$. Le problème se réduit à trouver un réel $\alpha$ tel que pour tout $x \in M$ et tout $t \in \mathbb{R}$ :
$$ f(x) + t\alpha \le p(x + t x_0) $$

- **Si $t = 0$**, la condition $f(x) \le p(x)$ est déjà satisfaite par hypothèse.
- **Si $t > 0$**, en divisant par $t$, la condition devient :
  $$ f(x/t) + \alpha \le p(x/t + x_0) $$
  Soit, pour tout $y \in M$ (en posant $y = x/t$) :
  $$ \alpha \le p(y + x_0) - f(y) $$
- **Si $t < 0$**, posons $t = -s$ avec $s > 0$. L'inégalité $f(x) - s\alpha \le p(x - s x_0)$ donne, en divisant par $s$ :
  $$ f(x/s) - \alpha \le p(x/s - x_0) $$
  Soit, pour tout $z \in M$ (en posant $z = x/s$) :
  $$ f(z) - p(z - x_0) \le \alpha $$

Ainsi, $\alpha$ doit satisfaire pour tout $y, z \in M$ :
$$ f(z) - p(z - x_0) \le \alpha \le p(y + x_0) - f(y) $$
Un tel $\alpha$ existe si et seulement si pour tout $y, z \in M$ :
$$ f(z) - p(z - x_0) \le p(y + x_0) - f(y) $$
Ce qui équivaut à :
$$ f(z) + f(y) \le p(y + x_0) + p(z - x_0) $$
Or, par linéarité de $f$ sur $M$ et sous-additivité de $p$ :
$$ f(z) + f(y) = f(z+y) \le p(z+y) = p(z - x_0 + y + x_0) \le p(z - x_0) + p(y + x_0) $$
L'inégalité est donc toujours vraie. L'ensemble des réels de la forme $f(z) - p(z - x_0)$ est majoré, il admet un supremum (borne supérieure). L'ensemble des réels $p(y + x_0) - f(y)$ est minoré, il admet un infimum (borne inférieure). Le supremum est inférieur ou égal à l'infimum, on peut donc choisir $\alpha$ n'importe où dans cet intervalle.
Le prolongement $F_1$ à $M_1$ est donc construit.

### Étape 2 : L'argument de Zorn pour le cas de dimension infinie

Soit $\mathcal{E}$ l'ensemble des couples $(N, g)$ où $N$ est un sous-espace de $E$ contenant $M$, et $g : N \to \mathbb{R}$ est une forme linéaire prolongeant $f$ et majorée par $p$.
On munit $\mathcal{E}$ de la relation d'ordre partiel suivante :
$(N_1, g_1) \preceq (N_2, g_2) \iff N_1 \subset N_2 \text{ et } g_2|_{N_1} = g_1$.

L'ensemble $\mathcal{E}$ est non vide car $(M, f) \in \mathcal{E}$.
Soit $\mathcal{C} = \{(N_i, g_i)\}_{i \in I}$ une chaîne totalement ordonnée dans $\mathcal{E}$.
Définissons $N^* = \bigcup_{i \in I} N_i$. $N^*$ est un sous-espace vectoriel car la chaîne est totalement ordonnée.
Définissons $g^* : N^* \to \mathbb{R}$ par $g^*(x) = g_i(x)$ si $x \in N_i$. Cette définition est non ambiguë grâce à la relation d'ordre de la chaîne.
Il est évident que $g^*$ est linéaire et dominée par $p$. Donc $(N^*, g^*) \in \mathcal{E}$, et c'est un majorant de la chaîne $\mathcal{C}$.

D'après le lemme de Zorn, l'ensemble ordonné inductif $(\mathcal{E}, \preceq)$ possède un élément maximal $(E_{max}, F_{max})$.
Supposons par l'absurde que $E_{max} \neq E$.
Il existe alors $x_0 \in E \setminus E_{max}$. Par l'Étape 1, on pourrait construire un prolongement strict de $F_{max}$ sur $E_{max} \oplus \mathbb{R}x_0$, ce qui contredit la maximalité de $(E_{max}, F_{max})$.
Par conséquent, $E_{max} = E$. La forme linéaire $F_{max}$ est le prolongement global recherché. La démonstration est achevée. $\blacksquare$

## 5. Corollaires fondamentaux

> **Corollaire (Existence de formes linéaires continues) :**
> Soit $E$ un espace normé et $x_0 \in E$ un vecteur non nul. Il existe une forme linéaire continue $F \in E'$ telle que $\|F\|_{E'} = 1$ et $F(x_0) = \|x_0\|_E$.

**Démonstration :** Posons $p(x) = \|x\|_E$, qui est sous-linéaire. Soit $M = \mathbb{R}x_0$. On définit $f : M \to \mathbb{R}$ par $f(t x_0) = t \|x_0\|_E$.
Pour $t \in \mathbb{R}$, $f(t x_0) = t \|x_0\|_E \le |t| \|x_0\|_E = \|t x_0\|_E = p(t x_0)$.
D'après le théorème de Hahn-Banach, $f$ se prolonge en $F : E \to \mathbb{R}$ telle que $F(x) \le \|x\|_E$ pour tout $x$.
Puisque $F(-x) \le \|-x\|_E = \|x\|_E$, on a $|F(x)| \le \|x\|_E$.
Donc $F$ est continue et de norme $\|F\|_{E'} \le 1$. Mais $F(x_0/\|x_0\|_E) = 1$, donc $\|F\|_{E'} = 1$. $\blacksquare$

## 6. Applications en Optimisation et en Intelligence Artificielle

### A. Dualité de Lagrange et Optimisation Convexe
Dans la théorie de l'optimisation, de nombreux problèmes de Machine Learning (tels que la régression Ridge, Lasso ou les Support Vector Machines) s'écrivent sous la forme de minimisation d'une fonctionnelle sous contraintes. Le théorème de Hahn-Banach garantit qu'un ensemble convexe et fermé peut être séparé d'un point extérieur par un hyperplan affine. C'est l'essence même de l'existence des multiplicateurs de Lagrange, qui permettent de formuler les problèmes duaux souvent plus faciles à résoudre computationnellement.

### B. Espace de Plongement et Apprentissage de Variétés
En analyse topologique des données, on cherche à plonger des données complexes dans des espaces normés ou de Hilbert. Les formes linéaires, dont l'existence riche est garantie par Hahn-Banach, servent de "coordonnées généralisées" (features) pour extraire l'information. La théorie des noyaux (Kernel trick) s'appuie profondément sur la riche structure duale des espaces fonctionnels, certifiant que tout point de données est séparable dans un espace de dimension infinie.

### C. Théorie de l'Information et Mesures de Probabilité
Dans les modèles génératifs comme les WGAN (Wasserstein Generative Adversarial Networks), la distance de Kantorovich-Rubinstein transforme un infimum sur des plans de transport en un supremum sur des fonctions Lipschitziennes. Cette formulation duale est une conséquence élégante de l'extension de formes linéaires, démontrant comment un pur résultat d'analyse abstraite de 1927 devient la clé de voûte de l'optimisation de réseaux de neurones profonds.
