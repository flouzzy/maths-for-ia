---
uuid: "jalon-8"
title: "Applications linéaires, noyau (ker), image (Im) et démonstration du théorème du rang"
year: 1
trimester: 1
tags:
  - math/algebre-lineaire
  - ia/transformation-lineaire
prev: "[[Jalon-7.md]]"
next: "[[Jalon-9.md]]"
---
# Jalon 8 : Applications linéaires, noyau ($\ker$), image ($\text{Im}$) et démonstration du théorème du rang

## 1. Présentation du concept clé

 Imaginez une machine à étirer ou à faire tourner de la pâte à modeler.
  - L'**Application Linéaire**, c'est une machine respectueuse : si vous doublez la quantité de pâte au départ, vous aurez le double à l'arrivée. Si vous mettez deux morceaux de couleurs différentes, le résultat sera le même que si vous les aviez traités séparément puis mélangés.
  - Le **Noyau ($\ker$)**, c'est la "poubelle" de la machine : ce sont tous les morceaux de pâte qui finissent écrasés en un tout petit point (zéro) après le passage dans la machine.
  - L'**Image ($\text{Im}$)**, c'est l'ensemble de toutes les formes que la machine est capable de fabriquer.
  - Le **Théorème du Rang**, c'est la loi de conservation : la complexité totale de votre pâte au départ est égale à la somme de ce qui a été écrasé (Noyau) et de ce qui a été transformé (Image).
 La plupart des phénomènes physiques simples sont linéaires. En IA, transformer une image ou un texte revient souvent à appliquer une suite de ces machines. Savoir ce qui est "perdu" (le noyau) est vital.
 Imaginez projeter l'ombre d'un cube 3D sur une feuille 2D. L'ombre est l'**Image** (2D). La direction de la lumière qui "écrase" la profondeur est le **Noyau** (1D). $3 = 1 + 2$. C'est le théorème du rang !

## 2. Formalisation

### A. Définitions Formelles
Soient $E$ et $F$ deux espaces vectoriels sur un corps commutatif $\mathbb{K}$.
1.  **Application Linéaire ($f : E \to F$) :** Une application $f: E \to F$ est dite linéaire si et seulement si elle vérifie les deux propriétés suivantes :
    -   $\forall x, y \in E, f(x + y) = f(x) + f(y)$ (Additivité).
    -   $\forall \lambda \in \mathbb{K}, \forall x \in E, f(\lambda \cdot x) = \lambda \cdot f(x)$ (Homogénéité).
    L'ensemble des applications linéaires de $E$ dans $F$ est noté $\mathcal{L}(E, F)$.

2.  **Noyau ($\ker f$) :** Le noyau de $f$ est l'ensemble des vecteurs de $E$ dont l'image par $f$ est le vecteur nul de $F$.
    $\ker f = \{ x \in E \mid f(x) = 0_F \}$.
    Le noyau $\ker f$ est un sous-espace vectoriel de $E$.

3.  **Image ($\text{Im } f$) :** L'image de $f$ est l'ensemble de toutes les images des vecteurs de $E$ par $f$.
    $\text{Im } f = f(E) = \{ f(x) \mid x \in E \}$.
    L'image $\text{Im } f$ est un sous-espace vectoriel de $F$.

4.  **Rang ($\text{rg } f$) :** On appelle rang de $f$ la dimension de son image.
    $\text{rg } f = \dim(\text{Im } f)$.

### B. Théorèmes, Propositions & Lemmes
> **Caractérisation de l'injectivité :**
> Une application linéaire $f: E \to F$ est injective si et seulement si son noyau est réduit au vecteur nul de $E$.
> $f \text{ est injective } \iff \ker f = \{ 0_E \}$.

> **Théorème du Rang (Théorème Fondamental) :**
> Soit $E$ un espace vectoriel de dimension finie sur un corps $\mathbb{K}$. Pour toute application linéaire $f : E \to F$ (où $F$ est un $\mathbb{K}$-espace vectoriel), on a la relation fondamentale :
> $$\dim E = \dim(\ker f) + \text{rg}(f)$$

## 3. Démonstrations

### Démonstration du Théorème Pivot : Théorème du Rang
Soient $E$ et $F$ deux $\mathbb{K}$-espaces vectoriels, avec $E$ de dimension finie. Soit $f \in \mathcal{L}(E, F)$ une application linéaire de $E$ vers $F$. Supposons que $\dim E = n$, où $n \in \mathbb{N}$ est un entier naturel.

