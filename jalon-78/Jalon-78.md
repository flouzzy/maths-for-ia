---
uuid: "jalon-78"
title: "Séries de Fourier"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon-77.md|Jalon 77 : Densité des fonctions simples]]"
next: "[[Jalon-79.md|Jalon 79 : Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.]]"
---

# Jalon 78 : Séries de Fourier

## 1. Introduction à la décomposition fréquentielle

Au début du XIXe siècle, Joseph Fourier, alors préoccupé par l'étude de la propagation de la chaleur dans les corps solides, propose une idée révolutionnaire qui heurtera de nombreux mathématiciens de son époque (comme Lagrange ou Laplace) : toute fonction périodique, même discontinue ou présentant des "sauts" brusques, peut être représentée comme une somme infinie de fonctions trigonométriques simples, c'est-à-dire des sinus et des cosinus.

Physiquement, cela revient à affirmer qu'un signal d'une complexité arbitraire (comme le son d'un orchestre, la variation d'une température ou les pulsations d'un courant électrique alternatif) n'est que la superposition d'ondes pures, chacune caractérisée par une fréquence propre (son rythme), une amplitude (son intensité) et une phase (son décalage).

Géométriquement, l'espace des fonctions périodiques peut être vu comme un espace vectoriel de dimension infinie. Dans cet espace, les fonctions $t \mapsto \cos(nt)$ et $t \mapsto \sin(nt)$ jouent le rôle de "vecteurs de base" formant un repère orthogonal. Calculer la série de Fourier d'un signal revient alors simplement à projeter ce signal sur chacun de ces axes fondamentaux, extrayant ainsi sa "recette" fréquentielle.

## 2. Définitions, Théorèmes et Exemples Concrets

Pour cette leçon, nous nous plaçons sur $\mathbb{R}$ et nous considérons des fonctions $T$-périodiques. Pour simplifier l'exposé algébrique, nous fixerons $T = 2\pi$. Soit $f : \mathbb{R} \to \mathbb{C}$ une fonction $2\pi$-périodique, localement intégrable au sens de Lebesgue (ou Riemann).

### Définition des coefficients de Fourier

**Coefficients complexes**
L'approche la plus élégante utilise l'exponentielle complexe. Pour tout entier relatif $n \in \mathbb{Z}$, on définit le $n$-ième coefficient de Fourier de $f$, noté $c_n(f)$, par la projection canonique :

$$ c_n(f) = \frac{1}{2\pi} \int_{0}^{2\pi} f(t) e^{-int} \, dt $$

**Coefficients réels**
Si le signal $f$ est à valeurs réelles, il est souvent plus intuitif de travailler avec des sinus et des cosinus. Pour $n \in \mathbb{N}$, on définit :

$$ a_n(f) = \frac{1}{\pi} \int_{0}^{2\pi} f(t) \cos(nt) \, dt \quad \text{pour } n \ge 0 $$
$$ b_n(f) = \frac{1}{\pi} \int_{0}^{2\pi} f(t) \sin(nt) \, dt \quad \text{pour } n \ge 1 $$

*(Note : On a $a_0(f) = 2c_0(f)$ qui représente la valeur moyenne du signal).* Les liens entre coefficients réels et complexes sont donnés par les formules d'Euler : $c_n = \frac{a_n - i b_n}{2}$ pour $n > 0$, et $c_{-n} = \frac{a_n + i b_n}{2}$.

### Série de Fourier formelle

La série de Fourier associée à la fonction $f$, notée $S(f)$, est la série de fonctions définie formellement par :

$$ S(f)(t) = \sum_{n=-\infty}^{+\infty} c_n(f) e^{int} = \frac{a_0(f)}{2} + \sum_{n=1}^{+\infty} \left( a_n(f) \cos(nt) + b_n(f) \sin(nt) \right) $$

La somme partielle d'ordre $N$, qui constitue l'approximation fréquentielle du signal, est :

$$ S_N(f)(t) = \sum_{n=-N}^{N} c_n(f) e^{int} $$

### Théorème de Dirichlet (Convergence ponctuelle)

> **Théorème de Dirichlet :**
> Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction $2\pi$-périodique et continue par morceaux. Si $f$ est de classe $C^1$ par morceaux sur $\mathbb{R}$, alors pour tout $t \in \mathbb{R}$, la série de Fourier de $f$ converge ponctuellement vers la valeur moyenne des limites à gauche et à droite de $f$ en $t$ :
> $$ \lim_{N \to +\infty} S_N(f)(t) = \frac{f(t^+) + f(t^-)}{2} $$
> En particulier, si $f$ est continue au point $t$, alors $S(f)(t) = f(t)$.

**Exemple concret immédiat : Le signal "Carré"**

Considérons un signal $2\pi$-périodique défini sur $]-\pi, \pi]$ par :
$$ f(t) = \begin{cases} -1 & \text{si } t \in ]-\pi, 0[ \\ 1 & \text{si } t \in [0, \pi] \end{cases} $$
(Ce signal est impair, sauf au point $t=0$ qui est un saut, où l'on pourrait le définir par convention à 0).
Puisque $f$ est impaire, tous ses coefficients $a_n$ sont nuls (l'intégrale d'une fonction impaire sur une période symétrique est nulle).
Calculons $b_n$ pour $n \ge 1$ :
$$ b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin(nt) \, dt = \frac{2}{\pi} \int_{0}^{\pi} 1 \cdot \sin(nt) \, dt $$
(car le produit de deux fonctions impaires est pair).
$$ b_n = \frac{2}{\pi} \left[ \frac{-\cos(nt)}{n} \right]_0^\pi = \frac{2}{n\pi} (1 - \cos(n\pi)) = \frac{2}{n\pi} (1 - (-1)^n) $$
Si $n=2k$ (pair), $1 - (-1)^{2k} = 0 \implies b_{2k} = 0$.
Si $n=2k+1$ (impair), $1 - (-1)^{2k+1} = 2 \implies b_{2k+1} = \frac{4}{(2k+1)\pi}$.

La série de Fourier est donc :
$$ S(f)(t) = \frac{4}{\pi} \sum_{k=0}^{+\infty} \frac{\sin((2k+1)t)}{2k+1} = \frac{4}{\pi} \left( \sin(t) + \frac{\sin(3t)}{3} + \frac{\sin(5t)}{5} + \dots \right) $$
En vertu du théorème de Dirichlet, pour $t \in ]0, \pi[$, la série vaut 1.
Au point de discontinuité $t=0$, la série donne trivialement $0$, ce qui correspond bien à la demi-somme des limites : $\frac{f(0^+) + f(0^-)}{2} = \frac{1 + (-1)}{2} = 0$.

## 3. Démonstrations Pas-à-Pas

Nous allons démontrer la formule des coefficients de Fourier, c'est-à-dire le caractère orthogonal de la famille $(e_n)_{n \in \mathbb{Z}}$ où $e_n(t) = e^{int}$.

**Théorème (Orthogonalité) :**
Pour tous $n, m \in \mathbb{Z}$, on a :
$$ \frac{1}{2\pi} \int_{0}^{2\pi} e^{int} e^{-imt} \, dt = \delta_{n,m} $$
où $\delta_{n,m}$ est le symbole de Kronecker (1 si $n=m$, 0 sinon).

**Démonstration rigoureuse :**

1. **Initialisation et cas où $n = m$ :**
   Fixons $n \in \mathbb{Z}$ et supposons que $m = n$. L'exposant devient $i(n-n)t = 0$.
   $$ \frac{1}{2\pi} \int_{0}^{2\pi} e^{int} e^{-int} \, dt = \frac{1}{2\pi} \int_{0}^{2\pi} e^0 \, dt $$
   $$ \frac{1}{2\pi} \int_{0}^{2\pi} 1 \, dt = \frac{1}{2\pi} [t]_0^{2\pi} = \frac{2\pi}{2\pi} = 1 $$

2. **Étape 2 : Cas où $n \neq m$ :**
   Supposons maintenant $n \neq m$, ce qui implique que $n-m \neq 0$. L'intégrande est $e^{i(n-m)t}$.
   $$ \frac{1}{2\pi} \int_{0}^{2\pi} e^{i(n-m)t} \, dt $$
   La fonction $t \mapsto e^{i(n-m)t}$ admet pour primitive $t \mapsto \frac{e^{i(n-m)t}}{i(n-m)}$.
   Appliquons les bornes d'intégration :
   $$ = \frac{1}{2\pi} \left[ \frac{e^{i(n-m)t}}{i(n-m)} \right]_0^{2\pi} = \frac{1}{2\pi i (n-m)} \left( e^{i(n-m)2\pi} - e^0 \right) $$

3. **Étape 3 : Évaluation de l'exponentielle complexe aux bornes :**
   Puisque $n-m$ est un entier non nul (disons $k \in \mathbb{Z}^*$), évaluons $e^{i2k\pi}$.
   Par la formule d'Euler :
   $$ e^{i2k\pi} = \cos(2k\pi) + i \sin(2k\pi) = 1 + i \cdot 0 = 1 $$
   Et $e^0 = 1$.
   Donc la différence entre les bornes donne :
   $$ e^{i(n-m)2\pi} - e^0 = 1 - 1 = 0 $$

4. **Conclusion :**
   L'intégrale est donc strictement nulle pour tout $n \neq m$. La famille des exponentielles complexes est bien une famille orthonormée pour le produit scalaire hermitien canonique défini par $\langle f, g \rangle = \frac{1}{2\pi} \int_0^{2\pi} f(t)\overline{g(t)} dt$. Par conséquent, si un signal $f$ s'écrit comme une somme convergente (ou finie) $f(t) = \sum_{k \in \mathbb{Z}} \alpha_k e^{ikt}$, le calcul du coefficient $c_n(f)$ projette orthogonalement $f$ sur le vecteur de base $e_n$ et isole exactement le coefficient $\alpha_n$.

## 4. Applications en Intelligence Artificielle et en Physique

Les séries de Fourier forment le socle fondamental du traitement du signal, une branche devenue aujourd'hui indispensable au cœur des architectures d'Intelligence Artificielle.

**En Architecture Convolutive (CNNs) et Vision par Ordinateur :**
Le calcul d'une convolution entre un très grand filtre et une image haute résolution a une complexité temporelle désastreuse dans le domaine spatial. Le théorème de convolution stipule que la convolution dans l'espace "normal" équivaut à un simple produit terme à terme dans l'espace des fréquences (espace de Fourier). Ainsi, les algorithmes de FFT (Fast Fourier Transform, version discrète de la théorie des séries de Fourier) sont implémentés au niveau matériel (GPU) pour accélérer massivement les couches de convolution, rendant l'apprentissage des CNNs (ResNet, VGG) possible à l'échelle industrielle.

**En Traitement du Langage Naturel et Séries Temporelles (Transformers) :**
La notion de "fréquence" est réapparue brillamment dans l'architecture des Transformers sous le nom d'**Encodage Positionnel** (Positional Encoding). Pour injecter la notion d'ordre des mots dans une architecture qui traite tout en parallèle (via l'Attention), Vaswani et al. (2017) utilisent des ondes sinusoïdales et cosinusoïdales de différentes fréquences :
$$ PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$
$$ PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$
L'espace vectoriel engendré par ces bases trigonométriques permet au réseau de neurones de "calculer" des distances relatives entre les mots exactement comme l'analyse de Fourier décompose les relations temporelles d'un signal.

**En Audio et Spectrogrammes :**
Toute IA moderne de traitement vocal (Whisper d'OpenAI, Siri) ne lit pas le signal sonore brut (l'amplitude de l'air sur le microphone au cours du temps). Le signal est d'abord tronçonné en petites fenêtres temporelles, et sur chaque fenêtre, on calcule la décomposition en séries de Fourier (Transformée de Fourier à Court Terme). Le résultat est un spectrogramme (une carte 2D : temps vs. fréquence), sur lequel un réseau de neurones convolutif classique peut opérer pour déduire des phonèmes ou des mots. La théorie de Fourier est le pont absolu entre le monde physique continu de l'onde sonore et la matrice de données structurées exploitable par l'IA.
