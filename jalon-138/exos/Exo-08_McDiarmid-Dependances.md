# Exercice 8 : Inégalité de McDiarmid sous dépendances faibles (Niveau 8)

## Énoncé
Dans le théorème classique de McDiarmid, l'indépendance mutuelle des variables $X_1, \dots, X_n$ est cruciale. Cet exercice explore une extension lorsque les variables présentent une dépendance faible, modélisée par un couplage.
Soient $X_1, \dots, X_n$ des variables aléatoires (non nécessairement indépendantes) à valeurs dans $\mathcal{X}$.
Soit $f : \mathcal{X}^n \to \mathbb{R}$ une fonction vérifiant la propriété des différences bornées avec les constantes $c_1, \dots, c_n$.
Supposons que pour tout $i \in \{1, \dots, n\}$ et pour tous $x_1, \dots, x_i, x'_i \in \mathcal{X}$, on puisse construire deux vecteurs aléatoires $V$ et $V'$ définis sur le même espace de probabilité tels que :
1. La loi conditionnelle de $V$ est la loi conditionnelle de $(X_{i+1}, \dots, X_n)$ sachant $X_1=x_1, \dots, X_i=x_i$.
2. La loi conditionnelle de $V'$ est la loi conditionnelle de $(X_{i+1}, \dots, X_n)$ sachant $X_1=x_1, \dots, X_{i-1}=x_{i-1}, X_i=x'_i$.
3. On a l'inégalité sur la distance de Hamming de ces lois couplées :
$$\sum_{j=i+1}^n \mathbb{P}(V_j \neq V'_j) \le \gamma_i$$
où $\gamma_i \ge 0$ est une constante mesurant l'effet de propagation de la dépendance.

Démontrer que la martingale de Doob $Z_k = \mathbb{E}[f(X) \mid X_1, \dots, X_k]$ a des accroissements $D_k = Z_k - Z_{k-1}$ qui vérifient presque sûrement :
$$|D_k| \le c_k + \sum_{j=k+1}^n c_j \mathbb{P}(V_j \neq V'_j) \le c_k + \max_{j > k} c_j \gamma_k$$

---

## Correction Détaillée

### 1. Analyse de l'espérance conditionnelle par couplage
Écrivons la différence $D_k = Z_k - Z_{k-1}$ en utilisant la loi de probabilité conditionnelle.
Soient $x_1, \dots, x_k$ et $x'_k$ des valeurs fixées. La différence entre les espérances conditionnelles s'exprime comme :
$$\mathbb{E}[f(X) \mid X_1=x_1, \dots, X_k=x_k] - \mathbb{E}[f(X) \mid X_1=x_1, \dots, X_k=x'_k]$$

Puisque les variables $(X_{k+1}, \dots, X_n)$ sous ces deux conditionnements ont les mêmes lois que les vecteurs couplés $V$ et $V'$, nous pouvons réécrire cette différence d'espérances sur le même espace de probabilité :
$$\mathbb{E}[f(x_1, \dots, x_k, V_{k+1}, \dots, V_n)] - \mathbb{E}[f(x_1, \dots, x_{k-1}, x'_k, V'_{k+1}, \dots, V'_n)]$$
$$= \mathbb{E}\Big[ f(x_1, \dots, x_k, V_{k+1}, \dots, V_n) - f(x_1, \dots, x_{k-1}, x'_k, V'_{k+1}, \dots, V'_n) \Big]$$

### 2. Utilisation de la propriété de Lipschitz (différences bornées)
Décomposons la différence à l'intérieur de l'espérance en faisant apparaître des chemins de coordonnées :
$$f(x_1, \dots, x_k, V_{k+1}, \dots, V_n) - f(x_1, \dots, x_{k-1}, x'_k, V'_{k+1}, \dots, V'_n)$$
$$= \Big( f(x_1, \dots, x_k, V_{k+1}, \dots, V_n) - f(x_1, \dots, x_{k-1}, x'_k, V_{k+1}, \dots, V_n) \Big)$$
$$+ \Big( f(x_1, \dots, x_{k-1}, x'_k, V_{k+1}, \dots, V_n) - f(x_1, \dots, x_{k-1}, x'_k, V'_{k+1}, \dots, V'_n) \Big)$$

- Pour la première parenthèse, seul le $k$-ème terme change ($x_k$ vs $x'_k$). Par la propriété des différences bornées, cette différence est bornée par $c_k$.
- Pour la seconde parenthèse, les coordonnées modifiées sont $j \in \{k+1, \dots, n\}$. Nous pouvons borner cette différence par la somme des variations sur chaque coordonnée $j$ où $V_j \neq V'_j$ :
$$|f(x_1, \dots, x_{k-1}, x'_k, V_{k+1}, \dots, V_n) - f(x_1, \dots, x_{k-1}, x'_k, V'_{k+1}, \dots, V'_n)| \le \sum_{j=k+1}^n c_j \mathbf{1}_{V_j \neq V'_j}$$

### 3. Synthèse et espérance
En prenant la valeur absolue et en appliquant l'espérance :
$$|D_k| \le \mathbb{E}\left[ c_k + \sum_{j=k+1}^n c_j \mathbf{1}_{V_j \neq V'_j} \right] = c_k + \sum_{j=k+1}^n c_j \mathbb{P}(V_j \neq V'_j)$$

Puisque $\mathbb{P}(V_j \neq V'_j) \ge 0$, nous pouvons majorer $c_j$ par $\max_{r > k} c_r$ :
$$\sum_{j=k+1}^n c_j \mathbb{P}(V_j \neq V'_j) \le \left(\max_{r > k} c_r\right) \sum_{j=k+1}^n \mathbb{P}(V_j \neq V'_j)$$

En utilisant l'hypothèse de couplage $\sum_{j=k+1}^n \mathbb{P}(V_j \neq V'_j) \le \gamma_k$, on obtient :
$$|D_k| \le c_k + \max_{r > k} c_r \gamma_k$$

### Conclusion
Ce résultat montre que si les dépendances entre les variables sont faibles (c'est-à-dire que modifier $X_k$ n'a que très peu d'influence sur la loi conjointe des variables futures, représenté par un petit $\gamma_k$), les accroissements de la martingale de Doob restent bornés. On peut alors appliquer l'inégalité d'Azuma-Hoeffding avec des constantes effectives ajustées $c'_k = c_k + \max_{r > k} c_r \gamma_k$, ce qui étend la puissance de McDiarmid aux processus stochastiques faiblement dépendants (comme les chaînes de Markov mélangeantes).
