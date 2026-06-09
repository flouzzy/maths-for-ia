```yaml
uuid: exercise-7-spectral-graph-theory-min-cut
title: "Exercice 7 : Relaxation Spectrale du Problème de Coupure Normalisée"
```
# Exercice 7 : Relaxation Spectrale du Problème de Coupure Normalisée

**Contexte :** Le problème de la coupure normalisée (Normalized Cut, NCut) est un problème fondamental en partitionnement de graphes, notamment en vision par ordinateur et en apprentissage automatique. Il vise à trouver une partition d'un graphe en deux sous-ensembles de sommets de telle sorte que la "force" de la coupure entre eux soit minimisée, tout en tenant compte des volumes des sous-ensembles. Ce problème est NP-difficile. Les méthodes spectrales offrent une relaxation continue qui permet d'obtenir des solutions approximatives efficaces.

Soit $G=(V,E)$ un graphe non orienté, connexe, avec $n=|V|$ sommets et $m=|E|$ arêtes. On suppose que le graphe est pondéré par des poids $w_{uv} \ge 0$ pour chaque arête $(u,v) \in E$. Pour simplifier, nous prendrons $w_{uv}=1$ pour toutes les arêtes.
Soit $d_u = \sum_{v \in N(u)} w_{uv}$ le degré du sommet $u$. La matrice des degrés $D$ est une matrice diagonale où $D_{uu} = d_u$. La matrice d'adjacence est $A_{adj}$.
Le Laplacien combinatoire est $L = D - A_{adj}$.
Le Laplacien normalisé symétrique est $L_{sym} = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A_{adj} D^{-1/2}$.

---

**Partie 1 : Définition de la Coupure Normalisée (NCut)**

Pour une partition $(A, \bar{A})$ des sommets $V$ (où $A \neq \emptyset$ et $\bar{A} \neq \emptyset$), la valeur de la coupure est définie par :
$$ \text{cut}(A, \bar{A}) = \sum_{u \in A, v \in \bar{A}} w_{uv} $$
Le volume d'un sous-ensemble $A \subset V$ est défini par :
$$ \text{vol}(A) = \sum_{u \in A} d_u $$
Le problème de la coupure normalisée consiste à trouver une partition $(A, \bar{A})$ qui minimise la fonction objectif :
$$ \text{NCut}(A, \bar{A}) = \frac{\text{cut}(A, \bar{A})}{\text{vol}(A)} + \frac{\text{cut}(A, \bar{A})}{\text{vol}(\bar{A})} $$

---

**Partie 2 : Formulation du NCut en Termes de Vecteurs**

Pour une partition $(A, \bar{A})$ de $V$, nous définissons un vecteur $y \in \mathbb{R}^n$ de la manière suivante :
$$ y_i = \begin{cases} \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} & \text{si } i \in A \\ -\sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} & \text{si } i \in \bar{A} \end{cases} $$

1.  Montrer que $y^T D y = \text{vol}(V)$ et $y^T D \mathbf{1} = 0$, où $\mathbf{1}$ est le vecteur de tous les uns.
2.  Montrer que la forme quadratique du Laplacien combinatoire $y^T L y$ peut s'écrire comme :
    $$ y^T L y = \text{cut}(A, \bar{A}) \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} \right)^2 $$
3.  En utilisant les résultats précédents, démontrer que :
    $$ \frac{y^T L y}{y^T D y} = \text{NCut}(A, \bar{A}) $$
    Ce résultat établit un lien direct entre le problème de la coupure normalisée et un quotient de Rayleigh généralisé.

---

**Partie 3 : Relaxation Spectrale et Vecteur de Fiedler Normalisé**

Le problème de minimisation de $\text{NCut}(A, \bar{A})$ sur toutes les partitions binaires est NP-difficile. Une approche courante est de relaxer le problème en permettant au vecteur $y$ d'être un vecteur réel arbitraire.

4.  Considérer le problème de minimisation relaxé :
    $$ \min_{y \in \mathbb{R}^n, y \neq \mathbf{0}, y^T D \mathbf{1} = 0} \frac{y^T L y}{y^T D y} $$
    Montrer que ce problème de minimisation est équivalent à trouver la deuxième plus petite valeur propre $\lambda_2$ du Laplacien normalisé symétrique $L_{sym}$. Préciser la relation entre le vecteur $y$ optimal et le vecteur propre $x_2$ de $L_{sym}$ correspondant à $\lambda_2$.
    *(Indice : Utiliser la transformation $x = D^{1/2} y$ et les propriétés du quotient de Rayleigh.)*
