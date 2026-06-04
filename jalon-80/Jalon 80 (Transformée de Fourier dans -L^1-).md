---
uuid: "jalon-80"
title: "Transformée de Fourier dans L1"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 79 (Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.).md]]"
next: "[[Jalon 81 (Transformée de Fourier dans L2).md]]"
---

# Jalon 80 : Transformée de Fourier dans $L^1$

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous parliez. Votre voix n'est pas un son qui se répète en boucle à l'infini (comme une sirène), c'est un flux de sons qui changent tout le temps.
    - Les **Séries de Fourier** (Jalon 78) étaient faites pour les sons répétitifs.
    - La **Transformée de Fourier**, c'est l'outil pour les sons qui ne se répètent pas. C'est comme un prisme qui prend un rayon de lumière blanche (un signal ponctuel) et l'étale pour montrer toutes les couleurs de l'arc-en-ciel (toutes les fréquences) qui le composent.
    - Au lieu d'avoir une liste de notes discrètes (Do, Ré, Mi), vous avez un curseur continu qui parcourt toutes les hauteurs de son possibles.
- **Le "Pourquoi on a inventé ça" :** Pour résoudre des équations où les choses se passent sur toute la droite réelle (de $-\infty$ à $+\infty$). La transformée de Fourier a une propriété magique : elle transforme la dérivation (opération difficile) en une simple multiplication (opération facile).
- **Visualisation :** On passe d'un graphique "Amplitude en fonction du temps" à un graphique "Amplitude en fonction de la fréquence". Une cloche très large dans le temps devient une cloche très étroite dans les fréquences, et vice versa (Principe d'incertitude).

## 2. Formalisation & Rigueur Académique

Soit $L^1(\mathbb{R})$ l'espace des fonctions intégrables par rapport à la mesure de Lebesgue.

### A. Définition

> **Définition (Transformée de Fourier) :**
> Pour toute fonction $f \in L^1(\mathbb{R})$, on définit sa transformée de Fourier $\hat{f}$ (ou $\mathcal{F}f$) par :
> $$\forall \xi \in \mathbb{R}, \quad \hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t) e^{-i\xi t} dt$$
> *Note :* La fonction $\hat{f}$ est bornée et continue sur $\mathbb{R}$.

### B. Propriétés Fondamentales

> **Lemme de Riemann-Lebesgue :**
> Si $f \in L^1(\mathbb{R})$, alors $\lim_{|\xi| \to \infty} \hat{f}(\xi) = 0$.
> (Les très hautes fréquences finissent par s'annuler).

> **Théorème de la Dérivée :**
> Si $f \in L^1$ est de classe $\mathcal{C}^1$ et $f' \in L^1$, alors :
> $$\widehat{f'}(\xi) = i\xi \hat{f}(\xi)$$

### C. Produit de Convolution

> **Définition (Convolution) :** $(f * g)(t) = \int f(t-s) g(s) ds$.
> **Théorème :** $\widehat{f * g} = \hat{f} \cdot \hat{g}$.
> La transformée d'une convolution est le produit des transformées.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Transformée de la dérivée

1. **Cadre :** Soit $f \in \mathcal{C}^1 \cap L^1$ telle que $f' \in L^1$. Comme $f'$ est intégrable, $f$ admet des limites nulles en $\pm \infty$.
2. **Définition :** $\widehat{f'}(\xi) = \int_{-\infty}^{+\infty} f'(t) e^{-i\xi t} dt$.
3. **Intégration par parties (IPP) :**
   Posons $u = e^{-i\xi t} \implies u' = -i\xi e^{-i\xi t}$.
   Posons $v' = f'(t) \implies v = f(t)$.
4. **Calcul :**
   $$\widehat{f'}(\xi) = [f(t) e^{-i\xi t}]_{-\infty}^{+\infty} - \int_{-\infty}^{+\infty} f(t) (-i\xi e^{-i\xi t}) dt$$
5. **Analyse des termes :**
   - Le terme entre crochets est nul car $f(\pm \infty) = 0$.
   - Le second terme devient : $+i\xi \int f(t) e^{-i\xi t} dt = i\xi \hat{f}(\xi)$.
6. **Conclusion :** $\widehat{f'}(\xi) = i\xi \hat{f}(\xi)$. Dériver revient à multiplier par la fréquence.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Transformée d'une porte (Cénneau)
**Énoncé :** Calculer la transformée de Fourier de $f = \mathbf{1}_{[-a, a]}$.
**Correction Détaillée :**
1. $\hat{f}(\xi) = \int_{-a}^a 1 \cdot e^{-i\xi t} dt$.
2. $\hat{f}(\xi) = [\frac{e^{-i\xi t}}{-i\xi}]_{-a}^a = \frac{e^{-i\xi a} - e^{i\xi a}}{-i\xi}$.
3. On utilise Euler : $\sin(\xi a) = \frac{e^{i\xi a} - e^{-i\xi a}}{2i}$.
4. $\hat{f}(\xi) = \frac{-2i \sin(\xi a)}{-i\xi} = 2a \frac{\sin(\xi a)}{\xi a} = 2a \text{sinc}(\xi a)$.
**Résultat :** Un signal rectangulaire a pour transformée un sinus cardinal.

### Exercice 2 : Niveau Avancé (La Gaussienne)
**Énoncé :** Montrer que la transformée de Fourier de $g(x) = e^{-x^2/2}$ est proportionnelle à elle-même.
**Correction Détaillée :**
On montre que $\hat{g}$ vérifie la même équation différentielle que $g$.
$g'(x) = -x g(x)$.
En passant en Fourier : $i\xi \hat{g}(\xi) = - \widehat{xg}(\xi) = - (i \frac{d}{d\xi} \hat{g}(\xi))$.
D'où $\hat{g}'(\xi) = -\xi \hat{g}(\xi)$, ce qui implique $\hat{g}(\xi) = C e^{-\xi^2/2}$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** La transformée de Fourier est l'outil fondamental de la **Théorie des Probabilités** (sous le nom de **Fonction Caractéristique**, Jalon 93). Elle permet de manipuler les sommes de variables aléatoires via des produits de fonctions.
- **Example Concret :**
    - **Convolutional Neural Networks (CNNs) :** La couche de convolution d'un réseau est littéralement un produit de transformées de Fourier dans l'espace des fréquences. Les architectures "FFT-based Conv" utilisent cette propriété pour être beaucoup plus rapides sur de grandes images.
    - **Algorithmes de compression (Audio/Image) :** La transformée en cosinus discrète (DCT), une variante de Fourier, est le cœur du format **JPEG** et du **MP3**. On ne garde que les fréquences basses car l'œil et l'oreille y sont plus sensibles.
    - **Signal Denoising :** Pour nettoyer un signal bruité, on le passe en Fourier, on coupe les hautes fréquences (le bruit), et on revient dans le temps. C'est le principe des filtres utilisés pour nettoyer les données avant l'entrée dans un modèle d'IA.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 39 (Intégrales généralisées sur un intervalle quelconque et critères de convergence.).md]], [[Jalon 73 (Espaces Lp et passage au quotient).md]]
- **Concepts Futurs dépendants :** [[Jalon 81 (Transformée de Fourier dans L2).md]], [[Jalon 93 (Fonctions caractéristiques).md]]
