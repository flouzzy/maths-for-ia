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

## 1. Genèse du concept et intuition physique

Historiquement, la théorie des séries de Fourier prend racine dans l'étude de l'équation de la chaleur par Joseph Fourier en 1822. Face à l'impossibilité de résoudre de manière exacte l'évolution de la température dans un corps solide en utilisant les outils classiques de l'analyse, Fourier postula une idée profondément révolutionnaire : tout signal périodique, aussi complexe ou irrégulier soit-il, peut être décomposé en une somme infinie d'ondes sinusoïdales pures.

Physiquement et géométriquement, cela revient à percevoir un signal compliqué non plus dans le domaine temporel ou spatial, mais dans le domaine fréquentiel. Au lieu de voir la variation de l'amplitude au cours du temps, nous observons le spectre des fréquences qui le composent : chaque onde élémentaire est caractérisée par une fréquence spécifique (sa "vitesse" d'oscillation) et une amplitude (son "poids" dans le signal global).

Mathématiquement, cette décomposition n'est autre qu'un changement de base dans un espace vectoriel de dimension infinie. Les fonctions trigonométriques forment une base orthogonale de l'espace des fonctions périodiques de carré intégrable. Les coefficients de Fourier apparaissent alors naturellement comme les coordonnées du signal projeté sur cette base de fonctions pures.

## 2. Définitions et Théorèmes Fondamentaux

### A. Espace des fonctions périodiques et produit scalaire

Considérons $E$, l'espace vectoriel des fonctions $f : \mathbb{R} \to \mathbb{C}$ qui sont $T$-périodiques (pour simplifier, nous prendrons $T = 2\pi$) et localement intégrables sur $[0, 2\pi]$. Pour les fonctions à valeurs complexes, nous munissons cet espace (quotienté par la relation d'égalité presque partout) du produit scalaire hermitien usuel :

> **Définition (Produit scalaire sur $L^2([0, 2\pi])$) :**
> Soient $f, g \in L^2([0, 2\pi])$. Le produit scalaire hermitien est défini par :
> $$\langle f, g \rangle = \frac{1}{2\pi} \int_0^{2\pi} f(t) \overline{g(t)} dt$$

La famille de fonctions $(e_n)_{n \in \mathbb{Z}}$ définie par $e_n(t) = e^{int}$ forme une famille orthonormale pour ce produit scalaire.

### B. Coefficients de Fourier

> **Définition (Coefficients complexes) :**
> Soit $f$ une fonction $2\pi$-périodique et intégrable sur une période. Pour tout entier $n \in \mathbb{Z}$, le $n$-ième coefficient de Fourier complexe de $f$, noté $c_n(f)$, est la projection de $f$ sur le vecteur de base $e_n$ :
> $$c_n(f) = \langle f, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} dt$$

Pour les fonctions à valeurs réelles, il est souvent plus commode d'utiliser la décomposition trigonométrique réelle.

> **Définition (Coefficients réels) :**
> Si $f : \mathbb{R} \to \mathbb{R}$ est $2\pi$-périodique, ses coefficients de Fourier réels $a_n$ et $b_n$ sont donnés par :
> $$a_0 = \frac{1}{\pi} \int_0^{2\pi} f(t) dt \quad \text{ (à noter que } c_0 = \frac{a_0}{2} \text{) }$$
> $$a_n = \frac{1}{\pi} \int_0^{2\pi} f(t) \cos(nt) dt \quad \text{pour } n \ge 1$$
> $$b_n = \frac{1}{\pi} \int_0^{2\pi} f(t) \sin(nt) dt \quad \text{pour } n \ge 1$$
> La relation entre les coefficients est : $c_n = \frac{a_n - i b_n}{2}$ pour $n \ge 1$, et $c_{-n} = \overline{c_n}$.

### C. Série de Fourier et Théorème de Dirichlet

> **Définition (Série de Fourier) :**
> La série de Fourier associée à $f$ est la série de fonctions dont les sommes partielles sont :
> $$S_N(f)(t) = \sum_{n=-N}^N c_n(f) e^{int} = \frac{a_0}{2} + \sum_{n=1}^N \left( a_n \cos(nt) + b_n \sin(nt) \right)$$

Un point fondamental est de déterminer en quel sens cette série converge vers $f$. Le théorème suivant, dû à Peter Gustav Lejeune Dirichlet, donne une condition suffisante pour la convergence ponctuelle.

> **Théorème de Dirichlet :**
> Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction $2\pi$-périodique. Si $f$ est de classe $C^1$ par morceaux sur $\mathbb{R}$, alors pour tout $t \in \mathbb{R}$, la série de Fourier de $f$ converge et sa somme vaut la moyenne des limites à gauche et à droite de $f$ en $t$ :
> $$\lim_{N \to +\infty} S_N(f)(t) = \frac{f(t^+) + f(t^-)}{2}$$
> En particulier, si $f$ est continue en $t$, la série converge vers $f(t)$.

