# Exercice 3 : $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $E = \ell^2(\mathbb{N})$ l'espace des suites de carré sommable.
Considérons l'ensemble $A = \{ u = (u_n)_{n \in \mathbb{N}} \in \ell^2 \mid \forall n, u_n \ge 0, \sum_{n=0}^{\infty} (n+1)u_n^2 \le 1 \}$.
Considérons $B = \{ u \in \ell^2 \mid \forall n, u_n = -1/2^{n+1} \}$. $B$ est réduit à un point $b$.
Montrer que $A$ et $B$ peuvent être séparés strictement.

## Correction

**Étape 1 : Propriétés de A**
$A$ est l'intersection de demi-espaces fermés $u_n \ge 0$ et de l'ellipsoïde de Hilbert $\sum (n+1)u_n^2 \le 1$.
$A$ est convexe car intersection de convexes.
$A$ est fermé car la fonctionnelle $u \mapsto \sum (n+1)u_n^2$ est semi-continue inférieurement (par le lemme de Fatou sur les sommes) et $u_n \ge 0$ sont des conditions fermées.

**Étape 2 : Propriétés de B et disjonction**
$B = \{b\}$ avec $b_n = -1/2^{n+1} < 0$. $B$ est compact (singleton) et convexe.
Puisque tous les éléments $a \in A$ ont $a_n \ge 0$, on a $a \neq b$. Donc $A \cap B = \emptyset$.

**Étape 3 : Application de Hahn-Banach**
L'espace $E = \ell^2$ est un Hilbert, donc un Banach.
$A$ est convexe fermé, $B$ convexe compact, et ils sont disjoints.
Par le théorème de Hahn-Banach (forme stricte), ils peuvent être séparés strictement par un hyperplan affine fermé. $\blacksquare$
