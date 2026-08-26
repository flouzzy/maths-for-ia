### Intégrale par rapport à une mesure de Dirac \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(X, \mathcal{F})$ un espace mesurable, $a \in X$, et $\delta_a$ la mesure de Dirac en $a$.
Démontrer que pour toute fonction mesurable positive $f \in \mathcal{M}_+$, on a :
$$\int_X f d\delta_a = f(a)$$

**Correction Détaillée :**
**Étape 1 : Intégration d'une indicatrice.**
Soit $A \in \mathcal{F}$. L'intégrale de la fonction indicatrice $\mathbf{1}_A$ est :
$$\int_X \mathbf{1}_A d\delta_a = \delta_a(A)$$
Par définition de la mesure de Dirac :
- Si $a \in A$, $\delta_a(A) = 1$, et $\mathbf{1}_A(a) = 1$.
- Si $a \notin A$, $\delta_a(A) = 0$, et $\mathbf{1}_A(a) = 0$.
Dans tous les cas, on a l'égalité : $\int_X \mathbf{1}_A d\delta_a = \mathbf{1}_A(a)$.

**Étape 2 : Extension aux fonctions simples.**
Soit $s = \sum_{i=1}^n c_i \mathbf{1}_{A_i}$ une fonction simple positive, avec les $A_i$ formant une partition de $X$.
Par linéarité de l'intégrale pour les fonctions simples :
$$\int_X s d\delta_a = \sum_{i=1}^n c_i \int_X \mathbf{1}_{A_i} d\delta_a = \sum_{i=1}^n c_i \delta_a(A_i)$$
Puisque les $A_i$ partitionnent $X$, le point $a$ appartient à exactement un seul ensemble de la partition, disons $A_k$.
Donc $\delta_a(A_k) = 1$ et pour $i \neq k$, $\delta_a(A_i) = 0$.
La somme se réduit donc à $c_k$. Or, par définition de $s$, on a précisément $s(a) = c_k$.
Donc $\int_X s d\delta_a = s(a)$.

**Étape 3 : Généralisation à $\mathcal{M}_+$.**
Soit $f \in \mathcal{M}_+$. Par définition, l'intégrale est le supremum des intégrales des fonctions simples $s \le f$ :
$$\int_X f d\delta_a = \sup_{s \le f} \int_X s d\delta_a = \sup_{s \le f} s(a)$$
Puisque $s(x) \le f(x)$ pour tout $x$, en particulier $s(a) \le f(a)$. Donc le supremum est inférieur ou égal à $f(a)$ :
$$\int_X f d\delta_a \le f(a)$$
Pour montrer l'inégalité inverse, considérons la fonction simple particulière $s_0 = f(a) \mathbf{1}_{\{a\}}$.
Cette fonction est bien mesurable (car $\{a\}$ est mesurable), elle est positive, et pour tout $x \in X$, $s_0(x) \le f(x)$.
Donc $s_0$ fait partie de l'ensemble sur lequel on prend le supremum.
Ainsi :
$$\int_X f d\delta_a \ge \int_X s_0 d\delta_a = f(a) \delta_a(\{a\}) = f(a) \cdot 1 = f(a)$$

**Conclusion :**
On a bien $\int_X f d\delta_a = f(a)$ pour toute fonction $f \in \mathcal{M}_+$.
