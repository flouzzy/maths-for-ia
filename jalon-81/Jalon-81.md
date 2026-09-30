---
uuid: "jalon-81"
title: "Transformée de Fourier dans L2 et Plancherel"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 80 (Transformée de Fourier dans L1).md]]"
next: "[[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]]"
---
# Jalon 81 : Transformée de Fourier dans $L^2$ et Théorème de Plancherel

## Introduction

La transformée de Fourier, initialement définie pour les fonctions de l'espace $L^1(\mathbb{R})$, est un outil puissant pour l'analyse harmonique. Cependant, l'espace $L^1$ ne possède pas de structure hilbertienne, contrairement à l'espace $L^2(\mathbb{R})$ des fonctions de carré intégrable, qui est fondamental en mécanique quantique et en théorie du signal (où le carré de la norme représente l'énergie).

Le défi majeur réside dans le fait que l'intégrale définissant la transformée de Fourier ne converge pas absolument pour une fonction $f \in L^2(\mathbb{R})$ quelconque. La construction de la transformée de Fourier sur $L^2(\mathbb{R})$ requiert donc une approche par prolongement continu. Ce passage est rendu possible par le théorème de Plancherel, qui établit que la transformée de Fourier, convenablement normalisée, agit comme une isométrie sur l'espace dense $L^1 \cap L^2$.

## Théorème de Plancherel et Prolongement par Densité

### Définitions et Théorème de Plancherel

Soit $\mathcal{S}(\mathbb{R})$ l'espace de Schwartz des fonctions à décroissance rapide. L'espace $\mathcal{S}(\mathbb{R})$ est dense à la fois dans $L^1(\mathbb{R})$ et dans $L^2(\mathbb{R})$. Pour $f \in L^1(\mathbb{R})$, la transformée de Fourier est définie par :
$$ \hat{f}(\xi) = \mathcal{F}(f)(\xi) = \int_{\mathbb{R}} f(t) e^{-i\xi t} dt $$

**Théorème (Plancherel-Parseval sur l'espace de Schwartz) :**
Pour toute fonction $f \in \mathcal{S}(\mathbb{R})$, sa transformée de Fourier $\hat{f}$ appartient également à $\mathcal{S}(\mathbb{R})$, et l'identité suivante (identité de Plancherel) est vérifiée :
$$ \|\hat{f}\|_{L^2}^2 = 2\pi \|f\|_{L^2}^2 $$
Autrement dit, $\int_{\mathbb{R}} |\hat{f}(\xi)|^2 d\xi = 2\pi \int_{\mathbb{R}} |f(t)|^2 dt$.

**Exemple 1 : Vérification pour la fonction gaussienne**
Considérons la fonction gaussienne normalisée $f(t) = e^{-t^2/2}$.
Sa norme $L^2$ au carré est :
$$ \|f\|_{L^2}^2 = \int_{\mathbb{R}} (e^{-t^2/2})^2 dt = \int_{\mathbb{R}} e^{-t^2} dt = \sqrt{\pi} $$
Sa transformée de Fourier est bien connue (caractère propre de la gaussienne) : $\hat{f}(\xi) = \sqrt{2\pi} e^{-\xi^2/2}$.
Calculons la norme $L^2$ au carré de $\hat{f}$ :
$$ \|\hat{f}\|_{L^2}^2 = \int_{\mathbb{R}} (\sqrt{2\pi} e^{-\xi^2/2})^2 d\xi = 2\pi \int_{\mathbb{R}} e^{-\xi^2} d\xi = 2\pi \sqrt{\pi} $$
On vérifie immédiatement que $\|\hat{f}\|_{L^2}^2 = 2\pi \|f\|_{L^2}^2$, conformément au théorème de Plancherel.

### Le processus de prolongement

L'application $\mathcal{F} : \mathcal{S}(\mathbb{R}) \to L^2(\mathbb{R})$ est donc une application linéaire continue vis-à-vis de la topologie de $L^2$ (à une constante $\sqrt{2\pi}$ près).

Puisque $\mathcal{S}(\mathbb{R})$ est un sous-espace dense de $L^2(\mathbb{R})$, le théorème de prolongement des applications uniformément continues permet d'étendre de manière unique cette application à l'espace complet $L^2(\mathbb{R})$.

**Théorème (Transformée de Fourier dans $L^2$) :**
Il existe un unique prolongement linéaire continu de la transformée de Fourier de $\mathcal{S}(\mathbb{R})$ (ou de $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$) à $L^2(\mathbb{R})$, que nous noterons encore $\mathcal{F}$.
Pour tout $f \in L^2(\mathbb{R})$, $\mathcal{F}(f) \in L^2(\mathbb{R})$ et l'égalité $\|\mathcal{F}(f)\|_{L^2} = \sqrt{2\pi} \|f\|_{L^2}$ reste vraie.

Concrètement, pour $f \in L^2(\mathbb{R})$, la transformée de Fourier est définie comme la limite dans $L^2$ des transformées tronquées :
$$ \hat{f} = \lim_{R \to \infty}^{(L^2)} \int_{-R}^{R} f(t) e^{-i\xi t} dt $$
Cette limite est prise au sens de la norme $L^2$, c'est-à-dire que $\lim_{R \to \infty} \left\| \hat{f}(\cdot) - \int_{-R}^{R} f(t) e^{-i(\cdot)t} dt \right\|_{L^2} = 0$.

**Exemple 2 : Fonction porte et sinus cardinal**
Considérons la fonction indicatrice (ou "porte") $f(t) = \mathbf{1}_{[-a, a]}(t)$ pour $a > 0$. Clairement, $f \in L^1 \cap L^2$.
Sa transformée de Fourier se calcule directement :
$$ \hat{f}(\xi) = \int_{-a}^{a} e^{-i\xi t} dt = \left[ \frac{e^{-i\xi t}}{-i\xi} \right]_{-a}^{a} = \frac{e^{i\xi a} - e^{-i\xi a}}{i\xi} = \frac{2\sin(a\xi)}{\xi} = 2a \, \text{sinc}(a\xi) $$
Vérifions Plancherel.
L'énergie de $f$ est $\|f\|_{L^2}^2 = \int_{-a}^{a} 1^2 dt = 2a$.
L'énergie de $\hat{f}$ est $\|\hat{f}\|_{L^2}^2 = \int_{\mathbb{R}} \left( \frac{2\sin(a\xi)}{\xi} \right)^2 d\xi$.
Par le théorème de Plancherel, $\|\hat{f}\|_{L^2}^2 = 2\pi \times 2a = 4\pi a$.
Nous retrouvons ainsi élégamment l'intégrale de Dirichlet classique de manière indirecte : $\int_{\mathbb{R}} \frac{\sin^2(a\xi)}{\xi^2} d\xi = a\pi$.

## Le Théorème d'Inversion et l'Isomorphisme

Un résultat central de la théorie de Fourier sur $L^2$ est que l'opérateur de Fourier, à normalisation près, est un opérateur unitaire.

**Théorème (Inversion de Fourier dans $L^2$) :**
L'opérateur $\frac{1}{\sqrt{2\pi}}\mathcal{F}$ est un opérateur unitaire (bijectif et isométrique) de $L^2(\mathbb{R})$ sur lui-même.
En particulier, $\mathcal{F}$ est une bijection de $L^2(\mathbb{R})$ sur lui-même, et la formule d'inversion est vraie presque partout :
$$ f(t) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{f}(\xi) e^{i\xi t} d\xi $$
(L'intégrale étant comprise, là encore, au sens d'une limite $L^2$ de troncatures).

L'identité de Parseval généralisée pour le produit scalaire stipule que pour $f, g \in L^2(\mathbb{R})$ :
$$ \langle f, g \rangle_{L^2} = \frac{1}{2\pi} \langle \hat{f}, \hat{g} \rangle_{L^2} $$
soit
$$ \int_{\mathbb{R}} f(t) \overline{g(t)} dt = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi $$

**Exemple 3 : Produit scalaire de deux fonctions portes**
Soit $f(t) = \mathbf{1}_{[-1, 1]}(t)$ et $g(t) = \mathbf{1}_{[-2, 2]}(t)$.
Le produit scalaire direct dans $L^2$ est :
$$ \langle f, g \rangle = \int_{\mathbb{R}} \mathbf{1}_{[-1, 1]}(t) \mathbf{1}_{[-2, 2]}(t) dt = \int_{-1}^{1} 1 dt = 2 $$
En utilisant les transformées de Fourier, on a $\hat{f}(\xi) = \frac{2\sin(\xi)}{\xi}$ et $\hat{g}(\xi) = \frac{2\sin(2\xi)}{\xi}$.
L'identité de Parseval nous donne :
$$ \frac{1}{2\pi} \int_{\mathbb{R}} \frac{2\sin(\xi)}{\xi} \frac{2\sin(2\xi)}{\xi} d\xi = 2 $$
Ce qui permet d'évaluer une intégrale non triviale : $\int_{\mathbb{R}} \frac{\sin(\xi)\sin(2\xi)}{\xi^2} d\xi = \pi$.

## Démonstrations Pas-à-Pas

### Preuve du théorème de Plancherel pour la classe de Schwartz

Soient $f, g \in \mathcal{S}(\mathbb{R})$. Nous allons montrer l'identité de Parseval $\langle f, g \rangle = \frac{1}{2\pi} \langle \hat{f}, \hat{g} \rangle$. En prenant $f=g$, nous obtiendrons le théorème de Plancherel.

1. **Étape 1 : Formule de Dualité**
Définissons la fonction d'interversion. Pour $f, g \in \mathcal{S}(\mathbb{R})$, considérons l'intégrale double :
$$ I = \int_{\mathbb{R}} \int_{\mathbb{R}} f(x) g(y) e^{-ixy} dx dy $$
Comme $f$ et $g$ sont à décroissance rapide, la fonction intégrande $(x,y) \mapsto f(x)g(y)e^{-ixy}$ est dominée par $|f(x)||g(y)|$, qui est intégrable sur $\mathbb{R}^2$.
Le théorème de Fubini s'applique, et nous pouvons intégrer dans n'importe quel ordre.
Intégration d'abord par rapport à $x$ :
$$ I = \int_{\mathbb{R}} g(y) \left( \int_{\mathbb{R}} f(x) e^{-ixy} dx \right) dy = \int_{\mathbb{R}} g(y) \hat{f}(y) dy $$
Intégration d'abord par rapport à $y$ :
$$ I = \int_{\mathbb{R}} f(x) \left( \int_{\mathbb{R}} g(y) e^{-ixy} dy \right) dx = \int_{\mathbb{R}} f(x) \hat{g}(x) dx $$
Nous obtenons ainsi la formule d'échange :
$$ \int_{\mathbb{R}} \hat{f}(y) g(y) dy = \int_{\mathbb{R}} f(x) \hat{g}(x) dx $$

2. **Étape 2 : Application à la fonction de Gauss**
Soit $f \in \mathcal{S}(\mathbb{R})$. Soit $h(x) = e^{-a x^2 / 2}$ (avec $a > 0$).
Sa transformée est $\hat{h}(\xi) = \sqrt{\frac{2\pi}{a}} e^{-\xi^2 / (2a)}$.
Appliquons la formule d'échange avec $f$ et $h$ :
$$ \int_{\mathbb{R}} \hat{f}(y) e^{-a y^2 / 2} dy = \int_{\mathbb{R}} f(x) \sqrt{\frac{2\pi}{a}} e^{-x^2 / (2a)} dx $$

3. **Étape 3 : Passage à la limite pour construire l'inversion**
Multiplions les deux côtés par $\frac{1}{\sqrt{2\pi}}$ (ou considérons cela en posant $x = \sqrt{a} u$ dans le second membre).
$$ \int_{\mathbb{R}} \hat{f}(y) e^{-a y^2 / 2} dy = \sqrt{2\pi} \int_{\mathbb{R}} f(\sqrt{a}u) e^{-u^2/2} du $$
Prenons la limite quand $a \to 0^+$.
À gauche, $\lim_{a \to 0} e^{-a y^2 / 2} = 1$. Comme $\hat{f} \in \mathcal{S} \subset L^1$, le théorème de convergence dominée s'applique.
À droite, $f(\sqrt{a}u) \to f(0)$. Comme $f$ est bornée (étant dans $\mathcal{S}$), la fonction intégrande est dominée par $M e^{-u^2/2}$, intégrable.
On obtient :
$$ \int_{\mathbb{R}} \hat{f}(y) dy = \sqrt{2\pi} f(0) \int_{\mathbb{R}} e^{-u^2/2} du = \sqrt{2\pi} f(0) \times \sqrt{2\pi} = 2\pi f(0) $$
On en déduit que $f(0) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{f}(y) dy$.
Par translation, en appliquant ce résultat à $f_x(t) = f(t+x)$ dont la transformée est $\hat{f}_x(\xi) = \hat{f}(\xi)e^{i\xi x}$, on obtient la formule d'inversion :
$$ f(x) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{f}(\xi) e^{i\xi x} d\xi $$

4. **Étape 4 : Identité de Parseval et Plancherel**
Nous avons, d'après la formule d'inversion, pour toute fonction $h \in \mathcal{S}$ :
$$ h(x) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{h}(\xi) e^{i\xi x} d\xi $$
Soient $f, g \in \mathcal{S}$. Posons $h = f * g^*$ où $g^*(x) = \overline{g(-x)}$.
On sait que la transformée d'une convolution est le produit des transformées : $\hat{h} = \hat{f} \widehat{g^*}$.
Et $\widehat{g^*}(\xi) = \overline{\hat{g}(\xi)}$.
Ainsi, $\hat{h}(\xi) = \hat{f}(\xi) \overline{\hat{g}(\xi)}$.
Évaluons $h$ en 0 de deux manières.
D'une part, par définition de la convolution :
$$ h(0) = (f * g^*)(0) = \int_{\mathbb{R}} f(t) g^*(0-t) dt = \int_{\mathbb{R}} f(t) \overline{g(t)} dt = \langle f, g \rangle $$
D'autre part, par la formule d'inversion pour $h$ en $x=0$ :
$$ h(0) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{h}(\xi) e^{i\xi \cdot 0} d\xi = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi = \frac{1}{2\pi} \langle \hat{f}, \hat{g} \rangle $$
En égalant les deux expressions, nous obtenons l'identité de Parseval. En prenant $f = g$, nous obtenons l'identité de Plancherel $\|\hat{f}\|_{L^2}^2 = 2\pi \|f\|_{L^2}^2$, ce qui achève la démonstration.

## Applications

### En Physique : Densité Spectrale de Puissance

L'identité de Plancherel est la pierre angulaire du traitement du signal et de la physique quantique. Pour un signal temporel $s(t)$ modélisant par exemple un courant électrique traversant une résistance de $1\,\Omega$, la puissance instantanée dissipée est proportionnelle à $|s(t)|^2$.
L'énergie totale dissipée sur tout le temps est $E = \int_{\mathbb{R}} |s(t)|^2 dt$.
Le théorème de Plancherel énonce que $E = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{s}(\xi)|^2 d\xi$.
La quantité $|\hat{s}(\xi)|^2$ est appelée la **densité spectrale d'énergie**. Elle quantifie la distribution de l'énergie du signal à travers ses différentes fréquences composantes $\xi$. Cette équivalence stipule le principe physique fondamental de conservation de l'énergie entre le domaine temporel et le domaine fréquentiel.

### En Intelligence Artificielle et Analyse de Données

Dans le domaine du Machine Learning et des réseaux de neurones, la transformée de Fourier dans $L^2$ intervient dans :
1.  **L'analyse des opérateurs de convolution :** Dans les réseaux CNN, la convolution par un filtre $w$ dans l'espace temporel équivaut à une multiplication point par point par $\hat{w}$ dans l'espace de Fourier. Plancherel assure que la norme spectrale de l'opérateur (déterminant la constante de Lipschitz du réseau, cruciale pour la robustesse et les WGANs) est directement reliée au supremum de $|\hat{w}(\xi)|$.
2.  **Traitement Audio et Parole :** Les algorithmes d'extraction de caractéristiques comme le MFCC (Mel-Frequency Cepstral Coefficients) s'appuient sur le calcul de la densité spectrale d'énergie (le module au carré de la transformée de Fourier, validé par Plancherel) pour capturer les "formants" du signal vocal, avant d'appliquer des échelles logarithmiques imitant la perception humaine.
