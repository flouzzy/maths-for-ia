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

# Jalon 84 : Livrable IA T7 : Analyse spectrale et extraction de caractéristiques audio à partir de la transformée de Fourier dans $L^2$

## 1. Introduction historique et physique

La compréhension fine d'un signal naturel — qu'il s'agisse de la voix humaine, du son d'un violoncelle ou d'une onde sismique — nécessite de le décomposer en briques élémentaires fondamentales. L'onde sonore, telle qu'elle est captée par un microphone, n'est qu'une fluctuation globale de pression au cours du temps. Vue sous cet angle, elle est souvent illisible et son analyse directe s'avère inefficace pour en extraire des motifs structurés.

L'impulsion théorique de cette analyse provient des travaux fondateurs de Joseph Fourier au début du XIXe siècle sur la propagation de la chaleur, puis de leur extension au XXe siècle par des mathématiciens comme Andreï Kolmogorov ou Dennis Gabor. L'idée est de substituer à la représentation temporelle brute une "image" fréquentielle. On décompose l'énergie du signal en composantes harmoniques pures (des sinusoïdes) pondérées par leur intensité.

Cependant, la transformée de Fourier classique perd la notion de temps. Un signal n'est presque jamais stationnaire ; les fréquences qui le composent évoluent continuellement. Ainsi, pour analyser un signal audio, il faut concevoir une mathématique capable de capturer à la fois *quand* un événement se produit et *quelles* fréquences il contient. C'est la naissance de la transformée de Fourier à court terme (STFT) et de sa représentation graphique : le spectrogramme. Ce passage du domaine temporel 1D au domaine temps-fréquence 2D est l'opération géométrique fondamentale qui rend possible l'analyse par l'intelligence artificielle moderne.

## 2. Définitions, Théorèmes et Structures

### 2.1 La Transformée de Fourier à Court Terme (STFT)

Pour analyser localement le contenu fréquentiel d'un signal $f$, on le multiplie par une fonction "fenêtre" $w$ qui glisse le long de l'axe temporel.

**Définition 1 (Transformée de Fourier à Court Terme).**
Soit $f \in L^2(\mathbb{R})$ un signal temporel de carré intégrable et $w \in L^2(\mathbb{R})$ une fonction de fenêtrage, généralement à support compact ou à décroissance rapide, normalisée telle que $\|w\|_{L^2} = 1$.
La transformée de Fourier à court terme (STFT) de $f$ par rapport à $w$ est l'application $V_w f : \mathbb{R}^2 \to \mathbb{C}$ définie par :
$$ V_w f(t, \omega) = \int_{-\infty}^{+\infty} f(\tau) \overline{w(\tau - t)} e^{-i\omega \tau} \, d\tau $$
où $t \in \mathbb{R}$ représente le décalage temporel et $\omega \in \mathbb{R}$ la fréquence.

**Exemple concret immédiat :**
Considérons un signal constant $f(\tau) = e^{i \omega_0 \tau}$ et une fenêtre rectangulaire $w(\tau) = \frac{1}{\sqrt{2T}} \mathbb{1}_{[-T, T]}(\tau)$.
Calculons la STFT en $t=0$ :
$$ \begin{aligned} V_w f(0, \omega) &= \int_{-\infty}^{+\infty} e^{i \omega_0 \tau} \frac{1}{\sqrt{2T}} \mathbb{1}_{[-T, T]}(\tau) e^{-i\omega \tau} \, d\tau \\ &= \frac{1}{\sqrt{2T}} \int_{-T}^{T} e^{i(\omega_0 - \omega)\tau} \, d\tau \end{aligned} $$
Si $\omega \neq \omega_0$ :
$$ \begin{aligned} V_w f(0, \omega) &= \frac{1}{\sqrt{2T}} \left[ \frac{e^{i(\omega_0 - \omega)\tau}}{i(\omega_0 - \omega)} \right]_{-T}^{T} \\ &= \frac{1}{\sqrt{2T}} \frac{e^{i(\omega_0 - \omega)T} - e^{-i(\omega_0 - \omega)T}}{i(\omega_0 - \omega)} \\ &= \frac{2}{\sqrt{2T}} \frac{\sin((\omega_0 - \omega)T)}{\omega_0 - \omega} \\ &= \sqrt{2T} \, \text{sinc}((\omega_0 - \omega)T) \end{aligned} $$
Si $\omega = \omega_0$, l'intégrale donne $2T / \sqrt{2T} = \sqrt{2T}$. La STFT révèle bien un pic d'énergie centré sur la fréquence $\omega_0$, étalé par le sinus cardinal (effet de "leakage" dû à la fenêtre rectangulaire).

