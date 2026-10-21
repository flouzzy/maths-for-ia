Niveau de difficulté : $\bigstar\bigstar\bigstar\star\star$

Dans le domaine de l'intelligence artificielle, l'entraînement des modèles de langage s'appuie fortement sur la théorie de l'information pour évaluer et optimiser leurs performances. Ces modèles sont entraînés à prédire le mot suivant une séquence donnée, ou à estimer la probabilité d'une phrase. Les métriques telles que l'entropie de Shannon, l'entropie croisée et la divergence de Kullback-Leibler (KL) sont des outils fondamentaux pour y parvenir.

Considérons un scénario simplifié où nous évaluons deux modèles de langage, A et B, sur leur capacité à prédire le mot suivant le déterminant féminin 'la'. Notre vocabulaire simplifié est $\mathcal{V} = \{$'maison', 'ville', 'rue', 'voiture', 'autre'$\}$, où 'autre' représente tous les autres mots possibles non spécifiés dans ce contexte réduit.

Nous disposons des distributions de probabilité suivantes :
*   $P(x)$ : La distribution de probabilité réelle, observée dans un corpus de données très vaste et représentative, pour le mot $x$ suivant 'la'.
*   $Q_A(x)$ : La distribution de probabilité prédite par le modèle de langage A pour le mot $x$ suivant 'la'.
*   $Q_B(x)$ : La distribution de probabilité prédite par le modèle de langage B pour le mot $x$ suivant 'la'.

Les distributions sont données par les tableaux suivants :

| Mot $x$      | $P(x)$ | $Q_A(x)$ | $Q_B(x)$ |
| :----------- | :----- | :------- | :------- |
| 'maison'     | 0.40   | 0.35     | 0.45     |
| 'ville'      | 0.30   | 0.25     | 0.20     |
| 'rue'        | 0.20   | 0.20     | 0.15     |
| 'voiture'    | 0.05   | 0.10     | 0.10     |
| 'autre'      | 0.05   | 0.10     | 0.10     |

Pour tous les calculs nécessitant des logarithmes, nous utiliserons la base 2. Les résultats finaux seront arrondis à trois décimales. Pour les calculs intermédiaires, une précision supérieure sera maintenue.

---

**Partie A : Entropie de Shannon et Mesure d'Incertitude**

1.  Rappelez la définition de l'entropie de Shannon $H(P)$ pour une distribution de probabilité discrète $P$ sur un ensemble de symboles $\mathcal{V}$.
2.  Calculez l'entropie $H(P)$ de la distribution réelle $P$.
3.  Interprétez la valeur obtenue de $H(P)$ dans le contexte de la prédiction du mot suivant. Que nous indique-t-elle sur la prévisibilité de cette tâche ?

**Partie B : Entropie Croisée et Fonction de Perte pour les Modèles de Langage**

1.  Rappelez la définition de l'entropie croisée $H_C(P, Q)$ entre une distribution réelle $P$ et une distribution prédite $Q$.
2.  Calculez l'entropie croisée $H_C(P, Q_A)$ pour le modèle de langage A.
3.  Calculez l'entropie croisée $H_C(P, Q_B)$ pour le modèle de langage B.
4.  En vous basant sur les valeurs d'entropie croisée, quel modèle de langage, A ou B, offre une meilleure prédiction des mots suivants 'la' selon cette métrique ? Justifiez votre réponse.
5.  Expliquez pourquoi l'entropie croisée est une fonction de perte couramment utilisée pour l'entraînement des modèles de langage.

**Partie C : Divergence de Kullback-Leibler et Différence entre Distributions**

1.  Rappelez la définition de la divergence de Kullback-Leibler $D_{KL}(P || Q)$ entre deux distributions $P$ et $Q$.
2.  Calculez la divergence $D_{KL}(P || Q_A)$.
3.  Calculez la divergence $D_{KL}(P || Q_B)$.
4.  Confirmez-vous le résultat de la question B.4 en utilisant la divergence KL ? Quel modèle est le meilleur ? Justifiez.
5.  Démontrez la relation fondamentale $D_{KL}(P || Q) = H_C(P, Q) - H(P)$.
6.  Discutez pourquoi, malgré sa capacité à mesurer la "distance" entre $P$ et $Q$, $H_C(P, Q)$ est souvent préférée à $D_{KL}(P || Q)$ comme fonction de perte lors de l'entraînement des modèles de langage.

