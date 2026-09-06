---
uuid: "exo-67-09"
title: "Exercice 09 : Contre-exemple avec la condition de positivité"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 09 : Contre-exemple avec la condition de positivité ($\bigstar\bigstar\bigstar\bigstar\bigstar$)

## Énoncé

Soit $f_n(x) = -\frac{1}{n} \mathbf{1}_{]0, \infty[}(x)$. Montrer que $f_n$ est croissante mais que le TCM échoue car la positivité n'est pas respectée.

## Corrigé Rigoureux

1. **Croissance :** $f_{n+1}(x) - f_n(x) = -\frac{1}{n+1} + \frac{1}{n} = \frac{1}{n(n+1)} \ge 0$. Donc la suite est croissante.
2. **Limites :** $\lim_{n \to \infty} f_n(x) = 0$ pour tout $x$. Donc $\int \lim f_n = 0$.
3. **Calcul des intégrales :** $\int_{]0, \infty[} f_n(x) dx = -\frac{1}{n} \times (+\infty) = -\infty$.
La limite des intégrales est $\lim (-\infty) = -\infty$.
L'égalité $\int \lim = \lim \int$ est FAUSSE ($0 \neq -\infty$).
Le théorème de Beppo Levi exige impérativement des fonctions positives, sinon on obtient des formes indéterminées avec l'infini (comme $-\infty + \infty$).