1.  **Initialisation / Cadre :**
    -   Soit $p$ la dimension du noyau de $f$, notée $p = \dim(\ker f)$. Par définition, $p \in \mathbb{N}$ et $0 \le p \le n$.
    -   Si $p > 0$, soit $\mathcal{B}_{\ker f} = (e_1, ..., e_p)$ une base du sous-espace vectoriel $\ker f$. Si $p=0$, alors $\ker f = \{0_E\}$ et la base est vide.
    -   D'après le théorème de la base incomplète, puisque $\mathcal{B}_{\ker f}$ est une famille libre dans $E$, nous pouvons la compléter en une base de l'espace vectoriel $E$. Soit cette base $\mathcal{B}_E = (e_1, ..., e_p, e_{p+1}, ..., e_n)$, où les vecteurs $e_{p+1}, ..., e_n$ sont choisis de manière appropriée.
    -   Notre objectif est de démontrer que la famille de vecteurs $\mathcal{B}_{\text{Im } f} = (f(e_{p+1}), ..., f(e_n))$ constitue une base de l'image de $f$, $\text{Im } f$. Si cette démonstration est concluante, alors la dimension de l'image sera $\dim(\text{Im } f) = n - p$. En substituant cette relation dans l'équation du théorème du rang, nous obtiendrons $\dim E = \dim(\ker f) + \dim(\text{Im } f)$, c'est-à-dire $n = p + (n-p)$, ce qui validera le théorème.

2.  **Étape 1 : Montrons que la famille $(f(e_{p+1}), ..., f(e_n))$ est génératrice de $\text{Im } f$**
    -   Soit $y$ un vecteur arbitraire appartenant à l'image de $f$, c'est-à-dire $y \in \text{Im } f \subseteq F$.
    -   Par définition de l'image, il existe un vecteur $x \in E$ tel que $y = f(x)$.
    -   Puisque $\mathcal{B}_E = (e_1, ..., e_n)$ est une base de l'espace vectoriel $E$, tout vecteur $x \in E$ peut être exprimé comme une combinaison linéaire unique des vecteurs de cette base. Ainsi, il existe des scalaires uniques $\lambda_1, ..., \lambda_n \in \mathbb{K}$ tels que :
        $x = \sum_{i=1}^n \lambda_i e_i$.
    -   Appliquons l'application linéaire $f$ au vecteur $x$ :
        $y = f\left(\sum_{i=1}^n \lambda_i e_i\right)$.
    -   Par la propriété de linéarité de $f$ (additivité et homogénéité), nous pouvons écrire :
        $y = \sum_{i=1}^n \lambda_i f(e_i)$.
    -   Nous pouvons séparer cette somme en deux parties :
        $y = \sum_{i=1}^p \lambda_i f(e_i) + \sum_{i=p+1}^n \lambda_i f(e_i)$.
    -   Par définition du noyau, pour tout $i \in \{1, ..., p\}$, le vecteur $e_i$ appartient à $\ker f$. Par conséquent, l'image de $e_i$ par $f$ est le vecteur nul de $F$, c'est-à-dire $f(e_i) = 0_F$.
    -   Substituons cette information dans la somme :
        $y = \sum_{i=1}^p \lambda_i \cdot 0_F + \sum_{i=p+1}^n \lambda_i f(e_i)$.
    -   Puisque $\lambda_i \cdot 0_F = 0_F$ pour tout $\lambda_i \in \mathbb{K}$, la première somme est nulle :
        $y = 0_F + \sum_{i=p+1}^n \lambda_i f(e_i)$.
    -   Ainsi, nous obtenons :
        $y = \sum_{i=p+1}^n \lambda_i f(e_i)$.
    -   Puisque tout vecteur $y \in \text{Im } f$ peut être exprimé comme une combinaison linéaire des vecteurs $(f(e_{p+1}), ..., f(e_n))$, la famille $\mathcal{B}_{\text{Im } f} = (f(e_{p+1}), ..., f(e_n))$ est une famille génératrice de $\text{Im } f$.

