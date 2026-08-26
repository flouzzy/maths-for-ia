### Absolue continuité (cas discret) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $\mu$ une mesure. On définit une fonction d'ensemble $\nu(A) = \int_A f d\mu = \int_X f \mathbf{1}_A d\mu$, avec $f \in \mathcal{M}_+$.
Montrer que si $\mu(A) = 0$, alors $\nu(A) = 0$. (Ceci prouve que $\nu$ est absolument continue par rapport à $\mu$).

**Correction Détaillée :**
**Étape 1 : Traduction du problème.**
Nous voulons montrer que si $\mu(A) = 0$, l'intégrale de $g = f \mathbf{1}_A$ par rapport à $\mu$ est nulle.

**Étape 2 : Support de la fonction.**
Où la fonction $g$ est-elle strictement positive ?
$g(x) > 0 \iff f(x) \mathbf{1}_A(x) > 0 \iff f(x) > 0 \text{ ET } x \in A$.
Donc, le support strict de $g$, notons-le $E_g = \{x \mid g(x) > 0\}$, est un sous-ensemble de $A$ : $E_g \subset A$.

**Étape 3 : Mesure du support.**
Par croissance de la mesure, $\mu(E_g) \le \mu(A)$.
Puisque $\mu(A) = 0$ par hypothèse, on a $\mu(E_g) = 0$.

**Étape 4 : Utilisation du résultat établi.**
Nous avons vu (Exo 8) que si le support strict d'une fonction mesurable positive est de mesure nulle, alors son intégrale est nulle.
Ainsi, $\int_X g d\mu = 0$, ce qui signifie exactement que $\nu(A) = 0$.

**Conclusion :**
La "mesure à densité" $\nu$ hérite des propriétés de nullité de la mesure de base $\mu$. C'est le principe fondamental qui fonde le théorème de Radon-Nikodym.
