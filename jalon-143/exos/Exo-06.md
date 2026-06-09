```yaml
uuid: 6a7b8c9d-0e1f-2a3b-4c5d-6e7f8a9b0c1d
title: "Exercice 6 : Théorie Spectrale des Graphes et Bornes de Coupures Optimales"
```
# Exercice 6 : Théorie Spectrale des Graphes et Bornes de Coupures Optimales

**Contexte :** On considère un graphe non orienté, simple et connexe $G=(V,E)$ avec $n$ sommets. Soit $L = D-A$ son Laplacien combinatoire, où $D$ est la matrice des degrés et $A$ la matrice d'adjacence. On note $\lambda_1 \le \lambda_2 \le \dots \le \lambda_n$ les valeurs propres de $L$. On sait que $\lambda_1 = 0$ avec le vecteur propre $\mathbf{1}$ (le vecteur de tous les 1), et que $G$ étant connexe, $\lambda_2 > 0$.

De même, on considère le Laplacien normalisé symétrique $L_{sym} = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}$. Ses valeurs propres sont $\mu_1 \le \mu_2 \le \dots \le \mu_n$. On sait que $\mu_1 = 0$ avec le vecteur propre $D^{1/2}\mathbf{1}$, et que $G$ étant connexe, $\mu_2 > 0$.

Cet exercice explore les liens entre les secondes valeurs propres de ces Laplaciens et différentes notions de "coupures optimales" dans un graphe.

---

### Partie 1 : Le Laplacien Combinatoire et les Coupures

1.  Soit $S \subset V$ un sous-ensemble non vide et propre de sommets. On définit le vecteur $x_S \in \mathbb{R}^n$ par $(x_S)_u = 1$ si $u \in S$ et $(x_S)_u = 0$ si $u \notin S$.
    Montrer que $x_S^T L x_S = \text{cut}(S, \bar{S})$, où $\text{cut}(S, \bar{S})$ est le nombre d'arêtes entre $S$ et son complémentaire $\bar{S}$.

2.  Rappeler la définition de la deuxième valeur propre $\lambda_2$ du Laplacien combinatoire $L$ en termes de quotient de Rayleigh.

---

### Partie 2 : Borne inférieure pour la Coupure de Ratio

Pour une partition $(S, \bar{S})$ de $V$, la *coupure de ratio* est définie par $\text{RC}(S, \bar{S}) = \text{cut}(S, \bar{S}) \left( \frac{1}{|S|} + \frac{1}{|\bar{S}|} \right)$.

1.  Soit $S \subset V$ un sous-ensemble non vide et propre. On définit le vecteur $y_S \in \mathbb{R}^n$ par :
    $$ (y_S)_u = \begin{cases} \frac{|\bar{S}|}{n} & \text{si } u \in S \\ -\frac{|S|}{n} & \text{si } u \in \bar{S} \end{cases} $$
    a) Vérifier que $y_S$ est orthogonal au vecteur $\mathbf{1}$, c'est-à-dire $y_S^T \mathbf{1} = 0$.
    b) Calculer $y_S^T L y_S$.
    c) Calculer $y_S^T y_S$.
    d) En déduire que $\lambda_2 \le \text{RC}(S, \bar{S})$ pour toute partition $(S, \bar{S})$.

---

### Partie 3 : Le Laplacien Normalisé et la Coupure Normalisée

La *coupure normalisée* (NCut) d'une partition $(S, \bar{S})$ est définie par $\text{NCut}(S, \bar{S}) = \frac{\text{cut}(S, \bar{S})}{\text{vol}(S)} + \frac{\text{cut}(S, \bar{S})}{\text{vol}(\bar{S})}$, où $\text{vol}(S) = \sum_{u \in S} d_u$ est le volume de $S$.

1.  Montrer que pour tout vecteur $x \in \mathbb{R}^n$, la forme quadratique associée à $L_{sym}$ est donnée par :
    $$ x^T L_{sym} x = \sum_{(u,v) \in E} \left(\frac{x_u}{\sqrt{d_u}} - \frac{x_v}{\sqrt{d_v}}\right)^2 $$

