# Exercice 8 : Indice de Fitting et Décomposition de Fitting (Difficulté : ****)

Soit $\mathbb{K}$ un corps commutatif.
Soit $E$ un espace vectoriel sur $\mathbb{K}$ de dimension finie $n \ge 1$.
Soit $f \in \mathcal{L}(E)$ un endomorphisme de $E$.
On définit l'application $f^0 = \text{Id}_E$ (l'application identité sur $E$), et pour tout entier $k \in \mathbb{N}$, $f^{k+1} = f \circ f^k$.

---

## Énoncé du problème

1.  **Analyse des Noyaux**
    a.  Montrer que la suite des noyaux $(\ker(f^k))_{k \in \mathbb{N}}$ est une suite croissante de sous-espaces vectoriels de $E$, c'est-à-dire, montrer que $\ker(f^k) \subseteq \ker(f^{k+1})$ pour tout $k \in \mathbb{N}$.
    b.  Justifier que cette suite de sous-espaces vectoriels doit nécessairement stabiliser. On notera $d_0$ le plus petit entier naturel tel que $\ker(f^{d_0}) = \ker(f^{d_0+1})$.
    c.  Montrer que pour tout entier $k \ge d_0$, on a $\ker(f^k) = \ker(f^{d_0})$.

2.  **Analyse des Images**
    a.  Montrer que la suite des images $(\text{Im}(f^k))_{k \in \mathbb{N}}$ est une suite décroissante de sous-espaces vectoriels de $E$, c'est-à-dire, montrer que $\text{Im}(f^{k+1}) \subseteq \text{Im}(f^k)$ pour tout $k \in \mathbb{N}$.
    b.  Justifier que cette suite de sous-espaces vectoriels doit nécessairement stabiliser. On notera $p_0$ le plus petit entier naturel tel que $\text{Im}(f^{p_0}) = \text{Im}(f^{p_0+1})$.
    c.  Montrer que pour tout entier $k \ge p_0$, on a $\text{Im}(f^k) = \text{Im}(f^{p_0})$.

3.  **Lien entre Noyau et Image (Théorème du Rang)**
    a.  En utilisant le théorème du rang, montrer que $d_0 = p_0$. On notera $k_0$ cette valeur commune, appelée l'indice de Fitting de $f$.
    b.  Montrer que la restriction de $f$ à $\text{Im}(f^{k_0})$ induit un automorphisme de $\text{Im}(f^{k_0})$, c'est-à-dire que $f|_{\text{Im}(f^{k_0})} : \text{Im}(f^{k_0}) \to \text{Im}(f^{k_0})$ est un isomorphisme.

4.  **Décomposition de Fitting**
    a.  Montrer que $\ker(f^{k_0}) \cap \text{Im}(f^{k_0}) = \{0_E\}$, où $0_E$ est le vecteur nul de $E$.
    b.  En déduire que $E = \ker(f^{k_0}) \oplus \text{Im}(f^{k_0})$.

---

## Correction détaillée

