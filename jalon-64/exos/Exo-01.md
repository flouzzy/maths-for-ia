# Exercice 1 : Propriétés fondamentales de la mesure

**Difficulté :** $\displaystyle \\bigstar\\star\\star$

## Énoncé

Démontrer formellement que pour tout ensemble mesurable $A$ et tout réel $c$, si nous définissons la dilatation $cA = \{cx \mid x \in A\}$, alors $cA$ est Lebesgue-mesurable et $\lambda(cA) = |c|\lambda(A)$. Appliquer ensuite ce résultat à un segment $A = [0, 1]$ et une constante $c = 3$, puis à l'ensemble de Cantor pour tout $c \neq 0$.

## Correction Détaillée

1. **Mesure extérieure sous dilatation :** Soit $\epsilon > 0$ et $A \subset \mathbb{R}$. Par définition de la mesure extérieure, il existe une suite d'intervalles ouverts $I_n = ]a_n, b_n[$ telle que $A \subset \bigcup I_n$ et $\sum \ell(I_n) < \lambda^*(A) + \epsilon$.
2. Considérons l'ensemble $cI_n$. Si $c > 0$, $cI_n = ]ca_n, cb_n[$, dont la longueur est $cb_n - ca_n = c(b_n - a_n) = |c|\ell(I_n)$.
   Si $c < 0$, $cI_n = ]cb_n, ca_n[$, dont la longueur est $ca_n - cb_n = -c(b_n - a_n) = |c|\ell(I_n)$.
   Si $c = 0$, $cI_n = \{0\}$, de longueur nulle.
3. La suite d'intervalles $(cI_n)$ forme un recouvrement ouvert de $cA$. Ainsi, $\lambda^*(cA) \le \sum \ell(cI_n) = |c|\sum \ell(I_n) < |c|(\lambda^*(A) + \epsilon)$. Puisque $\epsilon$ est arbitraire, $\lambda^*(cA) \le |c|\lambda^*(A)$.
4. En appliquant la même logique à la transformation inverse par $1/c$ sur l'ensemble $cA$, nous obtenons : $\lambda^*(A) \le (1/|c|)\lambda^*(cA)$. D'où $\lambda^*(cA) \ge |c|\lambda^*(A)$.
5. Donc $\lambda^*(cA) = |c|\lambda^*(A)$.
6. **Mesurabilité :** Soit un ensemble de test $E$. $\lambda^*(E \cap cA) + \lambda^*(E \cap (\mathbb{R} \setminus cA)) = \lambda^*(c(E/c \cap A)) + \lambda^*(c(E/c \cap (\mathbb{R} \setminus A))) = |c| [ \lambda^*(E/c \cap A) + \lambda^*(E/c \cap (\mathbb{R} \setminus A)) ] = |c|\lambda^*(E/c) = \lambda^*(E)$. Le critère de Carathéodory est respecté.
7. **Applications concrètes :** Pour $A = [0, 1]$ et $c = 3$, $cA = [0, 3]$. $\lambda(cA) = |3|\times 1 = 3$. Pour l'ensemble de Cantor $\mathcal{C}$, $\lambda(c\mathcal{C}) = |c| \times 0 = 0$.
