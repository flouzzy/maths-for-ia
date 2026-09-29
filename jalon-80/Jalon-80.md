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

## Introduction

La Transformée de Fourier est un outil fondamental de l'analyse mathématique, généralisant le concept des séries de Fourier aux fonctions non périodiques définies sur l'ensemble des réels $\mathbb{R}$. Historiquement, cette transformation a émergé du besoin de résoudre l'équation de la chaleur sur des domaines infinis, où les méthodes de décomposition en modes discrets (Séries de Fourier) s'avèrent inopérantes.

Physiquement, la Transformée de Fourier agit comme un prisme spectral continu : elle décompose un signal (une fonction du temps ou de l'espace) en une superposition continue d'ondes sinusoïdales élémentaires. On passe ainsi d'une représentation temporelle ou spatiale (domaine direct) à une représentation fréquentielle (domaine spectral). Cette transformation est omniprésente en traitement du signal, en mécanique quantique et, plus récemment, en apprentissage automatique pour l'analyse des données structurées.

Mathématiquement, elle offre une propriété remarquable : elle diagonalise l'opérateur de dérivation. En d'autres termes, elle transforme les équations différentielles linéaires complexes en de simples équations algébriques. C'est cette caractéristique qui en fait un outil si puissant pour l'analyse des EDP et la théorie des probabilités.

## Définitions, Théorèmes \& Exemples

Soit $L^1(\mathbb{R})$ l'espace vectoriel des fonctions à valeurs complexes, mesurables au sens de Lebesgue et intégrables sur $\mathbb{R}$. On rappelle que la norme sur $L^1(\mathbb{R})$ est donnée par $\|f\|_1 = \int_{-\infty}^{+\infty} |f(t)| \, dt$.

### Définition de la Transformée de Fourier

> **Définition (Transformée de Fourier)**
> Pour toute fonction $f \in L^1(\mathbb{R})$, on définit sa transformée de Fourier, notée $\hat{f}$ ou $\mathcal{F}(f)$, comme la fonction de la variable réelle $\xi$ donnée par :
> $$ \forall \xi \in \mathbb{R}, \quad \hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t) e^{-i\xi t} \, dt $$

*Remarque :* Puisque $|f(t) e^{-i\xi t}| = |f(t)|$, l'intégrale est absolument convergente pour tout $\xi \in \mathbb{R}$. Par domination, on déduit immédiatement que la fonction $\hat{f}$ est bornée sur $\mathbb{R}$ par $\|f\|_1$.

> **Exemple Concret : Transformée de la fonction porte (Créneau)**
> Considérons la fonction indicatrice $f(t) = \mathbf{1}_{[-a, a]}(t)$ avec $a > 0$. Clairement, $f \in L^1(\mathbb{R})$.
> Calculons sa transformée de Fourier $\hat{f}(\xi)$ pour $\xi \neq 0$ :
> $$ \hat{f}(\xi) = \int_{-\infty}^{+\infty} \mathbf{1}_{[-a, a]}(t) e^{-i\xi t} \, dt = \int_{-a}^{a} e^{-i\xi t} \, dt $$
> Une primitive immédiate est :
> $$ \hat{f}(\xi) = \left[ \frac{e^{-i\xi t}}{-i\xi} \right]_{-a}^{a} = \frac{e^{-i\xi a} - e^{i\xi a}}{-i\xi} $$
> En utilisant la formule d'Euler $2i\sin(\xi a) = e^{i\xi a} - e^{-i\xi a}$, on obtient :
> $$ \hat{f}(\xi) = \frac{-2i\sin(\xi a)}{-i\xi} = 2 \frac{\sin(\xi a)}{\xi} = 2a \, \text{sinc}(\xi a) $$
> Pour $\xi = 0$, le calcul direct donne $\hat{f}(0) = \int_{-a}^a 1 \, dt = 2a$, ce qui prolonge par continuité l'expression précédente.

### Propriétés Algébriques et Topologiques

> **Théorème de Continuité**
> Si $f \in L^1(\mathbb{R})$, alors sa transformée de Fourier $\hat{f}$ est uniformément continue sur $\mathbb{R}$.

> **Lemme de Riemann-Lebesgue**
> Si $f \in L^1(\mathbb{R})$, alors $\hat{f}$ s'annule à l'infini :
> $$ \lim_{|\xi| \to +\infty} \hat{f}(\xi) = 0 $$
> On note souvent $C_0(\mathbb{R})$ l'espace des fonctions continues s'annulant à l'infini. Ainsi, l'opérateur $\mathcal{F}$ envoie continûment $L^1(\mathbb{R})$ dans $C_0(\mathbb{R})$.

