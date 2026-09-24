---
uuid: "jalon-77"
title: "Densité dans Lp"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]"
next: "[[Jalon 78 (Séries de Fourier).md]]"
---

# Jalon 77 : Densité dans $L^p$

## 1. Introduction à la Densité dans $L^p$

Le concept de densité est fondamental en analyse fonctionnelle. Historiquement, l'étude des espaces de Lebesgue $L^p$ pour $1 \le p < \infty$ s'est heurtée à la complexité structurelle des fonctions qui les composent. Ces fonctions peuvent présenter des discontinuités denses, des variations infinies ou des comportements locaux pathologiques.

La notion de densité offre une solution élégante : elle permet d'approcher arbitrairement près (au sens de la norme $L^p$) n'importe quelle fonction complexe de l'espace par des fonctions appartenant à une classe beaucoup plus "régulière" et maniable, telles que les fonctions étagées (ou simples), les fonctions continues, ou encore les fonctions indéfiniment dérivables à support compact.

En termes géométriques, dire qu'un sous-espace $A$ est dense dans un espace $E$ signifie que l'adhérence de $A$ est égale à $E$. Ainsi, tout point de $E$ est limite d'une suite d'éléments de $A$.

### Exemple 1 : Intuition de l'approximation par des fonctions en escalier
Considérons une fonction continue $f(x) = x^2$ sur l'intervalle $[0,1]$.
Si l'on cherche à l'approcher par une fonction étagée $s_n(x)$ constante sur les intervalles $[k/n, (k+1)/n[$ en prenant la valeur $(k/n)^2$, l'erreur maximale entre $f(x)$ et $s_n(x)$ sur cet intervalle est :
$$ \sup_{x} |f(x) - s_n(x)| \le \frac{2}{n} $$
Ainsi, la distance en norme $L^1$ est majorée par $2/n$, qui tend vers $0$ lorsque $n \to \infty$.

## 2. Définitions, Théorèmes et Exemples

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $1 \le p < \infty$. L'espace $L^p(\mu)$ est l'ensemble des classes d'équivalence de fonctions mesurables $f : X \to \mathbb{R}$ ou $\mathbb{C}$ telles que $\int_X |f|^p \, d\mu < \infty$.

### 2.1 Densité des fonctions simples (étagées)

**Définition (Fonction simple) :**
Une fonction simple (ou étagée) $s$ est une combinaison linéaire finie de fonctions indicatrices d'ensembles mesurables :
$$ s(x) = \sum_{i=1}^k c_i \mathbf{1}_{A_i}(x) $$
où $c_i \in \mathbb{R}$ (ou $\mathbb{C}$) et les $A_i \in \mathcal{F}$ sont deux à deux disjoints.

**Théorème 1 (Densité des fonctions simples dans $L^p$) :**
Pour tout $1 \le p < \infty$, l'espace vectoriel des fonctions simples intégrables est dense dans $L^p(\mu)$.
Autrement dit, pour tout $f \in L^p(\mu)$ et tout $\epsilon > 0$, il existe une fonction simple $s \in L^p(\mu)$ telle que :
$$ \| f - s \|_p < \epsilon $$

**Exemple 2 : Calcul de l'approximation d'une fonction continue par une fonction simple**
Considérons $f(x) = x$ sur $[0,1]$ muni de la mesure de Lebesgue.
Définissons la fonction simple $s(x) = \frac{1}{2} \mathbf{1}_{[0, 1/2[}(x) + 1 \cdot \mathbf{1}_{[1/2, 1]}(x)$.
Calculons la norme $L^2$ de l'erreur :
$$ \| f - s \|_2^2 = \int_0^{1/2} (x - 1/2)^2 \, dx + \int_{1/2}^1 (x - 1)^2 \, dx $$
$$ \int_0^{1/2} (x - 1/2)^2 \, dx = \left[ \frac{(x-1/2)^3}{3} \right]_0^{1/2} = 0 - \left(\frac{-1/8}{3}\right) = \frac{1}{24} $$
$$ \int_{1/2}^1 (x - 1)^2 \, dx = \left[ \frac{(x-1)^3}{3} \right]_{1/2}^1 = 0 - \left(\frac{-1/8}{3}\right) = \frac{1}{24} $$
Ainsi, $\| f - s \|_2^2 = \frac{1}{12}$, ce qui donne $\| f - s \|_2 = \frac{1}{\sqrt{12}} \approx 0.288$.

### 2.2 Densité des fonctions continues à support compact

Soit $\Omega$ un ouvert de $\mathbb{R}^n$ muni de la mesure de Lebesgue. On note $C_c(\Omega)$ l'espace vectoriel des fonctions continues sur $\Omega$ à support compact contenu dans $\Omega$.

**Théorème 2 (Densité de $C_c$ dans $L^p$) :**
Pour tout $1 \le p < \infty$, l'espace $C_c(\Omega)$ est dense dans $L^p(\Omega)$.

**Exemple 3 : Approximation d'une indicatrice par des fonctions continues**
Soit $f = \mathbf{1}_{[0,1]} \in L^1(\mathbb{R})$.
Définissons une suite de fonctions continues $g_n(x)$ :
$$
g_n(x) = \begin{cases}
0 & \text{si } x \le -1/n \\
nx + 1 & \text{si } -1/n < x < 0 \\
1 & \text{si } 0 \le x \le 1 \\
-nx + n + 1 & \text{si } 1 < x < 1+1/n \\
0 & \text{si } x \ge 1+1/n
\end{cases}
$$
L'intégrale de la différence $|f - g_n|$ est géométriquement la somme des aires de deux petits triangles de base $1/n$ et de hauteur $1$.
$$ \| f - g_n \|_1 = 2 \times \left( \frac{1}{2} \times \frac{1}{n} \times 1 \right) = \frac{1}{n} $$
Ainsi, quand $n \to \infty$, $\| f - g_n \|_1 \to 0$.

### 2.3 Densité des fonctions régulières

On note $C_c^\infty(\Omega)$ l'espace des fonctions de classe $C^\infty$ à support compact (aussi appelées fonctions tests).

**Théorème 3 (Densité de $C_c^\infty$ dans $L^p$) :**
Pour tout $1 \le p < \infty$, l'espace $C_c^\infty(\Omega)$ est dense dans $L^p(\Omega)$.

**Exemple 4 : Construction d'une fonction plateau régulière**
On considère la fonction de base $\varphi(x) = e^{-\frac{1}{1-x^2}} \mathbf{1}_{]-1,1[}(x)$, qui est $C^\infty$ à support compact $[-1, 1]$.
Par changement d'échelle et translation, on peut construire une fonction $\psi \in C_c^\infty$ valant $1$ sur un compact $K$ et s'annulant hors d'un voisinage $U$ de $K$. On l'utilise ensuite pour lisser les fonctions indicatrices par convolution.

## 3. Démonstrations

### 3.1 Démonstration du Théorème 1 (Densité des fonctions simples)

Soit $f \in L^p(\mu)$ pour $1 \le p < \infty$.
Écrivons $f = f^+ - f^-$, où $f^+ = \max(f, 0)$ et $f^- = \max(-f, 0)$. Il suffit de démontrer le résultat pour les fonctions positives, puis d'appliquer la linéarité.
Supposons donc $f \ge 0$ et $f \in L^p(\mu)$.

Il existe une suite $(s_n)$ de fonctions simples mesurables, positives et croissantes telle que pour tout $x \in X$, $\lim_{n \to \infty} s_n(x) = f(x)$.
Puisque $0 \le s_n(x) \le f(x)$, nous avons $s_n \in L^p(\mu)$ (car $s_n^p \le f^p$ et $f \in L^p$).
Considérons la suite de fonctions $g_n = |f - s_n|^p = (f - s_n)^p$.
1. $g_n(x) \to 0$ pour presque tout $x$.
2. $|g_n(x)| \le f(x)^p$ pour tout $n$, et $f^p \in L^1(\mu)$.
Par le Théorème de Convergence Dominée de Lebesgue, nous déduisons que :
$$ \lim_{n \to \infty} \int_X |f - s_n|^p \, d\mu = \lim_{n \to \infty} \int_X g_n \, d\mu = 0 $$
Ainsi, $s_n \to f$ dans $L^p(\mu)$. Le théorème est démontré.

### 3.2 Idée de la démonstration pour la densité de $C_c(\Omega)$ (Théorème 2)

D'après le théorème 1, il suffit de montrer que toute fonction simple intégrable peut être approchée par une fonction de $C_c(\Omega)$. Par linéarité, il suffit de l'établir pour l'indicatrice $\mathbf{1}_A$ d'un ensemble mesurable $A$ de mesure finie.
En utilisant la régularité de la mesure de Lebesgue, pour tout $\epsilon > 0$, il existe un compact $K$ et un ouvert $U$ tels que $K \subset A \subset U$ et $\mu(U \setminus K) < \epsilon$.
Par le Lemme d'Urysohn, il existe une fonction continue $g \in C_c(\Omega)$ telle que $0 \le g \le 1$, $g|_K = 1$ et $g|_{U^c} = 0$.
On a alors $\mathbf{1}_A - g = 0$ sur $K$ et sur $U^c$. L'erreur est concentrée sur $U \setminus K$, dont la mesure est très petite.
$$ \int_\Omega |\mathbf{1}_A - g|^p \, d\mu \le \mu(U \setminus K) < \epsilon $$
Ceci conclut l'approximation par des fonctions continues.

### 3.3 Illustration vectorielle : Schéma de densité

\begin{tikzpicture}
\draw[->] (-0.5, 0) -- (6, 0) node[right] {$x$};
\draw[->] (0, -0.5) -- (0, 3) node[above] {$y$};
\draw[blue, thick] (0.5, 0) -- (0.5, 2) -- (2.5, 2) -- (2.5, 0.5) -- (4, 0.5) -- (4, 0);
\draw[red, dashed, thick] (0, 0) -- (0.5, 2) -- (2.5, 2) -- (2.7, 0.5) -- (4, 0.5) -- (4.5, 0);
\node[blue] at (1.5, 2.3) {$f$ (fonction simple)};
\node[red] at (3.5, 1) {$g$ (fonction continue)};
\end{tikzpicture}

## 4. Applications en Physique, Logique et IA

### 4.1 Physique et mécanique quantique
En mécanique quantique, l'espace d'états d'une particule est un espace de Hilbert $L^2(\mathbb{R}^d)$. La densité des fonctions régulières ($C_c^\infty$) permet d'affirmer que des observables comme l'opérateur impulsion $-i\hbar\nabla$ peuvent être définies sur un domaine dense (les fonctions tests). Ainsi, l'opérateur est densément défini, ce qui est une condition sine qua non pour étudier ses propriétés d'auto-adjonction.

### 4.2 Analyse des signaux
En traitement du signal, un signal physique appartient à $L^2$. Les théorèmes de densité assurent qu'on peut approcher ce signal avec une précision infinie par des sommes finies d'harmoniques (séries de Fourier) ou par des ondelettes lisses, ce qui est le fondement de la compression de données (MP3, JPEG).

### 4.3 Intelligence Artificielle et Réseaux de Neurones
Le Théorème d'Approximation Universelle repose fondamentalement sur la densité. Un réseau de neurones multicouches avec une fonction d'activation non polynomiale génère un sous-espace vectoriel de fonctions. Démontrer l'universalité revient à démontrer que ce sous-espace est dense dans l'espace des fonctions continues $C(K)$, et par extension, dense dans $L^p(K)$.
La garantie qu'un réseau de neurones de taille finie peut approcher n'importe quelle fonction d'erreur mesurable $L^p$ à une erreur arbitrairement petite $\epsilon$ provient de ces théorèmes fondamentaux de la théorie de la mesure.
