---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-66.md]]"
next: "[[Jalon-68.md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Genèse et positionnement conceptuel

La construction de l'intégrale de Riemann, bien qu'intuitive par son approche géométrique (sommes de Darboux), se heurte rapidement à des impasses majeures lorsqu'il s'agit de manipuler des limites. En analyse classique, la question centrale est souvent : sous quelles conditions peut-on permuter les opérateurs de limite et d'intégrale ? C'est-à-dire, quand a-t-on $\lim_{n \to \infty} \int_a^b f_n(x) dx = \int_a^b \left(\lim_{n \to \infty} f_n(x)\right) dx$ ?

Avec Riemann, les conditions requises (comme la convergence uniforme) sont extrêmement restrictives. Henri Lebesgue, au début du XXe siècle, révolutionne cette approche en changeant la façon de mesurer les ensembles. L'intégrale de Lebesgue offre une robustesse inégalée face aux passages à la limite. Le mathématicien italien Beppo Levi (1906) formalise un résultat fondateur de cette nouvelle théorie : pour une suite de fonctions mesurables positives qui ne font que croître, la permutation limite-intégrale est toujours valide, même si la limite vaut l'infini.

Cette propriété fondamentale élimine le besoin de convergence uniforme et devient la pierre angulaire sur laquelle reposent presque tous les théorèmes d'intégration avancés (comme le Lemme de Fatou et le Théorème de Convergence Dominée).

## 2. Énoncé fondamental et exemples d'application

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.

### Théorème de Convergence Monotone (Beppo Levi)

> **Théorème :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ dans $\overline{\mathbb{R}}_+$ mesurables.
> Si la suite $(f_n)$ est **croissante presque partout** sur $X$, c'est-à-dire :
> $$\mu(\{x \in X \mid \exists n \in \mathbb{N}, f_n(x) > f_{n+1}(x)\}) = 0$$
> Alors la fonction limite $f = \lim_{n \to \infty} f_n$ (qui existe dans $\overline{\mathbb{R}}_+$ et est mesurable) vérifie :
> $$\int_X f(x) d\mu(x) = \lim_{n \to \infty} \int_X f_n(x) d\mu(x)$$

*Remarque typologique :* Les fonctions $f_n$ et $f$ prennent leurs valeurs dans $\overline{\mathbb{R}}_+ = [0, +\infty]$. L'intégrale peut tout à fait valoir $+\infty$, l'égalité reste vraie au sens étendu. L'hypothèse de positivité est absolument cruciale (sans elle, on pourrait avoir une forme indéterminée ou un défaut d'intégrabilité).

### Corollaire d'intégration terme à terme

Une conséquence immédiate, très utilisée en pratique, concerne les séries de fonctions positives.

> **Corollaire :**
> Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ dans $\overline{\mathbb{R}}_+$ mesurables. Alors :
> $$\int_X \left( \sum_{n=0}^{+\infty} u_n(x) \right) d\mu(x) = \sum_{n=0}^{+\infty} \int_X u_n(x) d\mu(x)$$

### Exemples concrets immédiats

**Exemple 1 : Intégration sur une union croissante de domaines**
Considérons l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$. Soit $f(x) = \frac{1}{\sqrt{x}} \mathbf{1}_{]0, 1]}(x)$. $f$ est mesurable et positive.
Définissons une suite d'ensembles $A_n = [\frac{1}{n}, 1]$ pour $n \ge 1$. La suite d'ensembles $(A_n)$ est croissante ($A_n \subset A_{n+1}$) et $\bigcup_{n=1}^\infty A_n = ]0, 1]$.
Posons $f_n(x) = f(x) \mathbf{1}_{A_n}(x)$.
Pour tout $x \in \mathbb{R}$, la suite numérique $(f_n(x))$ est croissante et converge vers $f(x) \mathbf{1}_{]0, 1]}(x) = f(x)$.
D'après le théorème de Beppo Levi :
$$\int_{\mathbb{R}} f d\lambda = \lim_{n \to \infty} \int_{\mathbb{R}} f_n d\lambda = \lim_{n \to \infty} \int_{1/n}^1 x^{-1/2} dx$$
Calculons l'intégrale pour un $n$ fixé :
$$\int_{1/n}^1 x^{-1/2} dx = \left[ 2x^{1/2} \right]_{1/n}^1 = 2 - \frac{2}{\sqrt{n}}$$
En passant à la limite quand $n \to \infty$, on obtient $\int_{\mathbb{R}} f d\lambda = 2$.
L'intégrale de Lebesgue retrouve ici (et justifie proprement) la notion d'intégrale impropre de Riemann.

