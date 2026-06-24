# Exercice 05
## Énoncé
Soit $E = \mathbb{R}_2[X]$ l'espace vectoriel des polynômes de degré inférieur ou égal à 2.
On considère la base canonique $\mathcal{B} = (1, X, X^2)$.
Soit $\mathcal{B}' = (P_0, P_1, P_2)$ la famille de polynômes définie par :
$P_0(X) = 1$
$P_1(X) = X + 1$
$P_2(X) = (X+1)^2 = X^2 + 2X + 1$

1. Démontrer que $\mathcal{B}'$ est une base de $E$.
2. Déterminer la matrice de passage $P$ de $\mathcal{B}$ à $\mathcal{B}'$.
3. Déterminer la matrice de passage inverse $P^{-1}$.
4. Soit l'endomorphisme $D$ de $E$ défini par $D(P) = P'$ (dérivation formelle).
   Écrire la matrice $A$ de $D$ dans la base canonique $\mathcal{B}$.
5. Écrire la matrice $A'$ de $D$ dans la base $\mathcal{B}'$ en utilisant la formule de changement de base.

## Correction
**1. Démontrer que $\mathcal{B}'$ est une base de $E$ :**
Les degrés des polynômes sont respectivement $\deg(P_0)=0$, $\deg(P_1)=1$, $\deg(P_2)=2$.
Une famille de polynômes non nuls de degrés échelonnés est toujours libre.
Comme la famille $(P_0, P_1, P_2)$ comporte 3 vecteurs et que $\dim(\mathbb{R}_2[X]) = 3$, c'est une base de $E$.

**2. Matrice de passage $P$ :**
On exprime les vecteurs de $\mathcal{B}'$ dans la base $\mathcal{B} = (1, X, X^2)$ :
$P_0(X) = 1 \cdot 1 + 0 \cdot X + 0 \cdot X^2 \implies \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$
$P_1(X) = 1 \cdot 1 + 1 \cdot X + 0 \cdot X^2 \implies \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$
$P_2(X) = 1 \cdot 1 + 2 \cdot X + 1 \cdot X^2 \implies \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$

La matrice de passage est constituée de ces vecteurs colonnes :
$P = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$.

**3. Matrice inverse $P^{-1}$ :**
Pour inverser la matrice, on peut résoudre le système $Y = P X \iff X = P^{-1} Y$. Cela revient à exprimer les vecteurs de $\mathcal{B}$ en fonction de ceux de $\mathcal{B}'$.
$1 = P_0$
$X = P_1 - 1 = P_1 - P_0$
$X^2 = P_2 - 2X - 1 = P_2 - 2(P_1 - P_0) - P_0 = P_2 - 2P_1 + 2P_0 - P_0 = P_2 - 2P_1 + P_0$
On peut lire directement les coefficients sur les colonnes de $P^{-1}$ :
$P^{-1} = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}$.
*Vérification :* $\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3$.

**4. Matrice $A$ de $D$ dans $\mathcal{B}$ :**
$D(1) = 0 = 0 \cdot 1 + 0 \cdot X + 0 \cdot X^2$
$D(X) = 1 = 1 \cdot 1 + 0 \cdot X + 0 \cdot X^2$
$D(X^2) = 2X = 0 \cdot 1 + 2 \cdot X + 0 \cdot X^2$
Donc $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$.

**5. Matrice $A'$ de $D$ dans $\mathcal{B}'$ :**
D'après la formule de changement de base pour un endomorphisme : $A' = P^{-1} A P$.
Calculons d'abord $AP$ :
$AP = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$.
Maintenant calculons $P^{-1}(AP)$ :
$A' = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}$.
On remarque que $A' = A$. Ce résultat pouvait être prévu car $D(P_0) = 0$, $D(P_1) = 1 = P_0$, et $D(P_2) = 2(X+1) = 2P_1$.