1.  **Analyse des Noyaux**

    a.  Pour montrer que $\ker(f^k) \subseteq \ker(f^{k+1})$ pour tout $k \in \mathbb{N}$ :
        Soit $x \in \ker(f^k)$. Par définition du noyau d'une application linéaire, cela signifie que $f^k(x) = 0_E$.
        Appliquons l'endomorphisme $f$ à cette égalité. Puisque $f$ est linéaire, $f(0_E) = 0_E$.
        Nous obtenons $f(f^k(x)) = f(0_E)$, ce qui se simplifie en $f^{k+1}(x) = 0_E$ par définition de la composition des applications.
        L'égalité $f^{k+1}(x) = 0_E$ signifie que $x$ appartient au noyau de $f^{k+1}$, c'est-à-dire $x \in \ker(f^{k+1})$.
        Par conséquent, tout élément de $\ker(f^k)$ est aussi un élément de $\ker(f^{k+1})$, d'où l'inclusion $\ker(f^k) \subseteq \ker(f^{k+1})$ pour tout $k \in \mathbb{N}$.

    b.  La suite $(\ker(f^k))_{k \in \mathbb{N}}$ est une suite croissante de sous-espaces vectoriels de $E$.
        Puisque $E$ est un espace vectoriel de dimension finie $n$, la dimension de chaque sous-espace vectoriel $\ker(f^k)$ est un entier naturel. Cette dimension est bornée supérieurement par la dimension de $E$, c'est-à-dire $n$.
        Nous avons la suite d'inégalités de dimensions :
        $0 \le \dim(\ker(f^0)) \le \dim(\ker(f^1)) \le \dim(\ker(f^2)) \le \dots \le \dim(E) = n$.
        Une suite croissante d'entiers naturels qui est bornée supérieurement converge et donc doit nécessairement stabiliser à partir d'un certain rang.
        Si la dimension $\dim(\ker(f^k))$ est égale à $\dim(\ker(f^{k+1}))$, et comme nous avons déjà établi l'inclusion $\ker(f^k) \subseteq \ker(f^{k+1})$, l'égalité des dimensions implique que les deux sous-espaces vectoriels sont identiques : $\ker(f^k) = \ker(f^{k+1})$.
        Ainsi, la suite des noyaux doit stabiliser. Par le principe du bon ordre des entiers naturels, il existe un plus petit entier naturel $d_0$ tel que $\ker(f^{d_0}) = \ker(f^{d_0+1})$.

    c.  Nous montrons par récurrence sur $k$ que pour tout $k \ge d_0$, on a $\ker(f^k) = \ker(f^{d_0})$.
        *   **Initialisation (k = d_0) :** La propriété est vraie par définition de $d_0$, puisque $\ker(f^{d_0}) = \ker(f^{d_0+1})$.
        *   **Hypothèse de récurrence :** Supposons que pour un certain entier $k \ge d_0$, on ait $\ker(f^k) = \ker(f^{d_0})$.
        *   **Hérédité :** Démontrons que $\ker(f^{k+1}) = \ker(f^{d_0})$.
            Nous savons d'après 1.a que $\ker(f^k) \subseteq \ker(f^{k+1})$. Par transitivité, $\ker(f^{d_0}) = \ker(f^k) \subseteq \ker(f^{k+1})$.
            Il reste à prouver l'inclusion inverse : $\ker(f^{k+1}) \subseteq \ker(f^{d_0})$.
            Soit $x \in \ker(f^{k+1})$. Par définition, $f^{k+1}(x) = 0_E$.
            On peut écrire $f^{k+1}(x) = f^k(f(x))$. Donc $f^k(f(x)) = 0_E$.
            Ceci signifie que $f(x) \in \ker(f^k)$.
            D'après l'hypothèse de récurrence, $\ker(f^k) = \ker(f^{d_0})$.
            Par conséquent, $f(x) \in \ker(f^{d_0})$.
            Cela implique que $f^{d_0}(f(x)) = 0_E$, ce qui est équivalent à $f^{d_0+1}(x) = 0_E$.
            Puisque, par définition de $d_0$, nous avons $\ker(f^{d_0+1}) = \ker(f^{d_0})$, l'égalité $f^{d_0+1}(x) = 0_E$ signifie que $x \in \ker(f^{d_0})$.
            Ainsi, $\ker(f^{k+1}) \subseteq \ker(f^{d_0})$.
            En combinant les inclusions, nous avons $\ker(f^{k+1}) = \ker(f^{d_0})$.
        Par le principe de récurrence, pour tout $k \ge d_0$, l'égalité $\ker(f^k) = \ker(f^{d_0})$ est établie.

