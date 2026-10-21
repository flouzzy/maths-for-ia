Niveau de difficulté : $\bigstar\bigstar\bigstar\star\star$

Cher étudiant,

Nous allons explorer les fondements informationnels de l'apprentissage des modèles de langage à travers une série de problèmes concrets. Vous êtes invité à appliquer les concepts d'Entropie de Shannon, de Cross-Entropie et de Divergence de Kullback-Leibler (KL) à un scénario simplifié de prédiction de caractères. Pour toutes les questions impliquant des logarithmes, nous utiliserons la base 2 (logarithme binaire), et les résultats seront exprimés en bits. Les calculs intermédiaires seront arrondis à quatre décimales, et les résultats finaux à trois décimales.

**Contexte de l'exercice :**
Imaginez un modèle de langage rudimentaire dont la tâche est de prédire le caractère suivant dans une séquence. Nous nous concentrerons sur la prédiction du caractère suivant après la séquence "ap". Le vocabulaire des caractères possibles est $\mathcal{V} = \{ \text{'p'}, \text{'l'}, \text{'e'}, \text{'s'} \}$.

**Partie 1 : L'Entropie Intrinsèque de la Source**

1.  La distribution de probabilité réelle (la "vérité terrain") des caractères suivant "ap" est donnée par $P$:
    $P(\text{'p'}) = 0.6$
    $P(\text{'l'}) = 0.1$
    $P(\text{'e'}) = 0.2$
    $P(\text{'s'}) = 0.1$

    Calculez l'Entropie de Shannon $H(P)$ de cette distribution. Expliquez ce que cette valeur représente.

**Partie 2 : L'Évaluation d'un Modèle par la Cross-Entropie**

1.  Un premier modèle de langage, que nous nommerons $M_1$, propose la distribution de probabilité suivante pour les caractères suivant "ap", notée $Q_1$:
    $Q_1(\text{'p'}) = 0.5$
    $Q_1(\text{'l'}) = 0.2$
    $Q_1(\text{'e'}) = 0.2$
    $Q_1(\text{'s'}) = 0.1$

    Calculez la Cross-Entropie $H(P, Q_1)$ entre la distribution réelle $P$ et la distribution prédite par $M_1$, $Q_1$. Expliquez la signification de cette métrique dans le contexte de l'entraînement d'un modèle de langage.

2.  Un deuxième modèle de langage, $M_2$, propose une autre distribution, $Q_2$:
    $Q_2(\text{'p'}) = 0.7$
    $Q_2(\text{'l'}) = 0.05$
    $Q_2(\text{'e'}) = 0.15$
    $Q_2(\text{'s'}) = 0.1$

    Calculez $H(P, Q_2)$. En comparant $H(P, Q_1)$ et $H(P, Q_2)$, quel modèle semble être le plus performant et pourquoi ?

**Partie 3 : La Divergence de Kullback-Leibler**

1.  Calculez la Divergence de Kullback-Leibler $D_{KL}(P\|Q_1)$ pour le modèle $M_1$.

2.  Calculez la Divergence de Kullback-Leibler $D_{KL}(P\|Q_2)$ pour le modèle $M_2$.

3.  Vérifiez la relation fondamentale $D_{KL}(P\|Q) = H(P, Q) - H(P)$ pour les deux modèles $M_1$ et $M_2$.

4.  Interprétez les valeurs de $D_{KL}(P\|Q_1)$ et $D_{KL}(P\|Q_2)$. Comment ces valeurs reflètent-elles la qualité des distributions $Q_1$ et $Q_2$ par rapport à $P$ ?

**Partie 4 : Application à des Contextes Multiples et à l'Optimisation**

Dans un scénario plus réaliste, un modèle de langage doit prédire le caractère suivant pour de nombreux contextes différents. Considérons maintenant deux tâches de prédiction distinctes pour notre modèle:

*   **Tâche 1 (Contexte "ap") :** Utilise la distribution réelle $P_1$ et les distributions prédites $Q_{A,1}$ du modèle $M_A$.
    $P_1 = P = (0.6, 0.1, 0.2, 0.1)$ pour les caractères {'p', 'l', 'e', 's'}.
    Pour cette tâche, le modèle $M_A$ prédit $Q_{A,1} = Q_1 = (0.5, 0.2, 0.2, 0.1)$.