**Exemple 2 : Calcul avec des séries (Application du corollaire)**
Calculons $\int_0^1 \frac{\ln(x)}{1-x} dx$.
La fonction $x \mapsto \frac{-\ln(x)}{1-x}$ est mesurable et positive sur $]0, 1[$.
On peut développer $\frac{1}{1-x}$ en série entière sur $]0, 1[$ : $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
Ainsi, $\frac{-\ln(x)}{1-x} = \sum_{n=0}^\infty (-x^n \ln(x))$.
Posons $u_n(x) = -x^n \ln(x)$. Chaque $u_n$ est positive sur $]0, 1]$. Par le corollaire du théorème de Beppo Levi :
$$\int_0^1 \left( \sum_{n=0}^\infty -x^n \ln(x) \right) dx = \sum_{n=0}^\infty \int_0^1 -x^n \ln(x) dx$$
On calcule l'intégrale $\int_0^1 -x^n \ln(x) dx$ par parties (en posant $u=-\ln x$, $v' = x^n$ $\implies u' = -1/x, v = x^{n+1}/(n+1)$) :
$$\int_0^1 -x^n \ln(x) dx = \left[ \frac{-x^{n+1}\ln x}{n+1} \right]_0^1 + \int_0^1 \frac{x^n}{n+1} dx = 0 + \left[ \frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2}$$
On obtient donc :
$$\int_0^1 \frac{-\ln(x)}{1-x} dx = \sum_{n=0}^\infty \frac{1}{(n+1)^2} = \sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$$

### Contre-exemple : La nécessité de l'hypothèse de croissance
Considérons l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.
Soit $f_n(x) = n \mathbf{1}_{]0, 1/n]}(x)$.
Pour tout $x \in \mathbb{R}$, on a $\lim_{n \to \infty} f_n(x) = 0$. Donc la fonction limite $f$ est nulle partout.
Calculons les intégrales :
$\int_\mathbb{R} f d\lambda = \int_\mathbb{R} 0 d\lambda = 0$
Pour tout $n \ge 1$, $\int_\mathbb{R} f_n d\lambda = n \lambda(]0, 1/n]) = n \times \frac{1}{n} = 1$.
On a donc $\lim_{n \to \infty} \int_\mathbb{R} f_n d\lambda = 1 \neq 0 = \int_\mathbb{R} \left( \lim_{n \to \infty} f_n \right) d\lambda$.
Pourquoi le théorème s'effondre-t-il ici ? Parce que la suite $(f_n)$ **n'est pas croissante**. En effet, $f_1(x) = 1$ sur $]0, 1]$ tandis que $f_2(x) = 2$ sur $]0, 1/2]$ mais vaut $0$ sur $]1/2, 1]$. Donc sur l'intervalle $]1/2, 1]$, on a $f_2(x) < f_1(x)$.