**Partie D : Cas Spécifiques et Réflexions Avancées**

1.  Considérons un cas où, pour un certain mot $x_0 \in \mathcal{V}$, la distribution réelle $P(x_0)$ est strictement positive, mais le modèle prédit $Q(x_0) = 0$. Que se passe-t-il pour $H_C(P, Q)$ et $D_{KL}(P || Q)$ dans cette situation ? Interprétez la signification de ce résultat pour l'entraînement d'un modèle.
2.  À l'inverse, si $P(x_0) = 0$ et $Q(x_0) > 0$ pour un mot $x_0$, que deviennent les termes correspondants dans $H_C(P, Q)$ et $D_{KL}(P || Q)$ ?

---

### Corrigé Détaillé

Pour faciliter les calculs, voici les valeurs de $\log_2(x)$ pour les probabilités données, arrondies à six décimales :

*   $\log_2(0.40) \approx -1.321928$
*   $\log_2(0.30) \approx -1.736966$
*   $\log_2(0.20) \approx -2.321928$
*   $\log_2(0.05) \approx -4.321928$

*   $\log_2(0.35) \approx -1.514573$
*   $\log_2(0.25) = -2.000000$
*   $\log_2(0.10) \approx -3.321928$

*   $\log_2(0.45) \approx -1.157523$
*   $\log_2(0.15) \approx -2.736966$

---

**Partie A : Entropie de Shannon et Mesure d'Incertitude**

1.  **Définition de l'entropie de Shannon $H(P)$ :**
    L'entropie de Shannon $H(P)$ d'une distribution de probabilité discrète $P$ sur un ensemble de symboles $\mathcal{V}$ mesure l'incertitude ou la quantité d'information moyenne contenue dans un événement tiré de cette distribution. Elle est définie par la formule :
    $$H(P) = - \sum_{x \in \mathcal{V}} P(x) \log_2 P(x)$$
    où $P(x)$ est la probabilité du symbole $x$, et le logarithme est en base 2, ce qui donne un résultat en bits. Par convention, si $P(x)=0$, le terme $P(x)\log_2 P(x)$ est pris comme 0.

2.  **Calcul de l'entropie $H(P)$ de la distribution réelle $P$ :**
    Nous appliquons la formule avec les probabilités de la distribution $P$ :
    $H(P) = - [P(\text{'maison'}) \log_2 P(\text{'maison'}) + P(\text{'ville'}) \log_2 P(\text{'ville'}) + P(\text{'rue'}) \log_2 P(\text{'rue'}) + P(\text{'voiture'}) \log_2 P(\text{'voiture'}) + P(\text{'autre'}) \log_2 P(\text{'autre'})]$
    $H(P) = - [0.40 \log_2(0.40) + 0.30 \log_2(0.30) + 0.20 \log_2(0.20) + 0.05 \log_2(0.05) + 0.05 \log_2(0.05)]$
    En utilisant les valeurs des logarithmes :
    $H(P) = - [0.40(-1.321928) + 0.30(-1.736966) + 0.20(-2.321928) + 0.05(-4.321928) + 0.05(-4.321928)]$
    $H(P) = - [-0.5287712 - 0.5210898 - 0.4643856 - 0.2160964 - 0.2160964]$
    $H(P) = - [-1.9464394]$
    $H(P) \approx 1.946$ bits