*   **Tâche 2 (Contexte "ba") :** Le vocabulaire est le même. La distribution réelle $P_2$ des caractères suivant "ba" est:
    $P_2(\text{'n'}) = 0.4$
    $P_2(\text{'t'}) = 0.3$
    $P_2(\text{'l'}) = 0.2$
    $P_2(\text{'d'}) = 0.1$
    Pour cette tâche, le modèle $M_A$ prédit $Q_{A,2}$:
    $Q_{A,2}(\text{'n'}) = 0.3$
    $Q_{A,2}(\text{'t'}) = 0.4$
    $Q_{A,2}(\text{'l'}) = 0.2$
    $Q_{A,2}(\text{'d'}) = 0.1$

1.  Calculez l'Entropie de Shannon $H(P_2)$ pour la distribution réelle de la Tâche 2.

2.  Calculez la Cross-Entropie $H(P_2, Q_{A,2})$ pour la Tâche 2.

3.  Calculez la Divergence de Kullback-Leibler $D_{KL}(P_2\|Q_{A,2})$ pour la Tâche 2.

4.  Lors de l'entraînement, un modèle de langage cherche à minimiser la Cross-Entropie moyenne sur un ensemble d'exemples. Calculez la Cross-Entropie moyenne $L_{\text{moyenne}}$ du modèle $M_A$ sur ces deux tâches.
    $L_{\text{moyenne}} = \frac{1}{2} (H(P_1, Q_{A,1}) + H(P_2, Q_{A,2}))$.

5.  Expliquez pourquoi la Cross-Entropie est une fonction de perte si couramment utilisée dans l'entraînement des modèles de langage et comment sa minimisation contribue à l'amélioration du modèle.

---

**Corrigé :**

**Rappel des formules utilisées (logarithmes en base 2) :**
*   **Entropie de Shannon :** $H(P) = - \sum_{x \in \mathcal{V}} P(x) \log_2 P(x)$
*   **Cross-Entropie :** $H(P, Q) = - \sum_{x \in \mathcal{V}} P(x) \log_2 Q(x)$
*   **Divergence de Kullback-Leibler :** $D_{KL}(P\|Q) = \sum_{x \in \mathcal{V}} P(x) \log_2 \frac{P(x)}{Q(x)}$
    Nous savons également que $D_{KL}(P\|Q) = H(P, Q) - H(P)$.

**Partie 1 : L'Entropie Intrinsèque de la Source**

1.  **Calcul de l'Entropie de Shannon $H(P)$ :**
    La distribution réelle $P$ est :
    $P(\text{'p'}) = 0.6$
    $P(\text{'l'}) = 0.1$
    $P(\text{'e'}) = 0.2$
    $P(\text{'s'}) = 0.1$

    La formule de l'Entropie de Shannon est $H(P) = - \sum_{x \in \mathcal{V}} P(x) \log_2 P(x)$.
    Calculons les termes individuels :
    *   $P(\text{'p'}) \log_2 P(\text{'p'}) = 0.6 \times \log_2(0.6)$
        $\log_2(0.6) = \frac{\ln(0.6)}{\ln(2)} \approx \frac{-0.5108256}{0.69314718} \approx -0.73696559 \approx -0.7370$
        $0.6 \times (-0.7370) = -0.4422$
    *   $P(\text{'l'}) \log_2 P(\text{'l'}) = 0.1 \times \log_2(0.1)$
        $\log_2(0.1) = \frac{\ln(0.1)}{\ln(2)} \approx \frac{-2.30258509}{0.69314718} \approx -3.32192809 \approx -3.3219$
        $0.1 \times (-3.3219) = -0.3322$
    *   $P(\text{'e'}) \log_2 P(\text{'e'}) = 0.2 \times \log_2(0.2)$
        $\log_2(0.2) = \frac{\ln(0.2)}{\ln(2)} \approx \frac{-1.60943791}{0.69314718} \approx -2.32192809 \approx -2.3219$
        $0.2 \times (-2.3219) = -0.4644$
    *   $P(\text{'s'}) \log_2 P(\text{'s'}) = 0.1 \times \log_2(0.1)$
        $0.1 \times (-3.3219) = -0.3322$

    $H(P) = - ((-0.4422) + (-0.3322) + (-0.4644) + (-0.3322))$
    $H(P) = - (-1.5710)$
    $H(P) = 1.571$ bits

    **Interprétation :**
    L'Entropie de Shannon $H(P)$ mesure la quantité moyenne d'information contenue dans la variable aléatoire (le prochain caractère) distribuée selon $P$. C'est l'incertitude intrinsèque de la source. Plus la valeur est élevée, plus la distribution est uniforme ou imprévisible. Un modèle de langage "parfait" ne pourrait pas faire mieux que cette entropie pour compresser ou prédire la source, car c'est la limite inférieure théorique du nombre de bits nécessaires pour coder chaque caractère en moyenne, étant donnée la distribution $P$. Ici, 1.571 bits signifie qu'en moyenne, il faut 1.571 bits pour identifier un caractère choisi selon la distribution $P$.

