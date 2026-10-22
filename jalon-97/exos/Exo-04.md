# Exercice 4

**Difficulté :** $\star\star\star\star\☆$

**Énoncé :**
Sur l'espace vectoriel $E = \mathbb{R}[X]$ des polynômes à coefficients réels, on considère la norme $\|P\| = \sup_{t \in [0,1]} |P(t)|$. Soit l'opérateur de dérivation $D : P \mapsto P'$. Montrer que $D$ n'est pas continu de $(E, \|\cdot\|)$ dans lui-même.

**Correction Détaillée :**
1. Pour démontrer qu'un opérateur linéaire n'est pas continu, il suffit de trouver une suite de vecteurs $(P_n)_{n \in \mathbb{N}}$ telle que le rapport $\frac{\|D(P_n)\|}{\|P_n\|}$ n'est pas borné.
2. Considérons la suite de monômes $P_n(X) = X^n$ pour $n \ge 1$.
3. Calculons la norme de $P_n$ :
   $$ \|P_n\| = \sup_{t \in [0,1]} |t^n| = 1^n = 1. $$
4. Appliquons l'opérateur de dérivation : $D(P_n)(X) = nX^{n-1}$.
5. Calculons la norme de l'image :
   $$ \|D(P_n)\| = \sup_{t \in [0,1]} |n t^{n-1}| = n \cdot 1^{n-1} = n. $$
6. Évaluons le rapport :
   $$ \frac{\|D(P_n)\|}{\|P_n\|} = \frac{n}{1} = n. $$
7. Lorsque $n \to \infty$, ce rapport tend vers l'infini. Il n'existe donc aucune constante $C$ telle que $\|D(P)\| \le C\|P\|$ pour tout polynôme $P$.
8. **Conclusion :** L'opérateur de dérivation $D$ n'est pas continu pour la norme uniforme sur cet espace.
9. **Note additionnelle :** Ce résultat met en évidence un phénomène typique de la dimension infinie : des opérateurs naturels peuvent être discontinus selon la norme choisie. Cela motive l'introduction des normes de Sobolev qui intègrent les dérivées pour contrôler ce comportement.