2.  **Analyse des Images**

    a.  Pour montrer que $\text{Im}(f^{k+1}) \subseteq \text{Im}(f^k)$ pour tout $k \in \mathbb{N}$ :
        Soit $y \in \text{Im}(f^{k+1})$. Par définition de l'image, il existe un vecteur $x \in E$ tel que $y = f^{k+1}(x)$.
        On peut réécrire $f^{k+1}(x)$ comme $f^k(f(x))$.
        Posons $x' = f(x)$. Alors $x'$ est un vecteur de $E$.
        L'égalité devient $y = f^k(x')$.
        Ceci signifie que $y$ appartient à l'image de $f^k$, c'est-à-dire $y \in \text{Im}(f^k)$.
        Par conséquent, $\text{Im}(f^{k+1}) \subseteq \text{Im}(f^k)$ pour tout $k \in \mathbb{N}$.

    b.  La suite $(\text{Im}(f^k))_{k \in \mathbb{N}}$ est une suite décroissante de sous-espaces vectoriels de $E$.
        Puisque $E$ est un espace vectoriel de dimension finie $n$, la dimension de chaque sous-espace vectoriel $\text{Im}(f^k)$ est un entier naturel, bornée inférieurement par 0.
        Nous avons la suite d'inégalités de dimensions :
        $n = \dim(E) \ge \dim(\text{Im}(f^0)) \ge \dim(\text{Im}(f^1)) \ge \dim(\text{Im}(f^2)) \ge \dots \ge 0$.
        Une suite décroissante d'entiers naturels qui est bornée inférieurement doit nécessairement stabiliser à partir d'un certain rang.
        Si la dimension $\dim(\text{Im}(f^k))$ est égale à $\dim(\text{Im}(f^{k+1}))$, et comme nous avons déjà établi l'inclusion $\text{Im}(f^{k+1}) \subseteq \text{Im}(f^k)$, l'égalité des dimensions implique que les deux sous-espaces vectoriels sont identiques : $\text{Im}(f^k) = \text{Im}(f^{k+1})$.
        Ainsi, la suite des images doit stabiliser. Par le principe du bon ordre des entiers naturels, il existe un plus petit entier naturel $p_0$ tel que $\text{Im}(f^{p_0}) = \text{Im}(f^{p_0+1})$.

    c.  Nous devons montrer que pour tout $k \ge p_0$, on a $\text{Im}(f^k) = \text{Im}(f^{p_0})$.
        Par définition de $p_0$, nous avons $\text{Im}(f^{p_0}) = \text{Im}(f^{p_0+1})$.
        Considérons la restriction de $f$ à $\text{Im}(f^{p_0})$. Notons cette application $g = f|_{\text{Im}(f^{p_0})} : \text{Im}(f^{p_0}) \to E$.
        L'image de cette application est $g(\text{Im}(f^{p_0})) = f(\text{Im}(f^{p_0})) = f(f^{p_0}(E)) = f^{p_0+1}(E) = \text{Im}(f^{p_0+1})$.
        Puisque $\text{Im}(f^{p_0}) = \text{Im}(f^{p_0+1})$, cela signifie que l'image de $g$ est $\text{Im}(f^{p_0})$.
        Ainsi, $g: \text{Im}(f^{p_0}) \to \text{Im}(f^{p_0})$ est un endomorphisme de l'espace $\text{Im}(f^{p_0})$.
        De plus, puisque l'image de $g$ est $\text{Im}(f^{p_0})$ lui-même, cet endomorphisme $g$ est surjectif.
        Comme $\text{Im}(f^{p_0})$ est un sous-espace vectoriel de $E$, il est de dimension finie. Pour un espace vectoriel de dimension finie, un endomorphisme surjectif est aussi injectif, et donc un automorphisme.
        Par conséquent, $f|_{\text{Im}(f^{p_0})} : \text{Im}(f^{p_0}) \to \text{Im}(f^{p_0})$ est un automorphisme.
        Cela signifie que pour tout entier $k \ge 1$, la $k$-ième composition de $f|_{\text{Im}(f^{p_0})}$ sur lui-même, notée $(f|_{\text{Im}(f^{p_0})})^k$, est également un automorphisme de $\text{Im}(f^{p_0})$.
        En particulier, $(f|_{\text{Im}(f^{p_0})})^k$ est surjective, ce qui implique que $f^k(\text{Im}(f^{p_0})) = \text{Im}(f^{p_0})$ pour tout $k \ge 1$.
        Par définition, $f^k(\text{Im}(f^{p_0})) = f^k(f^{p_0}(E)) = f^{k+p_0}(E) = \text{Im}(f^{k+p_0})$.
        En combinant ces résultats, nous obtenons $\text{Im}(f^{p_0+k}) = \text{Im}(f^{p_0})$ pour tout $k \ge 1$.
        Ceci démontre que pour tout $k \ge p_0$, on a $\text{Im}(f^k) = \text{Im}(f^{p_0})$.