3.  **Interprétation de $H(P)$ :**
    La valeur $H(P) \approx 1.946$ bits représente l'incertitude moyenne inhérente à la tâche de prédire le mot suivant 'la' dans le corpus réel. Cela signifie qu'en moyenne, pour identifier le mot suivant 'la', nous avons besoin d'environ 1.946 bits d'information. Plus cette valeur est élevée, plus la distribution est uniforme (les mots sont également probables), et donc plus la tâche de prédiction est difficile. Inversement, une valeur faible indique une forte prévisibilité (certains mots sont beaucoup plus probables que d'autres). Ici, la valeur est modérée, indiquant que bien qu'il y ait une certaine incertitude, la distribution n'est pas complètement uniforme.

---

**Partie B : Entropie Croisée et Fonction de Perte pour les Modèles de Langage**

1.  **Définition de l'entropie croisée $H_C(P, Q)$ :**
    L'entropie croisée $H_C(P, Q)$ entre une distribution réelle (ou cible) $P$ et une distribution prédite (ou modèle) $Q$ mesure la quantité moyenne de bits nécessaires pour identifier un événement tiré de $P$ en utilisant une fonction d'encodage optimisée pour $Q$. C'est une mesure de l'erreur entre les deux distributions. Elle est définie par la formule :
    $$H_C(P, Q) = - \sum_{x \in \mathcal{V}} P(x) \log_2 Q(x)$$
    où $P(x)$ est la probabilité réelle du symbole $x$ et $Q(x)$ est la probabilité prédite par le modèle pour le symbole $x$. Si $P(x) > 0$ et $Q(x) = 0$ pour un $x$, l'entropie croisée devient infinie.

2.  **Calcul de l'entropie croisée $H_C(P, Q_A)$ :**
    $H_C(P, Q_A) = - [P(\text{'maison'}) \log_2 Q_A(\text{'maison'}) + P(\text{'ville'}) \log_2 Q_A(\text{'ville'}) + P(\text{'rue'}) \log_2 Q_A(\text{'rue'}) + P(\text{'voiture'}) \log_2 Q_A(\text{'voiture'}) + P(\text{'autre'}) \log_2 Q_A(\text{'autre'})]$
    $H_C(P, Q_A) = - [0.40 \log_2(0.35) + 0.30 \log_2(0.25) + 0.20 \log_2(0.20) + 0.05 \log_2(0.10) + 0.05 \log_2(0.10)]$
    En utilisant les valeurs des logarithmes :
    $H_C(P, Q_A) = - [0.40(-1.514573) + 0.30(-2.000000) + 0.20(-2.321928) + 0.05(-3.321928) + 0.05(-3.321928)]$
    $H_C(P, Q_A) = - [-0.6058292 - 0.6000000 - 0.4643856 - 0.1660964 - 0.1660964]$
    $H_C(P, Q_A) = - [-2.0024076]$
    $H_C(P, Q_A) \approx 2.002$ bits

3.  **Calcul de l'entropie croisée $H_C(P, Q_B)$ :**
    $H_C(P, Q_B) = - [P(\text{'maison'}) \log_2 Q_B(\text{'maison'}) + P(\text{'ville'}) \log_2 Q_B(\text{'ville'}) + P(\text{'rue'}) \log_2 Q_B(\text{'rue'}) + P(\text{'voiture'}) \log_2 Q_B(\text{'voiture'}) + P(\text{'autre'}) \log_2 Q_B(\text{'autre'})]$
    $H_C(P, Q_B) = - [0.40 \log_2(0.45) + 0.30 \log_2(0.20) + 0.20 \log_2(0.15) + 0.05 \log_2(0.10) + 0.05 \log_2(0.10)]$
    En utilisant les valeurs des logarithmes :
    $H_C(P, Q_B) = - [0.40(-1.157523) + 0.30(-2.321928) + 0.20(-2.736966) + 0.05(-3.321928) + 0.05(-3.321928)]$
    $H_C(P, Q_B) = - [-0.4630092 - 0.6965784 - 0.5473932 - 0.1660964 - 0.1660964]$
    $H_C(P, Q_B) = - [-2.0391736]$
    $H_C(P, Q_B) \approx 2.039$ bits

4.  **Comparaison des modèles A et B basée sur l'entropie croisée :**
    Nous avons $H_C(P, Q_A) \approx 2.002$ bits et $H_C(P, Q_B) \approx 2.039$ bits.
    L'entropie croisée est une mesure de l'erreur ou de la divergence entre la distribution réelle et la distribution prédite. Une valeur plus faible d'entropie croisée indique que la distribution prédite par le modèle est plus proche de la distribution réelle.
    Puisque $H_C(P, Q_A) < H_C(P, Q_B)$, le modèle de langage A offre une meilleure prédiction des mots suivants 'la' que le modèle B, selon cette métrique. Le modèle A est "moins surpris" par les événements réels.

5.  **Pourquoi l'entropie croisée est une fonction de perte couramment utilisée :**
    L'entropie croisée est une fonction de perte clé pour les modèles de langage (et plus généralement pour les tâches de classification) pour plusieurs raisons :
    *   **Mesure de l'écart :** Elle quantifie à quel point la distribution de probabilité prédite par le modèle diffère de la distribution de probabilité réelle. Minimiser l'entropie croisée équivaut à rendre la distribution prédite aussi proche que possible de la distribution réelle.
    *   **Pénalité forte pour les erreurs graves :** Si le modèle prédit une probabilité très faible pour un événement qui s'avère être la vérité (c'est-à-dire $P(x)$ est élevée et $Q(x)$ est faible), le terme $-P(x) \log_2 Q(x)$ sera très grand (et positif, car $\log_2 Q(x)$ est un grand nombre négatif), pénalisant fortement le modèle. Si $Q(x)$ est 0 alors que $P(x)$ est positive, la pénalité est infinie, ce qui est souhaitable pour éviter de telles erreurs catastrophiques.
    *   **Gradient utile :** La fonction d'entropie croisée est différentiable, ce qui permet d'utiliser des algorithmes d'optimisation basés sur le gradient (comme la descente de gradient) pour ajuster les poids du modèle pendant l'entraînement.
    *   **Relation avec la Vraisemblance Maximale :** Minimiser l'entropie croisée est équivalent à maximiser la vraisemblance (ou le log-vraisemblance) des données d'entraînement. C'est un principe statistique bien établi pour l'estimation de modèles.

