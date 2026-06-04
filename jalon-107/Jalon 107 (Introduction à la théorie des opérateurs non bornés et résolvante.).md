---
uuid: "jalon-107"
title: "Introduction aux opérateurs non bornés"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/fondations
prev: "[[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]]"
next: "[[Jalon 108 (Livrable IA).md]]"
---

# Jalon 107 : Introduction aux opérateurs non bornés

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez une machine à laver très puissante.
    - La machine ne peut pas laver n'importe quoi : si vous mettez des briques dedans, elle casse (c'est le **Domaine** de la machine).
    - Pour certains vêtements très délicats qui tournent très vite, la force centrifuge peut devenir infinie (c'est le caractère **Non borné**).
    - L'**Opérateur de dérivation** est cette machine : plus une fonction ondule vite, plus sa dérivée est grande. Comme on peut onduler "infiniment vite", la dérivée peut être "infiniment grande".
    - La **Résolvante**, c'est comme une pédale de frein ou un stabilisateur : c'est un outil qui permet de rendre la machine "calme" et manipulable en lui ajoutant un paramètre de sécurité.
- **Le "Pourquoi on a inventé ça" :** Pour modéliser la physique. L'énergie d'une particule (Hamiltonien) ou la chaleur qui se diffuse sont des processus qui font intervenir des dérivées. En IA, cela permet d'étudier comment un réseau de neurones apprend de manière continue dans le temps.
- **Visualisation :** Un élastique que l'on tend. Pour la plupart des formes, tout va bien. Mais pour certaines formes très pointues, l'élastique casse car la tension (l'opérateur) devient trop forte.

## 2. Formalisation & Rigueur Académique

Soit $H$ un espace de Hilbert.

### A. Définition d'un Opérateur non borné

> **Définition 1 (Opérateur et Domaine) :**
> Un opérateur linéaire $T$ sur $H$ est la donnée d'un sous-espace vectoriel $D(T) \subset H$ (le **domaine**) et d'une application linéaire $T : D(T) \to H$.
> On dit qu'il est **non borné** s'il n'existe pas de constante $C$ telle que $\|Tx\| \le C \|x\|$ pour tout $x \in D(T)$.

> **Définition 2 (Opérateur fermé) :**
> $T$ est dit **fermé** si son graphe est fermé dans $H \times H$. C'est une propriété de "solidité" qui remplace la continuité pour les opérateurs non bornés.

### B. Spectre et Résolvante

Soit $T$ un opérateur fermé de domaine dense.

> **Définition 3 (Ensemble résolvant) :**
> L'ensemble résolvant $\rho(T)$ est l'ensemble des $\lambda \in \mathbb{C}$ tels que $(T - \lambda I) : D(T) \to H$ soit une bijection.
> Pour $\lambda \in \rho(T)$, l'opérateur $R_\lambda(T) = (T - \lambda I)^{-1}$ est appelé **résolvante** de $T$. Il est **automatiquement continu** (Jalon 101).

> **Définition 4 (Spectre) :**
> Le spectre est le complémentaire $\sigma(T) = \mathbb{C} \setminus \rho(T)$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Exemple fondamental : L'opérateur de dérivation

Soit $H = L^2([0, 1])$ and $T = \frac{d}{dx}$ avec $D(T) = \{ f \in H^1([0, 1]) \mid f(0) = 0 \}$.

1. **Montrons que T est non borné :**
   Considérons $f_n(x) = x^n$. $\|f_n\|_2^2 = \int x^{2n} = \frac{1}{2n+1} \approx \frac{1}{\sqrt{2n}}$.
   $Tf_n(x) = n x^{n-1}$. $\|Tf_n\|_2^2 = \int n^2 x^{2n-2} = \frac{n^2}{2n-1} \approx \frac{n}{2}$.
   Le rapport $\frac{\|Tf_n\|}{\|f_n\|} \approx \frac{\sqrt{n}/ \sqrt{2}}{1 / \sqrt{2n}} = n \to \infty$.
   Donc $T$ est non borné.
2. **Calcul de la résolvante :** On cherche $f \in D(T)$ tel que $(T - \lambda I)f = g$ pour $g \in H$ fixé.
   $f' - \lambda f = g$.
   C'est une EDO du premier ordre (Jalon 41). Comme $f(0)=0$, la solution unique est :
   $f(x) = \int_0^x e^{\lambda(x-s)} g(s) ds$.
3. **Conclusion :** L'opérateur $R_\lambda(g) = \int_0^x e^{\lambda(x-s)} g(s) ds$ est un opérateur intégral. On montre qu'il est continu pour tout $\lambda$. Donc $\rho(T) = \mathbb{C}$ et le spectre est vide (dans ce cas précis avec cette condition au bord).

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Opérateur de multiplication
**Énoncé :** Sur $L^2(\mathbb{R})$, soit $Tf(x) = x f(x)$. Quel est son domaine ? Est-il borné ?
**Correction Détaillée :**
1. **Domaine :** Pour que $Tf \in L^2$, il faut $\int |x f(x)|^2 dx < \infty$. Le domaine est $D(T) = \{ f \in L^2 \mid x f \in L^2 \}$.
2. **Bornitude :** En prenant $f_n = \mathbf{1}_{[n, n+1]}$, on a $\|f_n\|=1$ and $\|Tf_n\| \ge n$. Le rapport tend vers l'infini. $T$ est non borné.
3. **Spectre :** $\sigma(T) = \mathbb{R}$.

### Exercice 2 : Niveau Avancé (Adjoint d'un non borné)
**Énoncé :** Comment définir $T^*$ si $T$ n'est pas continu ?
**Correction Détaillée :**
On dit que $y \in D(T^*)$ s'il existe $z \in H$ tel que $\forall x \in D(T), \langle Tx, y \rangle = \langle x, z \rangle$. On pose alors $T^*y = z$. C'est beaucoup plus restrictif que pour les opérateurs bornés (Jalon 105).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on étudie le **Gradient Flow** : la trajectoire des poids d'un réseau pendant l'entraînement. Dans la limite où la couche est infinie, le gradient devient un opérateur non borné sur un espace de Hilbert.
- **Example Concret :**
    - **Diffusion Models :** L'équation de diffusion (Fokker-Planck) fait intervenir le Laplacien, qui est un opérateur non borné. Pour simuler la génération d'images, on doit inverser cet opérateur ou calculer sa résolvante (méthodes implicites).
    - **Smoothing et Régularisation :** Appliquer un flou Gaussien à une image revient à appliquer l'opérateur $e^{t\Delta}$. Pour "dé-flouter" (deconvolution), on doit inverser cet opérateur, ce qui est très instable car son inverse est "très" non borné (il amplifie le bruit infiniment).
    - **Kernel Methods (RKHS) :** Les fonctions de l'espace de Hilbert peuvent être très régulières, mais les opérateurs de dérivation dessus sont souvent non bornés. Cela impose d'utiliser des noyaux très lisses (comme le noyau RBF) pour pouvoir calculer des dérivées de manière stable.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]], [[Jalon 41 (Équations différentielles linéaires du premier ordre et méthode de variation de la constante.).md]]
- **Concepts Futurs dépendants :** [[Jalon 115 (Démonstration du théorème de Stokes généralisé).md]], [[Jalon 128 (Flots de gradient).md]]
