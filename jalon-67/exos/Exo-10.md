# Exercice 10 : L'espace $L^1$ et complétude approchée

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
On rappelle que $L^1(X)$ est l'espace des fonctions intégrables (modulo l'égalité p.p.).
Soit $(f_n)$ une suite de fonctions mesurables dans $L^1$ telles que $\sum_{n=1}^\infty \int_X |f_n| d\mu < +\infty$.
Montrer que la série $\sum_{n=1}^\infty f_n(x)$ converge absolument presque partout vers une fonction $f \in L^1$, et que :
$$\int_X f d\mu = \sum_{n=1}^\infty \int_X f_n d\mu$$

**Solution Détaillée :**
1. **Utilisation du corollaire positif :**
Posons $g(x) = \sum_{n=1}^\infty |f_n(x)|$. Les fonctions $|f_n|$ sont mesurables et positives. Par le corollaire du TCM :
$$\int_X g d\mu = \sum_{n=1}^\infty \int_X |f_n| d\mu < +\infty$$
2. **Propriété presque partout :**
Puisque l'intégrale de la fonction positive $g$ est finie, on en déduit que $g(x)$ est finie **presque partout** (sur le complémentaire d'un ensemble négligeable $N$). Donc, pour tout $x \notin N$, la série $\sum |f_n(x)|$ converge dans $\mathbb{R}$.
Cela prouve que la série $\sum f_n(x)$ converge absolument presque partout vers une fonction notée $f(x)$. Sur l'ensemble négligeable $N$, on pose $f(x)=0$.
3. **Appartenance à $L^1$ :**
On a $|f(x)| \le g(x)$. Par croissance de l'intégrale, $\int |f| \le \int g < +\infty$, donc $f \in L^1$.
4. **Interversion sans croissance (anticipation du théorème de Lebesgue) :**
La suite des sommes partielles $S_N(x) = \sum_{n=1}^N f_n(x)$ n'est pas nécessairement croissante (car les $f_n$ peuvent être négatives). Mais on peut dominer : $|S_N(x)| \le \sum_{n=1}^N |f_n(x)| \le g(x)$ avec $g \in L^1$. Bien qu'on ait besoin du Théorème de Convergence Dominée (prochain jalon) pour conclure formellement en toute généralité pour les séries de signe quelconque, on voit ici que Beppo Levi sur la valeur absolue a fait 90% du travail abstrait topologique pour établir la convergence presque partout de la limite, prouvant que $L^1$ est complet.