2.  Soit $S \subset V$ un sous-ensemble non vide et propre. On définit le vecteur $z_S \in \mathbb{R}^n$ par :
    $$ (z_S)_u = \begin{cases} \frac{\sqrt{d_u}}{\text{vol}(S)} & \text{si } u \in S \\ -\frac{\sqrt{d_u}}{\text{vol}(\bar{S})} & \text{si } u \in \bar{S} \end{cases} $$
    a) Montrer que $z_S$ est orthogonal au vecteur propre trivial $D^{1/2}\mathbf{1}$ de $L_{sym}$ (associé à $\mu_1=0$). C'est-à-dire, montrer que $\sum_{u \in V} (z_S)_u \sqrt{d_u} = 0$.
    b) Calculer $z_S^T L_{sym} z_S$.
    c) Calculer $z_S^T z_S$.
    d) En déduire que $\mu_2 \le \text{NCut}(S, \bar{S})$ pour toute partition $(S, \bar{S})$.

---

# Correction Détaillée

### Partie 1 : Le Laplacien Combinatoire et les Coupures

1.  La forme quadratique associée au Laplacien combinatoire $L$ est donnée par $x^T L x = \sum_{(u,v) \in E} ((x_u - x_v)^2)$.
    Pour le vecteur $x_S$ défini par $(x_S)_u = 1$ si $u \in S$ et $(x_S)_u = 0$ si $u \notin S$, nous calculons $x_S^T L x_S$:
    $$ x_S^T L x_S = \sum_{(u,v) \in E} ((x_S)_u - (x_S)_v)^2 $$
    Nous analysons les termes de la somme en fonction de la localisation des sommets $u$ et $v$:
    *   Si $u \in S$ et $v \in S$, alors $(x_S)_u = 1$ et $(x_S)_v = 1$. Donc $((x_S)_u - (x_S)_v)^2 = (1-1)^2 = 0$.
    *   Si $u \in \bar{S}$ et $v \in \bar{S}$, alors $(x_S)_u = 0$ et $(x_S)_v = 0$. Donc $((x_S)_u - (x_S)_v)^2 = (0-0)^2 = 0$.
    *   Si $u \in S$ et $v \in \bar{S}$, alors $(x_S)_u = 1$ et $(x_S)_v = 0$. Donc $((x_S)_u - (x_S)_v)^2 = (1-0)^2 = 1$.
    *   Si $u \in \bar{S}$ et $v \in S$, alors $(x_S)_u = 0$ et $(x_S)_v = 1$. Donc $((x_S)_u - (x_S)_v)^2 = (0-1)^2 = 1$.

    Ainsi, seuls les termes correspondant aux arêtes $(u,v)$ qui traversent la coupure (c'est-à-dire avec un sommet dans $S$ et l'autre dans $\bar{S}$) contribuent à la somme. La valeur de chaque contribution est 1.
    Par conséquent, $x_S^T L x_S = \sum_{(u,v) \in E, u \in S, v \in \bar{S}} 1 = \text{cut}(S, \bar{S})$.

2.  La deuxième valeur propre $\lambda_2$ du Laplacien combinatoire $L$ est définie par le quotient de Rayleigh minimisé sur l'espace orthogonal au vecteur propre trivial $\mathbf{1}$ :
    $$ \lambda_2 = \min_{x \in \mathbb{R}^n, x \neq \mathbf{0}, x^T \mathbf{1} = 0} \frac{x^T L x}{x^T x} $$
    où $x^T L x = \sum_{(u,v) \in E} (x_u - x_v)^2$.

### Partie 2 : Borne inférieure pour la Coupure de Ratio