3.  **Étape 2 : Montrons que la famille $(f(e_{p+1}), ..., f(e_n))$ est libre**
    -   Considérons une combinaison linéaire nulle des vecteurs de la famille $\mathcal{B}_{\text{Im } f}$. Soient $\mu_{p+1}, ..., \mu_n \in \mathbb{K}$ des scalaires tels que :
        $\sum_{i=p+1}^n \mu_i f(e_i) = 0_F$.
    -   En utilisant la linéarité de l'application $f$, nous pouvons réécrire cette somme comme :
        $f\left(\sum_{i=p+1}^n \mu_i e_i\right) = 0_F$.
    -   Par définition du noyau, cela signifie que le vecteur $v = \sum_{i=p+1}^n \mu_i e_i$ appartient à $\ker f$.
    -   Puisque $\mathcal{B}_{\ker f} = (e_1, ..., e_p)$ est une base de $\ker f$, tout vecteur de $\ker f$ peut être exprimé comme une combinaison linéaire des éléments de $\mathcal{B}_{\ker f}$. Par conséquent, il existe des scalaires $\alpha_1, ..., \alpha_p \in \mathbb{K}$ tels que :
        $v = \sum_{j=1}^p \alpha_j e_j$.
    -   Ainsi, nous avons l'égalité :
        $\sum_{i=p+1}^n \mu_i e_i = \sum_{j=1}^p \alpha_j e_j$.
    -   Regroupons tous les termes du même côté de l'équation pour obtenir le vecteur nul $0_E$ :
        $\sum_{i=p+1}^n \mu_i e_i - \sum_{j=1}^p \alpha_j e_j = 0_E$.
    -   Réarrangeons les termes pour correspondre à l'ordre de la base $\mathcal{B}_E$ :
        $\sum_{j=1}^p (-\alpha_j) e_j + \sum_{i=p+1}^n \mu_i e_i = 0_E$.
    -   La famille $\mathcal{B}_E = (e_1, ..., e_p, e_{p+1}, ..., e_n)$ est une base de $E$, ce qui implique qu'elle est une famille libre. Par conséquent, la seule combinaison linéaire de ses vecteurs qui est égale au vecteur nul $0_E$ est celle où tous les coefficients sont nuls.
    -   De l'équation $\sum_{j=1}^p (-\alpha_j) e_j + \sum_{i=p+1}^n \mu_i e_i = 0_E$, il découle que tous les scalaires associés doivent être nuls :
        -   Pour $j \in \{1, ..., p\}$, $-\alpha_j = 0$, ce qui implique $\alpha_j = 0$.
        -   Pour $i \in \{p+1, ..., n\}$, $\mu_i = 0$.
    -   En particulier, tous les scalaires $\mu_i$ pour $i \in \{p+1, ..., n\}$ sont nuls.
    -   Puisque tous les scalaires $\mu_i$ sont nuls, la famille $\mathcal{B}_{\text{Im } f} = (f(e_{p+1}), ..., f(e_n))$ est une famille libre.

4.  **Conclusion :**
    -   Ayant démontré que la famille $(f(e_{p+1}), ..., f(e_n))$ est à la fois génératrice de $\text{Im } f$ et libre, nous pouvons affirmer qu'elle constitue une base de $\text{Im } f$. Le nombre de vecteurs dans cette base est $n - p$.
    -   Par définition du rang, $\text{rg}(f) = \dim(\text{Im } f)$. Donc, nous avons $\text{rg}(f) = n - p$.
    -   En substituant les définitions de $n$ et $p$, nous obtenons : $\text{rg}(f) = \dim E - \dim(\ker f)$.
    -   En réarrangeant les termes, nous obtenons l'énoncé du théorème du rang : $\dim E = \dim(\ker f) + \text{rg}(f)$.

## 4. Exercices d'Application

### Exercice 1 : Application Directe (Noyau et Image)
 Soit $f : \mathbb{R}^3 \to \mathbb{R}^2$ une application définie pour tout $(x,y,z) \in \mathbb{R}^3$ par $f(x,y,z) = (x+y, y+z)$. Déterminer le noyau de $f$, $\ker f$, et le rang de $f$, $\text{rg } f$.

