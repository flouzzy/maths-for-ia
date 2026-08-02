# Exercice 08 : Décomposition d'un noyau itéré et stabilité (⭐⭐⭐⭐)

## Énoncé
Soit $E$ un espace vectoriel de dimension finie, et $u \in \mathcal{L}(E)$ nilpotent d'indice $p$.
Pour $1 \le k \le p$, on définit les sous-espaces $N_k = \ker(u^k)$ et $I_k = \text{Im}(u^k)$.
1. Montrer que $E = N_p$.
2. Démontrer que $u(N_{k}) \subseteq N_{k-1}$ pour tout $1 \le k \le p$.
3. Démontrer que si $F$ est un sous-espace vectoriel de $E$ supplémentaire de $N_{p-1}$ dans $N_p$ (soit $N_p = N_{p-1} \oplus F$), alors l'application restreinte $u : F \to u(F)$ est un isomorphisme.
4. En déduire que $u(F) \cap N_{p-2} = \{0_E\}$.

## Corrigé Rigoureux : Démonstration Complète

### 1. $E = N_p$
Par définition de l'indice de nilpotence, $p$ est l'entier tel que $u^p = 0_{\mathcal{L}(E)}$.
Pour tout $x \in E$, on a $u^p(x) = 0_E$.
Donc par définition du noyau, $x \in \ker(u^p) = N_p$. Ainsi $E \subseteq N_p$.
Comme $N_p \subseteq E$ trivialement, $E = N_p$.

### 2. Stabilité descendante
Soit $k \in \{1, \dots, p\}$. Soit $y \in u(N_k)$.
Par définition de l'image directe, il existe $x \in N_k$ tel que $y = u(x)$.
Comme $x \in N_k$, on a $u^k(x) = 0_E$.
Calculons l'action de $u^{k-1}$ sur $y$ :
$u^{k-1}(y) = u^{k-1}(u(x)) = u^k(x) = 0_E$.
Donc par définition, $y \in \ker(u^{k-1}) = N_{k-1}$.
L'inclusion $u(N_k) \subseteq N_{k-1}$ est démontrée.

### 3. Isomorphisme de restriction
Soit $F$ tel que $N_p = N_{p-1} \oplus F$.
L'application $u_F : F \to u(F)$ définie par $x \mapsto u(x)$ est trivialement surjective par définition de son espace d'arrivée.
Montrons qu'elle est injective. Soit $x \in F$ tel que $u_F(x) = 0_E$.
Alors $u(x) = 0_E$, ce qui implique $x \in \ker(u) = N_1$.
Comme $p \ge 1$, et sachant que la suite des noyaux est croissante, on a $N_1 \subseteq N_{p-1}$.
Donc $x \in N_{p-1}$.
Or $x$ appartient aussi à $F$. Donc $x \in N_{p-1} \cap F$.
Par définition de la somme directe $N_{p-1} \oplus F$, l'intersection est réduite à $\{0_E\}$.
Donc $x = 0_E$.
L'application $u_F$ est linéaire, surjective et injective, c'est donc un isomorphisme d'espaces vectoriels. On en déduit notamment que $\dim(u(F)) = \dim(F)$.

### 4. Intersection avec $N_{p-2}$
Soit $y \in u(F) \cap N_{p-2}$.
Puisque $y \in u(F)$, il existe un unique $x \in F$ tel que $y = u(x)$.
Puisque $y \in N_{p-2}$, on a $u^{p-2}(y) = 0_E$.
Remplaçons $y$ : $u^{p-2}(u(x)) = 0_E$, c'est-à-dire $u^{p-1}(x) = 0_E$.
Cela signifie que $x \in \ker(u^{p-1}) = N_{p-1}$.
Or, nous savons que $x \in F$.
Donc $x \in N_{p-1} \cap F = \{0_E\}$ par la somme directe.
Ainsi, $x = 0_E$, ce qui implique $y = u(0_E) = 0_E$.
L'intersection est donc bien réduite au vecteur nul : $u(F) \cap N_{p-2} = \{0_E\}$.
*(Ce résultat est fondamental pour construire la base de Jordan "du haut vers le bas").*
