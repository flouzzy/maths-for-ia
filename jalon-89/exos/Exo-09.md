# Exercice 9

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Promenade aléatoire sur $\mathbb{Z}$ et récurrence

Considérons une marche aléatoire simple et symétrique sur $\mathbb{Z}$, définie par $S_n = \sum_{i=1}^n X_i$, où $X_i \in \{-1, 1\}$ sont i.i.d. avec probabilité $\frac{1}{2}$.
En sachant que $\mathbb{P}(S_{2n} = 0) \sim \frac{1}{\sqrt{\pi n}}$, prouver que la marche aléatoire repasse par l'origine une infinité de fois presque sûrement.

**Correction détaillée :**
1. On s'intéresse aux événements $A_{n} = \{S_{2n} = 0\}$ qui caractérisent un retour à l'origine à un instant pair (un retour à un instant impair est impossible).
2. L'énoncé donne un équivalent asymptotique issu de la formule de Stirling : $\mathbb{P}(A_n) \sim \frac{1}{\sqrt{\pi n}}$.
3. La série associée est $\sum_{n=1}^{\infty} \mathbb{P}(A_n)$. Puisque le terme général est équivalent à $\frac{1}{\sqrt{\pi} n^{1/2}}$ et que $1/2 \le 1$, la série diverge d'après le critère de Riemann.
4. On ne peut pas directement appliquer le second lemme de Borel-Cantelli car les événements $A_n$ ne sont pas indépendants (si l'on est en zéro en $2n$, on a de fortes chances d'y être à nouveau plus tard qu'une marche qui part de loin).
5. Pour contourner cela, on s'appuie sur un corollaire classique ou sur l'espérance du nombre de retours. Posons $N = \sum_{n=1}^{\infty} \mathbf{1}_{A_n}$, le nombre total de retours.
6. L'espérance vaut $\mathbb{E}[N] = \sum_{n=1}^{\infty} \mathbb{P}(A_n) = +\infty$.
7. Soit $f$ la probabilité qu'en partant de l'origine, on y revienne au moins une fois en temps fini. Si $f < 1$, le nombre total de retours suit une loi géométrique sur $\mathbb{N}$ de paramètre $1-f$. Dans ce cas, $\mathbb{E}[N] = \frac{f}{1-f} < +\infty$.
8. Puisque nous avons prouvé par la série que $\mathbb{E}[N] = +\infty$, il est nécessaire que $f = 1$.
9. Si le retour est certain ($f=1$), par propriété de Markov forte à chaque retour, on repart à zéro et le prochain retour est également certain. On déduit que le retour se produit une infinité de fois avec probabilité 1.
