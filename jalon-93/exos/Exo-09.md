# Exercice 09 : Théorème de Bochner et Noyaux (Introduction)
Difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Une fonction complexe $\phi$ définie sur $\mathbb{R}$ est dite définie positive si pour tout entier $n \ge 1$, pour tous réels $t_1, \dots, t_n$ et tous complexes $c_1, \dots, c_n$, on a :
$\sum_{j=1}^n \sum_{k=1}^n c_j \overline{c_k} \phi(t_j - t_k) \ge 0$.
Montrer que toute fonction caractéristique d'une variable aléatoire réelle est définie positive.

**Correction pas à pas :**
1. Soit $\phi(t) = \mathbb{E}[e^{itX}]$ une fonction caractéristique.
2. Écrivons la double somme :
   $S = \sum_{j=1}^n \sum_{k=1}^n c_j \overline{c_k} \mathbb{E}[e^{i(t_j - t_k)X}]$.
3. Par linéarité de l'espérance, on peut entrer les sommes et les coefficients (qui sont déterministes) à l'intérieur de l'espérance :
   $S = \mathbb{E} \left[ \sum_{j=1}^n \sum_{k=1}^n c_j \overline{c_k} e^{it_j X} e^{-it_k X} \right]$.
4. Remarquons que $e^{-it_k X} = \overline{e^{it_k X}}$. On peut donc factoriser l'expression sous l'espérance :
   $\sum_{j=1}^n \sum_{k=1}^n c_j e^{it_j X} \overline{c_k e^{it_k X}} = \left( \sum_{j=1}^n c_j e^{it_j X} \right) \left( \sum_{k=1}^n \overline{c_k e^{it_k X}} \right)$.
5. Soit $Z = \sum_{j=1}^n c_j e^{it_j X}$. $Z$ est une variable aléatoire complexe.
   La deuxième parenthèse est exactement $\overline{Z}$.
   Donc le produit est $Z \cdot \overline{Z} = |Z|^2$.
6. L'expression devient $S = \mathbb{E} [ |Z|^2 ]$.
7. Comme le module au carré d'un complexe est toujours un réel positif ou nul, et que l'espérance préserve la positivité :
   $S \ge 0$.
C'est le sens direct du théorème de Bochner : toute fonction caractéristique est définie positive. C'est le fondement de la théorie des noyaux en Machine Learning (où la fonction définie positive devient le noyau du RKHS).