### 2.2 Le Spectrogramme de Puissance

L'information pertinente en audio réside souvent dans l'amplitude plutôt que dans la phase, du fait des propriétés de la perception humaine.

**Définition 2 (Spectrogramme).**
Le spectrogramme $S(t, \omega)$ d'un signal $f$ par rapport à une fenêtre $w$ est la densité d'énergie locale dans le plan temps-fréquence, définie comme le carré du module de sa STFT :
$$ S(t, \omega) = |V_w f(t, \omega)|^2 $$

**Théorème 1 (Conservation de l'énergie et Formule de Plancherel pour la STFT).**
Soit $f \in L^2(\mathbb{R})$ et $w \in L^2(\mathbb{R})$ avec $\|w\|_{L^2} = 1$. L'énergie totale du signal est conservée dans le plan temps-fréquence :
$$ \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} S(t, \omega) \, \frac{d\omega}{2\pi} \, dt = \int_{-\infty}^{+\infty} |f(\tau)|^2 \, d\tau = \|f\|_{L^2}^2 $$

**Cas limite : Le principe d'incertitude d'Heisenberg-Gabor.**
On ne peut pas concentrer arbitrairement l'énergie à la fois en temps et en fréquence. Si l'on choisit une fenêtre $w$ très étroite (durée courte) pour avoir une résolution temporelle fine, sa transformée de Fourier $\hat{w}$ sera étalée, rendant la résolution fréquentielle floue. Formellement, $\Delta t \cdot \Delta \omega \ge \frac{1}{2}$. Une fenêtre gaussienne minimise cette inégalité.

### 2.3 L'Échelle de Mel

Le système auditif humain ne perçoit pas les variations de hauteur de manière linéaire. Une augmentation de 100 Hz est très perceptible dans les graves, mais presque indétectable dans les aigus. L'échelle de Mel est une transformation non-linéaire (quasi-logarithmique) des fréquences visant à mimer cette perception.

**Définition 3 (Fréquence Mel).**
La conversion usuelle d'une fréquence physique $f$ (en Hertz) vers la fréquence psychoacoustique $m$ (en Mels) est donnée par :
$$ m = 2595 \log_{10}\left(1 + \frac{f}{700}\right) $$
La transformation inverse est :
$$ f = 700 \left(10^{m / 2595} - 1\right) $$

**Exemple concret de passage à l'échelle Mel :**
Soit une fréquence de $1000$ Hz (souvent le point de référence $1000 \text{ Hz} = 1000 \text{ Mels}$).
$$ m = 2595 \log_{10}\left(1 + \frac{1000}{700}\right) \approx 2595 \log_{10}(2.428) \approx 2595 \times 0.385 \approx 1000 \text{ Mels} $$
Si on passe à $f = 8000$ Hz :
$$ m = 2595 \log_{10}\left(1 + \frac{8000}{700}\right) \approx 2595 \log_{10}(12.42) \approx 2595 \times 1.094 \approx 2839 \text{ Mels} $$

## 3. Démonstrations

### 3.1 Démonstration du Théorème de Conservation de l'énergie (Isométrie)

