Mes chers étudiants,

Aujourd'hui, nous allons approfondir notre compréhension des concepts fondamentaux de la théorie de l'information appliqués aux modèles de langage. La capacité d'un modèle à prédire la prochaine unité lexicale est au cœur de son utilité, et l'évaluation de cette capacité repose sur des mesures rigoureuses. Nous nous concentrerons sur l'Entropie de Shannon, l'Entropie Croisée et la Divergence de Kullback-Leibler, des outils indispensables pour quantifier l'incertitude et la qualité des prédictions.

Niveau de difficulté : $\bigstar\star\star\star\star$

Considérons un modèle de langage simplifié dont la tâche est de prédire le mot suivant après la séquence "Le chat". Pour simplifier notre exercice, notre vocabulaire est limité à trois mots : $\mathcal{V} = \{ \text{mange}, \text{court}, \text{dort} \}$.

Nous disposons de la distribution de probabilité réelle, $P(x)$, qui reflète la fréquence avec laquelle chaque mot apparaît dans un très grand corpus après "Le chat" :
*   $P(\text{mange}) = 0.6$
*   $P(\text{court}) = 0.3$
*   $P(\text{dort}) = 0.1$

Notre premier modèle de langage, que nous nommerons $M_1$, produit la distribution de probabilité prédite $Q_1(x)$ pour le mot suivant :
*   $Q_1(\text{mange}) = 0.4$
*   $Q_1(\text{court}) = 0.4$
*   $Q_1(\text{dort}) = 0.2$

Toutes les probabilités sont bien sûr positives et leur somme est égale à 1. Dans cet exercice, nous utiliserons le logarithme en base 2, et nous arrondirons les valeurs des logarithmes à trois décimales si nécessaire pour les calculs intermédiaires.

---

**Partie A : Entropie de Shannon**

L'Entropie de Shannon, $H(P)$, mesure l'incertitude intrinsèque d'une distribution de probabilité $P$. Elle quantifie le nombre minimal de bits en moyenne nécessaire pour encoder un événement tiré de cette distribution. Sa formule est donnée par :
$$ H(P) = -\sum_{x \in \mathcal{V}} P(x) \log_2 P(x) $$

1.  Calculez l'Entropie de Shannon pour la distribution réelle $P$.
2.  Interprétez la valeur obtenue dans le contexte de notre modèle de langage.

---

**Partie B : Entropie Croisée (Cross-Entropy)**

L'Entropie Croisée, $H(P, Q)$, est une mesure de la quantité moyenne de bits nécessaires pour identifier un événement à partir de la distribution réelle $P$, si nous utilisons un modèle de codage optimisé pour la distribution prédite $Q$. C'est une métrique cruciale pour évaluer la performance d'un modèle de langage. Sa formule est donnée par :
$$ H(P, Q) = -\sum_{x \in \mathcal{V}} P(x) \log_2 Q(x) $$

1.  Calculez l'Entropie Croisée entre la distribution réelle $P$ et la distribution prédite par notre premier modèle $Q_1$.
2.  Interprétez le résultat : que signifie cette valeur pour la performance du modèle $M_1$ ?

---

**Partie C : Divergence de Kullback-Leibler (KL Divergence)**

La Divergence de Kullback-Leibler, $D_{KL}(P || Q)$, quantifie la perte d'information lorsque la distribution $Q$ est utilisée pour approximer la distribution réelle $P$. Elle mesure les "bits supplémentaires" nécessaires pour encoder des événements provenant de $P$ si nous utilisons $Q$ au lieu de $P$. Sa formule est :
$$ D_{KL}(P || Q) = \sum_{x \in \mathcal{V}} P(x) \log_2 \left( \frac{P(x)}{Q(x)} \right) $$
Il existe également une relation fondamentale entre les trois mesures : $D_{KL}(P || Q) = H(P, Q) - H(P)$.

1.  Calculez la Divergence de Kullback-Leibler entre $P$ et $Q_1$. Vous pouvez utiliser l'une des deux formules proposées.
2.  Interprétez cette valeur. Que nous indique-t-elle sur la différence entre la prédiction de $M_1$ et la réalité ?
3.  Vérifiez que la relation $D_{KL}(P || Q) = H(P, Q) - H(P)$ est satisfaite avec vos résultats précédents.

---

**Partie D : Amélioration du Modèle**

