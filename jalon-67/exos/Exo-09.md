# Exercice 9 : Théorème de Fubini abstrait (cas positif) \quad $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
Soit $\mu$ et $\nu$ deux mesures de comptage sur $\mathbb{N}$. Montrer que $\sum_i \sum_j a_{i,j} = \sum_j \sum_i a_{i,j}$ pour $a_{i,j} \ge 0$.

## Correction Détaillée
C'est l'application directe du corollaire de Beppo Levi. On définit $u_j(i) = a_{i,j}$. Chaque $u_j$ est une fonction mesurable positive sur $\mathbb{N}$.
L'intégrale par rapport à la mesure de comptage sur $i$ est la somme sur $i$. Donc :
$$\int_{\mathbb{N}} \left(\sum_j u_j(i)\right) d\mu(i) = \sum_j \int_{\mathbb{N}} u_j(i) d\mu(i)$$
Ce qui s'écrit $\sum_i (\sum_j a_{i,j}) = \sum_j (\sum_i a_{i,j})$. La positivité garantit qu'il n'y a pas d'ambiguïté en cas de valeur infinie.