**Démonstration :**
Calculons l'intégrale double de l'énergie du spectrogramme. Par définition, $S(t, \omega) = |V_w f(t, \omega)|^2 = V_w f(t, \omega) \overline{V_w f(t, \omega)}$.
$$ \iint_{\mathbb{R}^2} |V_w f(t, \omega)|^2 \, dt \, d\omega = \iint_{\mathbb{R}^2} \left| \int_{\mathbb{R}} f(\tau) \overline{w(\tau - t)} e^{-i\omega \tau} \, d\tau \right|^2 dt \, d\omega $$
Pour un $t$ fixé, la fonction $\tau \mapsto f(\tau) \overline{w(\tau - t)}$ appartient à $L^2(\mathbb{R})$ car $f$ et $w$ le sont et $w$ est bornée (ou en appliquant Hölder dans des espaces adaptés, et par densité). L'intégrale interne est exactement la transformée de Fourier de la fonction $g_t(\tau) = f(\tau) \overline{w(\tau - t)}$ évaluée en $\omega$.
Notons $\mathcal{F}$ l'opérateur de transformée de Fourier.
$$ V_w f(t, \omega) = \mathcal{F}(g_t)(\omega) $$
On intègre d'abord sur $\omega$. Par le théorème de Plancherel usuel pour $L^2(\mathbb{R})$, on a :
$$ \int_{\mathbb{R}} |\mathcal{F}(g_t)(\omega)|^2 \, d\omega = 2\pi \int_{\mathbb{R}} |g_t(\tau)|^2 \, d\tau $$
Réinjectons ce résultat dans l'intégrale globale (après division par $2\pi$) :
$$ \frac{1}{2\pi} \iint_{\mathbb{R}^2} |V_w f(t, \omega)|^2 \, d\omega \, dt = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} |f(\tau)|^2 |w(\tau - t)|^2 \, d\tau \right) dt $$
Toutes les fonctions étant positives, nous pouvons intervertir l'ordre d'intégration par le théorème de Fubini-Tonelli :
$$ \int_{\mathbb{R}} |f(\tau)|^2 \left( \int_{\mathbb{R}} |w(\tau - t)|^2 \, dt \right) d\tau $$
Effectuons le changement de variable $u = \tau - t$, $du = -dt$. L'intégrale interne devient :
$$ \int_{\mathbb{R}} |w(u)|^2 \, du = \|w\|_{L^2}^2 $$
Comme par hypothèse $\|w\|_{L^2} = 1$, il reste exactement :
$$ \int_{\mathbb{R}} |f(\tau)|^2 \times 1 \, d\tau = \|f\|_{L^2}^2 $$
Ce qui clôt rigoureusement la démonstration. $\blacksquare$

### 3.2 Implémentation discrète et coefficients MFCC

Pour une machine, l'espace $L^2$ est discrétisé. On utilise la **Discrete Fourier Transform (DFT)** sur des segments de longueur $N$.
1. **Fenêtrage :** $x_n = s_n \cdot w_n$
2. **DFT :** $X_k = \sum_{n=0}^{N-1} x_n e^{-i \frac{2\pi}{N} k n}$
3. **Spectre de puissance :** $P_k = \frac{1}{N} |X_k|^2$
4. **Bancs de filtres Mel :** On pondère $P_k$ par des filtres triangulaires $H_m(k)$ espacés selon l'échelle Mel pour obtenir l'énergie par bande Mel $E_m$.
5. **Compression logarithmique :** $L_m = \log(E_m)$
6. **DCT (Discrete Cosine Transform) :** Les bandes Mel adjacentes étant très corrélées, on applique une DCT pour décorréler les caractéristiques et obtenir les Mel-Frequency Cepstral Coefficients (MFCC) :
$$ C_j = \sum_{m=1}^{M} L_m \cos\left( \frac{\pi j (m - 0.5)}{M} \right) $$

## 4. Applications en Physique et Intelligence Artificielle

L'extraction de ces caractéristiques par l'analyse spectrale constitue la matrice originelle de tout traitement du signal par les architectures neuronales profondes :

1. **Reconnaissance vocale (ASR) :** Les modèles comme Whisper (OpenAI) ou wav2vec 2.0 (Meta) ne traitent presque jamais la forme d'onde brute. Ils s'alimentent d'une représentation temps-fréquence, typiquement des spectrogrammes Mel (Log-Mel Spectrograms). Le signal 1D est transformé en une image 2D riche et dense, sur laquelle les réseaux convolutifs (CNN) ou les Transformers appliquent l'apprentissage.
2. **Physique Quantique et Mécanique Ondulatoire :** L'isométrie démontrée plus haut est le pendant mathématique de la conservation des probabilités (ou de l'énergie). En mécanique quantique, les états vivent dans $L^2$. La transformation de Wigner-Ville, cousine de la STFT, dresse un portrait de l'état d'une particule à la fois en position et en impulsion, tout en respectant l'inégalité d'Heisenberg.
3. **Compression Audio (MP3 / AAC) :** La psychophysique de l'audition, modélisée mathématiquement par l'échelle de Mel, permet de déterminer quelles fréquences sont masquées ou inaudibles pour l'oreille humaine. On applique une analyse de Fourier, et on quantifie drastiquement (on retire de l'information) dans les bandes fréquentielles où la sensibilité humaine est faible, réalisant ainsi une compression destructrice mais perceptivement imperceptible.
