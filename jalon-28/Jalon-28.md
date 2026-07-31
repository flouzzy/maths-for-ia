---
uuid: "jalon-28"
title: "Polynômes d'endomorphismes, idéaux annulateurs et théorème de Cayley-Hamilton"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/reduction-endomorphismes
prev: "[[Jalon 27 (Endomorphismes symétriques).md]]"
next: "[[Jalon 29 (Éléments propres).md]]"
---
# Jalon 28 : Polynômes d'endomorphismes, idéaux annulateurs et théorème de Cayley-Hamilton

## 1. Introduction

La réduction des endomorphismes constitue l'un des piliers centraux de l'algèbre linéaire, et sa formalisation repose intimement sur la théorie des polynômes. Pour comprendre pourquoi les mathématiciens ont eu besoin d'introduire la notion de "polynôme d'endomorphisme", il faut se replonger dans les problèmes de dynamique et de calcul itératif du XIXe siècle.

Lorsqu'on étudie un système dynamique discret, modélisé par une relation de récurrence linéaire vectorielle $X_{n+1} = A X_n$ (où $A$ est une matrice carrée), la prédiction de l'état du système à l'instant $n$ requiert le calcul de $A^n$. Pour des matrices de grande taille, le calcul direct de $A^n$ par multiplications successives est numériquement instable et astronomiquement coûteux en termes de complexité. Les mathématiciens comme Arthur Cayley et William Rowan Hamilton se sont alors posé une question vertigineuse : existe-t-il une relation intrinsèque liant les différentes puissances d'une même matrice (ou d'un même endomorphisme) entre elles ? Autrement dit, peut-on exprimer $A^n$ comme une combinaison linéaire de puissances strictement inférieures ?

L'intuition géniale a consisté à jeter un pont entre deux mondes algébriques a priori distincts : l'anneau des polynômes $\mathbb{K}[X]$ (construit sur une indéterminée formelle $X$) et l'algèbre des endomorphismes $\mathcal{L}(E)$ (ou l'algèbre des matrices $\mathcal{M}_n(\mathbb{K})$). Si l'on peut "évaluer" un polynôme scalaire $P(X) = a_0 + a_1 X + a_2 X^2$ en substituant $X$ par un scalaire $x \in \mathbb{K}$, ne pourrait-on pas évaluer ce même polynôme en substituant $X$ par un endomorphisme $u \in \mathcal{L}(E)$ ?

Cette substitution, $P(u) = a_0 \text{id}_E + a_1 u + a_2 u^2$, dote l'espace vectoriel d'une structure de $\mathbb{K}[X]$-module. Dès lors, la recherche de relations de dépendance linéaire entre les puissances de $u$ se traduit par la recherche des polynômes $P$ tels que $P(u) = 0_{\mathcal{L}(E)}$. L'ensemble de ces "polynômes annulateurs" forme un idéal de $\mathbb{K}[X]$. Puisque $\mathbb{K}[X]$ est un anneau principal, cet idéal est engendré par un unique polynôme unitaire : le **polynôme minimal**.

Le point d'orgue de cette théorie est le célèbre **Théorème de Cayley-Hamilton**, qui affirme que le polynôme caractéristique d'un endomorphisme est toujours un polynôme annulateur. Historiquement, ce résultat a d'abord été vérifié empiriquement par Hamilton pour les matrices $2 \times 2$ et $3 \times 3$ issues de ses travaux sur les quaternions, puis conjecturé pour la dimension $n$ par Cayley en 1858, qui écrivit : *« Je n'ai pas cru nécessaire d'entreprendre une démonstration formelle du théorème dans le cas général d'une matrice de degré quelconque. »* La démonstration rigoureuse fut apportée plus tard par Frobenius. Ce théorème est d'une profondeur inouïe : il affirme que l'ADN spectral de la matrice (son polynôme caractéristique) contient en lui-même la clé pour annihiler l'opérateur tout entier.

## 2. Protocole d'Exégèse Conceptuelle et Formalisation

Dans toute cette section, on désigne par $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$), $E$ un $\mathbb{K}$-espace vectoriel, et $u \in \mathcal{L}(E)$ un endomorphisme de $E$. On note $\mathbb{K}[X]$ l'anneau des polynômes à coefficients dans $\mathbb{K}$.

### 2.1 Polynômes d'endomorphismes et morphismes d'évaluation

#### A. Énoncé Symbolique Strict
Soit $P \in \mathbb{K}[X]$ un polynôme tel que $P(X) = \sum_{k=0}^d a_k X^k$. On définit l'endomorphisme $P(u) \in \mathcal{L}(E)$ par :
$$P(u) = \sum_{k=0}^d a_k u^k$$
avec la convention $u^0 = \text{id}_E$.

