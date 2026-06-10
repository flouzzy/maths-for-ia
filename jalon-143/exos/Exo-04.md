```yaml
uuid: 143-04
title: "Analyse Spectrale d'un Graphe Composé : Le Cas des Graphes Completement Connectés par une Arête"
```

## Exercice 4 : Analyse Spectrale d'un Graphe Composé

**Contexte :**
Nous étudions les propriétés spectrales des graphes, en particulier comment les matrices Laplaciennes (combinatoire et normalisée) sont liées aux coupures de graphes. Ces concepts sont fondamentaux pour la compréhension de la structure des graphes et pour des applications telles que la segmentation d'images ou le partitionnement de réseaux.

**Définition du Graphe :**
Soit $G = (V, E)$ un graphe non orienté, simple et connexe. On considère un graphe $G$ construit à partir de deux graphes complets $K_n$ et $K_m$ (avec $n, m \ge 2$). Soient $V_1$ l'ensemble des sommets de $K_n$ et $V_2$ l'ensemble des sommets de $K_m$. Le graphe $G$ est formé en ajoutant une unique arête $(u, v)$ entre un sommet $u \in V_1$ et un sommet $v \in V_2$. Tous les autres sommets de $V_1 \setminus \{u\}$ ne sont connectés qu'à des sommets de $V_1$, et de même pour $V_2 \setminus \{v\}$.
*   Le nombre total de sommets est $|V| = n+m$.
*   Le nombre total d'arêtes est $|E| = \binom{n}{2} + \binom{m}{2} + 1$.

**Questions :**

1.  **Analyse du Laplacien Combinatoire et des Coupures :**
    *   a) Déterminez les degrés $d_i$ de tous les sommets $i \in V$ de $G$.
    *   b) Soit $x \in \mathbb{R}^{|V|}$ un vecteur. Démontrez la forme quadratique suivante pour le Laplacien combinatoire $L$ de $G$ :
        $$x^T L x = \sum_{(i,j) \in E} (x_i - x_j)^2$$
    *   c) Considérons la coupure $S = V_1$ et $\bar{S} = V_2$. Calculez la taille de cette coupure, notée $|E(S, \bar{S})|$.
    *   d) En utilisant la forme quadratique de la question (b), construisez un vecteur $x^*$ non nul et orthogonal au vecteur $\mathbf{1}$ (le vecteur de tous les uns) tel que $x^{*T} L x^*$ soit directement lié à la structure de la coupure $(V_1, V_2)$. Calculez le quotient de Rayleigh $\frac{x^{*T} L x^*}{x^{*T} x^*}$ pour ce vecteur. Discutez qualitativement pourquoi la deuxième plus petite valeur propre $\lambda_1(L)$ du Laplacien combinatoire est susceptible d'être petite pour ce type de graphe, en particulier lorsque $n$ et $m$ sont grands.

2.  **Analyse du Laplacien Normalisé et de la Constante de Cheeger :**
    *   a) Rappelez la définition du Laplacien normalisé $\mathcal{L} = I - D^{-1/2} A D^{-1/2}$, où $D$ est la matrice des degrés et $A$ est la matrice d'adjacence.
    *   b) Calculez le volume de $S=V_1$ et $\bar{S}=V_2$, notés $\text{vol}(S)$ et $\text{vol}(\bar{S})$. Rappel : $\text{vol}(S) = \sum_{i \in S} d_i$.
    *   c) Calculez la valeur de la coupure de Cheeger $\Phi(S) = \frac{|E(S, \bar{S})|}{\min(\text{vol}(S), \text{vol}(\bar{S}))}$ pour la coupure $(V_1, V_2)$.
    *   d) Discutez comment la deuxième plus petite valeur propre $\mu_1(\mathcal{L})$ du Laplacien normalisé reflète la présence de cette coupure "goulot d'étranglement" (bottleneck) et comment elle est liée à la constante de Cheeger du graphe.

---

## Correction Détaillée

### 1. Analyse du Laplacien Combinatoire et des Coupures :

