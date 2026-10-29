# Exercice 4 : Opérateurs Adjoints
$\bigstar\bigstar\star\star\star$
**Énoncé :**
Soient $E$ et $F$ des espaces de Banach. Soit $(T_n)$ une suite d'opérateurs dans $\mathcal{L}(E, F)$.
Soit $(T_n^*)$ la suite des opérateurs adjoints dans $\mathcal{L}(F^*, E^*)$.
On suppose que pour tout $y^* \in F^*$, la suite $(T_n^*(y^*))$ est bornée dans $E^*$.
Montrer que la suite des opérateurs originaux $(T_n)$ est uniformément bornée, c'est-à-dire $\sup_n \|T_n\| < \infty$.

**Correction :**
1. L'opérateur adjoint $T_n^* : F^* \to E^*$ est défini par $T_n^*(y^*)(x) = y^*(T_n(x))$.
2. Par hypothèse, pour tout $y^* \in F^*$, la famille $(T_n^*(y^*))_{n \in \mathbb{N}}$ est bornée dans $E^*$.
   Or $F^*$ est un espace de Banach (dual d'un espace normé).
   Par le théorème de Banach-Steinhaus appliqué aux opérateurs $(T_n^*)$ sur l'espace de Banach $F^*$, on a $\sup_n \|T_n^*\|_{\mathcal{L}(F^*, E^*)} < \infty$.
3. Lien entre la norme de l'opérateur et celle de son adjoint :
   On sait (conséquence du théorème de Hahn-Banach) que $\|T_n\| = \|T_n^*\|$.
4. Conclusion :
   Puisque $\sup_n \|T_n^*\| < \infty$, on a immédiatement $\sup_n \|T_n\| < \infty$.