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

# Jalon 81 : Transformée de Fourier dans $L^2$ et Plancherel

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez une lampe torche magique.
    - Dans le monde réel, vous voyez des objets (le signal $f$).
    - Quand vous allumez la lampe, les objets se transforment en ombres colorées sur le mur (les fréquences $\hat{f}$).
    - L'**Isométrie de Plancherel**, c'est la garantie que la luminosité totale de la lampe reste la même, que vous regardiez l'objet ou son ombre. L'énergie n'est ni créée ni détruite par la transformation de Fourier.
    - Mieux encore : cette lampe marche pour TOUS les objets qui ont une énergie finie (espace $L^2$), même ceux qui sont infiniment longs et que vous ne pouviez pas mesurer avec les outils du Jalon 80.
- **Le "Pourquoi on a inventé ça" :** La définition du Jalon 80 (intégrale directe) ne marche que si la fonction décroît assez vite vers zéro ($L^1$). Mais en physique, beaucoup de signaux (comme une onde sinusoïdale pure) ne sont pas dans $L^1$. Le théorème de Plancherel permet d'étendre la transformée de Fourier à tout l'espace $L^2$, rendant l'outil enfin universel pour les ingénieurs.
- **Visualisation :** Une rotation dans l'espace de Hilbert. Comme une rotation en 3D ne change pas la longueur d'un vecteur, la transformée de Fourier "tourne" notre fonction du domaine temporel vers le domaine fréquentiel sans changer sa "longueur" (son énergie).

## 2. Formalisation

Soit $L^2(\mathbb{R})$ l'espace des fonctions dont le carré est intégrable.

### A. Prolongement par densité

La transformée de Fourier $\mathcal{F}$ est initialement définie sur $L^1 \cap L^2$ (qui est dense dans $L^2$).

> **Théorème de Plancherel :**
> L'application $\mathcal{F} : L^1 \cap L^2 \to L^2$ est une isométrie (à une constante près). Elle se prolonge de manière unique en un isomorphisme d'espaces de Hilbert sur $L^2$ tout entier.
> Pour tout $f \in L^2(\mathbb{R})$, on a l'égalité des normes :
> $$\|\hat{f}\|_2 = \sqrt{2\pi} \|f\|_2 \quad \text{(Convention : } \hat{f}(\xi) = \int f(t) e^{-i\xi t} dt \text{)}$$

### B. Conséquence : Théorème d'Inversion

> **Théorème :** La transformée de Fourier est une bijection de $L^2(\mathbb{R})$ sur lui-même. Son inverse est donnée par :
> $$f(t) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{f}(\xi) e^{i\xi t} d\xi$$
> (L'intégrale est ici une limite au sens $L^2$).

## 3. Démonstrations

### Esquisse de la preuve du prolongement

1. **Étape 1 : Isométrie sur $\mathcal{C}_c$**
   Pour $f, g \in \mathcal{S}$ (fonctions de Schwartz ou $\mathcal{C}_c$), on montre par un calcul direct (utilisant Fubini et l'intégrale de Gauss) que $\langle \hat{f}, \hat{g} \rangle = 2\pi \langle f, g \rangle$.
2. **Étape 2 : Densité**
   Comme $L^1 \cap L^2$ est dense dans $L^2$ (Jalon 77), pour tout $f \in L^2$, il existe une suite $f_n \in L^1 \cap L^2$ telle que $f_n \to f$ dans $L^2$.
3. **Étape 3 : Suites de Cauchy**
   Par l'isométrie démontrée à l'étape 1 : $\|\hat{f}_n - \hat{f}_m\|_2 = \sqrt{2\pi} \|f_n - f_m\|_2$.
   Comme $(f_n)$ est de Cauchy, $(\hat{f}_n)$ est aussi de Cauchy dans $L^2$.
4. **Étape 4 : Complétude**
   Comme $L^2$ est complet (Riesz-Fischer, Jalon 75), la suite $(\hat{f}_n)$ converge vers une limite que l'on définit comme étant $\hat{f}$.
5. **Conclusion :** La transformée de Fourier est définie sur $L^2$ par passage à la limite.

## 4. Exercices d'Application

### Exercice 1 : Transformée du Sinus Cardinal
**Énoncé :** On sait que $\mathcal{F}(\mathbf{1}_{[-1, 1]}) = 2 \text{sinc}(\xi)$. En déduire la transformée de Fourier de $f(x) = \text{sinc}(x)$.
**Correction Détaillée :**
Par la formule d'inversion $L^2$ : si $\hat{g} = h$, alors $\hat{h} = 2\pi \check{g}$ (où $\check{g}(x) = g(-x)$).
Ici, $g = \mathbf{1}_{[-1, 1]}$ et $h = 2\text{sinc}$.
Donc $\mathcal{F}(2\text{sinc}) = 2\pi \mathbf{1}_{[-1, 1]}$ (car l'indicatrice est paire).
Par linéarité : $\hat{f}(\xi) = \pi \mathbf{1}_{[-1, 1]}(\xi)$.
**Conclusion :** Le sinus cardinal (signal qui dure "longtemps") a une transformée de Fourier qui est une porte (spectre limité). C'est le principe du filtrage idéal.

### Exercice 2 : Niveau Avancé (Conservation du produit scalaire)
**Énoncé :** Montrer que $\int f(x) \overline{g(x)} dx = \frac{1}{2\pi} \int \hat{f}(\xi) \overline{\hat{g}(\xi)} d\xi$.
**Correction Détaillée :**
C'est l'identité de Parseval-Plancherel. Elle découle directement du fait que $\mathcal{F}$ est une isométrie (à un facteur près) sur un espace de Hilbert.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Plancherel permet de définir la **Densité Spectrale de Puissance** (PSD). En IA, pour analyser des séries temporelles (vent, électricité, battements de cœur), on ne regarde pas le signal mais son énergie par bande de fréquence.
- **Example Concret :**
    - **Normalisation Spectrale (Spectral Norm) :** Dans les GANs de pointe (SNGAN), on contraint la plus grande valeur propre (valeur singulière) de la matrice de poids. En continu, cela revient à borner la norme de la transformée de Fourier de l'opérateur de convolution. Cela garantit que le réseau est lipschitzien et stable.
    - **Génération d'images (StyleGAN) :** L'analyse fréquentielle via Plancherel permet de séparer les "styles" (basses fréquences pour la forme du visage, hautes fréquences pour les pores de la peau). On peut alors mixer les énergies de deux images pour en créer une troisième.
    - **Algorithmes de compression sans perte :** L'isométrie garantit qu'en travaillant dans l'espace de Fourier, on dispose de toute l'information nécessaire pour reconstruire le signal original sans aucune distorsion d'énergie.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 80 (Transformée de Fourier dans L1).md]], [[Jalon 75 (Preuve de la complétude des espaces Lp).md]]
- **Concepts Futurs dépendants :** [[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]], [[Jalon 115 (Démonstration du théorème de Stokes généralisé).md]]