**a) Détermination des degrés des sommets :**
Soit $V_1 = \{u_1, \dots, u_n\}$ et $V_2 = \{v_1, \dots, v_m\}$. Sans perte de généralité, supposons que l'arête de connexion est $(u_1, v_1)$, donc $u=u_1$ et $v=v_1$.

*   Pour les sommets $u_i \in V_1 \setminus \{u_1\}$ (il y en a $n-1$) : Chaque $u_i$ est connecté aux $n-1$ autres sommets de $K_n$. Son degré est donc $d_{u_i} = n-1$.
*   Pour le sommet $u_1 \in V_1$ : Il est connecté aux $n-1$ autres sommets de $K_n$ et à $v_1 \in V_2$. Son degré est donc $d_{u_1} = (n-1) + 1 = n$.
*   Pour les sommets $v_j \in V_2 \setminus \{v_1\}$ (il y en a $m-1$) : Chaque $v_j$ est connecté aux $m-1$ autres sommets de $K_m$. Son degré est donc $d_{v_j} = m-1$.
*   Pour le sommet $v_1 \in V_2$ : Il est connecté aux $m-1$ autres sommets de $K_m$ et à $u_1 \in V_1$. Son degré est donc $d_{v_1} = (m-1) + 1 = m$.

**b) Démonstration de la forme quadratique $x^T L x = \sum_{(i,j) \in E} (x_i - x_j)^2$ :**
Le Laplacien combinatoire $L$ est défini comme $L = D - A$, où $D$ est la matrice des degrés (diagonale, $D_{ii} = d_i$) et $A$ est la matrice d'adjacence.
Considérons la forme quadratique $x^T L x$ :
$$x^T L x = x^T (D - A) x = x^T D x - x^T A x$$
Le terme $x^T D x$ est :
$$x^T D x = \sum_{i=1}^{|V|} x_i (D x)_i = \sum_{i=1}^{|V|} x_i (d_i x_i) = \sum_{i=1}^{|V|} d_i x_i^2$$
Le terme $x^T A x$ est :
$$x^T A x = \sum_{i=1}^{|V|} \sum_{j=1}^{|V|} x_i A_{ij} x_j$$
Puisque $A_{ij}=1$ si $(i,j) \in E$ et $A_{ij}=0$ sinon (et $A_{ii}=0$), et que le graphe est non orienté ($A_{ij}=A_{ji}$), on a :
$$x^T A x = \sum_{(i,j) \in E} (x_i A_{ij} x_j + x_j A_{ji} x_i) = \sum_{(i,j) \in E} (x_i x_j + x_j x_i) = \sum_{(i,j) \in E} 2 x_i x_j$$
En combinant les deux termes :
$$x^T L x = \sum_{i=1}^{|V|} d_i x_i^2 - \sum_{(i,j) \in E} 2 x_i x_j$$
Nous savons que $d_i = \sum_{j \text{ t.q. } (i,j) \in E} 1$. Donc $\sum_{i=1}^{|V|} d_i x_i^2 = \sum_{i=1}^{|V|} \sum_{j \text{ t.q. } (i,j) \in E} x_i^2$.
Puisque chaque arête $(i,j)$ est comptée deux fois dans cette somme (une fois pour $i$ et une fois pour $j$), on peut écrire :
$$\sum_{i=1}^{|V|} d_i x_i^2 = \sum_{(i,j) \in E} (x_i^2 + x_j^2)$$
En substituant cela dans l'expression de $x^T L x$ :
$$x^T L x = \sum_{(i,j) \in E} (x_i^2 + x_j^2) - \sum_{(i,j) \in E} 2 x_i x_j = \sum_{(i,j) \in E} (x_i^2 - 2 x_i x_j + x_j^2) = \sum_{(i,j) \in E} (x_i - x_j)^2$$
La forme quadratique est démontrée.

**c) Calcul de la taille de la coupure $(V_1, V_2)$ :**
La coupure $S=V_1$ et $\bar{S}=V_2$ est l'ensemble des arêtes ayant une extrémité dans $V_1$ et l'autre dans $V_2$. Par construction du graphe $G$, la seule arête entre $V_1$ et $V_2$ est l'arête $(u, v)$.
Donc, $|E(S, \bar{S})| = |E(V_1, V_2)| = 1$.

