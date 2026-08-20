---
title: "Exercice 9 : Continuité croissante de la mesure de Lebesgue"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

## Énoncé

Soit $(A_n)_{n \in \mathbb{N}}$ une suite croissante d'ensembles mesurables au sens de Lebesgue, c'est-à-dire que pour tout entier $n$, on a géométriquement $A_n \subset A_{n+1}$.
Soit $A = \bigcup_{n=0}^{+\infty} A_n$ l'ensemble limite.
Démontrer, en utilisant l'axiome de $\sigma$-additivité des mesures, la propriété de continuité croissante :
$$\lambda(A) = \lim_{n \to +\infty} \lambda(A_n)$$

## Correction Détaillée

Bien que $(A_n)$ soit une union, la difficulté réside dans le fait que les ensembles ne sont pas disjoints, ce qui interdit l'application directe de la $\sigma$-additivité. La technique analytique standard consiste à "disjointiser" la suite ("astuce des couronnes concentriques").

Posons la nouvelle suite analytique d'ensembles suivante :
$B_0 = A_0$
Pour tout entier $n \ge 1$, $B_n = A_n \setminus A_{n-1}$.

**Vérification des propriétés algébriques de la suite $(B_n)$ :**
1. **Mesurabilité :** Chaque $B_n$ est l'intersection de $A_n$ et du complémentaire de $A_{n-1}$. La tribu de Lebesgue $\mathcal{L}(\mathbb{R})$ étant stable par complémentation et intersection, chaque sous-ensemble $B_n$ est parfaitement mesurable.
2. **Disjonction mutuelle :** Soient $i, j$ deux entiers distincts. Supposons, sans perte de généralité algébrique, que $i < j$. Par construction, $B_j = A_j \setminus A_{j-1}$. Puisque la suite $(A_n)$ est croissante ($A_i \subset A_{j-1}$), l'ensemble $A_i$ est entièrement retiré lors de l'opération de différence. Par suite, $B_j \cap A_i = \emptyset$. Comme $B_i \subset A_i$, on en déduit formellement la disjonction stricte : $B_i \cap B_j = \emptyset$.
3. **Reconstitution de l'union :** Une simple récurrence sur les unions finies (somme télescopique ensembliste) montre que pour tout entier $N \ge 0$ :
$$\bigcup_{n=0}^{N} B_n = A_N$$
Par extension à l'infini (les éléments apparaissant dans l'union globale apparaissent à une certaine étape $N$), on démontre l'identité structurelle limite :
$$A = \bigcup_{n=0}^{+\infty} A_n = \bigcup_{n=0}^{+\infty} B_n$$

**Évaluation par la mesure de Lebesgue :**
Nous sommes désormais en présence d'une union dénombrable d'ensembles disjoints mesurables. La puissance du théorème de $\sigma$-additivité (propre aux vraies mesures sur une tribu, contrairement à la mesure extérieure non contrainte) s'applique parfaitement. Pour l'ensemble global de gauche :
$$\lambda(A) = \lambda\left( \bigcup_{n=0}^{+\infty} B_n \right) = \sum_{n=0}^{+\infty} \lambda(B_n)$$

Par la définition fondamentale analytique d'une série convergente ou divergente, la somme infinie est définie comme la limite de la séquence de ses sommes partielles algébriques :
$$\lambda(A) = \lim_{N \to +\infty} \sum_{n=0}^{N} \lambda(B_n)$$

Appliquons à nouveau l'additivité finie à l'intérieur de la limite, en se rappelant la reconstitution ensembliste $\bigcup_{n=0}^{N} B_n = A_N$ des ensembles disjoints :
$$\sum_{n=0}^{N} \lambda(B_n) = \lambda\left( \bigcup_{n=0}^{N} B_n \right) = \lambda(A_N)$$

En substituant cette équivalence directe sous l'opérateur limite, nous obtenons l'équation terminale :
$$\lambda(A) = \lim_{N \to +\infty} \lambda(A_N)$$
Ce théorème de "continuité croissante" de la mesure permet de traiter les ensembles limites par un passage à la limite analytique sécurisé sur les mesures scalaires des approximations.