```latex
\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Axes
    \draw[->] (-0.5, 0) -- (3, 0) node[right] {$x$};
    \draw[->] (0, -0.2) -- (0, 3) node[above] {$y$};

    % f1
    \draw[blue, thick] (0, 1) -- (2, 1);
    \draw[blue, thick, dashed] (2, 1) -- (2, 0);
    \node[blue] at (1, 1.2) {$f_1$};

    % f2
    \draw[red, thick] (0, 2) -- (1, 2);
    \draw[red, thick, dashed] (1, 2) -- (1, 0);
    \node[red] at (0.5, 2.2) {$f_2$};

    % Labels
    \node[below] at (2, 0) {$1$};
    \node[below] at (1, 0) {$1/2$};
    \node[left] at (0, 1) {$1$};
    \node[left] at (0, 2) {$2$};
\end{tikzpicture}
\end{center}
```
*Le contre-exemple classique : la masse (l'intégrale) "fuit" vers l'origine (ou vers l'infini) parce que la masse se concentre sur un support de mesure tendant vers zéro tout en gardant une intégrale constante.*

## 3. Démonstration détaillée ligne par ligne

**Hypothèses :** $(f_n)$ est une suite de fonctions mesurables positives telles que $0 \le f_n(x) \le f_{n+1}(x)$ pour presque tout $x \in X$. $f(x) = \lim_{n \to \infty} f_n(x) = \sup_{n} f_n(x)$. (On peut supposer la croissance vraie partout quite à redéfinir les fonctions sur un ensemble de mesure nulle).

**Objectif :** Montrer que $\int f d\mu = \lim \int f_n d\mu$.

**Étape 1 : Une inégalité triviale par croissance**
Pour tout $x \in X$ et tout $n \in \mathbb{N}$, on a $f_n(x) \le f(x)$ puisque la suite est croissante.
L'intégrale (comme définie au Jalon 66 via le sup sur les fonctions étagées) conserve l'ordre.
Donc, pour tout $n$, on a :
$$\int_X f_n d\mu \le \int_X f d\mu$$
La suite numérique $u_n = \int_X f_n d\mu$ est une suite croissante (car $f_n \le f_{n+1}$) dans $\overline{\mathbb{R}}_+$. Elle admet donc une limite. Par passage à la limite dans l'inégalité précédente, on obtient :
$$\lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu \quad \text{ (Inégalité 1)}$$

**Étape 2 : L'inégalité fine inverse via les fonctions étagées**
Pour obtenir l'inégalité dans l'autre sens, nous devons revenir à la définition fondamentale de l'intégrale d'une fonction mesurable positive $f$, qui est le supremum des intégrales des fonctions étagées positives $s$ telles que $s \le f$.
Soit $s = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$ une fonction étagée mesurable telle que $0 \le s \le f$.
Introduisons une constante $c \in ]0, 1[$.
Pour chaque entier $n \ge 0$, on définit l'ensemble $E_n$ par :
$$E_n = \{x \in X \mid f_n(x) \ge c \cdot s(x)\}$$
Analysons ces ensembles $E_n$ :
1.  **Mesurabilité :** $E_n$ est mesurable car c'est l'image réciproque d'un borélien par la fonction mesurable $f_n - cs$.
2.  **Croissance :** Puisque la suite $(f_n)$ est croissante ($f_n(x) \le f_{n+1}(x)$), si $x \in E_n$ alors $f_{n+1}(x) \ge f_n(x) \ge c \cdot s(x)$, donc $x \in E_{n+1}$. Ainsi $E_n \subset E_{n+1}$. La suite d'ensembles $(E_n)$ est croissante.
3.  **Union recouvrant $X$ :** Montrons que $\bigcup_{n=0}^\infty E_n = X$. Soit $x \in X$.
    - Si $f(x) = 0$, alors $s(x) = 0$ (car $0 \le s \le f$). Donc $c \cdot s(x) = 0$. Comme $f_n(x) \ge 0$, on a $f_n(x) \ge c \cdot s(x)$ pour tout $n$, et $x \in E_0 \subset \bigcup E_n$.
    - Si $f(x) > 0$, comme $f(x) \ge s(x)$ et $0 < c < 1$, on a strictement $f(x) > c \cdot s(x)$. Puisque $f_n(x)$ tend vers $f(x)$ (qui peut être $+\infty$), il existe un rang $N$ à partir duquel $f_N(x) > c \cdot s(x)$. Donc $x \in E_N \subset \bigcup E_n$.
    L'union de ces ensembles croissants est bien l'espace $X$ tout entier.

Maintenant, minorons l'intégrale de $f_n$. Sur l'ensemble $E_n$, on a par définition $f_n \ge cs$.
Donc, par positivité, on peut minorer l'intégrale globale par l'intégrale sur la sous-partie $E_n$ :
$$\int_X f_n d\mu \ge \int_{E_n} f_n d\mu \ge \int_{E_n} c \cdot s d\mu = c \int_{E_n} s d\mu$$
Rappelons que $s = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$. L'intégrale de $s$ sur $E_n$ s'écrit :
$$\int_{E_n} s d\mu = \sum_{i=1}^k a_i \mu(A_i \cap E_n)$$
Par continuité monotone de la mesure $\mu$ (Jalon 63), puisque la suite d'ensembles $A_i \cap E_n$ est croissante de limite $A_i \cap X = A_i$, on a $\lim_{n \to \infty} \mu(A_i \cap E_n) = \mu(A_i)$.
En passant à la limite quand $n \to \infty$ dans notre minoration :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \lim_{n \to \infty} c \sum_{i=1}^k a_i \mu(A_i \cap E_n) = c \sum_{i=1}^k a_i \mu(A_i) = c \int_X s d\mu$$
Cette inégalité $\lim_{n} \int f_n d\mu \ge c \int s d\mu$ est vraie pour tout $c \in ]0, 1[$.
En faisant tendre $c \to 1$, on obtient :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu$$
Enfin, cette dernière inégalité est vraie pour *toute* fonction étagée $s$ telle que $0 \le s \le f$.
En passant au supremum sur toutes ces fonctions étagées $s$, par définition de l'intégrale de $f$ :
$$\lim_{n \to \infty} \int_X f_n d\mu \ge \sup_{s \le f} \int_X s d\mu = \int_X f d\mu \quad \text{ (Inégalité 2)}$$

**Conclusion :**
En combinant (Inégalité 1) et (Inégalité 2), on obtient bien $\int_X f d\mu = \lim_{n \to \infty} \int_X f_n d\mu$. $\blacksquare$

## 4. Applications en Théorie des Probabilités et Modélisation Numérique

Le théorème de convergence monotone est l'outil privilégié dès que l'on manipule des sommes infinies d'entités positives en analyse stochastique ou en Machine Learning.

### 4.1. Espérance et variables aléatoires discrètes infinies
En théorie des probabilités, l'espérance d'une variable aléatoire $X \ge 0$ est définie par l'intégrale de Lebesgue $\mathbb{E}[X] = \int_\Omega X(\omega) dP(\omega)$.
Si $X$ prend ses valeurs dans $\mathbb{N}$ (par exemple, une distribution de Poisson modélisant un nombre d'arrivées), on peut écrire $X = \sum_{k=1}^\infty \mathbf{1}_{\{X \ge k\}}$.
Le corollaire du théorème de Beppo Levi garantit que l'on peut intervertir la somme infinie et l'intégrale :
$$\mathbb{E}[X] = \int_\Omega \left( \sum_{k=1}^\infty \mathbf{1}_{\{X \ge k\}} \right) dP = \sum_{k=1}^\infty \int_\Omega \mathbf{1}_{\{X \ge k\}} dP = \sum_{k=1}^\infty P(X \ge k)$$
C'est une formule extrêmement élégante et pratique pour calculer l'espérance d'une variable entière à partir des queues de distribution, sans avoir à calculer $\sum k P(X=k)$.

### 4.2. Analyse de la convergence des algorithmes itératifs (IA)
Dans de nombreux algorithmes d'optimisation (comme l'Expectation-Maximization - EM, ou certaines variantes de descente de gradient avec accumulation d'informations), on construit une suite de densités de probabilités ou de fonctions d'information de Fisher.
Si l'algorithme génère une suite de fonctions objectif $(L_n(\theta))$ qui augmentent de manière monotone (par construction, l'algorithme garantit une amélioration locale à chaque pas) vers une limite $L(\theta)$, le théorème de convergence monotone permet de garantir que le comportement global (l'intégrale de cette perte sur l'espace des paramètres, ou son espérance) converge bien vers l'espérance de la perte limite. Cela assure la robustesse mathématique des méthodes de Monte-Carlo appliquées à des problèmes de maximisation d'espérance infinie.
