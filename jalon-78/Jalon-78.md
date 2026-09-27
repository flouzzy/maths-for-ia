---
uuid: "jalon-78"
title: "Séries de Fourier"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 77 (Densité des fonctions simples).md]]"
next: "[[Jalon 79 (Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.).md]]"
---

# Jalon 78 : Séries de Fourier

## 1. Genèse et Intuition Physique

Historiquement, le concept des séries de Fourier prend racine dans les travaux de Joseph Fourier (1822) sur la propagation de la chaleur. À cette époque, la communauté scientifique, menée par Lagrange et Laplace, considérait qu'une fonction arbitraire, surtout si elle présentait des discontinuités ou des points anguleux (comme un signal en "dents de scie"), ne pouvait pas être représentée par une unique expression analytique sur tout son domaine.

Fourier bouleverse cette conception en postulant que *tout* profil de température initial (périodique) peut être décomposé en une somme infinie d'ondes sinusoïdales pures. Géométriquement, cela revient à affirmer que les fonctions trigonométriques forment une "base" de l'espace des fonctions périodiques, tout comme les vecteurs de base engendrent un espace vectoriel. Ainsi, un signal complexe dans le domaine temporel est transformé en un spectre discret dans le domaine fréquentiel. Chaque onde composante est caractérisée par sa fréquence, son amplitude (l'intensité de cette fréquence dans le signal) et sa phase. Cette découverte a fondé l'analyse harmonique, ouvrant la voie non seulement à la thermodynamique, mais aussi au traitement du signal moderne et à la mécanique quantique.

## 2. Définitions, Théorèmes et Exemples

### Espace des fonctions et produit scalaire

Soit $T > 0$. On note $L^2_{per}(0, T)$ l'espace des fonctions $f : \mathbb{R} \to \mathbb{C}$ qui sont $T$-périodiques et de carré intégrable sur une période, c'est-à-dire telles que $\int_0^T |f(t)|^2 dt < +\infty$. On munit cet espace du produit scalaire hermitien suivant (en prenant $T=2\pi$ pour simplifier les notations) :

$$ \langle f, g \rangle = \frac{1}{2\pi} \int_0^{2\pi} \overline{f(t)} g(t) dt $$

**Théorème 1 (Famille orthonormale) :**
La famille de fonctions $(e_n)_{n \in \mathbb{Z}}$ définie par $e_n(t) = e^{int}$ forme une famille orthonormale pour ce produit scalaire. C'est-à-dire :
$$ \langle e_m, e_n \rangle = \delta_{m,n} $$
où $\delta_{m,n}$ est le symbole de Kronecker (1 si $m=n$, 0 sinon).

**Exemple de calcul d'orthogonalité :**
Vérifions que $e_1(t) = e^{it}$ et $e_2(t) = e^{2it}$ sont orthogonales.
$$ \langle e_1, e_2 \rangle = \frac{1}{2\pi} \int_0^{2\pi} \overline{e^{it}} e^{2it} dt = \frac{1}{2\pi} \int_0^{2\pi} e^{-it} e^{2it} dt = \frac{1}{2\pi} \int_0^{2\pi} e^{it} dt $$
$$ \langle e_1, e_2 \rangle = \frac{1}{2\pi} \left[ \frac{e^{it}}{i} \right]_0^{2\pi} = \frac{1}{2\pi i} (e^{2i\pi} - e^0) = \frac{1}{2\pi i} (1 - 1) = 0 $$

### Coefficients de Fourier

**Définition 1 (Coefficients complexes) :**
Pour tout entier $n \in \mathbb{Z}$, on définit le $n$-ième coefficient de Fourier exponentiel de $f \in L^1_{per}(0, 2\pi)$ par :
$$ c_n(f) = \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt $$

**Définition 2 (Coefficients trigonométriques réels) :**
Si $f$ est à valeurs réelles, on peut également utiliser la décomposition en cosinus et sinus. On définit les coefficients réels pour $n \in \mathbb{N}$ par :
$$ a_n(f) = \frac{1}{\pi} \int_0^{2\pi} f(t) \cos(nt) dt \quad \text{et} \quad b_n(f) = \frac{1}{\pi} \int_0^{2\pi} f(t) \sin(nt) dt $$
Avec la relation $c_n = \frac{a_n - i b_n}{2}$ (pour $n>0$) et $c_0 = \frac{a_0}{2}$.

**Exemple de calcul de coefficients :**
Considérons le signal créneau pair, $f(t) = 1$ pour $t \in [-\pi/2, \pi/2]$ et $f(t) = -1$ pour $t \in ]\pi/2, 3\pi/2]$ (sur une période de $2\pi$ centrée en 0).
Puisque $f$ est paire, $b_n = 0$ pour tout $n$.
Calculons $a_0$ :
$$ a_0 = \frac{1}{\pi} \int_{-\pi}^\pi f(t) dt = \frac{1}{\pi} \left( \int_{-\pi}^{-\pi/2} (-1) dt + \int_{-\pi/2}^{\pi/2} (1) dt + \int_{\pi/2}^{\pi} (-1) dt \right) $$
$$ a_0 = \frac{1}{\pi} \left( -\frac{\pi}{2} + \pi - \frac{\pi}{2} \right) = 0 $$
Pour $n \geq 1$ :
$$ a_n = \frac{2}{\pi} \int_0^\pi f(t) \cos(nt) dt = \frac{2}{\pi} \left( \int_0^{\pi/2} \cos(nt) dt - \int_{\pi/2}^\pi \cos(nt) dt \right) $$
$$ a_n = \frac{2}{\pi} \left( \left[ \frac{\sin(nt)}{n} \right]_0^{\pi/2} - \left[ \frac{\sin(nt)}{n} \right]_{\pi/2}^\pi \right) = \frac{2}{n\pi} \left( \sin\left(\frac{n\pi}{2}\right) - (\sin(n\pi) - \sin\left(\frac{n\pi}{2}\right)) \right) $$
$$ a_n = \frac{4}{n\pi} \sin\left(\frac{n\pi}{2}\right) $$
Ainsi, $a_n = 0$ si $n$ est pair, $a_n = \frac{4}{n\pi}$ si $n = 1, 5, 9\dots$ et $a_n = -\frac{4}{n\pi}$ si $n = 3, 7, 11\dots$.