5.  Expliquer comment le vecteur propre $x_2$ (souvent appelé le "vecteur de Fiedler normalisé") correspondant à $\lambda_2(L_{sym})$ peut être utilisé pour obtenir une partition binaire $(A, \bar{A})$ approximative du graphe. Discuter brièvement des méthodes de seuillage courantes pour cette conversion.

---

# Correction Détaillée

---

**Partie 1 : Définition de la Coupure Normalisée (NCut)**

Les définitions sont fournies dans l'énoncé.

---

**Partie 2 : Formulation du NCut en Termes de Vecteurs**

Nous avons défini le vecteur $y \in \mathbb{R}^n$ pour une partition $(A, \bar{A})$ comme suit :
$$ y_i = \begin{cases} \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} & \text{si } i \in A \\ -\sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} & \text{si } i \in \bar{A} \end{cases} $$

1.  **Démonstration de $y^T D y = \text{vol}(V)$ et $y^T D \mathbf{1} = 0$ :**

    *   Calcul de $y^T D y$ :
        $$ y^T D y = \sum_{i \in V} d_i y_i^2 $$
        En substituant les valeurs de $y_i$ :
        $$ y^T D y = \sum_{i \in A} d_i \left(\sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}}\right)^2 + \sum_{i \in \bar{A}} d_i \left(-\sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}}\right)^2 $$
        $$ y^T D y = \sum_{i \in A} d_i \frac{\text{vol}(\bar{A})}{\text{vol}(A)} + \sum_{i \in \bar{A}} d_i \frac{\text{vol}(A)}{\text{vol}(\bar{A})} $$
        Puisque $\sum_{i \in A} d_i = \text{vol}(A)$ et $\sum_{i \in \bar{A}} d_i = \text{vol}(\bar{A})$ :
        $$ y^T D y = \text{vol}(A) \frac{\text{vol}(\bar{A})}{\text{vol}(A)} + \text{vol}(\bar{A}) \frac{\text{vol}(A)}{\text{vol}(\bar{A})} $$
        $$ y^T D y = \text{vol}(\bar{A}) + \text{vol}(A) = \text{vol}(V) $$

    *   Calcul de $y^T D \mathbf{1}$ :
        $$ y^T D \mathbf{1} = \sum_{i \in V} d_i y_i $$
        En substituant les valeurs de $y_i$ :
        $$ y^T D \mathbf{1} = \sum_{i \in A} d_i \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sum_{i \in \bar{A}} d_i \left(-\sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}}\right) $$
        $$ y^T D \mathbf{1} = \text{vol}(A) \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} - \text{vol}(\bar{A}) \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} $$
        $$ y^T D \mathbf{1} = \sqrt{\text{vol}(A)\text{vol}(\bar{A})} - \sqrt{\text{vol}(\bar{A})\text{vol}(A)} = 0 $$

2.  **Démonstration de $y^T L y = \text{cut}(A, \bar{A}) \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} \right)^2$ :**

    La forme quadratique du Laplacien combinatoire est donnée par :
    $$ y^T L y = \sum_{(u,v) \in E} w_{uv} (y_u - y_v)^2 $$
    Considérons les différents cas pour les arêtes $(u,v)$ :
    *   Si $u,v \in A$ : $y_u = y_v = \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}}$, donc $(y_u - y_v)^2 = 0$.
    *   Si $u,v \in \bar{A}$ : $y_u = y_v = -\sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}}$, donc $(y_u - y_v)^2 = 0$.
    *   Si $u \in A$ et $v \in \bar{A}$ (ou vice versa) :
        $$ (y_u - y_v)^2 = \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} - \left(-\sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}}\right) \right)^2 $$
        $$ (y_u - y_v)^2 = \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} \right)^2 $$
    En sommant sur toutes les arêtes :
    $$ y^T L y = \sum_{u \in A, v \in \bar{A}} w_{uv} \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} \right)^2 $$
    Par définition, $\sum_{u \in A, v \in \bar{A}} w_{uv} = \text{cut}(A, \bar{A})$. Donc :
    $$ y^T L y = \text{cut}(A, \bar{A}) \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} \right)^2 $$