---

**Partie C : Divergence de Kullback-Leibler et Différence entre Distributions**

1.  **Définition de la divergence de Kullback-Leibler $D_{KL}(P || Q)$ :**
    La divergence de Kullback-Leibler (KL) $D_{KL}(P || Q)$, également appelée entropie relative, mesure la "quantité d'information perdue" lorsqu'une distribution $Q$ est utilisée pour approximer une distribution $P$. Elle quantifie la différence entre deux distributions de probabilité. Elle est définie par la formule :
    $$D_{KL}(P || Q) = \sum_{x \in \mathcal{V}} P(x) \log_2 \frac{P(x)}{Q(x)}$$
    La divergence KL est toujours non-négative ($D_{KL}(P || Q) \geq 0$) et est égale à zéro si et seulement si $P = Q$. Elle n'est pas symétrique, c'est-à-dire $D_{KL}(P || Q) \neq D_{KL}(Q || P)$.

2.  **Calcul de la divergence $D_{KL}(P || Q_A)$ :**
    Nous allons utiliser la relation $D_{KL}(P || Q) = H_C(P, Q) - H(P)$ démontrée plus loin pour simplifier le calcul.
    En utilisant les valeurs calculées précédemment :
    $D_{KL}(P || Q_A) = H_C(P, Q_A) - H(P)$
    $D_{KL}(P || Q_A) = 2.0024076 - 1.9464394$
    $D_{KL}(P || Q_A) = 0.0559682$
    $D_{KL}(P || Q_A) \approx 0.056$ bits

3.  **Calcul de la divergence $D_{KL}(P || Q_B)$ :**
    De même pour $Q_B$ :
    $D_{KL}(P || Q_B) = H_C(P, Q_B) - H(P)$
    $D_{KL}(P || Q_B) = 2.0391736 - 1.9464394$
    $D_{KL}(P || Q_B) = 0.0927342$
    $D_{KL}(P || Q_B) \approx 0.093$ bits

