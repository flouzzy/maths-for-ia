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

## 1. Introduction

L'analyse de Fourier classique, telle qu'introduite historiquement par Joseph Fourier pour l'étude de la propagation de la chaleur, s'appuie naturellement sur l'espace $L^1(\mathbb{R})$ des fonctions absolument intégrables. Dans ce cadre, l'intégrale définissant la transformée de Fourier, $\hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-i\xi x} dx$, converge absolument pour tout $\xi$. Cependant, cette approche rencontre rapidement une impasse majeure en physique théorique et en ingénierie des signaux.

De nombreux signaux physiques fondamentaux ne sont pas absolument intégrables. Par exemple, la fonction sinus cardinal $x \mapsto \frac{\sin(x)}{x}$, archétype de la réponse impulsionnelle d'un filtre passe-bas idéal, appartient à $L^2(\mathbb{R})$ (signaux d'énergie finie) mais pas à $L^1(\mathbb{R})$. Plus fondamentalement encore, la formulation de la mécanique quantique par Paul Dirac et John von Neumann nécessite que les fonctions d'onde appartiennent à un espace de Hilbert, $L^2(\mathbb{R})$, afin que l'interprétation probabiliste de Max Born soit valide. L'opérateur impulsion est intimement lié à la transformée de Fourier, ce qui impose d'étendre la définition de cette dernière à $L^2(\mathbb{R})$.

Le défi mathématique est de taille : si $f \in L^2(\mathbb{R})$ n'est pas dans $L^1(\mathbb{R})$, l'intégrale $\int_{\mathbb{R}} f(x) e^{-i\xi x} dx$ n'a aucune raison de converger au sens de Lebesgue. Michel Plancherel (en 1910) a résolu ce problème par un argument magistral de densité. L'idée est de s'appuyer sur l'intersection $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, un sous-espace dense dans $L^2(\mathbb{R})$. Sur cet espace, on montre que la transformée de Fourier préserve la norme $L^2$ (l'énergie du signal). Par continuité, cette isométrie peut être prolongée de manière unique à l'espace de Hilbert $L^2(\mathbb{R})$ tout entier. Ce théorème de Plancherel (ou Parseval-Plancherel) est le pilier central du traitement moderne du signal, garantissant que l'énergie totale d'un signal dans le domaine temporel est strictement égale à son énergie dans le domaine spectral. Géométriquement, la transformée de Fourier devient une "rotation" unitaire infinie-dimensionnelle de l'espace des états.

## 2. Définitions, Théorèmes et Exemples

### Définition 1 : La classe de Schwartz $\mathcal{S}(\mathbb{R})$ et l'espace $L^1 \cap L^2$

Pour construire rigoureusement la transformée de Fourier sur $L^2(\mathbb{R})$, il est commode de travailler avec des espaces de fonctions régulières à décroissance rapide, comme l'espace de Schwartz $\mathcal{S}(\mathbb{R})$, ou simplement avec le sous-espace $E = L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.

Pour toute fonction $f \in L^1(\mathbb{R})$, on rappelle la définition de sa transformée de Fourier $\mathcal{F}(f) = \hat{f}$ :
$$ \hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-i \xi x} dx, \quad \forall \xi \in \mathbb{R} $$

**Exemple concret : La porte rectangulaire**
Considérons la fonction indicatrice de l'intervalle $[-1, 1]$, notée $f(x) = \mathbb{1}_{[-1, 1]}(x)$.
Cette fonction appartient clairement à $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.
Calculons son énergie (norme $L^2$ au carré) :
$$ \|f\|_{L^2}^2 = \int_{\mathbb{R}} |f(x)|^2 dx = \int_{-1}^1 1^2 dx = 2 $$
Sa transformée de Fourier est :
$$ \hat{f}(\xi) = \int_{-1}^1 e^{-i \xi x} dx = \left[ \frac{e^{-i \xi x}}{-i \xi} \right]_{-1}^1 = \frac{e^{-i\xi} - e^{i\xi}}{-i\xi} = \frac{-2i \sin(\xi)}{-i\xi} = 2 \frac{\sin(\xi)}{\xi} = 2 \text{sinc}(\xi) $$
(où $\text{sinc}(\xi) = \frac{\sin(\xi)}{\xi}$ est le sinus cardinal).
On remarque que $\hat{f}$ n'est pas dans $L^1(\mathbb{R})$ car $\int |\text{sinc}(\xi)| d\xi = +\infty$, mais elle est dans $L^2(\mathbb{R})$.