**Partie 2 : L'Évaluation d'un Modèle par la Cross-Entropie**

1.  **Calcul de la Cross-Entropie $H(P, Q_1)$ :**
    Distribution réelle $P$: $(0.6, 0.1, 0.2, 0.1)$
    Distribution prédite par $M_1$, $Q_1$: $(0.5, 0.2, 0.2, 0.1)$

    La formule de la Cross-Entropie est $H(P, Q_1) = - \sum_{x \in \mathcal{V}} P(x) \log_2 Q_1(x)$.
    *   $P(\text{'p'}) \log_2 Q_1(\text{'p'}) = 0.6 \times \log_2(0.5)$
        $\log_2(0.5) = -1.0$
        $0.6 \times (-1.0) = -0.6000$
    *   $P(\text{'l'}) \log_2 Q_1(\text{'l'}) = 0.1 \times \log_2(0.2)$
        $\log_2(0.2) \approx -2.3219$
        $0.1 \times (-2.3219) = -0.2322$
    *   $P(\text{'e'}) \log_2 Q_1(\text{'e'}) = 0.2 \times \log_2(0.2)$
        $\log_2(0.2) \approx -2.3219$
        $0.2 \times (-2.3219) = -0.4644$
    *   $P(\text{'s'}) \log_2 Q_1(\text{'s'}) = 0.1 \times \log_2(0.1)$
        $\log_2(0.1) \approx -3.3219$
        $0.1 \times (-3.3219) = -0.3322$

    $H(P, Q_1) = - ((-0.6000) + (-0.2322) + (-0.4644) + (-0.3322))$
    $H(P, Q_1) = - (-1.6288)$
    $H(P, Q_1) = 1.629$ bits

    **Interprétation :**
    La Cross-Entropie $H(P, Q_1)$ mesure le nombre moyen de bits nécessaires pour identifier un événement tiré de la distribution réelle $P$, si nous utilisons un code optimisé pour la distribution $Q_1$. Dans le cadre d'un modèle de langage, elle quantifie la performance de la distribution de probabilité $Q_1$ prédite par le modèle pour représenter la distribution réelle $P$. Un modèle qui prédit parfaitement $P$ aurait une Cross-Entropie égale à l'Entropie de Shannon $H(P)$. Plus la Cross-Entropie est faible, meilleure est la prédiction du modèle $Q_1$ par rapport à la distribution réelle $P$. La Cross-Entropie est la fonction de perte principale utilisée pour entraîner les modèles de langage, car minimiser $H(P, Q)$ revient à rendre $Q$ aussi proche de $P$ que possible.

2.  **Calcul de $H(P, Q_2)$ et comparaison :**
    Distribution réelle $P$: $(0.6, 0.1, 0.2, 0.1)$
    Distribution prédite par $M_2$, $Q_2$: $(0.7, 0.05, 0.15, 0.1)$

    La formule de la Cross-Entropie est $H(P, Q_2) = - \sum_{x \in \mathcal{V}} P(x) \log_2 Q_2(x)$.
    *   $P(\text{'p'}) \log_2 Q_2(\text{'p'}) = 0.6 \times \log_2(0.7)$
        $\log_2(0.7) = \frac{\ln(0.7)}{\ln(2)} \approx \frac{-0.35667494}{0.69314718} \approx -0.51457317 \approx -0.5146$
        $0.6 \times (-0.5146) = -0.3088$
    *   $P(\text{'l'}) \log_2 Q_2(\text{'l'}) = 0.1 \times \log_2(0.05)$
        $\log_2(0.05) = \frac{\ln(0.05)}{\ln(2)} \approx \frac{-2.99573227}{0.69314718} \approx -4.32192809 \approx -4.3219$
        $0.1 \times (-4.3219) = -0.4322$
    *   $P(\text{'e'}) \log_2 Q_2(\text{'e'}) = 0.2 \times \log_2(0.15)$
        $\log_2(0.15) = \frac{\ln(0.15)}{\ln(2)} \approx \frac{-1.89711998}{0.69314718} \approx -2.73696559 \approx -2.7370$
        $0.2 \times (-2.7370) = -0.5474$
    *   $P(\text{'s'}) \log_2 Q_2(\text{'s'}) = 0.1 \times \log_2(0.1)$
        $\log_2(0.1) \approx -3.3219$
        $0.1 \times (-3.3219) = -0.3322$

    $H(P, Q_2) = - ((-0.3088) + (-0.4322) + (-0.5474) + (-0.3322))$
    $H(P, Q_2) = - (-1.6206)$
    $H(P, Q_2) = 1.621$ bits

    **Comparaison :**
    Nous avons $H(P, Q_1) = 1.629$ bits et $H(P, Q_2) = 1.621$ bits.
    Étant donné qu'une valeur de Cross-Entropie plus faible indique une meilleure adéquation entre la distribution prédite par le modèle et la distribution réelle, le modèle $M_2$ est légèrement plus performant que $M_1$ dans la prédiction des caractères suivant "ap" puisque $H(P, Q_2) < H(P, Q_1)$. Cela signifie que le code optimisé pour $Q_2$ nécessite en moyenne légèrement moins de bits pour coder les événements de $P$ que le code optimisé pour $Q_1$.

