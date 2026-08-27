# Exercice 7 : Inégalité sur les Limites (Prélude à Fatou)
$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'ensembles mesurables dans $(X, \mathcal{A}, \mu)$.
On rappelle que $\liminf A_n = \bigcup_{N=0}^\infty \bigcap_{n \ge N} A_n$.
Démontrer que $\mu(\liminf A_n) \le \liminf \mu(A_n)$.

**Correction :**
1. Notons $B_N = \bigcap_{n \ge N} A_n$.
   Par définition, $B_N$ est l'ensemble des éléments qui appartiennent à tous les $A_n$ à partir du rang $N$.
2. La suite d'ensembles $(B_N)_{N \in \mathbb{N}}$ est croissante pour l'inclusion.
   En effet, $B_N = A_N \cap (\bigcap_{n \ge N+1} A_n) = A_N \cap B_{N+1}$.
   Donc $B_N \subset B_{N+1}$.
3. De plus, on observe que pour tout $n \ge N$, $B_N \subset A_n$.
   Par monotonie de la mesure, $\mu(B_N) \le \mu(A_n)$ pour tout $n \ge N$.
4. En prenant l'infimum sur les indices $n \ge N$ :
   $$\mu(B_N) \le \inf_{n \ge N} \mu(A_n)$$
5. Or, l'ensemble $\liminf A_n$ est défini comme $\bigcup_{N=0}^\infty B_N$, union croissante.
   Par la propriété de continuité croissante des mesures (établie au Jalon 63) :
   $$\mu(\liminf A_n) = \mu\left(\bigcup_{N=0}^\infty B_N\right) = \lim_{N \to \infty} \mu(B_N)$$
6. Passons à la limite quand $N \to \infty$ dans l'inégalité de l'étape 4 :
   $$\lim_{N \to \infty} \mu(B_N) \le \lim_{N \to \infty} \inf_{n \ge N} \mu(A_n)$$
7. Le membre de droite est exactement la définition de la limite inférieure d'une suite de réels.
   On obtient donc :
   $$\mu(\liminf A_n) \le \liminf_{n \to \infty} \mu(A_n)$$
   *Ce résultat est un cas particulier du futur Lemme de Fatou, appliqué aux fonctions indicatrices $f_n = \mathbf{1}_{A_n}$.*
