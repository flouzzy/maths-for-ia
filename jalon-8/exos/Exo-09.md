# Exercice 9 : Décomposition de Fitting et endomorphismes nilpotents/inversibles (Difficulté : *****)

Soit $K$ un corps commutatif quelconque. Soit $E$ un $K$-espace vectoriel de dimension finie $n \ge 1$.
Soit $u \in L(E)$ un endomorphisme de $E$.

Pour tout entier naturel $k \ge 0$, on définit les sous-espaces vectoriels :
- $K_k = \ker(u^k)$, le noyau de $u^k$.
- $I_k = \mathrm{Im}(u^k)$, l'image de $u^k$.
Par convention, $u^0 = \mathrm{id}_E$, donc $K_0 = \{0\}$ et $I_0 = E$.

1.  Démontrer que la suite $(K_k)_{k \ge 0}$ est une suite croissante de sous-espaces vectoriels de $E$ (pour l'inclusion), et que la suite $(I_k)_{k \ge 0}$ est une suite décroissante de sous-espaces vectoriels de $E$.
2.  Démontrer qu'il existe un plus petit entier $p \in \{0, \dots, n\}$ tel que $K_p = K_{p+1}$. Démontrer alors que pour tout $k \ge p$, on a $K_k = K_p$. Démontrer un résultat analogue pour la suite $(I_k)_{k \ge 0}$, c'est-à-dire $I_p = I_{p+1}$ et $I_k = I_p$ pour tout $k \ge p$. Cet entier $p$ est appelé l'indice de Fitting de l'endomorphisme $u$.
3.  On se place avec l'entier $p$ défini à la question précédente. Démontrer que $E = K_p \oplus I_p$.
4.  Démontrer que les sous-espaces $K_p$ et $I_p$ sont stables par $u$. On note $u_K$ la restriction de $u$ à $K_p$ (vue comme endomorphisme de $K_p$) et $u_I$ la restriction de $u$ à $I_p$ (vue comme endomorphisme de $I_p$). Démontrer que $u_K$ est un endomorphisme nilpotent et que $u_I$ est un automorphisme.

---

## Correction détaillée

1.  **Monotonie des suites $(K_k)_{k \ge 0}$ et $(I_k)_{k \ge 0}$**

    *   **Pour $(K_k)_{k \ge 0}$ :**
        Soit $k \ge 0$. Nous voulons montrer que $K_k \subseteq K_{k+1}$.
        Soit $x \in K_k$. Par définition, $u^k(x) = 0$.
        Alors $u^{k+1}(x) = u(u^k(x)) = u(0) = 0$.
        Donc $x \in K_{k+1}$.
        Ceci prouve que $K_k \subseteq K_{k+1}$ pour tout $k \ge 0$. La suite $(K_k)_{k \ge 0}$ est donc croissante pour l'inclusion.

    *   **Pour $(I_k)_{k \ge 0}$ :**
        Soit $k \ge 0$. Nous voulons montrer que $I_{k+1} \subseteq I_k$.
        Soit $y \in I_{k+1}$. Par définition, il existe $x \in E$ tel que $y = u^{k+1}(x)$.
        On peut écrire $y = u^k(u(x))$.
        Puisque $u(x) \in E$, $y$ est l'image d'un élément de $E$ par $u^k$.
        Donc $y \in I_k$.
        Ceci prouve que $I_{k+1} \subseteq I_k$ pour tout $k \ge 0$. La suite $(I_k)_{k \ge 0}$ est donc décroissante pour l'inclusion.

2.  **Stabilisation des suites $(K_k)_{k \ge 0}$ et $(I_k)_{k \ge 0}$**

    *   **Pour $(K_k)_{k \ge 0}$ :**
        La suite $(K_k)_{k \ge 0}$ est une suite croissante de sous-espaces vectoriels de $E$.
        De plus, $E$ est de dimension finie $n$.
        Cela implique que la suite des dimensions $\mathrm{dim}(K_k)$ est une suite croissante d'entiers naturels, majorée par $n$.
        Une telle suite doit nécessairement stationner. C'est-à-dire qu'il existe un entier $p_0$ tel que $\mathrm{dim}(K_{p_0}) = \mathrm{dim}(K_{p_0+1})$.
        Puisque $K_{p_0} \subseteq K_{p_0+1}$ et qu'ils ont la même dimension, on en déduit que $K_{p_0} = K_{p_0+1}$.
        Soit $p$ le plus petit entier tel que $K_p = K_{p+1}$. Un tel $p$ existe car la suite stationne et $K_0 \subseteq K_1 \subseteq \dots \subseteq K_n = E$ est la chaîne maximale de sous-espaces strictement croissants. Si $K_i \subsetneq K_{i+1}$ pour tout $i$, alors on aurait $\mathrm{dim}(K_{i+1}) \ge \mathrm{dim}(K_i) + 1$, ce qui impliquerait $\mathrm{dim}(K_n) \ge \mathrm{dim}(K_0) + n = n$, atteignant la dimension de $E$ au plus en $n$ étapes.
        Nous allons montrer par récurrence que pour tout $k \ge p$, $K_k = K_p$.
        L'initialisation ($k=p$) est triviale : $K_p = K_p$.
        L'étape de récurrence : Supposons que $K_k = K_p$ pour un $k \ge p$. Nous voulons montrer que $K_{k+1} = K_p$.
        Nous savons déjà que $K_p \subseteq K_{k+1}$ (car la suite est croissante).
        Il reste à montrer que $K_{k+1} \subseteq K_p$. Soit $x \in K_{k+1}$. Alors $u^{k+1}(x) = 0$.
        Nous avons $u^p(x) \in E$. Alors $u^{k+1-p}(u^p(x)) = u^{k+1}(x) = 0$.
        Puisque $k \ge p$, $k+1-p \ge 1$.
        Considérons l'application $u$ restreinte à $K_{j+1}$ pour un certain $j$.
        Si $y \in K_{k+1}$, alors $u^{k+1}(y)=0$.
        Si $K_p=K_{p+1}$, montrons $K_{p+1}=K_{p+2}$.
        Soit $x \in K_{p+2}$. Alors $u^{p+2}(x)=0$. On peut écrire $u^{p+1}(u(x))=0$. Donc $u(x) \in K_{p+1}$.
        Puisque $K_{p+1} = K_p$, on a $u(x) \in K_p$, ce qui signifie $u^p(u(x)) = 0$, donc $u^{p+1}(x) = 0$.
        Par conséquent $x \in K_{p+1}$. Comme $K_{p+1} = K_p$, on a $x \in K_p$.
        Donc $K_{p+2} \subseteq K_p$. Puisque $K_p \subseteq K_{p+2}$ (par croissance), on a $K_{p+2}=K_p$.
        En réitérant ce raisonnement, on montre par récurrence que $K_k=K_p$ pour tout $k \ge p$.

    *   **Pour $(I_k)_{k \ge 0}$ :**
        La suite $(I_k)_{k \ge 0}$ est une suite décroissante de sous-espaces vectoriels de $E$.
        Comme précédemment, la suite des dimensions $\mathrm{dim}(I_k)$ est une suite décroissante d'entiers naturels, minorée par $0$.
        Elle doit donc stationner. Il existe un entier $p'$ tel que $\mathrm{dim}(I_{p'}) = \mathrm{dim}(I_{p'+1})$.
        Puisque $I_{p'+1} \subseteq I_{p'}$ et qu'ils ont la même dimension, on en déduit que $I_{p'} = I_{p'+1}$.
        Le théorème du rang stipule que $\mathrm{dim}(E) = \mathrm{dim}(\ker(u^k)) + \mathrm{dim}(\mathrm{Im}(u^k))$, soit $n = \mathrm{dim}(K_k) + \mathrm{dim}(I_k)$.
        Si $K_p = K_{p+1}$, alors $\mathrm{dim}(K_p) = \mathrm{dim}(K_{p+1})$.
        Donc $n - \mathrm{dim}(I_p) = n - \mathrm{dim}(I_{p+1})$, ce qui implique $\mathrm{dim}(I_p) = \mathrm{dim}(I_{p+1})$.
        Puisque $I_{p+1} \subseteq I_p$ et qu'ils ont la même dimension, on a $I_p = I_{p+1}$.
        Ainsi, l'entier $p$ est le même pour la stabilisation de $(K_k)$ et $(I_k)$.
        Pour montrer $I_k = I_p$ pour tout $k \ge p$:
        Nous savons déjà que $I_k \subseteq I_p$ (car la suite est décroissante).
        Il reste à montrer $I_p \subseteq I_k$.
        Puisque $I_p = I_{p+1}$, cela signifie que pour tout $y \in I_p$, $y \in I_{p+1}$, donc $y = u^{p+1}(x')$ pour un certain $x' \in E$.
        Plus généralement, si $I_j = I_{j+1}$, alors l'application $u$ restreinte à $I_j$ est surjective de $I_j$ dans $I_j$. En effet, $u(I_j) = u(\mathrm{Im}(u^j)) = \mathrm{Im}(u^{j+1}) = I_{j+1} = I_j$. Étant surjective sur un espace de dimension finie, elle est un automorphisme.
        Donc $u|_{I_p} : I_p \to I_p$ est un automorphisme.
        Ceci signifie que $u(I_p) = I_p$. Par conséquent $u^2(I_p) = u(I_p) = I_p$, et par récurrence $u^k(I_p) = I_p$ pour tout $k \ge 0$.
        En particulier, $u^k(E) = u^k(I_0) \supseteq u^k(I_p)$.
        Soit $y \in I_p$. Alors $y = u^p(x)$ pour un certain $x \in E$.
        Puisque $I_p = I_k$ pour $k \ge p$, et on sait que $I_k \subseteq I_p$.
        Si $y \in I_p$, alors $y = u^p(x)$. Mais on a montré que $u|_{I_p}$ est un automorphisme.
        Donc $u^k|_{I_p}$ est aussi un automorphisme pour tout $k \ge 0$.
        Conséquence : $\mathrm{Im}(u^k|_{I_p}) = I_p$.
        Mais $\mathrm{Im}(u^k|_{I_p})$ est l'ensemble des éléments de la forme $u^k(z)$ où $z \in I_p$.
        C'est donc un sous-ensemble de $I_k$.
        Non, c'est $u^k(I_p)$. Et nous avons montré que $u^k(I_p) = I_p$.
        Donc $I_p \subseteq I_k$ pour $k \ge p$.
        Puisque nous avons aussi $I_k \subseteq I_p$, il s'ensuit que $I_k = I_p$ pour tout $k \ge p$.

3.  **Décomposition $E = K_p \oplus I_p$**

    Pour montrer que $E = K_p \oplus I_p$, nous devons montrer deux choses :
    a. $K_p \cap I_p = \{0\}$
    b. $K_p + I_p = E$ (ou de manière équivalente $\mathrm{dim}(K_p) + \mathrm{dim}(I_p) = \mathrm{dim}(E)$ si $K_p \cap I_p = \{0\}$)

    *   **a. $K_p \cap I_p = \{0\}$ :**
        Soit $y \in K_p \cap I_p$.
        Puisque $y \in K_p$, on a $u^p(y) = 0$.
        Puisque $y \in I_p$, il existe un $x \in E$ tel que $y = u^p(x)$.
        En substituant, nous obtenons $u^p(u^p(x)) = 0$, c'est-à-dire $u^{2p}(x) = 0$.
        Cela signifie que $x \in K_{2p}$.
        Or, d'après la question 2, puisque $p$ est l'indice de stabilisation, nous avons $K_{2p} = K_p$ (car $2p \ge p$).
        Donc $x \in K_p$.
        Par conséquent, $u^p(x) = 0$.
        Puisque $y = u^p(x)$, on en déduit $y = 0$.
        Donc $K_p \cap I_p = \{0\}$.

    *   **b. $K_p + I_p = E$ :**
        D'après le théorème du rang appliqué à $u^p$:
        $\mathrm{dim}(E) = \mathrm{dim}(\ker(u^p)) + \mathrm{dim}(\mathrm{Im}(u^p))$
        $\mathrm{dim}(E) = \mathrm{dim}(K_p) + \mathrm{dim}(I_p)$.
        Puisque $K_p \cap I_p = \{0\}$, la somme $K_p + I_p$ est directe, et sa dimension est $\mathrm{dim}(K_p \oplus I_p) = \mathrm{dim}(K_p) + \mathrm{dim}(I_p)$.
        Donc $\mathrm{dim}(K_p \oplus I_p) = \mathrm{dim}(E)$.
        Puisque $K_p \oplus I_p$ est un sous-espace vectoriel de $E$ et qu'il a la même dimension que $E$, il est égal à $E$.
        Ainsi, $E = K_p \oplus I_p$.

4.  **Stabilité par $u$, nilpotence et automorphisme**

    *   **Stabilité des sous-espaces $K_p$ et $I_p$ par $u$ :**
        *   **Pour $K_p$ :**
            Soit $x \in K_p$. Alors $u^p(x) = 0$.
            Nous devons montrer que $u(x) \in K_p$.
            Calculons $u^p(u(x))$. C'est $u^{p+1}(x)$.
            D'après la question 2, $K_p = K_{p+1}$ (par définition de $p$).
            Puisque $x \in K_p$, $u^p(x)=0$. On peut dire que $x \in K_{p+1}$ également.
            Or $K_p = K_{p+1}$ signifie que si $u^{p+1}(x) = 0$, alors $u^p(x) = 0$.
            Ah, wait. $u(x) \in K_p$ requires $u^p(u(x))=0$.
            We know $u^p(x)=0$. So $x \in K_p$.
            We want to check if $u(x) \in K_p$. This means $u^p(u(x))=0$, i.e. $u^{p+1}(x)=0$.
            Since $x \in K_p$ and $K_p = K_{p+1}$, it implies that $x \in K_{p+1}$, so $u^{p+1}(x)=0$ holds.
            Therefore, $u(x) \in K_p$.
            Ceci prouve que $K_p$ est stable par $u$.

        *   **Pour $I_p$ :**
            Soit $y \in I_p$. Alors il existe $x \in E$ tel que $y = u^p(x)$.
            Nous devons montrer que $u(y) \in I_p$.
            Calculons $u(y) = u(u^p(x)) = u^{p+1}(x)$.
            Par définition, $u^{p+1}(x) \in \mathrm{Im}(u^{p+1}) = I_{p+1}$.
            D'après la question 2, $I_p = I_{p+1}$ (car $p$ est l'indice de stabilisation).
            Donc $u(y) \in I_p$.
            Ceci prouve que $I_p$ est stable par $u$.

    *   **Nature des endomorphismes $u_K$ et $u_I$ :**
        *   **Pour $u_K : K_p \to K_p$ :**
            Par définition, $u_K(x) = u(x)$ pour $x \in K_p$.
            Pour tout $x \in K_p$, nous avons $u^p(x) = 0$.
            Donc $u_K^p(x) = u^p(x) = 0$.
            Ceci signifie que $u_K^p$ est l'endomorphisme nul sur $K_p$.
            Par conséquent, $u_K$ est un endomorphisme nilpotent.

        *   **Pour $u_I : I_p \to I_p$ :**
            Par définition, $u_I(y) = u(y)$ pour $y \in I_p$.
            Nous savons que $u_I$ est un endomorphisme de $I_p$.
            Pour montrer que $u_I$ est un automorphisme, il suffit de montrer qu'il est injectif ou surjectif, car $I_p$ est de dimension finie.
            Montrons que $u_I$ est surjectif.
            L'image de $u_I$ est $\mathrm{Im}(u_I) = \{u(y) \mid y \in I_p\}$.
            Puisque $y \in I_p = \mathrm{Im}(u^p)$, il existe $x \in E$ tel que $y = u^p(x)$.
            Alors $u(y) = u(u^p(x)) = u^{p+1}(x)$.
            Ainsi, $\mathrm{Im}(u_I) = \{u^{p+1}(x) \mid x \in E\} = \mathrm{Im}(u^{p+1}) = I_{p+1}$.
            D'après la question 2, nous savons que $I_{p+1} = I_p$.
            Donc $\mathrm{Im}(u_I) = I_p$.
            Ceci signifie que $u_I$ est surjectif.
            Puisque $u_I$ est un endomorphisme d'un espace de dimension finie $I_p$ et qu'il est surjectif, il est également injectif.
            Par conséquent, $u_I$ est un automorphisme de $I_p$.

Cette décomposition $E = K_p \oplus I_p$ est connue sous le nom de **Décomposition de Fitting**, et elle est fondamentale dans l'étude des endomorphismes en dimension finie, notamment pour la forme de Jordan ou la décomposition de Dunford.