3.  **Lien entre Noyau et Image (Théorème du Rang)**

    a.  Le théorème du rang affirme que pour toute application linéaire $L: V \to W$ où $V$ est de dimension finie, on a $\dim(V) = \dim(\ker(L)) + \dim(\text{Im}(L))$.
        Appliquons ce théorème à l'endomorphisme $f^k: E \to E$ pour tout $k \in \mathbb{N}$. L'espace $E$ est de dimension finie $n$.
        Donc, $n = \dim(\ker(f^k)) + \dim(\text{Im}(f^k))$.

        *   Montrons que $p_0 \le d_0$ :
            Par définition de $d_0$, nous avons $\ker(f^{d_0}) = \ker(f^{d_0+1})$.
            Ceci implique que $\dim(\ker(f^{d_0})) = \dim(\ker(f^{d_0+1}))$.
            En utilisant le théorème du rang pour $f^{d_0}$ et $f^{d_0+1}$ :
            $\dim(\text{Im}(f^{d_0})) = n - \dim(\ker(f^{d_0}))$
            $\dim(\text{Im}(f^{d_0+1})) = n - \dim(\ker(f^{d_0+1}))$
            Puisque $\dim(\ker(f^{d_0})) = \dim(\ker(f^{d_0+1}))$, il s'ensuit que $\dim(\text{Im}(f^{d_0})) = \dim(\text{Im}(f^{d_0+1}))$.
            Comme nous savons que $\text{Im}(f^{d_0+1}) \subseteq \text{Im}(f^{d_0})$ (d'après 2.a), l'égalité des dimensions implique que $\text{Im}(f^{d_0}) = \text{Im}(f^{d_0+1})$.
            Par définition, $p_0$ est le plus petit entier tel que $\text{Im}(f^{p_0}) = \text{Im}(f^{p_0+1})$. Puisque cette égalité est vérifiée pour $d_0$, nous devons avoir $p_0 \le d_0$.

        *   Montrons que $d_0 \le p_0$ :
            Par définition de $p_0$, nous avons $\text{Im}(f^{p_0}) = \text{Im}(f^{p_0+1})$.
            Ceci implique que $\dim(\text{Im}(f^{p_0})) = \dim(\text{Im}(f^{p_0+1}))$.
            En utilisant le théorème du rang pour $f^{p_0}$ et $f^{p_0+1}$ :
            $\dim(\ker(f^{p_0})) = n - \dim(\text{Im}(f^{p_0}))$
            $\dim(\ker(f^{p_0+1})) = n - \dim(\text{Im}(f^{p_0+1}))$
            Puisque $\dim(\text{Im}(f^{p_0})) = \dim(\text{Im}(f^{p_0+1}))$, il s'ensuit que $\dim(\ker(f^{p_0})) = \dim(\ker(f^{p_0+1}))$.
            Comme nous savons que $\ker(f^{p_0}) \subseteq \ker(f^{p_0+1})$ (d'après 1.a), l'égalité des dimensions implique que $\ker(f^{p_0}) = \ker(f^{p_0+1})$.
            Par définition, $d_0$ est le plus petit entier tel que $\ker(f^{d_0}) = \ker(f^{d_0+1})$. Puisque cette égalité est vérifiée pour $p_0$, nous devons avoir $d_0 \le p_0$.

        Des deux inégalités $p_0 \le d_0$ et $d_0 \le p_0$, nous concluons que $d_0 = p_0$. Nous noterons cette valeur commune $k_0$.

    b.  D'après la question 2.c, la condition $\text{Im}(f^{p_0}) = \text{Im}(f^{p_0+1})$ implique que la restriction de $f$ à $\text{Im}(f^{p_0})$, soit $f|_{\text{Im}(f^{p_0})}$, est un automorphisme de $\text{Im}(f^{p_0})$.
        En utilisant $k_0 = p_0$, cela signifie que $f|_{\text{Im}(f^{k_0})} : \text{Im}(f^{k_0}) \to \text{Im}(f^{k_0})$ est un endomorphisme dont l'image est $\text{Im}(f^{k_0+1})$, qui est égale à $\text{Im}(f^{k_0})$.
        Par conséquent, $f|_{\text{Im}(f^{k_0})}$ est un endomorphisme surjectif de $\text{Im}(f^{k_0})$.
        Puisque $\text{Im}(f^{k_0})$ est un sous-espace vectoriel de $E$, il est de dimension finie.
        Dans un espace vectoriel de dimension finie, un endomorphisme surjectif est nécessairement bijectif (et donc injectif).
        Ainsi, $f|_{\text{Im}(f^{k_0})}$ est un isomorphisme (un automorphisme) de $\text{Im}(f^{k_0})$ sur lui-même.

4.  **Décomposition de Fitting**

    a.  Nous devons montrer que $\ker(f^{k_0}) \cap \text{Im}(f^{k_0}) = \{0_E\}$.
        Soit $x \in \ker(f^{k_0}) \cap \text{Im}(f^{k_0})$.
        Puisque $x \in \ker(f^{k_0})$, par définition, $f^{k_0}(x) = 0_E$.
        Puisque $x \in \text{Im}(f^{k_0})$, par définition, il existe un vecteur $y \in E$ tel que $x = f^{k_0}(y)$.
        Substituons cette expression de $x$ dans la première égalité :
        $f^{k_0}(f^{k_0}(y)) = 0_E$.
        Ceci s'écrit $f^{2k_0}(y) = 0_E$.
        Cela implique que $y \in \ker(f^{2k_0})$.
        D'après la question 1.c, nous savons que pour tout $k \ge d_0$, $\ker(f^k) = \ker(f^{d_0})$. Puisque $k_0 = d_0$, cette propriété s'applique à $k_0$.
        En particulier, puisque $2k_0 \ge k_0$ (tout en supposant $k_0 \ge 0$; si $k_0=0$, $\ker(f^0)=\{0_E\}$, alors $\ker(f^{2\cdot 0})=\ker(f^0)$), nous avons $\ker(f^{2k_0}) = \ker(f^{k_0})$.
        Par conséquent, $y \in \ker(f^{k_0})$.
        Cela signifie que $f^{k_0}(y) = 0_E$.
        Puisque nous avions posé $x = f^{k_0}(y)$, nous en déduisons que $x = 0_E$.
        Ainsi, le seul élément de l'intersection de $\ker(f^{k_0})$ et $\text{Im}(f^{k_0})$ est le vecteur nul, donc $\ker(f^{k_0}) \cap \text{Im}(f^{k_0}) = \{0_E\}$.

    b.  Pour prouver que $E = \ker(f^{k_0}) \oplus \text{Im}(f^{k_0})$, il suffit de montrer deux conditions pour les sous-espaces vectoriels $U = \ker(f^{k_0})$ et $V = \text{Im}(f^{k_0})$ :
        i.  Leur intersection est triviale : $U \cap V = \{0_E\}$. Cette condition a été démontrée à la question 4.a.
        ii. La somme de leurs dimensions est égale à la dimension de l'espace ambiant : $\dim(U) + \dim(V) = \dim(E)$.
            Appliquons le théorème du rang à l'endomorphisme $f^{k_0} : E \to E$:
            $\dim(E) = \dim(\ker(f^{k_0})) + \dim(\text{Im}(f^{k_0}))$.
            Cette condition est également vérifiée.

        Étant donné que ces deux conditions sont satisfaites, nous pouvons conclure que l'espace vectoriel $E$ est la somme directe de $\ker(f^{k_0})$ et $\text{Im}(f^{k_0})$.
        Ainsi, $E = \ker(f^{k_0}) \oplus \text{Im}(f^{k_0})$.