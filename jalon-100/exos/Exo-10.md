# Exercice 10 : Condensation des singularités
$\bigstar\bigstar\bigstar\bigstar\bigstar$
**Énoncé :**
Soit $E$ un espace de Banach. Soient $F_n$ des espaces vectoriels normés et $T_{n,m} \in \mathcal{L}(E, F_n)$ pour $n, m \ge 1$.
Supposons que pour tout $n$, $\sup_m \|T_{n,m}\| = \infty$.
Montrer que l'ensemble $\{x \in E : \forall n, \sup_m \|T_{n,m}(x)\| = \infty \}$ est un $G_\delta$ dense dans $E$ (intersection dénombrable d'ouverts denses).
C'est le théorème de condensation des singularités.

**Correction :**
1. Fixons $n$. Posons $E_n = \{x \in E : \sup_m \|T_{n,m}(x)\| = \infty\}$.
   On sait par la contraposée du théorème de Banach-Steinhaus, et puisque $\sup_m \|T_{n,m}\| = \infty$, que $E_n$ n'est pas vide.
   Plus précisément, par la preuve de Baire, le complémentaire $E \setminus E_n = \{x \in E : \sup_m \|T_{n,m}(x)\| < \infty\}$ est une réunion dénombrable de fermés d'intérieurs vides (car sinon la norme serait bornée).
   Donc $E \setminus E_n$ est maigre (première catégorie de Baire).
2. Par le théorème de Baire sur l'espace complet $E$, le complémentaire d'un ensemble maigre est un $G_\delta$ dense.
   Ainsi, $E_n$, qui est l'intersection des ouverts denses $O_{n,k} = \{x : \exists m, \|T_{n,m}(x)\| > k\}$, est dense dans $E$.
3. Considérons l'ensemble total de singularités $S = \bigcap_{n \in \mathbb{N}} E_n$.
   L'ensemble $S$ est une intersection dénombrable d'ensembles $E_n$, où chaque $E_n$ est lui-même une intersection dénombrable d'ouverts denses.
4. $S$ est donc une intersection dénombrable d'ouverts denses dans un espace de Banach.
   Par le théorème de Baire, $S$ est dense dans $E$ (et non vide).
5. Conclusion : Il existe des vecteurs $x \in E$ (et ils sont denses dans $E$) pour lesquels toutes les familles $(T_{n,m}(x))_m$ "explosent" simultanément pour chaque $n$.