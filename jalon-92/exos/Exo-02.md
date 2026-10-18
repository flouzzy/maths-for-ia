# Exercice 2 : Convergence Asymptotique d'une Moyenne de Variables Exponentielles Non Identiquement Distribuées
$\bigstar\star\star\star\star$

## Énoncé

Soit $(X_k)_{k \ge 1}$ une suite de variables aléatoires indépendantes. Pour chaque $k \ge 1$, la variable $X_k$ suit une loi exponentielle de paramètre $\lambda_k = k^2$.

1.  Rappeler la fonction de densité de probabilité d'une variable aléatoire $X \sim \mathcal{E}(\lambda)$. Calculer l'espérance $\mathbb{E}[X_k]$ et la variance $\text{Var}(X_k)$ pour tout $k \ge 1$.
2.  Énoncer précisément la Loi Forte des Grands Nombres de Kolmogorov pour une suite de variables aléatoires indépendantes (non nécessairement identiquement distribuées).
3.  Vérifier si les conditions de la Loi Forte des Grands Nombres de Kolmogorov sont satisfaites pour la suite $(X_k)_{k \ge 1}$.
4.  En déduire la limite presque sûre de la moyenne arithmétique $S_n/n = \frac{1}{n} \sum_{k=1}^n X_k$ lorsque $n \to \infty$. Justifier chaque étape de la démonstration.

---

## Correction

### Question 1 : Rappeler la fonction de densité de probabilité d'une variable aléatoire $X \sim \mathcal{E}(\lambda)$. Calculer l'espérance $\mathbb{E}[X_k]$ et la variance $\text{Var}(X_k)$ pour tout $k \ge 1$.

La fonction de densité de probabilité d'une variable aléatoire $X$ suivant une loi exponentielle de paramètre $\lambda > 0$, notée $X \sim \mathcal{E}(\lambda)$, est donnée par :
$f(x) = \lambda e^{-\lambda x}$ pour $x \ge 0$
$f(x) = 0$ pour $x < 0$.

Calcul de l'espérance $\mathbb{E}[X_k]$ :
Pour une variable $X \sim \mathcal{E}(\lambda)$, l'espérance est $\mathbb{E}[X] = \int_0^\infty x \lambda e^{-\lambda x} dx$.
Nous utilisons l'intégration par parties avec $u=x$ et $dv=\lambda e^{-\lambda x} dx$.
Alors $du=dx$ et $v=-e^{-\lambda x}$.
$\mathbb{E}[X] = [-x e^{-\lambda x}]_0^\infty - \int_0^\infty (-e^{-\lambda x}) dx$
$\mathbb{E}[X] = (0 - 0) + \int_0^\infty e^{-\lambda x} dx$
$\mathbb{E}[X] = [-\frac{1}{\lambda} e^{-\lambda x}]_0^\infty$
$\mathbb{E}[X] = (0 - (-\frac{1}{\lambda})) = \frac{1}{\lambda}$.
Pour la variable $X_k$, le paramètre est $\lambda_k = k^2$.
Donc, $\mathbb{E}[X_k] = \frac{1}{\lambda_k} = \frac{1}{k^2}$.

Calcul de la variance $\text{Var}(X_k)$ :
La variance est donnée par $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$.
Nous devons d'abord calculer $\mathbb{E}[X^2] = \int_0^\infty x^2 \lambda e^{-\lambda x} dx$.
Nous utilisons l'intégration par parties avec $u=x^2$ et $dv=\lambda e^{-\lambda x} dx$.
Alors $du=2x dx$ et $v=-e^{-\lambda x}$.
$\mathbb{E}[X^2] = [-x^2 e^{-\lambda x}]_0^\infty - \int_0^\infty (-e^{-\lambda x}) 2x dx$
$\mathbb{E}[X^2] = (0 - 0) + 2 \int_0^\infty x e^{-\lambda x} dx$.
Nous reconnaissons que $\int_0^\infty x e^{-\lambda x} dx = \frac{1}{\lambda} \int_0^\infty x \lambda e^{-\lambda x} dx = \frac{1}{\lambda} \mathbb{E}[X] = \frac{1}{\lambda} \cdot \frac{1}{\lambda} = \frac{1}{\lambda^2}$.
Donc, $\mathbb{E}[X^2] = 2 \cdot \frac{1}{\lambda^2} = \frac{2}{\lambda^2}$.
Maintenant, nous pouvons calculer la variance :
$\text{Var}(X) = \frac{2}{\lambda^2} - \left(\frac{1}{\lambda}\right)^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$.
Pour la variable $X_k$, le paramètre est $\lambda_k = k^2$.
Donc, $\text{Var}(X_k) = \frac{1}{\lambda_k^2} = \frac{1}{(k^2)^2} = \frac{1}{k^4}$.

En résumé :
$\mathbb{E}[X_k] = \frac{1}{k^2}$
$\text{Var}(X_k) = \frac{1}{k^4}$

### Question 2 : Énoncer précisément la Loi Forte des Grands Nombres de Kolmogorov pour une suite de variables aléatoires indépendantes (non nécessairement identiquement distribuées).

La Loi Forte des Grands Nombres de Kolmogorov stipule ce qui suit :
Soit $(X_k)_{k \ge 1}$ une suite de variables aléatoires indépendantes.
Si les espérances $\mathbb{E}[X_k]$ et les variances $\text{Var}(X_k)$ existent pour tout $k \ge 1$, et si la série des variances normalisées converge, c'est-à-dire si :
$$ \sum_{k=1}^\infty \frac{\text{Var}(X_k)}{k^2} < \infty $$
Alors, la moyenne des variables centrées converge presque sûrement vers zéro lorsque $n \to \infty$ :
$$ \frac{1}{n} \sum_{k=1}^n (X_k - \mathbb{E}[X_k]) \xrightarrow{a.s.} 0 $$