3.  **Démonstration de $\frac{y^T L y}{y^T D y} = \text{NCut}(A, \bar{A})$ :**

    Nous avons $y^T D y = \text{vol}(V)$.
    Nous avons $y^T L y = \text{cut}(A, \bar{A}) \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} \right)^2$.
    Simplifions le terme entre parenthèses :
    $$ \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} = \frac{\sqrt{\text{vol}(\bar{A})^2} + \sqrt{\text{vol}(A)^2}}{\sqrt{\text{vol}(A)\text{vol}(\bar{A})}} = \frac{\text{vol}(\bar{A}) + \text{vol}(A)}{\sqrt{\text{vol}(A)\text{vol}(\bar{A})}} = \frac{\text{vol}(V)}{\sqrt{\text{vol}(A)\text{vol}(\bar{A})}} $$
    En élevant au carré :
    $$ \left( \sqrt{\frac{\text{vol}(\bar{A})}{\text{vol}(A)}} + \sqrt{\frac{\text{vol}(A)}{\text{vol}(\bar{A})}} \right)^2 = \frac{\text{vol}(V)^2}{\text{vol}(A)\text{vol}(\bar{A})} $$
    Maintenant, substituons cela dans l'expression de $y^T L y$ :
    $$ y^T L y = \text{cut}(A, \bar{A}) \frac{\text{vol}(V)^2}{\text{vol}(A)\text{vol}(\bar{A})} $$
    Enfin, calculons le quotient :
    $$ \frac{y^T L y}{y^T D y} = \frac{\text{cut}(A, \bar{A}) \frac{\text{vol}(V)^2}{\text{vol}(A)\text{vol}(\bar{A})}}{\text{vol}(V)} = \text{cut}(A, \bar{A}) \frac{\text{vol}(V)}{\text{vol}(A)\text{vol}(\bar{A})} $$
    D'autre part, la définition de $\text{NCut}(A, \bar{A})$ est :
    $$ \text{NCut}(A, \bar{A}) = \frac{\text{cut}(A, \bar{A})}{\text{vol}(A)} + \frac{\text{cut}(A, \bar{A})}{\text{vol}(\bar{A})} = \text{cut}(A, \bar{A}) \left( \frac{1}{\text{vol}(A)} + \frac{1}{\text{vol}(\bar{A})} \right) $$
    $$ \text{NCut}(A, \bar{A}) = \text{cut}(A, \bar{A}) \left( \frac{\text{vol}(\bar{A}) + \text{vol}(A)}{\text{vol}(A)\text{vol}(\bar{A})} \right) = \text{cut}(A, \bar{A}) \frac{\text{vol}(V)}{\text{vol}(A)\text{vol}(\bar{A})} $$
    Les deux expressions sont identiques. Par conséquent :
    $$ \frac{y^T L y}{y^T D y} = \text{NCut}(A, \bar{A}) $$

---

**Partie 3 : Relaxation Spectrale et Vecteur de Fiedler Normalisé**

