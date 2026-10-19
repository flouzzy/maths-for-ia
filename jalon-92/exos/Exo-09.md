# Exercice 9 : Convergence des fonctions empiriques de répartition (Théorème de Glivenko-Cantelli)

$\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires I.I.D. dont la fonction de répartition commune est notée $F(x) = \mathbb{P}(X_1 \leq x)$.
Pour tout réel $x$, on définit la fonction de répartition empirique :
$$ F_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{X_i \leq x} $$
où l'indicatrice $\mathbf{1}_{A}$ vaut 1 si l'événement $A$ est réalisé, et 0 sinon.

1. Fixons un $x \in \mathbb{R}$. Montrer rigoureusement que $F_n(x) \xrightarrow{p.s.} F(x)$.
2. (Discussion) Le théorème de Glivenko-Cantelli affirme que cette convergence est uniforme sur $\mathbb{R}$ presque sûrement. Pourquoi la LFGN classique ne suffit-elle pas à prouver directement le théorème de Glivenko-Cantelli ?

**Correction détaillée :**

1. Fixons un $x \in \mathbb{R}$.
   Définissons la suite de variables aléatoires $Y_i = \mathbf{1}_{X_i \leq x}$.
   Puisque les $X_i$ sont I.I.D., les variables $Y_i$ sont également I.I.D.
   Les $Y_i$ suivent une loi de Bernoulli. Calculons leur espérance :
   $$ \mathbb{E}[Y_1] = \mathbb{E}[\mathbf{1}_{X_1 \leq x}] = \mathbb{P}(X_1 \leq x) = F(x) $$
   Cette espérance est finie (elle appartient à $[0,1]$).
   Par définition, $F_n(x) = \frac{1}{n} \sum_{i=1}^n Y_i$ est la moyenne empirique des $Y_i$.
   D'après la loi forte des grands nombres appliquée à la suite $(Y_i)$, on a :
   $$ F_n(x) \xrightarrow{p.s.} \mathbb{E}[Y_1] = F(x) $$
2. L'argument précédent montre que pour **chaque** $x$ fixé, l'ensemble exceptionnel (de probabilité nulle) $\mathcal{N}_x$ sur lequel on n'a pas convergence dépend de $x$.
   Puisqu'il y a une indénombrabilité de points $x \in \mathbb{R}$, l'union des ensembles exceptionnels $\bigcup_{x \in \mathbb{R}} \mathcal{N}_x$ pourrait ne plus être de probabilité nulle !
   La LFGN classique nous donne une convergence ponctuelle presque sûre, mais pas la convergence de la borne supérieure (supremum).
   Le théorème de Glivenko-Cantelli requiert un argument supplémentaire de compacité ou de monotonie des fonctions de répartition pour "densifier" l'espace réel (par exemple via les rationnels $\mathbb{Q}$) afin de contourner le problème de l'union indénombrable.
