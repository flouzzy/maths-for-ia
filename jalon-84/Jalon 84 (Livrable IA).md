---
uuid: "jalon-84"
title: "Livrable IA T7 : Analyse spectrale et extraction de caractéristiques audio"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 83 (Dérivation au sens des distributions).md]]"
next: "[[Jalon 85 (Axiomes de Kolmogorov).md]]"
---

# Jalon 84 : Livrable IA T7 : Analyse spectrale et extraction de caractéristiques audio

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous regardiez un orchestre jouer.
    - Le signal audio brut, c'est comme regarder l'orchestre de très loin : vous voyez un groupe de gens qui bougent, mais vous ne savez pas qui fait quoi.
    - L'**Analyse spectrale**, c'est comme avoir des super-pouvoirs qui vous permettent de voir chaque musicien séparément. Vous voyez la flûte qui joue des notes très hautes (hautes fréquences) et la contrebasse qui fait vibrer le sol (basses fréquences).
    - Pour une IA, cette vue "par musicien" est beaucoup plus utile que la vue d'ensemble pour comprendre ce qui est dit ou quel instrument joue. On transforme un son en une "image" de fréquences.
- **Le "Pourquoi on a inventé ça" :** Une onde sonore change trop vite pour qu'une IA puisse l'analyser directement de manière efficace. En passant dans le domaine de Fourier, on extrait les motifs stables (les notes, les voyelles) qui portent le sens de l'information.
- **Visualisation :** Le **Spectrogramme**. C'est une carte où l'axe horizontal est le temps, l'axe vertical est la fréquence, et la couleur indique l'intensité du son à cet instant et à cette fréquence.

## 2. Formalisation

### A. La Transformée de Fourier à Court Terme (STFT)

Comme un signal audio n'est pas stationnaire (les fréquences changent au fil du temps), on ne peut pas faire une seule transformée de Fourier sur tout le signal.

> **Définition 1 (STFT) :**
> Soit $f \in L^2(\mathbb{R})$ un signal et $w$ une fonction de fenêtrage (ex: fenêtre de Hann) à support compact. La STFT de $f$ est définie par :
> $$X(t, \omega) = \int_{-\infty}^{+\infty} f(\tau) w(\tau - t) e^{-i\omega \tau} d\tau$$
> $X(t, \omega)$ donne le contenu fréquentiel du signal "autour" de l'instant $t$.

### B. Le Spectrogramme de Puissance

> **Définition 2 :**
> Le spectrogramme est le carré du module de la STFT :
> $$S(t, \omega) = |X(t, \omega)|^2$$
> Il appartient à $L^1(\mathbb{R} \times \mathbb{R})$ et représente la distribution de l'énergie dans le plan temps-fréquence.

### C. Échelle de Mel (Lien avec la perception)

L'oreille humaine ne perçoit pas les fréquences de manière linéaire. On utilise une transformation logarithmique de l'axe des fréquences appelée **échelle de Mel**.
$$m = 2595 \log_{10}(1 + \frac{f}{700})$$

## 3. Démonstrations

### Justification de la discrétisation (DFT)

En pratique, l'IA travaille sur des signaux discrets de longueur $N$.

1. **Orthogonalité :** Dans $\mathbb{C}^N$, les vecteurs $e_k = [e^{i 2\pi k n / N}]_{n=0 \dots N-1}$ forment une base orthonormée (pour le produit scalaire hermitien usuel).
2. **Projection :** Calculer la transformée de Fourier discrète (DFT) revient à projeter le vecteur signal $x$ sur cette base : $X_k = \langle x, e_k \rangle$.
3. **Inversion :** On peut reconstruire exactement le signal original par $x = \frac{1}{N} \sum X_k e_k$.
4. **Conclusion :** Le spectrogramme discret est une décomposition orthogonale locale du signal. Chaque "bin" de fréquence capture l'énergie d'une bande spécifique.

## 4. Exercices d'Application

### Exercice 1 : Résolution fréquentielle
**Énoncé :** On échantillonne un son à $44100$ Hz. On fait une FFT sur des fenêtres de $1024$ échantillons. Quelle est la largeur de chaque "bin" de fréquence ?
**Correction Détaillée :**
1. La plage de fréquences couverte est de $0$ à $44100$ Hz.
2. Le nombre de points est $1024$.
3. La largeur d'un bin est $\Delta f = \frac{F_s}{N} = \frac{44100}{1024} \approx 43$ Hz.
**Conséquence :** Si deux sons ont des fréquences distantes de moins de $43$ Hz, l'IA ne pourra pas les distinguer dans ce spectrogramme. Pour être plus précis, il faudrait augmenter la taille de la fenêtre (mais on perdrait en précision temporelle : principe d'incertitude de Heisenberg-Gabor).

### Exercice 2 : Niveau Avancé (Fenêtrage et Effet de bord)
**Énoncé :** Pourquoi multiplie-t-on le signal par une fenêtre $w$ (ex: une cloche) avant de faire la FFT ?
**Correction Détaillée :**
Le signal réel est "coupé" brusquement aux bords de la fenêtre. Cette coupure est une discontinuité qui génère des hautes fréquences artificielles en Fourier (Leakage). En utilisant une fenêtre qui s'adoucit vers zéro aux extrémités, on rend le signal périodique de manière fluide, ce qui nettoie le spectre et permet à l'IA de se concentrer sur les vraies fréquences.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** L'analyse spectrale est la couche de **Feature Extraction** obligatoire pour toute IA traitant du son ou des vibrations.
- **Example Concret :**
    - **Reconnaissance vocale (Whisper, Wav2Vec) :** Ces modèles ne prennent pas le son brut. Ils calculent d'abord des **MFCC** (Mel-Frequency Cepstral Coefficients) ou des bancs de filtres Mel. C'est sur ces images temps-fréquence que les Transformers apprennent à reconnaître les mots.
    - **Classification de musique (Shazam) :** L'empreinte digitale d'une chanson est basée sur les "pics" de son spectrogramme. On cherche les points de plus haute énergie dans le plan temps-fréquence pour identifier le morceau.
    - **Analyse de séries temporelles financières :** On utilise Fourier pour détecter des cycles (saisonnalité) dans les cours de bourse ou la consommation d'énergie.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 81 (Transformée de Fourier dans L2).md]], [[Jalon 78 (Séries de Fourier).md]]
- **Concepts Futurs dépendants :** [[Jalon 113 (Tenseurs).md]], [[Jalon 144 (Le phénomène de double descente).md]]