Suite à un processus d'entraînement intensif, notre modèle de langage est amélioré. Le nouveau modèle, $M_2$, produit la distribution de probabilité prédite $Q_2(x)$ :
*   $Q_2(\text{mange}) = 0.55$
*   $Q_2(\text{court}) = 0.35$
*   $Q_2(\text{dort}) = 0.10$

1.  Calculez l'Entropie Croisée entre la distribution réelle $P$ et la nouvelle distribution prédite $Q_2$.
2.  Calculez la Divergence de Kullback-Leibler entre $P$ et $Q_2$.
3.  Comparez les valeurs d'Entropie Croisée et de Divergence KL obtenues pour $M_1$ et $M_2$. Quelles conclusions générales pouvez-vous tirer quant à l'amélioration du modèle et l'objectif de l'entraînement des modèles de langage ?

---

## Corrigé de l'Exercice

Nous allons détailler chaque étape des calculs et fournir des interprétations précises pour chaque mesure. Nous utiliserons les logarithmes en base 2 et les arrondirons à trois décimales pour les calculs intermédiaires.

**Valeurs des Logarithmes en base 2 nécessaires (arrondies à 3 décimales) :**
*   $\log_2 0.1 \approx -3.322$
*   $\log_2 0.2 \approx -2.322$
*   $\log_2 0.3 \approx -1.737$
*   $\log_2 0.35 \approx -1.515$
*   $\log_2 0.4 \approx -1.322$
*   $\log_2 0.5 \approx -1.000$ (valeur exacte)
*   $\log_2 0.55 \approx -0.860$
*   $\log_2 0.6 \approx -0.737$
*   $\log_2 0.75 \approx -0.415$
*   $\log_2 1.5 \approx 0.585$

---

**Partie A : Entropie de Shannon**

1.  **Calcul de l'Entropie de Shannon pour $P$ :**
    La formule est $H(P) = -\sum_{x \in \mathcal{V}} P(x) \log_2 P(x)$.
    Pour la distribution réelle $P(x)$ :
    *   $P(\text{mange}) = 0.6$
    *   $P(\text{court}) = 0.3$
    *   $P(\text{dort}) = 0.1$

    Calculons chaque terme :
    *   $P(\text{mange}) \log_2 P(\text{mange}) = 0.6 \times \log_2 0.6 \approx 0.6 \times (-0.737) = -0.4422$
    *   $P(\text{court}) \log_2 P(\text{court}) = 0.3 \times \log_2 0.3 \approx 0.3 \times (-1.737) = -0.5211$
    *   $P(\text{dort}) \log_2 P(\text{dort}) = 0.1 \times \log_2 0.1 \approx 0.1 \times (-3.322) = -0.3322$

    En sommant ces termes :
    $$ \sum_{x \in \mathcal{V}} P(x) \log_2 P(x) \approx -0.4422 - 0.5211 - 0.3322 = -1.2955 $$
    Donc, l'Entropie de Shannon est :
    $$ H(P) = -(-1.2955) = 1.2955 \text{ bits} $$

2.  **Interprétation de l'Entropie de Shannon :**
    La valeur $H(P) \approx 1.2955$ bits représente l'incertitude intrinsèque associée à la prédiction du mot suivant "Le chat" dans le monde réel, selon notre corpus de référence. C'est le nombre minimal moyen de bits qui serait nécessaire pour encoder le mot suivant si nous utilisions le code le plus efficace possible, basé sur la vraie distribution $P$. Une valeur plus élevée indiquerait une plus grande incertitude (des probabilités plus uniformes), tandis qu'une valeur plus faible (proche de 0) indiquerait que le mot suivant est très prévisible (une probabilité proche de 1 pour un mot en particulier).

---

**Partie B : Entropie Croisée (Cross-Entropy)**

1.  **Calcul de l'Entropie Croisée entre $P$ et $Q_1$ :**
    La formule est $H(P, Q) = -\sum_{x \in \mathcal{V}} P(x) \log_2 Q(x)$.
    Nous utilisons $P$ (réelle) et $Q_1$ (prédite par $M_1$) :
    *   $P(\text{mange}) = 0.6$, $Q_1(\text{mange}) = 0.4$
    *   $P(\text{court}) = 0.3$, $Q_1(\text{court}) = 0.4$
    *   $P(\text{dort}) = 0.1$, $Q_1(\text{dort}) = 0.2$

    Calculons chaque terme :
    *   $P(\text{mange}) \log_2 Q_1(\text{mange}) = 0.6 \times \log_2 0.4 \approx 0.6 \times (-1.322) = -0.7932$
    *   $P(\text{court}) \log_2 Q_1(\text{court}) = 0.3 \times \log_2 0.4 \approx 0.3 \times (-1.322) = -0.3966$
    *   $P(\text{dort}) \log_2 Q_1(\text{dort}) = 0.1 \times \log_2 0.2 \approx 0.1 \times (-2.322) = -0.2322$

    En sommant ces termes :
    $$ \sum_{x \in \mathcal{V}} P(x) \log_2 Q_1(x) \approx -0.7932 - 0.3966 - 0.2322 = -1.4220 $$
    Donc, l'Entropie Croisée est :
    $$ H(P, Q_1) = -(-1.4220) = 1.4220 \text{ bits} $$

