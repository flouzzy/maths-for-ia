# Covariance nulle n'implique pas l'indépendance

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Soit $X$ une variable aléatoire suivant une loi Normale centrée réduite, c'est-à-dire $X \sim \mathcal{N}(0,1)$.
On pose une nouvelle variable aléatoire $Y = X^2$.
1. Calculer la covariance entre $X$ et $Y$.
2. Montrer que $X$ et $Y$ ne sont pourtant pas indépendantes.

### Correction

Soit $X \sim \mathcal{N}(0,1)$ et $Y = X^2$.

**1. Calcul de la covariance**
Par définition, la covariance de deux variables est $\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.
- Calculons $\mathbb{E}[X]$ : Puisque $X$ est une loi normale standard centrée, $\mathbb{E}[X] = 0$.
- Déduisons-en la covariance : $\text{Cov}(X,Y) = \mathbb{E}[XY] - 0 \times \mathbb{E}[Y] = \mathbb{E}[XY]$.
- Remplaçons $Y$ par son expression : $\text{Cov}(X,Y) = \mathbb{E}[X \cdot X^2] = \mathbb{E}[X^3]$.
- La variable $X$ suit une loi $\mathcal{N}(0,1)$, dont la densité $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ est une fonction paire. La fonction de la variable aléatoire intégrée $g(x) = x^3$ est une fonction impaire. Le produit d'une fonction paire et d'une fonction impaire est une fonction impaire.
- L'intégrale d'une fonction intégrable impaire sur un domaine symétrique par rapport à l'origine (ici $\mathbb{R}$) est rigoureusement nulle : $\mathbb{E}[X^3] = \int_{-\infty}^{\infty} x^3 \frac{1}{\sqrt{2\pi}}e^{-x^2/2} dx = 0$.
La covariance entre $X$ et $Y$ est donc nulle : $\text{Cov}(X,Y) = 0$.

**2. Réfutation de l'indépendance**
La définition de l'indépendance stipule que pour tout choix d'ensembles boréliens $A$ et $B$, $\mathbb{P}(X \in A \cap Y \in B) = \mathbb{P}(X \in A)\mathbb{P}(Y \in B)$.
Choississons $A = [1, 2]$ et $B = [4, \infty[$.
- Calculons $\mathbb{P}(X \in A \cap Y \in B)$ :
  L'événement $(X \in [1, 2])$ s'est réalisé.
  Puisque $Y = X^2$, si $X \in [1, 2]$, alors $Y = X^2 \in [1^2, 2^2] = [1, 4]$.
  L'événement $(Y \in [4, \infty[)$ requiert que $Y \geq 4$. L'intersection est donc réduite au point singulier $X=2, Y=4$.
  Puisque les variables sont absolument continues (à densité), la probabilité d'un point est nulle : $\mathbb{P}(X \in [1, 2] \cap Y \in [4, \infty[) = 0$.
- Cependant, le produit des probabilités marginales $\mathbb{P}(X \in [1, 2]) \times \mathbb{P}(Y \in [4, \infty[)$ est le produit de deux probabilités strictement positives (car il s'agit d'intégrales de la densité gaussienne et chi-carré strictement positives sur des intervalles de mesure de Lebesgue non nulle).
Ainsi, $\mathbb{P}(X \in A \cap Y \in B) = 0 \neq \mathbb{P}(X \in A)\mathbb{P}(Y \in B) > 0$.
**Conclusion :** Bien que non corrélées (covariance nulle), $X$ et $Y$ ne sont absolument pas indépendantes (elles sont même totalement dépendantes de manière déterministe non-linéaire).
