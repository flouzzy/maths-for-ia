# Exercice 10

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Théorème de l'inverse continu. Soient $E, F$ des espaces de Banach et $T \in \mathcal{L}(E,F)$ un opérateur bijectif. Si l'on suppose connu le théorème de l'application ouverte, montrer que l'opérateur inverse $T^{-1} : F \to E$ est nécessairement continu (c'est-à-dire appartient à $\mathcal{L}(F,E)$).

**Correction Détaillée :**
1. Soit $T$ un opérateur linéaire continu bijectif entre deux espaces de Banach $E$ et $F$. Puisque $T$ est bijectif, l'opérateur inverse $T^{-1}$ est bien défini sur l'ensemble de $F$ et à valeurs dans $E$, et il est fondamentalement algébriquement linéaire.
2. La question est de prouver qu'il existe une constante $C > 0$ telle que $\|T^{-1}(y)\|_E \le C \|y\|_F$ pour tout $y \in F$.
3. Le théorème de l'application ouverte (un pilier de l'analyse fonctionnelle sur les espaces de Banach) stipule que toute application linéaire continue et surjective entre deux espaces de Banach est ouverte.
4. Une application est dite ouverte si l'image de tout ensemble ouvert de l'espace de départ est un ensemble ouvert de l'espace d'arrivée.
5. Soit $U$ un sous-ensemble ouvert quelconque de $E$. Par le théorème de l'application ouverte, $T(U)$ est un ouvert dans $F$.
6. L'image de $U$ par $T$ n'est autre que la pré-image de $U$ par l'application inverse $T^{-1}$, c'est-à-dire $(T^{-1})^{-1}(U) = T(U)$.
7. Nous venons donc de montrer que pour tout ouvert $U$ de $E$, son image réciproque par $T^{-1}$ (qui est $T(U)$) est un ouvert de $F$.
8. Or, la définition topologique de la continuité stipule qu'une application est continue si et seulement si l'image réciproque de tout ouvert est un ouvert.
9. Par conséquent, l'opérateur $T^{-1}$ est topologiquement continu.
10. Comme $T^{-1}$ est un opérateur linéaire entre espaces normés, la continuité topologique est équivalente à la continuité (ou bornitude) métrique. $T^{-1}$ est donc continu, ce qui conclut la démonstration.
