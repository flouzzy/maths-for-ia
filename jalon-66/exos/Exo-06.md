---
uuid: "jalon-66-exo-06"
title: "Exercice 6 - Jalon 66"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 6 : Limite d'une intégrale (Prémices de la convergence monotone)

**Énoncé :**
Soit $X = [0, 1]$ muni de la mesure de Lebesgue $\lambda$.
Soit la suite de fonctions $f_n(x) = x^n$ pour $n \ge 1$.
1. Ces fonctions sont-elles mesurables et positives ?
2. Calculer $I_n = \int_{[0, 1]} f_n \, d\lambda$ par la formule classique (ici Riemann coïncide avec Lebesgue).
3. Déterminer la limite ponctuelle $f$ de la suite $(f_n)$ sur $[0, 1]$.
4. Calculer l'intégrale de Lebesgue de $f$, puis vérifier que $\lim_{n \to +\infty} \int f_n \, d\lambda = \int (\lim_{n \to +\infty} f_n) \, d\lambda$.

**Corrigé :**

1. **Mesurabilité et positivité :**
   Pour tout $n \ge 1$, la fonction $x \mapsto x^n$ est continue sur $[0, 1]$. Toute fonction continue est mesurable pour la tribu borélienne.
   De plus, pour $x \in [0, 1]$, $x \ge 0$, donc $x^n \ge 0$. Les fonctions $f_n$ sont bien positives.

2. **Calcul de $I_n$ :**
   Puisque $f_n$ est continue sur un intervalle borné, son intégrale de Riemann existe et coïncide avec son intégrale de Lebesgue.
   $$I_n = \int_0^1 x^n \, dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1} - 0 = \frac{1}{n+1}$$

3. **Limite ponctuelle :**
   Pour $x \in [0, 1[$, $0 \le x < 1$, donc $\lim_{n \to +\infty} x^n = 0$.
   Pour $x = 1$, $1^n = 1$ pour tout $n$, donc $\lim_{n \to +\infty} 1^n = 1$.
   La suite $(f_n)$ converge simplement vers la fonction $f$ définie par :
   $$f(x) = \begin{cases} 0 & \text{si } x \in [0, 1[ \\ 1 & \text{si } x = 1 \end{cases}$$
   Cette fonction $f$ s'écrit formellement avec l'indicatrice : $f(x) = \mathbf{1}_{\{1\}}(x)$.

4. **Intégrale de la limite et vérification :**
   La fonction $f = \mathbf{1}_{\{1\}}$ est une fonction simple positive.
   Son intégrale de Lebesgue est :
   $$\int_{[0, 1]} f \, d\lambda = 1 \times \lambda(\{1\}) = 1 \times 0 = 0$$
   (La mesure de Lebesgue d'un point est nulle).

   Regardons la limite des intégrales :
   $$\lim_{n \to +\infty} I_n = \lim_{n \to +\infty} \frac{1}{n+1} = 0$$

   Nous constatons que :
   $$\lim_{n \to +\infty} \int f_n \, d\lambda = 0 = \int f \, d\lambda = \int (\lim_{n \to +\infty} f_n) \, d\lambda$$
   Le passage à la limite sous le signe intégral est ici valide. Ce principe sera généralisé par le théorème de convergence dominée et de convergence monotone (Jalon 67).
