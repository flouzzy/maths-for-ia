# Exercice 5

## Exercice 5 : Théorème de Mazur \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $E$ un espace de Banach. Montrer que si une suite $(x_n)_{n \ge 1}$ converge faiblement vers $x$, alors il existe une suite de combinaisons linéaires convexes des $(x_n)$ qui converge fortement vers $x$.

**Correction :**
*Analyse de l'énoncé :* On relie la convergence faible et la convergence forte à l'aide des enveloppes convexes et du lemme sur les sous-espaces fermés et convexes.
*Résolution pas-à-pas :*
1. **Étape 1 : L'enveloppe convexe fermée.**
   Soit $K_n = \text{Conv}(\{ x_k \mid k \ge n \})$ l'enveloppe convexe des termes de la suite à partir du rang $n$.
   Soit $\overline{K_n}$ l'adhérence (forte) de $K_n$.
   Comme $\overline{K_n}$ est fortement fermé et convexe, d'après le résultat classique (démontré via Hahn-Banach), il est aussi faiblement fermé.
2. **Étape 2 : Appartenance de la limite faible.**
   La suite $(x_k)_{k \ge n}$ converge faiblement vers $x$.
   Comme tous les termes de la suite appartiennent à $K_n \subset \overline{K_n}$, et que $\overline{K_n}$ est faiblement fermé, sa limite faible $x$ appartient nécessairement à $\overline{K_n}$.
3. **Étape 3 : Construction de la suite fortement convergente.**
   Puisque $x \in \overline{K_n}$ pour tout $n$, il existe par définition de l'adhérence un élément $y_n \in K_n$ tel que $\|y_n - x\| < 1/n$.
   Mais $y_n \in K_n$ signifie que $y_n$ est une combinaison linéaire convexe finie d'éléments de la forme $x_k$ avec $k \ge n$.
   La suite $(y_n)_{n \ge 1}$ converge fortement vers $x$ (puisque $\|y_n - x\| < 1/n \to 0$) et est constituée de combinaisons linéaires convexes des $(x_n)$.
