# Exercice 7

## Exercice 7 : Théorème de Banach-Saks dans $L^2$ \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(x_n)_{n \ge 1}$ une suite faiblement convergente vers $0$ dans un espace de Hilbert $H$. Montrer qu'il existe une sous-suite $(x_{\phi(n)})$ dont les moyennes de Cesàro convergent fortement vers $0$.

**Correction :**
*Analyse de l'énoncé :* On construit une sous-suite presque orthogonale pour s'assurer que la norme de la somme croît au plus linéairement.
*Résolution pas-à-pas :*
1. **Étape 1 : Construction de la sous-suite.**
   Puisque $x_n \rightharpoonup 0$, la suite est bornée : $\|x_n\| \le M$.
   Posons $y_1 = x_1$.
   Supposons construits $y_1, \dots, y_k$.
   Comme $x_n \rightharpoonup 0$, on a $\langle x_n, y_i \rangle \to 0$ pour chaque $i \in \{1, \dots, k\}$.
   Il existe donc un rang $N$ tel que pour tout $n \ge N$ et pour $i \in \{1, \dots, k\}$, $|\langle x_n, y_i \rangle| \le \frac{1}{k}$.
   On choisit $y_{k+1} = x_{N}$. On a ainsi extrait une sous-suite telle que $|\langle y_n, y_m \rangle| \le \frac{1}{\max(n, m)-1}$ pour $n \neq m$.
2. **Étape 2 : Norme de la somme.**
   Soit $S_n = \sum_{i=1}^n y_i$. Calculons sa norme au carré :
   $$\|S_n\|^2 = \sum_{i=1}^n \|y_i\|^2 + 2 \sum_{1 \le i < j \le n} \text{Re}(\langle y_i, y_j \rangle)$$
   On sait que $\|y_i\|^2 \le M^2$. Pour les termes croisés, par construction $|\langle y_i, y_j \rangle| \le \frac{1}{j-1}$.
   $$\|S_n\|^2 \le n M^2 + 2 \sum_{j=2}^n \sum_{i=1}^{j-1} \frac{1}{j-1} = n M^2 + 2 \sum_{j=2}^n (j-1) \frac{1}{j-1} = n M^2 + 2(n-1)$$
3. **Étape 3 : Convergence des moyennes de Cesàro.**
   La moyenne de Cesàro est $M_n = \frac{1}{n} S_n$.
   On a $\|M_n\|^2 = \frac{1}{n^2} \|S_n\|^2 \le \frac{n M^2 + 2n}{n^2} = \frac{M^2 + 2}{n}$.
   Lorsque $n \to \infty$, cette norme tend vers 0.
   Donc la moyenne de Cesàro de la sous-suite converge fortement vers $0$.
