---
title: "Exercice 5"
---
## Exercice 5 : Fonctions sous-additives $\bigstar\bigstar\star\star$

**Énoncé :**
Soit $\mu$ une mesure finie sur $X$. Soit $(f_n)$ une suite de fonctions mesurables positives telles que $f_n \to f$ p.p.
Supposons qu'il existe une fonction $g$ intégrable telle que pour tout $n$, $f_n \le g$ p.p.
Prouver que $\int f \le \liminf \int f_n$ sans utiliser le lemme de Fatou (en utilisant Beppo Levi).

**Correction Détaillée :**
1. Posons $h_n = \inf_{k \ge n} f_k$.
2. Par définition, pour tout $k \ge n$, $h_n \le f_k$, donc en particulier $h_n \le f_n$.
3. La suite $(h_n)$ est une suite croissante de fonctions mesurables.
4. Comme $f_n \ge 0$, $h_n \ge 0$.
5. Comme $f_n \to f$ p.p., on a $\lim_{n \to \infty} h_n = \liminf_{n \to \infty} f_n = f$ p.p.
6. Appliquons le théorème de convergence monotone à la suite $(h_n)$ :
   $$\int \lim h_n = \lim \int h_n$$
   Donc $\int f = \lim \int h_n$.
7. Or, pour tout $n$, $h_n \le f_n$, donc $\int h_n \le \int f_n$.
8. En prenant la limite inférieure des deux côtés, on obtient :
   $$\lim_{n \to \infty} \int h_n \le \liminf_{n \to \infty} \int f_n$$
9. Soit $\int f \le \liminf \int f_n$.
C'est précisément la démonstration standard du Lemme de Fatou via Beppo Levi. L'hypothèse de majoration par $g$ n'était d'ailleurs pas nécessaire pour ce résultat minimal (Fatou est inconditionnel pour les fonctions positives).
