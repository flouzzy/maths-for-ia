# Exercice 04

Cet exercice profond explore les liens intimes entre la complétude des espaces fonctionnels, la continuité des opérateurs linéaires, et les outils fondamentaux de l'Analyse Fonctionnelle : le Théorème de l'Application Ouverte et le Théorème du Graphe Fermé. Nous examinerons l'opérateur de dérivation sur des espaces de fonctions continûment différentiables, révélant la subtilité de la notion de complétude.

Difficulté : $\bigstar$\bigstar\star\star\star$

---

**Énoncé de l'Exercice**

Soit $X = C([0,1])$ l'espace des fonctions réelles continues sur l'intervalle $[0,1]$, muni de la norme du supremum $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$. Il est bien connu que $(X, \|\cdot\|_\infty)$ est un espace de Banach.

Soit $Y = C^1([0,1])$ l'espace des fonctions réelles continûment différentiables sur $[0,1]$.
Nous munissons $Y$ de deux normes distinctes :
\begin{enumerate}
    \item La norme de la convergence uniforme : $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$.
    \item La norme $C^1$ : $\|f\|_{C^1} = \|f\|_\infty + \|f'\|_\infty$.
\end{enumerate}

---

**Partie I : Équivalence de Normes et Théorème de l'Isomorphisme de Banach**

1.  Démontrer que $(Y, \|\cdot\|_{C^1})$ est un espace de Banach.
2.  Considérons l'opérateur identité $I : (Y, \|\cdot\|_{C^1}) \to (Y, \|\cdot\|_\infty)$, défini par $I(f) = f$.
    \begin{enumerate}
        \item Montrer que $I$ est un opérateur linéaire borné.
        \item Montrer que l'opérateur inverse $I^{-1} : (Y, \|\cdot\|_\infty) \to (Y, \|\cdot\|_{C^1})$ n'est pas borné.
        \item En déduire, en utilisant le Théorème de l'Isomorphisme de Banach (ou le Théorème de l'Application Ouverte), que $(Y, \|\cdot\|_\infty)$ n'est pas un espace de Banach.
    \end{enumerate}

---

**Partie II : L'Opérateur de Dérivation et le Théorème du Graphe Fermé**

Soit $D : (Y, \|\cdot\|_\infty) \to (X, \|\cdot\|_\infty)$ l'opérateur de dérivation défini par $D(f) = f'$.

1.  Montrer que $D$ est un opérateur linéaire.
2.  Démontrer que $D$ n'est pas borné.
3.  Soit $\mathcal{G}(D)$ le graphe de $D$, défini comme l'ensemble des couples $(f, Df)$ dans $(Y, \|\cdot\|_\infty) \times (X, \|\cdot\|_\infty)$. Démontrer que $\mathcal{G}(D)$ est fermé dans l'espace produit $(Y, \|\cdot\|_\infty) \times (X, \|\cdot\|_\infty)$. (Rappel : La convergence dans $Y$ munie de $\|\cdot\|_\infty$ est la convergence uniforme des fonctions. La convergence dans $X$ munie de $\|\cdot\|_\infty$ est également la convergence uniforme.)
4.  À la lumière des résultats précédents et du Théorème du Graphe Fermé, quelle conclusion peut-on tirer sur l'espace $(Y, \|\cdot\|_\infty)$ ? Comparer cette conclusion avec celle obtenue dans la Partie I.

---

**Correction Détaillée**

**Partie I : Équivalence de Normes et Théorème de l'Isomorphisme de Banach**

