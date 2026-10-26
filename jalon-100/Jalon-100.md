---
uuid: "jalon-100"
title: "Théorème de Banach-Steinhaus"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/fondations
prev: "[[Jalon 99 (Théorème de Hahn-Banach (forme géométrique)).md]]"
next: "[[Jalon 101 (Théorème de l'application ouverte et théorème du graphe fermé.).md]]"
---



## 2. Formalisation

### A. Énoncé du Théorème

Soit $E$ un espace de **Banach** (complet) et $F$ un espace vectoriel normé quelconque.
Soit $(T_i)_{i \in I}$ une famille d'opérateurs linéaires **continus** de $E$ vers $F$.

> **Théorème de Banach-Steinhaus (Principe de la Borne Uniforme) :**
> On suppose que pour tout $x \in E$, la famille des images est bornée dans $F$ :
> $$\forall x \in E, \quad \sup_{i \in I} \|T_i(x)\|_F < +\infty$$
> Alors, la famille des normes d'opérateurs est bornée :
> $$\sup_{i \in I} \|T_i\|_{\mathcal{L}(E,F)} < +\infty$$


**Exemple Concret 1 : Matrice et Normes en dimension finie**
Considérons l'espace $E = \mathbb{R}^2$ muni de la norme $\| (x, y) \|_\infty = \max(|x|, |y|)$, et $F = \mathbb{R}$.
Soit la famille d'opérateurs linéaires $T_n : \mathbb{R}^2 \to \mathbb{R}$ définie par $T_n(x, y) = n x + y$.
Fixons un vecteur $u = (1, 0)$. Alors $\| T_n(u) \| = n$.
Pour que la famille $T_n(u)$ soit bornée pour tout vecteur $u$, il faudrait que $n$ soit borné.
Ici, si on prend la famille $(T_n)_{n \in \mathbb{N}}$, on voit bien que $\sup_{n} \| T_n(1,0) \| = +\infty$.
La condition du théorème n'est pas remplie, donc la norme d'opérateur n'est pas bornée (ici $\|T_n\| = n+1$).

**Exemple Concret 2 : Intégrales sur $C([0, 1])$**
Soit $E = C([0, 1])$ muni de la norme $\|f\|_\infty = \sup_{t \in [0, 1]} |f(t)|$.
Définissons $T_n : E \to \mathbb{R}$ par $T_n(f) = n \int_0^{1/n} f(t) dt$.
Pour une fonction $f$ donnée, $T_n(f)$ est la moyenne de $f$ sur $[0, 1/n]$.
Puisque $f$ est continue, $T_n(f) \to f(0)$ quand $n \to \infty$.
La suite $(T_n(f))$ est convergente, donc elle est bornée : $\forall f \in E, \sup_n |T_n(f)| < \infty$.
D'après le Théorème de Banach-Steinhaus, la suite des normes $\|T_n\|$ doit être bornée.
Calculons cette norme pas-à-pas :
1) Pour tout $f \in C([0, 1])$, on a $|T_n(f)| \le n \int_0^{1/n} |f(t)| dt \le n \int_0^{1/n} \|f\|_\infty dt = n \cdot \frac{1}{n} \|f\|_\infty = \|f\|_\infty$.
2) On en déduit que $\|T_n\| \le 1$.
3) En prenant la fonction constante $f(t) = 1$ pour tout $t$, $\|f\|_\infty = 1$, et $T_n(f) = n \int_0^{1/n} 1 dt = 1$.
4) Donc $\|T_n\| = 1$.
La borne est bien uniforme, illustrant parfaitement le théorème.


**Exemple Concret 3 : Suite de fonctionnelles sur $L^2$**
Prenons l'espace $E = L^2([0, 1])$ muni de la norme $\|f\|_2 = (\int_0^1 |f(x)|^2 dx)^{1/2}$.
On définit une suite de formes linéaires $T_n(f) = n \int_0^{1/n} f(x) dx$.
Pour toute fonction $f \in L^2$, l'inégalité de Cauchy-Schwarz donne :
$|T_n(f)| \le n (\int_0^{1/n} 1^2 dx)^{1/2} (\int_0^{1/n} |f(x)|^2 dx)^{1/2} = n \frac{1}{\sqrt{n}} \|f\|_{L^2(0, 1/n)} = \sqrt{n} \|f\|_{L^2}$.
Si $f$ est une fonction continue, $T_n(f) \to f(0)$ donc la limite est finie pour ces fonctions. Cependant, il existe des fonctions dans $L^2$ (comme $f(x) = x^{-1/3}$) pour lesquelles $T_n(f)$ diverge.
Ici, $\|T_n\| = \sqrt{n}$, qui n'est pas bornée. Par Banach-Steinhaus, la famille ne peut pas être ponctuellement bornée sur tout $L^2$.

