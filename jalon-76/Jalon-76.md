---
uuid: "jalon-76"
title: "Propriétés géométriques de l'espace de Hilbert L2"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 75 (Preuve de la complétude des espaces Lp).md]]"
next: "[[Jalon 77 (Densité des fonctions simples).md]]"
---

# Jalon 76 : Propriétés géométriques de l'espace de Hilbert $L^2$

## 1. Introduction

L'étude des espaces de fonctions a connu une révolution conceptuelle majeure au début du XXe siècle. Historiquement, l'analyse mathématique peinait à unifier l'étude des séries de Fourier et la géométrie des espaces vectoriels de dimension infinie. Le problème central résidait dans l'absence d'une structure permettant de mesurer des angles, de définir l'orthogonalité et d'appliquer le théorème de Pythagore dans des espaces de fonctions, de la même manière que dans l'espace euclidien $\mathbb{R}^3$.

David Hilbert et John von Neumann ont introduit le concept d'espace de Hilbert pour répondre à ce besoin. L'espace $L^2$, constitué des fonctions de carré intégrable, est le prototype absolu de cette structure. Dans cet espace, l'énergie d'un signal (mesurée par son intégrale quadratique) devient une norme euclidienne. L'intuition physique est directe : dans le traitement du signal, si deux ondes ne partagent aucune fréquence commune, leurs énergies s'additionnent sans interférence, ce qui se traduit mathématiquement par l'orthogonalité de deux vecteurs dans $L^2$.

Visualisons l'espace $L^2$ non pas comme un ensemble amorphe de fonctions, mais comme un espace infiniment dimensionnel où chaque fonction est un vecteur. La sphère unité dans cet espace est parfaitement "ronde", sans coins, garantissant l'existence et l'unicité de la projection d'un point sur un sous-espace fermé.

## 2. Définitions, Théorèmes & Exemples

### A. Définition de l'espace $L^2$ et Produit Scalaire

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

**Définition (Espace $L^2$) :**
L'espace $\mathcal{L}^2(X, \mu)$ est l'espace vectoriel des fonctions mesurables $f : X \to \mathbb{C}$ (ou $\mathbb{R}$) telles que :
$$ \int_X |f(x)|^2 d\mu(x) < \infty $$
L'espace $L^2(X, \mu)$ est le quotient de $\mathcal{L}^2(X, \mu)$ par la relation d'équivalence $f \sim g \iff f = g \text{ presque partout}$.

**Définition (Produit Scalaire) :**
Pour $f, g \in L^2(X, \mu)$, on définit le produit scalaire sesquilinéaire (ou bilinéaire dans le cas réel) par :
$$ \langle f, g \rangle_{L^2} = \int_X f(x) \overline{g(x)} d\mu(x) $$

**Exemple Concret (Orthogonalité dans $L^2([-\pi, \pi])$) :**
Considérons l'espace mesuré $([-\pi, \pi], \mathcal{B}([-\pi, \pi]), \frac{dx}{2\pi})$ et les fonctions $f(x) = \cos(x)$ et $g(x) = \sin(x)$.
Calculons leur produit scalaire :
$$ \langle f, g \rangle = \frac{1}{2\pi} \int_{-\pi}^{\pi} \cos(x) \sin(x) dx $$
En utilisant l'identité $\cos(x)\sin(x) = \frac{1}{2}\sin(2x)$, on obtient :
$$ \langle f, g \rangle = \frac{1}{4\pi} \int_{-\pi}^{\pi} \sin(2x) dx = \frac{1}{4\pi} \left[ -\frac{\cos(2x)}{2} \right]_{-\pi}^{\pi} = \frac{1}{4\pi} \left( -\frac{1}{2} - \left(-\frac{1}{2}\right) \right) = 0 $$
Les fonctions $f$ et $g$ sont donc orthogonales dans $L^2$.

### B. Inégalité de Cauchy-Schwarz et Norme