**Partie 3 : La Divergence de Kullback-Leibler**

1.  **Calcul de $D_{KL}(P\|Q_1)$ :**
    Nous utiliserons la relation $D_{KL}(P\|Q_1) = H(P, Q_1) - H(P)$.
    En utilisant les valeurs calculées précédemment :
    $H(P) = 1.5710$ bits
    $H(P, Q_1) = 1.6288$ bits
    $D_{KL}(P\|Q_1) = 1.6288 - 1.5710 = 0.0578$ bits
    $D_{KL}(P\|Q_1) = 0.058$ bits

    Vérification par la première formule pour s'assurer de la cohérence :
    *   $P(\text{'p'}) \log_2 \frac{P(\text{'p'})}{Q_1(\text{'p'})} = 0.6 \log_2 \frac{0.6}{0.5} = 0.6 \log_2(1.2)$
        $\log_2(1.2) = \frac{\ln(1.2)}{\ln(2)} \approx \frac{0.18232155}{0.69314718} \approx 0.26303441 \approx 0.2630$
        $0.6 \times 0.2630 = 0.1578$
    *   $P(\text{'l'}) \log_2 \frac{P(\text{'l'})}{Q_1(\text{'l'})} = 0.1 \log_2 \frac{0.1}{0.2} = 0.1 \log_2(0.5)$
        $\log_2(0.5) = -1.0$
        $0.1 \times (-1.0) = -0.1000$
    *   $P(\text{'e'}) \log_2 \frac{P(\text{'e'})}{Q_1(\text{'e'})} = 0.2 \log_2 \frac{0.2}{0.2} = 0.2 \log_2(1.0)$
        $\log_2(1.0) = 0.0$
        $0.2 \times 0.0 = 0.0000$
    *   $P(\text{'s'}) \log_2 \frac{P(\text{'s'})}{Q_1(\text{'s'})} = 0.1 \log_2 \frac{0.1}{0.1} = 0.1 \log_2(1.0)$
        $\log_2(1.0) = 0.0$
        $0.1 \times 0.0 = 0.0000$

    $D_{KL}(P\|Q_1) = 0.1578 + (-0.1000) + 0.0000 + 0.0000 = 0.0578$ bits.
    Les deux méthodes donnent des résultats cohérents.

2.  **Calcul de $D_{KL}(P\|Q_2)$ :**
    Utilisons la relation $D_{KL}(P\|Q_2) = H(P, Q_2) - H(P)$.
    $H(P) = 1.5710$ bits
    $H(P, Q_2) = 1.6206$ bits
    $D_{KL}(P\|Q_2) = 1.6206 - 1.5710 = 0.0496$ bits
    $D_{KL}(P\|Q_2) = 0.050$ bits

3.  **Vérification de la relation $D_{KL}(P\|Q) = H(P, Q) - H(P)$ :**
    *   Pour $M_1$ :
        Calcul direct $D_{KL}(P\|Q_1) = 0.0578$ bits.
        Calcul par soustraction $H(P, Q_1) - H(P) = 1.6288 - 1.5710 = 0.0578$ bits.
        La relation est vérifiée.
    *   Pour $M_2$ :
        Calcul par soustraction $H(P, Q_2) - H(P) = 1.6206 - 1.5710 = 0.0496$ bits.
        La relation est vérifiée.

