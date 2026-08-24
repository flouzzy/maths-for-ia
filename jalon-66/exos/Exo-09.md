---
title: "Exercice 09 : Condition d'égalité dans l'inégalité de Markov"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 09 : Condition d'égalité dans l'inégalité de Markov

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f \in \mathcal{M}^+$ telle que $\int f \, d\mu = c < \infty$. On suppose qu'il existe un $t > 0$ tel que l'inégalité de Markov soit une égalité stricte : $\mu(\{f \ge t\}) = \frac{1}{t} \int f \, d\mu$. Que peut-on dire de $f$ ?

---

## Correction détaillée

1. **Analyse de l'inégalité de base :**
L'inégalité de Markov repose sur la minoration $f \ge t \mathbf{1}_{A_t}$, où $A_t = \{f \ge t\}$.
L'intégrale donne : $\int f \, d\mu \ge \int t \mathbf{1}_{A_t} \, d\mu = t \mu(A_t)$.

2. **Hypothèse d'égalité :**
Si $\mu(A_t) = \frac{1}{t} \int f \, d\mu$, alors $\int f \, d\mu = t \mu(A_t)$.
Cela s'écrit aussi $\int f \, d\mu - \int t \mathbf{1}_{A_t} \, d\mu = 0$.
Par linéarité (admettons la pour l'instant pour des fonctions $L^1$, prouvée plus tard pour $f$ via $f - t\mathbf{1}_{A_t}$ qui est positive), on obtient :
$$ \int (f - t \mathbf{1}_{A_t}) \, d\mu = 0 $$

3. **Étude du signe de l'intégrande :**
La fonction $g = f - t \mathbf{1}_{A_t}$ n'est pas forcément positive partout, mais :
- Sur $A_t$, $g(x) = f(x) - t \ge 0$.
- Sur $A_t^c$, $g(x) = f(x) - 0 = f(x) \ge 0$.
Donc $g \in \mathcal{M}^+$.

4. **Application du théorème du cours :**
Puisque $g \ge 0$ et $\int g \, d\mu = 0$, le théorème du cours affirme que $g = 0$ presque partout.
Donc, presque partout, $f(x) = t \mathbf{1}_{A_t}(x)$.
Cela signifie que presque partout, soit $f(x) = t$ (sur $A_t$), soit $f(x) = 0$ (sur $A_t^c$).
La fonction $f$ est donc une fonction simple (presque partout) ne prenant que les valeurs 0 et $t$.