**d) Construction d'un vecteur $x^*$ et discussion de $\lambda_1(L)$ :**
Nous cherchons un vecteur $x^*$ non nul et orthogonal à $\mathbf{1}$ (le vecteur de tous les uns) tel que $x^{*T} L x^*$ soit lié à la coupure.
Soit $x^*$ un vecteur défini par :
$$x^*_i = \begin{cases} |V_2| = m & \text{si } i \in V_1 \\ -|V_1| = -n & \text{si } i \in V_2 \end{cases}$$
Vérifions que $x^* \ne \mathbf{0}$ (ce qui est vrai car $n,m \ge 2$) et que $x^*$ est orthogonal à $\mathbf{1}$ :
$$\sum_{i \in V} x^*_i = \sum_{i \in V_1} m + \sum_{i \in V_2} (-n) = n \cdot m + m \cdot (-n) = nm - mn = 0$$
Le vecteur $x^*$ est bien orthogonal à $\mathbf{1}$.
Calculons $x^{*T} L x^*$ en utilisant la forme quadratique de la question (b) :
$$x^{*T} L x^* = \sum_{(i,j) \in E} (x^*_i - x^*_j)^2$$
*   Si $(i,j)$ est une arête interne à $V_1$ (i.e., $i,j \in V_1$), alors $x^*_i = m$ et $x^*_j = m$. Donc $(x^*_i - x^*_j)^2 = (m-m)^2 = 0$.
*   Si $(i,j)$ est une arête interne à $V_2$ (i.e., $i,j \in V_2$), alors $x^*_i = -n$ et $x^*_j = -n$. Donc $(x^*_i - x^*_j)^2 = (-n - (-n))^2 = 0$.
*   Si $(i,j)$ est l'arête de connexion $(u,v)$ (où $u \in V_1, v \in V_2$), alors $x^*_u = m$ et $x^*_v = -n$. Donc $(x^*_u - x^*_v)^2 = (m - (-n))^2 = (m+n)^2$.
Ainsi, la somme ne contient qu'un seul terme non nul :
$$x^{*T} L x^* = (m+n)^2$$
Maintenant, calculons $x^{*T} x^*$ :
$$x^{*T} x^* = \sum_{i \in V} (x^*_i)^2 = \sum_{i \in V_1} m^2 + \sum_{i \in V_2} (-n)^2 = n \cdot m^2 + m \cdot n^2 = nm(m+n)$$
Le quotient de Rayleigh pour ce vecteur $x^*$ est :
$$\frac{x^{*T} L x^*}{x^{*T} x^*} = \frac{(m+n)^2}{nm(m+n)} = \frac{m+n}{nm} = \frac{1}{n} + \frac{1}{m}$$
La deuxième plus petite valeur propre $\lambda_1(L)$ est donnée par le minimum du quotient de Rayleigh sur tous les vecteurs non nuls orthogonaux à $\mathbf{1}$. Par conséquent, la valeur que nous avons calculée est une borne supérieure pour $\lambda_1(L)$ :
$$\lambda_1(L) \le \frac{1}{n} + \frac{1}{m}$$
Lorsque $n$ et $m$ sont grands, la valeur $\frac{1}{n} + \frac{1}{m}$ devient très petite. Une petite valeur de $\lambda_1(L)$ indique que le graphe est "facile à couper" en deux composants. Dans notre cas, la coupure $(V_1, V_2)$ est un goulot d'étranglement (une seule arête), et la petite valeur de $\lambda_1(L)$ reflète cette faible connectivité entre les deux sous-graphes denses.

### 2. Analyse du Laplacien Normalisé et de la Constante de Cheeger :

**a) Définition du Laplacien normalisé :**
Le Laplacien normalisé $\mathcal{L}$ est défini comme $\mathcal{L} = I - D^{-1/2} A D^{-1/2}$, où $I$ est la matrice identité, $D$ est la matrice des degrés et $A$ est la matrice d'adjacence. Alternativement, il peut être défini comme $\mathcal{L} = D^{-1/2} L D^{-1/2}$.