1.  **Démonstration que $(Y, \|\cdot\|_{C^1})$ est un espace de Banach.**

    Pour montrer que $(Y, \|\cdot\|_{C^1})$ est un espace de Banach, nous devons prouver qu'il est complet. Pour ce faire, nous allons prendre une suite de Cauchy arbitraire dans $Y$ munie de la norme $\|\cdot\|_{C^1}$ et montrer qu'elle converge vers un élément de $Y$ sous cette même norme.

    Soit $(f_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $(Y, \|\cdot\|_{C^1})$.
    Par définition, cela signifie que pour tout $\varepsilon > 0$, il existe un entier $N$ tel que pour tout $n, m \ge N$, nous avons :
    $$ \|f_n - f_m\|_{C^1} < \varepsilon $$
    En utilisant la définition de la norme $\|\cdot\|_{C^1}$, cela s'écrit :
    $$ \|f_n - f_m\|_\infty + \|f_n' - f_m'\|_\infty < \varepsilon $$
    Cette inégalité implique que :
    $$ \|f_n - f_m\|_\infty < \varepsilon \quad \text{et} \quad \|f_n' - f_m'\|_\infty < \varepsilon $$
    Ceci nous montre que $(f_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $(X, \|\cdot\|_\infty)$ et que $(f_n')_{n \in \mathbb{N}}$ est également une suite de Cauchy dans $(X, \|\cdot\|_\infty)$.

    Puisque $(X, \|\cdot\|_\infty)$ est un espace de Banach (par hypothèse), toute suite de Cauchy dans cet espace converge.
    Par conséquent, il existe une fonction $f \in X$ telle que $f_n \xrightarrow{\|\cdot\|_\infty} f$, c'est-à-dire $f_n \to f$ uniformément sur $[0,1]$.
    De même, il existe une fonction $g \in X$ telle que $f_n' \xrightarrow{\|\cdot\|_\infty} g$, c'est-à-dire $f_n' \to g$ uniformément sur $[0,1]$.

    Maintenant, nous devons montrer que la fonction limite $f$ appartient à $Y$, c'est-à-dire que $f$ est continûment différentiable sur $[0,1]$, et que sa dérivée est $g$.
    Utilisons le théorème fondamental du calcul. Pour tout $x_0, x \in [0,1]$, nous avons :
    $$ f_n(x) - f_n(x_0) = \int_{x_0}^x f_n'(t) dt $$
    Puisque $f_n \to f$ uniformément sur $[0,1]$, nous pouvons prendre la limite sous le signe de la fonction pour le membre de gauche :
    $$ \lim_{n \to \infty} (f_n(x) - f_n(x_0)) = f(x) - f(x_0) $$
    Puisque $f_n' \to g$ uniformément sur $[0,1]$ et que les fonctions $f_n'$ sont continues (car $f_n \in C^1([0,1])$), la fonction limite $g$ est également continue. De plus, par le théorème d'interversion des limites et de l'intégration pour la convergence uniforme, nous avons :
    $$ \lim_{n \to \infty} \int_{x_0}^x f_n'(t) dt = \int_{x_0}^x g(t) dt $$
    En combinant ces deux résultats, nous obtenons :
    $$ f(x) - f(x_0) = \int_{x_0}^x g(t) dt $$
    Par le Théorème Fondamental du Calcul, puisque $g$ est une fonction continue, la fonction $x \mapsto \int_{x_0}^x g(t) dt$ est différentiable, et sa dérivée est $g(x)$.
    Par conséquent, $f$ est différentiable sur $[0,1]$ et $f'(x) = g(x)$ pour tout $x \in [0,1]$.
    Puisque $g$ est continue (comme limite uniforme de fonctions continues), $f'$ est continue. Ainsi, $f \in C^1([0,1])$, ce qui signifie $f \in Y$.

    Enfin, nous devons vérifier que $f_n$ converge vers $f$ sous la norme $\|\cdot\|_{C^1}$.
    Nous avons :
    $$ \|f_n - f\|_{C^1} = \|f_n - f\|_\infty + \|f_n' - f'\|_\infty $$
    Nous savons que $f_n \xrightarrow{\|\cdot\|_\infty} f$ et $f_n' \xrightarrow{\|\cdot\|_\infty} g = f'$. Par conséquent :
    $$ \lim_{n \to \infty} \|f_n - f\|_\infty = 0 \quad \text{et} \quad \lim_{n \to \infty} \|f_n' - f'\|_\infty = 0 $$
    Donc, $\lim_{n \to \infty} \|f_n - f\|_{C^1} = 0$.
    La suite de Cauchy $(f_n)$ converge bien vers $f \in Y$ dans l'espace $(Y, \|\cdot\|_{C^1})$.
    Ceci prouve que $(Y, \|\cdot\|_{C^1})$ est un espace de Banach.

2.  **L'opérateur identité $I : (Y, \|\cdot\|_{C^1}) \to (Y, \|\cdot\|_\infty)$**

    a.  **Montrer que $I$ est un opérateur linéaire borné.**
        *   **Linéarité :** Pour tout $f, g \in Y$ et tout scalaire $\alpha \in \mathbb{R}$ :
            $I(f+g) = f+g = I(f)+I(g)$.
            $I(\alpha f) = \alpha f = \alpha I(f)$.
            $I$ est donc un opérateur linéaire.
        *   **Borné (ou Continu) :** Nous devons trouver une constante $M > 0$ telle que $\|I(f)\|_\infty \le M \|f\|_{C^1}$ pour tout $f \in Y$.
            Par définition, $\|I(f)\|_\infty = \|f\|_\infty$.
            Et $\|f\|_{C^1} = \|f\|_\infty + \|f'\|_\infty$.
            Nous avons clairement $\|f\|_\infty \le \|f\|_\infty + \|f'\|_\infty = \|f\|_{C^1}$.
            Nous pouvons choisir $M=1$.
            Donc, $I$ est un opérateur linéaire borné.

    b.  **Montrer que l'opérateur inverse $I^{-1} : (Y, \|\cdot\|_\infty) \to (Y, \|\cdot\|_{C^1})$ n'est pas borné.**

        L'opérateur $I^{-1}$ prend une fonction $f$ de $(Y, \|\cdot\|_\infty)$ et la renvoie en tant que fonction de $(Y, \|\cdot\|_{C^1})$. S'il était borné, il existerait une constante $M > 0$ telle que pour tout $f \in Y$ :
        $$ \|I^{-1}(f)\|_{C^1} \le M \|f\|_\infty $$
        Ceci signifie $\|f\|_{C^1} \le M \|f\|_\infty$.
        Considérons la suite de fonctions $(f_n)_{n \in \mathbb{N}^*}$ définie par $f_n(x) = \frac{1}{n} \sin(n^2 x)$ pour $x \in [0,1]$.
        Chaque $f_n$ est continûment différentiable, donc $f_n \in Y$.
        Calculons les normes :
        *   $\|f_n\|_\infty = \sup_{x \in [0,1]} \left|\frac{1}{n} \sin(n^2 x)\right| = \frac{1}{n} \sup_{x \in [0,1]} |\sin(n^2 x)| = \frac{1}{n} \cdot 1 = \frac{1}{n}$.
        *   Calculons la dérivée $f_n'(x) = \frac{1}{n} (n^2) \cos(n^2 x) = n \cos(n^2 x)$.
        *   $\|f_n'\|_\infty = \sup_{x \in [0,1]} |n \cos(n^2 x)| = n \sup_{x \in [0,1]} |\cos(n^2 x)| = n \cdot 1 = n$.
        *   Alors, $\|f_n\|_{C^1} = \|f_n\|_\infty + \|f_n'\|_\infty = \frac{1}{n} + n$.

        Si $I^{-1}$ était borné, nous aurions $\frac{1}{n} + n \le M \left(\frac{1}{n}\right)$ pour tout $n \in \mathbb{N}^*$.
        Multiplions par $n$ (qui est positif) : $1 + n^2 \le M$.
        Cette inégalité $1+n^2 \le M$ ne peut pas être vraie pour tout $n \in \mathbb{N}^*$, car le membre de gauche $1+n^2$ tend vers l'infini lorsque $n \to \infty$.
        Par conséquent, $I^{-1}$ n'est pas borné.

    c.  **En déduire, en utilisant le Théorème de l'Isomorphisme de Banach (ou Théorème de l'Application Ouverte), que $(Y, \|\cdot\|_\infty)$ n'est pas un espace de Banach.**

        Le Théorème de l'Isomorphisme de Banach (qui est un corollaire direct du Théorème de l'Application Ouverte) stipule que si $T: E \to F$ est un opérateur linéaire borné et bijectif entre deux espaces de Banach $E$ et $F$, alors son inverse $T^{-1}: F \to E$ est également borné.

        Dans notre cas, $I: (Y, \|\cdot\|_{C^1}) \to (Y, \|\cdot\|_\infty)$ est un opérateur linéaire bijectif (car c'est l'identité) et borné (démontré en I.2.a).
        Nous avons montré en I.1 que $(Y, \|\cdot\|_{C^1})$ est un espace de Banach.
        Si $(Y, \|\cdot\|_\infty)$ était également un espace de Banach, alors, selon le Théorème de l'Isomorphisme de Banach, l'opérateur $I^{-1}$ devrait être borné.
        Cependant, nous avons montré en I.2.b que $I^{-1}$ n'est pas borné.
        Cette contradiction implique que l'hypothèse que $(Y, \|\cdot\|_\infty)$ est un espace de Banach doit être fausse.
        Par conséquent, $(Y, \|\cdot\|_\infty)$ n'est pas un espace de Banach.

**Partie II : L'Opérateur de Dérivation et le Théorème du Graphe Fermé**

Soit $D : (Y, \|\cdot\|_\infty) \to (X, \|\cdot\|_\infty)$ l'opérateur de dérivation défini par $D(f) = f'$.

1.  **Montrer que $D$ est un opérateur linéaire.**

    Pour tout $f, g \in Y$ et tout scalaire $\alpha \in \mathbb{R}$ :
    *   $D(f+g) = (f+g)' = f' + g' = D(f) + D(g)$ (par linéarité de la dérivation).
    *   $D(\alpha f) = (\alpha f)' = \alpha f' = \alpha D(f)$ (par linéarité de la dérivation).
    L'opérateur $D$ est donc linéaire.

2.  **Démontrer que $D$ n'est pas borné.**

    Pour que $D$ soit borné, il faudrait qu'il existe une constante $M > 0$ telle que $\|D(f)\|_\infty \le M \|f\|_\infty$ pour tout $f \in Y$.
    Reprenons la suite de fonctions $(f_n)_{n \in \mathbb{N}^*}$ définie par $f_n(x) = \frac{1}{n} \sin(n^2 x)$ pour $x \in [0,1]$.
    Nous avons calculé en I.2.b :
    *   $\|f_n\|_\infty = \frac{1}{n}$.
    *   $\|D(f_n)\|_\infty = \|f_n'\|_\infty = n$.
    Si $D$ était borné, nous aurions $n \le M \left(\frac{1}{n}\right)$ pour tout $n \in \mathbb{N}^*$.
    Ceci implique $n^2 \le M$ pour tout $n \in \mathbb{N}^*$.
    Cette inégalité est fausse car $n^2$ peut être arbitrairement grand.
    Par conséquent, l'opérateur de dérivation $D$ n'est pas borné.

3.  **Démontrer que le graphe $\mathcal{G}(D)$ est fermé dans l'espace produit $(Y, \|\cdot\|_\infty) \times (X, \|\cdot\|_\infty)$.**

    Le graphe de $D$ est défini comme $\mathcal{G}(D) = \{ (f, D(f)) \mid f \in Y \}$.
    Pour montrer que $\mathcal{G}(D)$ est fermé, nous devons prouver que si une suite d'éléments du graphe converge vers un point dans l'espace produit, alors ce point limite appartient également au graphe.

    Soit une suite $((f_k, D(f_k)))_{k \in \mathbb{N}}$ dans $\mathcal{G}(D)$ qui converge vers un point $(f, g)$ dans $(Y, \|\cdot\|_\infty) \times (X, \|\cdot\|_\infty)$.
    La convergence dans l'espace produit signifie que :
    *   $f_k \to f$ dans $(Y, \|\cdot\|_\infty)$, ce qui signifie que $f_k$ converge uniformément vers $f$ sur $[0,1]$.
    *   $D(f_k) \to g$ dans $(X, \|\cdot\|_\infty)$, ce qui signifie que $f_k'$ converge uniformément vers $g$ sur $[0,1]$.

    Nous devons montrer que $(f, g) \in \mathcal{G}(D)$, c'est-à-dire que $f \in Y$ (donc $f \in C^1([0,1])$) et que $D(f) = f' = g$.
    Ceci est un résultat fondamental de l'analyse réelle concernant la convergence uniforme des fonctions et de leurs dérivées.
    Puisque $f_k \in Y = C^1([0,1])$, chaque $f_k$ est continûment différentiable, et donc $f_k'$ est continue.
    Comme la suite $(f_k')$ converge uniformément vers $g$, la fonction limite $g$ doit être continue.

    Considérons l'intégrale de $f_k'$ sur un intervalle $[x_0, x] \subseteq [0,1]$. Par le Théorème Fondamental du Calcul :
    $$ f_k(x) - f_k(x_0) = \int_{x_0}^x f_k'(t) dt $$
    Puisque $f_k \to f$ uniformément, en passant à la limite $k \to \infty$ pour le membre de gauche :
    $$ \lim_{k \to \infty} (f_k(x) - f_k(x_0)) = f(x) - f(x_0) $$
    Puisque $f_k' \to g$ uniformément sur $[0,1]$ et que $g$ est continue, nous pouvons intervertir la limite et l'intégrale pour le membre de droite :
    $$ \lim_{k \to \infty} \int_{x_0}^x f_k'(t) dt = \int_{x_0}^x g(t) dt $$
    En égalisant les limites, nous obtenons :
    $$ f(x) - f(x_0) = \int_{x_0}^x g(t) dt $$
    Puisque $g$ est continue sur $[0,1]$, d'après la première partie du Théorème Fondamental du Calcul, la fonction définie par $F(x) = \int_{x_0}^x g(t) dt$ est différentiable, et $F'(x) = g(x)$.
    Par conséquent, $f$ est différentiable sur $[0,1]$, et sa dérivée $f'(x)$ est égale à $g(x)$.
    De plus, puisque $g$ est continue, $f'$ est continue. Ainsi, $f \in C^1([0,1])$, ce qui signifie que $f \in Y$.

    Nous avons donc prouvé que $f \in Y$ et $g = f'$. Cela signifie que $(f, g) = (f, D(f))$, donc $(f, g) \in \mathcal{G}(D)$.
    Le graphe $\mathcal{G}(D)$ est bien fermé dans $(Y, \|\cdot\|_\infty) \times (X, \|\cdot\|_\infty)$.

4.  **Conclusion utilisant le Théorème du Graphe Fermé et comparaison avec la Partie I.**

    Le Théorème du Graphe Fermé stipule que si $T: E \to F$ est un opérateur linéaire entre deux espaces de Banach $E$ et $F$, et si son graphe $\mathcal{G}(T)$ est fermé dans $E \times F$, alors $T$ est borné.

    Appliquons ce théorème à notre opérateur $D: (Y, \|\cdot\|_\infty) \to (X, \|\cdot\|_\infty)$.
    *   Nous avons montré en II.1 que $D$ est un opérateur linéaire.
    *   Nous avons montré en II.3 que le graphe $\mathcal{G}(D)$ est fermé.
    *   Nous savons que $(X, \|\cdot\|_\infty)$ est un espace de Banach (hypothèse de l'exercice).
    *   Nous avons montré en II.2 que $D$ n'est pas borné.

    Si $(Y, \|\cdot\|_\infty)$ était un espace de Banach, alors toutes les conditions du Théorème du Graphe Fermé seraient remplies (opérateur linéaire, graphe fermé, espace de départ et d'arrivée Banach). Dans ce cas, le théorème impliquerait que $D$ doit être borné.
    Cependant, nous avons démontré que $D$ n'est *pas* borné.
    Cette contradiction signifie que l'une des hypothèses du Théorème du Graphe Fermé doit être fausse. Puisque $D$ est linéaire, $\mathcal{G}(D)$ est fermé et $(X, \|\cdot\|_\infty)$ est un Banach, la seule possibilité est que $(Y, \|\cdot\|_\infty)$ ne soit pas un espace de Banach.

    **Conclusion :** L'espace $(Y, \|\cdot\|_\infty)$ n'est pas un espace de Banach.

    **Comparaison avec la Partie I :**
    La conclusion obtenue dans la Partie I.2.c était que $(Y, \|\cdot\|_\infty)$ n'est pas un espace de Banach, déduite de l'échec de l'inverse de l'opérateur identité à être borné, en contradiction avec le Théorème de l'Isomorphisme de Banach.
    La conclusion obtenue dans la Partie II.4 est exactement la même, mais elle est atteinte par une voie différente, en utilisant le Théorème du Graphe Fermé et les propriétés de l'opérateur de dérivation.

    Cette concordance illustre la profonde interconnexion et la cohérence de ces théorèmes fondamentaux de l'Analyse Fonctionnelle. Ils fournissent des outils puissants pour caractériser la complétude des espaces et la continuité des opérateurs, même dans des contextes où les propriétés ne sont pas immédiatement évidentes.