### Question 3 : Vérifier si les conditions de la Loi Forte des Grands Nombres de Kolmogorov sont satisfaites pour la suite $(X_k)_{k \ge 1}$.

Nous avons les informations suivantes de la Question 1 :
1.  Les variables $X_k$ sont indépendantes (donné dans l'énoncé).
2.  Les espérances $\mathbb{E}[X_k] = \frac{1}{k^2}$ existent pour tout $k \ge 1$.
3.  Les variances $\text{Var}(X_k) = \frac{1}{k^4}$ existent pour tout $k \ge 1$.

Il nous reste à vérifier la condition de convergence de la série des variances normalisées :
$$ \sum_{k=1}^\infty \frac{\text{Var}(X_k)}{k^2} $$
Substituons l'expression de $\text{Var}(X_k)$ que nous avons trouvée :
$$ \sum_{k=1}^\infty \frac{1/k^4}{k^2} = \sum_{k=1}^\infty \frac{1}{k^4 \cdot k^2} = \sum_{k=1}^\infty \frac{1}{k^6} $$
Cette série est une série de Riemann (ou p-série) de la forme $\sum_{k=1}^\infty \frac{1}{k^p}$.
Une série de Riemann converge si et seulement si l'exposant $p$ est strictement supérieur à 1.
Dans notre cas, $p=6$. Puisque $6 > 1$, la série $\sum_{k=1}^\infty \frac{1}{k^6}$ converge.
Par conséquent, toutes les conditions de la Loi Forte des Grands Nombres de Kolmogorov sont satisfaites pour la suite $(X_k)_{k \ge 1}$.

### Question 4 : En déduire la limite presque sûre de la moyenne arithmétique $S_n/n = \frac{1}{n} \sum_{k=1}^n X_k$ lorsque $n \to \infty$. Justifier chaque étape de la démonstration.

Puisque les conditions de la Loi Forte des Grands Nombres de Kolmogorov sont satisfaites (d'après la Question 3), nous pouvons affirmer que :
$$ \frac{1}{n} \sum_{k=1}^n (X_k - \mathbb{E}[X_k]) \xrightarrow{a.s.} 0 \quad \text{lorsque } n \to \infty $$
Nous cherchons la limite presque sûre de la moyenne arithmétique $\frac{1}{n} \sum_{k=1}^n X_k$. Nous pouvons réécrire cette expression en séparant les termes d'espérance :
$$ \frac{1}{n} \sum_{k=1}^n X_k = \frac{1}{n} \sum_{k=1}^n (X_k - \mathbb{E}[X_k] + \mathbb{E}[X_k]) $$
$$ \frac{1}{n} \sum_{k=1}^n X_k = \frac{1}{n} \sum_{k=1}^n (X_k - \mathbb{E}[X_k]) + \frac{1}{n} \sum_{k=1}^n \mathbb{E}[X_k] $$
Nous savons que le premier terme du membre de droite converge presque sûrement vers 0. Il nous faut donc évaluer la limite du second terme : $\frac{1}{n} \sum_{k=1}^n \mathbb{E}[X_k]$.
D'après la Question 1, nous avons $\mathbb{E}[X_k] = \frac{1}{k^2}$. Le second terme devient donc :
$$ \frac{1}{n} \sum_{k=1}^n \frac{1}{k^2} $$
Considérons la série $\sum_{k=1}^\infty \frac{1}{k^2}$. Il s'agit d'une série de Riemann avec $p=2$. Puisque $p=2 > 1$, cette série converge. Sa somme est un résultat classique, $\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$.
Soit $A_n = \sum_{k=1}^n \frac{1}{k^2}$. Nous savons que $\lim_{n \to \infty} A_n = \frac{\pi^2}{6}$.
Nous devons trouver la limite de $\frac{1}{n} A_n$.
Puisque $A_n$ converge vers une valeur finie ($\frac{\pi^2}{6}$), et que nous divisons par $n$ qui tend vers l'infini, la limite de $\frac{A_n}{n}$ est :
$$ \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n \frac{1}{k^2} = \lim_{n \to \infty} \frac{A_n}{n} = \frac{\pi^2/6}{\infty} = 0 $$
Ce résultat est une propriété fondamentale des suites : si une suite $(a_n)$ converge vers une limite finie $L$, alors la suite de ses moyennes arithmétiques $\frac{1}{n} \sum_{k=1}^n a_k$ converge aussi vers $L$. Ici, la suite des termes $a_k = \frac{1}{k^2}$ converge vers 0. Donc $\frac{1}{n} \sum_{k=1}^n \frac{1}{k^2}$ converge vers 0. Alternativement, si une suite de sommes partielles $A_n = \sum_{k=1}^n a_k$ converge vers une limite finie $L$, alors $\lim_{n \to \infty} \frac{A_n}{n} = 0$.

En combinant les limites des deux termes :
$$ \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n X_k = \lim_{n \to \infty} \left( \frac{1}{n} \sum_{k=1}^n (X_k - \mathbb{E}[X_k]) + \frac{1}{n} \sum_{k=1}^n \mathbb{E}[X_k] \right) $$
$$ \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n X_k = 0 \quad (\text{presque sûrement}) + 0 $$
$$ \lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^n X_k = 0 \quad \text{presque sûrement} $$
Par conséquent, la moyenne arithmétique $S_n/n$ converge presque sûrement vers 0 lorsque $n \to \infty$.