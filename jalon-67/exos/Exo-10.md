---
title: "Exercice 10 : Application fonctionnelle : Continuité des opérateurs intégraux"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Application fonctionnelle : Continuité des opérateurs intégraux

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Problème

Soit $T$ un opérateur défini sur les fonctions positives par $Tf(x) = \int_0^x f(t) dt$. Démontrer, en détaillant chaque argument de la théorie de la mesure, que si $f_n \ge 0$ croît vers $f$, alors $Tf_n$ croît vers $Tf$.

## Démonstration et Résolution

### Étape 1 : Hypothèses et définition de l'opérateur
Nous travaillons sur un intervalle $I \subset \mathbb{R}$ muni de la tribu borélienne et de la mesure de Lebesgue.
Soit $(f_n)$ une suite de fonctions mesurables positives telles que $f_n(x) \le f_{n+1}(x)$ pour presque tout $x$, et $\lim_{n \to \infty} f_n(x) = f(x)$.
L'opérateur $T$ assigne à chaque fonction $f$ une nouvelle fonction dont la valeur en $x$ est l'intégrale de $f$ sur le segment $[0,x]$. Rigoureusement, on l'écrit avec une fonction indicatrice pour travailler sur l'espace entier :
$$ Tf_n(x) = \int_0^\infty f_n(t) \mathbf{1}_{[0,x]}(t) dt $$

### Étape 2 : Monotonie de l'opérateur
Fixons un réel $x \ge 0$. Nous devons prouver que la suite numérique $(Tf_n(x))_{n \in \mathbb{N}}$ est croissante.
Puisque $f_n(t) \le f_{n+1}(t)$ pour tout $t$, en multipliant par la fonction indicatrice (qui est positive), l'inégalité est conservée :
$$ f_n(t) \mathbf{1}_{[0,x]}(t) \le f_{n+1}(t) \mathbf{1}_{[0,x]}(t) $$
Par croissance de l'intégrale de Lebesgue :
$$ \int_0^\infty f_n(t) \mathbf{1}_{[0,x]}(t) dt \le \int_0^\infty f_{n+1}(t) \mathbf{1}_{[0,x]}(t) dt $$
Soit $Tf_n(x) \le Tf_{n+1}(x)$. L'opérateur préserve donc la monotonie.

### Étape 3 : Application locale de Beppo Levi
Pour ce $x$ fixé, posons $h_n(t) = f_n(t) \mathbf{1}_{[0,x]}(t)$.
- Les $h_n$ sont mesurables car produit de fonctions mesurables.
- Les $h_n$ sont positives car $f_n \ge 0$ et $\mathbf{1} \ge 0$.
- La suite $(h_n)$ est croissante en $n$ comme démontré ci-dessus.
- La limite simple de $h_n(t)$ quand $n \to \infty$ est $\lim (f_n(t)) \mathbf{1}_{[0,x]}(t) = f(t) \mathbf{1}_{[0,x]}(t)$.

Toutes les conditions du Théorème de Convergence Monotone de Beppo Levi sont réunies pour la suite $(h_n)$.
On applique le théorème :
$$ \lim_{n \to \infty} \int_0^\infty h_n(t) dt = \int_0^\infty \lim_{n \to \infty} h_n(t) dt $$

### Étape 4 : Conclusion
En remplaçant les termes de l'équation précédente par leur définition par l'opérateur $T$ :
$$ \lim_{n \to \infty} Tf_n(x) = \int_0^\infty f(t) \mathbf{1}_{[0,x]}(t) dt = Tf(x) $$
Cette égalité étant vraie pour tout $x \ge 0$, nous avons démontré que la suite de fonctions $Tf_n$ converge ponctuellement vers $Tf$. Associée au résultat de l'Étape 2, nous affirmons avec rigueur que $Tf_n$ croît vers $Tf$.
