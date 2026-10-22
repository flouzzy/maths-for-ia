# Exercice 1

**Difficulté :** $\star\☆☆☆☆$

**Énoncé :**
Montrer que l'espace vectoriel $\mathbb{R}^n$ muni de la norme $\|x\|_1 = \sum_{i=1}^n |x_i|$ est un espace de Banach.

**Correction Détaillée :**
1. Soit $(x^{(k)})_{k \in \mathbb{N}}$ une suite de Cauchy dans $(\mathbb{R}^n, \|\cdot\|_1)$. Notons $x^{(k)} = (x_1^{(k)}, \dots, x_n^{(k)})$.
2. Par définition, pour tout $\varepsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tous $p, q \ge N$, $\|x^{(p)} - x^{(q)}\|_1 < \varepsilon$.
3. En développant la norme, on a $\sum_{i=1}^n |x_i^{(p)} - x_i^{(q)}| < \varepsilon$.
4. Pour chaque coordonnée $i \in \{1, \dots, n\}$, on déduit que $|x_i^{(p)} - x_i^{(q)}| \le \sum_{j=1}^n |x_j^{(p)} - x_j^{(q)}| < \varepsilon$.
5. Ainsi, pour chaque $i$, la suite réelle $(x_i^{(k)})_{k \in \mathbb{N}}$ est une suite de Cauchy dans $\mathbb{R}$.
6. Or, l'espace des nombres réels $\mathbb{R}$ muni de la valeur absolue est un espace métrique complet. Donc, pour chaque $i$, la suite $(x_i^{(k)})_{k \in \mathbb{N}}$ converge vers un réel $x_i \in \mathbb{R}$.
7. Considérons le vecteur $x = (x_1, \dots, x_n) \in \mathbb{R}^n$. Montrons que la suite $(x^{(k)})$ converge vers $x$ pour la norme $\|\cdot\|_1$.
8. Soit $\varepsilon > 0$. Puisque pour chaque $i$, $x_i^{(k)} \to x_i$, il existe un rang $N_i$ tel que pour $k \ge N_i$, $|x_i^{(k)} - x_i| < \frac{\varepsilon}{n}$.
9. Soit $N = \max(N_1, \dots, N_n)$. Pour tout $k \ge N$, on a :
   $$ \|x^{(k)} - x\|_1 = \sum_{i=1}^n |x_i^{(k)} - x_i| < \sum_{i=1}^n \frac{\varepsilon}{n} = \varepsilon. $$
10. La suite $(x^{(k)})$ converge donc vers $x \in \mathbb{R}^n$ pour la norme considérée. L'espace est par conséquent complet, c'est un espace de Banach.