4.  **Interprétation des valeurs de $D_{KL}$ :**
    La Divergence de Kullback-Leibler $D_{KL}(P\|Q)$ mesure la perte d'information lorsque la distribution $Q$ est utilisée pour approximer la distribution $P$. Elle quantifie la "distance" ou la "dissimilarité" entre les deux distributions. Une valeur de $D_{KL}$ de zéro indique que $Q$ est identique à $P$. Plus la valeur est grande, plus les distributions sont différentes.

    *   $D_{KL}(P\|Q_1) = 0.058$ bits.
    *   $D_{KL}(P\|Q_2) = 0.050$ bits.

    Puisque $D_{KL}(P\|Q_2) < D_{KL}(P\|Q_1)$, la distribution $Q_2$ du modèle $M_2$ est plus proche de la distribution réelle $P$ que ne l'est la distribution $Q_1$ du modèle $M_1$. Cela confirme l'observation faite avec la Cross-Entropie : le modèle $M_2$ est un meilleur estimateur de la vérité terrain que $M_1$. La divergence KL représente l'information supplémentaire (en bits) qui doit être transmise si on utilise un code basé sur $Q$ au lieu du code optimal basé sur $P$.

**Partie 4 : Application à des Contextes Multiples et à l'Optimisation**

1.  **Calcul de l'Entropie de Shannon $H(P_2)$ pour la Tâche 2 :**
    Distribution réelle $P_2$:
    $P_2(\text{'n'}) = 0.4$
    $P_2(\text{'t'}) = 0.3$
    $P_2(\text{'l'}) = 0.2$
    $P_2(\text{'d'}) = 0.1$

    $H(P_2) = - \sum_{x \in \mathcal{V}} P_2(x) \log_2 P_2(x)$.
    *   $P_2(\text{'n'}) \log_2 P_2(\text{'n'}) = 0.4 \times \log_2(0.4)$
        $\log_2(0.4) = \frac{\ln(0.4)}{\ln(2)} \approx \frac{-0.91629073}{0.69314718} \approx -1.32192809 \approx -1.3219$
        $0.4 \times (-1.3219) = -0.5288$
    *   $P_2(\text{'t'}) \log_2 P_2(\text{'t'}) = 0.3 \times \log_2(0.3)$
        $\log_2(0.3) = \frac{\ln(0.3)}{\ln(2)} \approx \frac{-1.20397289}{0.69314718} \approx -1.73696559 \approx -1.7370$
        $0.3 \times (-1.7370) = -0.5211$
    *   $P_2(\text{'l'}) \log_2 P_2(\text{'l'}) = 0.2 \times \log_2(0.2)$
        $\log_2(0.2) \approx -2.3219$
        $0.2 \times (-2.3219) = -0.4644$
    *   $P_2(\text{'d'}) \log_2 P_2(\text{'d'}) = 0.1 \times \log_2(0.1)$
        $\log_2(0.1) \approx -3.3219$
        $0.1 \times (-3.3219) = -0.3322$

    $H(P_2) = - ((-0.5288) + (-0.5211) + (-0.4644) + (-0.3322))$
    $H(P_2) = - (-1.8465)$
    $H(P_2) = 1.847$ bits

2.  **Calcul de la Cross-Entropie $H(P_2, Q_{A,2})$ pour la Tâche 2 :**
    Distribution réelle $P_2$: $(0.4, 0.3, 0.2, 0.1)$
    Distribution prédite par $M_A$, $Q_{A,2}$: $(0.3, 0.4, 0.2, 0.1)$

    $H(P_2, Q_{A,2}) = - \sum_{x \in \mathcal{V}} P_2(x) \log_2 Q_{A,2}(x)$.
    *   $P_2(\text{'n'}) \log_2 Q_{A,2}(\text{'n'}) = 0.4 \times \log_2(0.3)$
        $\log_2(0.3) \approx -1.7370$
        $0.4 \times (-1.7370) = -0.6948$
    *   $P_2(\text{'t'}) \log_2 Q_{A,2}(\text{'t'}) = 0.3 \times \log_2(0.4)$
        $\log_2(0.4) \approx -1.3219$
        $0.3 \times (-1.3219) = -0.3966$
    *   $P_2(\text{'l'}) \log_2 Q_{A,2}(\text{'l'}) = 0.2 \times \log_2(0.2)$
        $\log_2(0.2) \approx -2.3219$
        $0.2 \times (-2.3219) = -0.4644$
    *   $P_2(\text{'d'}) \log_2 Q_{A,2}(\text{'d'}) = 0.1 \times \log_2(0.1)$
        $\log_2(0.1) \approx -3.3219$
        $0.1 \times (-3.3219) = -0.3322$

    $H(P_2, Q_{A,2}) = - ((-0.6948) + (-0.3966) + (-0.4644) + (-0.3322))$
    $H(P_2, Q_{A,2}) = - (-1.8880)$
    $H(P_2, Q_{A,2}) = 1.888$ bits

