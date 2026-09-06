---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]"
next: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## Présentation du concept clé

Le théorème de convergence monotone, également connu sous le nom de théorème de Beppo Levi, constitue l'un des piliers fondamentaux de la théorie de l'intégration de Lebesgue. Son objet principal est de fournir des conditions suffisantes et extrêmement souples pour permettre l'interversion d'une limite et d'une intégrale. Contrairement à la théorie de Riemann qui exige souvent une convergence uniforme sur des compacts, la théorie de Lebesgue s'accommode de la simple convergence ponctuelle, pourvu que la suite de fonctions présente une propriété de monotonicité.

Ce résultat stipule que la limite de l'intégrale d'une suite croissante de fonctions positives est exactement égale à l'intégrale de sa limite ponctuelle. Cette souplesse opératoire est essentielle dans de multiples domaines des mathématiques analytiques et des probabilités, garantissant la cohérence des sommations infinies (séries de fonctions) et des passages à la limite au sein d'espaces fonctionnels de dimension infinie.


## Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Énoncé du Théorème

\begin{center}
\begin{tikzpicture}[scale=1.2]
  \draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,4) node[above] {$f(x)$};

  \draw[thick, blue, dashed] (0,0) to[out=20,in=180] (2,2.5) to[out=0,in=180] (4.5,3.5) node[right] {$f(x) = \lim f_n(x)$};

  \draw[thick, red!40] (0,0) to[out=10,in=180] (2,1) to[out=0,in=180] (4.5,1.5) node[right] {$f_1(x)$};
  \draw[thick, red!60] (0,0) to[out=15,in=180] (2,1.8) to[out=0,in=180] (4.5,2.5) node[right] {$f_2(x)$};
  \draw[thick, red!80] (0,0) to[out=18,in=180] (2,2.2) to[out=0,in=180] (4.5,3.1) node[right] {$f_3(x)$};

  \node at (2.5, -0.5) {Convergence d'une suite croissante de fonctions};
\end{tikzpicture}
\end{center}


> **Théorème de Convergence Monotone (Beppo Levi) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$.
> Si la suite est **croissante** presque partout :
> $$\forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \text{ p.p.}$$
> Alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable et :
> $$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \lim_{n \to \infty} \int_X f_n d\mu$$

### Corollaire (Sommation terme à terme)

> **Théorème :** Pour toute suite de fonctions mesurables **positives** $(u_n)$ :
> $$\int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \int_X u_n d\mu$$


### Exemples d'application du Théorème de Convergence Monotone

Pour bien saisir la portée du théorème, étudions plusieurs exemples fondamentaux et cas limites.

\textbf{Exemple 1 : Intégrale de Gauss (passage à la limite)}
Considérons la suite de fonctions $f_n(x) = \left(1 - \frac{x^2}{n}\right)^n \mathbf{1}_{[0,\sqrt{n}]}(x)$.
On montre que $(f_n)$ est une suite croissante de fonctions mesurables positives convergeant simplement vers $f(x) = e^{-x^2}$.
Par le théorème de convergence monotone :
$$ \int_0^\infty e^{-x^2} dx = \lim_{n \to \infty} \int_0^{\sqrt{n}} \left(1 - \frac{x^2}{n}\right)^n dx $$
Le calcul de l'intégrale de droite (via les intégrales de Wallis) donne directement la valeur $\frac{\sqrt{\pi}}{2}$.

\textbf{Exemple 2 : Fonctions en escalier}
Soit $X = \mathbb{R}$ muni de la mesure de Lebesgue.
Posons $f_n = \mathbf{1}_{[0, 1 - \frac{1}{n}]}$.
Clairement $f_n \ge 0$ et $f_n \le f_{n+1}$.
La limite simple est $f = \mathbf{1}_{[0, 1[}$.
L'intégrale de $f_n$ est $1 - \frac{1}{n}$, qui converge vers $1$.
L'intégrale de $f$ est la mesure de $[0, 1[$, qui vaut $1$. On vérifie bien l'égalité.

\textbf{Exemple 3 : Échappement de masse (contre-exemple si on supprime la croissance)}
Soit $g_n = n \mathbf{1}_{]0, \frac{1}{n}]}$.
Pour tout $x > 0$, $g_n(x) = 0$ pour $n$ assez grand. Donc $\lim g_n = 0$.
L'intégrale de la limite est $0$.
Pourtant, $\int g_n = n \times \frac{1}{n} = 1$. La limite des intégrales est $1 \neq 0$.
Pourquoi Beppo Levi ne s'applique-t-il pas ? Parce que la suite $(g_n)$ n'est \textbf{pas croissante}.

\textbf{Exemple 4 : Série harmonique et mesure de comptage}
Soit $X = \mathbb{N}$ muni de la mesure de comptage. Une fonction positive $f : \mathbb{N} \to \mathbb{R}^+$ n'est rien d'autre qu'une suite $(u_k)_{k \ge 0}$ de réels positifs.
Soit $u_k = \frac{1}{k+1}$ pour $k \ge 0$.
L'intégrale $\int_X u \, d\mu$ correspond à la série $\sum_{k=0}^\infty \frac{1}{k+1} = +\infty$.
Le corollaire de Beppo Levi garantit que la somme infinie (intégrale de Lebesgue) a un sens, même si elle vaut $+\infty$.

\textbf{Exemple 5 : L'escalier du Diable (Fonction de Cantor)}
Bien que plus subtil, la construction de la fonction de Cantor se fait par limite de fonctions continues $f_n$.
En considérant $g_n = f_{n+1} - f_n \ge 0$, on peut utiliser le théorème de convergence monotone pour prouver que la fonction de Cantor est intégrable et calculer son intégrale (qui vaut $1/2$ sur $[0,1]$).

\textbf{Exemple 6 : Croissance vers l'infini}
Soit $f_n(x) = n \mathbf{1}_{[0, 1]}(x)$.
La suite $(f_n)$ est croissante vers la fonction qui vaut $+\infty$ sur $[0, 1]$.
L'intégrale de $f_n$ est $n$, qui tend vers $+\infty$.
L'intégrale de la limite est $\int_{[0, 1]} +\infty \, dx = +\infty \times 1 = +\infty$. L'égalité tient toujours.

\textbf{Exemple 7 : Application en probabilités (Espérance)}
Si $X_n$ est une suite de variables aléatoires réelles positives, alors $\mathbb{E}[X_n] = \int_\Omega X_n d\mathbb{P}$.
Si $X_n \le X_{n+1}$ presque sûrement, alors le TCM garantit que l'espérance de la limite est la limite des espérances : $\mathbb{E}[\lim X_n] = \lim \mathbb{E}[X_n]$.

\textbf{Exemple 8 : Dérivation sous le signe somme}
Dans certains cas limites où l'on souhaite intégrer des séries entières terme à terme près du rayon de convergence, le TCM justifie que l'on puisse permuter l'intégrale et la somme infinie, tant que les termes de la série sont des fonctions positives.


## Démonstrations

### Démonstration du Théorème de Beppo Levi

1. **Existence de la limite :** Comme $(f_n(x))$ est une suite croissante de $[0, +\infty]$, elle admet toujours une limite dans $[0, +\infty]$ pour chaque $x$. On a vu (Jalon 65) que le sup (ou la limite ici) de fonctions mesurables est mesurable.
2. **Inégalité facile ($\ge$) :** Comme $f_n \le f$ pour tout $n$, par croissance de l'intégrale (Jalon 66) :
   $\int f_n \le \int f$. En prenant la limite : $\lim \int f_n \le \int f$.
3. **Inégalité difficile ($\le$) :** Soit $s$ une fonction simple telle que $0 \le s \le f$. Soit $\alpha \in ]0, 1[$.
   On définit $A_n = \{x \in X \mid f_n(x) \ge \alpha s(x) \}$.
   - Comme $f_n$ croît vers $f$ et $\alpha s < f$ (là où $s>0$), la suite d'ensembles $(A_n)$ est croissante et son union est $X$.
   - On a $\int f_n \ge \int_{A_n} f_n \ge \int_{A_n} \alpha s = \alpha \int_{A_n} s$.
   - Par continuité monotone de la mesure (Jalon 63), $\lim \int_{A_n} s = \int_X s$.
   - Donc $\lim \int f_n \ge \alpha \int_X s$.
   - En faisant tendre $\alpha \to 1$, on a $\lim \int f_n \ge \int s$.
4. **Conclusion :** Comme c'est vrai pour tout $s \le f$, alors $\lim \int f_n \ge \sup \int s = \int f$.
   Les deux inégalités prouvent l'égalité.

## Exercices d'Application

### Exercice 1 : Intégrale d'une série
**Énoncé :** Calculer $\int_0^1 \sum_{n=1}^\infty x^n dx$.
**Correction Détaillée :**
1. Les fonctions $u_n(x) = x^n$ sont mesurables et positives sur $[0, 1]$.
2. Par le corollaire du TCM, on peut intervertir somme et intégrale.
3. $I = \sum_{n=1}^\infty \int_0^1 x^n dx = \sum_{n=1}^\infty \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \sum_{n=1}^\infty \frac{1}{n+1}$.
4. Cette série est la série harmonique (moins son premier terme), elle diverge vers $+\infty$.
5. L'intégrale de la somme est donc $+\infty$.

### Exercice 2 : Niveau Avancé (Utilisation de la mesure de comptage)
**Énoncé :** Retrouver le théorème de sommation des séries à termes positifs doubles : $\sum_{i} \sum_{j} a_{i,j} = \sum_{j} \sum_{i} a_{i,j}$.
**Correction Détaillée :**
On considère l'espace $\mathbb{N}$ muni de la mesure de comptage $\mu$. Soit $f_n(i) = \sum_{j=0}^n a_{i,j}$. La suite de fonctions $(f_n)$ est croissante car $a_{i,j} \ge 0$. Par Beppo Levi, l'intégrale de la limite est la limite des intégrales, ce qui correspond exactement à l'interversion des sommes.

## Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on manipule souvent des **Espérances de sommes infinies** ou des limites de processus. Le TCM est l'outil qui permet de passer à la limite sous l'espérance en toute sécurité.
- **Example Concret :**
    - **Processus de Poisson :** Pour calculer le nombre moyen d'événements (ex: clics sur une pub) sur un intervalle de temps, on somme les probabilités d'événements infinitésimaux. Le TCM garantit que la somme de ces moyennes locales donne bien la moyenne globale.
    - **Séries de Taylor de fonctions de perte :** Si on décompose une fonction de coût complexe en une série de fonctions positives, on peut intégrer cette série terme à terme pour obtenir une approximation de la perte attendue.
    - **Théorie des Noyaux (Kernels) :** De nombreux noyaux (comme le noyau RBF) peuvent être vus comme des sommes infinies de caractéristiques. Le TCM permet de manipuler ces représentations de dimension infinie comme si elles étaient finies lors des calculs d'intégrales de risque.

## Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