### Convergence ponctuelle : Le Théorème de Dirichlet

La série de Fourier (partielle) d'ordre $N$ est la fonction :
$$ S_N(f)(t) = \sum_{n=-N}^{N} c_n(f) e^{int} = \frac{a_0}{2} + \sum_{n=1}^N (a_n \cos(nt) + b_n \sin(nt)) $$

**Théorème 2 (Théorème de Dirichlet) :**
Soit $f : \mathbb{R} \to \mathbb{C}$ une fonction $2\pi$-périodique, continue par morceaux et de classe $C^1$ par morceaux sur $\mathbb{R}$.
Alors, pour tout réel $t$, la série de Fourier de $f$ converge, et sa somme vaut la moyenne des limites à gauche et à droite de $f$ en $t$ :
$$ \lim_{N \to +\infty} S_N(f)(t) = \frac{f(t^+) + f(t^-)}{2} $$
En particulier, si $f$ est continue en $t$, la série converge vers $f(t)$.

**Exemple d'application du Théorème de Dirichlet :**
Reprenons le signal en dents de scie défini par $f(t) = t$ sur $]-\pi, \pi]$ et périodisé. En $t=0$, $f$ est continue et $f(0) = 0$. La série de Fourier converge bien vers 0. En $t=\pi$, qui est un point de discontinuité, les limites sont $f(\pi^-) = \pi$ et $f(\pi^+) = -\pi$. La série de Fourier au point $\pi$ converge donc vers $\frac{\pi - \pi}{2} = 0$.

## 3. Démonstrations

### Démonstration du Théorème d'orthonormalité

Nous voulons prouver que la famille $(e_n)_{n\in\mathbb{Z}}$ définie par $e_n(t) = e^{int}$ est orthonormale pour le produit scalaire $\langle \cdot, \cdot \rangle$.

Soient $m, n \in \mathbb{Z}$. Évaluons le produit scalaire :
$$ \langle e_m, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} \overline{e^{imt}} e^{int} dt $$

Par définition de l'exponentielle complexe conjuguée, $\overline{e^{imt}} = e^{-imt}$.
$$ \langle e_m, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{-imt} e^{int} dt = \frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)t} dt $$

Distinguons deux cas.
**Cas 1 : $m = n$.**
L'exposant est nul.
$$ \langle e_n, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{0} dt = \frac{1}{2\pi} \int_0^{2\pi} 1 dt = \frac{1}{2\pi} [t]_0^{2\pi} = \frac{2\pi}{2\pi} = 1 $$
La famille est donc normée.

