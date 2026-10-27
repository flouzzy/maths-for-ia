# Exercice 07: Étude Approfondie d'Opérateurs Différentiels et des Théorèmes Fondamentaux de l'Analyse Fonctionnelle

Cet exercice rigoureux a pour objectif d'explorer les propriétés de continuité et de fermeture d'un opérateur de dérivation dans différents espaces fonctionnels, mettant en lumière la pertinence et les conditions d'application du Théorème du Graphe Fermé.

Difficulté : $\bigstar$\bigstar$\bigstar$\bigstar\star

\vspace{0.5cm}

\noindent \textbf{Énoncé :}

Soient $X$ et $Y$ des espaces vectoriels normés sur le corps des réels $\mathbb{R}$. Un opérateur linéaire $T: X \to Y$ est dit \textit{fermé} si son graphe $G(T) = \{(x, Tx) \mid x \in D(T)\}$ est un sous-espace fermé de l'espace produit $X \times Y$, muni de la norme produit $\|(x,y)\|_{X \times Y} = \|x\|_X + \|y\|_Y$. Par convention, le domaine $D(T)$ est ici $X$ tout entier.

Considérons l'espace $C([0,1])$ des fonctions continues sur l'intervalle $[0,1]$ à valeurs réelles, muni de la norme de la convergence uniforme $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$. Il est un résultat fondamental de l'analyse réelle que $(C([0,1]), \|\cdot\|_\infty)$ est un espace de Banach.

Soit $C^1([0,1])$ l'espace des fonctions continûment différentiables sur l'intervalle $[0,1]$ à valeurs réelles.
Nous définissons l'opérateur de dérivation $D: C^1([0,1]) \to C([0,1])$ par $D(f) = f'$.

Nous allons examiner cet opérateur $D$ en considérant $C^1([0,1])$ muni de deux normes distinctes :

\begin{enumerate}
    \item La norme usuelle de l'espace $C^1$: $\|f\|_{C^1} = \|f\|_\infty + \|f'\|_\infty$.
    \item La norme de la convergence uniforme: $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$.
\end{enumerate}

Répondez aux questions suivantes avec la rigueur la plus absolue :

\begin{enumerate}
    \item Montrer que $(C^1([0,1]), \|\cdot\|_{C^1})$ est un espace de Banach.
    \item Montrer que l'opérateur $D: (C^1([0,1]), \|\cdot\|_{C^1}) \to (C([0,1]), \|\cdot\|_\infty)$ est continu.
    \item Considérons maintenant l'opérateur $D: (C^1([0,1]), \|\cdot\|_\infty) \to (C([0,1]), \|\cdot\|_\infty)$.
    \begin{enumerate}
        \item Montrer que l'opérateur $D$ est linéaire et fermé.
        \item Montrer que $D$ n'est pas continu.
        \item Expliquer pourquoi le Théorème du Graphe Fermé ne contredit pas le résultat de la question 3.b. Pour cela, vous devrez notamment prouver explicitement une propriété cruciale de l'espace $(C^1([0,1]), \|\cdot\|_\infty)$.
    \end{enumerate}
\end{enumerate}

\vspace{1cm}

\noindent \textbf{Correction :}

\vspace{0.5cm}

