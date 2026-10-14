# Exercice 2

\subsection*{Exercice 2 : Indépendance et événement contraire \quad $\bigstar\star\star\star\star$}

**Énoncé :**
Montrer que si $A$ et $B$ sont indépendants, alors $A$ et $B^c$ le sont aussi, où $B^c$ désigne le complémentaire de $B$.

**Correction :**
1. On sait que $B$ et $B^c$ forment une partition de $\Omega$. Donc $A = (A \cap B) \cup (A \cap B^c)$.
2. Les ensembles $(A \cap B)$ et $(A \cap B^c)$ sont disjoints.
3. Par additivité de la mesure de probabilité $P$ :
   $P(A) = P(A \cap B) + P(A \cap B^c)$.
4. Puisque $A$ et $B$ sont indépendants, on a $P(A \cap B) = P(A)P(B)$.
5. En substituant dans l'équation de l'étape 3 :
   $P(A) = P(A)P(B) + P(A \cap B^c)$.
6. On isole $P(A \cap B^c)$ :
   $P(A \cap B^c) = P(A) - P(A)P(B)$.
7. On factorise par $P(A)$ :
   $P(A \cap B^c) = P(A)(1 - P(B))$.
8. Or, par propriété du complémentaire, $1 - P(B) = P(B^c)$.
9. Ainsi, $P(A \cap B^c) = P(A)P(B^c)$.
10. Cela correspond exactement à la définition de l'indépendance de $A$ et $B^c$.
