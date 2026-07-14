---
title: "Exercice 6 : Transformation d'Abel"
difficulty: ★★★☆☆
---
# Exercice 6 : Transformation d'Abel

## Énoncé
Énoncer et démontrer la règle d'Abel (ou transformation d'Abel) pour les séries de la forme $\sum a_n b_n$, puis l'appliquer pour montrer la convergence de la série $\sum \frac{\cos(n\theta)}{n}$ pour $\theta \notin 2\pi\mathbb{Z}$.

## Correction

1. **Règle d'Abel (Énoncé) :** Soient $(a_n)$ et $(b_n)$ deux suites telles que :
   - $(a_n)$ est décroissante, positive, de limite nulle.
   - Les sommes partielles $B_n = \sum_{k=0}^n b_k$ sont bornées (il existe $M > 0$ t.q. $|B_n| \le M \ \forall n$).
   Alors la série $\sum a_n b_n$ converge.
2. **Démonstration :** Posons $S_N = \sum_{n=1}^N a_n b_n$. Comme $b_n = B_n - B_{n-1}$ (avec $B_0=0$), on a par sommation par parties :
   $S_N = \sum_{n=1}^N a_n (B_n - B_{n-1}) = \sum_{n=1}^N a_n B_n - \sum_{n=1}^N a_n B_{n-1} = \sum_{n=1}^N a_n B_n - \sum_{n=0}^{N-1} a_{n+1} B_n$
   $S_N = a_N B_N + \sum_{n=1}^{N-1} (a_n - a_{n+1}) B_n$.
   - Le terme de bord $a_N B_N$ tend vers 0 (car $a_N \to 0$ et $B_N$ est bornée).
   - La série $\sum (a_n - a_{n+1}) B_n$ converge absolument : en effet, $|(a_n - a_{n+1}) B_n| \le M(a_n - a_{n+1})$ car $(a_n)$ est décroissante, et $\sum (a_n - a_{n+1}) = a_1 - a_N \to a_1$, donc cette somme télescopique converge.
   La convergence absolue impliquant la convergence simple, $S_N$ admet une limite, d'où la convergence de la série.
3. **Application :** Prenons $a_n = 1/n$ (qui tend vers 0 en décroissant) et $b_n = \cos(n\theta)$.
   $B_n = \sum_{k=1}^n \cos(k\theta) = \text{Re}(\sum_{k=1}^n e^{ik\theta})$. C'est une somme géométrique de raison $e^{i\theta} \neq 1$.
   $|B_n| = |\frac{e^{i\theta} - e^{i(n+1)\theta}}{1 - e^{i\theta}}| \le \frac{2}{|1 - e^{i\theta}|} = \frac{1}{|\sin(\theta/2)|}$.
   La suite $(B_n)$ est bornée par une constante $M_\theta$. D'après la règle d'Abel, la série converge.