**Exemple Concret 4 : Famille de matrices diagonales**
Prenons $E = \ell^2(\mathbb{N})$ muni de sa norme classique.
Considérons les matrices $T_n$ telles que $T_n x = (x_0, 2x_1, 3x_2, \dots, n x_{n-1}, 0, \dots)$.
La norme de chaque $T_n$ est $n$. La famille de ces opérateurs a des normes non bornées.
Par le théorème de Banach-Steinhaus, on peut affirmer qu'il existe un vecteur $x \in \ell^2$ pour lequel la suite $\|T_n x\|$ n'est pas bornée (par exemple $x_k = \frac{1}{k+1}$ donne $\|T_n x\| \sim \ln n$).

**Exemple Concret 5 : Opérateurs de dérivations discrétisées**
Soit $E = C^1([0, 1])$ muni de la norme $\|f\| = \|f\|_\infty + \|f'\|_\infty$ (qui en fait un espace de Banach) et $F = C([0, 1])$ avec la norme uniforme.
Soit $T_n(f)(t) = \frac{f(t+1/n) - f(t)}{1/n}$ (avec prolongement adapté ou pris sur un intervalle légèrement plus petit).
Pour $f$ donnée, $T_n(f) \to f'$ uniformément, donc la famille est ponctuellement bornée dans $F$.
Banach-Steinhaus affirme alors que les opérateurs $T_n$ sont uniformément bornés en norme, ce qui est cohérent car $\|T_n f\|_\infty \le \|f'\|_\infty \le \|f\|$.

\begin{tikzpicture}[scale=1.5]
\draw[->,thick] (0,0) -- (4,0) node[right] {$E$};
\draw[->,thick] (0,0) -- (0,3) node[above] {$F$};
\draw[domain=0:3.5, smooth, variable=\x, blue, thick] plot ({\x}, {0.5*\x});
\draw[domain=0:3.5, smooth, variable=\x, red, thick] plot ({\x}, {0.7*\x});
\draw[domain=0:3.5, smooth, variable=\x, green!60!black, thick] plot ({\x}, {0.3*\x});
\node at (2, 1.8) {$T_i(x)$};
\draw[dashed] (3,0) node[below] {$x_0$} -- (3,2.5);
\fill (3,1.5) circle (1.5pt) node[right] {$T_1(x_0)$};
\fill (3,2.1) circle (1.5pt) node[right] {$T_2(x_0)$};
\fill (3,0.9) circle (1.5pt) node[right] {$T_3(x_0)$};
\node[align=center] at (2,-0.8) {\textit{Figure 1 : Pour chaque point $x_0$,} \\ \textit{les images $T_i(x_0)$ sont confinées.}};
\draw [decorate,decoration={brace,amplitude=5pt,mirror}] (3.2,0.9) -- (3.2,2.1) node [midway,right=4pt] {Borné};
\end{tikzpicture}

### B. Conséquence : Convergence des opérateurs

Si une suite d'opérateurs continus $(T_n)$ converge ponctuellement vers un opérateur $T$ (i.e. $T_n(x) \to T(x)$ pour tout $x$), alors l'opérateur limite $T$ est lui aussi continu.

## 3. Démonstrations

### Démonstration utilisant le Théorème de Baire

1. **Définition d'ensembles fermés :** Pour chaque $n \in \mathbb{N}$, posons :
   $$X_n = \{ x \in E \mid \forall i \in I, \|T_i(x)\|_F \le n \}$$
