# Exercice 10

## Exercice 10 : Compacité faible-* des mesures de probabilité \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $X$ un espace métrique compact. Considérons l'espace des mesures de Radon signées $\mathcal{M}(X)$, dual de l'espace des fonctions continues $C(X)$. Soit $P(X)$ l'ensemble des mesures de probabilité sur $X$. Montrer que $P(X)$ est compact pour la topologie faible-*.

**Correction :**
*Analyse de l'énoncé :* On utilise le théorème de Banach-Alaoglu et on montre que $P(X)$ est un fermé pour la topologie faible-*.
*Résolution pas-à-pas :*
1. **Étape 1 : Le cadre de Banach-Alaoglu.**
   L'espace $C(X)$ muni de la norme $\| \cdot \|_\infty$ est un espace de Banach.
   Son dual topologique est l'espace des mesures de Radon $\mathcal{M}(X)$, avec pour norme la variation totale.
   Par le théorème de Banach-Alaoglu, la boule unité fermée $B = \{ \mu \in \mathcal{M}(X) \mid \|\mu\| \le 1 \}$ est compacte pour la topologie faible-*.
2. **Étape 2 : Inclusion de $P(X)$ dans la boule unité.**
   Une mesure de probabilité est une mesure positive de masse totale égale à 1.
   Donc si $\mu \in P(X)$, sa norme en variation totale est $\|\mu\| = \mu(X) = 1 \le 1$.
   Ainsi, $P(X) \subset B$.
3. **Étape 3 : Fermeture faible-* de $P(X)$.**
   Il suffit de montrer que $P(X)$ est fermé pour la topologie faible-*. Puisqu'il est inclus dans un compact, un fermé est un compact.
   La topologie faible-* est définie par la convergence : $\mu_\alpha \rightharpoonup^* \mu \iff \int_X f d\mu_\alpha \to \int_X f d\mu$ pour tout $f \in C(X)$.
   Soit une suite (ou un filtre) de mesures $\mu_n \in P(X)$ qui converge faiblement-* vers $\mu \in \mathcal{M}(X)$.
   Vérifions que $\mu \in P(X)$.
   a) Positivité : Si $f \ge 0$, alors $\int_X f d\mu_n \ge 0$. Par passage à la limite, $\int_X f d\mu \ge 0$. Par le théorème de représentation de Riesz, ceci assure que la mesure $\mu$ est positive.
   b) Masse totale : Prenons la fonction constante $\mathbf{1} \in C(X)$ (qui est bien continue puisque $X$ est compact).
   $\mu(X) = \int_X \mathbf{1} d\mu = \lim_{n \to \infty} \int_X \mathbf{1} d\mu_n = \lim_{n \to \infty} \mu_n(X) = \lim_{n \to \infty} 1 = 1$.
   Donc $\mu$ est bien une mesure de probabilité.
4. **Étape 4 : Conclusion.**
   $P(X)$ est un sous-ensemble fermé (pour la topologie faible-*) du compact faible-* $B$. Donc $P(X)$ est compact pour la topologie faible-*.