1.  Soit $S \subset V$ un sous-ensemble non vide et propre. On définit le vecteur $y_S \in \mathbb{R}^n$ par $(y_S)_u = \frac{|\bar{S}|}{n}$ si $u \in S$ et $(y_S)_u = -\frac{|S|}{n}$ si $u \in \bar{S}$.

    a) Vérifions que $y_S^T \mathbf{1} = 0$:
    $$ y_S^T \mathbf{1} = \sum_{u \in V} (y_S)_u = \sum_{u \in S} \frac{|\bar{S}|}{n} + \sum_{u \in \bar{S}} \left(-\frac{|S|}{n}\right) $$
    $$ = |S| \frac{|\bar{S}|}{n} - |\bar{S}| \frac{|S|}{n} = \frac{|S||\bar{S}|}{n} - \frac{|S||\bar{S}|}{n} = 0 $$
    Le vecteur $y_S$ est bien orthogonal à $\mathbf{1}$.

    b) Calculons $y_S^T L y_S$:
    $$ y_S^T L y_S = \sum_{(u,v) \in E} ((y_S)_u - (y_S)_v)^2 $$
    *   Si $u \in S$ et $v \in S$, alors $(y_S)_u = \frac{|\bar{S}|}{n}$ et $(y_S)_v = \frac{|\bar{S}|}{n}$. Donc $((y_S)_u - (y_S)_v)^2 = 0$.
    *   Si $u \in \bar{S}$ et $v \in \bar{S}$, alors $(y_S)_u = -\frac{|S|}{n}$ et $(y_S)_v = -\frac{|S|}{n}$. Donc $((y_S)_u - (y_S)_v)^2 = 0$.
    *   Si $u \in S$ et $v \in \bar{S}$, alors $(y_S)_u = \frac{|\bar{S}|}{n}$ et $(y_S)_v = -\frac{|S|}{n}$.
        $$ ((y_S)_u - (y_S)_v)^2 = \left(\frac{|\bar{S}|}{n} - \left(-\frac{|S|}{n}\right)\right)^2 = \left(\frac{|\bar{S}|+|S|}{n}\right)^2 = \left(\frac{n}{n}\right)^2 = 1^2 = 1 $$
    *   Si $u \in \bar{S}$ et $v \in S$, alors $(y_S)_u = -\frac{|S|}{n}$ et $(y_S)_v = \frac{|\bar{S}|}{n}$.
        $$ ((y_S)_u - (y_S)_v)^2 = \left(-\frac{|S|}{n} - \frac{|\bar{S}|}{n}\right)^2 = \left(-\frac{|S|+|\bar{S}|}{n}\right)^2 = \left(-\frac{n}{n}\right)^2 = (-1)^2 = 1 $$
    Par conséquent, $y_S^T L y_S = \sum_{(u,v) \in E, u \in S, v \in \bar{S}} 1 = \text{cut}(S, \bar{S})$.

    c) Calculons $y_S^T y_S$:
    $$ y_S^T y_S = \sum_{u \in V} (y_S)_u^2 = \sum_{u \in S} \left(\frac{|\bar{S}|}{n}\right)^2 + \sum_{u \in \bar{S}} \left(-\frac{|S|}{n}\right)^2 $$
    $$ = |S| \frac{|\bar{S}|^2}{n^2} + |\bar{S}| \frac{|S|^2}{n^2} = \frac{|S||\bar{S}|^2 + |\bar{S}||S|^2}{n^2} = \frac{|S||\bar{S}|(|\bar{S}|+|S|)}{n^2} $$
    Puisque $|S|+|\bar{S}| = n$, nous avons :
    $$ y_S^T y_S = \frac{|S||\bar{S}|n}{n^2} = \frac{|S||\bar{S}|}{n} $$

    d) En déduire que $\lambda_2 \le \text{RC}(S, \bar{S})$:
    D'après la définition du quotient de Rayleigh pour $\lambda_2$ (Partie 1, question 2), et puisque $y_S^T \mathbf{1} = 0$ et $y_S \neq \mathbf{0}$ (car $S$ est non vide et propre), nous avons :
    $$ \lambda_2 \le \frac{y_S^T L y_S}{y_S^T y_S} $$
    En substituant les résultats des questions 1b et 1c :
    $$ \lambda_2 \le \frac{\text{cut}(S, \bar{S})}{\frac{|S||\bar{S}|}{n}} = \text{cut}(S, \bar{S}) \frac{n}{|S||\bar{S}|} $$
    D'autre part, la coupure de ratio est définie comme $\text{RC}(S, \bar{S}) = \text{cut}(S, \bar{S}) \left( \frac{1}{|S|} + \frac{1}{|\bar{S}|} \right)$.
    $$ \text{RC}(S, \bar{S}) = \text{cut}(S, \bar{S}) \left( \frac{|\bar{S}|+|S|}{|S||\bar{S}|} \right) = \text{cut}(S, \bar{S}) \frac{n}{|S||\bar{S}|} $$
    Nous voyons que $\frac{y_S^T L y_S}{y_S^T y_S} = \text{RC}(S, \bar{S})$.
    Par conséquent, $\lambda_2 \le \text{RC}(S, \bar{S})$ pour toute partition $(S, \bar{S})$.
    Cela signifie que $\lambda_2$ est une borne inférieure pour la coupure de ratio minimale.

