---
title: "Exercice 09 : Densité de masse glissante"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 09 : Densité de masse glissante

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

On étudie une autre configuration de perte de masse.
Soit $f_n(x) = \mathbf{1}_{[n, n+1]}(x)$ sur l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$.
Montrez que $\int_{\mathbb{R}} f_n \, d\lambda = 1$ pour tout $n$.
Déterminez la limite simple $f$ et son intégrale.
Prouvez que la suite $(f_n)$ ne possède aucune sous-suite dominée par une fonction intégrable $g$.

### Correction détaillée

1. $f_n$ est l'indicatrice d'un intervalle de longueur $(n+1) - n = 1$. Donc $\int f_n \, d\lambda = 1$ pour tout $n$.
2. **Limite simple :** Soit un réel $x$ fixé. Il existe un entier $N \ge x$. Pour tout $n > N$, $x \notin [n, n+1]$.
   Donc à partir d'un certain rang, $f_n(x) = 0$. Ainsi, la limite simple de $f_n$ est la fonction identiquement nulle : $f(x) = 0$ pour tout $x$.
3. **Intégrale de la limite :** L'intégrale de $f = 0$ est évidemment $0$.
   De nouveau, la limite de l'intégrale (1) diffère de l'intégrale de la limite (0). Ici, la masse ne s'échappe pas verticalement, mais "horizontalement" vers l'infini.
4. **Absence de domination :** Supposons par l'absurde qu'il existe une fonction Lebesgue-intégrable $g \ge 0$ telle que pour tout $n$ et tout $x$, $f_n(x) \le g(x)$.
   Cela signifie que pour tout $x \in \mathbb{R}_+$, puisque $x$ appartient à un intervalle $[n, n+1]$ (avec chevauchements aux entiers), la fonction indicatrice correspondante y vaut 1.
   Donc $g(x) \ge 1$ pour tout $x \ge 0$.
   Intégrons sur $\mathbb{R}_+$ :
   $$ \int_{\mathbb{R}_+} g \, d\lambda \ge \int_{\mathbb{R}_+} 1 \, d\lambda = \lambda(\mathbb{R}_+) = +\infty $$
   L'intégrale de $g$ est infinie, ce qui contredit l'hypothèse que $g$ est intégrable.
   La condition de domination est impossible, justifiant l'échec de la convergence.