**Théorème (Inégalité de Cauchy-Schwarz) :**
Pour toutes $f, g \in L^2(X, \mu)$, le produit $f \overline{g}$ est intégrable (i.e., $f \overline{g} \in L^1(X, \mu)$) et l'on a :
$$ |\langle f, g \rangle_{L^2}| \le \|f\|_{L^2} \|g\|_{L^2} $$
où $\|f\|_{L^2} = \left( \int_X |f(x)|^2 d\mu(x) \right)^{1/2}$.

**Exemple d'application numérique :**
Prenons $X = [0, 1]$ avec la mesure de Lebesgue, $f(x) = x$ et $g(x) = x^2$.
$$ \langle f, g \rangle = \int_0^1 x \cdot x^2 dx = \int_0^1 x^3 dx = \frac{1}{4} $$
Calculons les normes :
$$ \|f\|_{L^2}^2 = \int_0^1 x^2 dx = \frac{1}{3} \implies \|f\|_{L^2} = \frac{1}{\sqrt{3}} $$
$$ \|g\|_{L^2}^2 = \int_0^1 x^4 dx = \frac{1}{5} \implies \|g\|_{L^2} = \frac{1}{\sqrt{5}} $$
L'inégalité stipule que $\frac{1}{4} \le \frac{1}{\sqrt{15}}$. On vérifie que $\frac{1}{16} \le \frac{1}{15}$, ce qui est bien correct.

### C. Identité du Parallélogramme

L'identité du parallélogramme caractérise géométriquement les normes issues d'un produit scalaire. C'est elle qui assure la "rotondité" parfaite de la boule unité de $L^2$.

**Théorème (Identité du Parallélogramme) :**
Pour toutes $f, g \in L^2(X, \mu)$, on a :
$$ \|f + g\|_{L^2}^2 + \|f - g\|_{L^2}^2 = 2\left(\|f\|_{L^2}^2 + \|g\|_{L^2}^2\right) $$

**Contre-exemple (Espace $L^1$) :**
Considérons $L^1(\mathbb{R})$ avec $f = \mathbf{1}_{[0, 1]}$ et $g = \mathbf{1}_{[1, 2]}$.
On a $\|f\|_{L^1} = 1$ et $\|g\|_{L^1} = 1$.
$f + g = \mathbf{1}_{[0, 2]} \implies \|f + g\|_{L^1} = 2$.
$f - g = \mathbf{1}_{[0, 1]} - \mathbf{1}_{[1, 2]} \implies \|f - g\|_{L^1} = 2$.
Dans l'identité du parallélogramme, le membre de gauche vaudrait $2^2 + 2^2 = 8$. Le membre de droite vaudrait $2(1^2 + 1^2) = 4$. L'égalité est fausse, donc $L^1$ n'est pas un espace de Hilbert.

## 3. Démonstrations

### Démonstration de l'Identité du Parallélogramme

Cette démonstration repose exclusivement sur les propriétés algébriques du produit scalaire (bilinéarité et symétrie hermitienne). Soient $f, g \in L^2(X, \mu)$.

1.  **Développement de $\|f + g\|^2$ :**
    Par définition, $\|h\|^2 = \langle h, h \rangle$.
    $$ \|f + g\|^2 = \langle f + g, f + g \rangle $$
    En utilisant la linéarité par rapport à la première variable et l'antilinéarité par rapport à la seconde :
    $$ \|f + g\|^2 = \langle f, f \rangle + \langle f, g \rangle + \langle g, f \rangle + \langle g, g \rangle $$
    $$ \|f + g\|^2 = \|f\|^2 + \langle f, g \rangle + \overline{\langle f, g \rangle} + \|g\|^2 $$
    $$ \|f + g\|^2 = \|f\|^2 + 2 \text{Re}(\langle f, g \rangle) + \|g\|^2 $$

2.  **Développement de $\|f - g\|^2$ :**
    De manière analogue :
    $$ \|f - g\|^2 = \langle f - g, f - g \rangle $$
    $$ \|f - g\|^2 = \langle f, f \rangle - \langle f, g \rangle - \langle g, f \rangle + \langle g, g \rangle $$
    $$ \|f - g\|^2 = \|f\|^2 - \langle f, g \rangle - \overline{\langle f, g \rangle} + \|g\|^2 $$
    $$ \|f - g\|^2 = \|f\|^2 - 2 \text{Re}(\langle f, g \rangle) + \|g\|^2 $$