> **Théorème (Transformée de la dérivée)**
> Soit $f \in \mathcal{C}^1(\mathbb{R}) \cap L^1(\mathbb{R})$ telle que sa dérivée $f'$ appartienne également à $L^1(\mathbb{R})$. Alors :
> $$ \forall \xi \in \mathbb{R}, \quad \widehat{f'}(\xi) = i\xi \hat{f}(\xi) $$

> **Exemple Concret : Transformée d'une exponentielle décroissante unilatérale**
> Soit $f(t) = e^{-t} \mathbf{1}_{[0, +\infty[}(t)$. Cette fonction est dans $L^1(\mathbb{R})$.
> Calculons $\hat{f}(\xi)$ :
> $$ \hat{f}(\xi) = \int_{0}^{+\infty} e^{-t} e^{-i\xi t} \, dt = \int_{0}^{+\infty} e^{-(1+i\xi)t} \, dt $$
> $$ \hat{f}(\xi) = \left[ \frac{e^{-(1+i\xi)t}}{-(1+i\xi)} \right]_0^{+\infty} = \frac{0 - 1}{-(1+i\xi)} = \frac{1}{1+i\xi} $$
> En multipliant par la quantité conjuguée :
> $$ \hat{f}(\xi) = \frac{1 - i\xi}{1+\xi^2} $$
> On observe bien que $\lim_{|\xi| \to \infty} \hat{f}(\xi) = 0$, illustrant le lemme de Riemann-Lebesgue.


> **Exemple Concret : Transformée de Fourier du Dirac (Distribution)**
> Bien que le Dirac $\delta_0$ ne soit pas une fonction de $L^1$, on peut l'approcher. Formellement, sa transformée est :
> $$ \hat{\delta_0}(\xi) = \int \delta_0(t) e^{-i\xi t} dt = e^{-i\xi \cdot 0} = 1 $$
> Le spectre est plat, signifiant que l'impulsion ponctuelle contient toutes les fréquences de manière égale.

> **Exemple Concret : Inversion temporelle**
> Soit $f(t)$ une fonction de $L^1$ et $g(t) = f(-t)$.
> $$ \hat{g}(\xi) = \int f(-t) e^{-i\xi t} dt = \int f(u) e^{i\xi u} du = \hat{f}(-\xi) $$
> Retourner le temps revient à inverser les fréquences.

### Produit de Convolution

La transformée de Fourier interagit de manière fondamentale avec le produit de convolution, simplifiant radicalement son calcul.

> **Définition (Convolution dans $L^1$)**
> Soient $f, g \in L^1(\mathbb{R})$. Leur produit de convolution, noté $f * g$, est défini presque partout par :
> $$ (f * g)(t) = \int_{-\infty}^{+\infty} f(t-s)g(s) \, ds $$
> Le théorème de Fubini garantit que $f * g \in L^1(\mathbb{R})$ et $\|f * g\|_1 \le \|f\|_1 \|g\|_1$.

> **Théorème de Convolution**
> Soient $f, g \in L^1(\mathbb{R})$. Alors la transformée de Fourier du produit de convolution est le produit ponctuel des transformées de Fourier :
> $$ \forall \xi \in \mathbb{R}, \quad \widehat{f * g}(\xi) = \hat{f}(\xi) \cdot \hat{g}(\xi) $$

> **Exemple Concret : Auto-convolution d'une porte**
> Soit $f(t) = \mathbf{1}_{[-1/2, 1/2]}(t)$. Sa transformée est $\hat{f}(\xi) = \frac{\sin(\xi/2)}{\xi/2}$.
> Par le théorème, l'auto-convolution $h = f * f$ admet pour transformée de Fourier :
> $$ \hat{h}(\xi) = \left( \frac{\sin(\xi/2)}{\xi/2} \right)^2 $$
> Géométriquement, $h(t)$ est une fonction triangle valant $1 - |t|$ sur $[-1, 1]$ et $0$ ailleurs.

## Démonstrations

### Démonstration : Théorème de la Transformée de la Dérivée

1. **Cadre de travail :**
   Soit $f \in \mathcal{C}^1(\mathbb{R}) \cap L^1(\mathbb{R})$ avec $f' \in L^1(\mathbb{R})$.
   Puisque $f'$ est intégrable, la fonction $f$ possède des limites en $\pm\infty$.
   De plus, comme $f$ est intégrable, la seule limite possible en l'infini pour assurer que $\int |f| < \infty$ est $0$. Ainsi, $\lim_{t \to \pm\infty} f(t) = 0$.

2. **Écriture de l'intégrale :**
   Par définition, pour un $\xi \in \mathbb{R}$ fixé :
   $$ \widehat{f'}(\xi) = \int_{-\infty}^{+\infty} f'(t) e^{-i\xi t} \, dt $$

3. **Intégration par parties :**
   On fixe un segment $[-M, M]$ et on y effectue une intégration par parties.
   Posons $u(t) = e^{-i\xi t}$, d'où $u'(t) = -i\xi e^{-i\xi t}$.
   Posons $v'(t) = f'(t)$, d'où $v(t) = f(t)$.

   $$ \int_{-M}^{M} f'(t) e^{-i\xi t} \, dt = \left[ f(t) e^{-i\xi t} \right]_{-M}^{M} - \int_{-M}^{M} f(t) (-i\xi e^{-i\xi t}) \, dt $$

4. **Passage à la limite :**
   Le terme de bord (tout intégré) s'écrit :
   $$ f(M)e^{-i\xi M} - f(-M)e^{i\xi (-M)} $$
   Puisque $|e^{\pm i\xi M}| = 1$ et $\lim_{M \to \infty} f(M) = \lim_{M \to \infty} f(-M) = 0$, ce terme de bord converge vers $0$ lorsque $M \to +\infty$.

5. **Conclusion :**
   L'intégrale restante devient :
   $$ \int_{-\infty}^{+\infty} i\xi f(t) e^{-i\xi t} \, dt = i\xi \int_{-\infty}^{+\infty} f(t) e^{-i\xi t} \, dt = i\xi \hat{f}(\xi) $$
   Ainsi, $\widehat{f'}(\xi) = i\xi \hat{f}(\xi)$.

### Démonstration : Théorème de Convolution

1. **Écriture initiale :**
   Soient $f, g \in L^1(\mathbb{R})$. Soit $\xi \in \mathbb{R}$.
   $$ \widehat{f * g}(\xi) = \int_{-\infty}^{+\infty} (f * g)(t) e^{-i\xi t} \, dt = \int_{-\infty}^{+\infty} \left( \int_{-\infty}^{+\infty} f(t-s)g(s) \, ds \right) e^{-i\xi t} \, dt $$

2. **Application du théorème de Fubini :**
   La fonction $(t, s) \mapsto f(t-s)g(s)e^{-i\xi t}$ est intégrable sur $\mathbb{R}^2$. On peut donc intervertir les intégrales :
   $$ \widehat{f * g}(\xi) = \int_{-\infty}^{+\infty} \left( \int_{-\infty}^{+\infty} f(t-s) e^{-i\xi t} \, dt \right) g(s) \, ds $$

3. **Changement de variable :**
   Dans l'intégrale interne (par rapport à $t$), on effectue le changement de variable $u = t - s$, donc $t = u + s$ et $dt = du$.
   $$ \int_{-\infty}^{+\infty} f(u) e^{-i\xi (u+s)} \, du = e^{-i\xi s} \int_{-\infty}^{+\infty} f(u) e^{-i\xi u} \, du = e^{-i\xi s} \hat{f}(\xi) $$

4. **Conclusion :**
   On remplace dans l'intégrale externe :
   $$ \widehat{f * g}(\xi) = \int_{-\infty}^{+\infty} \left( \hat{f}(\xi) e^{-i\xi s} \right) g(s) \, ds = \hat{f}(\xi) \int_{-\infty}^{+\infty} g(s) e^{-i\xi s} \, ds = \hat{f}(\xi) \hat{g}(\xi) $$

## Applications en Physique, Logique \& Intelligence Artificielle

### Analyse Spectrale et Traitement du Signal (Audio/Image)

Dans les architectures d'apprentissage profond traitant du signal (comme l'audio ou les séries temporelles), la transformée de Fourier constitue souvent la première étape de l'ingénierie des caractéristiques. Les réseaux de neurones sont plus à même d'apprendre des motifs invariants par translation lorsqu'ils sont exprimés dans le domaine fréquentiel, via les spectrogrammes. L'algorithme de Transformée de Fourier Rapide (FFT) permet de réaliser cette conversion en un temps très court $\mathcal{O}(N \log N)$.

### Théorie des Probabilités et Fonctions Caractéristiques

En probabilité, la fonction caractéristique d'une variable aléatoire $X$ de densité de probabilité $p(x)$ est définie comme l'espérance $\mathbb{E}[e^{itX}] = \int_{-\infty}^{+\infty} p(x) e^{itx} \, dx$.
On reconnaît exactement la transformée de Fourier de la densité $p$ (évaluée en $-t$). Cette correspondance est vitale car elle permet, grâce au théorème de convolution, de caractériser la distribution de la somme de deux variables aléatoires indépendantes : la fonction caractéristique de $X+Y$ est le produit ponctuel des fonctions caractéristiques de $X$ et de $Y$. Ce formalisme est au cœur de la démonstration du Théorème Central Limite.

### Opérations de Convolution Réseaux de Neurones (CNNs)

Les réseaux de neurones convolutifs (CNNs) s'appuient massivement sur des opérations de convolution discrètes pour extraire des filtres spatiaux sur les images. En vertu du théorème de convolution, filtrer une image avec un noyau équivaut à un simple produit scalaire dans le domaine de Fourier. Pour de très grands noyaux, certaines implémentations hautement optimisées calculent la convolution en passant les entrées et les filtres dans le domaine de Fourier (FFT), multipliant ponctuellement les matrices spectrales, puis en appliquant une transformée inverse (IFFT), ce qui réduit drastiquement la complexité algorithmique de $\mathcal{O}(N^2 M^2)$ à $\mathcal{O}(N^2 \log(N))$.