**Exemple Concret 1 : Calcul sur un signal en créneau**
Considérons le signal en créneau $2\pi$-périodique défini sur $]-\pi, \pi]$ par :
$$f(t) = \begin{cases} -1 & \text{si } t \in ]-\pi, 0[ \\ 1 & \text{si } t \in ]0, \pi] \end{cases}$$
La fonction est impaire, donc tous les coefficients $a_n$ sont nuls pour $n \ge 0$.
Calculons les coefficients $b_n$ pour $n \ge 1$ :
$$b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) dt = \frac{1}{\pi} \left( \int_{-\pi}^{0} (-1) \sin(nt) dt + \int_{0}^{\pi} (1) \sin(nt) dt \right)$$
La fonction $t \mapsto f(t)\sin(nt)$ est paire, donc :
$$b_n = \frac{2}{\pi} \int_{0}^{\pi} \sin(nt) dt = \frac{2}{\pi} \left[ -\frac{\cos(nt)}{n} \right]_0^\pi = \frac{2}{\pi n} \left( 1 - (-1)^n \right)$$
Ainsi, si $n = 2k$ est pair, $b_{2k} = 0$.
Si $n = 2k+1$ est impair, $b_{2k+1} = \frac{4}{\pi (2k+1)}$.
La série de Fourier de $f$ s'écrit donc :
$$S(f)(t) = \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{\sin((2k+1)t)}{2k+1} = \frac{4}{\pi} \left( \sin(t) + \frac{\sin(3t)}{3} + \frac{\sin(5t)}{5} + \dots \right)$$
Le théorème de Dirichlet nous assure que pour $t \in ]0, \pi[$, la série converge vers $1$.
Pour $t = 0$ ou $t = \pi$, les limites à gauche et à droite sont $1$ et $-1$, la demi-somme vaut $0$, ce qui est cohérent avec le fait que tous les $\sin(nt)$ sont nuls en ces points.

## 3. Démonstrations

### Démonstration de l'orthonormalité de la famille $(e_n)_{n \in \mathbb{Z}}$

Nous devons prouver que $\langle e_n, e_m \rangle = \delta_{n,m}$, où $\delta_{n,m}$ est le symbole de Kronecker.
Par définition du produit scalaire sur $L^2([0, 2\pi])$ :
$$\langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e_n(t) \overline{e_m(t)} dt = \frac{1}{2\pi} \int_0^{2\pi} e^{int} e^{-imt} dt = \frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)t} dt$$
Séparons en deux cas :
1. **Si $n = m$ :**
   Alors $n-m = 0$, d'où $e^{i(n-m)t} = e^0 = 1$.
   L'intégrale devient :
   $$\langle e_n, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} 1 dt = \frac{1}{2\pi} \left[ t \right]_0^{2\pi} = \frac{2\pi}{2\pi} = 1$$
2. **Si $n \neq m$ :**
   Alors $n-m \neq 0$. La primitive de $t \mapsto e^{i(n-m)t}$ est $t \mapsto \frac{e^{i(n-m)t}}{i(n-m)}$.
   L'intégrale devient :
   $$\langle e_n, e_m \rangle = \frac{1}{2\pi} \left[ \frac{e^{i(n-m)t}}{i(n-m)} \right]_0^{2\pi} = \frac{1}{2\pi i (n-m)} \left( e^{i(n-m)2\pi} - e^0 \right)$$
   Puisque $n-m$ est un entier non nul, la fonction complexe $z \mapsto e^{iz}$ est $2\pi$-périodique, d'où $e^{i(n-m)2\pi} = 1$.
   Ainsi :
   $$\langle e_n, e_m \rangle = \frac{1}{2\pi i (n-m)} (1 - 1) = 0$$

Cela prouve que la famille $(e_n)_{n \in \mathbb{Z}}$ est bien orthonormale. De cette orthonormalité découle directement l'unicité des coefficients pour un polynôme trigonométrique. Si $f(t) = \sum_{k=-N}^N \alpha_k e^{ikt}$, alors la projection de $f$ sur $e_n$ donne $\langle f, e_n \rangle = \sum_{k=-N}^N \alpha_k \langle e_k, e_n \rangle = \alpha_n$. Les coefficients de Fourier sont ainsi les seules composantes possibles d'un signal sur la base fréquentielle.

## 4. Applications en Physique, Logique et Intelligence Artificielle

L'analyse de Fourier dépasse largement le cadre des mathématiques pures et constitue le socle du traitement moderne du signal et de l'intelligence artificielle.

- **Traitement du Signal et Acoustique :** En physique des ondes, toute vibration (sonore, lumineuse, sismique) est analysée par ses composantes de Fourier. Les algorithmes de compression comme le format MP3 exploitent cette décomposition : l'oreille humaine étant insensible à certaines hautes et basses fréquences, l'algorithme calcule les coefficients de Fourier du signal audio, supprime les fréquences inaudibles (mettant les coefficients correspondants à zéro), puis transmet un signal reconstitué, réduisant drastiquement la taille du fichier.
- **Réseaux de Neurones et Biais Spectral :** En Intelligence Artificielle, les réseaux de neurones profonds exhibent un phénomène connu sous le nom de "biais spectral" (spectral bias). Lorsqu'un réseau de neurones apprend une fonction, il apprend d'abord les composantes à basse fréquence de cette fonction avant de s'adapter aux composantes à haute fréquence. L'analyse de Fourier permet aux chercheurs en IA d'étudier la dynamique d'apprentissage et explique pourquoi les réseaux sont robustes au bruit haute-fréquence, mais peinent parfois à modéliser des détails très fins sans architectures adaptées (comme les Positional Encodings dans les Transformers).
- **Transformée de Fourier Rapide (FFT) en Convolution :** Les réseaux de neurones convolutifs (CNN) appliquent des filtres sur des images de manière spatiale. Pour des filtres de grande taille, le calcul direct de la convolution est coûteux (complexité quadratique). Grâce au théorème de convolution (qui stipule que la transformée de Fourier d'une convolution est le produit des transformées de Fourier), il est possible de calculer les CNN de manière extrêmement rapide en utilisant la FFT, réduisant la complexité computationnelle et permettant le traitement en temps réel d'images haute résolution.
