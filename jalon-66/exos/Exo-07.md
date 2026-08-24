---
title: "Exercice 07 : Limites de fonctions simples majorantes"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 07 : Limites de fonctions simples majorantes

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $f \in \mathcal{M}^+$. Soit $s$ une fonction simple positive telle que $s \le f$. Montrer l'existence d'une suite $(s_n)$ de fonctions simples, croissante, tendant vers $f$, telle que $s_n \ge s$ pour tout $n$.

---

## Correction détaillée

1. **L'approximation standard de Lebesgue :**
Le théorème fondamental d'approximation de Lebesgue garantit l'existence d'une suite $(t_n)_{n \in \mathbb{N}}$ de fonctions simples positives, croissante, convergeant simplement vers $f$.

2. **Garantir la minoration par $s$ :**
On sait que $s \le f$, mais les $t_n$ ne sont pas nécessairement au-dessus de $s$ pour les petites valeurs de $n$.
Posons $s_n = \max(t_n, s)$.

3. **Propriétés de $s_n$ :**
- **Simplicité :** $t_n$ et $s$ sont simples (prennent un nombre fini de valeurs). Le maximum de deux fonctions simples prend des valeurs parmi toutes les paires de maxima, soit un nombre fini. Elle est mesurable car max de mesurables. Donc $s_n$ est simple.
- **Minoration :** Par définition du maximum, $s_n \ge s$.
- **Majorisation par $f$ :** Puisque $t_n \le f$ et $s \le f$, on a $s_n = \max(t_n, s) \le f$.
- **Croissance :** $t_n \le t_{n+1} \implies \max(t_n, s) \le \max(t_{n+1}, s) \implies s_n \le s_{n+1}$.
- **Convergence :** Fixons $x$. Puisque $\lim t_n(x) = f(x)$, et que $f(x) \ge s(x)$, on aura $\lim \max(t_n(x), s(x)) = \max(f(x), s(x)) = f(x)$.
La suite $(s_n)$ vérifie donc toutes les propriétés requises.