4.  **Confirmation du résultat de la question B.4 avec la divergence KL :**
    Nous avons $D_{KL}(P || Q_A) \approx 0.056$ bits et $D_{KL}(P || Q_B) \approx 0.093$ bits.
    La divergence KL mesure la "distance" ou la "différence" entre la distribution réelle $P$ et la distribution prédite $Q$. Une valeur plus faible de $D_{KL}$ indique que $Q$ est une meilleure approximation de $P$.
    Puisque $D_{KL}(P || Q_A) < D_{KL}(P || Q_B)$, le modèle de langage A est une meilleure approximation de la distribution réelle $P$ que le modèle B. Cela confirme le résultat obtenu avec l'entropie croisée : le modèle A est meilleur.

5.  **Démonstration de la relation fondamentale $D_{KL}(P || Q) = H_C(P, Q) - H(P)$ :**
    Partons de la définition de la divergence KL :
    $D_{KL}(P || Q) = \sum_{x \in \mathcal{V}} P(x) \log_2 \frac{P(x)}{Q(x)}$
    En utilisant la propriété des logarithmes $\log_b(\frac{A}{B}) = \log_b(A) - \log_b(B)$, nous obtenons :
    $D_{KL}(P || Q) = \sum_{x \in \mathcal{V}} P(x) (\log_2 P(x) - \log_2 Q(x))$
    Nous pouvons séparer la somme :
    $D_{KL}(P || Q) = \sum_{x \in \mathcal{V}} P(x) \log_2 P(x) - \sum_{x \in \mathcal{V}} P(x) \log_2 Q(x)$
    Reconnaissons les définitions de $H(P)$ et $H_C(P, Q)$ :
    Nous savons que $H(P) = - \sum_{x \in \mathcal{V}} P(x) \log_2 P(x)$, donc $\sum_{x \in \mathcal{V}} P(x) \log_2 P(x) = - H(P)$.
    Nous savons aussi que $H_C(P, Q) = - \sum_{x \in \mathcal{V}} P(x) \log_2 Q(x)$.
    En substituant ces expressions dans l'équation de la divergence KL :
    $D_{KL}(P || Q) = (-H(P)) - (-H_C(P, Q))$
    $D_{KL}(P || Q) = H_C(P, Q) - H(P)$
    La relation est ainsi démontrée.

6.  **Pourquoi $H_C(P, Q)$ est souvent préférée à $D_{KL}(P || Q)$ comme fonction de perte :**
    Bien que la divergence KL mesure directement la "distance" entre $P$ et $Q$, l'entropie croisée est souvent préférée comme fonction de perte en apprentissage automatique pour des raisons pratiques :
    *   **Simplification :** Comme démontré, $D_{KL}(P || Q) = H_C(P, Q) - H(P)$. Lors de l'entraînement d'un modèle, la distribution réelle $P$ est fixe et ne dépend pas des paramètres du modèle. Par conséquent, l'entropie de Shannon $H(P)$ est une constante. Minimiser $H_C(P, Q)$ est donc équivalent à minimiser $D_{KL}(P || Q)$ puisque la différence n'est qu'une constante additive. Utiliser $H_C(P, Q)$ revient à ignorer cette constante, ce qui simplifie légèrement le calcul sans affecter le processus d'optimisation.
    *   **Nature intrinsèque de la tâche :** Pour de nombreuses tâches d'apprentissage supervisé, l'objectif est de prédire la bonne étiquette (représentée par $P$) avec la plus haute probabilité possible (représentée par $Q$). L'entropie croisée mesure directement la performance de cette prédiction.
    *   **Conventions et implémentations :** Dans de nombreuses bibliothèques d'apprentissage automatique, l'entropie croisée est la fonction de perte par défaut pour les tâches de classification (en particulier pour la classification multi-classes avec Softmax en sortie), en raison de sa simplicité et de son efficacité.

---

**Partie D : Cas Spécifiques et Réflexions Avancées**

