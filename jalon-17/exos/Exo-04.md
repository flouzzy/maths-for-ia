---
title: "Exercice 4 : Comparaison série/intégrale pour une semi-convergence"
difficulty: ★★☆☆☆
---
# Exercice 4 : Comparaison série/intégrale pour une semi-convergence

## Énoncé
Montrer que la série de terme général $u_n = \frac{\sin(\sqrt{n})}{n}$ est convergente, bien qu'elle ne soit pas absolument convergente.

## Correction
1. **Étude de la convergence absolue :** $|u_n| = \frac{|\sin(\sqrt{n})|}{n}$. On sait que $\sin^2(x) \le |\sin(x)|$. Ainsi, $|u_n| \ge \frac{\sin^2(\sqrt{n})}{n} = \frac{1 - \cos(2\sqrt{n})}{2n}$.
La série $\sum \frac{1}{2n}$ diverge (série harmonique). La série $\sum \frac{\cos(2\sqrt{n})}{2n}$ est convergente (par transformation d'Abel ou comparaison intégrale). Ainsi, la somme $\sum |u_n|$ diverge. La série n'est pas absolument convergente.
2. **Étude de la convergence simple :** Posons $f(t) = \frac{\sin(\sqrt{t})}{t}$ pour $t \ge 1$.
On effectue un développement asymptotique par intégration par parties. Calculons $\int_1^X \frac{\sin(\sqrt{t})}{t} dt$. Changement de variable $u = \sqrt{t}$, $dt = 2u du$ :
$= \int_1^{\sqrt{X}} \frac{\sin(u)}{u^2} 2u du = 2 \int_1^{\sqrt{X}} \frac{\sin(u)}{u} du$.
L'intégrale de Dirichlet $\int_1^\infty \frac{\sin(u)}{u} du$ converge. Donc l'intégrale impropre $\int_1^\infty f(t) dt$ converge.
3. **Lien avec la série :** Par la formule d'Euler-Maclaurin ou une simple comparaison série/intégrale, la série $\sum u_n$ a la même nature que l'intégrale $\int_1^\infty f(t) dt$ car l'erreur $\sum_{n=1}^N u_n - \int_1^N f(t) dt$ converge.
La série $\sum u_n$ est donc semi-convergente.