3.  **Conclusion par sommation :**
    En additionnant membre à membre les deux égalités obtenues :
    $$ \|f + g\|^2 + \|f - g\|^2 = \left( \|f\|^2 + 2 \text{Re}(\langle f, g \rangle) + \|g\|^2 \right) + \left( \|f\|^2 - 2 \text{Re}(\langle f, g \rangle) + \|g\|^2 \right) $$
    Les termes croisés $2 \text{Re}(\langle f, g \rangle)$ et $- 2 \text{Re}(\langle f, g \rangle)$ s'annulent :
    $$ \|f + g\|^2 + \|f - g\|^2 = 2\|f\|^2 + 2\|g\|^2 = 2\left(\|f\|^2 + \|g\|^2\right) $$
    L'identité du parallélogramme est ainsi rigoureusement démontrée.

### Démonstration du Théorème de Pythagore Généralisé

Si $f_1, \dots, f_n$ sont des éléments de $L^2(X, \mu)$ deux à deux orthogonaux (i.e., $\langle f_i, f_j \rangle = 0$ pour tout $i \neq j$), alors :
$$ \left\| \sum_{i=1}^n f_i \right\|^2 = \sum_{i=1}^n \|f_i\|^2 $$

1.  **Initialisation :**
    On développe le carré de la norme de la somme :
    $$ \left\| \sum_{i=1}^n f_i \right\|^2 = \left\langle \sum_{i=1}^n f_i, \sum_{j=1}^n f_j \right\rangle $$

2.  **Développement :**
    Par bilinéarité du produit scalaire :
    $$ \left\langle \sum_{i=1}^n f_i, \sum_{j=1}^n f_j \right\rangle = \sum_{i=1}^n \sum_{j=1}^n \langle f_i, f_j \rangle $$

3.  **Application de l'orthogonalité :**
    Puisque $\langle f_i, f_j \rangle = 0$ lorsque $i \neq j$, seuls les termes de la diagonale ($i = j$) subsistent dans la double somme :
    $$ \sum_{i=1}^n \sum_{j=1}^n \langle f_i, f_j \rangle = \sum_{i=1}^n \langle f_i, f_i \rangle $$
    $$ \sum_{i=1}^n \langle f_i, f_i \rangle = \sum_{i=1}^n \|f_i\|^2 $$
    Ce qui achève la démonstration.

## 4. Applications en Physique, Logique & IA

L'espace $L^2$ n'est pas qu'une abstraction mathématique ; c'est le cadre opérationnel fondamental de plusieurs domaines :

-   **Traitement du Signal et de l'Image (Transformée de Fourier) :** En IA, lorsqu'on analyse des signaux audio (Speech-to-Text) avec des MFCC ou des spectrogrammes, on exploite le fait que l'espace des signaux d'énergie finie est $L^2$. Les exponentielles complexes $e^{inx}$ forment une base hilbertienne, permettant la décomposition et la compression sans perte conceptuelle grâce à l'égalité de Parseval (Théorème de Pythagore en dimension infinie).
-   **Mécanique Quantique :** L'espace d'états d'un système quantique est formellement un espace de Hilbert $L^2$. La fonction d'onde $\psi(x)$ donne la densité de probabilité de présence via $|\psi(x)|^2$. Le fait que $\|\psi\|^2 = 1$ (probabilité totale de 1) nécessite la structure géométrique de $L^2$.
-   **Méthodes à Noyaux (Kernel Machines) en Machine Learning :** Les SVM (Support Vector Machines) et l'astuce du noyau (Kernel Trick) s'appuient sur les espaces de Hilbert à noyau reproduisant (RKHS). Les produits scalaires $\langle \Phi(x), \Phi(y) \rangle$ dans ces espaces, qui peuvent être équivalents à $L^2$ avec une mesure appropriée, permettent de résoudre des problèmes de classification non linéaires en projetant les données dans un espace de dimension infinie où l'hyperplan séparateur est bien défini.
