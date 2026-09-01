# Théorème de convergence monotone (Beppo Levi)

## Introduction et genèse

Le théorème de convergence monotone, formulé par Beppo Levi (1906), constitue l'une des pierres angulaires de la théorie de l'intégration de Lebesgue. Face aux limites de l'intégrale de Riemann, qui se révèle incapable de garantir la stabilité de l'intégration par passage à la limite pour des suites de fonctions pourtant simples, l'approche de Lebesgue offre une robustesse remarquable. Le besoin géométrique et physique sous-jacent est fondamental : si un phénomène croît continûment en accumulant des contributions positives, la mesure totale de ces contributions à la limite doit être rigoureusement égale à la limite des mesures successives.

L'impossibilité d'intervertir intégrale et limite avec Riemann provient de sa définition par approximations en "escaliers" uniformes. En mesurant d'abord l'image (Lebesgue) plutôt que l'antécédent (Riemann), le théorème de Beppo Levi montre que pour une suite croissante de fonctions mesurables positives, l'intégrale de la limite est la limite des intégrales, peu importe que la limite soit finie ou non.

\begin{tikzpicture}
  \draw[->] (-1,0) -- (6,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,4) node[above] {$y$};

  \draw[domain=0.5:5, smooth, variable=\x, blue, thick] plot ({\x}, {3 - 2/\x}) node[right] {$f(x)$};

  \draw[domain=0.5:5, smooth, variable=\x, dashed, red] plot ({\x}, {3 - 2/\x - 1}) node[right] {$f_n(x)$};
  \draw[domain=0.5:5, smooth, variable=\x, dashed, red] plot ({\x}, {3 - 2/\x - 0.5}) node[right] {$f_{n+1}(x)$};

  \node[text width=4cm, align=center] at (3, -1) {Convergence monotone\\ $f_n \uparrow f$};
\end{tikzpicture}

## Théorèmes, définitions et exemples immédiats

**Théorème (Convergence monotone de Beppo Levi) :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives de $X$ dans $\overline{\mathbb{R}}_+$.
On suppose que la suite est croissante : pour tout $x \in X$, $f_n(x) \leq f_{n+1}(x)$.
Soit $f : X \to \overline{\mathbb{R}}_+$ la fonction définie par $f(x) = \lim_{n \to +\infty} f_n(x)$ (qui existe dans $\overline{\mathbb{R}}_+$ car la suite est croissante).
Alors $f$ est mesurable positive et :
$$ \int_X f \, d\mu = \lim_{n \to +\infty} \int_X f_n \, d\mu $$

**Analyse chirurgicale des variables :**
- $X$ : l'espace de base (par exemple $\mathbb{R}$).
- $\mathcal{A}$ : la tribu des ensembles mesurables (par exemple la tribu borélienne).
- $\mu$ : une mesure positive (par exemple la mesure de Lebesgue $\lambda$).
- $f_n(x)$ : suite d'applications $\mathcal{A}$-mesurables. La positivité ($f_n \ge 0$) est cruciale pour éviter les formes indéterminées $\infty - \infty$.
- $f(x)$ : limite simple.

**Exemples de validation géométrique et calculatoire :**

