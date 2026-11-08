# Exercice 02

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
On considère une suite de variables aléatoires $(X_n)_{n \ge 1}$ telles que pour chaque $n \ge 1$, $X_n$ suit une loi uniforme sur l'intervalle $[0, \frac{1}{n}]$.
Démontrez de manière exhaustive que $X_n$ converge presque sûrement (p.s.) vers $0$.

**Correction :**

Nous devons démontrer que $X_n \xrightarrow{p.s.} 0$, ce qui signifie que l'événement $\{\omega \in \Omega \mid \lim_{n \to \infty} X_n(\omega) = 0\}$ possède une probabilité égale à $1$.
Pour ce faire, nous allons utiliser le fait que la convergence presque sûre est assurée si pour tout $\varepsilon > 0$, la série des probabilités des écarts est convergente (corollaire du lemme de Borel-Cantelli). Cependant, vu la nature très simple de la loi, une approche directe par encadrement est plus élégante et fondamentale.

Rappelons la définition de la loi uniforme : la variable $X_n$ prend ses valeurs exclusivement dans l'intervalle $[0, \frac{1}{n}]$.
Ceci signifie que l'événement $\{ 0 \le X_n \le \frac{1}{n} \}$ est l'événement certain (probabilité $1$).
Formellement, il existe un ensemble $A_n \in \mathcal{F}$ avec $\mathbb{P}(A_n) = 1$ tel que pour tout $\omega \in A_n$, $0 \le X_n(\omega) \le \frac{1}{n}$.

Considérons l'intersection dénombrable de ces ensembles de mesure pleine : $A = \bigcap_{n=1}^\infty A_n$.
D'après les propriétés fondamentales des mesures de probabilité (continuité par intersection décroissante ou simple calcul sur les complémentaires), l'intersection dénombrable d'ensembles de probabilité $1$ est un ensemble de probabilité $1$.
En effet, $\mathbb{P}(A^c) = \mathbb{P}(\bigcup A_n^c) \le \sum \mathbb{P}(A_n^c) = \sum 0 = 0$, d'où $\mathbb{P}(A) = 1$.

Soit $\omega$ une réalisation arbitraire appartenant à cet ensemble $A$ de mesure pleine.
Par définition de $A$, pour tout entier $n \ge 1$, la réalisation $X_n(\omega)$ vérifie l'inégalité stricte :
$$ 0 \le X_n(\omega) \le \frac{1}{n} $$
Nous sommes maintenant face à une simple suite déterministe de nombres réels. Appliquons le théorème des gendarmes (ou théorème d'encadrement) de l'analyse réelle classique :
Puisque $\lim_{n \to \infty} 0 = 0$ et $\lim_{n \to \infty} \frac{1}{n} = 0$, il s'ensuit nécessairement que la suite $(X_n(\omega))_{n \ge 1}$ converge vers $0$.

Ceci étant vrai pour tout $\omega \in A$, et sachant que $\mathbb{P}(A) = 1$, nous avons rigoureusement prouvé que :
$$ \mathbb{P}\left(\left\{ \omega \in \Omega \mathrel{\Big|} \lim_{n \to \infty} X_n(\omega) = 0 \right\}\right) = 1 $$
La suite $(X_n)$ converge bien presque sûrement vers la constante $0$.