3.  **Calcul de la Divergence de Kullback-Leibler $D_{KL}(P_2\|Q_{A,2})$ pour la Tâche 2 :**
    Utilisons la relation $D_{KL}(P_2\|Q_{A,2}) = H(P_2, Q_{A,2}) - H(P_2)$.
    $H(P_2) = 1.8465$ bits
    $H(P_2, Q_{A,2}) = 1.8880$ bits
    $D_{KL}(P_2\|Q_{A,2}) = 1.8880 - 1.8465 = 0.0415$ bits
    $D_{KL}(P_2\|Q_{A,2}) = 0.042$ bits

4.  **Calcul de la Cross-Entropie moyenne $L_{\text{moyenne}}$ :**
    Nous avons $H(P_1, Q_{A,1}) = H(P, Q_1) = 1.6288$ bits (calculé en Partie 2.1).
    Nous avons $H(P_2, Q_{A,2}) = 1.8880$ bits (calculé en Partie 4.2).

    $L_{\text{moyenne}} = \frac{1}{2} (H(P_1, Q_{A,1}) + H(P_2, Q_{A,2}))$
    $L_{\text{moyenne}} = \frac{1}{2} (1.6288 + 1.8880)$
    $L_{\text{moyenne}} = \frac{1}{2} (3.5168)$
    $L_{\text{moyenne}} = 1.7584$ bits
    $L_{\text{moyenne}} = 1.758$ bits

5.  **Explication de la Cross-Entropie comme fonction de perte et son rôle dans l'amélioration du modèle :**
    La Cross-Entropie est une fonction de perte (ou fonction objectif) très utilisée dans l'entraînement des modèles de classification et de langage, car elle mesure directement la "distance" entre la distribution de probabilité prédite par le modèle ($Q$) et la distribution de probabilité réelle ($P$) des données.

    Lorsque l'on entraîne un modèle de langage, l'objectif est de faire en sorte que ses prédictions $Q$ ressemblent le plus possible aux vraies distributions $P$ observées dans les données d'entraînement. Minimiser la Cross-Entropie $H(P, Q)$ revient à :
    *   **Maximiser la vraisemblance :** La Cross-Entropie est étroitement liée à la maximisation de la vraisemblance des données d'entraînement sous le modèle. Minimiser $H(P,Q)$ est équivalent à maximiser $\sum P(x) \log_2 Q(x)$, ce qui correspond à maximiser le logarithme de la probabilité que le modèle attribue aux vrais événements. Un modèle qui attribue une probabilité élevée aux événements réels est considéré comme un bon modèle.
    *   **Réduire l'incertitude du modèle :** Une faible Cross-Entropie signifie que le modèle attribue une probabilité élevée aux événements qui se produisent réellement, réduisant ainsi l'incertitude quant à la prédiction du prochain token. En d'autres termes, le modèle est plus "sûr" de ses bonnes prédictions.
    *   **Exploiter la relation avec la KL Divergence :** Nous savons que $H(P, Q) = H(P) + D_{KL}(P\|Q)$. Comme $H(P)$ est une constante (l'entropie intrinsèque de la distribution réelle, indépendante du modèle), minimiser $H(P, Q)$ est équivalent à minimiser $D_{KL}(P\|Q)$. La KL Divergence est toujours non-négative et est nulle si et seulement si $P=Q$. Par conséquent, minimiser la Cross-Entropie pousse le modèle à faire en sorte que sa distribution prédite $Q$ converge vers la distribution réelle $P$.

    En minimisant la Cross-Entropie moyenne sur un grand nombre d'exemples et de contextes (comme $L_{\text{moyenne}}$ calculée pour ces deux tâches), le modèle apprend à ajuster ses paramètres internes (poids et biais) pour produire des distributions de probabilité $Q$ qui sont de plus en plus précises et fiables. Cela permet au modèle de mieux comprendre les patterns linguistiques et de générer du texte plus cohérent et pertinent. L'amélioration est mesurable par la diminution de cette valeur de Cross-Entropie au cours de l'entraînement, indiquant une meilleure capacité de prédiction du modèle.