### Partie 3 : Le Laplacien Normalisé et la Coupure Normalisée

1.  La forme quadratique associée au Laplacien normalisé symétrique $L_{sym} = D^{-1/2} L D^{-1/2}$ est donnée par $x^T L_{sym} x$.
    En utilisant la définition de la forme quadratique pour $L$: $y^T L y = \sum_{(u,v) \in E} (y_u - y_v)^2$.
    Soit $y = D^{-1/2}x$, c'est-à-dire $y_u = x_u/\sqrt{d_u}$. Alors $x = D^{1/2}y$.
    $$ x^T L_{sym} x = (D^{1/2}y)^T D^{-1/2} L D^{-1/2} (D^{1/2}y) = y^T D^{1/2} D^{-1/2} L D^{-1/2} D^{1/2} y = y^T L y $$
    $$ = \sum_{(u,v) \in E} (y_u - y_v)^2 = \sum_{(u,v) \in E} \left(\frac{x_u}{\sqrt{d_u}} - \frac{x_v}{\sqrt{d_v}}\right)^2 $$
    Ceci est la forme quadratique recherchée.

2.  Soit $S \subset V$ un sous-ensemble non vide et propre. On définit le vecteur $z_S \in \mathbb{R}^n$ par :
    $$ (z_S)_u = \begin{cases} \frac{\sqrt{d_u}}{\text{vol}(S)} & \text{si } u \in S \\ -\frac{\sqrt{d_u}}{\text{vol}(\bar{S})} & \text{si } u \in \bar{S} \end{cases} $$

    a) Le vecteur propre trivial de $L_{sym}$ associé à $\mu_1=0$ est $D^{1/2}\mathbf{1}$. Ses composantes sont $(D^{1/2}\mathbf{1})_u = \sqrt{d_u}$.
    Pour montrer que $z_S$ est orthogonal à $D^{1/2}\mathbf{1}$, nous devons vérifier que leur produit scalaire est nul :
    $$ \sum_{u \in V} (z_S)_u (D^{1/2}\mathbf{1})_u = \sum_{u \in V} (z_S)_u \sqrt{d_u} $$
    $$ = \sum_{u \in S} \left(\frac{\sqrt{d_u}}{\text{vol}(S)}\right) \sqrt{d_u} + \sum_{u \in \bar{S}} \left(-\frac{\sqrt{d_u}}{\text{vol}(\bar{S})}\right) \sqrt{d_u} $$
    $$ = \sum_{u \in S} \frac{d_u}{\text{vol}(S)} - \sum_{u \in \bar{S}} \frac{d_u}{\text{vol}(\bar{S})} $$
    Par définition, $\sum_{u \in S} d_u = \text{vol}(S)$ et $\sum_{u \in \bar{S}} d_u = \text{vol}(\bar{S})$.
    $$ = \frac{\text{vol}(S)}{\text{vol}(S)} - \frac{\text{vol}(\bar{S})}{\text{vol}(\bar{S})} = 1 - 1 = 0 $$
    Le vecteur $z_S$ est bien orthogonal à $D^{1/2}\mathbf{1}$.

    b) Calculons $z_S^T L_{sym} z_S$:
    En utilisant la formule de la question 3.1 :
    $$ z_S^T L_{sym} z_S = \sum_{(u,v) \in E} \left(\frac{(z_S)_u}{\sqrt{d_u}} - \frac{(z_S)_v}{\sqrt{d_v}}\right)^2 $$
    Calculons les termes $\frac{(z_S)_u}{\sqrt{d_u}}$ :
    *   Si $u \in S$, alors $\frac{(z_S)_u}{\sqrt{d_u}} = \frac{\sqrt{d_u}/\text{vol}(S)}{\sqrt{d_u}} = \frac{1}{\text{vol}(S)}$.
    *   Si $u \in \bar{S}$, alors $\frac{(z_S)_u}{\sqrt{d_u}} = \frac{-\sqrt{d_u}/\text{vol}(\bar{S})}{\sqrt{d_u}} = -\frac{1}{\text{vol}(\bar{S})}$.

    Maintenant, analysons les termes de la somme :
    *   Si $u \in S$ et $v \in S$, alors $\left(\frac{1}{\text{vol}(S)} - \frac{1}{\text{vol}(S)}\right)^2 = 0$.
    *   Si $u \in \bar{S}$ et $v \in \bar{S}$, alors $\left(-\frac{1}{\text{vol}(\bar{S})} - \left(-\frac{1}{\text{vol}(\bar{S})}\right)\right)^2 = 0$.
    *   Si $u \in S$ et $v \in \bar{S}$, alors $\left(\frac{1}{\text{vol}(S)} - \left(-\frac{1}{\text{vol}(\bar{S})}\right)\right)^2 = \left(\frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})}\right)^2$.
    *   Si $u \in \bar{S}$ et $v \in S$, alors $\left(-\frac{1}{\text{vol}(\bar{S})} - \frac{1}{\text{vol}(S)}\right)^2 = \left(-\left(\frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})}\right)\right)^2 = \left(\frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})}\right)^2$.

    Par conséquent, $z_S^T L_{sym} z_S = \text{cut}(S, \bar{S}) \left(\frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})}\right)^2$.

    c) Calculons $z_S^T z_S$:
    $$ z_S^T z_S = \sum_{u \in V} (z_S)_u^2 = \sum_{u \in S} \left(\frac{\sqrt{d_u}}{\text{vol}(S)}\right)^2 + \sum_{u \in \bar{S}} \left(-\frac{\sqrt{d_u}}{\text{vol}(\bar{S})}\right)^2 $$
    $$ = \sum_{u \in S} \frac{d_u}{\text{vol}(S)^2} + \sum_{u \in \bar{S}} \frac{d_u}{\text{vol}(\bar{S})^2} $$
    $$ = \frac{1}{\text{vol}(S)^2} \sum_{u \in S} d_u + \frac{1}{\text{vol}(\bar{S})^2} \sum_{u \in \bar{S}} d_u $$
    $$ = \frac{\text{vol}(S)}{\text{vol}(S)^2} + \frac{\text{vol}(\bar{S})}{\text{vol}(\bar{S})^2} = \frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})} $$

    d) En déduire que $\mu_2 \le \text{NCut}(S, \bar{S})$:
    D'après la définition du quotient de Rayleigh pour $\mu_2$, et puisque $z_S$ est orthogonal à $D^{1/2}\mathbf{1}$ et $z_S \neq \mathbf{0}$ (car $S$ est non vide et propre), nous avons :
    $$ \mu_2 \le \frac{z_S^T L_{sym} z_S}{z_S^T z_S} $$
    En substituant les résultats des questions 3.2b et 3.2c :
    $$ \mu_2 \le \frac{\text{cut}(S, \bar{S}) \left(\frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})}\right)^2}{\frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})}} $$
    $$ \mu_2 \le \text{cut}(S, \bar{S}) \left(\frac{1}{\text{vol}(S)} + \frac{1}{\text{vol}(\bar{S})}\right) $$
    Ceci est exactement la définition de $\text{NCut}(S, \bar{S})$.
    Donc, $\mu_2 \le \text{NCut}(S, \bar{S})$ pour toute partition $(S, \bar{S})$.
    Cela signifie que $\mu_2$ est une borne inférieure pour la coupure normalisée minimale.