2. **Fermeture :** Comme chaque $T_i$ est continu et que la norme l'est aussi, $x \mapsto \|T_i(x)\|$ est continue. $X_n$ est une intersection de fermés, c'est donc un **fermé**.
3. **Recouvrement :** Par hypothèse de bornitude ponctuelle, pour tout $x$, il existe un $n$ tel que $x \in X_n$.
   Donc $E = \bigcup_{n \in \mathbb{N}} X_n$.
4. **Utilisation du Théorème de Baire (Jalon 58) :** Comme $E$ est un espace de Banach (complet), il n'est pas "maigre". L'un des fermés $X_N$ doit donc être d'**intérieur non vide**.
5. **Existence d'une boule :** Il existe $x_0 \in E$ et $r > 0$ tels que la boule $B(x_0, r) \subset X_N$.
   Cela signifie que pour tout $h$ tel que $\|h\| \le r$ and tout $i \in I$ :
   $\|T_i(x_0 + h)\| \le N$.
6. **Majoration de la norme :** Par linéarité et inégalité triangulaire :
   $\|T_i(h)\| = \|T_i(x_0+h) - T_i(x_0)\| \le \|T_i(x_0+h)\| + \|T_i(x_0)\| \le N + N = 2N$.
7. **Conclusion :** Pour tout vecteur unitaire $u$ ($\|u\|=1$), en posant $h = r u$, on a :
   $\|T_i(u)\| = \frac{1}{r} \|T_i(h)\| \le \frac{2N}{r}$.
   La borne $\frac{2N}{r}$ est indépendante de $x$ et de $i$. Donc $\sup_I \|T_i\| < \infty$.

## 4. Exercices d'Application

### Exercice 1 : Divergence des séries de Fourier
**Énoncé :** Utiliser Banach-Steinhaus pour montrer qu'il existe des fonctions continues dont la série de Fourier diverge en 0.
**Correction Détaillée :**
1. On considère l'espace $E = \mathcal{C}_{2\pi}$ muni de la norme uniforme.
2. On définit $L_n(f) = S_n(f)(0) = \frac{1}{2\pi} \int f(t) D_n(t) dt$ (noyau de Dirichlet).
3. On montre que $\|L_n\| = \|D_n\|_1 \to \infty$ (en $\ln n$).
4. Par Banach-Steinhaus, s'il n'y avait pas de divergence, les normes seraient bornées.
5. **Conclusion :** Comme les normes explosent, il existe forcément une fonction $f$ pour laquelle la suite $L_n(f)$ n'est pas bornée.

### Exercice 2 : Niveau Avancé (Convergence simple vs uniforme)
**Énoncé :** Soit $T_n \to T$ ponctuellement. La convergence est-elle uniforme sur tout compact ?
**Correction Détaillée :**
Oui. On utilise Banach-Steinhaus pour dire que $\sup \|T_n\| < \infty$, puis on utilise un argument d'équicontinuïté (Jalon 59) pour passer de la convergence ponctuelle à la convergence uniforme sur les parties compactes.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Ce jalon garantit la **Stabilité Numérique** des processus d'apprentissage infinis. Il assure que si un système réagit de manière finie à chaque donnée, il ne possède pas de "faille" cachée qui le ferait exploser.
- **Example Concret :**
    - **Apprentissage par transfert (Transfer Learning) :** On a une famille de modèles $f_\theta$. On veut s'assurer que si chaque modèle est performant sur une tâche donnée, la famille entière reste "sous contrôle" lorsqu'on l'applique à de nouvelles données. Banach-Steinhaus donne les conditions de cette stabilité collective.
    - **Réseaux de neurones de largeur infinie (NTK) :** Dans l'analyse théorique, on regarde la limite d'opérateurs quand le nombre de neurones tend vers l'infini. Le principe de la borne uniforme garantit que l'opérateur limite (le noyau tangentiel) reste continu et bien défini.
    - **Stabilité des ODE Solvers :** En Neural ODEs, on utilise des solveurs itératifs. Ce théorème justifie que si le solveur converge pour chaque condition initiale, alors l'erreur globale du solveur est bornée uniformément.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 97 (Espaces de Banach et Opérateurs Linéaires).md]], [[Jalon 58 (Théorème de Baire).md]]
- **Concepts Futurs dépendants :** [[Jalon 101 (Théorème de l'application ouverte et théorème du graphe fermé.).md]], [[Jalon 102 (Topologies faibles et faibles-).md]]
