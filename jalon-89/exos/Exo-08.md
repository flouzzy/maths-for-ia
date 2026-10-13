# Exercice 8

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Enregistrement de records

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables indépendantes et de même loi uniforme sur $[0, 1]$.
On dit que le terme $X_n$ est un "record" s'il est strictement supérieur à tous les précédents : $X_n > \max(X_1, \dots, X_{n-1})$.
1. Calculer la probabilité que $X_n$ soit un record.
2. Déduire le nombre de records enregistrés asymptotiquement.

**Correction détaillée :**
1. Les variables $X_1, \dots, X_n$ sont continues, indépendantes et identiquement distribuées. La probabilité qu'il existe deux valeurs égales parmi elles est nulle.
2. Par symétrie stricte de l'espace probabilisé, chaque variable $X_i$ pour $1 \le i \le n$ a exactement la même chance d'être la valeur maximale de l'échantillon fini $\{X_1, \dots, X_n\}$.
3. Il y a $n$ variables dans cet échantillon, donc la probabilité que la dernière, $X_n$, soit le maximum, est $\mathbb{P}(A_n) = \frac{1}{n}$.
4. Étudions l'événement $A_n$ : "$X_n$ est un record". La série associée est $\sum_{n=1}^{\infty} \mathbb{P}(A_n) = \sum_{n=1}^{\infty} \frac{1}{n}$.
5. Cette série harmonique diverge.
6. On peut démontrer (via un calcul d'intégrale) que les événements $A_n$ sont mutuellement indépendants, car l'ordre relatif des nouvelles variables par rapport aux anciennes dépend de permutations aléatoires uniformes.
7. Par le second lemme de Borel-Cantelli, l'indépendance et la divergence impliquent que la probabilité d'avoir une infinité de records est de 1.