### Théorème 1 (Egalité de Parseval sur $L^1 \cap L^2$)

Soit $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$. Si de plus sa transformée de Fourier $\hat{f}$ appartient à $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, alors on a l'égalité d'énergie :
$$ \int_{\mathbb{R}} |f(x)|^2 dx = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{f}(\xi)|^2 d\xi $$
Ce résultat peut être généralisé à tout l'espace $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.

**Exemple concret immédiat :**
Reprenons la fonction porte $f(x) = \mathbb{1}_{[-1, 1]}(x)$. Nous avons vu que $\|f\|_{L^2}^2 = 2$.
D'après le théorème, nous devons avoir $\frac{1}{2\pi} \int_{\mathbb{R}} |2 \text{sinc}(\xi)|^2 d\xi = 2$.
Vérifions-le analytiquement :
$$ \int_{\mathbb{R}} 4 \frac{\sin^2(\xi)}{\xi^2} d\xi = 4 \times \pi = 4\pi $$
(Rappelons que $\int_{\mathbb{R}} \frac{\sin^2(\xi)}{\xi^2} d\xi = \pi$).
Ainsi, $\frac{1}{2\pi} (4\pi) = 2$, ce qui coïncide parfaitement avec $\|f\|_{L^2}^2$. Le théorème est vérifié numériquement.

### Théorème 2 (Isométrie de Plancherel)

L'opérateur $\mathcal{F} : L^1(\mathbb{R}) \cap L^2(\mathbb{R}) \subset L^2(\mathbb{R}) \to L^2(\mathbb{R})$, défini par $\mathcal{F}(f) = \frac{1}{\sqrt{2\pi}} \hat{f}$, se prolonge de manière unique en un opérateur linéaire continu $\widetilde{\mathcal{F}} : L^2(\mathbb{R}) \to L^2(\mathbb{R})$.
De plus, $\widetilde{\mathcal{F}}$ est un **isomorphisme isométrique** (ou opérateur unitaire) de l'espace de Hilbert $L^2(\mathbb{R})$ sur lui-même, c'est-à-dire :
1. Pour tout $f \in L^2(\mathbb{R})$, $\|\widetilde{\mathcal{F}}(f)\|_{L^2} = \|f\|_{L^2}$.
2. (Identité de Parseval polarisée) Pour tous $f, g \in L^2(\mathbb{R})$,
$$ \langle f, g \rangle_{L^2} = \int_{\mathbb{R}} f(x) \overline{g(x)} dx = \langle \widetilde{\mathcal{F}}(f), \widetilde{\mathcal{F}}(g) \rangle_{L^2} = \int_{\mathbb{R}} \widetilde{\mathcal{F}}(f)(\xi) \overline{\widetilde{\mathcal{F}}(g)(\xi)} d\xi $$
La transformée inverse $\widetilde{\mathcal{F}}^{-1}$ est donnée par le prolongement unitaire de $g \mapsto \frac{1}{\sqrt{2\pi}} \int_{\mathbb{R}} g(\xi) e^{i x \xi} d\xi$.

*Remarque de notation :* En pratique, la constante $\frac{1}{\sqrt{2\pi}}$ est souvent absorbée dans la définition de la transformée de Fourier, ou bien la mesure de Lebesgue est modifiée. Ici, on maintient la convention standard des analystes : $\hat{f}(\xi) = \int f(x)e^{-i\xi x}dx$ et l'isométrie porte le facteur $\frac{1}{2\pi}$ sur le carré de la norme. On continuera souvent à noter abusivement $\hat{f}$ pour $\widetilde{\mathcal{F}}(f)$ à une constante près.

**Cas limite et pathologie :**
Si $f \in L^2(\mathbb{R}) \setminus L^1(\mathbb{R})$ (par exemple $f(x) = \frac{1}{1+|x|}$), l'intégrale $\int_{\mathbb{R}} f(x) e^{-i\xi x} dx$ diverge au sens classique. La transformée $\widetilde{\mathcal{F}}(f)$ n'est définie **qu'en tant que limite en norme $L^2$** :
$$ \widetilde{\mathcal{F}}(f)(\xi) = \lim_{R \to \infty} \left( L^2 \right) \frac{1}{\sqrt{2\pi}} \int_{-R}^R f(x) e^{-i\xi x} dx $$
Cette limite presque partout n'est garantie que par des théorèmes fins d'analyse (comme le théorème de Carleson).

