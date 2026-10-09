# Exercice 3 : Application de la linéarité de l'espérance

**Difficulté :** $\bigstarigstar\star\star\star$

Un professeur rend les copies à un groupe de $N$ élèves de manière totalement aléatoire. Chaque élève a donc $1/N$ probabilité de recevoir sa propre copie.
Soit $X$ la variable aléatoire représentant le nombre d'élèves recevant leur propre copie.
Calculer l'espérance $\mathbb{E}[X]$.

### Correction détaillée

Ce problème classique (le problème des chapeaux ou des dérangements) peut sembler complexe si l'on cherche la loi de $X$ (qui est difficile à exprimer). Cependant, l'utilisation astucieuse des variables indicatrices et de la linéarité de l'espérance rend la solution élégante.

1. Définissons une variable aléatoire indicatrice $I_k$ pour chaque élève $k \in \{1, \dots, N\}$ telle que :
   $$ I_k = \begin{cases} 1 & \text{si l'élève } k \text{ reçoit sa propre copie} \\ 0 & \text{sinon} \end{cases} $$
2. Le nombre total d'élèves recevant leur copie est la somme de ces indicatrices :
   $$ X = \sum_{k=1}^N I_k $$
3. Calculons l'espérance de $I_k$. Comme c'est une variable de Bernoulli :
   $$ \mathbb{E}[I_k] = 1 \cdot \mathbb{P}(I_k = 1) + 0 \cdot \mathbb{P}(I_k = 0) = \mathbb{P}(I_k = 1) $$
   Puisque les copies sont distribuées uniformément au hasard, la probabilité que la copie $k$ atterrisse entre les mains de l'élève $k$ est exactement $\frac{1}{N}$.
   Donc, $\mathbb{E}[I_k] = \frac{1}{N}$.
4. On applique la linéarité de l'espérance. Le théorème stipule que $\mathbb{E}[X+Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ quelles que soient les dépendances entre $X$ et $Y$. (Et ici, les $I_k$ sont fortement dépendantes).
   $$ \mathbb{E}[X] = \mathbb{E}\left[ \sum_{k=1}^N I_k \right] = \sum_{k=1}^N \mathbb{E}[I_k] $$
   $$ \mathbb{E}[X] = \sum_{k=1}^N \frac{1}{N} = N \times \frac{1}{N} = 1 $$

L'espérance est de 1 : en moyenne, un seul élève reçoit sa copie, indépendamment du nombre d'élèves $N$.