1.  **Cas où $P(x_0) > 0$ et $Q(x_0) = 0$ :**
    Si pour un certain mot $x_0$, la distribution réelle $P(x_0)$ est strictement positive (c'est-à-dire que ce mot peut réellement apparaître), mais le modèle prédit $Q(x_0) = 0$ (le modèle pense que ce mot ne peut jamais apparaître), examinons les formules :
    *   **Pour $H_C(P, Q)$ :** Le terme correspondant est $-P(x_0) \log_2 Q(x_0)$. Puisque $Q(x_0) \to 0^+$, $\log_2 Q(x_0) \to -\infty$. Par conséquent, $-P(x_0) \log_2 Q(x_0) \to +\infty$ (car $P(x_0) > 0$).
        Ainsi, $H_C(P, Q)$ tend vers l'infini.
    *   **Pour $D_{KL}(P || Q)$ :** Le terme correspondant est $P(x_0) \log_2 \frac{P(x_0)}{Q(x_0)}$. Puisque $Q(x_0) \to 0^+$, $\frac{P(x_0)}{Q(x_0)} \to +\infty$, et donc $\log_2 \frac{P(x_0)}{Q(x_0)} \to +\infty$. Par conséquent, $P(x_0) \log_2 \frac{P(x_0)}{Q(x_0)} \to +\infty$.
        Ainsi, $D_{KL}(P || Q)$ tend également vers l'infini.

    **Interprétation :** Ce résultat est très important dans l'entraînement des modèles. Il signifie qu'un modèle qui attribue une probabilité nulle à un événement qui se produit réellement est pénalisé de manière infinie. Cela empêche les modèles d'être "trop confiants" et de ne pas considérer des possibilités qui existent dans la réalité. C'est une propriété désirée pour les fonctions de perte, car elle force le modèle à toujours attribuer au moins une très petite probabilité positive à toute éventualité qui n'est pas strictement impossible dans les données d'entraînement. En pratique, on utilise souvent des techniques de "lissage" pour éviter que des $Q(x)=0$ ne se produisent, par exemple en ajoutant une petite constante à toutes les probabilités prédites (lissage de Laplace).

2.  **Cas où $P(x_0) = 0$ et $Q(x_0) > 0$ :**
    Si pour un mot $x_0$, la distribution réelle $P(x_0)$ est nulle (ce mot ne devrait jamais apparaître), mais le modèle prédit $Q(x_0) > 0$ (le modèle pense que ce mot peut apparaître avec une certaine probabilité), examinons les formules :
    *   **Pour $H_C(P, Q)$ :** Le terme correspondant est $-P(x_0) \log_2 Q(x_0)$. Puisque $P(x_0) = 0$, ce terme devient $0 \cdot \log_2 Q(x_0)$. Par convention, $0 \cdot \log(n)$ pour $n>0$ est défini comme 0. Ainsi, ce terme ne contribue pas à l'entropie croisée.
    *   **Pour $D_{KL}(P || Q)$ :** Le terme correspondant est $P(x_0) \log_2 \frac{P(x_0)}{Q(x_0)}$. Puisque $P(x_0) = 0$, ce terme devient $0 \cdot \log_2 \frac{0}{Q(x_0)}$. Par convention mathématique, la limite de $x \log x$ quand $x \to 0^+$ est 0. Appliquant cela à $P(x_0) \log_2 P(x_0)$ (qui est une partie de la réécriture de $P(x_0) \log_2 \frac{P(x_0)}{Q(x_0)}$), ce terme est également pris comme 0. Ainsi, ce terme ne contribue pas non plus à la divergence KL.

    **Interprétation :** Dans ce scénario, la divergence KL et l'entropie croisée ne pénalisent pas le modèle pour avoir prédit une probabilité non nulle pour un événement qui, selon la distribution réelle, n'arrive jamais. Cette asymétrie est caractéristique de la divergence KL (et par extension de l'entropie croisée). Le modèle n'est pas pénalisé s'il "voit des fantômes" (prédit des choses qui ne sont pas dans $P$) tant que ces fantômes n'apparaissent jamais dans les données réelles. Cette propriété est généralement acceptable pour les modèles de langage où un modèle pourrait prédire un mot rare qui n'a pas été observé dans les données d'entraînement, mais qui n'est pas "incorrect" en soi. L'accent est mis sur la prédiction correcte des événements *observés* dans $P$.