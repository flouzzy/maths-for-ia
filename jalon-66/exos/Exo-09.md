---
uuid: "jalon-66-exo-09"
title: "Exercice 9 - Jalon 66"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Continuité de l'intégrale par rapport aux ensembles

**Énoncé :**
Soit $f : (X, \mathcal{A}) \to [0, +\infty]$ une fonction mesurable. On définit sur $\mathcal{A}$ l'application $\nu$ par :
$$\nu(A) = \int_A f \, d\mu = \int_X f \cdot \mathbf{1}_A \, d\mu$$
Soit $(A_n)_{n \ge 1}$ une suite croissante d'ensembles mesurables, c'est-à-dire $A_1 \subset A_2 \subset A_3 \dots$, et $A = \bigcup_{n=1}^{+\infty} A_n$.
En admettant le théorème de convergence monotone (qui dit que si $g_n \uparrow g$ alors $\int g_n \to \int g$), démontrer que :
$$\lim_{n \to +\infty} \nu(A_n) = \nu(A)$$

**Corrigé :**
C'est une propriété de "continuité par valeurs inférieures" pour l'intégrale, prouvant que $\nu$ définit elle-même une nouvelle mesure (mesure à densité).

1. **Définition de la suite de fonctions :**
   Définissons la suite de fonctions $g_n = f \cdot \mathbf{1}_{A_n}$.
   Puisque $f$ est positive et les indicatrices le sont, $g_n$ est positive et mesurable.

2. **Croissance de la suite :**
   Soit $x \in X$.
   Puisque $A_n \subset A_{n+1}$, la fonction indicatrice vérifie $\mathbf{1}_{A_n}(x) \le \mathbf{1}_{A_{n+1}}(x)$.
   Comme $f(x) \ge 0$, on a $f(x) \mathbf{1}_{A_n}(x) \le f(x) \mathbf{1}_{A_{n+1}}(x)$.
   Donc pour tout $x$, $g_n(x) \le g_{n+1}(x)$.
   La suite de fonctions $(g_n)$ est croissante.

3. **Convergence simple :**
   Regardons la limite ponctuelle de $g_n(x)$.
   - Si $x \notin A$, alors $x \notin A_n$ pour tout $n$. Donc $g_n(x) = 0$ pour tout $n$. Sa limite est $0$. Or $f(x)\mathbf{1}_A(x) = 0$.
   - Si $x \in A$, par définition de l'union, il existe un rang $N$ tel que $x \in A_N$.
     Comme la suite $(A_n)$ est croissante, pour tout $n \ge N$, $x \in A_n$.
     Ainsi, pour tout $n \ge N$, $\mathbf{1}_{A_n}(x) = 1$, et $g_n(x) = f(x)$.
     La suite $(g_n(x))$ est stationnaire à $f(x)$, donc converge vers $f(x)$.
   Dans tous les cas, la suite $(g_n)$ converge ponctuellement vers $g = f \cdot \mathbf{1}_A$.

4. **Application du théorème admis (Convergence Monotone) :**
   Puisque $g_n \ge 0$, $g_n$ est croissante et $g_n \to g$ ponctuellement, le théorème de convergence monotone s'applique :
   $$\lim_{n \to +\infty} \int_X g_n \, d\mu = \int_X g \, d\mu$$
   En remplaçant par nos définitions :
   $$\lim_{n \to +\infty} \int_X f \cdot \mathbf{1}_{A_n} \, d\mu = \int_X f \cdot \mathbf{1}_A \, d\mu$$
   $$\lim_{n \to +\infty} \nu(A_n) = \nu(A)$$
La propriété est démontrée rigoureusement.
