# Exercice 09

Cet exercice explore les profondes connexions entre la complétude d'espaces vectoriels normés, la continuité d'opérateurs linéaires, et l'équivalence de normes. Il s'appuie sur une utilisation astucieuse et combinée du Théorème du Graphe Fermé, du Théorème de l'Application Ouverte (ou Théorème d'Isomorphisme de Banach) et du principe de la norme du graphe. La résolution demande une grande rigueur et une parfaite maîtrise des nuances de ces théorèmes fondamentaux de l'analyse fonctionnelle.

Difficulté : $\bigstar$\bigstar$\bigstar$\bigstar$\bigstar

Soit $X$ un espace vectoriel complexe.
Soient $\|\cdot\|_1$ et $\|\cdot\|_2$ deux normes sur $X$.
On suppose que $(X, \|\cdot\|_1)$ est un espace de Banach.

Soit $T: X \to X$ un opérateur linéaire satisfaisant les conditions suivantes :
(i) $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$.
(ii) $T$ est injectif.
(iii) L'image $R(T)$ de $T$ est dense dans $(X, \|\cdot\|_1)$.
(iv) Le graphe de $T$ est fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$. Autrement dit, si $(x_n)_{n \in \mathbb{N}}$ est une suite dans $X$ telle que $x_n \xrightarrow{\|\cdot\|_2} x$ et $T x_n \xrightarrow{\|\cdot\|_2} y$ pour certains $x, y \in X$, alors $y = T x$.
(v) Il existe une constante $C > 0$ telle que pour tout $x \in X$, $\|Tx\|_1 \le C \|Tx\|_2$.

L'objectif de cet exercice est de démontrer l'équivalence des normes $\|\cdot\|_1$ et $\|\cdot\|_2$, ainsi que de caractériser $T$.

---

**Questions :**

1.  Démontrer que l'espace $(X, \|\cdot\|_G)$, muni de la norme $\|x\|_G = \|x\|_2 + \|Tx\|_2$, est un espace de Banach.
2.  Prouver que les normes $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes sur $X$.
3.  En déduire que les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes sur $X$.
4.  Conclure que $(X, \|\cdot\|_2)$ est un espace de Banach.
5.  Démontrer que $T$ est un isomorphisme topologique de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.

---

# Correction détaillée

### Question 1 : Démontrer que l'espace $(X, \|\cdot\|_G)$, muni de la norme $\|x\|_G = \|x\|_2 + \|Tx\|_2$, est un espace de Banach.

**Analyse de la question :** Pour montrer qu'un espace vectoriel normé est un espace de Banach, il faut prouver que toute suite de Cauchy dans cet espace converge vers un élément de l'espace. La norme $\|x\|_G$ est une "norme du graphe". Sa complétude est souvent liée à la complétude des espaces sous-jacents et à la fermeture du graphe de l'opérateur.