2.  **Interprétation de l'Entropie Croisée :**
    La valeur $H(P, Q_1) \approx 1.4220$ bits représente le nombre moyen de bits nécessaires pour encoder le mot suivant "Le chat" si nous utilisons le schéma de codage optimal basé sur la distribution prédite par $M_1$ ($Q_1$), alors que les événements proviennent réellement de la distribution $P$. En d'autres termes, c'est une mesure de la "surprise" moyenne ou de l'inefficacité de $Q_1$ par rapport à $P$. Pour un modèle de langage, une Entropie Croisée plus faible indique une meilleure adéquation entre les prédictions du modèle et la réalité. Ici, 1.4220 bits est l'effort moyen pour coder l'information quand on s'appuie sur la distribution erronée $Q_1$.

---

**Partie C : Divergence de Kullback-Leibler (KL Divergence)**

1.  **Calcul de la Divergence KL entre $P$ et $Q_1$ :**
    Nous pouvons utiliser la relation $D_{KL}(P || Q_1) = H(P, Q_1) - H(P)$.
    Avec nos valeurs calculées précédemment :
    $$ D_{KL}(P || Q_1) \approx 1.4220 - 1.2955 = 0.1265 \text{ bits} $$

    Alternativement, par la formule directe $D_{KL}(P || Q) = \sum_{x \in \mathcal{V}} P(x) \log_2 \left( \frac{P(x)}{Q(x)} \right)$ :
    *   Pour "mange" : $P(\text{mange}) \log_2 \left( \frac{P(\text{mange})}{Q_1(\text{mange})} \right) = 0.6 \log_2 \left( \frac{0.6}{0.4} \right) = 0.6 \log_2 (1.5) \approx 0.6 \times 0.585 = 0.3510$
    *   Pour "court" : $P(\text{court}) \log_2 \left( \frac{P(\text{court})}{Q_1(\text{court})} \right) = 0.3 \log_2 \left( \frac{0.3}{0.4} \right) = 0.3 \log_2 (0.75) \approx 0.3 \times (-0.415) = -0.1245$
    *   Pour "dort" : $P(\text{dort}) \log_2 \left( \frac{P(\text{dort})}{Q_1(\text{dort})} \right) = 0.1 \log_2 \left( \frac{0.1}{0.2} \right) = 0.1 \log_2 (0.5) \approx 0.1 \times (-1.000) = -0.1000$

    En sommant ces termes :
    $$ D_{KL}(P || Q_1) \approx 0.3510 - 0.1245 - 0.1000 = 0.1265 \text{ bits} $$
    Les deux méthodes donnent des résultats identiques, ce qui est une excellente vérification de nos calculs.

2.  **Interprétation de la Divergence KL :**
    La valeur $D_{KL}(P || Q_1) \approx 0.1265$ bits représente la quantité d'information perdue (ou l'inefficacité) lorsque nous utilisons la distribution $Q_1$ du modèle $M_1$ pour approximer la distribution réelle $P$. C'est le nombre de bits supplémentaires en moyenne que nous devons dépenser pour coder le mot suivant si nous utilisons $Q_1$ au lieu de la distribution optimale $P$. Une divergence KL de 0 signifierait que $Q_1$ est identique à $P$. Plus la valeur est grande, plus la différence entre les deux distributions est importante.

3.  **Vérification de la relation :**
    Nous avons calculé :
    *   $H(P) = 1.2955$ bits
    *   $H(P, Q_1) = 1.4220$ bits
    *   $D_{KL}(P || Q_1) = 0.1265$ bits

    La relation $D_{KL}(P || Q_1) = H(P, Q_1) - H(P)$ donne :
    $$ 0.1265 \approx 1.4220 - 1.2955 $$
    $$ 0.1265 \approx 0.1265 $$
    La relation est parfaitement satisfaite, confirmant la cohérence de nos calculs et la compréhension des liens entre ces trois mesures fondamentales.

