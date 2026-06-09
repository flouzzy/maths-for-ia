---
uuid: "jalon-143"
title: "Théorie spectrale des graphes"
year: 3
trimester: 12
tags:
  - math/fondations
  - ia/theorie
prev: "[[Jalon-142.md]]"
next: "[[Jalon 144 (Le phénomène de double descente).md]]"
---

# Jalon 143 : Théorie spectrale des graphes

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*
- **La Métaphore :** Imaginez un réseau de trampolines interconnectés. Chaque trampoline représente un point (un "sommet") et les ressorts qui les relient représentent les liens (les "arêtes"). Si vous tapez sur un trampoline, l'onde se propage à travers le réseau. La "théorie spectrale des graphes" est l'étude des "fréquences naturelles" ou des "modes de vibration" de ce réseau. Tout comme un instrument de musique a un son unique défini par ses fréquences fondamentales, un réseau a des propriétés intrinsèques révélées par ses "fréquences spectrales". Ces fréquences nous disent comment le réseau est structuré, s'il est facile à briser en morceaux, ou comment l'information pourrait y circuler.
- **Le "Pourquoi on a inventé ça" :** Historiquement, les mathématiciens et les scientifiques ont cherché des moyens de comprendre la structure globale de systèmes complexes interconnectés, bien au-delà de la simple liste de leurs connexions. Comment identifier les communautés dans un réseau social ? Comment segmenter une image en régions cohérentes ? Comment prédire la robustesse d'un réseau électrique ? Les méthodes traditionnelles de la théorie des graphes, basées sur des parcours ou des flux, étaient souvent trop locales ou trop coûteuses. L'idée était d'emprunter les outils puissants de l'algèbre linéaire (valeurs propres et vecteurs propres) pour "sonder" le graphe dans son ensemble, révélant des propriétés structurelles profondes qui ne sont pas évidentes à première vue. C'était une quête pour trouver une "empreinte digitale" mathématique unique pour chaque réseau.
- **Visualisation :** Imaginez un graphe dessiné sur une feuille de papier. Si vous pouviez attribuer une "hauteur" ou une "intensité de couleur" à chaque sommet, et que ces hauteurs devaient respecter certaines règles de "lissage" par rapport aux connexions, alors les "modes de vibration" du graphe correspondraient à des motifs de hauteurs spécifiques. Par exemple, le mode de vibration le plus simple (associé à la plus petite "fréquence" non nulle) pourrait montrer une séparation naturelle du graphe en deux groupes : les sommets d'un groupe auraient des hauteurs positives, et ceux de l'autre des hauteurs négatives. La "coupure" entre ces deux groupes serait l'endroit où la transition de hauteur est la plus abrupte, indiquant une faiblesse structurelle du réseau. C'est comme si le graphe lui-même nous "disait" où il préférerait se diviser.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $G = (V, E)$ un graphe non orienté simple, où $V = \{v_1, \dots, v_n\}$ est l'ensemble des $n$ sommets et $E \subseteq \{\{u,v\} \mid u,v \in V, u \neq v\}$ est l'ensemble des $m$ arêtes. Un graphe est simple s'il ne contient ni boucles (arêtes reliant un sommet à lui-même) ni arêtes multiples entre les mêmes paires de sommets.

1.  **Matrice d'Adjacence :**
    La matrice d'adjacence $A(G) \in \mathbb{R}^{n \times n}$ d'un graphe $G$ est définie par ses coefficients $A_{ij}$ pour $i,j \in \{1, \dots, n\}$ :
    $$A_{ij} = \begin{cases} 1 & \text{si } \{v_i, v_j\} \in E \\ 0 & \text{sinon} \end{cases}$$
    Pour un graphe non orienté, $A(G)$ est une matrice symétrique, c'est-à-dire $A_{ij} = A_{ji}$.

2.  **Degré d'un Sommet :**
    Le degré $\deg(v_i)$ d'un sommet $v_i \in V$ est le nombre d'arêtes incidentes à $v_i$. Formellement :
    $$\deg(v_i) = \sum_{j=1}^n A_{ij}$$

3.  **Matrice de Degrés :**
    La matrice de degrés $D(G) \in \mathbb{R}^{n \times n}$ est une matrice diagonale dont les éléments diagonaux sont les degrés des sommets :
    $$D_{ii} = \deg(v_i) \quad \text{et} \quad D_{ij} = 0 \text{ pour } i \neq j$$

4.  **Laplacien Combinatoire (ou Laplacien non-normalisé) :**
    Le Laplacien combinatoire $L(G) \in \mathbb{R}^{n \times n}$ est défini comme la différence entre la matrice de degrés et la matrice d'adjacence :
    $$L(G) = D(G) - A(G)$$
    Ses coefficients sont donnés par :
    $$L_{ij} = \begin{cases} \deg(v_i) & \text{si } i=j \\ -1 & \text{si } \{v_i, v_j\} \in E \\ 0 & \text{sinon (si } i \neq j \text{ et } \{v_i, v_j\} \notin E) \end{cases}$$

