---
title: "Exercice 7 : Théorème de convergence monotone pour des suites presque croissantes"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Théorème de convergence monotone pour des suites presque croissantes

## Énoncé

Soit $(f_n)$ une suite de fonctions mesurables positives telles que $f_n(x) \le f_{n+1}(x)$ pour presque tout $x$ et pour tout $n$.
On note $N_n = \{ x \in X \mid f_n(x) > f_{n+1}(x) \}$, de mesure $\mu(N_n) = 0$.
Prouver que le TCM s'applique en modifiant la suite sur un ensemble de mesure nulle global.

## Correction

1. **L'ensemble d'exception :**
Pour un $n$ donné, l'inégalité $f_n \le f_{n+1}$ est violée sur l'ensemble $N_n$.
Par hypothèse, $\mu(N_n) = 0$.
Soit $N = \bigcup_{n \in \mathbb{N}} N_n$.
Par sous-additivité de la mesure, la mesure d'une union dénombrable d'ensembles de mesure nulle est nulle :
$$ \mu(N) \le \sum_{n \in \mathbb{N}} \mu(N_n) = \sum 0 = 0. $$
Sur le complémentaire $N^c$, pour tout $n$, l'inégalité $f_n(x) \le f_{n+1}(x)$ est rigoureusement vraie.

2. **Modification des fonctions :**
Définissons une nouvelle suite de fonctions :
$$ \tilde{f}_n(x) = f_n(x) \mathbf{1}_{N^c}(x) = \begin{cases} f_n(x) & \text{si } x \notin N \\ 0 & \text{si } x \in N \end{cases} $$
Les fonctions $\tilde{f}_n$ sont mesurables (produit de mesurables) et positives.
Pour tout $x \in X$, la suite $(\tilde{f}_n(x))$ est *partout* croissante. En effet, si $x \in N$, la suite est identiquement nulle ($0 \le 0$). Si $x \notin N$, par définition de $N^c$, $f_n(x) \le f_{n+1}(x)$.

3. **Application de Beppo Levi strict :**
La limite ponctuelle est $\tilde{f}(x) = \lim \tilde{f}_n(x)$.
Le TCM classique (où la croissance est exigée partout) s'applique à la suite $(\tilde{f}_n)$ :
$$ \int_X \tilde{f} d\mu = \lim_{n \to \infty} \int_X \tilde{f}_n d\mu. $$

4. **Transfert aux fonctions originales :**
Puisque $\mu(N) = 0$, modifier une fonction sur un ensemble de mesure nulle ne change pas son intégrale.
Donc $\int_X \tilde{f}_n d\mu = \int_X f_n d\mu$.
De même, $f = \lim f_n$ existe presque partout (sur $N^c$), et $\tilde{f}$ coïncide avec $f$ presque partout. Donc $\int_X \tilde{f} d\mu = \int_X f d\mu$.
En remplaçant ces égalités dans la relation de l'étape 3, on obtient l'énoncé relaxé :
$$ \int_X f d\mu = \lim_{n \to \infty} \int_X f_n d\mu. $$
La démonstration met en lumière la toute-puissance de la notion de propriété "presque partout" dans la théorie de Lebesgue.