**Cas 2 : $m \neq n$.**
Posons $k = n - m$. Puisque $m \neq n$, $k \in \mathbb{Z}^*$ (entier non nul).
$$ \langle e_m, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{ikt} dt $$
La primitive de $e^{ikt}$ (pour $k \neq 0$) est $\frac{e^{ikt}}{ik}$.
$$ \langle e_m, e_n \rangle = \frac{1}{2\pi} \left[ \frac{e^{ikt}}{ik} \right]_0^{2\pi} = \frac{1}{2\pi ik} (e^{2ik\pi} - e^0) $$
Puisque $k$ est un entier, $e^{2ik\pi} = \cos(2k\pi) + i\sin(2k\pi) = 1 + i(0) = 1$.
$$ \langle e_m, e_n \rangle = \frac{1}{2\pi ik} (1 - 1) = 0 $$
La famille est donc orthogonale.

Cela achève la démonstration. \square

### Justification heuristique de l'extraction des coefficients

Supposons qu'une fonction périodique $f$ puisse s'écrire comme une somme infinie (avec convergence suffisamment forte pour permettre l'interversion série/intégrale) :
$$ f(t) = \sum_{k=-\infty}^{+\infty} c_k e^{ikt} $$
Comment isoler un coefficient spécifique $c_n$ ? On multiplie les deux membres de l'équation par $e^{-int}$ et on intègre sur une période :
$$ \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt = \frac{1}{2\pi} \int_0^{2\pi} \left( \sum_{k=-\infty}^{+\infty} c_k e^{ikt} \right) e^{-int} dt $$
En supposant la convergence uniforme de la série, on permute la somme et l'intégrale :
$$ \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt = \sum_{k=-\infty}^{+\infty} c_k \left( \frac{1}{2\pi} \int_0^{2\pi} e^{i(k-n)t} dt \right) $$
L'intégrale entre parenthèses n'est autre que le produit scalaire $\langle e_n, e_k \rangle$. D'après le théorème d'orthonormalité prouvé précédemment, ce terme vaut $0$ pour tout $k \neq n$, et $1$ pour $k = n$.
Ainsi, tous les termes de la somme infinie s'annulent, à l'exception du terme où $k=n$. On obtient donc :
$$ \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt = c_n $$
Ceci constitue la définition fondamentale des coefficients de Fourier.

## 4. Applications en Physique, Logique et Intelligence Artificielle

L'analyse de Fourier n'est pas qu'une abstraction mathématique ; c'est le socle de nombreuses technologies modernes.

### En Physique : Optique et Équation de la Chaleur
La résolution de l'équation de la chaleur de Fourier, $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$, se fait naturellement en décomposant la distribution de température initiale $u(x,0)$ en série de Fourier. Chaque harmonique spatiale décroît exponentiellement dans le temps à une vitesse proportionnelle au carré de sa fréquence. Les hautes fréquences (les variations brusques de température) s'estompent donc très rapidement, lissant le profil de température. Ce même principe s'applique en optique physique pour l'étude de la diffraction (Transformée de Fourier bidimensionnelle).

### En Intelligence Artificielle : Convolutions, Biais Spectral et Traitement Audio
En IA et traitement du signal, les séries de Fourier et la FFT (Fast Fourier Transform) sont omniprésentes :
1.  **Traitement Audio et ASR (Automatic Speech Recognition) :** Les réseaux de neurones analysant le son (comme ceux de Siri ou Whisper) ne prennent généralement pas le signal brut (amplitudes au cours du temps) en entrée. Le signal est d'abord converti via une transformée de Fourier à court terme (STFT) en un spectrogramme, révélant la répartition des fréquences temporelles. Ce spectrogramme est ensuite traité par des réseaux convolutifs (CNN) ou des Transformers.
2.  **Accélération des Convolutions :** Le théorème de convolution énonce que le produit de convolution dans le domaine temporel/spatial équivaut à un produit terme à terme dans le domaine fréquentiel. Pour de très grands filtres (kernels) en Deep Learning, il est computationnellement plus efficace de passer les images et les filtres dans le domaine de Fourier, de les multiplier, puis de faire la transformée inverse.
3.  **Le Biais Spectral des Réseaux de Neurones :** La théorie de Fourier permet de comprendre la dynamique d'apprentissage des réseaux de neurones profonds. Le "spectral bias" (ou F-principle) stipule que lors de l'entraînement par descente de gradient, un réseau de neurones apprend naturellement les composantes de basse fréquence (la tendance globale de la fonction) avant de s'adapter aux composantes de haute fréquence (les détails ou le bruit). Cette propriété inhérente aide à expliquer pourquoi les réseaux de neurones généralisent bien sans surapprendre immédiatement le bruit des données d'entraînement.