L'application d'évaluation $\Phi_u : \mathbb{K}[X] \to \mathcal{L}(E)$ définie par $\Phi_u(P) = P(u)$ est un morphisme d'algèbres.


\begin{tikzpicture}[scale=1.5, auto, >=stealth']
    \node (KX) at (0, 2) {$\mathbb{K}[X]$};
    \node (LE) at (3, 2) {$\mathcal{L}(E)$};
    \node (K) at (1.5, 0) {$\mathbb{K}$};
    \draw[->, thick] (KX) -- node[above] {$\Phi_u$} (LE);
    \draw[->, dashed, thick] (KX) -- node[below left] {$\text{évaluation en } \lambda$} (K);
    \draw[->, dashed, thick] (K) -- node[below right] {$\lambda \mapsto \lambda \text{id}_E$} (LE);
\end{tikzpicture}


#### B. Anatomie et Typage Chirurgical
- $P \in \mathbb{K}[X]$ : $P$ est un objet algébrique abstrait, une suite de coefficients $(a_k)_{k \in \mathbb{N}}$ presque nulle.
- $u \in \mathcal{L}(E)$ : Un opérateur linéaire agissant sur les vecteurs de $E$.
- $u^k \in \mathcal{L}(E)$ : Désigne la composition itérée de $u$ avec lui-même $k$ fois ($u \circ u \circ \dots \circ u$). Ce n'est en aucun cas le produit scalaire ou vectoriel. L'opération sous-jacente est la composition des applications.
- $P(u) \in \mathcal{L}(E)$ : C'est un nouvel endomorphisme, obtenu par combinaison linéaire des itérés de $u$.
- $\Phi_u$ : Morphisme d'algèbres signifie qu'il préserve l'addition ($\Phi_u(P+Q) = \Phi_u(P) + \Phi_u(Q)$), la multiplication par un scalaire ($\Phi_u(\lambda P) = \lambda \Phi_u(P)$) et surtout le produit polynômial : $\Phi_u(PQ) = \Phi_u(P) \circ \Phi_u(Q) = P(u) \circ Q(u)$.

**Corollaire fondamental :** L'anneau $\mathbb{K}[X]$ étant commutatif, on en déduit que pour tous polynômes $P, Q \in \mathbb{K}[X]$, les endomorphismes $P(u)$ et $Q(u)$ commutent : $P(u) \circ Q(u) = Q(u) \circ P(u)$. En particulier, $P(u)$ commute avec $u$.

#### C. Exemples de Validation
- **Exemple trivial :** Soit $P(X) = X^2 - 2X + 3$. Pour un endomorphisme $u$, $P(u) = u^2 - 2u + 3\text{id}_E$. Si $u = \text{id}_E$, alors $P(\text{id}_E) = \text{id}_E - 2\text{id}_E + 3\text{id}_E = 2\text{id}_E$.
- **Exemple matriciel :** Soit $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \in \mathcal{M}_2(\mathbb{R})$ (une symétrie) et $P(X) = X^2 - 1$. Alors $P(A) = A^2 - I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0_{\mathcal{M}_2(\mathbb{R})}$.

#### D. Cas Pathologiques
- **Erreur de typage fatale :** Écrire $P(u) = a_0 + a_1 u + a_2 u^2$. C'est syntaxiquement incorrect en algèbre, car on additionne un scalaire $a_0$ avec des endomorphismes. Il faut impérativement écrire $a_0 \text{id}_E$ ou, en version matricielle, $a_0 I_n$.

### 2.2 Idéal annulateur et polynôme minimal

#### A. Énoncé Symbolique Strict
On appelle **idéal annulateur** de $u$, noté $\mathcal{I}_u$, le noyau du morphisme d'évaluation $\Phi_u$ :
$$\mathcal{I}_u = \{ P \in \mathbb{K}[X] \mid P(u) = 0_{\mathcal{L}(E)} \}$$

Si $E$ est de dimension finie $n \ge 1$, alors $\mathcal{I}_u \neq \{0\}$. De plus, $\mathbb{K}[X]$ étant un anneau principal, il existe un unique polynôme unitaire $\pi_u$ engendrant $\mathcal{I}_u$. On l'appelle le **polynôme minimal** de $u$ :
$$\mathcal{I}_u = \pi_u \mathbb{K}[X] = \{ \pi_u Q \mid Q \in \mathbb{K}[X] \}$$

#### B. Anatomie et Typage Chirurgical
- $\mathcal{I}_u \subset \mathbb{K}[X]$ : C'est un ensemble de polynômes. Par définition du noyau, c'est un sous-espace vectoriel de $\mathbb{K}[X]$, absorbant pour le produit ($P \in \mathcal{I}_u, Q \in \mathbb{K}[X] \implies PQ \in \mathcal{I}_u$).
- $0_{\mathcal{L}(E)}$ : L'endomorphisme nul, qui à tout vecteur associe $0_E$.
- Dimension finie : Si $\dim E = n$, la dimension de $\mathcal{L}(E)$ est $n^2$. La famille $(\text{id}_E, u, u^2, \dots, u^{n^2})$ comporte $n^2 + 1$ vecteurs dans un espace de dimension $n^2$. Elle est donc nécessairement liée. Il existe ainsi une combinaison linéaire non triviale nulle, ce qui fournit un polynôme annulateur non nul, prouvant que $\mathcal{I}_u \neq \{0\}$.
- Polynôme unitaire : Un polynôme dont le coefficient dominant est 1. Cette restriction garantit l'unicité du générateur de l'idéal.
- $\pi_u$ divise tout polynôme annulateur de $u$. C'est le polynôme annulateur non nul de plus bas degré.

#### C. Exemples de Validation
- **Projecteurs :** Soit $p$ un projecteur non trivial ($p \neq 0, p \neq \text{id}$). Par définition, $p^2 = p$, donc $p^2 - p = 0$. Le polynôme $P(X) = X^2 - X = X(X-1)$ est annulateur. Le polynôme minimal $\pi_p$ divise $X(X-1)$. Comme $p$ n'est ni l'identité ni l'application nulle, $\pi_p(X)$ ne peut être ni $X$ ni $X-1$. Donc $\pi_p(X) = X^2 - X$.
- **Symétries :** Soit $s$ une symétrie non triviale. $s^2 = \text{id}_E$, donc $X^2 - 1$ est annulateur. $\pi_s(X) = X^2 - 1$.

#### D. Cas Pathologiques
- **Dimension infinie :** Si $E = \mathbb{K}[X]$ et que $u$ est l'endomorphisme de dérivation $P \mapsto P'$, alors $u$ est nilpotent sur le sous-espace des polynômes de degré $\le n$ (ici $u^{n+1} = 0$), mais n'admet **aucun** polynôme annulateur non nul sur $E$ entier. L'idéal annulateur est réduit à $\{0\}$, et le polynôme minimal n'est pas défini (ou est par convention $0$).

### 2.3 Le Théorème de Cayley-Hamilton

#### A. Énoncé Symbolique Strict
Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n$. Soit $u \in \mathcal{L}(E)$.
On note $\chi_u(X) = \det(X \text{id}_E - u)$ le polynôme caractéristique de $u$.
Le théorème de Cayley-Hamilton affirme que $\chi_u$ est un polynôme annulateur de $u$ :
$$\chi_u(u) = 0_{\mathcal{L}(E)}$$
Autrement dit, $\chi_u \in \mathcal{I}_u$, ce qui équivaut à affirmer que le polynôme minimal $\pi_u$ divise le polynôme caractéristique $\chi_u$.

#### B. Anatomie et Typage Chirurgical
- $\chi_u(X)$ : Polynôme unitaire de degré $n$, de la forme $X^n - \text{Tr}(u)X^{n-1} + \dots + (-1)^n \det(u)$.
- $\chi_u(u) = 0$ : Cela signifie que si l'on effectue la composition $u^n - \text{Tr}(u)u^{n-1} + \dots + (-1)^n \det(u)\text{id}_E$, l'opérateur résultant est l'opérateur nul.
- Attention suprême à la substitution de $X$ par $u$ dans la formule du déterminant : l'expression $\det(u \text{id}_E - u) = \det(0) = 0$ est un **non-sens algébrique**. La fonction déterminant prend en argument une matrice à coefficients dans un anneau commutatif, et retourne un élément de cet anneau. L'expression $X \text{id}_E - u$ a des coefficients dans $\mathbb{K}[X]$. Substituer formellement l'indéterminée scalaire $X$ par l'opérateur $u$ *à l'intérieur* du déterminant n'a pas de sens mathématique (car $\mathcal{L}(E)$ n'est pas commutatif en général). L'évaluation se fait *après* le calcul formel du polynôme $\chi_u$.

## 3. Zéro Ellipse : Preuve du Théorème de Cayley-Hamilton

La preuve matricielle reposant sur la comatrice est canonique. Soit $A \in \mathcal{M}_n(\mathbb{K})$ une matrice carrée. Nous allons prouver que $\chi_A(A) = 0_{n}$.

Considérons la matrice à coefficients dans l'anneau des polynômes $\mathbb{K}[X]$, définie par :
$$M(X) = X I_n - A \in \mathcal{M}_n(\mathbb{K}[X])$$

Son déterminant est, par définition, le polynôme caractéristique :
$$\det(M(X)) = \chi_A(X)$$

Soit $\widetilde{M}(X)$ la transposée de la comatrice de $M(X)$, communément appelée matrice adjointe (classique). La relation fondamentale liant une matrice et sa comatrice est valide pour toute matrice à coefficients dans un anneau commutatif (ici $\mathbb{K}[X]$) :
$$M(X) \widetilde{M}(X) = \det(M(X)) I_n = \chi_A(X) I_n \quad \text{(*)}$$

Les coefficients de $\widetilde{M}(X)$ sont des déterminants de sous-matrices de taille $(n-1) \times (n-1)$ de $M(X)$. Les coefficients de $M(X)$ étant des polynômes de degré au plus 1, les coefficients de $\widetilde{M}(X)$ sont des polynômes de degré au plus $n-1$.
Nous pouvons donc exprimer $\widetilde{M}(X)$ comme un polynôme à coefficients matriciels. Il existe des matrices $B_0, B_1, \dots, B_{n-1} \in \mathcal{M}_n(\mathbb{K})$ telles que :
$$\widetilde{M}(X) = \sum_{k=0}^{n-1} B_k X^k = B_0 + B_1 X + \dots + B_{n-1} X^{n-1}$$

Écrivons formellement le polynôme caractéristique :
$$\chi_A(X) = a_0 + a_1 X + \dots + a_n X^n \quad (\text{avec } a_n = 1)$$

Substituons ces expressions de $\widetilde{M}(X)$ et de $\chi_A(X)$ dans la relation fondamentale (*) :
$$(X I_n - A) \left( \sum_{k=0}^{n-1} B_k X^k \right) = \left( \sum_{k=0}^n a_k X^k \right) I_n$$

Développons le membre de gauche de cette identité entre polynômes à coefficients matriciels :
$$X I_n \left( \sum_{k=0}^{n-1} B_k X^k \right) - A \left( \sum_{k=0}^{n-1} B_k X^k \right) = \sum_{k=0}^{n-1} B_k X^{k+1} - \sum_{k=0}^{n-1} A B_k X^k$$

Opérons un changement d'indice dans la première somme en posant $j = k+1$ (donc $k = j-1$) :
$$ \sum_{j=1}^n B_{j-1} X^j - \sum_{k=0}^{n-1} A B_k X^k $$

Réindexons la seconde somme avec $j$ :
$$ \sum_{j=1}^n B_{j-1} X^j - \sum_{j=0}^{n-1} A B_j X^j $$

Regroupons les termes de même puissance $X^j$ de part et d'autre de l'égalité. L'égalité polynomiale donne par identification des coefficients :
- Pour le degré 0 : $-A B_0 = a_0 I_n$
- Pour les degrés $1 \le j \le n-1$ : $B_{j-1} - A B_j = a_j I_n$
- Pour le degré $n$ : $B_{n-1} = a_n I_n$

Nous allons multiplier chacune de ces équations matricielles à gauche par $A^j$ :
- Pour $j=0$ : $A^0 (-A B_0) = a_0 A^0 \implies -A B_0 = a_0 I_n$
- Pour $1 \le j \le n-1$ : $A^j (B_{j-1} - A B_j) = a_j A^j \implies A^j B_{j-1} - A^{j+1} B_j = a_j A^j$
- Pour $j=n$ : $A^n B_{n-1} = a_n A^n$

Sommons toutes ces identités de $j=0$ à $j=n$ :
$$\sum_{j=0}^n a_j A^j = (-A B_0) + \sum_{j=1}^{n-1} (A^j B_{j-1} - A^{j+1} B_j) + A^n B_{n-1}$$

La somme du membre de droite est télescopique. Développons ses premiers termes pour l'observer :
$$-A B_0 + (A B_0 - A^2 B_1) + (A^2 B_1 - A^3 B_2) + \dots + (A^{n-1} B_{n-2} - A^n B_{n-1}) + A^n B_{n-1}$$

L'annulation en cascade de tous les termes successifs donne rigoureusement la matrice nulle :
$$\sum_{j=0}^n a_j A^j = 0_n$$

Or, le membre de gauche est par définition $\chi_A(A)$. Nous avons donc rigoureusement démontré que :
$$\chi_A(A) = 0_n$$
Ce qui achève la démonstration du théorème de Cayley-Hamilton. $\blacksquare$