## 3. Démonstrations

### Lemme préliminaire
Soit $f, g \in L^1(\mathbb{R})$. Alors on a l'identité :
$$ \int_{\mathbb{R}} \hat{f}(x) g(x) dx = \int_{\mathbb{R}} f(x) \hat{g}(x) dx $$

**Démonstration du lemme :**
Écrivons l'intégrale de gauche en remplaçant $\hat{f}(x)$ par sa définition :
$$ I = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} f(y) e^{-ixy} dy \right) g(x) dx $$
Puisque $f, g \in L^1(\mathbb{R})$, la fonction $(x,y) \mapsto f(y)g(x)e^{-ixy}$ est mesurable et son module est $|f(y)||g(x)|$, qui est intégrable sur $\mathbb{R}^2$ car l'intégrale de ce module vaut $\|f\|_{L^1} \|g\|_{L^1} < \infty$.
D'après le théorème de Fubini, on peut permuter l'ordre d'intégration :
$$ I = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} g(x) e^{-ixy} dx \right) f(y) dy $$
L'intégrale intérieure est exactement $\hat{g}(y)$. Donc :
$$ I = \int_{\mathbb{R}} f(y) \hat{g}(y) dy $$
Ce qui conclut le lemme.

### Démonstration du Théorème de Plancherel (Isométrie sur $L^1 \cap L^2$)

Nous allons démontrer que si $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ et si nous supposons que pour une certaine famille d'approximations de l'identité, l'inversion de Fourier tient. Plus simplement, utilisons l'espace de Schwartz $\mathcal{S}(\mathbb{R})$ (dense dans $L^2$) pour la preuve algébrique.

Soient $f \in \mathcal{S}(\mathbb{R})$. Définissons $g(x) = \overline{f(-x)}$.
Puisque $f \in \mathcal{S}(\mathbb{R})$, on a aussi $g \in \mathcal{S}(\mathbb{R})$.
Calculons la transformée de Fourier de $g$ :
$$ \hat{g}(\xi) = \int_{\mathbb{R}} \overline{f(-x)} e^{-i\xi x} dx $$
Posons le changement de variable $y = -x$, $dx = -dy$. Les bornes d'intégration s'inversent : de $+\infty$ à $-\infty$, ce qui annule le signe du $dx$.
$$ \hat{g}(\xi) = \int_{\mathbb{R}} \overline{f(y)} e^{i\xi y} dy $$
Remarquons que $e^{i\xi y} = \overline{e^{-i\xi y}}$. Ainsi,
$$ \hat{g}(\xi) = \overline{\int_{\mathbb{R}} f(y) e^{-i\xi y} dy} = \overline{\hat{f}(\xi)} $$
Considérons le produit de convolution $h = f * g$.
$$ h(x) = \int_{\mathbb{R}} f(y) g(x-y) dy = \int_{\mathbb{R}} f(y) \overline{f(y-x)} dy $$
En particulier, évaluons $h$ en $x=0$ :
$$ h(0) = \int_{\mathbb{R}} f(y) \overline{f(y)} dy = \int_{\mathbb{R}} |f(y)|^2 dy = \|f\|_{L^2}^2 $$
D'autre part, la transformée de Fourier transforme la convolution en produit (propriété fondamentale dans $L^1$). Donc :
$$ \hat{h}(\xi) = \widehat{(f * g)}(\xi) = \hat{f}(\xi) \hat{g}(\xi) $$
En utilisant l'expression de $\hat{g}(\xi)$, on obtient :
$$ \hat{h}(\xi) = \hat{f}(\xi) \overline{\hat{f}(\xi)} = |\hat{f}(\xi)|^2 $$
Puisque $f, g \in \mathcal{S}(\mathbb{R})$, $h \in \mathcal{S}(\mathbb{R})$. On peut lui appliquer la formule d'inversion de Fourier, qui stipule que pour $h \in \mathcal{S}(\mathbb{R})$, $h(x) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{h}(\xi) e^{i\xi x} d\xi$.
Évaluons cette formule d'inversion en $x=0$ :
$$ h(0) = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{h}(\xi) e^{0} d\xi = \frac{1}{2\pi} \int_{\mathbb{R}} \hat{h}(\xi) d\xi $$
En remplaçant $h(0)$ par $\|f\|_{L^2}^2$ et $\hat{h}(\xi)$ par $|\hat{f}(\xi)|^2$, on obtient finalement :
$$ \|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{f}(\xi)|^2 d\xi $$
Cette isométrie sur $\mathcal{S}(\mathbb{R})$ (qui est un sous-espace dense de $L^2(\mathbb{R})$) s'étend de manière unique à tout l'espace $L^2(\mathbb{R})$ par le théorème de prolongement des opérateurs uniformément continus sur des espaces de Banach (ou Hilbert).

