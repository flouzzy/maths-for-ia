# Exercice 8 : Convergence Presque Sûre des Séries de Dirichlet Aléatoires

$\bigstar\bigstar\bigstar\bigstar\star$

Considérons une suite $(X_n)_{n \ge 1}$ de variables aléatoires réelles indépendantes et identiquement distribuées (i.i.d.) définies sur un espace de probabilité $(\Omega, \mathcal{F}, P)$. On suppose que $E[|X_1|] < \infty$, et on note $\mu = E[X_1]$.

L'objectif de cet exercice est d'établir un résultat de convergence presque sûre pour une moyenne pondérée des variables $X_n$ qui diffère de la moyenne arithmétique usuelle.

1.  **Rappel de la Loi Forte des Grands Nombres (LFGN)**
    Énoncez précisément la Loi Forte des Grands Nombres pour la suite $(X_n)_{n \ge 1}$.

2.  **Préparation à l'application**
    Soit $S_n = \sum_{k=1}^n (X_k - \mu)$ pour $n \ge 1$.
    Démontrez que la suite $\left(\frac{S_n}{n}\right)_{n \ge 1}$ converge presque sûrement vers 0.

3.  **Transformation par Sommation par Parties (Formule d'Abel)**
    Pour une suite de nombres réels $(a_k)_{k \ge 1}$ et une suite de nombres réels $(b_k)_{k \ge 1}$, la formule de sommation par parties (ou formule d'Abel) s'écrit :
    $\sum_{k=1}^n a_k b_k = A_n b_n - \sum_{k=1}^{n-1} A_k (b_{k+1} - b_k)$, où $A_k = \sum_{j=1}^k a_j$.
    Appliquez cette formule à la somme $\sum_{k=1}^n \frac{X_k - \mu}{k}$. Identifiez clairement les suites $(a_k)$ et $(b_k)$ que vous utilisez.

4.  **Démonstration de la Convergence**
    En utilisant les résultats des questions précédentes et la transformation obtenue, démontrez que la suite de variables aléatoires $M_n = \frac{1}{\ln n} \sum_{k=1}^n \frac{X_k}{k}$ converge presque sûrement vers $\mu$ lorsque $n \to \infty$.
    Vous pourrez utiliser le fait que $\sum_{k=1}^{n-1} \frac{1}{k(k+1)} = 1 - \frac{1}{n}$.

---

## Correction de l'Exercice 8

1.  **Rappel de la Loi Forte des Grands Nombres (LFGN)**

    La Loi Forte des Grands Nombres stipule que si $(X_n)_{n \ge 1}$ est une suite de variables aléatoires réelles indépendantes et identiquement distribuées (i.i.d.) avec $E[|X_1|] < \infty$, alors la moyenne arithmétique des $n$ premières variables converge presque sûrement vers l'espérance de $X_1$.
    Plus précisément, si $S_n = \sum_{k=1}^n X_k$, alors :
    $$ \lim_{n \to \infty} \frac{S_n}{n} = E[X_1] = \mu \quad \text{presque sûrement (p.s.)} $$

2.  **Préparation à l'application**

    Soit $S_n = \sum_{k=1}^n (X_k - \mu)$ pour $n \ge 1$.
    Nous voulons démontrer que la suite $\left(\frac{S_n}{n}\right)_{n \ge 1}$ converge presque sûrement vers 0.
    Considérons la suite de variables aléatoires $(Y_n)_{n \ge 1}$ définie par $Y_n = X_n - \mu$.
    Puisque $(X_n)_{n \ge 1}$ est une suite de variables aléatoires indépendantes et identiquement distribuées, la suite $(Y_n)_{n \ge 1}$ est également une suite de variables aléatoires indépendantes et identiquement distribuées.
    Calculons l'espérance de $Y_1$:
    $E[Y_1] = E[X_1 - \mu]$. Par linéarité de l'espérance, $E[X_1 - \mu] = E[X_1] - E[\mu]$.
    Puisque $E[X_1] = \mu$ et $E[\mu] = \mu$ (l'espérance d'une constante est la constante elle-même), nous avons $E[Y_1] = \mu - \mu = 0$.
    De plus, nous devons vérifier la condition d'intégrabilité $E[|Y_1|] < \infty$.
    $E[|Y_1|] = E[|X_1 - \mu|]$. Par l'inégalité triangulaire, nous savons que $|X_1 - \mu| \le |X_1| + |-\mu| = |X_1| + |\mu|$.
    En prenant l'espérance des deux côtés, $E[|Y_1|] \le E[|X_1| + |\mu|]$. Par linéarité de l'espérance, $E[|Y_1|] \le E[|X_1|] + E[|\mu|]$.
    Puisque $E[|X_1|] < \infty$ par hypothèse, et $|\mu| = |E[X_1]| \le E[|X_1|]$ (par l'inégalité de Jensen pour la valeur absolue), il s'ensuit que $|\mu|$ est une constante finie.
    Donc, $E[|Y_1|] \le E[|X_1|] + |\mu| < \infty$.
    Les conditions de la Loi Forte des Grands Nombres sont donc satisfaites pour la suite $(Y_n)_{n \ge 1}$.
    En appliquant la LFGN à la suite $(Y_n)_{n \ge 1}$, nous obtenons :
    $$ \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n Y_k = E[Y_1] \quad \text{presque sûrement} $$
    En substituant $Y_k = X_k - \mu$ et $E[Y_1] = 0$, nous avons :
    $$ \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n (X_k - \mu) = 0 \quad \text{presque sûrement} $$
    Par définition, $\sum_{k=1}^n (X_k - \mu) = S_n$.
    Donc, nous avons bien démontré que :
    $$ \lim_{n \to \infty} \frac{S_n}{n} = 0 \quad \text{presque sûrement} $$

3.  **Transformation par Sommation par Parties (Formule d'Abel)**

    Nous souhaitons appliquer la formule de sommation par parties à la somme $\sum_{k=1}^n \frac{X_k - \mu}{k}$.
    La formule est $\sum_{k=1}^n a_k b_k = A_n b_n - \sum_{k=1}^{n-1} A_k (b_{k+1} - b_k)$, où $A_k = \sum_{j=1}^k a_j$.
    Pour notre somme, nous identifions les suites $(a_k)$ et $(b_k)$ comme suit :
    *   $a_k = X_k - \mu$
    *   $b_k = \frac{1}{k}$

    Calculons $A_k = \sum_{j=1}^k a_j = \sum_{j=1}^k (X_j - \mu)$. D'après la définition donnée dans la question 2, $A_k = S_k$.
    Calculons la différence $b_{k+1} - b_k$:
    $b_{k+1} - b_k = \frac{1}{k+1} - \frac{1}{k}$.
    Pour simplifier cette expression, nous mettons les fractions sur un dénominateur commun :
    $b_{k+1} - b_k = \frac{k}{k(k+1)} - \frac{k+1}{k(k+1)} = \frac{k - (k+1)}{k(k+1)} = \frac{-1}{k(k+1)}$.

    Appliquons la formule d'Abel avec ces identifications :
    $$ \sum_{k=1}^n \frac{X_k - \mu}{k} = A_n b_n - \sum_{k=1}^{n-1} A_k (b_{k+1} - b_k) $$
    $$ \sum_{k=1}^n \frac{X_k - \mu}{k} = S_n \cdot \frac{1}{n} - \sum_{k=1}^{n-1} S_k \left(-\frac{1}{k(k+1)}\right) $$
    En simplifiant le signe négatif dans le second terme :
    $$ \sum_{k=1}^n \frac{X_k - \mu}{k} = \frac{S_n}{n} + \sum_{k=1}^{n-1} \frac{S_k}{k(k+1)} $$
    Cette transformation est une étape cruciale pour la suite de la démonstration, car elle relie la somme souhaitée à la suite $S_k/k$ dont nous connaissons le comportement asymptotique.

4.  **Démonstration de la Convergence**

    Nous voulons démontrer que la suite de variables aléatoires $M_n = \frac{1}{\ln n} \sum_{k=1}^n \frac{X_k}{k}$ converge presque sûrement vers $\mu$.
    Commençons par réécrire $M_n$ en soustrayant et ajoutant $\mu$ à $X_k$ dans la somme :
    $$ M_n = \frac{1}{\ln n} \sum_{k=1}^n \frac{X_k - \mu + \mu}{k} $$
    Nous pouvons séparer la somme en deux termes :
    $$ M_n = \frac{1}{\ln n} \left( \sum_{k=1}^n \frac{X_k - \mu}{k} + \sum_{k=1}^n \frac{\mu}{k} \right) $$
    $$ M_n = \frac{1}{\ln n} \sum_{k=1}^n \frac{X_k - \mu}{k} + \frac{\mu}{\ln n} \sum_{k=1}^n \frac{1}{k} $$
    Considérons le second terme : $\frac{\mu}{\ln n} \sum_{k=1}^n \frac{1}{k}$.
    Nous savons que la somme harmonique $\sum_{k=1}^n \frac{1}{k}$ est asymptotiquement équivalente à $\ln n$ lorsque $n \to \infty$. Plus précisément, $\sum_{k=1}^n \frac{1}{k} = \ln n + \gamma + o(1)$, où $\gamma$ est la constante d'Euler-Mascheroni.
    Donc, $\lim_{n \to \infty} \frac{1}{\ln n} \sum_{k=1}^n \frac{1}{k} = \lim_{n \to \infty} \frac{\ln n + \gamma + o(1)}{\ln n} = \lim_{n \to \infty} \left( 1 + \frac{\gamma}{\ln n} + \frac{o(1)}{\ln n} \right) = 1$.
    Par conséquent, le second terme converge presque sûrement vers $\mu$:
    $$ \lim_{n \to \infty} \frac{\mu}{\ln n} \sum_{k=1}^n \frac{1}{k} = \mu \cdot 1 = \mu \quad \text{presque sûrement} $$
    Il nous reste à montrer que le premier terme converge presque sûrement vers 0 :
    $$ \lim_{n \to \infty} \frac{1}{\ln n} \sum_{k=1}^n \frac{X_k - \mu}{k} = 0 \quad \text{presque sûrement} $$
    En utilisant le résultat de la question 3, nous pouvons remplacer la somme :
    $$ \frac{1}{\ln n} \sum_{k=1}^n \frac{X_k - \mu}{k} = \frac{1}{\ln n} \left( \frac{S_n}{n} + \sum_{k=1}^{n-1} \frac{S_k}{k(k+1)} \right) $$
    Nous allons analyser les deux sous-termes de cette expression séparément.

    **Analyse du premier sous-terme :** $\frac{1}{\ln n} \frac{S_n}{n}$.
    D'après la question 2, nous savons que $\lim_{n \to \infty} \frac{S_n}{n} = 0$ presque sûrement.
    Puisque $\lim_{n \to \infty} \ln n = \infty$, la multiplication par $\frac{1}{\ln n}$ ne change pas la limite de 0.
    Donc, nous avons :
    $$ \lim_{n \to \infty} \frac{1}{\ln n} \frac{S_n}{n} = 0 \quad \text{presque sûrement} $$

    **Analyse du second sous-terme :** $\frac{1}{\ln n} \sum_{k=1}^{n-1} \frac{S_k}{k(k+1)}$.
    Nous savons que $\lim_{k \to \infty} \frac{S_k}{k} = 0$ presque sûrement. Cela signifie qu'il existe un ensemble $A \subset \Omega$ avec $P(A)=1$ tel que pour tout $\omega \in A$, la suite de nombres réels $\left(\frac{S_k(\omega)}{k}\right)_{k \ge 1}$ converge vers 0.
    Fixons un $\omega \in A$. Pour tout $\epsilon > 0$, par définition de la convergence, il existe un entier $N_0(\omega)$ (qui dépend de $\omega$ et de $\epsilon$) tel que pour tout $k \ge N_0(\omega)$, nous avons $\left|\frac{S_k(\omega)}{k}\right| < \epsilon$.
    Alors, pour $n > N_0(\omega)$, nous pouvons décomposer la somme :
    $$ \left| \sum_{k=1}^{n-1} \frac{S_k(\omega)}{k(k+1)} \right| \le \sum_{k=1}^{n-1} \frac{|S_k(\omega)|}{k(k+1)} $$
    $$ \le \sum_{k=1}^{N_0(\omega)-1} \frac{|S_k(\omega)|}{k(k+1)} + \sum_{k=N_0(\omega)}^{n-1} \frac{|S_k(\omega)|}{k(k+1)} $$
    Le premier terme, $\sum_{k=1}^{N_0(\omega)-1} \frac{|S_k(\omega)|}{k(k+1)}$, est une somme finie de valeurs finies (pour un $\omega$ et un $N_0(\omega)$ donnés). Notons cette constante $C_1(\omega)$.
    Pour le second terme, en utilisant l'inégalité $|S_k(\omega)| < k\epsilon$ pour $k \ge N_0(\omega)$:
    $$ \sum_{k=N_0(\omega)}^{n-1} \frac{|S_k(\omega)|}{k(k+1)} < \sum_{k=N_0(\omega)}^{n-1} \frac{k\epsilon}{k(k+1)} = \epsilon \sum_{k=N_0(\omega)}^{n-1} \frac{1}{k+1} $$
    Nous savons que $\sum_{k=1}^{n-1} \frac{1}{k+1} = \sum_{j=2}^n \frac{1}{j}$. Cette somme est égale à $\ln n + \gamma - 1 + o(1)$.
    Donc, $\sum_{k=N_0(\omega)}^{n-1} \frac{1}{k+1} = \left(\sum_{k=1}^{n-1} \frac{1}{k+1}\right) - \left(\sum_{k=1}^{N_0(\omega)-1} \frac{1}{k+1}\right)$.
    Le terme $\sum_{k=1}^{N_0(\omega)-1} \frac{1}{k+1}$ est une constante finie (pour un $N_0(\omega)$ donné). Notons-la $C_2(\omega)$.
    Ainsi, $\sum_{k=N_0(\omega)}^{n-1} \frac{1}{k+1} \le \sum_{k=1}^{n-1} \frac{1}{k+1} = \ln n + O(1)$.
    En combinant ces résultats, pour $n$ suffisamment grand (tel que $n > N_0(\omega)$):
    $$ \left| \sum_{k=1}^{n-1} \frac{S_k(\omega)}{k(k+1)} \right| \le C_1(\omega) + \epsilon \left( \ln n + C_3(\omega) \right) $$
    où $C_3(\omega)$ est une constante finie dépendant de $N_0(\omega)$.
    Maintenant, divisons par $\ln n$:
    $$ \left| \frac{1}{\ln n} \sum_{k=1}^{n-1} \frac{S_k(\omega)}{k(k+1)} \right| \le \frac{C_1(\omega)}{\ln n} + \epsilon \left( 1 + \frac{C_3(\omega)}{\ln n} \right) $$
    Lorsque $n \to \infty$, $\ln n \to \infty$. Par conséquent, $\frac{C_1(\omega)}{\ln n} \to 0$ et $\frac{C_3(\omega)}{\ln n} \to 0$.
    Donc, pour tout $\omega \in A$,
    $$ \limsup_{n \to \infty} \left| \frac{1}{\ln n} \sum_{k=1}^{n-1} \frac{S_k(\omega)}{k(k+1)} \right| \le \epsilon $$
    Puisque cette inégalité est vraie pour tout $\epsilon > 0$, cela implique que la limite supérieure est 0. Comme la valeur absolue est non-négative, la limite inférieure est également 0.
    Par conséquent, pour tout $\omega \in A$:
    $$ \lim_{n \to \infty} \frac{1}{\ln n} \sum_{k=1}^{n-1} \frac{S_k(\omega)}{k(k+1)} = 0 $$
    Ceci étant vrai pour tout $\omega \in A$ (un ensemble de probabilité 1), nous avons :
    $$ \lim_{n \to \infty} \frac{1}{\ln n} \sum_{k=1}^{n-1} \frac{S_k}{k(k+1)} = 0 \quad \text{presque sûrement} $$

    **Conclusion de la convergence de $M_n$ :**
    En combinant les résultats pour les deux sous-termes de l'expression transformée :
    $$ \lim_{n \to \infty} \frac{1}{\ln n} \left( \frac{S_n}{n} + \sum_{k=1}^{n-1} \frac{S_k}{k(k+1)} \right) = 0 + 0 = 0 \quad \text{presque sûrement} $$
    Finalement, en reprenant l'expression initiale de $M_n$:
    $$ M_n = \frac{1}{\ln n} \sum_{k=1}^n \frac{X_k - \mu}{k} + \frac{\mu}{\ln n} \sum_{k=1}^n \frac{1}{k} $$
    Nous avons montré que le premier terme converge presque sûrement vers 0 et le second terme converge presque sûrement vers $\mu$.
    Par conséquent, la suite $M_n$ converge presque sûrement vers $\mu$:
    $$ \lim_{n \to \infty} M_n = \mu \quad \text{presque sûrement} $$
    Ceci conclut la démonstration.