**b) Calcul des volumes de $S=V_1$ et $\bar{S}=V_2$ :**
Le volume d'un ensemble de sommets $S$ est la somme des degrés des sommets dans $S$, c'est-à-dire $\text{vol}(S) = \sum_{i \in S} d_i$.
En utilisant les degrés calculés en 1.a) :
*   Pour $S=V_1$ :
    $\text{vol}(V_1) = \sum_{u_i \in V_1 \setminus \{u_1\}} d_{u_i} + d_{u_1} = (n-1)(n-1) + n = n^2 - 2n + 1 + n = n^2 - n + 1$.
*   Pour $\bar{S}=V_2$ :
    $\text{vol}(V_2) = \sum_{v_j \in V_2 \setminus \{v_1\}} d_{v_j} + d_{v_1} = (m-1)(m-1) + m = m^2 - 2m + 1 + m = m^2 - m + 1$.

**c) Calcul de la valeur de la coupure de Cheeger $\Phi(S)$ pour la coupure $(V_1, V_2)$ :**
La valeur de la coupure de Cheeger pour un ensemble $S$ est donnée par $\Phi(S) = \frac{|E(S, \bar{S})|}{\min(\text{vol}(S), \text{vol}(\bar{S}))}$.
Nous avons calculé $|E(S, \bar{S})| = 1$ en 1.c).
Nous avons calculé $\text{vol}(V_1) = n^2 - n + 1$ et $\text{vol}(V_2) = m^2 - m + 1$.
Donc, pour la coupure $(V_1, V_2)$ :
$$\Phi(V_1) = \frac{1}{\min(n^2 - n + 1, m^2 - m + 1)}$$

**d) Discussion sur la relation entre $\mu_1(\mathcal{L})$ et la constante de Cheeger :**
La constante de Cheeger $h_G$ d'un graphe $G$ est définie comme le minimum de $\Phi(S)$ sur toutes les coupures $S$ telles que $\text{vol}(S) \le \text{vol}(V)/2$. La coupure $(V_1, V_2)$ est un candidat très fort pour être la coupure de Cheeger minimale dans ce type de graphe, car elle est la seule coupure de taille 1.
Les inégalités de Cheeger établissent une relation fondamentale entre la deuxième plus petite valeur propre du Laplacien normalisé, $\mu_1(\mathcal{L})$, et la constante de Cheeger $h_G$ :
$$\frac{\mu_1(\mathcal{L})}{2} \le h_G \le \sqrt{2\mu_1(\mathcal{L})}$$
Dans notre cas, si la coupure $(V_1, V_2)$ est la coupure de Cheeger optimale (ce qui est très probable pour $n,m \ge 2$), alors $h_G = \Phi(V_1) = \frac{1}{\min(n^2 - n + 1, m^2 - m + 1)}$.
Lorsque $n$ et $m$ sont grands, $\min(n^2 - n + 1, m^2 - m + 1)$ devient très grand. Par conséquent, $\Phi(V_1)$ devient très petit.
Selon les inégalités de Cheeger, une petite valeur de $h_G$ implique une petite valeur de $\mu_1(\mathcal{L})$.
La petite valeur de $\mu_1(\mathcal{L})$ reflète la présence d'un "goulot d'étranglement" dans le graphe. Cela signifie que le graphe peut être partitionné en deux sous-ensembles de sommets (ici $V_1$ et $V_2$) qui sont très denses en interne (car ce sont des cliques) mais faiblement connectés entre eux (par une seule arête), par rapport à leur volume. Le Laplacien normalisé est particulièrement adapté pour détecter de telles structures, car il pondère les coupures par le volume des composants, évitant ainsi de privilégier les coupures de petits composants isolés. Une petite $\mu_1(\mathcal{L})$ est donc un indicateur spectral fort d'une bonne partitionnement en deux communautés faiblement connectées.
