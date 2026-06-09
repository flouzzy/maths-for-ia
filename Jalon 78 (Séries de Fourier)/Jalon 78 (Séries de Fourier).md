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

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un chef cuisinier. On vous apporte un plat tout prêt (un signal complexe $f$) et on vous demande de retrouver la recette.
    - Les **Séries de Fourier**, c'est l'art de décomposer n'importe quel signal périodique en une liste d'ingrédients de base : des ondes pures (des sinus et des cosinus).
    - Chaque ingrédient a une vitesse (fréquence) et une quantité (amplitude).
    - En mélangeant ces ondes simples, vous pouvez reconstruire n'importe quel son, n'importe quelle image ou n'importe quel mouvement vibratoire.
- **Le "Pourquoi on a inventé ça" :** Joseph Fourier voulait comprendre comment la chaleur se propage dans un objet. Il a réalisé qu'il était beaucoup plus facile de résoudre des équations compliquées en travaillant sur des ondes simples. Aujourd'hui, c'est le langage universel des télécommunications (Wifi, 5G), de la musique numérique (MP3) et de l'imagerie médicale.
- **Visualisation :** Un signal carré qui est approché par des vagues de plus en plus nombreuses. Au début, c'est très approximatif, mais avec une infinité d'ondes, on obtient les angles droits parfaits du carré.

## 2. Formalisation

Soit $f : \mathbb{R} \to \mathbb{C}$ une fonction $T$-périodique (généralement $T=2\pi$) et localement intégrable.

### A. Coefficients de Fourier

On utilise la famille orthonormée de $L^2([0, 2\pi])$ définie par $e_n(t) = e^{int}$.

> **Définition 1 (Coefficients complexes) :**
> Pour tout $n \in \mathbb{Z}$, le $n$-ième coefficient de Fourier de $f$ est :
> $$c_n(f) = \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt$$

> **Définition 2 (Coefficients réels) :**
> Si $f$ est à valeurs réelles, on définit $a_n$ et $b_n$ tels que :
> $a_n = c_n + c_{-n} = \frac{1}{\pi} \int_0^{2\pi} f(t) \cos(nt) dt$
> $b_n = i(c_n - c_{-n}) = \frac{1}{\pi} \int_0^{2\pi} f(t) \sin(nt) dt$

### B. Somme de Fourier

La série de Fourier associée à $f$ est la série de fonctions :
$$S_N(f)(t) = \sum_{n=-N}^N c_n(f) e^{int} = \frac{a_0}{2} + \sum_{n=1}^N (a_n \cos(nt) + b_n \sin(nt))$$

## 3. Démonstrations

### Pourquoi la formule du coefficient $c_n$ marche-t-elle ?

Supposons que $f(t) = \sum_{k=-\infty}^{+\infty} \alpha_k e^{ikt}$. Nous voulons retrouver les $\alpha_k$.

1. **Projection :** Multiplions les deux côtés par $e^{-int}$ et intégrons sur une période $[0, 2\pi]$ :
   $$\int_0^{2\pi} f(t) e^{-int} dt = \int_0^{2\pi} \left( \sum_{k=-\infty}^{+\infty} \alpha_k e^{ikt} \right) e^{-int} dt$$
2. **Interversion :** Sous réserve de convergence uniforme (ou dans $L^2$), on intervertit somme et intégrale :
   $$\int_0^{2\pi} f(t) e^{-int} dt = \sum_{k=-\infty}^{+\infty} \alpha_k \left( \int_0^{2\pi} e^{i(k-n)t} dt \right)$$
3. **Orthogonalité :** Calculons l'intégrale élémentaire :
   - Si $k \neq n$ : $\int_0^{2\pi} e^{i(k-n)t} dt = [\frac{e^{i(k-n)t}}{i(k-n)}]_0^{2\pi} = \frac{1 - 1}{i(k-n)} = 0$.
   - Si $k = n$ : $\int_0^{2\pi} e^0 dt = 2\pi$.
4. **Conclusion :** Dans la somme infinie, seul le terme $k=n$ survit.
   $$\int_0^{2\pi} f(t) e^{-int} dt = \alpha_n \cdot 2\pi \implies \alpha_n = c_n(f)$$

## 4. Exercices d'Application

### Exercice 1 : Signal en dents de scie
**Énoncé :** Soit $f$ la fonction $2\pi$-périodique définie par $f(t) = t$ sur $]-\pi, \pi]$. Calculer ses coefficients de Fourier.
**Correction Détaillée :**
1. **Parité :** $f$ est impaire, donc $a_n = 0$ pour tout $n$.
2. **Calcul de $b_n$ :** $b_n = \frac{2}{\pi} \int_0^\pi t \sin(nt) dt$.
3. **IPP :** $u=t, v'=\sin(nt) \implies u'=1, v=-\cos(nt)/n$.
   $b_n = \frac{2}{\pi} \left( [-\frac{t \cos(nt)}{n}]_0^\pi + \int_0^\pi \frac{\cos(nt)}{n} dt \right) = \frac{2}{\pi} [-\frac{\pi \cos(n\pi)}{n} + 0] = -\frac{2}{n} (-1)^n = \frac{2(-1)^{n+1}}{n}$.
4. **Résultat :** $S(f)(t) = 2 \left( \sin(t) - \frac{\sin(2t)}{2} + \frac{\sin(3t)}{3} - \dots \right)$.

### Exercice 2 : Niveau Avancé (Théorème de Dirichlet)
**Énoncé :** Vers quoi converge la série de Fourier au point de discontinuité $\pi$ pour la fonction précédente ?
**Correction Détaillée :**
D'après le théorème de Dirichlet, la série converge vers la demi-somme des limites à gauche et à droite : $\frac{f(\pi^-) + f(\pi^+)}{2} = \frac{\pi + (-\pi)}{2} = 0$. On remarque que pour $t=\pi$, tous les $\sin(n\pi)$ sont nuls, donc la somme est bien 0.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Fourier permet de passer du **domaine temporel** (ou spatial) au **domaine fréquentiel**. En IA, de nombreux problèmes sont beaucoup plus simples à résoudre dans l'espace des fréquences.
- **Example Concret :**
    - **Audio et Spectrogrammes :** Pour qu'une IA reconnaisse votre voix (Siri/Alexa), elle transforme d'abord l'onde sonore en spectrogramme (une image des fréquences au cours du temps) via une transformée de Fourier rapide (FFT). Le réseau de neurones "voit" alors les fréquences fondamentales de votre voix.
    - **Convolution et FFT :** Faire une convolution dans le domaine spatial (image) revient à faire un simple produit dans le domaine fréquentiel (Fourier). Pour les très grands filtres, on utilise Fourier pour accélérer l'IA.
    - **Analyse du "Spectral Bias" :** Les réseaux de neurones ont une tendance naturelle à apprendre les fonctions de basse fréquence avant les hautes fréquences. L'analyse de Fourier permet de quantifier cette préférence et d'expliquer pourquoi les réseaux sont robustes au bruit (le bruit est souvent de haute fréquence).

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]], [[Jalon 37 (Intégrale de Riemann sur un segment).md]]
- **Concepts Futurs dépendants :** [[Jalon 79 (Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]]
