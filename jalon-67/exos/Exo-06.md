---
title: "Exercice 6 : TCM"
difficulty: "★★★☆☆"
---
# Exercice 6 : L'Intégrale paramétrique radiale

**Niveau :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Montrer que $\lim_{t \to 0^+} \int_0^{+\infty} \frac{\sin(tx)}{tx} e^{-x} dx = 1$. L'utilisation du TCM est-elle possible ?

**Correction détaillée :**
1. Si l'on pose $f_t(x) = \frac{\sin(tx)}{tx} e^{-x}$, on sait que $\frac{\sin(u)}{u} \le 1$ pour $u \ge 0$, donc $f_t(x) \le e^{-x}$.
2. Quand $t \searrow 0$, $f_t(x) \to e^{-x}$.
3. La fonction $t \mapsto \frac{\sin(tx)}{tx}$ sur $[0, \pi]$ est décroissante. Donc quand $t \searrow 0$, $f_t(x)$ croît (localement) vers $e^{-x}$.
4. La suite $n \mapsto f_{1/n}(x)$ est donc croissante pour $n$ assez grand, et positive. On peut appliquer le TCM pour les $n$ grands.
5. La limite de l'intégrale est donc l'intégrale de la limite : $\int_0^{+\infty} e^{-x} dx = 1$.
*(Note : Cet exercice préfigure le théorème de convergence dominée qui sera vu au Jalon 69, qui est beaucoup plus souple ici).*