1.  **Détermination du Noyau ($\ker f$) :**
    -   Pour déterminer le noyau de $f$, nous cherchons l'ensemble des vecteurs $(x,y,z) \in \mathbb{R}^3$ tels que $f(x,y,z) = 0_{\mathbb{R}^2}$, où $0_{\mathbb{R}^2} = (0,0)$ est le vecteur nul de l'espace d'arrivée $\mathbb{R}^2$.
    -   Cela conduit au système d'équations linéaires suivant :
        1.  $x+y = 0$
        2.  $y+z = 0$
    -   De la première équation (1), nous déduisons une expression pour $x$ en fonction de $y$ :
        $x = -y$.
    -   De la seconde équation (2), nous déduisons une expression pour $z$ en fonction de $y$ :
        $z = -y$.
    -   Ainsi, tout vecteur $(x,y,z)$ appartenant à $\ker f$ doit être de la forme $(-y, y, -y)$ pour un certain scalaire $y \in \mathbb{R}$.
    -   Nous pouvons factoriser le scalaire $y$ de ce vecteur :
        $(-y, y, -y) = y \cdot (-1, 1, -1)$.
    -   Par conséquent, le noyau de $f$ est l'ensemble des multiples scalaires du vecteur $(-1, 1, -1)$ :
        $\ker f = \{ y \cdot (-1, 1, -1) \mid y \in \mathbb{R} \}$.
    -   Ceci est l'espace vectoriel engendré par le vecteur $(-1, 1, -1)$, noté $\text{Vect}((-1, 1, -1))$.
    -   Le vecteur $(-1, 1, -1)$ est non nul. Par conséquent, il forme une base de $\ker f$.
    -   La dimension du noyau est le nombre de vecteurs dans cette base :
        $\dim(\ker f) = 1$.

2.  **Détermination du Rang ($\text{rg } f$) en utilisant le Théorème du Rang :**
    -   L'espace de départ $E = \mathbb{R}^3$ est de dimension finie, et sa dimension est $\dim \mathbb{R}^3 = 3$.
    -   Nous pouvons appliquer le théorème du rang pour l'application linéaire $f : \mathbb{R}^3 \to \mathbb{R}^2$ :
        $\dim E = \dim(\ker f) + \text{rg}(f)$.
    -   En substituant les valeurs connues de $\dim E$ et $\dim(\ker f)$ :
        $3 = 1 + \text{rg}(f)$.
    -   Par conséquent, nous pouvons calculer le rang de $f$ :
        $\text{rg}(f) = 3 - 1 = 2$.

**Conclusion :**
Le noyau $\ker f$ est une droite vectorielle dans $\mathbb{R}^3$, engendrée par le vecteur $(-1, 1, -1)$. Sa dimension est $\dim(\ker f) = 1$.
Le rang de $f$ est $\text{rg}(f) = 2$. Puisque l'espace d'arrivée $F = \mathbb{R}^2$ a une dimension de 2, et que $\text{Im } f$ est un sous-espace vectoriel de $\mathbb{R}^2$ de dimension 2, il s'ensuit que $\text{Im } f = \mathbb{R}^2$. L'application $f$ est donc surjective.

### Exercice 2 : Niveau Avancé (Projecteurs)
 Soit $E$ un $\mathbb{K}$-espace vectoriel. Soit $p \in \mathcal{L}(E, E)$ un endomorphisme de $E$ (appelé projecteur) tel que $p \circ p = p$, c'est-à-dire $p(p(x)) = p(x)$ pour tout $x \in E$. Démontrer que $E$ est la somme directe du noyau de $p$ et de l'image de $p$, notée $E = \ker p \oplus \text{Im } p$.

Pour démontrer que $E = \ker p \oplus \text{Im } p$, nous devons établir deux conditions :
1.  **Somme :** Pour tout vecteur $x \in E$, il existe au moins un couple de vecteurs $(y, z)$ tel que $y \in \ker p$, $z \in \text{Im } p$ et $x = y + z$. (Ceci montre que $E = \ker p + \text{Im } p$).
2.  **Intersection réduite au vecteur nul :** L'intersection du noyau et de l'image est réduite au vecteur nul de $E$, c'est-à-dire $\ker p \cap \text{Im } p = \{0_E\}$. (Ceci montre que la somme est directe).