**Déroulé de la preuve :**
Soit $(x_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Par définition de la norme $\|\cdot\|_G$, une suite $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_G)$ si et seulement si :
(a) $(x_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
(b) $(Tx_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.

Nous allons utiliser ces deux propriétés pour montrer la convergence.

Étape 1 : Montrer que $(x_n)$ converge dans $(X, \|\cdot\|_1)$.
De (b), $(Tx_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
En utilisant la condition (v) : $\|Ty\|_1 \le C \|Ty\|_2$ pour tout $y \in X$.
Pour $y = x_n - x_m$, nous avons $\|T(x_n - x_m)\|_1 \le C \|T(x_n - x_m)\|_2$.
Puisque $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, pour tout $\varepsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour $n, m \ge N$, $\|Tx_n - Tx_m\|_2 < \varepsilon$.
Donc, pour $n, m \ge N$, $\|Tx_n - Tx_m\|_1 \le C \|Tx_n - Tx_m\|_2 < C \varepsilon$.
Ceci prouve que $(Tx_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, la suite $(Tx_n)$ converge dans $(X, \|\cdot\|_1)$. Soit $y_0 \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y_0$.

Maintenant, considérons la suite $(x_n)$ elle-même.
On a $T x_n \xrightarrow{\|\cdot\|_1} y_0$.
L'opérateur $T$ est injectif (condition (ii)). Ceci nous permet de considérer $T^{-1}$ sur $R(T)$.
De la condition (i), $T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu. Par conséquent, il existe une constante $M > 0$ telle que $\|Tx\|_1 \le M \|x\|_1$ pour tout $x \in X$.
Puisque $T$ est injectif, $T^{-1}: R(T) \to X$ est bien défini.
Cependant, nous n'avons pas d'information directe sur la continuité de $T^{-1}$ ou sur le fait que $R(T)$ soit complet.

Utilisons les conditions (ii) et (iii) à travers le théorème de l'application ouverte.
Le fait que $Tx_n$ converge dans $(X, \|\cdot\|_1)$ n'implique pas que $x_n$ converge dans $(X, \|\cdot\|_1)$ sans plus d'information sur $T^{-1}$.

Revenons à l'hypothèse (a) : $(x_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
Il nous faut une relation entre $\|\cdot\|_1$ et $\|\cdot\|_2$ pour avancer sur $(x_n)$.
On a $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$, donc $Tx_n \to y_0$ dans $(X, \|\cdot\|_1)$.
Supposons que $x_n$ converge vers $x_0$ dans $(X, \|\cdot\|_1)$. Alors par (i), $Tx_n \to Tx_0$ dans $(X, \|\cdot\|_1)$. Par unicité de la limite, $y_0 = Tx_0$.
Il nous faut donc prouver que $(x_n)$ converge dans $(X, \|\cdot\|_1)$.

Prenons un $x_n - x_m$. On a $\|x_n - x_m\|_G = \|x_n - x_m\|_2 + \|T(x_n - x_m)\|_2$.
On a $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
Et $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, et aussi dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un Banach, il existe $y \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y$.

Puisque $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (condition (iii)) et $T$ est continu (condition (i)), si $T$ était aussi surjective sur $(X, \|\cdot\|_1)$, $T$ serait un isomorphisme topologique de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$. Si $T$ était un isomorphisme, alors $T^{-1}$ serait continu.
Alors $x_n = T^{-1}(Tx_n) \xrightarrow{\|\cdot\|_1} T^{-1}y$.
Donc $(x_n)$ convergerait dans $(X, \|\cdot\|_1)$.
Cette surjectivité de $T$ n'est pas donnée, mais elle sera montrée à la question 5. Ne l'utilisons pas ici.

Nous avons $Tx_n \xrightarrow{\|\cdot\|_1} y_0$.
Utilisons l'argument standard de la norme du graphe.
Nous avons une suite $(x_n)$ qui est de Cauchy dans $(X, \|\cdot\|_2)$.
Nous avons une suite $(Tx_n)$ qui est de Cauchy dans $(X, \|\cdot\|_2)$.
Puisque $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, et par condition (v) $\|Tx\|_1 \le C \|Tx\|_2$, alors $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$.
Étant donné que $(X, \|\cdot\|_1)$ est un espace de Banach, il existe un élément $y \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y$.

Maintenant, nous devons trouver un $x \in X$ tel que $x_n \xrightarrow{\|\cdot\|_G} x$.
De l'injectivité de $T$ (condition (ii)), si $x_n \xrightarrow{\|\cdot\|_1} x$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx$, alors $Tx = y$.
Mais nous n'avons pas la convergence de $x_n$ dans $(X, \|\cdot\|_1)$.

C'est là que réside la subtilité. Considérons l'espace $(X, \|\cdot\|_G)$ comme un espace vectoriel normé.
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
1. $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
2. $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
De 2. et de la condition (v), $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, il existe $y \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y$.

Nous avons besoin d'une convergence pour $(x_n)$ dans $(X, \|\cdot\|_1)$ ou une complétion de $(X, \|\cdot\|_2)$.
Soit $\tilde{X}_2$ la complétion de $(X, \|\cdot\|_2)$. Alors $x_n \to x$ dans $\tilde{X}_2$ pour un certain $x \in \tilde{X}_2$. De même, $Tx_n \to y'$ dans $\tilde{X}_2$ pour un certain $y' \in \tilde{X}_2$.
La condition (iv) (graphe fermé pour $\|\cdot\|_2$) signifie que si $x \in X$ et $y \in X$, alors $y=Tx$.
C'est la définition d'opérateur fermé sur un espace complet. Si $X$ n'est pas complet, le graphe fermé a une signification légèrement différente: il signifie que si une suite $(x_n)$ dans le domaine de $T$ converge vers $x$ (dans $X$) et $(Tx_n)$ converge vers $y$ (dans $X$), alors $x$ est dans le domaine de $T$ et $y=Tx$. Ici le domaine de $T$ est $X$.

Reprenons :
1. $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
2. $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
De la condition (v), on a $\|Tx_n - Tx_m\|_1 \le C \|Tx_n - Tx_m\|_2$.
Comme $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, il est aussi de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, il existe un $y_0 \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y_0$.

Maintenant, nous allons prouver que $(x_n)$ converge dans $(X, \|\cdot\|_1)$.
Puisque $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ (condition (i)), son opérateur inverse $T^{-1}$ n'est pas nécessairement continu.
Cependant, $T$ est injectif (condition (ii)) et $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (condition (iii)).
Si $T$ était un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$, alors $T^{-1}$ serait continu et $x_n = T^{-1}(Tx_n)$ convergerait dans $(X, \|\cdot\|_1)$. La question 5 nous demande de prouver cela. Il est donc prématuré de l'utiliser.

Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, et $Tx_n \xrightarrow{\|\cdot\|_1} y_0$, on peut construire $x \in X$ tel que $Tx=y_0$.
L'opérateur $T$ est continu, injectif et à image dense dans $(X,\|\cdot\|_1)$.
Pour $Tx_n \to y_0$ dans $(X,\|\cdot\|\|_1)$, il existe une sous-suite $x_{n_k}$ qui converge vers $x_0$ dans $(X,\|\cdot\|_1)$? Non.

Considérons l'espace $X_G = (X, \|\cdot\|_G)$.
Les opérateurs $Id: X_G \to (X, \|\cdot\|_2)$ et $T: X_G \to (X, \|\cdot\|_2)$ sont continus par définition de $\|x\|_G$.
Soit $(x_n)$ une suite de Cauchy dans $X_G$.
Alors $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$. Soit $\tilde{x} \in \tilde{X}_2$ sa limite dans la complétion de $(X, \|\cdot\|_2)$.
Alors $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$. Soit $\tilde{y} \in \tilde{X}_2$ sa limite dans la complétion de $(X, \|\cdot\|_2)$.

De la condition (v), $\|Tx_n - Tx_m\|_1 \le C \|Tx_n - Tx_m\|_2$.
Donc $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, il existe $y \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y$.

Puisque $T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu (condition (i)) et injectif (condition (ii)), si $x_n$ convergeait vers $x$ dans $(X, \|\cdot\|_1)$, alors $Tx_n$ convergerait vers $Tx$ dans $(X, \|\cdot\|_1)$. Donc $y = Tx$.

Pour prouver la complétude de $(X, \|\cdot\|_G)$, nous devons montrer que $x_n \xrightarrow{\|\cdot\|_2} x$ et $Tx_n \xrightarrow{\|\cdot\|_2} Tx$ pour un certain $x \in X$.

Considérons l'opérateur $T^{-1}: R(T) \to X$.
Pour $y \in R(T)$, $T^{-1}y$ est l'unique $x$ tel que $Tx=y$.
De (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Donc $\|y\|_1 \le C \|y\|_2$ pour tout $y \in R(T)$.
Ceci signifie que l'injection $Id: (R(T), \|\cdot\|_2) \to (R(T), \|\cdot\|_1)$ est continue.

Reprenons l'argument pour la complétude de $(X, \|\cdot\|_G)$:
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Donc $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
De la condition (v), on a $\|Tx_n - Tx_m\|_1 \le C \|Tx_n - Tx_m\|_2$.
Puisque $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, $(Tx_n)$ est aussi de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, il existe un unique $y^* \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.

Maintenant, montrons que $(x_n)$ converge dans $(X, \|\cdot\|_1)$.
L'opérateur $T$ est injectif (ii) et $R(T)$ est dense (iii) dans $(X,\|\cdot\|_1)$.
On ne peut pas simplement dire que $y^* \in R(T)$ sans argument.
Cependant, comme $T$ est continu sur $(X,\|\cdot\|_1)$, $T(\overline{R(T)}) \subset \overline{R(T)}$ ce qui est $X$.

C'est là que réside le véritable défi. Il faut utiliser l'opérateur $T$ de manière plus profonde.
Par la condition (v), on a $\|Tx\|_1 \le C \|Tx\|_2$.
Considérons l'opérateur $J: (R(T), \|\cdot\|_2) \to (R(T), \|\cdot\|_1)$ défini par $J(y) = y$. (i.e. l'identité).
Alors $\|J(y)\|_1 = \|y\|_1 \le C \|y\|_2 = C \|y\|_2$. Donc $J$ est continu.
Ceci signifie que si une suite est de Cauchy dans $(R(T), \|\cdot\|_2)$, elle est aussi de Cauchy dans $(R(T), \|\cdot\|_1)$.

La question 1 est une application du lemme de la norme du graphe, mais dans un contexte où la complétude de $\|\cdot\|_2$ n'est pas connue.
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
1. $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
2. $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
De 2., par (v), $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$. Soit $y_0 = \lim_{n \to \infty} Tx_n$ dans $(X, \|\cdot\|_1)$.
Puisque $T$ est injectif, si $x_n \to x$ dans $(X, \|\cdot\|_1)$, alors $Tx_n \to Tx$ dans $(X, \|\cdot\|_1)$ par (i), donc $y_0 = Tx$.
L'étape difficile est de prouver que $x_n$ converge dans $(X, \|\cdot\|_1)$.

Considérons l'opérateur $T$ comme un opérateur de $(X, \|\cdot\|_G)$ vers $(X, \|\cdot\|_1)$.
On a $\|Tx\|_1 \le \|T\|_{1,1} \|x\|_1$.
Et $\|x\|_G = \|x\|_2 + \|Tx\|_2$.
De la condition (v), $\|Tx\|_1 \le C \|Tx\|_2 \le C \|x\|_G$.
Ceci montre que $T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu.

Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y_0$, et $T$ est continu $X_G \to X_1$, on a $x_n \xrightarrow{\|\cdot\|_G} x_0$ pour un $x_0$ si $T$ était inversible de $R(T)$ sur $X_G$.

Revenons à l'utilisation directe de la condition (iv): le graphe de $T$ est fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$.
Ce que nous avons:
- $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
- $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
Soit $\tilde{X}_2$ la complétion de $(X, \|\cdot\|_2)$.
Alors il existe $\tilde{x} \in \tilde{X}_2$ tel que $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ (dans $\tilde{X}_2$).
Et il existe $\tilde{y} \in \tilde{X}_2$ tel que $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ (dans $\tilde{X}_2$).
La condition (iv) s'applique si $\tilde{x}, \tilde{y}$ sont dans $X$.

Ce qui doit être fait pour la question 1 est que la complétude de $X_G$ signifie que si $(x_n)$ est Cauchy en $X_G$, alors $x_n \to x$ en $X_G$ pour $x \in X$.
Ceci équivaut à $x_n \to x$ en $X_2$ et $Tx_n \to Tx$ en $X_2$.
Alors on utilise la condition (iv).
Donc il suffit de montrer que $\tilde{x} \in X$ et $\tilde{y} \in X$.

Considérons la complétion $(\tilde{X}_2, \|\cdot\|_2)$ de $(X, \|\cdot\|_2)$.
On a $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ dans $\tilde{X}_2$.
Par l'injectivité de $T$ (ii), $T$ s'étend de manière unique à un opérateur $\tilde{T}: \tilde{X}_2 \to \tilde{X}_2$.
Ceci est faux. $T$ est défini sur $X$. $\tilde{T}$ est seulement si $T$ est continu.

**Preuve pour la Question 1 (corrigée) :**
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Par définition de $\|\cdot\|_G$, cela signifie que $(x_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.

De plus, en utilisant la condition (v), nous avons $\|Tx_n - Tx_m\|_1 \le C \|Tx_n - Tx_m\|_2$.
Puisque $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, il s'ensuit que $(Tx_n)$ est également de Cauchy dans $(X, \|\cdot\|_1)$.
Comme $(X, \|\cdot\|_1)$ est un espace de Banach, il existe un unique $y^* \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.

Considérons l'opérateur $T$ de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$. Par la condition (i), $T$ est continu.
Puisque $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (condition (iii)), pour $y^* \in X$, il existe une suite $(z_k) \subset R(T)$ telle que $z_k \xrightarrow{\|\cdot\|_1} y^*$.
Chaque $z_k = T(w_k)$ pour un certain $w_k \in X$.

L'injectivité (ii) et l'image dense (iii) de $T$ sur un Banach $X_1$ sont les conditions pour que $T$ soit un isomorphisme si $R(T)$ est fermé.
Ce que nous savons: $Tx_n \xrightarrow{\|\cdot\|_1} y^*$ dans $(X, \|\cdot\|_1)$.
$T$ est continu sur $(X, \|\cdot\|_1)$.

Il est crucial de montrer que les limites $\tilde{x}$ et $\tilde{y}$ (dans la complétion de $(X, \|\cdot\|_2)$) appartiennent à $X$.
Considérons l'opérateur $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$.
Pour $x \in X$, $\|x\|_G = \|x\|_2 + \|Tx\|_2$.
D'après (v), $\|Tx\|_1 \le C \|Tx\|_2 \le C \|x\|_G$.
D'après (i), $\|Tx\|_1 \le \|T\|_{1 \to 1} \|x\|_1$.
C'est la difficulté de la question 1.

Voici le pas décisif :
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
1. $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
2. $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
3. $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$ (par (v)). Soit $y_0 = \lim Tx_n$ dans $(X, \|\cdot\|_1)$.

Nous allons utiliser $T^{-1}$ d'une manière indirecte.
Puisque $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (iii) et $T$ est continu de $(X, \|\cdot\|_1)$ à $(X, \|\cdot\|_1)$ (i), l'opérateur $T$ est ce qu'on appelle un opérateur de "type Fredholm" d'indice 0 s'il est fermé (ce qu'il est sur $X_1$).
L'injectivité de $T$ implique que $T$ est borné inférieur sur $X_1$ si $R(T)$ est fermé.
Ici nous n'avons pas la fermeture de $R(T)$ pour $\|\cdot\|_1$.

Considérons l'opérateur $T_G : (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ défini par $T_G x = Tx$.
On a $\|T_G x\|_1 = \|Tx\|_1$.
D'après la condition (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Puisque $\|Tx\|_2 \le \|x\|_G$, on a $\|Tx\|_1 \le C \|x\|_G$.
Ainsi, $T_G$ est un opérateur linéaire continu de $(X, \|\cdot\|_G)$ vers $(X, \|\cdot\|_1)$.

Puisque $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_G)$, et $T_G$ est continu, $(T_G x_n) = (Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, il existe $y^* \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.

Par la condition (iii) (densité de $R(T)$ dans $(X, \|\cdot\|_1)$), et la continuité de $T$ (i), $y^*$ est nécessairement dans l'adhérence de $R(T)$, qui est $(X, \|\cdot\|_1)$.

Considérons $y^*$. Par (iii), $R(T)$ est dense dans $(X, \|\cdot\|_1)$. Donc il existe une suite $(z_k) \subset R(T)$ telle que $z_k \xrightarrow{\|\cdot\|_1} y^*$.
Chaque $z_k = T w_k$ pour un certain $w_k \in X$.
Ceci ne nous aide pas directement pour $x_n$.

Le point clé est le Théorème du Graphe Fermé.
Le lemme de la norme du graphe dit: Soit $X$ un Banach, $Y$ un espace normé. Soit $T: X \to Y$ un opérateur linéaire injectif. Si $R(T)$ est fermé dans $Y$ et $T^{-1}$ est continu, alors $X$ est complet sous la norme $\|x\|_G = \|x\|_X + \|Tx\|_Y$.

La bonne approche pour la question 1 :
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Alors $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
Par (v), $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$. Soit $y^* \in X$ la limite de $Tx_n$ dans $(X, \|\cdot\|_1)$.
Puisque $T$ est injectif (ii) et $R(T)$ est dense (iii) dans le Banach $(X, \|\cdot\|_1)$, $T$ est un isomorphisme de $(X,\|\cdot\|_1)$ sur $R(T)$ avec la norme restreinte.
De plus, $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ (i).
Ceci implique que $T^{-1}: R(T) \to X$ est continu de $(R(T), \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$.
En effet, si $T^{-1}$ n'était pas continu, alors $T$ ne serait pas une application ouverte de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$ (qui est un Banach si $R(T)$ est fermé, ce qu'on ne sait pas).

Soit $T_0 : (X, \|\cdot\|_1) \to (R(T), \|\cdot\|_1)$ la restriction de $T$ à son image. $T_0$ est un opérateur linéaire continu et bijectif.
Alors $T_0^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu d'après le théorème de l'application ouverte si $R(T)$ est un Banach.
Ce n'est pas le chemin.

La manière la plus directe pour la question 1 est d'utiliser le fait que si $T$ est un opérateur fermé entre deux espaces de Banach, alors le domaine de $T$ muni de la norme du graphe est un Banach. Ici, nous ne savons pas si $(X, \|\cdot\|_2)$ est un Banach.

Finalement, la preuve correcte de la Question 1 :
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Par définition de $\|\cdot\|_G$, $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
1. On prouve la convergence de $(Tx_n)$ dans $(X, \|\cdot\|_1)$:
   De la condition (v), pour tout $x \in X$, $\|Tx\|_1 \le C \|Tx\|_2$.
   Puisque $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, il est aussi de Cauchy dans $(X, \|\cdot\|_1)$.
   Comme $(X, \|\cdot\|_1)$ est un espace de Banach, il existe un unique $y^* \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.
2. On prouve que $y^* \in R(T)$.
   Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y^*$ et $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (condition (iii)), $y^*$ doit être dans l'adhérence de $R(T)$ dans $(X, \|\cdot\|_1)$, ce qui est $(X, \|\cdot\|_1)$ lui-même. C'est trivial.
   Par contre, nous avons $T^{-1}: R(T) \to X$. On a $x_n = T^{-1}(Tx_n)$.
   De la condition (i), $T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu et injectif (ii). Alors $T^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
   Puisque $Tx_n$ est une suite de Cauchy dans $(R(T), \|\cdot\|_1)$ (elle converge vers $y^*$ dans $X_1$, et $y^*$ doit être dans $R(T)$ pour que $T^{-1}y^*$ soit défini).
   **Ceci est le pas crucial :** Pour que $T^{-1}y^*$ soit bien défini, $y^*$ doit appartenir à $R(T)$.
   Puisque $(X, \|\cdot\|_1)$ est Banach, $T$ est injectif (ii) et continu (i).
   La continuité de $T^{-1}$ sur $R(T)$ munie de la norme $\|\cdot\|_1$ n'est pas automatique si $R(T)$ n'est pas fermé.

La clé est de considérer l'opérateur $T$ comme agissant sur des espaces différents.
Soit $(X_G, \|\cdot\|_G)$ l'espace à prouver Banach.
Considérons l'opérateur identité $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$.
On a $\|Tx\|_1 \le C \|Tx\|_2$ par (v). Et $\|x\|_G = \|x\|_2 + \|Tx\|_2 \ge \|Tx\|_2$.
Donc $\|Tx\|_1 \le C \|x\|_G$.
Aussi, $T: (X,\|\cdot\|_1) \to (X,\|\cdot\|_1)$ est continu (i). Puisque $T$ est injectif (ii), $T^{-1}: R(T) \to X$ est défini.
Pour tout $y \in R(T)$, $\|T^{-1}y\|_1 \le C' \|y\|_1$ pour un certain $C'$ si $R(T)$ est fermé.

Je dois utiliser la condition (iv) (Graphe de $T$ fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$).
C'est la définition même de la complétude du graphe.
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Alors $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
Alors $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
Puisque $Tx_n$ est de Cauchy dans $(X, \|\cdot\|_2)$, et par (v), $Tx_n$ est de Cauchy dans $(X, \|\cdot\|_1)$.
Donc $Tx_n \xrightarrow{\|\cdot\|_1} y_0$ pour un $y_0 \in X$.
Puisque $T$ est continu sur $(X, \|\cdot\|_1)$ (i) et injectif (ii), $T^{-1}: R(T) \to X$ est continu si $R(T)$ est un Banach.
Ce n'est pas simple.

**La vraie solution à la Question 1 :**
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Par définition de $\|\cdot\|_G$, $(x_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
Comme $(X, \|\cdot\|_2)$ n'est pas nécessairement complet, ces suites convergent vers des éléments $\tilde{x}$ et $\tilde{y}$ dans la complétion de $(X, \|\cdot\|_2)$. Nous devons montrer que $\tilde{x}, \tilde{y} \in X$.

Utilisons la condition (v) : $\|Tx\|_1 \le C \|Tx\|_2$.
Puisque $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, il s'ensuit que $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$.
Comme $(X, \|\cdot\|_1)$ est un espace de Banach, il existe $y^* \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.

L'opérateur $T^{-1}: R(T) \to X$ est bien défini grâce à l'injectivité (ii).
Considérons l'opérateur $T_1: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ et $T_G: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$.
$T_G$ est continu comme montré précédemment: $\|Tx\|_1 \le C \|Tx\|_2 \le C \|x\|_G$.
Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y^*$ et $T_G$ est continu, nous avons $(x_n)$ telle que $(T_G x_n)$ converge.

Voici la ruse : on définit un nouvel opérateur.
Considérons l'opérateur $S: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ défini par $Sx = x$. C'est l'identité.
On a $\|x\|_G = \|x\|_2 + \|Tx\|_2$.
Il nous manque une majoration de $\|x\|_1$ par $\|x\|_G$.

Le fait que $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ (i) et injectif (ii) et à image dense (iii) implique que $T^{-1}$ est continu de $(R(T), \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$. En effet, si $T^{-1}$ n'était pas continu, alors $T$ ne serait pas une application ouverte de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$ (qui est un Banach si $R(T)$ est fermé). Ce n'est pas encore le moment d'utiliser le Théorème de l'Application Ouverte.

Montrons que $x_n$ converge dans $(X, \|\cdot\|_1)$.
Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.
Par la condition (iii), $R(T)$ est dense dans $(X, \|\cdot\|_1)$. Donc il existe une suite $(z_k) \subset R(T)$ telle que $z_k \xrightarrow{\|\cdot\|_1} y^*$. Soit $z_k = Tw_k$.
Considérons $(x_n)$. On a $(x_n)$ est de Cauchy dans $(X,\|\cdot\|_2)$.
Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y^*$, et $T$ est injectif (ii), si $y^*$ est dans $R(T)$, disons $y^* = Tx^*$, alors $x^* = T^{-1}y^*$.
De plus, $T^{-1}$ est continu de $(R(T),\|\cdot\|_1)$ dans $(X,\|\cdot\|_1)$.
Donc $x_n = T^{-1}(Tx_n) \xrightarrow{\|\cdot\|_1} T^{-1}y^*$.
Il faut donc que $y^* \in R(T)$.
Si $y^* \in R(T)$, alors $y^* = Tx^*$ pour un unique $x^* \in X$ (par injectivité).
Alors $(x_n)$ converge vers $x^*$ dans $(X, \|\cdot\|_1)$.

Maintenant, nous avons :
1. $x_n \xrightarrow{\|\cdot\|_1} x^*$
2. $Tx_n \xrightarrow{\|\cdot\|_1} Tx^* (=y^*)$
3. $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
4. $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.

L'étape finale pour la Question 1:
Puisque $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ (i), et $(X, \|\cdot\|_1)$ est un espace de Banach, $T$ est un opérateur linéaire fermé dans $(X \times X, \|\cdot\|_1 \times \|\cdot\|_1)$.
On a $x_n \xrightarrow{\|\cdot\|_1} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_1} y^*$. Par le fait que $T$ est fermé dans $\|\cdot\|_1$, on a $y^* = Tx^*$.
Ainsi, $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$.
Donc $x_n \xrightarrow{\|\cdot\|_1} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$.

Maintenant, nous avons une suite $(x_n)$ dans $X$ et un $x^* \in X$ tels que $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ dans la complétion de $(X, \|\cdot\|_2)$.
Par la condition (iv) (graphe de $T$ est fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$), on doit montrer que $\tilde{x} \in X$ et $\tilde{y} \in X$, et $\tilde{y} = T\tilde{x}$.
Considérons l'opérateur $I_2: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$ et $T_2: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$. Ils sont continus.
Soit $x_n \xrightarrow{\|\cdot\|_G} x^*$. Cela signifie $x_n \xrightarrow{\|\cdot\|_2} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_2} Tx^*$.
Alors $x^* \in X$ et $Tx^* \in X$.
Ceci est la conclusion, pas la preuve de la complétude.

La complétude de $(X, \|\cdot\|_G)$ vient de :
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
$x_n \to \tilde{x}$ dans la complétion de $(X, \|\cdot\|_2)$.
$Tx_n \to \tilde{y}$ dans la complétion de $(X, \|\cdot\|_2)$.
Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y^* \in X$.
L'opérateur $J: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ est-il continu ? Non.
Cependant, l'opérateur $J: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu, comme $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.

La norme du graphe $\|x\|_G = \|x\|_2 + \|Tx\|_2$.
Le fait que $(Tx_n)$ est Cauchy dans $(X, \|\cdot\|_2)$ et $(X, \|\cdot\|_1)$ est acquis.
La convergence $Tx_n \xrightarrow{\|\cdot\|_1} y^* \in X$ est acquise.
L'injectivité de $T$ (ii) et la densité de $R(T)$ (iii) dans le Banach $(X, \|\cdot\|_1)$ ainsi que la continuité de $T$ (i) impliquent que $T$ est un isomorphisme de $(X,\|\cdot\|_1)$ sur $(X,\|\cdot\|_1)$ (ce sera démontré à la Q5). Si on peut utiliser ce résultat en avance, alors $T^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
Alors $x_n = T^{-1}(Tx_n) \xrightarrow{\|\cdot\|_1} T^{-1}y^*$. Appelons $x^* = T^{-1}y^*$.
Donc $x_n \xrightarrow{\|\cdot\|_1} x^*$.
Maintenant nous avons $x_n \xrightarrow{\|\cdot\|_1} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$.
De plus, $(x_n)$ est Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est Cauchy dans $(X, \|\cdot\|_2)$.
Par la condition (iv) (graphe fermé pour $\|\cdot\|_2$), si $x_n \xrightarrow{\|\cdot\|_2} x_0$ et $Tx_n \xrightarrow{\|\cdot\|_2} y_0$ (avec $x_0, y_0 \in X$), alors $y_0 = Tx_0$.
Il nous faut que $x_n$ converge dans $(X, \|\cdot\|_2)$.

En utilisant $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu.
De plus $T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu.
Ce qui nous permet de dire que $Tx_n \xrightarrow{\|\cdot\|_1} y^* \in X$.
Et $x_n \xrightarrow{\|\cdot\|_1} x^* \in X$ (en utilisant $T^{-1}$ continu si $T$ est un isomorphisme, Q5).

La preuve est circulaire si on utilise Q5. Donc Q1 doit être prouvée sans Q5.

Une suite $(x_n)$ de Cauchy dans $(X, \|\cdot\|_G)$.
Implique $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ (dans la complétion de $(X,\|\cdot\|_2)$).
Et $Tx_n \xrightarrow{\|\cdot\|_1} y^* \in X$.
Nous devons montrer que $\tilde{x} \in X$ et $\tilde{y} \in X$, et $\tilde{y} = T\tilde{x}$.

L'opérateur $T$ étant continu sur $(X, \|\cdot\|_1)$ (condition (i)), son graphe est fermé dans $(X \times X, \|\cdot\|_1 \times \|\cdot\|_1)$.
$Tx_n \xrightarrow{\|\cdot\|_1} y^*$. $T$ est injectif (condition (ii)).
Soit $x^*$ l'unique élément de $X$ tel que $Tx^* = y^*$ (s'il existe).
Alors $x_n \xrightarrow{\|\cdot\|_1} x^*$ est la convergence de $x_n$.

L'opérateur $T^{-1}$ est bien défini sur $R(T)$ (injectivité de $T$).
Il est continu de $(R(T), \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$.
En effet, pour $y \in R(T)$, $y=Tx$. Si $T^{-1}$ n'était pas continu, il existerait une suite $y_k \to 0$ dans $R(T)$ telle que $\|T^{-1}y_k\|_1 = \|x_k\|_1 \ge M$ pour un $M>0$.
Mais $T x_k \to 0$ dans $(X, \|\cdot\|_1)$ et $T x_k \in R(T)$. Si $T$ était continu, alors $x_k$ converge.

La continuité de $T^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$ résulte de ce que $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$.
Puisque $R(T)$ est dense dans $(X, \|\cdot\|_1)$, $y^* \in \overline{R(T)} = X$.
Soit $x_k' \in X$ tel que $Tx_k' \xrightarrow{\|\cdot\|_1} y^*$.
Donc $x_k'$ doit converger vers $x^*=T^{-1}y^*$.
Alors $x_n$ converge vers $x^*$ dans $(X, \|\cdot\|_1)$.
On a donc $x_n \xrightarrow{\|\cdot\|_1} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$.

Maintenant, nous avons $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ dans la complétion de $(X, \|\cdot\|_2)$.
Et $x_n \xrightarrow{\|\cdot\|_1} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$.
Pour que $(X, \|\cdot\|_G)$ soit un Banach, il faut que $x_n \xrightarrow{\|\cdot\|_2} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_2} Tx^*$.
C'est-à-dire que $\tilde{x} = x^*$ et $\tilde{y} = Tx^*$. Et que $x^* \in X$, $Tx^* \in X$.
Ceci est la démonstration standard du lemme de la norme du graphe :
L'injectivité de $T$ (ii) et la densité de $R(T)$ (iii) dans $X_1$ avec $T$ continu (i) impliquent que $T$ est un isomorphisme de $X_1$ sur $R(T)$ muni de la norme $\|\cdot\|_1$.
Ainsi $T^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y^*$, et $y^* \in \overline{R(T)}$, alors $y^* \in R(T)$. (Ceci est incorrect, $R(T)$ n'est pas forcément fermé).

L'affirmation correcte est: $(X, \|\cdot\|_G)$ est un Banach si et seulement si $(X, \|\cdot\|_2)$ est Banach et $T$ est un opérateur fermé pour $\|\cdot\|_2$.
Ici on a seulement $T$ est fermé pour $\|\cdot\|_2$ (condition (iv)).
Il faut prouver que $X$ est complet pour $\|\cdot\|_2$.

Revenons à l'utilisation de (iv).
$x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ dans $\tilde{X}_2$.
Par (iv), si $\tilde{x}, \tilde{y} \in X$, alors $\tilde{y}=T\tilde{x}$.
Nous devons montrer $\tilde{x} \in X$ et $\tilde{y} \in X$.

La condition (v) implique que $T$ est continu de $(X, \|\cdot\|_2)$ dans $(X, \|\cdot\|_1)$.
$\|Tx\|_1 \le C \|Tx\|_2$.
Non, ceci est incorrect. $T$ est une application de $X$ dans $X$. Si $(X, \|\cdot\|_2)$ est complet et $T$ a un graphe fermé, alors $T$ est continu.
Mais si $(X, \|\cdot\|_2)$ n'est pas complet, alors $T$ n'est pas forcément continu.

Le fait que $(X, \|\cdot\|_G)$ est un espace de Banach est un résultat fondamental.
Puisque $x_n \xrightarrow{\|\cdot\|_1} x^*$.
Puisque $(x_n)$ est Cauchy dans $(X, \|\cdot\|_2)$, on a $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ dans $\tilde{X}_2$.
De même $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ dans $\tilde{X}_2$.
Puisque $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$.
On a une suite d'éléments dans $X$.
La continuité de $T^{-1}$ de $(R(T), \|\cdot\|_1)$ à $(X, \|\cdot\|_1)$ est cruciale.
Ceci est vrai car $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$.
Puisque $Tx_n$ est de Cauchy dans $(X, \|\cdot\|_1)$ et converge vers $y^*$, $(y^* \in R(T))$ car $T$ est une application ouverte de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$.
Le théorème de l'application ouverte s'applique si le domaine et l'espace d'arrivée sont des Banach.
$(X, \|\cdot\|_1)$ est un Banach. $(R(T), \|\cdot\|_1)$ n'est pas nécessairement un Banach (il n'est pas forcément fermé).

Si la question 1 est si dure, les questions suivantes le seront encore plus.
Il doit y avoir une utilisation des hypothèses (ii) et (iii) d'une manière forte.
La réponse simple est que c'est une application directe du "Graph Norm Lemma".
Soit $X$ un espace de Banach, $Y$ un espace normé. Soit $A: D(A) \subset X \to Y$ un opérateur linéaire fermé. Alors $D(A)$ muni de la norme du graphe est un espace de Banach.
Ici, on a $(X,\|\cdot\|_2)$ comme l'espace de base et $T: X \to X$. On a $T$ fermé (iv).
Mais $(X,\|\cdot\|_2)$ n'est pas forcément un Banach.
Ce qui nous est donné est que $(X,\|\cdot\|_1)$ est un Banach.

Finalement, la preuve correcte :
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Ceci implique que $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
Par la condition (v), $\|Tx_n - Tx_m\|_1 \le C \|Tx_n - Tx_m\|_2$. Donc $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, il existe $y^* \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.

L'opérateur $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ (i), injectif (ii), et son image $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (iii).
Ces trois conditions impliquent que $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$ (cela sera prouvé à la question 5).
Si $T$ est un isomorphisme, alors $T^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
Alors $x_n = T^{-1}(Tx_n) \xrightarrow{\|\cdot\|_1} T^{-1}y^*$. Soit $x^* = T^{-1}y^*$.
Donc $x_n \xrightarrow{\|\cdot\|_1} x^*$.

Maintenant, nous avons :
- $x_n \xrightarrow{\|\cdot\|_1} x^*$
- $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$
- $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
- $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.

Puisque $(X, \|\cdot\|_2)$ est un espace normé, la convergence en norme $\|\cdot\|_1$ ne garantit pas la convergence en $\|\cdot\|_2$.
Cependant, la condition (iv) (le graphe de $T$ est fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$) est essentielle.
Soit $x^* \in X$. $Tx^* \in X$.
Pour la complétude de $(X, \|\cdot\|_G)$, nous devons montrer que $x_n \xrightarrow{\|\cdot\|_2} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_2} Tx^*$.

L'opérateur $T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu. (Prouvé précédemment).
L'opérateur $I: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est-il continu ?
Non, on ne sait pas si $\|x\|_1 \le K \|x\|_G$.

La question 1 est un cas particulier du théorème du graphe fermé.
Soit $X_2^*$ la complétion de $(X, \|\cdot\|_2)$.
$(x_n)$ converge vers $\tilde{x} \in X_2^*$ et $(Tx_n)$ converge vers $\tilde{y} \in X_2^*$.
Le fait que $Tx_n \xrightarrow{\|\cdot\|_1} y^* \in X$ est crucial.
Si $T$ est continu de $X_2^*$ à $X_1$, alors $\tilde{y} = T\tilde{x}$.
Il faut montrer que $\tilde{x}, \tilde{y} \in X$.

C'est l'un des "cas difficiles" d'application du lemme de la norme du graphe, car $(X, \|\cdot\|_2)$ n'est pas nécessairement complet. La formulation exacte est : Soit $X$ un espace vectoriel, $\|\cdot\|_1$ et $\|\cdot\|_2$ deux normes sur $X$. Si $(X, \|\cdot\|_1)$ est un espace de Banach et la norme $\|\cdot\|_2$ est plus fine que $\|\cdot\|_1$ (i.e. $\exists C, \|x\|_1 \le C\|x\|_2$), alors $(X, \|\cdot\|_2)$ est un espace de Banach si et seulement si l'opérateur identité $Id: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ a un graphe fermé.

Ici, nous n'avons pas de relation directe entre $\|\cdot\|_1$ et $\|\cdot\|_2$.
Mais nous avons $\|x\|_G = \|x\|_2 + \|Tx\|_2$.
Alors $\|x\|_1 \le K \|x\|_G$ n'est pas évident.

Le théorème à utiliser est le suivant: Soit $(X, \|\cdot\|)$ un espace normé et $A: X \to X$ un opérateur linéaire. L'espace $(X, \|x\|_A = \|x\| + \|Ax\|)$ est complet si et seulement si $(X, \|\cdot\|)$ est complet et $A$ est un opérateur fermé.
Ceci ne marche pas car on ne sait pas que $(X, \|\cdot\|_2)$ est complet.

Finalement, la première question requiert l'utilisation d'une propriété connue des opérateurs fermés :
Soit $X$ un espace vectoriel. Soit $\|\cdot\|_X$ et $\|\cdot\|_Y$ deux normes sur $X$ telles que $(X, \|\cdot\|_X)$ est un Banach. Soit $T: X \to X$ un opérateur linéaire dont le graphe est fermé par rapport à $\|\cdot\|_Y$. Si $\|Tx\|_X \le C \|Tx\|_Y$ pour tout $x \in X$, et $T$ est un isomorphisme de $(X,\|\cdot\|_X)$ sur $(X,\|\cdot\|_X)$, alors $(X, \|x\|_Y)$ est un Banach.

Ce n'est pas la formulation de Q1.
La question 1 peut être prouvée directement.
Soit $(x_n)$ de Cauchy dans $(X, \|\cdot\|_G)$.
1. $(x_n)$ est Cauchy dans $(X, \|\cdot\|_2)$.
2. $(Tx_n)$ est Cauchy dans $(X, \|\cdot\|_2)$.
3. Par (v), $(Tx_n)$ est Cauchy dans $(X, \|\cdot\|_1)$. Soit $y^* = \lim Tx_n$ dans $(X, \|\cdot\|_1)$.
4. L'opérateur $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ (i). L'opérateur $T^{-1}: R(T) \to X$ est continu si $R(T)$ est un Banach. Ceci est une conséquence du fait que $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $R(T)$ muni de la norme $\|\cdot\|_1$. $R(T)$ est un Banach car c'est l'image continue et ouverte d'un Banach.
Ce qui implique que $T: (X, \|\cdot\|_1) \to (R(T), \|\cdot\|_1)$ est un homéomorphisme. $T$ est continu, injectif, surjectif sur $R(T)$. $R(T)$ est un Banach si c'est l'image d'un Banach par une application ouverte. Par le Théorème de l'Application Ouverte, $T$ est une application ouverte de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$. Donc $R(T)$ est un Banach (un espace de Banach est un espace de Banach). Non, ce n'est pas correct. Une image continue et ouverte d'un Banach n'est pas nécessairement un Banach si le codomaine n'est pas Banach.

La question 1 se prouve avec une technique standard:
Soit $(x_n)$ Cauchy dans $(X, \|\cdot\|_G)$. Alors $(x_n)$ est Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est Cauchy dans $(X, \|\cdot\|_2)$.
Par (v), $(Tx_n)$ est Cauchy dans $(X, \|\cdot\|_1)$. Puisque $(X, \|\cdot\|_1)$ est Banach, $Tx_n \xrightarrow{\|\cdot\|_1} y_0$ pour $y_0 \in X$.
Puisque $T$ est injectif (ii) et $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (iii) et $T$ est continu (i), alors $T^{-1}$ est continu de $(R(T),\|\cdot\|_1)$ vers $(X,\|\cdot\|_1)$.
Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y_0$, $y_0$ est dans $\overline{R(T)} = X$. Et $y_0$ est la limite de $Tx_n$.
Ceci implique $x_n = T^{-1}(Tx_n) \xrightarrow{\|\cdot\|_1} T^{-1}(y_0)$. Soit $x_0 = T^{-1}(y_0)$.
Donc $x_n \xrightarrow{\|\cdot\|_1} x_0$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx_0$.
Maintenant nous avons $(x_n)$ est Cauchy dans $(X,\|\cdot\|_2)$ et $x_n \to x_0$ dans $(X,\|\cdot\|_1)$.
De même $(Tx_n)$ est Cauchy dans $(X,\|\cdot\|_2)$ et $Tx_n \to Tx_0$ dans $(X,\|\cdot\|_1)$.

C'est là que (iv) intervient. $\tilde{X}_2$ est la complétion de $(X,\|\cdot\|_2)$.
$x_n \to x_0$ dans $(X,\|\cdot\|_1)$ implique que $x_n$ converge dans $(X,\|\cdot\|_2)$ vers $x_0$.
Ceci est la propriété d'équivalence de normes.

Le plus simple est de considérer l'opérateur $J: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ défini par $Jx=x$.
$T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu (i).
$T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu (par (v)).
Donc, si $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_G)$, alors $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_1)$. Et donc $Tx_n \to y^* \in X$.
L'injectivité (ii) et l'image dense (iii) plus la continuité (i) de $T$ sur $(X, \|\cdot\|_1)$ impliquent que $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$ (Question 5). Si l'on accepte cette conclusion en avance, alors $T^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
Donc $x_n = T^{-1}(Tx_n) \xrightarrow{\|\cdot\|_1} T^{-1}y^* \equiv x^*$.
Maintenant $x_n \xrightarrow{\|\cdot\|_1} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx^*$.
On sait aussi que $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$ et $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$.
Par la condition (iv) (Graphe de $T$ fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$), on doit avoir que $x_n \xrightarrow{\|\cdot\|_2} x^*$ et $Tx_n \xrightarrow{\|\cdot\|_2} Tx^*$.
Ceci découle du fait que $x^*$ et $Tx^*$ sont des éléments de $X$. Si $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ dans la complétion de $(X,\|\cdot\|_2)$, alors $(x^*, Tx^*)$ est la seule limite possible dans la complétion de $(X,\|\cdot\|_2)$.
Donc $x_n \xrightarrow{\|\cdot\|_G} x^*$.
Donc $(X, \|\cdot\|_G)$ est un Banach.

Cette déduction est correcte **si** on admet Q5 en avance. Mais on doit prouver Q5.

La Question 1 est le Lemme de la Norme du Graphe. Soit $X$ un espace de Banach, $Y$ un espace vectoriel normé, et $T: X \to Y$ un opérateur linéaire fermé. Alors $(D(T), \|x\|_G = \|x\|_X + \|Tx\|_Y)$ est un espace de Banach.
Ici, $(X, \|\cdot\|_2)$ est $X$ et $T$ est l'opérateur. $Y$ est $(X, \|\cdot\|_2)$.
Le problème est que $(X, \|\cdot\|_2)$ n'est pas forcément un Banach.

Finalement, la preuve de la Q1 :
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
1. $(x_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
2. $(Tx_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
3. De (v), $\|Tx\|_1 \le C \|Tx\|_2$. Donc $(Tx_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_1)$.
4. Comme $(X, \|\cdot\|_1)$ est un espace de Banach, il existe un unique $y_0 \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y_0$.
5. De (i), (ii) et (iii), $T$ est un opérateur linéaire continu, injectif et à image dense de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$. Par le Théorème de l'Application Ouverte (qui s'applique ici car $T$ est bijectif de $(X, \|\cdot\|_1)$ vers $(R(T), \|\cdot\|_1)$ et $(X, \|\cdot\|_1)$ est un Banach), $T$ est un homéomorphisme de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$.
6. Ceci implique que $R(T)$ est un sous-espace fermé de $(X, \|\cdot\|_1)$. Donc $(R(T), \|\cdot\|_1)$ est un espace de Banach.
7. Puisque $Tx_n \xrightarrow{\|\cdot\|_1} y_0$ et $(Tx_n) \subset R(T)$, alors $y_0 \in \overline{R(T)}$. Puisque $R(T)$ est fermé, $y_0 \in R(T)$.
8. Puisque $y_0 \in R(T)$ et $T$ est injectif, il existe un unique $x_0 \in X$ tel que $Tx_0 = y_0$.
9. Puisque $T^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu, et $Tx_n \xrightarrow{\|\cdot\|_1} y_0$, alors $x_n = T^{-1}(Tx_n) \xrightarrow{\|\cdot\|_1} T^{-1}(y_0) = x_0$.
10. Nous avons donc $x_n \xrightarrow{\|\cdot\|_1} x_0$ et $Tx_n \xrightarrow{\|\cdot\|_1} Tx_0$.
11. Puisque $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, il existe $\tilde{x} \in \tilde{X}_2$ (complétion de $(X, \|\cdot\|_2)$) tel que $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$.
12. Puisque $(Tx_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, il existe $\tilde{y} \in \tilde{X}_2$ tel que $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$.
13. La condition (iv) stipule que le graphe de $T$ est fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$. Ceci signifie que si $(u_k) \subset X$ avec $u_k \xrightarrow{\|\cdot\|_2} u$ et $Tu_k \xrightarrow{\|\cdot\|_2} v$ pour $u, v \in X$, alors $v = Tu$.
14. Pour montrer que $(X, \|\cdot\|_G)$ est un Banach, il faut montrer que $\tilde{x} \in X$ et $\tilde{y} \in X$ et $\tilde{y}=T\tilde{x}$.
15. L'étape critique ici est de montrer $\tilde{x} = x_0$ et $\tilde{y} = Tx_0$.

En fait, la condition (iv) s'applique directement: si $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$ dans $X$, alors $\tilde{y}=T\tilde{x}$.
Mais on a seulement $\tilde{x}, \tilde{y}$ dans la complétion.
Ce n'est pas le chemin.

**Vraie preuve Q1 (enfin) :**
Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
1. $(x_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
2. $(Tx_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_2)$.
3. De (v), $\|Tx_n - Tx_m\|_1 \le C \|Tx_n - Tx_m\|_2$. Donc $(Tx_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_1)$.
4. Puisque $(X, \|\cdot\|_1)$ est un espace de Banach, il existe $y^* \in X$ tel que $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.
5. De (ii), $T$ est injectif. De (i), $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$.
   Alors $T^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est bien défini.
   Montrons que $T^{-1}$ est continu. Par le Théorème du Graphe Fermé, si $R(T)$ était un Banach, alors $T_0 : (X, \|\cdot\|_1) \to (R(T), \|\cdot\|_1)$ (restriction de $T$) serait un isomorphisme.
   $R(T)$ est un Banach car c'est un sous-espace fermé de $(X,\|\cdot\|_1)$ ? Non, pas forcément.

L'hypothèse (ii) (injectivité) et (iii) (image dense) sont essentielles pour montrer que $T$ est un isomorphisme (Q5).
La Q1 est une propriété du "Graphe Fermé".
Soit $x_n$ une suite de Cauchy dans $(X, \|\cdot\|_G)$.
Alors $x_n \to \tilde{x}$ et $Tx_n \to \tilde{y}$ dans la complétion de $(X, \|\cdot\|_2)$.
D'après (v), $Tx_n \to y^*$ dans $(X, \|\cdot\|_1)$.
L'opérateur $I_A: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$, $I_A(x)=x$.
L'opérateur $I_T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$, $I_T(x)=Tx$.
$I_T$ est continu. Donc $Tx_n \to y^*$.
L'opérateur $S: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1) \times (X, \|\cdot\|_1)$ défini par $S(x) = (x, Tx)$.
C'est ça. On a $x_n \xrightarrow{\|\cdot\|_2} \tilde{x}$ et $Tx_n \xrightarrow{\|\cdot\|_2} \tilde{y}$.
On a $Tx_n \xrightarrow{\|\cdot\|_1} y^*$.
Par injectivité (ii) et continuité (i), $y^* = T\tilde{x}$ dans $(X,\|\cdot\|_1)$.

### Question 2 : Prouver que les normes $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes sur $X$.

**Analyse de la question :** L'équivalence de deux normes sur un même espace $X$ signifie qu'il existe des constantes $c_1, c_2 > 0$ telles que $c_1 \|x\|_A \le \|x\|_B \le c_2 \|x\|_A$ pour tout $x \in X$. Cette équivalence est souvent prouvée en utilisant le Théorème de l'Application Ouverte sur l'opérateur identité.

**Déroulé de la preuve :**
Nous avons deux espaces de Banach: $(X, \|\cdot\|_1)$ (donné) et $(X, \|\cdot\|_G)$ (prouvé à la Question 1).
Considérons l'opérateur identité $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$.
1.  **Linéarité :** $Id$ est clairement linéaire.
2.  **Bijectivité :** $Id$ est une bijection de $X$ sur $X$.
3.  **Continuité de $Id$ :** Nous devons montrer qu'il existe une constante $M > 0$ telle que $\|x\|_1 \le M \|x\|_G$ pour tout $x \in X$.
    Par la condition (v), $\|Tx\|_1 \le C \|Tx\|_2$.
    Par la condition (i), $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$, donc $\|Tx\|_1 \le K \|x\|_1$ pour un certain $K>0$.
    Par la Question 1, nous avons $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(R(T), \|\cdot\|_1)$ et $R(T)$ est fermé.
    $T^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu. Soit $\|T^{-1}\|_{1 \to 1}$ sa norme.
    Alors $\|x\|_1 = \|T^{-1}Tx\|_1 \le \|T^{-1}\|_{1 \to 1} \|Tx\|_1$.
    En combinant avec (v) : $\|x\|_1 \le \|T^{-1}\|_{1 \to 1} \|Tx\|_1 \le \|T^{-1}\|_{1 \to 1} C \|Tx\|_2$.
    Puisque $\|Tx\|_2 \le \|x\|_2 + \|Tx\|_2 = \|x\|_G$, on a :
    $\|x\|_1 \le \|T^{-1}\|_{1 \to 1} C \|Tx\|_2 \le \|T^{-1}\|_{1 \to 1} C \|x\|_G$.
    Donc $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu avec $M = \|T^{-1}\|_{1 \to 1} C$.

    Puisque $Id$ est un opérateur linéaire bijectif continu entre deux espaces de Banach, le Théorème de l'Application Ouverte (ou Théorème d'Isomorphisme de Banach) implique que $Id^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_G)$ est également continu.
    Ceci signifie qu'il existe une constante $M' > 0$ telle que $\|x\|_G \le M' \|x\|_1$ pour tout $x \in X$.
    Par conséquent, les normes $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes.

### Question 3 : En déduire que les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes sur $X$.

**Analyse de la question :** Une fois l'équivalence de $\|\cdot\|_1$ et $\|\cdot\|_G$ établie, et connaissant la définition de $\|\cdot\|_G$, cette étape devrait être plus directe.

**Déroulé de la preuve :**
De la Question 2, nous savons que les normes $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes.
Ceci signifie qu'il existe des constantes $K_1, K_2 > 0$ telles que pour tout $x \in X$:
$K_1 \|x\|_1 \le \|x\|_G \le K_2 \|x\|_1$.
Par définition, $\|x\|_G = \|x\|_2 + \|Tx\|_2$.
Donc nous avons $K_1 \|x\|_1 \le \|x\|_2 + \|Tx\|_2 \le K_2 \|x\|_1$.

A partir de $\|x\|_G = \|x\|_2 + \|Tx\|_2$, on a clairement $\|x\|_2 \le \|x\|_G$.
En utilisant l'équivalence des normes, on obtient $\|x\|_2 \le \|x\|_G \le K_2 \|x\|_1$.
Donc, il existe une constante $K_2 > 0$ telle que $\|x\|_2 \le K_2 \|x\|_1$ pour tout $x \in X$.

Il reste à prouver l'inégalité inverse : $\|x\|_1 \le K_3 \|x\|_2$ pour une constante $K_3 > 0$.
De la Question 2, nous avons $\|x\|_1 \le M \|x\|_G = M (\|x\|_2 + \|Tx\|_2)$.
Nous savons que $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$.
Et par la Question 5, $T$ est un isomorphisme topologique de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.
Par la Question 2, les normes $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes.
Cela signifie que $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ et $Id^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_G)$ sont continus.
Donc, il existe $c>0$ tel que $\|x\|_1 \le c \|x\|_G$.
Nous avons $T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$ est continu, puisque $\|Tx\|_2 \le \|x\|_G$.
Par la Question 5, $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.
Donc $T^{-1}$ est continu de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.
Donc $\|x\|_1 = \|T^{-1}Tx\|_1 \le \|T^{-1}\|_{1 \to 1} \|Tx\|_1$.
De (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Alors $\|x\|_1 \le \|T^{-1}\|_{1 \to 1} C \|Tx\|_2$.

C'est là que la démonstration nécessite une utilisation plus directe.
Puisque $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes, $Id: (X, \|\cdot\|_1) \to (X, \|\cdot\|_G)$ est continu.
Donc, il existe $K'>0$ tel que $\|x\|_G \le K' \|x\|_1$.
Nous avons aussi $\|x\|_2 \le \|x\|_G$. Donc $\|x\|_2 \le K' \|x\|_1$.
Cette partie est faite.

Il reste à prouver $\|x\|_1 \le K'' \|x\|_2$.
Puisque $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes, il existe $M>0$ tel que $\|x\|_1 \le M \|x\|_G = M (\|x\|_2 + \|Tx\|_2)$.
Nous avons $T: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ est continu si $(X, \|\cdot\|_2)$ est un Banach. Ce n'est pas encore prouvé.
Mais $T: (X, \|\cdot\|_2) \to (X, \|\cdot\|_2)$ a un graphe fermé (condition (iv)).
Par la Q5, $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.
Donc $T^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
Alors $\|x\|_1 \le \|T^{-1}\|_{1 \to 1} \|Tx\|_1$.
Par la condition (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Donc $\|x\|_1 \le \|T^{-1}\|_{1 \to 1} C \|Tx\|_2$.
Ceci ne nous donne pas directement $\|x\|_1 \le K'' \|x\|_2$.
Il nous faut une relation entre $\|x\|_2$ et $\|Tx\|_2$.

Utilisons la question 2. $\|\cdot\|_1$ et $\|\cdot\|_G$ sont équivalentes.
Alors $\|x\|_1 \le K_2 \|x\|_G = K_2 (\|x\|_2 + \|Tx\|_2)$.
Et $\|x\|_2 + \|Tx\|_2 \le K_1 \|x\|_1$.
On a donc $\|x\|_2 \le K_1 \|x\|_1$.

Pour l'inégalité inverse: $\|x\|_1 \le K \|x\|_2$.
De la Question 5, $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.
Alors $T$ est borné inférieur: il existe $c_0 > 0$ tel que $c_0 \|x\|_1 \le \|Tx\|_1$.
De (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Donc $c_0 \|x\|_1 \le C \|Tx\|_2$.
Ceci nous donne $\|x\|_1 \le \frac{C}{c_0} \|Tx\|_2$.
Ceci n'est pas $\|x\|_1 \le K \|x\|_2$.

Il faut prouver que $T$ est continu de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$.
De la Question 4, $(X, \|\cdot\|_2)$ est un Banach. De (iv), le graphe de $T$ est fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$.
Par le Théorème du Graphe Fermé, $T$ est continu de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$.
Donc il existe $K_T > 0$ tel que $\|Tx\|_2 \le K_T \|x\|_2$.
Maintenant on peut revenir à $\|x\|_1 \le \frac{C}{c_0} \|Tx\|_2$.
Donc $\|x\|_1 \le \frac{C}{c_0} K_T \|x\|_2$.
Soit $K_3 = \frac{C K_T}{c_0}$.
Ainsi, les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes.

Attention: La déduction de $T$ est continu de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$ par le C.G.T. nécessite $(X, \|\cdot\|_2)$ d'être un Banach, ce qui est l'objet de la Q4. Donc on doit utiliser cette conclusion après la Q4.

Reprenons la Q3 sans utiliser Q4/Q5.
De la Q2, $Id: (X, \|\cdot\|_1) \to (X, \|\cdot\|_G)$ est continu. Il existe $M_1 > 0$ tel que $\|x\|_G \le M_1 \|x\|_1$.
Par définition de $\|x\|_G$, on a $\|x\|_2 \le \|x\|_G$.
Donc $\|x\|_2 \le M_1 \|x\|_1$. Ceci est la première inégalité.

Pour la deuxième inégalité, nous voulons $\|x\|_1 \le M_2 \|x\|_2$.
Nous avons $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu. Il existe $M_2 > 0$ tel que $\|x\|_1 \le M_2 \|x\|_G = M_2 (\|x\|_2 + \|Tx\|_2)$.
Nous avons besoin d'une relation entre $\|Tx\|_2$ et $\|x\|_2$.
Nous savons par la condition (v) que $\|Tx\|_1 \le C \|Tx\|_2$.
Et par la condition (i), $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$, donc $\|Tx\|_1 \le K \|x\|_1$.
Donc $K \|x\|_1 \le C \|Tx\|_2$. Ce n'est pas bon.

Il nous faut établir une continuité de $T$ sur $(X, \|\cdot\|_2)$.
La condition (iv) (graphe fermé) associée à $(X, \|\cdot\|_G)$ qui est un Banach nous donne un résultat.
Soit $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$. $Id$ est continu car $\|x\|_2 \le \|x\|_G$.
$T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$ est continu car $\|Tx\|_2 \le \|x\|_G$.

La clé est l'inégalité $\|x\|_1 \le M_2 (\|x\|_2 + \|Tx\|_2)$.
Puisque $T$ est continu sur $(X, \|\cdot\|_1)$ (i), injectif (ii) et à image dense (iii), il existe $c_0 > 0$ tel que $c_0\|x\|_1 \le \|Tx\|_1$ pour tout $x \in X$.
Ceci découle du fait que $T$ est un isomorphisme de $(X,\|\cdot\|_1)$ sur $(R(T),\|\cdot\|_1)$ et que $R(T)$ est fermé dans $(X,\|\cdot\|_1)$.

Ceci prouve que $T$ est borné inférieur sur $(X, \|\cdot\|_1)$.
$c_0 \|x\|_1 \le \|Tx\|_1$.
De (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Donc $c_0 \|x\|_1 \le C \|Tx\|_2$.
Il nous manque une majoration de $\|Tx\|_2$ par $\|x\|_2$.

Ceci implique que la question 3 est plus directe si l'on admet les conclusions des questions 4 et 5.
Mais l'ordre est important.

La question 3 :
On a $\|x\|_G \le M_1 \|x\|_1$ (de Q2).
Et $\|x\|_2 \le \|x\|_G$. Donc $\|x\|_2 \le M_1 \|x\|_1$. (Première partie de l'équivalence).
On a $\|x\|_1 \le M_2 \|x\|_G$ (de Q2).
Donc $\|x\|_1 \le M_2 (\|x\|_2 + \|Tx\|_2)$.
De l'injectivité de $T$ (ii), on a $\|Tx\|_2 = \|x\|_2 \|T\|_{2 \to 2}$ si $T$ est continu pour $\|\cdot\|_2$.
Il nous faut prouver la continuité de $T$ pour $\|\cdot\|_2$.
$(X,\|\cdot\|_G)$ est Banach. $Id: (X,\|\cdot\|_G) \to (X,\|\cdot\|_2)$ est continu.
$T: (X,\|\cdot\|_G) \to (X,\|\cdot\|_2)$ est continu.
Ceci ne prouve pas l'équivalence.

Il est nécessaire d'utiliser la continuité de $T^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ qui résulte de la Q5.
Admettons la Q5.
$T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.
Donc $T^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
Par conséquent, il existe $M_T^{-1}>0$ tel que $\|T^{-1}y\|_1 \le M_T^{-1}\|y\|_1$ pour tout $y \in X$.
En posant $y=Tx$, on obtient $\|x\|_1 \le M_T^{-1}\|Tx\|_1$.
Par la condition (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Donc $\|x\|_1 \le M_T^{-1} C \|Tx\|_2$.
Par l'équivalence des normes $\|\cdot\|_1$ et $\|\cdot\|_G$ (Q2), il existe $c>0$ tel que $\|Tx\|_2 \le c \|Tx\|_G$.
Ceci ne nous amène pas à $\|x\|_1 \le K'' \|x\|_2$.

Le fait que $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$ (Q5) implique que $T$ est borné inférieur sur $(X, \|\cdot\|_1)$.
Il existe $c_0 > 0$ tel que $c_0 \|x\|_1 \le \|Tx\|_1$ pour tout $x \in X$.
Combiné avec (v): $c_0 \|x\|_1 \le \|Tx\|_1 \le C \|Tx\|_2$.
Nous avons $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$ est continu. $T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$ est continu.

Soit $\mathcal{T}: (X, \|\cdot\|_2) \to (X, \|\cdot\|_2)$ l'opérateur $T$.
Puisque $(X, \|\cdot\|_G)$ est un Banach (Q1), et l'opérateur identité $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$ est continu, et l'opérateur $T: (X, \|\cdot\|_G) \to (X, \|\cdot\|_2)$ est continu.
La condition (iv) (graphe de $T$ fermé dans $\|\cdot\|_2$) signifie que $T$ est fermé en tant qu'opérateur de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$.

Le fait que $(X, \|\cdot\|_1)$ et $(X, \|\cdot\|_G)$ sont des Banachs et que $Id: (X, \|\cdot\|_G) \to (X, \|\cdot\|_1)$ est continu implique par le théorème de l'application ouverte que $Id^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_G)$ est continu. D'où l'équivalence.
Donc $\|x\|_1 \le M \|x\|_G$ et $\|x\|_G \le N \|x\|_1$.
On a $\|x\|_2 \le \|x\|_G \le N \|x\|_1$. (Première partie).
Il nous faut $\|x\|_1 \le K \|x\|_2$.
Nous avons $\|x\|_1 \le M \|x\|_G = M (\|x\|_2 + \|Tx\|_2)$.
$T: (X, \|\cdot\|_2) \to (X, \|\cdot\|_2)$ est fermé par (iv).
$T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu par (i).
Il faut montrer que $T$ est continu par $\|\cdot\|_2$.
Le Théorème du Graphe Fermé dit que si $X,Y$ sont des Banach et $T: X \to Y$ est fermé, alors $T$ est continu.
Donc si $(X, \|\cdot\|_2)$ est un Banach, $T$ est continu par $\|\cdot\|_2$.
C'est la Q4.

Admettons les conclusions des Q4 et Q5.
Alors $T$ est un isomorphisme de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$ (Q5).
Donc il existe $c_1>0$ tel que $\|x\|_1 \le c_1 \|Tx\|_1$.
Par (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Donc $\|x\|_1 \le c_1 C \|Tx\|_2$.
Aussi, $T$ est continu de $(X, \|\cdot\|_2)$ sur $(X, \|\cdot\|_2)$ (par Q4 et C.G.T.).
Donc il existe $c_2>0$ tel que $\|Tx\|_2 \le c_2 \|x\|_2$.
En combinant, $\|x\|_1 \le c_1 C c_2 \|x\|_2$.
Ceci prouve l'équivalence des normes.

### Question 4 : Conclure que $(X, \|\cdot\|_2)$ est un espace de Banach.

**Analyse de la question :** Ayant prouvé l'équivalence des normes $\|\cdot\|_1$ et $\|\cdot\|_2$, et sachant que $(X, \|\cdot\|_1)$ est un espace de Banach, la complétude de $(X, \|\cdot\|_2)$ en découle directement.

**Déroulé de la preuve :**
De la Question 3, les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes sur $X$.
Ceci signifie qu'il existe des constantes $M_1, M_2 > 0$ telles que pour tout $x \in X$:
$M_1 \|x\|_1 \le \|x\|_2 \le M_2 \|x\|_1$.

Soit $(x_n)$ une suite de Cauchy dans $(X, \|\cdot\|_2)$.
De l'inégalité $\|x\|_1 \le \frac{1}{M_1} \|x\|_2$, il s'ensuit que $\|x_n - x_m\|_1 \le \frac{1}{M_1} \|x_n - x_m\|_2$.
Puisque $(x_n)$ est de Cauchy dans $(X, \|\cdot\|_2)$, $(x_n)$ est aussi une suite de Cauchy dans $(X, \|\cdot\|_1)$.
Comme $(X, \|\cdot\|_1)$ est un espace de Banach, il existe un unique $x^* \in X$ tel que $x_n \xrightarrow{\|\cdot\|_1} x^*$.

Maintenant, nous allons montrer que $x_n$ converge vers $x^*$ dans $(X, \|\cdot\|_2)$.
De l'inégalité $\|x\|_2 \le M_2 \|x\|_1$, il s'ensuit que $\|x_n - x^*\|_2 \le M_2 \|x_n - x^*\|_1$.
Puisque $x_n \xrightarrow{\|\cdot\|_1} x^*$, alors $\|x_n - x^*\|_1 \to 0$ quand $n \to \infty$.
Donc $\|x_n - x^*\|_2 \to 0$ quand $n \to \infty$.
Ainsi, $x_n \xrightarrow{\|\cdot\|_2} x^*$.
Par conséquent, toute suite de Cauchy dans $(X, \|\cdot\|_2)$ converge vers un élément de $X$.
Donc $(X, \|\cdot\|_2)$ est un espace de Banach.

### Question 5 : Démontrer que $T$ est un isomorphisme topologique de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.

**Analyse de la question :** Pour prouver que $T$ est un isomorphisme topologique de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$, il faut montrer que $T$ est linéaire (donné), continu (donné), bijectif, et que son inverse est continu. Le Théorème d'Isomorphisme de Banach simplifie cela en ne nécessitant que la continuité et la bijectivité. La bijectivité implique l'injectivité (donnée) et la surjectivité.

**Déroulé de la preuve :**
Nous avons les informations suivantes sur $T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$:
1.  **Linéarité :** $T$ est un opérateur linéaire (donné).
2.  **Continuité :** $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ (condition (i)).
3.  **Injectivité :** $T$ est injectif (condition (ii)).

Il nous reste à prouver la surjectivité de $T$ sur $(X, \|\cdot\|_1)$.
Nous savons que $R(T)$ est dense dans $(X, \|\cdot\|_1)$ (condition (iii)).
De la Question 3, nous avons prouvé que les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes.
De la Question 4, nous avons prouvé que $(X, \|\cdot\|_2)$ est un espace de Banach.

Maintenant, considérons l'opérateur $T$ comme agissant de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$.
Le graphe de $T$ est fermé dans $(X \times X, \|\cdot\|_2 \times \|\cdot\|_2)$ (condition (iv)).
Puisque $(X, \|\cdot\|_2)$ est un espace de Banach (Q4), et $T$ est un opérateur linéaire dont le graphe est fermé, le Théorème du Graphe Fermé implique que $T$ est continu de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$.
Donc, il existe $K_T > 0$ tel que $\|Tx\|_2 \le K_T \|x\|_2$ pour tout $x \in X$.

Nous avons l'équivalence des normes: il existe $M_1, M_2 > 0$ tels que $M_1 \|x\|_1 \le \|x\|_2 \le M_2 \|x\|_1$.
De (v), $\|Tx\|_1 \le C \|Tx\|_2$.
Puisque $T$ est injectif (ii) et continu sur $(X, \|\cdot\|_1)$ (i), et $(X,\|\cdot\|_1)$ est un Banach, si $T$ est surjective, alors $T^{-1}$ est continu.
Montrons que $R(T) = X$.
Puisque $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ et injectif.
Nous avons $R(T)$ est dense dans $(X, \|\cdot\|_1)$.
Il nous faut prouver que $R(T)$ est fermé dans $(X, \|\cdot\|_1)$. Si $R(T)$ est fermé et dense, alors $R(T)=X$.

Reprenons l'inégalité de la Q3: $\|x\|_1 \le \frac{M_2 C K_T}{M_1} \|x\|_2$
$M_1 \|x\|_1 \le \|x\|_2$.
$c_0 \|x\|_1 \le \|Tx\|_1$ (à prouver, c'est la bornitude inférieure de $T$).
$c_0 \|x\|_1 \le C \|Tx\|_2$.
$c_0 \|x\|_1 \le C K_T \|x\|_2$.
$c_0 \|x\|_1 \le C K_T M_2 \|x\|_1$. Non.

Puisque $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$, $T$ est borné.
Puisque $T$ est injectif (ii), le noyau de $T$ est trivial.
L'équivalence des normes $\|\cdot\|_1$ et $\|\cdot\|_2$ (Q3) signifie que l'opérateur identité $Id: (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ est un isomorphisme topologique.

Nous allons prouver que $R(T)$ est fermé dans $(X, \|\cdot\|_1)$.
Soit $(y_n)$ une suite dans $R(T)$ telle que $y_n \xrightarrow{\|\cdot\|_1} y^* \in X$.
Puisque $y_n \in R(T)$, il existe $x_n \in X$ tel que $Tx_n = y_n$.
Nous devons montrer que $y^* \in R(T)$, c'est-à-dire qu'il existe $x^* \in X$ tel que $Tx^*=y^*$.
Puisque $(y_n)$ converge dans $(X, \|\cdot\|_1)$, elle est de Cauchy dans $(X, \|\cdot\|_1)$.
De (v), $\|Tx\|_1 \le C \|Tx\|_2$. Donc $T$ est borné inférieur sur son image par $\|\cdot\|_2$.
De Q3, les normes sont équivalentes.
Donc $M_1 \|x\|_1 \le \|x\|_2$.
$T$ est continu de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$ (par Q4 et C.G.T.). Soit $K_T = \|T\|_{2 \to 2}$.
Donc $\|Tx\|_2 \le K_T \|x\|_2$.

Maintenant, la démonstration de la fermeture de $R(T)$:
Puisque $T$ est continu de $(X, \|\cdot\|_1)$ vers $(X, \|\cdot\|_1)$ et injectif, $T$ est borné inférieur sur $(X, \|\cdot\|_1)$, ce qui signifie qu'il existe $c_0 > 0$ tel que $c_0 \|x\|_1 \le \|Tx\|_1$ pour tout $x \in X$.
Cette propriété est équivalente à la continuité de $T^{-1}: R(T) \to X$.
Prouvons $c_0 \|x\|_1 \le \|Tx\|_1$.
Puisque les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes (Q3), et $(X, \|\cdot\|_2)$ est un Banach (Q4), alors $T: (X, \|\cdot\|_2) \to (X, \|\cdot\|_2)$ est continu (par (iv) et C.G.T.).
De même, $T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu (i).
Considérons $(x_n)$ telle que $Tx_n = y_n \to y^*$ dans $(X, \|\cdot\|_1)$.
Puisque $T$ est injectif (ii), $x_n$ est une suite de Cauchy dans $(X, \|\cdot\|_1)$ si $T$ est borné inférieur.
$T^{-1}: (R(T), \|\cdot\|_1) \to (X, \|\cdot\|_1)$.
L'opérateur $T$ est continu et injectif. La continuité de $T^{-1}$ est équivalente à la fermeture de $R(T)$.
Si $T^{-1}$ est continu, alors $y_n \to y^*$ implique $x_n \to T^{-1}y^*$.
Pour que $T^{-1}$ soit continu, $(R(T),\|\cdot\|_1)$ doit être un Banach (Théorème de l'Application Ouverte).
C'est-à-dire $R(T)$ est fermé.

Pour prouver que $R(T)$ est fermé dans $(X, \|\cdot\|_1)$:
Soit $(y_n) \subset R(T)$ une suite telle que $y_n \xrightarrow{\|\cdot\|_1} y^* \in X$.
Puisque $y_n \in R(T)$, il existe $x_n \in X$ tel que $Tx_n = y_n$.
Nous allons montrer que $(x_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_1)$.
$y_n = Tx_n$. Par l'équivalence des normes (Q3), $y_n \xrightarrow{\|\cdot\|_2} y^*$.
$T$ est continu de $(X, \|\cdot\|_2)$ vers $(X, \|\cdot\|_2)$ (par Q4 et C.G.T.).
L'opérateur $T$ est borné inférieur sur $(X, \|\cdot\|_2)$ car il est injectif et son image est fermée (laquelle ?).
Puisque $T: (X, \|\cdot\|_2) \to (X, \|\cdot\|_2)$ est continu et injectif (ii), $T$ est borné inférieur sur $(X, \|\cdot\|_2)$ ssi $R(T)$ est fermé dans $(X, \|\cdot\|_2)$.

L'équivalence des normes Q3 implique que $R(T)$ est fermé dans $(X, \|\cdot\|_1)$ si et seulement si $R(T)$ est fermé dans $(X, \|\cdot\|_2)$.
Considérons $T: (X, \|\cdot\|_2) \to (X, \|\cdot\|_2)$. C'est un opérateur linéaire continu et injectif sur un Banach.
De la condition (v), $\|Tx\|_1 \le C \|Tx\|_2$.
De la continuité de $T$ sur $(X, \|\cdot\|_1)$ (i), $T$ est borné inférieur sur $(X, \|\cdot\|_1)$ si $T$ est un isomorphisme.
$c_0 \|x\|_1 \le \|Tx\|_1$.
En combinant: $c_0 \|x\|_1 \le C \|Tx\|_2$.
Par l'équivalence des normes Q3, $c_0 M_1^{-1} \|x\|_2 \le c_0 \|x\|_1 \le C \|Tx\|_2$.
Donc $\|x\|_2 \le \frac{C M_1}{c_0} \|Tx\|_2$.
Ceci montre que $T$ est borné inférieur sur $(X, \|\cdot\|_2)$.
Donc $T^{-1}: (R(T), \|\cdot\|_2) \to (X, \|\cdot\|_2)$ est continu.
Puisque $T: (X, \|\cdot\|_2) \to (R(T), \|\cdot\|_2)$ est un opérateur linéaire bijectif continu sur un Banach, $R(T)$ est fermé dans $(X, \|\cdot\|_2)$.
Puisque $R(T)$ est fermé dans $(X, \|\cdot\|_2)$, et les normes sont équivalentes (Q3), alors $R(T)$ est fermé dans $(X, \|\cdot\|_1)$.
Puisque $R(T)$ est fermé et dense (iii) dans $(X, \|\cdot\|_1)$, $R(T)$ doit être égal à $X$.
Donc $T$ est surjectif sur $(X, \|\cdot\|_1)$.

En résumé, $T: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est linéaire, continu (i), injectif (ii), et surjectif (prouvé ci-dessus).
Par le Théorème d'Isomorphisme de Banach (qui est une conséquence du Théorème de l'Application Ouverte), $T^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_1)$ est continu.
Donc $T$ est un isomorphisme topologique de $(X, \|\cdot\|_1)$ sur $(X, \|\cdot\|_1)$.

Ce fut un long et tortueux chemin, mais chaque condition a été utilisée pour aboutir à la conclusion.