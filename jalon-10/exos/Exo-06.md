# Exercice 06
## Énoncé
Soit $E$ un espace vectoriel de dimension 3 rapporté à une base $\mathcal{B} = (e_1, e_2, e_3)$.
Soit $f$ l'endomorphisme de $E$ dont la matrice dans la base $\mathcal{B}$ est :
$A = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix}$

1. On pose $u = e_1 + e_2 + e_3$. Calculer $f(u)$.
2. On pose $v = e_1 - e_2$ et $w = e_1 - e_3$. Calculer $f(v)$ et $f(w)$.
3. Montrer que $\mathcal{B}' = (u, v, w)$ est une base de $E$.
4. Écrire la matrice de passage $P$ de $\mathcal{B}$ à $\mathcal{B}'$.
5. Donner la matrice $A'$ de $f$ dans la base $\mathcal{B}'$ sans calculer $P^{-1}$.

## Correction
**1. Calcul de $f(u)$ :**
La colonne des coordonnées de $u$ dans $\mathcal{B}$ est $X = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$.
La matrice colonne de $f(u)$ est :
$AX = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2-1-1 \\ -1+2-1 \\ -1-1+2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$.
Donc $f(u) = 0_E$.

**2. Calcul de $f(v)$ et $f(w)$ :**
La colonne des coordonnées de $v$ dans $\mathcal{B}$ est $Y = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$.
$AY = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2-(-1)-0 \\ -1-2-0 \\ -1-(-1)-0 \end{pmatrix} = \begin{pmatrix} 3 \\ -3 \\ 0 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$.
Donc $f(v) = 3v$.

La colonne des coordonnées de $w$ dans $\mathcal{B}$ est $Z = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$.
$AZ = \begin{pmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 2-0-(-1) \\ -1-0-(-1) \\ -1-0-2 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ -3 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$.
Donc $f(w) = 3w$.

**3. Montrer que $\mathcal{B}'$ est une base de $E$ :**
Il s'agit de montrer que la famille $(u, v, w)$ est libre. Soient $\lambda_1, \lambda_2, \lambda_3 \in \mathbb{R}$ tels que $\lambda_1 u + \lambda_2 v + \lambda_3 w = 0_E$.
On remplace $u, v, w$ par leurs expressions en fonction de $e_1, e_2, e_3$ :
$\lambda_1(e_1+e_2+e_3) + \lambda_2(e_1-e_2) + \lambda_3(e_1-e_3) = 0_E$
$(\lambda_1+\lambda_2+\lambda_3)e_1 + (\lambda_1-\lambda_2)e_2 + (\lambda_1-\lambda_3)e_3 = 0_E$.
Comme $(e_1, e_2, e_3)$ est une base, c'est une famille libre. On obtient le système :
$\begin{cases} \lambda_1 + \lambda_2 + \lambda_3 = 0 \\ \lambda_1 - \lambda_2 = 0 \\ \lambda_1 - \lambda_3 = 0 \end{cases}$
De la 2e et 3e équation, on tire $\lambda_2 = \lambda_1$ et $\lambda_3 = \lambda_1$.
En remplaçant dans la 1ère : $\lambda_1 + \lambda_1 + \lambda_1 = 0 \implies 3\lambda_1 = 0 \implies \lambda_1 = 0$.
D'où $\lambda_2 = 0$ et $\lambda_3 = 0$.
La famille $(u, v, w)$ est libre. Étant de cardinal 3 dans un espace de dimension 3, c'est une base.

**4. Matrice de passage $P$ :**
Les colonnes de $P$ sont les coordonnées de $u, v, w$ exprimées dans la base $(e_1, e_2, e_3)$ :
$P = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 0 & -1 \end{pmatrix}$.

**5. Matrice $A'$ de $f$ dans $\mathcal{B}'$ :**
La matrice $A'$ représente l'endomorphisme $f$ dans la base $\mathcal{B}' = (u, v, w)$.
Ses colonnes sont les coordonnées de $f(u), f(v), f(w)$ exprimées dans la base $(u, v, w)$.
D'après les questions 1 et 2, on a :
$f(u) = 0_E = 0\cdot u + 0\cdot v + 0\cdot w$
$f(v) = 3v = 0\cdot u + 3\cdot v + 0\cdot w$
$f(w) = 3w = 0\cdot u + 0\cdot v + 3\cdot w$
Ainsi, la matrice s'écrit directement :
$A' = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix}$.
Cette méthode est bien plus rapide que de calculer explicitement $P^{-1} A P$.