1.  **Démonstration de la Somme ($E = \ker p + \text{Im } p$) :**
    -   Soit $x$ un vecteur arbitraire de $E$. Nous cherchons à décomposer $x$ en une somme d'un élément du noyau et d'un élément de l'image.
    -   Considérons la décomposition suivante :
        $x = (x - p(x)) + p(x)$.
    -   Posons $z = p(x)$.
    -   Par définition de l'image, puisque $x \in E$, le vecteur $z = p(x)$ appartient à l'image de $p$, donc $z \in \text{Im } p$.
    -   Posons $y = x - p(x)$.
    -   Pour montrer que $y \in \ker p$, nous devons vérifier que $p(y) = 0_E$. Calculons $p(y)$ :
        $p(y) = p(x - p(x))$.
    -   Par la propriété de linéarité de $p$, nous pouvons distribuer $p$ sur la soustraction :
        $p(x - p(x)) = p(x) - p(p(x))$.
    -   En utilisant la propriété du projecteur $p \circ p = p$, nous savons que $p(p(x)) = p(x)$.
    -   Substituons cette propriété dans l'expression de $p(y)$ :
        $p(y) = p(x) - p(x)$.
    -   Ce qui simplifie à :
        $p(y) = 0_E$.
    -   Par conséquent, $y \in \ker p$.
    -   Nous avons ainsi montré que pour tout $x \in E$, $x$ peut s'écrire comme la somme d'un vecteur $y \in \ker p$ et d'un vecteur $z \in \text{Im } p$. Ceci établit que $E = \ker p + \text{Im } p$.

2.  **Démonstration de l'Intersection réduite au vecteur nul ($\ker p \cap \text{Im } p = \{0_E\}$) :**
    -   Pour démontrer que la somme est directe, nous devons montrer que l'intersection $\ker p \cap \text{Im } p$ est réduite au seul vecteur nul $0_E$.
    -   Soit $u$ un vecteur arbitraire appartenant à cette intersection, c'est-à-dire $u \in \ker p \cap \text{Im } p$.
    -   Puisque $u \in \ker p$, par définition du noyau, nous avons :
        $p(u) = 0_E$.
    -   Puisque $u \in \text{Im } p$, par définition de l'image, il existe un vecteur $v \in E$ tel que :
        $u = p(v)$.
    -   Substituons cette expression de $u$ dans l'équation $p(u) = 0_E$ :
        $p(p(v)) = 0_E$.
    -   En utilisant la propriété du projecteur $p \circ p = p$, nous avons $p(p(v)) = p(v)$.
    -   Donc, l'équation devient :
        $p(v) = 0_E$.
    -   Puisque nous avons établi que $u = p(v)$, nous en déduisons que :
        $u = 0_E$.
    -   L'intersection $\ker p \cap \text{Im } p$ est donc réduite au seul vecteur nul $\{0_E\}$.

**Conclusion :**
Ayant démontré que $E = \ker p + \text{Im } p$ (la somme) et que $\ker p \cap \text{Im } p = \{0_E\}$ (l'intersection est réduite au vecteur nul), nous pouvons conclure que l'espace vectoriel $E$ est la somme directe du noyau de $p$ et de l'image de $p$, c'est-à-dire $E = \ker p \oplus \text{Im } p$.

## 5. Application en Intelligence Artificielle
-   **Le Pont Théorique :** Les couches denses (Dense Layers / Linear Layers) des réseaux de neurones sont des applications affines (Linéaire + Translation). Les concepts d'applications linéaires, de noyau et d'image sont donc directement applicables à la compréhension de ces couches.
-   **Exemple Concret :** Dans la **réduction de dimension** et la **Compression de Réseaux**, on cherche à savoir si une couche linéaire a un gros **Noyau**. Si $\dim(\ker f)$ est grand, cela signifie que beaucoup de combinaisons d'entrées sont "oubliées" ou projetées sur le même point (le vecteur nul) par le réseau, indiquant une redondance ou une faible expressivité dans certaines directions. Le **Rang** de la matrice de poids d'une couche détermine la "capacité expressive" de cette couche, c'est-à-dire la dimension de l'espace des sorties qu'elle peut effectivement générer. Un réseau "Low-Rank" (de faible rang) est plus rapide à entraîner et moins sujet au sur-apprentissage (Overfitting) car il impose une contrainte sur la complexité des transformations qu'il peut effectuer, favorisant ainsi la généralisation.

## 6. Liens Sémantiques
-   **Concepts Précédents requis :** [[Jalon-7.md|Jalon 7 (Espaces vectoriels abstraits)]]
-   **Concepts Futurs dépendants :** [[Jalon-9]], [[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.)]], [[Jalon 46 (Matrice jacobienne)]]