5.  **Laplacien Normalisé Symétrique :**
    Le Laplacien normalisé symétrique $\mathcal{L}_{sym}(G) \in \mathbb{R}^{n \times n}$ est défini pour les graphes sans sommets isolés (c'est-à-dire $\deg(v_i) > 0$ pour tout $v_i \in V$). Soit $D^{-1/2}$ la matrice diagonale dont les éléments diagonaux sont $1/\sqrt{\deg(v_i)}$.
    $$\mathcal{L}_{sym}(G) = D^{-1/2} L(G) D^{-1/2} = I_n - D^{-1/2} A(G) D^{-1/2}$$
    où $I_n$ est la matrice identité de taille $n$. Ses coefficients sont :
    $$(\mathcal{L}_{sym})_{ij} = \begin{cases} 1 & \text{si } i=j \text{ et } \deg(v_i) > 0 \\ - \frac{1}{\sqrt{\deg(v_i)\deg(v_j)}} & \text{si } \{v_i, v_j\} \in E \\ 0 & \text{sinon} \end{cases}$$

6.  **Laplacien Normalisé de Marche Aléatoire (Random Walk) :**
    Le Laplacien normalisé de marche aléatoire $\mathcal{L}_{rw}(G) \in \mathbb{R}^{n \times n}$ est défini pour les graphes sans sommets isolés :
    $$\mathcal{L}_{rw}(G) = D^{-1} L(G) = I_n - D^{-1} A(G)$$
    Ses coefficients sont :
    $$(\mathcal{L}_{rw})_{ij} = \begin{cases} 1 & \text{si } i=j \text{ et } \deg(v_i) > 0 \\ - \frac{1}{\deg(v_i)} & \text{si } \{v_i, v_j\} \in E \\ 0 & \text{sinon} \end{cases}$$

7.  **Valeurs Propres et Vecteurs Propres :**
    Pour une matrice carrée $M \in \mathbb{R}^{n \times n}$, un scalaire $\lambda \in \mathbb{C}$ est une valeur propre de $M$ s'il existe un vecteur non nul $x \in \mathbb{C}^n$ tel que $Mx = \lambda x$. Le vecteur $x$ est appelé vecteur propre associé à $\lambda$. Pour les matrices symétriques (comme $L(G)$ et $\mathcal{L}_{sym}(G)$), toutes les valeurs propres sont réelles et les vecteurs propres associés à des valeurs propres distinctes sont orthogonaux.

8.  **Coupure (Cut) :**
    Étant donné un graphe $G=(V,E)$ et un sous-ensemble de sommets $S \subset V$, la coupure entre $S$ et son complémentaire $\bar{S} = V \setminus S$ est l'ensemble des arêtes qui relient un sommet de $S$ à un sommet de $\bar{S}$. La capacité de cette coupure, notée $\text{cut}(S, \bar{S})$, est le nombre d'arêtes dans cet ensemble :
    $$\text{cut}(S, \bar{S}) = |\{\{u,v\} \in E \mid u \in S, v \in \bar{S}\}|$$

9.  **Min-Cut :**
    Le problème du Min-Cut consiste à trouver une partition de $V$ en deux sous-ensembles non vides $S$ et $\bar{S}$ telle que $\text{cut}(S, \bar{S})$ soit minimisé.

10. **Normalized Cut (Ncut) :**
    Pour une partition $(S, \bar{S})$ de $V$, le Normalized Cut est défini comme :
    $$\text{Ncut}(S, \bar{S}) = \frac{\text{cut}(S, \bar{S})}{\text{vol}(S)} + \frac{\text{cut}(S, \bar{S})}{\text{vol}(\bar{S})}$$
    où $\text{vol}(S) = \sum_{v_i \in S} \deg(v_i)$ est le volume de $S$. Le problème du Normalized Cut est de trouver une partition qui minimise cette valeur.

### B. Théorèmes, Propositions & Lemmes
> **Théorème 1 (Propriétés Fondamentales du Laplacien Combinatoire) :**
> Soit $G = (V, E)$ un graphe non orienté simple à $n$ sommets et $L(G)$ son Laplacien combinatoire. Alors :
> 1.  $L(G)$ est une matrice symétrique.
> 2.  $L(G)$ est une matrice semi-définie positive.
> 3.  Pour tout vecteur $x \in \mathbb{R}^n$, la forme quadratique associée est donnée par :
>     $$x^T L(G) x = \sum_{\{v_i, v_j\} \in E} (x_i - x_j)^2$$
> 4.  Le plus petit valeur propre de $L(G)$ est $\lambda_0 = 0$. Le vecteur $\mathbf{1} = (1, 1, \dots, 1)^T$ est un vecteur propre associé à $\lambda_0$.
> 5.  La multiplicité de la valeur propre $0$ est égale au nombre de composantes connexes du graphe $G$.
> 6.  Si $G$ est connexe, alors la deuxième plus petite valeur propre $\lambda_1$ (appelée valeur de Fiedler) est strictement positive ($\lambda_1 > 0$). Le vecteur propre associé, appelé vecteur de Fiedler, est crucial pour le partitionnement de graphes.

> **Théorème 2 (Propriétés Fondamentales du Laplacien Normalisé Symétrique) :**
> Soit $G = (V, E)$ un graphe non orienté simple sans sommets isolés, et $\mathcal{L}_{sym}(G)$ son Laplacien normalisé symétrique. Alors :
> 1.  $\mathcal{L}_{sym}(G)$ est une matrice symétrique.
> 2.  $\mathcal{L}_{sym}(G)$ est une matrice semi-définie positive.
> 3.  Pour tout vecteur $x \in \mathbb{R}^n$, la forme quadratique associée est donnée par :
>     $$x^T \mathcal{L}_{sym}(G) x = \sum_{\{v_i, v_j\} \in E} \left( \frac{x_i}{\sqrt{\deg(v_i)}} - \frac{x_j}{\sqrt{\deg(v_j)}} \right)^2$$
> 4.  Les valeurs propres de $\mathcal{L}_{sym}(G)$ sont réelles et appartiennent à l'intervalle $[0, 2]$.
> 5.  Le plus petit valeur propre est $\lambda_0 = 0$. Le vecteur $D^{1/2}\mathbf{1}$ est un vecteur propre associé à $\lambda_0$.
> 6.  La multiplicité de la valeur propre $0$ est égale au nombre de composantes connexes du graphe $G$.
> 7.  Le problème de minimisation du Normalized Cut est approximé par la minimisation du quotient de Rayleigh pour $\mathcal{L}_{sym}(G)$. Plus précisément, si $y \in \mathbb{R}^n$ est un vecteur tel que $y_i = \sqrt{\deg(v_i)}$ pour $v_i \in S$ et $y_i = -\sqrt{\deg(v_i)}$ pour $v_i \in \bar{S}$, alors :
>     $$\text{Ncut}(S, \bar{S}) = \frac{y^T \mathcal{L}_{sym}(G) y}{y^T y}$$
>     La solution continue relaxée du problème de minimisation du Normalized Cut est donnée par le vecteur propre associé à la deuxième plus petite valeur propre non nulle de $\mathcal{L}_{sym}(G)$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Propriétés Fondamentales du Laplacien Combinatoire
Nous allons démontrer les points 1, 2, 3, 4 et 5 du Théorème 1.

1.  **Initialisation / Cadre :**
    Soit $G=(V,E)$ un graphe non orienté simple avec $n=|V|$ sommets. Soit $L = D-A$ son Laplacien combinatoire, où $D$ est la matrice de degrés et $A$ est la matrice d'adjacence de $G$. Nous allons démontrer que $L$ est symétrique, semi-définie positive, que sa forme quadratique est $\sum_{\{v_i, v_j\} \in E} (x_i - x_j)^2$, que $0$ est une valeur propre avec $\mathbf{1}$ comme vecteur propre, et que la multiplicité de $0$ est le nombre de composantes connexes.

2.  **Étape 1 : Symétrie de $L(G)$**
    *   **Explication textuelle précise de l'action mathématique :** Nous devons montrer que $L_{ij} = L_{ji}$ pour tous $i,j$. Par définition, $L = D - A$. La matrice $D$ est une matrice diagonale, donc $D_{ij} = D_{ji}$ pour tous $i,j$ (en fait, $D_{ij}=0$ si $i \neq j$). La matrice $A$ est la matrice d'adjacence d'un graphe non orienté, ce qui signifie que $A_{ij} = A_{ji}$ pour tous $i,j$.
    *   **Formule ou égalité ultra-détaillée :**
        Pour tout $i,j \in \{1, \dots, n\}$ :
        $$L_{ij} = D_{ij} - A_{ij}$$
        $$L_{ji} = D_{ji} - A_{ji}$$
        Puisque $D_{ij} = D_{ji}$ (car $D$ est diagonale) et $A_{ij} = A_{ji}$ (car $A$ est symétrique pour un graphe non orienté), il s'ensuit que :
        $$L_{ij} = D_{ij} - A_{ij} = D_{ji} - A_{ji} = L_{ji}$$
        Donc, $L(G)$ est une matrice symétrique.

3.  **Étape 2 : Forme quadratique $x^T L(G) x$ et semi-définie positivité**
    *   **Explication textuelle précise de l'action mathématique :** Nous allons calculer la forme quadratique $x^T L x$ pour un vecteur $x = (x_1, \dots, x_n)^T \in \mathbb{R}^n$. Nous allons décomposer ce calcul en deux parties, $x^T D x$ et $x^T A x$, puis les combiner.
    *   **Développement complet :**
        $$x^T L x = x^T (D - A) x = x^T D x - x^T A x$$
        Calculons d'abord $x^T D x$:
        $$x^T D x = \sum_{i=1}^n \sum_{j=1}^n x_i D_{ij} x_j$$
        Puisque $D$ est une matrice diagonale, $D_{ij} = 0$ pour $i \neq j$, et $D_{ii} = \deg(v_i)$.
        $$x^T D x = \sum_{i=1}^n x_i D_{ii} x_i = \sum_{i=1}^n \deg(v_i) x_i^2$$
        Calculons ensuite $x^T A x$:
        $$x^T A x = \sum_{i=1}^n \sum_{j=1}^n x_i A_{ij} x_j$$
        Puisque $A_{ij} = 1$ si $\{v_i, v_j\} \in E$ et $0$ sinon, et $A_{ij} = A_{ji}$ pour un graphe non orienté :
        $$x^T A x = \sum_{\{v_i, v_j\} \in E} (x_i A_{ij} x_j + x_j A_{ji} x_i) = \sum_{\{v_i, v_j\} \in E} (x_i \cdot 1 \cdot x_j + x_j \cdot 1 \cdot x_i) = \sum_{\{v_i, v_j\} \in E} 2 x_i x_j$$
        Maintenant, combinons les deux termes :
        $$x^T L x = \sum_{i=1}^n \deg(v_i) x_i^2 - \sum_{\{v_i, v_j\} \in E} 2 x_i x_j$$
        Nous savons que $\deg(v_i) = \sum_{j \text{ t.q. } \{v_i, v_j\} \in E} 1$. Substituons cela dans le premier terme :
        $$x^T L x = \sum_{i=1}^n \left( \sum_{j \text{ t.q. } \{v_i, v_j\} \in E} 1 \right) x_i^2 - \sum_{\{v_i, v_j\} \in E} 2 x_i x_j$$
        Le premier terme peut être réécrit en sommant sur les arêtes. Pour chaque arête $\{v_i, v_j\} \in E$, $x_i^2$ est inclus dans la somme pour $\deg(v_i)$ et $x_j^2$ est inclus dans la somme pour $\deg(v_j)$. Donc :
        $$x^T L x = \sum_{\{v_i, v_j\} \in E} (x_i^2 + x_j^2) - \sum_{\{v_i, v_j\} \in E} 2 x_i x_j$$
        Regroupons les termes sous une seule somme :
        $$x^T L x = \sum_{\{v_i, v_j\} \in E} (x_i^2 + x_j^2 - 2 x_i x_j)$$
        Nous reconnaissons l'identité remarquable $(a-b)^2 = a^2 - 2ab + b^2$ :
        $$x^T L x = \sum_{\{v_i, v_j\} \in E} (x_i - x_j)^2$$
        Puisque $(x_i - x_j)^2 \ge 0$ pour tout $i,j \in \{1, \dots, n\}$, il s'ensuit que $x^T L x \ge 0$ pour tout $x \in \mathbb{R}^n$.
        Par définition, une matrice symétrique $M$ est semi-définie positive si et seulement si $x^T M x \ge 0$ pour tout $x \in \mathbb{R}^n$.
        Donc, $L(G)$ est une matrice semi-définie positive.

4.  **Étape 3 : La valeur propre 0 et son vecteur propre $\mathbf{1}$**
    *   **Explication textuelle précise de l'action mathématique :** Nous allons montrer que le vecteur $\mathbf{1} = (1, 1, \dots, 1)^T$ est un vecteur propre de $L(G)$ associé à la valeur propre $0$. Pour cela, nous devons vérifier que $L(G)\mathbf{1} = \mathbf{0}$.
    *   **Développement complet :**
        Considérons le produit $L\mathbf{1}$. La $i$-ème composante de ce vecteur est donnée par :
        $$(L\mathbf{1})_i = \sum_{j=1}^n L_{ij} \cdot 1$$
        En utilisant la définition des coefficients de $L$:
        $$(L\mathbf{1})_i = L_{ii} \cdot 1 + \sum_{j \neq i, \{v_i, v_j\} \in E} L_{ij} \cdot 1 + \sum_{j \neq i, \{v_i, v_j\} \notin E} L_{ij} \cdot 1$$
        $$(L\mathbf{1})_i = \deg(v_i) \cdot 1 + \sum_{j \neq i, \{v_i, v_j\} \in E} (-1) \cdot 1 + \sum_{j \neq i, \{v_i, v_j\} \notin E} 0 \cdot 1$$
        $$(L\mathbf{1})_i = \deg(v_i) - \sum_{j \text{ t.q. } \{v_i, v_j\} \in E} 1$$
        Par définition du degré d'un sommet :
        $$\deg(v_i) = \sum_{j \text{ t.q. } \{v_i, v_j\} \in E} 1$$
        Donc :
        $$(L\mathbf{1})_i = \deg(v_i) - \deg(v_i) = 0$$
        Puisque cette égalité est vraie pour toutes les composantes $i=1, \dots, n$, nous avons $L\mathbf{1} = \mathbf{0}$.
        Ceci signifie que $\mathbf{1}$ est un vecteur propre de $L(G)$ associé à la valeur propre $\lambda = 0$.
        Puisque $L(G)$ est semi-définie positive, toutes ses valeurs propres sont non négatives. Donc $0$ est la plus petite valeur propre.

5.  **Étape 4 : Multiplicité de la valeur propre 0 et composantes connexes**
    *   **Explication textuelle précise de l'action mathématique :** Nous allons montrer que la dimension du noyau de $L(G)$ (l'espace propre associé à la valeur propre 0) est égale au nombre de composantes connexes du graphe $G$.
    *   **Développement complet :**
        Soit $x \in \mathbb{R}^n$ un vecteur propre associé à la valeur propre $0$. Alors $Lx = \mathbf{0}$.
        D'après l'Étape 2, nous savons que $x^T L x = \sum_{\{v_i, v_j\} \in E} (x_i - x_j)^2$.
        Si $Lx = \mathbf{0}$, alors $x^T L x = x^T \mathbf{0} = 0$.
        Donc, $\sum_{\{v_i, v_j\} \in E} (x_i - x_j)^2 = 0$.
        Puisque chaque terme $(x_i - x_j)^2$ est non négatif, cette somme est nulle si et seulement si chaque terme est nul :
        $$(x_i - x_j)^2 = 0 \quad \text{pour toutes les arêtes } \{v_i, v_j\} \in E$$
        Ceci implique que $x_i = x_j$ pour toutes les arêtes $\{v_i, v_j\} \in E$.
        Considérons les composantes connexes de $G$. Soient $G_1, G_2, \dots, G_k$ les $k$ composantes connexes de $G$.
        Si $v_i$ et $v_j$ appartiennent à la même composante connexe $G_p$, alors il existe un chemin entre $v_i$ et $v_j$. En suivant ce chemin, nous pouvons déduire que $x_i$ doit être égal à $x_j$.
        Par exemple, si $v_i \sim v_{a_1} \sim v_{a_2} \sim \dots \sim v_{a_p} \sim v_j$, alors $x_i = x_{a_1}$, $x_{a_1} = x_{a_2}$, et ainsi de suite, jusqu'à $x_{a_p} = x_j$. Par transitivité, $x_i = x_j$.
        Cela signifie que $x$ doit être constant sur chaque composante connexe. Autrement dit, si $v_i, v_j \in V_p$ (où $V_p$ est l'ensemble des sommets de $G_p$), alors $x_i = x_j$.
        Soit $c_p$ la valeur constante de $x$ sur les sommets de $G_p$.
        Un tel vecteur $x$ peut être écrit comme une combinaison linéaire de $k$ vecteurs indicateurs. Pour chaque composante connexe $G_p$, définissons un vecteur $u_p \in \mathbb{R}^n$ tel que $(u_p)_i = 1$ si $v_i \in V_p$ et $(u_p)_i = 0$ sinon.
        Les vecteurs $u_1, u_2, \dots, u_k$ sont linéairement indépendants.
        Tout vecteur $x$ dans le noyau de $L(G)$ peut être écrit comme $x = c_1 u_1 + c_2 u_2 + \dots + c_k u_k$ pour des constantes $c_1, \dots, c_k \in \mathbb{R}$.
        L'espace propre associé à la valeur propre $0$ est donc engendré par ces $k$ vecteurs $u_p$.
        La dimension de cet espace propre est $k$, le nombre de composantes connexes de $G$.
        Par conséquent, la multiplicité de la valeur propre $0$ est égale au nombre de composantes connexes du graphe $G$.

6.  **Conclusion :**
    Nous avons démontré que le Laplacien combinatoire $L(G)$ est une matrice symétrique et semi-définie positive. Sa forme quadratique $x^T L(G) x = \sum_{\{v_i, v_j\} \in E} (x_i - x_j)^2$ est toujours non négative. La valeur propre $0$ est la plus petite valeur propre de $L(G)$, et le vecteur $\mathbf{1}$ est un vecteur propre associé. Enfin, la multiplicité de la valeur propre $0$ est égale au nombre de composantes connexes du graphe $G$.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe
**Énoncé :**
Soit $G$ le graphe chemin $P_3$ avec $V = \{v_1, v_2, v_3\}$ et $E = \{\{v_1, v_2\}, \{v_2, v_3\}\}$.
1.  Construire la matrice d'adjacence $A(G)$ et la matrice de degrés $D(G)$.
2.  Calculer le Laplacien combinatoire $L(G)$.
3.  Déterminer les valeurs propres de $L(G)$ et leurs vecteurs propres associés.
4.  Vérifier la multiplicité de la valeur propre $0$ en relation avec le nombre de composantes connexes.

**Correction Détaillée :**
*   *Analyse de l'énoncé :* Le graphe $P_3$ est un petit graphe simple et connexe. Il a 3 sommets et 2 arêtes. Les degrés des sommets sont $\deg(v_1)=1$, $\deg(v_2)=2$, $\deg(v_3)=1$.

*   *Résolution pas-à-pas :*
    1.  **Construction de $A(G)$ et $D(G)$ :**
        Les arêtes sont $\{v_1, v_2\}$ et $\{v_2, v_3\}$.
        La matrice d'adjacence $A(G)$ est :
        $$A(G) = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$
        Les degrés des sommets sont $\deg(v_1)=1$, $\deg(v_2)=2$, $\deg(v_3)=1$.
        La matrice de degrés $D(G)$ est :
        $$D(G) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

    2.  **Calcul du Laplacien combinatoire $L(G)$ :**
        $$L(G) = D(G) - A(G)$$
        $$L(G) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} - \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}$$

    3.  **Détermination des valeurs propres et vecteurs propres de $L(G)$ :**
        Pour trouver les valeurs propres, nous devons résoudre l'équation caractéristique $\det(L(G) - \lambda I) = 0$.
        $$\det \begin{pmatrix} 1-\lambda & -1 & 0 \\ -1 & 2-\lambda & -1 \\ 0 & -1 & 1-\lambda \end{pmatrix} = 0$$
        Calculons le déterminant par la règle de Sarrus ou par cofacteurs :
        $$(1-\lambda)[(2-\lambda)(1-\lambda) - (-1)(-1)] - (-1)[(-1)(1-\lambda) - (0)(-1)] + 0[\dots] = 0$$
        $$(1-\lambda)[(2-3\lambda+\lambda^2) - 1] + [-(1-\lambda)] = 0$$
        $$(1-\lambda)[\lambda^2 - 3\lambda + 1] - (1-\lambda) = 0$$
        Factorisons $(1-\lambda)$ :
        $$(1-\lambda)[\lambda^2 - 3\lambda + 1 - 1] = 0$$
        $$(1-\lambda)[\lambda^2 - 3\lambda] = 0$$
        $$(1-\lambda)\lambda(\lambda - 3) = 0$$
        Les valeurs propres sont donc $\lambda_0 = 0$, $\lambda_1 = 1$, et $\lambda_2 = 3$.

        Maintenant, trouvons les vecteurs propres associés :
        *   **Pour $\lambda_0 = 0$ :**
            Nous résolvons $L x = 0 x$, c'est-à-dire $L x = \mathbf{0}$.
            $$\begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
            Cela donne le système d'équations :
            1.  $x_1 - x_2 = 0 \implies x_1 = x_2$
            2.  $-x_1 + 2x_2 - x_3 = 0$
            3.  $-x_2 + x_3 = 0 \implies x_2 = x_3$
            De (1) et (3), nous avons $x_1 = x_2 = x_3$.
            Substituons dans (2) : $-x_1 + 2x_1 - x_1 = 0 \implies 0 = 0$.
            Le vecteur propre est de la forme $(c, c, c)^T$. En choisissant $c=1$, nous obtenons le vecteur propre $u_0 = (1, 1, 1)^T$.

        *   **Pour $\lambda_1 = 1$ :**
            Nous résolvons $L x = 1 x$, c'est-à-dire $(L - I) x = \mathbf{0}$.
            $$\begin{pmatrix} 1-1 & -1 & 0 \\ -1 & 2-1 & -1 \\ 0 & -1 & 1-1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
            $$\begin{pmatrix} 0 & -1 & 0 \\ -1 & 1 & -1 \\ 0 & -1 & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
            Cela donne le système d'équations :
            1.  $-x_2 = 0 \implies x_2 = 0$
            2.  $-x_1 + x_2 - x_3 = 0$
            3.  $-x_2 = 0 \implies x_2 = 0$
            De (1) ou (3), $x_2 = 0$. Substituons dans (2) : $-x_1 + 0 - x_3 = 0 \implies x_1 = -x_3$.
            Le vecteur propre est de la forme $(c, 0, -c)^T$. En choisissant $c=1$, nous obtenons le vecteur propre $u_1 = (1, 0, -1)^T$.

        *   **Pour $\lambda_2 = 3$ :**
            Nous résolvons $L x = 3 x$, c'est-à-dire $(L - 3I) x = \mathbf{0}$.
            $$\begin{pmatrix} 1-3 & -1 & 0 \\ -1 & 2-3 & -1 \\ 0 & -1 & 1-3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
            $$\begin{pmatrix} -2 & -1 & 0 \\ -1 & -1 & -1 \\ 0 & -1 & -2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
            Cela donne le système d'équations :
            1.  $-2x_1 - x_2 = 0 \implies x_2 = -2x_1$
            2.  $-x_1 - x_2 - x_3 = 0$
            3.  $-x_2 - 2x_3 = 0 \implies x_2 = -2x_3$
            De (1) et (3), $-2x_1 = -2x_3 \implies x_1 = x_3$.
            Substituons $x_1 = x_3$ et $x_2 = -2x_1$ dans (2) :
            $-x_1 - (-2x_1) - x_1 = 0$
            $-x_1 + 2x_1 - x_1 = 0 \implies 0 = 0$.
            Le vecteur propre est de la forme $(c, -2c, c)^T$. En choisissant $c=1$, nous obtenons le vecteur propre $u_2 = (1, -2, 1)^T$.

    4.  **Vérification de la multiplicité de la valeur propre $0$ :**
        Le graphe $P_3$ est un graphe connexe. Il n'a qu'une seule composante connexe.
        D'après le Théorème 1, la multiplicité de la valeur propre $0$ doit être égale au nombre de composantes connexes.
        Nous avons trouvé que $\lambda_0 = 0$ est une valeur propre simple (sa multiplicité est 1).
        Ceci est cohérent avec le fait que $P_3$ est un graphe connexe (1 composante connexe).

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT)
**Énoncé :**
Soit $G=(V,E)$ un graphe non orienté simple, $d$-régulier, c'est-à-dire que chaque sommet $v \in V$ a un degré $\deg(v) = d$.
1.  Exprimer le Laplacien combinatoire $L(G)$ en fonction de la matrice d'adjacence $A(G)$ et de la matrice identité $I_n$.
2.  Soit $\mu$ une valeur propre de $A(G)$ et $x$ un vecteur propre associé. Montrer que $x$ est également un vecteur propre de $L(G)$ et déterminer la valeur propre de $L(G)$ associée à $x$.
3.  En utilisant le fait que les valeurs propres de $A(G)$ sont réelles et bornées par $[-d, d]$ (c'est-à-dire $-d \le \mu_i \le d$ pour toutes les valeurs propres $\mu_i$ de $A(G)$), déduire l'intervalle dans lequel se situent les valeurs propres de $L(G)$ pour un graphe $d$-régulier.

**Correction Détaillée :**
*   *Analyse de l'énoncé :* Un graphe $d$-régulier simplifie la matrice de degrés. Cela permet d'établir une relation directe entre les spectres de $A(G)$ et $L(G)$. La borne des valeurs propres de $A(G)$ est une propriété connue des matrices d'adjacence de graphes réguliers (le rayon spectral est $d$).

*   *Résolution pas-à-pas :*
    1.  **Expression de $L(G)$ pour un graphe $d$-régulier :**
        Puisque $G$ est $d$-régulier, le degré de chaque sommet est $d$.
        La matrice de degrés $D(G)$ est une matrice diagonale où tous les éléments diagonaux sont $d$.
        $$D(G) = \begin{pmatrix} d & 0 & \dots & 0 \\ 0 & d & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & d \end{pmatrix} = d I_n$$
        Par définition, le Laplacien combinatoire est $L(G) = D(G) - A(G)$.
        En substituant l'expression de $D(G)$ :
        $$L(G) = d I_n - A(G)$$

    2.  **Relation entre les vecteurs propres et valeurs propres de $A(G)$ et $L(G)$ :**
        Soit $\mu$ une valeur propre de $A(G)$ et $x$ un vecteur propre associé. Par définition, cela signifie que $A(G)x = \mu x$.
        Appliquons $L(G)$ au vecteur $x$ :
        $$L(G)x = (d I_n - A(G))x$$
        Par linéarité de la multiplication matricielle :
        $$L(G)x = d I_n x - A(G)x$$
        Puisque $I_n x = x$ et $A(G)x = \mu x$ :
        $$L(G)x = d x - \mu x$$
        Factorisons $x$ :
        $$L(G)x = (d - \mu) x$$
        Cette équation montre que $x$ est un vecteur propre de $L(G)$ et que la valeur propre associée est $(d - \mu)$.
        Donc, si $\mu_1, \mu_2, \dots, \mu_n$ sont les valeurs propres de $A(G)$, alors les valeurs propres de $L(G)$ sont $d-\mu_1, d-\mu_2, \dots, d-\mu_n$.

    3.  **Intervalle des valeurs propres de $L(G)$ pour un graphe $d$-régulier :**
        Nous savons que pour un graphe $d$-régulier, les valeurs propres de sa matrice d'adjacence $A(G)$ sont bornées par $[-d, d]$. C'est-à-dire, pour toute valeur propre $\mu_i$ de $A(G)$ :
        $$-d \le \mu_i \le d$$
        Nous voulons trouver l'intervalle pour les valeurs propres de $L(G)$, qui sont de la forme $d - \mu_i$.
        Multiplions l'inégalité par $-1$ et inversons les signes :
        $$-d \le -\mu_i \le d$$
        Maintenant, ajoutons $d$ à tous les membres de l'inégalité :
        $$d - d \le d - \mu_i \le d + d$$
        $$0 \le d - \mu_i \le 2d$$
        Donc, les valeurs propres de $L(G)$ pour un graphe $d$-régulier sont dans l'intervalle $[0, 2d]$.
        Ceci est cohérent avec le fait que $L(G)$ est semi-définie positive (toutes les valeurs propres sont $\ge 0$). La valeur propre maximale est $2d$, qui est atteinte lorsque $\mu_i = -d$. La valeur propre minimale est $0$, qui est atteinte lorsque $\mu_i = d$. Pour un graphe connexe $d$-régulier, la valeur propre $d$ est toujours présente pour $A(G)$ (avec le vecteur $\mathbf{1}$), ce qui correspond à la valeur propre $0$ pour $L(G)$.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** La théorie spectrale des graphes est une pierre angulaire pour de nombreuses applications en Intelligence Artificielle, en particulier celles qui traitent de données structurées sous forme de réseaux. Elle offre un cadre mathématique rigoureux pour transformer la topologie complexe d'un graphe en un ensemble de valeurs numériques (le spectre) et de vecteurs (les vecteurs propres) qui capturent des propriétés globales et locales du réseau. Ces propriétés sont ensuite exploitées pour des tâches d'apprentissage automatique. Le Laplacien, en particulier, agit comme un opérateur de "lissage" ou de "diffusion" sur le graphe, et ses valeurs propres et vecteurs propres décrivent les modes fondamentaux de cette diffusion. Cela permet de projeter les sommets du graphe dans un espace euclidien de faible dimension (embedding spectral), où les relations structurelles sont préservées, facilitant ainsi l'application d'algorithmes d'apprentissage traditionnels.
- **Exemple Concret :**
    *   **Clustering Spectral :** C'est l'une des applications les plus emblématiques. L'objectif est de partitionner les sommets d'un graphe en groupes (clusters) de manière à ce que les sommets au sein d'un même groupe soient fortement connectés, et les groupes entre eux faiblement connectés. Le problème du Normalized Cut (Ncut) est NP-difficile. Cependant, le Théorème 2 montre que la minimisation du Ncut peut être relaxée en un problème de minimisation du quotient de Rayleigh, dont la solution est donnée par les vecteurs propres du Laplacien normalisé symétrique.
        **Calcul précis :**
        1.  **Construction du graphe de similarité :** Étant donné un ensemble de $n$ points de données $x_1, \dots, x_n \in \mathbb{R}^d$, on construit un graphe $G=(V,E)$ où chaque point $x_i$ est un sommet $v_i$. Les arêtes sont pondérées par une fonction de similarité, par exemple, la similarité gaussienne : $w_{ij} = \exp(-\|x_i - x_j\|^2 / (2\sigma^2))$.
        2.  **Calcul du Laplacien normalisé :** On calcule la matrice de degrés $D$ (où $D_{ii} = \sum_j w_{ij}$) et la matrice de poids $W$ (où $W_{ij} = w_{ij}$). On forme ensuite le Laplacien normalisé symétrique $\mathcal{L}_{sym} = I - D^{-1/2} W D^{-1/2}$.
        3.  **Calcul des vecteurs propres :** On calcule les $k$ plus petits vecteurs propres non nuls de $\mathcal{L}_{sym}$ (où $k$ est le nombre de clusters souhaité). Soient $u_1, \dots, u_k$ ces vecteurs propres.
        4.  **Embedding spectral :** On forme une matrice $U \in \mathbb{R}^{n \times k}$ en empilant ces $k$ vecteurs propres en colonnes. Chaque ligne de $U$ (par exemple, $U_i = (u_{1,i}, u_{2,i}, \dots, u_{k,i})$) représente un nouveau point de données pour le sommet $v_i$ dans un espace de dimension $k$.
        5.  **Clustering :** On applique un algorithme de clustering standard (comme K-means) sur les $n$ points $U_1, \dots, U_n$ dans l'espace de dimension $k$. Les clusters obtenus dans cet espace correspondent aux partitions du graphe original.
        Ce processus permet de segmenter des images, de détecter des communautés dans des réseaux sociaux, ou de regrouper des documents basés sur leur similarité sémantique, en exploitant les propriétés intrinsèques de la structure du graphe.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 042 (Algèbre linéaire avancée)]], [[Jalon 071 (Théorie des graphes - Fondamentaux)]], [[Jalon 098 (Optimisation - Méthodes numériques)]]
- **Concepts Futurs dépendants :** [[Jalon 144 (Le phénomène de double descente)]], [[Jalon 145 (Clustering spectral)]], [[Jalon 146 (Graph Neural Networks - Fondations)]], [[Jalon 147 (Réduction de dimension - Isomap, LLE)]], [[Jalon 148 (Analyse de réseaux complexes)]]