---

**Partie D : Amélioration du Modèle**

1.  **Calcul de l'Entropie Croisée entre $P$ et $Q_2$ :**
    Nous utilisons $P$ (réelle) et $Q_2$ (prédite par $M_2$) :
    *   $P(\text{mange}) = 0.6$, $Q_2(\text{mange}) = 0.55$
    *   $P(\text{court}) = 0.3$, $Q_2(\text{court}) = 0.35$
    *   $P(\text{dort}) = 0.1$, $Q_2(\text{dort}) = 0.10$

    Calculons chaque terme de $H(P, Q_2) = -\sum_{x \in \mathcal{V}} P(x) \log_2 Q_2(x)$ :
    *   $P(\text{mange}) \log_2 Q_2(\text{mange}) = 0.6 \times \log_2 0.55 \approx 0.6 \times (-0.860) = -0.5160$
    *   $P(\text{court}) \log_2 Q_2(\text{court}) = 0.3 \times \log_2 0.35 \approx 0.3 \times (-1.515) = -0.4545$
    *   $P(\text{dort}) \log_2 Q_2(\text{dort}) = 0.1 \times \log_2 0.10 \approx 0.1 \times (-3.322) = -0.3322$

    En sommant ces termes :
    $$ \sum_{x \in \mathcal{V}} P(x) \log_2 Q_2(x) \approx -0.5160 - 0.4545 - 0.3322 = -1.3027 $$
    Donc, l'Entropie Croisée est :
    $$ H(P, Q_2) = -(-1.3027) = 1.3027 \text{ bits} $$

2.  **Calcul de la Divergence KL entre $P$ et $Q_2$ :**
    Nous utilisons la relation $D_{KL}(P || Q_2) = H(P, Q_2) - H(P)$.
    Avec $H(P) = 1.2955$ bits (calculé en Partie A) et $H(P, Q_2) = 1.3027$ bits :
    $$ D_{KL}(P || Q_2) \approx 1.3027 - 1.2955 = 0.0072 \text{ bits} $$

3.  **Comparaison et conclusions générales :**
    Comparons les résultats des deux modèles :
    *   **Modèle $M_1$ :**
        *   Entropie Croisée $H(P, Q_1) \approx 1.4220$ bits
        *   Divergence KL $D_{KL}(P || Q_1) \approx 0.1265$ bits
    *   **Modèle $M_2$ :**
        *   Entropie Croisée $H(P, Q_2) \approx 1.3027$ bits
        *   Divergence KL $D_{KL}(P || Q_2) \approx 0.0072$ bits

    Nous observons que l'Entropie Croisée pour $M_2$ (1.3027 bits) est significativement plus faible que celle de $M_1$ (1.4220 bits). Cela indique que le modèle $M_2$ prédit des distributions de probabilité qui sont plus proches de la distribution réelle $P$. L'Entropie Croisée est une mesure directe de la qualité du modèle en termes d'efficacité de codage : plus elle est proche de l'Entropie de Shannon réelle $H(P)$ (qui est la borne inférieure), meilleur est le modèle. Ici, $H(P, Q_2)$ est beaucoup plus proche de $H(P) = 1.2955$ que ne l'était $H(P, Q_1)$.

    De même, la Divergence KL pour $M_2$ (0.0072 bits) est bien plus faible que pour $M_1$ (0.1265 bits). Une Divergence KL plus proche de zéro signifie que la distribution prédite par $M_2$ est beaucoup plus similaire à la distribution réelle $P$ que ne l'était celle de $M_1$. En d'autres termes, la perte d'information en utilisant $Q_2$ au lieu de $P$ est minime, ce qui démontre que $M_2$ est un modèle bien plus précis et fiable.

    En conclusion, l'entraînement d'un modèle de langage vise précisément à minimiser l'Entropie Croisée (ou, de manière équivalente, la Divergence KL) entre la distribution de probabilités prédite par le modèle et la distribution de probabilités réelle des données d'entraînement. Une Entropie Croisée et une Divergence KL plus faibles sont des indicateurs directs et quantifiables d'une meilleure performance et d'une meilleure compréhension des patterns linguistiques par le modèle. Ces mesures sont donc au cœur de l'évaluation et de l'optimisation des modèles de langage.