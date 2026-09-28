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

# Séries de Fourier

## Introduction Historique et Physique

L'étude des séries de Fourier trouve son origine dans les travaux de Joseph Fourier au début du XIXe siècle sur la propagation de la chaleur. Le problème consistait à déterminer l'évolution de la température dans un corps solide. Fourier a postulé et démontré de manière formelle que toute fonction périodique (représentant par exemple une condition initiale thermique ou une onde vibratoire) peut être décomposée en une somme, éventuellement infinie, de fonctions trigonométriques simples : des sinus et des cosinus.

Cette décomposition transforme un problème complexe dans le domaine temporel ou spatial en une analyse dans le domaine fréquentiel. L'importance de ce concept dépasse largement la thermodynamique : il est fondamental en traitement du signal, en mécanique quantique, en imagerie médicale, et dans les télécommunications modernes.

## Définitions, Théorèmes et Exemples

### Cadre et Espaces de Fonctions

Soit $T > 0$. On note $\omega = \frac{2\pi}{T}$ la pulsation fondamentale.
On travaille typiquement avec des fonctions $f : \mathbb{R} \to \mathbb{C}$, périodiques de période $T$ (souvent $T = 2\pi$, d'où $\omega = 1$).
Pour que les coefficients de Fourier soient bien définis, on demande que $f$ soit localement intégrable sur $\mathbb{R}$. L'espace naturel d'étude est $L^2([0, T])$, l'espace des fonctions de carré intégrable, muni du produit scalaire :
$$ \langle f, g \rangle = \frac{1}{T} \int_0^T f(t) \overline{g(t)} dt $$

### Coefficients de Fourier Exponentiels

**Définition (Coefficients complexes) :**
Pour tout entier $n \in \mathbb{Z}$, le $n$-ième coefficient de Fourier exponentiel de $f$ est défini par :
$$ c_n(f) = \frac{1}{T} \int_0^T f(t) e^{-in\omega t} dt $$

*Exemple 1 (Fonction constante) :*
Soit $f(t) = K$, une constante.
$c_0(f) = \frac{1}{2\pi} \int_0^{2\pi} K dt = K$.
Pour $n \neq 0$, $c_n(f) = \frac{K}{2\pi} \int_0^{2\pi} e^{-int} dt = \frac{K}{2\pi} \left[ \frac{e^{-int}}{-in} \right]_0^{2\pi} = 0$.

*Exemple 2 (Fonction sinus) :*
Soit $f(t) = \sin(t) = \frac{e^{it} - e^{-it}}{2i}$ (avec $T = 2\pi$).
On identifie directement les coefficients :
$c_1(f) = \frac{1}{2i} = -\frac{i}{2}$ et $c_{-1}(f) = -\frac{1}{2i} = \frac{i}{2}$.
Pour tout autre $n \notin \{-1, 1\}$, $c_n(f) = 0$.

### Coefficients de Fourier Trigonométriques

Si la fonction $f$ est à valeurs réelles, on peut utiliser la base trigonométrique.

**Définition (Coefficients réels) :**
Pour $n \ge 0$, on définit $a_n(f)$ et pour $n \ge 1$, $b_n(f)$ par :
$$ a_0(f) = \frac{1}{T} \int_0^T f(t) dt $$
$$ a_n(f) = \frac{2}{T} \int_0^T f(t) \cos(n\omega t) dt \quad (n \ge 1) $$
$$ b_n(f) = \frac{2}{T} \int_0^T f(t) \sin(n\omega t) dt \quad (n \ge 1) $$

*Exemple 3 (Relation entre les coefficients) :*
Calculons le lien explicite pour $T=2\pi$. On a $e^{-int} = \cos(nt) - i\sin(nt)$.
Donc $c_n = \frac{1}{2\pi} \int f(t)(\cos(nt) - i\sin(nt))dt = \frac{a_n - ib_n}{2}$ pour $n \ge 1$.
De même, $c_{-n} = \frac{a_n + ib_n}{2}$.
Et $a_n = c_n + c_{-n}$, $b_n = i(c_n - c_{-n})$.

*Exemple 4 (Signal carré) :*
Soit $f$ de période $2\pi$, définie par $f(t) = 1$ sur $[0, \pi[$ et $f(t) = -1$ sur $[\pi, 2\pi[$.
- Valeur moyenne $a_0 = \frac{1}{2\pi} (\int_0^\pi 1 dt + \int_\pi^{2\pi} (-1) dt) = 0$.
- $f$ étant impaire, on démontre que $a_n = 0$ pour tout $n$.
- Calculons $b_n$ :
$$ b_n = \frac{1}{\pi} \int_0^{2\pi} f(t) \sin(nt) dt = \frac{1}{\pi} \left( \int_0^\pi \sin(nt) dt - \int_\pi^{2\pi} \sin(nt) dt \right) $$
$$ \int_0^\pi \sin(nt) dt = \left[ -\frac{\cos(nt)}{n} \right]_0^\pi = \frac{1 - (-1)^n}{n} $$
Par périodicité de $\sin(nt)$, $\int_\pi^{2\pi} \sin(nt) dt = - \int_0^\pi \sin(nt) dt$.
Donc $b_n = \frac{2}{\pi} \frac{1 - (-1)^n}{n}$.
Si $n$ est pair ($n=2p$), $b_{2p} = 0$.
Si $n$ est impair ($n=2p+1$), $b_{2p+1} = \frac{4}{\pi(2p+1)}$.

### Sommes de Fourier et Théorème de Dirichlet

**Définition (Somme partielle) :**
La série de Fourier (ou somme partielle d'ordre $N$) associée à $f$ est la fonction :
$$ S_N(f)(t) = \sum_{n=-N}^N c_n(f) e^{in\omega t} = a_0(f) + \sum_{n=1}^N \left( a_n(f) \cos(n\omega t) + b_n(f) \sin(n\omega t) \right) $$

**Théorème (Théorème de Dirichlet) :**
Si $f$ est périodique et de classe $C^1$ par morceaux sur $\mathbb{R}$, alors pour tout $t \in \mathbb{R}$, la série de Fourier $S_N(f)(t)$ converge lorsque $N \to \infty$ vers la demi-somme des limites à gauche et à droite de $f$ en $t$ :
$$ \lim_{N \to \infty} S_N(f)(t) = \frac{f(t^+) + f(t^-)}{2} $$
En particulier, si $f$ est continue en $t$, la série converge vers $f(t)$.

*Exemple 5 (Application de Dirichlet au signal carré) :*
Pour le signal carré défini précédemment au point $t = \pi/2$ (où $f$ est continue et vaut $1$) :
$$ f(\pi/2) = 1 = \sum_{p=0}^\infty \frac{4}{\pi(2p+1)} \sin\left((2p+1)\frac{\pi}{2}\right) $$
Puisque $\sin\left(p\pi + \frac{\pi}{2}\right) = (-1)^p$, on obtient :
$$ 1 = \frac{4}{\pi} \sum_{p=0}^\infty \frac{(-1)^p}{2p+1} \implies \sum_{p=0}^\infty \frac{(-1)^p}{2p+1} = \frac{\pi}{4} $$
C'est la célèbre formule de Gregory-Leibniz.

*Exemple 6 (Discontinuité) :*
Pour le même signal carré en $t = 0$. La limite à droite est $1$, à gauche $-1$.
La demi-somme est $(1 + (-1)) / 2 = 0$.
Effectivement, en $t=0$, $S_N(f)(0) = \sum b_n \sin(0) = 0$.

## Démonstrations

### Preuve de l'orthogonalité de la base exponentielle

Nous devons montrer que la famille $e_n(t) = e^{int}$ (pour $T=2\pi$) forme un système orthogonal pour le produit scalaire usuel.
Soient $n, m \in \mathbb{Z}$. Calculons le produit scalaire :
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{int} \overline{e^{imt}} dt $$
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)t} dt $$

Cas 1 : $n = m$.
Alors $e^{i(n-m)t} = e^0 = 1$.
$$ \langle e_n, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} 1 dt = 1 $$

Cas 2 : $n \neq m$.
La primitive de $t \mapsto e^{i(n-m)t}$ est $t \mapsto \frac{1}{i(n-m)} e^{i(n-m)t}$.
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \left[ \frac{e^{i(n-m)t}}{i(n-m)} \right]_0^{2\pi} $$
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi i(n-m)} \left( e^{i(n-m)2\pi} - e^0 \right) $$
Or pour tout entier $k = n-m$, $e^{i2\pi k} = 1$.
Donc $\langle e_n, e_m \rangle = \frac{1}{2\pi i(n-m)} (1 - 1) = 0$.

La famille est bien orthonormée.

### Extraction des coefficients (Lemme d'unicité)

Supposons qu'une fonction se décompose en une série uniformément convergente $f(t) = \sum_{k=-\infty}^{+\infty} \alpha_k e^{ikt}$. Démontrons que $\alpha_n = c_n(f)$.
Multiplions l'égalité par $e^{-int}$ :
$$ f(t) e^{-int} = \sum_{k=-\infty}^{+\infty} \alpha_k e^{i(k-n)t} $$
Intégrons de $0$ à $2\pi$. La convergence uniforme permet d'intervertir l'intégrale et la somme infinie :
$$ \int_0^{2\pi} f(t) e^{-int} dt = \sum_{k=-\infty}^{+\infty} \alpha_k \int_0^{2\pi} e^{i(k-n)t} dt $$
D'après la propriété d'orthogonalité démontrée précédemment, l'intégrale du membre de droite est nulle pour tout $k \neq n$, et vaut $2\pi$ pour $k=n$.
Il ne reste qu'un seul terme dans la somme :
$$ \int_0^{2\pi} f(t) e^{-int} dt = \alpha_n \times 2\pi $$
D'où :
$$ \alpha_n = \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt = c_n(f) $$
Ce qui démontre rigoureusement l'unicité des coefficients de Fourier.

## Applications en Physique, Logique, et IA

L'analyse de Fourier est une pierre angulaire dans de multiples domaines appliqués et fondamentaux :

1.  **Traitement du Signal et Audio (IA) :**
    Les réseaux de neurones appliqués au son (comme l'architecture Whisper ou les modèles de séparation de sources) ne traitent presque jamais l'onde temporelle brute. Ils utilisent une Transformée de Fourier à Court Terme (STFT) pour générer un spectrogramme, qui représente l'énergie des différentes fréquences au cours du temps. L'apprentissage profond extrait ensuite des motifs (phonèmes, instruments) depuis cette représentation temps-fréquence.

2.  **Imagerie Médicale (IRM) :**
    La résonance magnétique nucléaire capte des données directement dans le domaine fréquentiel (appelé l'espace k). La reconstruction de l'image anatomique du patient est littéralement une transformée de Fourier inverse bidimensionnelle du signal capté.

3.  **Résolution d'Équations aux Dérivées Partielles (Physique) :**
    La décomposition d'une fonction spatiale en ondes de Fourier permet de transformer les opérateurs différentiels (comme le laplacien $\Delta$) en simples multiplications algébriques (par $-||\xi||^2$). C'est ainsi que l'on résout l'équation de la chaleur, l'équation des ondes, ou l'équation de Schrödinger en mécanique quantique.

4.  **Biais Spectral des Réseaux de Neurones :**
    En théorie de l'apprentissage automatique, le théorème de "Spectral Bias" montre, via l'analyse de Fourier, que les réseaux de neurones complètement connectés avec descente de gradient apprennent d'abord les composantes de basse fréquence (la tendance globale) avant de mémoriser les composantes de haute fréquence (les détails ou le bruit).