1. **Exemple fondamental (Suite géométrique) :**
   Considérons $X = [0, 1[$, avec la mesure de Lebesgue $\lambda$.
   Soit $f_n(x) = \sum_{k=0}^n x^k$.
   La suite $(f_n)$ est croissante ($f_{n+1}(x) = f_n(x) + x^{n+1} \ge f_n(x)$ car $x \ge 0$).
   Limites ponctuelles : $f(x) = \lim f_n(x) = \frac{1}{1-x}$.
   $\int_{[0,1[} f_n(x) dx = \sum_{k=0}^n \int_0^1 x^k dx = \sum_{k=0}^n \frac{1}{k+1}$.
   Par le théorème de convergence monotone :
   $\int_0^1 \frac{1}{1-x} dx = \lim_{n \to \infty} \sum_{k=0}^n \frac{1}{k+1} = +\infty$.

2. **Exemple pathologique (Dirac) :**
   $X = \mathbb{R}$, $\mu = \delta_0$ (mesure de Dirac en 0).
   $f_n(x) = e^{-n x^2}$.
   Ici $f_n(0) = 1$ pour tout $n$.
   Mais attention, la suite n'est *pas* croissante pour $x \neq 0$ car $e^{-n x^2}$ décroît vers 0. Le TCM ne s'applique pas directement (c'est le théorème de convergence dominée qui s'appliquera, cf. Jalon 69).
   Prenons plutôt $g_n(x) = 1 - e^{-nx^2}$.
   $g_n$ est positive, croissante en $n$. Limite $g(x) = 1$ si $x \neq 0$, $g(0) = 0$.
   $\int g_n d\delta_0 = g_n(0) = 0$.
   $\int g d\delta_0 = g(0) = 0$.
   La limite des intégrales (0) égale l'intégrale de la limite (0).

3. **Exemple avec une somme infinie (Corollaire) :**
   Si $u_n \ge 0$ sont mesurables, $\int \sum_{n=0}^\infty u_n d\mu = \sum_{n=0}^\infty \int u_n d\mu$.
   Soit $X = \mathbb{N}$, $\mu$ la mesure de comptage.
   Alors $f_n(k) = u_{n,k} \ge 0$.
   L'inversion somme / intégrale devient l'inversion de deux séries à termes positifs (Théorème de Fubini pour les séries).

4. **Exemple : Indicateurs d'ensembles emboîtés :**
   $A_1 \subset A_2 \subset A_3 \dots$
   $f_n = \mathbb{I}_{A_n}$. $f_n$ est croissante. $f = \mathbb{I}_{\cup A_n}$.
   TCM : $\mu(\cup A_n) = \lim \mu(A_n)$. C'est la continuité croissante de la mesure.

5. **Contre-exemple sans croissance :**
   $f_n(x) = n \mathbb{I}_{]0, 1/n[}$.
   $f_n(x) \to 0$ pour tout $x$.
   $\int f_n(x) dx = 1 \neq 0 = \int f(x) dx$.
   Le TCM ne s'applique pas car $f_n$ n'est pas croissante en $n$.

## Démonstrations rigoureuses pas à pas

**Démonstration du TCM :**
Puisque $f_n \leq f_{n+1} \leq f$, par croissance de l'intégrale, on a $\int f_n d\mu \leq \int f_{n+1} d\mu \leq \int f d\mu$.
La suite $(\int f_n d\mu)$ est donc croissante, elle admet une limite $L \in \overline{\mathbb{R}}_+$ telle que $L \leq \int f d\mu$.
Il reste à prouver l'inégalité inverse : $\int f d\mu \leq L$.

Rappelons que $\int f d\mu = \sup \{ \int s d\mu \mid s \text{ étagée}, 0 \leq s \leq f \}$.
Soit donc $s$ une fonction étagée mesurable telle que $0 \leq s \leq f$.
Soit un réel $c \in ]0, 1[$.
Définissons $A_n = \{ x \in X \mid f_n(x) \geq c s(x) \}$.
Puisque $f_n$ est croissante, la suite d'ensembles $(A_n)$ est croissante : $A_n \subset A_{n+1}$.
Pour tout $x \in X$, si $s(x) = 0$, $x \in A_n$. Si $s(x) > 0$, alors $c s(x) < s(x) \leq f(x)$.
Puisque $f_n(x) \to f(x)$, à partir d'un certain rang, $f_n(x) \geq c s(x)$.
Donc $\cup_n A_n = X$.

On a $f_n \geq f_n \mathbb{I}_{A_n} \geq c s \mathbb{I}_{A_n}$.
Donc $\int f_n d\mu \geq c \int_{A_n} s d\mu$.
Puisque $s$ est étagée, $s = \sum_{i=1}^k \alpha_i \mathbb{I}_{B_i}$.
$\int_{A_n} s d\mu = \sum_{i=1}^k \alpha_i \mu(B_i \cap A_n)$.
Par continuité croissante de la mesure $\mu$, $\lim_{n \to \infty} \mu(B_i \cap A_n) = \mu(B_i \cap X) = \mu(B_i)$.
Ainsi $\lim_{n \to \infty} \int_{A_n} s d\mu = \int s d\mu$.

Passons à la limite dans $\int f_n d\mu \geq c \int_{A_n} s d\mu$ :
$L \geq c \int s d\mu$.
Cette inégalité étant vraie pour tout $c < 1$, on a $L \geq \int s d\mu$.
En prenant le supremum sur toutes les fonctions étagées $s \leq f$, on obtient $L \geq \int f d\mu$.
D'où l'égalité. $\blacksquare$

## Applications physiques et algorithmiques

Dans le domaine des probabilités, l'espérance mathématique est une intégrale de Lebesgue. Le TCM permet de garantir la convergence des espérances pour des suites de variables aléatoires positives croissantes.
En apprentissage profond (Deep Learning), lorsque l'on optimise une fonction de coût (Loss) qui est définie par une série d'erreurs (par exemple la somme des erreurs de reconstruction), si on garantit que chaque terme ajouté apporte une contribution positive, le TCM assure que le coût global limite est bien la somme infinie des coûts individuels.