4.  **Équivalence avec la deuxième plus petite valeur propre de $L_{sym}$ :**

    Le problème de minimisation relaxé est :
    $$ \min_{y \in \mathbb{R}^n, y \neq \mathbf{0}, y^T D \mathbf{1} = 0} \frac{y^T L y}{y^T D y} $$
    Introduisons la transformation $x = D^{1/2} y$. Puisque $D$ est une matrice diagonale avec des éléments positifs (les degrés), $D^{1/2}$ est bien définie et inversible. Donc $y = D^{-1/2} x$.
    Substituons $y$ dans le numérateur :
    $$ y^T L y = (D^{-1/2} x)^T L (D^{-1/2} x) = x^T D^{-1/2} L D^{-1/2} x = x^T L_{sym} x $$
    Substituons $y$ dans le dénominateur :
    $$ y^T D y = (D^{-1/2} x)^T D (D^{-1/2} x) = x^T D^{-1/2} D D^{-1/2} x = x^T I x = x^T x $$
    La contrainte $y^T D \mathbf{1} = 0$ devient :
    $$ (D^{-1/2} x)^T D \mathbf{1} = x^T D^{-1/2} D \mathbf{1} = x^T D^{1/2} \mathbf{1} = 0 $$
    Soit $\mathbf{1}_D = D^{1/2} \mathbf{1}$. Ce vecteur a pour composantes $(\sqrt{d_1}, \sqrt{d_2}, \ldots, \sqrt{d_n})^T$.
    Le problème de minimisation transformé est donc :
    $$ \min_{x \in \mathbb{R}^n, x \neq \mathbf{0}, x^T \mathbf{1}_D = 0} \frac{x^T L_{sym} x}{x^T x} $$
    Ceci est le quotient de Rayleigh pour la matrice $L_{sym}$.
    Nous savons que $L_{sym}$ est une matrice symétrique semi-définie positive. Ses valeurs propres sont réelles et non négatives, et peuvent être ordonnées comme $0 = \lambda_1 \le \lambda_2 \le \ldots \le \lambda_n$.
    Le plus petit valeur propre $\lambda_1 = 0$ correspond au vecteur propre $x_1 = D^{1/2} \mathbf{1}$ (car $L_{sym} D^{1/2} \mathbf{1} = D^{-1/2} L \mathbf{1} = D^{-1/2} \mathbf{0} = \mathbf{0}$).
    La contrainte $x^T \mathbf{1}_D = 0$ signifie que le vecteur $x$ doit être orthogonal au vecteur propre $x_1 = \mathbf{1}_D$ correspondant à $\lambda_1$.
    Selon le théorème de Courant-Fischer (ou les propriétés du quotient de Rayleigh), le minimum du quotient de Rayleigh pour une matrice symétrique, restreint aux vecteurs orthogonaux au premier vecteur propre, est la deuxième plus petite valeur propre.
    Par conséquent, la valeur minimale du problème relaxé est $\lambda_2(L_{sym})$.
    Le vecteur $y$ optimal pour le problème relaxé est $y_2 = D^{-1/2} x_2$, où $x_2$ est le vecteur propre de $L_{sym}$ correspondant à $\lambda_2$.

5.  **Utilisation du vecteur de Fiedler normalisé pour la partition binaire :**

    Le vecteur propre $x_2$ de $L_{sym}$ (le vecteur de Fiedler normalisé) est un vecteur réel à $n$ dimensions. Ses composantes $x_{2,i}$ peuvent être interprétées comme des "coordonnées" des sommets dans un espace continu, où les sommets ayant des valeurs similaires sont fortement connectés.
    Pour obtenir une partition binaire $(A, \bar{A})$ à partir de ce vecteur continu, on utilise une technique de *seuillage* (thresholding). L'idée est de choisir une valeur seuil $t$ et de partitionner les sommets en fonction de cette valeur :
    $$ A = \{i \in V \mid x_{2,i} \ge t\} $$
    $$ \bar{A} = \{i \in V \mid x_{2,i} < t\} $$
    Le choix du seuil $t$ est crucial et peut influencer la qualité de la partition. Plusieurs stratégies existent :
    *   **Seuil à zéro :** Si le vecteur $x_2$ a des composantes positives et négatives, un seuil $t=0$ est souvent utilisé. Cela sépare les sommets en deux groupes en fonction du signe de leur composante dans $x_2$.
    *   **Seuil à la médiane :** Choisir $t$ comme la médiane des valeurs de $x_2$ peut aider à obtenir des partitions plus équilibrées en termes de nombre de sommets.
    *   **Seuil optimal :** Une approche plus sophistiquée consiste à tester tous les $n$ seuils possibles (c'est-à-dire, prendre chaque valeur $x_{2,i}$ comme seuil potentiel) et à choisir celui qui minimise la valeur réelle de $\text{NCut}(A, \bar{A})$ pour la partition binaire résultante. Cette méthode garantit de trouver la meilleure partition binaire que l'on puisse obtenir en seuillant le vecteur $x_2$.
    *   **Méthodes itératives :** Des algorithmes plus complexes peuvent affiner la partition obtenue par seuillage, par exemple en utilisant des techniques de k-means sur les composantes du vecteur de Fiedler ou en effectuant des ajustements locaux.

    La qualité de cette approximation spectrale est souvent justifiée par des inégalités de type Cheeger, qui relient la valeur de $\lambda_2$ à la "conductance" du graphe, une mesure de sa connectivité qui est étroitement liée aux coupures optimales. Le vecteur de Fiedler normalisé fournit ainsi une heuristique puissante pour le partitionnement de graphes.

---