\begin{enumerate}
    \item \textbf{Démonstration que $(C^1([0,1]), \|\cdot\|_{C^1})$ est un espace de Banach.}

    Pour montrer qu'un espace normé est un espace de Banach, il faut prouver qu'il est complet, c'est-à-dire que toute suite de Cauchy dans cet espace converge vers un élément de cet espace.

    Soit $(f_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $(C^1([0,1]), \|\cdot\|_{C^1})$.
    Par définition de la norme $\|f\|_{C^1}$, cela signifie que pour tout $\varepsilon > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tous $n, m \ge N$:
    $$ \|f_n - f_m\|_{C^1} < \varepsilon $$
    Ce qui équivaut à :
    $$ \|f_n - f_m\|_\infty + \|f_n' - f_m'\|_\infty < \varepsilon $$
    Cette inégalité implique deux conditions distinctes :
    \begin{itemize}
        \item $\|f_n - f_m\|_\infty < \varepsilon$. Ceci montre que $(f_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans l'espace $(C([0,1]), \|\cdot\|_\infty)$.
        \item $\|f_n' - f_m'\|_\infty < \varepsilon$. Ceci montre que $(f_n')_{n \in \mathbb{N}}$ est une suite de Cauchy dans l'espace $(C([0,1]), \|\cdot\|_\infty)$.
    \end{itemize}

    Puisque $(C([0,1]), \|\cdot\|_\infty)$ est un espace de Banach (il est complet), toute suite de Cauchy dans cet espace converge. Par conséquent :
    \begin{itemize}
        \item Il existe une fonction $f \in C([0,1])$ telle que $f_n \xrightarrow{\|\cdot\|_\infty} f$, c'est-à-dire $f_n$ converge uniformément vers $f$ sur $[0,1]$.
        \item Il existe une fonction $g \in C([0,1])$ telle que $f_n' \xrightarrow{\|\cdot\|_\infty} g$, c'est-à-dire $f_n'$ converge uniformément vers $g$ sur $[0,1]$.
    \end{itemize}

    Il nous reste à montrer que la fonction limite $f$ appartient à $C^1([0,1])$ et que sa dérivée $f'$ est égale à $g$. C'est un théorème fondamental d'analyse réelle concernant l'interversion des limites et de la dérivation :
    Soient $f_n$ une suite de fonctions continûment différentiables sur $[0,1]$ telle que $f_n$ converge uniformément vers $f$ et $f_n'$ converge uniformément vers $g$. Alors $f$ est continûment différentiable et $f' = g$.
    La démonstration s'appuie sur le théorème fondamental de l'analyse. Pour tout $x \in [0,1]$ et pour tout $y \in [0,1]$, on a :
    $$ f_n(y) - f_n(x) = \int_x^y f_n'(t) dt $$
    Comme $f_n \to f$ uniformément et $f_n' \to g$ uniformément, nous pouvons prendre la limite quand $n \to \infty$ sous le signe intégral (ceci est justifié par la convergence uniforme de l'intégrande) :
    $$ \lim_{n \to \infty} (f_n(y) - f_n(x)) = \lim_{n \to \infty} \int_x^y f_n'(t) dt $$
    $$ f(y) - f(x) = \int_x^y g(t) dt $$
    Puisque $g$ est continue sur $[0,1]$, le Théorème Fondamental de l'Analyse nous assure que la fonction $F(y) = \int_x^y g(t) dt$ est différentiable par rapport à $y$ et que $F'(y) = g(y)$. Par conséquent, $f$ est différentiable sur $[0,1]$ et sa dérivée $f'$ est égale à $g$.
    De plus, comme $g \in C([0,1])$, $f'$ est continue. Ainsi, $f \in C^1([0,1])$.

    Enfin, nous devons vérifier que la suite $(f_n)$ converge vers $f$ dans la norme $\|\cdot\|_{C^1}$.
    $$ \|f_n - f\|_{C^1} = \|f_n - f\|_\infty + \|f_n' - f'\|_\infty $$
    Nous savons que $f_n \xrightarrow{\|\cdot\|_\infty} f$, donc $\|f_n - f\|_\infty \to 0$ quand $n \to \infty$.
    Nous savons que $f_n' \xrightarrow{\|\cdot\|_\infty} g$ et nous avons montré que $g=f'$, donc $\|f_n' - f'\|_\infty \to 0$ quand $n \to \infty$.
    Par conséquent, $\|f_n - f\|_{C^1} \to 0$ quand $n \to \infty$.
    La suite $(f_n)$ converge donc vers $f \in C^1([0,1])$ dans la norme $\|\cdot\|_{C^1}$.
    L'espace $(C^1([0,1]), \|\cdot\|_{C^1})$ est donc complet, c'est un espace de Banach.

    \item \textbf{Démonstration que l'opérateur $D: (C^1([0,1]), \|\cdot\|_{C^1}) \to (C([0,1]), \|\cdot\|_\infty)$ est continu.}

    Un opérateur linéaire $T: X \to Y$ est continu si et seulement s'il est borné, c'est-à-dire s'il existe une constante $M > 0$ telle que pour tout $f \in X$:
    $$ \|Tf\|_Y \le M \|f\|_X $$
    Dans notre cas, $X = (C^1([0,1]), \|\cdot\|_{C^1})$ et $Y = (C([0,1]), \|\cdot\|_\infty)$. L'opérateur est $D(f) = f'$.
    Nous devons montrer qu'il existe $M > 0$ tel que pour tout $f \in C^1([0,1])$:
    $$ \|Df\|_\infty \le M \|f\|_{C^1} $$
    Par définition de la norme $\|\cdot\|_{C^1}$, nous avons :
    $$ \|f\|_{C^1} = \|f\|_\infty + \|f'\|_\infty $$
    Or, $\|Df\|_\infty = \|f'\|_\infty$.
    Il est clair que, puisque $\|f\|_\infty \ge 0$, nous avons $\|f'\|_\infty \le \|f\|_\infty + \|f'\|_\infty$.
    Par conséquent, nous pouvons écrire :
    $$ \|Df\|_\infty \le \|f\|_{C^1} $$
    Cette inégalité est valable pour tout $f \in C^1([0,1])$. Nous pouvons choisir $M=1$.
    L'opérateur $D$ est donc borné, et par suite continu.

    \item \textbf{Étude de l'opérateur $D: (C^1([0,1]), \|\cdot\|_\infty) \to (C([0,1]), \|\cdot\|_\infty)$.}

    \begin{enumerate}
        \item \textbf{Démonstration que $D$ est linéaire et fermé.}

        \textbf{Linéarité :}
        Soient $f, g \in C^1([0,1])$ et $\alpha \in \mathbb{R}$.
        L'opérateur $D$ agit comme la dérivation usuelle des fonctions. La propriété de linéarité de la dérivation est bien connue :
        $$ D(f+\alpha g) = (f+\alpha g)' = f' + \alpha g' = D(f) + \alpha D(g) $$
        L'opérateur $D$ est bien linéaire.

        \textbf{Fermeture :}
        Pour montrer que $D$ est un opérateur fermé, nous devons prendre une suite $(f_n)_{n \in \mathbb{N}}$ dans $C^1([0,1])$ telle que $f_n \xrightarrow{\|\cdot\|_\infty} f$ (pour un certain $f \in C([0,1])$) et $Df_n \xrightarrow{\|\cdot\|_\infty} g$ (pour un certain $g \in C([0,1])$). Nous devons ensuite prouver que la fonction limite $f$ appartient à $C^1([0,1])$ et que sa dérivée $f'$ est égale à $g$.
        \begin{itemize}
            \item L'hypothèse $f_n \xrightarrow{\|\cdot\|_\infty} f$ signifie que la suite $(f_n)$ converge uniformément vers $f$ sur l'intervalle $[0,1]$.
            \item L'hypothèse $Df_n \xrightarrow{\|\cdot\|_\infty} g$ signifie que la suite $(f_n')$ des dérivées converge uniformément vers $g$ sur l'intervalle $[0,1]$.
        \end{itemize}
        Comme établi dans la partie 1 de cette correction, un résultat fondamental de l'analyse réelle affirme que si une suite de fonctions continûment différentiables $(f_n)$ converge uniformément vers une fonction $f$, et si la suite de leurs dérivées $(f_n')$ converge uniformément vers une fonction $g$, alors $f$ est différentiable, sa dérivée $f'$ est égale à $g$, et $f'$ est continue car $g$ est continue (étant la limite uniforme de fonctions continues).
        Ainsi, nous avons $f \in C^1([0,1])$ et $D(f) = f' = g$.
        Par conséquent, le graphe de $D$ est fermé dans l'espace produit $(C^1([0,1]), \|\cdot\|_\infty) \times (C([0,1]), \|\cdot\|_\infty)$. L'opérateur $D$ est donc un opérateur fermé.

        \item \textbf{Démonstration que $D$ n'est pas continu.}

        Un opérateur linéaire $D$ n'est pas continu s'il n'est pas borné, c'est-à-dire s'il existe une suite $(f_n)_{n \in \mathbb{N}}$ dans le domaine $C^1([0,1])$ telle que $\|f_n\|_\infty \to 0$ mais $\|Df_n\|_\infty$ n'est pas bornée (par exemple, $\|Df_n\|_\infty \to \infty$).

        Considérons la suite de fonctions $(f_n)_{n \in \mathbb{N}^*}$ définie par :
        $$ f_n(x) = \frac{1}{n} \sin(n^2 x) \quad \text{pour tout } x \in [0,1] $$
        Chaque fonction $f_n$ est continûment différentiable sur $[0,1]$ (elle est même de classe $C^\infty$), donc $f_n \in C^1([0,1])$.

        Calculons la norme $\|f_n\|_\infty$:
        $$ \|f_n\|_\infty = \sup_{x \in [0,1]} \left| \frac{1}{n} \sin(n^2 x) \right| $$
        Puisque la fonction sinus a une amplitude maximale de $1$ ($|\sin(u)| \le 1$ pour tout $u \in \mathbb{R}$), et que $n^2 x$ peut prendre des valeurs pour lesquelles $\sin(n^2 x) = \pm 1$ sur l'intervalle $[0,1]$ (par exemple $x = \frac{\pi}{2n^2}$ si $\frac{\pi}{2n^2} \le 1$), nous avons :
        $$ \|f_n\|_\infty = \frac{1}{n} \sup_{x \in [0,1]} |\sin(n^2 x)| = \frac{1}{n} \cdot 1 = \frac{1}{n} $$
        Quand $n \to \infty$, $\|f_n\|_\infty \to 0$.

        Calculons maintenant $Df_n = f_n'$, la dérivée de $f_n(x)$ :
        $$ f_n'(x) = \frac{d}{dx} \left( \frac{1}{n} \sin(n^2 x) \right) = \frac{1}{n} (n^2 \cos(n^2 x)) = n \cos(n^2 x) $$
        Calculons la norme $\|Df_n\|_\infty$:
        $$ \|Df_n\|_\infty = \sup_{x \in [0,1]} |n \cos(n^2 x)| $$
        Puisque $\cos(u)$ peut prendre la valeur $1$ (par exemple pour $u=0$, ou $u=2k\pi$ pour $k \in \mathbb{Z}$), et que $n^2 x$ peut atteindre ces valeurs sur l'intervalle $[0, n^2]$ qui contient toujours $0$, nous avons :
        $$ \|Df_n\|_\infty = n \cdot 1 = n $$
        Quand $n \to \infty$, $\|Df_n\|_\infty = n \to \infty$.

        Puisque nous avons trouvé une suite $(f_n)$ telle que $\|f_n\|_\infty \to 0$ mais $\|Df_n\|_\infty$ est non bornée (elle tend vers l'infini), l'opérateur $D$ n'est pas continu. En effet, s'il était continu, il existerait une constante $M$ telle que $\|Df_n\|_\infty \le M \|f_n\|_\infty$ pour tout $n$. Ceci impliquerait $n \le M \frac{1}{n}$, soit $n^2 \le M$, ce qui est manifestement faux pour $n$ suffisamment grand.

        \item \textbf{Explication pourquoi le Théorème du Graphe Fermé ne contredit pas le résultat de la question 3.b.}

        Le Théorème du Graphe Fermé énonce formellement :
        Soient $X$ et $Y$ des espaces de Banach. Si $T: X \to Y$ est un opérateur linéaire dont le graphe est fermé, alors $T$ est continu.

        Dans notre situation :
        \begin{itemize}
            \item L'opérateur $D: (C^1([0,1]), \|\cdot\|_\infty) \to (C([0,1]), \|\cdot\|_\infty)$ est linéaire (démontré en 3.a).
            \item Le graphe de $D$ est fermé (démontré en 3.a).
            \item L'espace d'arrivée $Y = (C([0,1]), \|\cdot\|_\infty)$ est un espace de Banach (ceci est un résultat classique rappelé dans l'énoncé).
        \end{itemize}
        Cependant, nous avons démontré en 3.b que l'opérateur $D$ n'est pas continu.
        Pour que la conclusion du Théorème du Graphe Fermé (la continuité de $D$) soit valide, il est impératif que toutes ses prémisses soient satisfaites. En particulier, l'espace de départ $X$ doit être un espace de Banach.
        Le fait que $D$ soit linéaire et fermé, et que l'espace d'arrivée soit de Banach, mais que $D$ ne soit pas continu, implique logiquement que la condition restante du Théorème du Graphe Fermé n'est pas remplie. Autrement dit, l'espace de départ $X = (C^1([0,1]), \|\cdot\|_\infty)$ n'est \textit{pas} un espace de Banach.

        Prouvons explicitement que $(C^1([0,1]), \|\cdot\|_\infty)$ n'est pas un espace de Banach. Pour cela, nous devons exhiber une suite de Cauchy dans cet espace qui ne converge pas vers un élément de $C^1([0,1])$. Autrement dit, l'espace n'est pas complet.
        Considérons la suite de fonctions $(f_n)_{n \in \mathbb{N}^*}$ définie par :
        $$ f_n(x) = \sqrt{(x - 1/2)^2 + \frac{1}{n}} \quad \text{pour tout } x \in [0,1] $$
        \begin{enumerate}[I.]
            \item \textbf{Chaque $f_n$ est dans $C^1([0,1])$ :}
            La fonction $f_n(x)$ est la composition de $u \mapsto \sqrt{u}$ (qui est de classe $C^\infty$ sur $(0, \infty)$) avec la fonction $v(x) = (x-1/2)^2 + 1/n$.
            Puisque $(x-1/2)^2 + 1/n \ge 1/n > 0$ pour tout $x \in [0,1]$, le terme sous la racine est toujours strictement positif. La fonction $v(x)$ est un polynôme, donc de classe $C^\infty$.
            Par composition, $f_n$ est de classe $C^\infty$ sur $[0,1]$ pour tout $n$.
            En particulier, $f_n \in C^1([0,1])$.

            \item \textbf{La suite $(f_n)$ est de Cauchy dans $(C^1([0,1]), \|\cdot\|_\infty)$ :}
            Pour montrer qu'une suite est de Cauchy dans un espace normé, il suffit de montrer qu'elle converge dans cet espace.
            Calculons la limite ponctuelle de $f_n(x)$ lorsque $n \to \infty$ :
            $$ f(x) = \lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \sqrt{(x - 1/2)^2 + \frac{1}{n}} = \sqrt{(x - 1/2)^2} = |x - 1/2| $$
            Montrons que $f_n$ converge uniformément vers $f$ sur $[0,1]$.
            $$ \|f_n - f\|_\infty = \sup_{x \in [0,1]} \left| \sqrt{(x - 1/2)^2 + \frac{1}{n}} - |x - 1/2| \right| $$
            Utilisons l'identité algébrique $ \sqrt{a+b} - \sqrt{a} = \frac{b}{\sqrt{a+b} + \sqrt{a}} $ pour $a = (x - 1/2)^2$ et $b = 1/n$.
            $$ \left| \sqrt{(x - 1/2)^2 + \frac{1}{n}} - |x - 1/2| \right| = \frac{1/n}{\sqrt{(x - 1/2)^2 + \frac{1}{n}} + |x - 1/2|} $$
            Le dénominateur $\sqrt{(x - 1/2)^2 + \frac{1}{n}} + |x - 1/2|$ est toujours positif.
            De plus, il est minoré lorsque $|x-1/2|$ est minimal, c'est-à-dire quand $x=1/2$, où $|x-1/2|=0$.
            $$ \sqrt{(x - 1/2)^2 + \frac{1}{n}} + |x - 1/2| \ge \sqrt{0 + \frac{1}{n}} + 0 = \frac{1}{\sqrt{n}} $$
            Donc, pour tout $x \in [0,1]$,
            $$ 0 \le \frac{1/n}{\sqrt{(x - 1/2)^2 + \frac{1}{n}} + |x - 1/2|} \le \frac{1/n}{1/\sqrt{n}} = \frac{1}{\sqrt{n}} $$
            Par conséquent, $\|f_n - f\|_\infty \le \frac{1}{\sqrt{n}}$.
            Comme $\frac{1}{\sqrt{n}} \to 0$ lorsque $n \to \infty$, la suite $(f_n)$ converge uniformément vers $f$ dans $(C([0,1]), \|\cdot\|_\infty)$. Puisque $(C([0,1]), \|\cdot\|_\infty)$ est un espace complet, toute suite convergente est une suite de Cauchy. Ainsi, $(f_n)$ est une suite de Cauchy dans $(C^1([0,1]), \|\cdot\|_\infty)$.

            \item \textbf{La fonction limite $f$ n'appartient pas à $C^1([0,1])$ :}
            La fonction $f(x) = |x - 1/2|$ est continue sur $[0,1]$.
            Cependant, $f$ n'est pas différentiable au point $x = 1/2$.
            Pour s'en convaincre, calculons les dérivées à gauche et à droite en $x=1/2$:
            $$ f'_-(1/2) = \lim_{h \to 0^-} \frac{|(1/2 + h) - 1/2| - |1/2 - 1/2|}{h} = \lim_{h \to 0^-} \frac{|h|}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1 $$
            $$ f'_+(1/2) = \lim_{h \to 0^+} \frac{|(1/2 + h) - 1/2| - |1/2 - 1/2|}{h} = \lim_{h \to 0^+} \frac{|h|}{h} = \lim_{h \to 0^+} \frac{h}{h} = 1 $$
            Puisque $f'_-(1/2) = -1 \neq 1 = f'_+(1/2)$, la fonction $f(x)$ n'est pas différentiable en $x=1/2$.
            Par conséquent, $f \notin C^1([0,1])$.
        \end{enumerate}
        Nous avons ainsi construit une suite de Cauchy $(f_n)$ dans $(C^1([0,1]), \|\cdot\|_\infty)$ dont la limite n'appartient pas à $C^1([0,1])$. Cet espace n'est donc pas complet, et par suite, n'est pas un espace de Banach.

        En conclusion, le Théorème du Graphe Fermé ne s'applique pas car la condition que l'espace de départ $X = (C^1([0,1]), \|\cdot\|_\infty)$ soit un espace de Banach n'est pas remplie. C'est précisément cette défaillance de complétude qui permet à l'opérateur de dérivation $D$ d'être linéaire et fermé, mais non continu.
    \end{enumerate}
\end{enumerate}