Pour achever la surjectivité (donc l'unitarité complète de l'opérateur $\widetilde{\mathcal{F}}$ avec le facteur $1/\sqrt{2\pi}$), on utilise que l'image du prolongement isométrique d'un espace complet contient un sous-espace dense et est fermée, donc c'est l'espace entier.

## 4. Applications en Physique, Logique et Intelligence Artificielle

### Mécanique Quantique (Postulats de von Neumann)
En mécanique quantique, l'état d'une particule évoluant sur une droite est modélisé par une fonction d'onde $\psi \in L^2(\mathbb{R})$, avec la condition de normalisation $\|\psi\|_{L^2} = 1$. La quantité $|\psi(x)|^2$ représente la densité de probabilité de trouver la particule à la position $x$.
L'opérateur impulsion est défini par $P = -i\hbar \frac{d}{dx}$. Par la transformée de Fourier, cet opérateur de dérivation devient un opérateur de multiplication : $\widehat{P\psi}(p) = p \hat{\psi}(p)$.
Le théorème de Plancherel garantit que $\|\hat{\psi}\|_{L^2} = 1$ (avec la bonne normalisation), ce qui permet d'interpréter rigoureusement $|\hat{\psi}(p)|^2$ comme la densité de probabilité de mesurer l'impulsion $p$ de la particule. L'isométrie assure la conservation de la probabilité totale (qui doit valoir 1) entre l'espace des positions et l'espace des impulsions.

### Traitement du Signal et Égalité de Parseval
En théorie du signal, l'énergie d'un signal temporel $s(t)$ de tension à travers une résistance de 1 Ohm est donnée par $E = \int_{\mathbb{R}} |s(t)|^2 dt$. Le théorème de Plancherel assure que $E = \frac{1}{2\pi} \int_{\mathbb{R}} |\hat{s}(\omega)|^2 d\omega$. La quantité $|\hat{s}(\omega)|^2$ est appelée la **densité spectrale d'énergie**. Cela fonde toute l'analyse fréquentielle (filtrage de Wiener, compression audio MP3), permettant de manipuler l'énergie du signal directement dans le spectre (par exemple, supprimer une plage de fréquences sans se soucier du calcul exact dans le domaine temporel).

### Intelligence Artificielle : Les Réseaux de Neurones Convolutionnels (CNN) gaussiens
Dans les réseaux de neurones, la convolution est l'opération fondamentale (CNNs). Le calcul direct d'une convolution entre un signal $x$ de taille $N$ et un filtre $h$ est de complexité $O(N^2)$. Le théorème de convolution couplé à l'isométrie de Plancherel permet de passer dans le domaine spectral, de multiplier simplement les composantes, puis d'appliquer la transformée inverse, le tout en complexité $O(N \log N)$ grâce à la Fast Fourier Transform (FFT).
L'isométrie de Plancherel est aussi cruciale pour étudier la stabilité des architectures de deep learning par rapport aux déformations. Dans les travaux sur les "Scattering Transforms" (Stéphane Mallat), le réseau de neurones est construit en empilant des ondelettes. La propriété de préservation de la norme $L^2$ (Plancherel) permet de démontrer formellement que ces réseaux dispersent l'énergie du signal à travers différentes échelles sans la perdre et sans amplifier le bruit, offrant des garanties de robustesse contre les attaques adversarielles introuvables dans les réseaux empiriques classiques.
