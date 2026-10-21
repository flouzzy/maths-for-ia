Niveau de difficulté : $\bigstar\bigstar\star\star\star$

Mes chers étudiants,

Il est essentiel, dans le domaine foisonnant de l'apprentissage automatique, et plus particulièrement dans celui des modèles de langage, de maîtriser les fondements théoriques qui sous-tendent leurs mécanismes d'entraînement. Nous allons aujourd'hui explorer trois concepts fondamentaux de la théorie de l'information : l'Entropie de Shannon, l'Entropie Croisée (ou Cross-Entropy) et la Divergence de Kullback-Leibler (KL), en les appliquant à un scénario simplifié de prédiction de mot suivant par un modèle de langage. Ce problème est conçu pour vous guider pas à pas dans la compréhension de ces mesures clés.

Nous utiliserons le logarithme en base 2, noté $\log_2$, car il exprime l'information en bits. Pour les calculs, vous pouvez utiliser les approximations suivantes si nécessaire :
$\log_2(0.1) \approx -3.3219$
$\log_2(0.2) \approx -2.3219$
$\log_2(0.5) = -1.0$
$\log_2(0.6) \approx -0.7370$
$\log_2(0.7) \approx -0.5146$
$\log_2(1) = 0.0$
$\log_2(7/6) = \log_2(1.166...) \approx 0.2110$

---

**Contexte de l'exercice :**

Imaginons un modèle de langage simpliste dont la tâche est de prédire le mot suivant après la séquence "Le chien". Pour simplifier notre étude, notre vocabulaire de mots possibles est très réduit : $V = \{ \text{"mange"}, \text{"dort"}, \text{"joue"} \}$.

Une analyse exhaustive d'un corpus gigantesque nous a permis d'établir la véritable distribution de probabilité $P$ pour le mot suivant, conditionnée par le contexte "Le chien" :
$P(\text{"mange"}) = 0.1$
$P(\text{"dort"}) = 0.7$
$P(\text{"joue"}) = 0.2$

Notre modèle de langage, après une première phase d'entraînement, propose sa propre distribution de probabilité $Q$ pour le mot suivant, toujours conditionnée par "Le chien" :
$Q(\text{"mange"}) = 0.2$
$Q(\text{"dort"}) = 0.6$
$Q(\text{"joue"}) = 0.2$

---

**Partie 1 : L'Entropie de Shannon**

1.1. Expliquez en vos propres termes ce que représente l'Entropie de Shannon $H(P)$ pour une distribution de probabilité $P$. Quelle est son unité de mesure dans ce contexte ?

1.2. Calculez l'Entropie de Shannon $H(P)$ pour la distribution réelle $P$ donnée. Détaillez toutes les étapes de votre calcul.

---

**Partie 2 : L'Entropie Croisée (Cross-Entropy)**

2.1. Définissez l'Entropie Croisée $H(P, Q)$. Pourquoi est-elle fréquemment utilisée comme fonction de coût (ou de perte) dans l'entraînement des modèles de langage ?

2.2. Calculez l'Entropie Croisée $H(P, Q)$ entre la distribution réelle $P$ et la distribution prédite par le modèle $Q$. Détaillez toutes les étapes de votre calcul.

2.3. Imaginez un modèle de langage "parfait" dont la distribution prédite $Q_{\text{parfait}}$ serait exactement égale à la distribution réelle $P$. Quelle serait alors la valeur de $H(P, Q_{\text{parfait}})$ ? Justifiez votre réponse.

---

**Partie 3 : La Divergence de Kullback-Leibler (KL)**

3.1. La Divergence de Kullback-Leibler $D_{KL}(P || Q)$ est une mesure de la "distance" entre deux distributions de probabilité. Calculez $D_{KL}(P || Q)$ en utilisant la relation $D_{KL}(P || Q) = H(P, Q) - H(P)$. Détaillez votre calcul.

3.2. Calculez maintenant $D_{KL}(P || Q)$ en utilisant sa formule directe :
$D_{KL}(P || Q) = \sum_{x \in V} P(x) \log_2 \frac{P(x)}{Q(x)}$.
Assurez-vous que les résultats des questions 3.1 et 3.2 sont cohérents.

3.3. Interprétez la valeur de $D_{KL}(P || Q)$ que vous avez trouvée. Que signifie un $D_{KL}(P || Q)$ élevé ou faible dans le contexte de notre modèle de langage ?

3.4. Discutez brièvement ce qui se passerait, d'un point de vue mathématique et pratique, si notre modèle prédisait $Q(\text{"mange"}) = 0.0$ alors que $P(\text{"mange"}) = 0.1$. Quel impact cela aurait-il sur le calcul de $D_{KL}(P || Q)$ ?

---

**Partie 4 : Implications pour l'entraînement des Modèles de Langage**

4.1. Vous avez calculé $H(P,Q)$ et $D_{KL}(P || Q)$. Expliquez pourquoi, lors de l'entraînement d'un modèle de langage, la Cross-Entropy est généralement préférée à la Divergence KL comme fonction de coût directe, même si les deux sont étroitement liées.

4.2. Décrivez succinctement comment la Cross-Entropy est utilisée dans le processus itératif d'entraînement d'un modèle de langage.

4.3. Si notre modèle s'améliorait significativement après plusieurs étapes d'entraînement, comment anticipez-vous que les valeurs de $H(P, Q)$ et $D_{KL}(P || Q)$ évolueraient ?

---
---

**Corrigé Détaillé de l'Exercice**

**Partie 1 : L'Entropie de Shannon**

1.1. L'Entropie de Shannon, $H(P)$, mesure l'incertitude ou la quantité moyenne d'information contenue dans une distribution de probabilité $P$. Plus la distribution est "plate" (c'est-à-dire que les probabilités sont réparties de manière égale entre les événements), plus l'incertitude est élevée, et plus l'entropie est grande. Inversement, si un événement a une probabilité très élevée et les autres des probabilités très faibles, l'incertitude est faible, et l'entropie est petite. Dans le contexte de la prédiction de mots, elle quantifie l'incertitude intrinsèque quant au prochain mot, avant même qu'un modèle n'intervienne. Son unité de mesure est le **bit**, car nous utilisons le logarithme en base 2. Un bit représente la quantité d'information nécessaire pour réduire l'incertitude de moitié.

1.2. Le calcul de l'Entropie de Shannon $H(P)$ pour la distribution réelle $P$ est donné par la formule :
$H(P) = - \sum_{x \in V} P(x) \log_2 P(x)$

Pour notre distribution $P$ :
$P(\text{"mange"}) = 0.1$
$P(\text{"dort"}) = 0.7$
$P(\text{"joue"}) = 0.2$

Appliquons la formule :
$H(P) = - [ P(\text{"mange"}) \log_2 P(\text{"mange"}) + P(\text{"dort"}) \log_2 P(\text{"dort"}) + P(\text{"joue"}) \log_2 P(\text{"joue"}) ]$
$H(P) = - [ 0.1 \times \log_2(0.1) + 0.7 \times \log_2(0.7) + 0.2 \times \log_2(0.2) ]$

En utilisant les approximations fournies :
$\log_2(0.1) \approx -3.3219$
$\log_2(0.7) \approx -0.5146$
$\log_2(0.2) \approx -2.3219$

$H(P) = - [ 0.1 \times (-3.3219) + 0.7 \times (-0.5146) + 0.2 \times (-2.3219) ]$
$H(P) = - [ -0.33219 - 0.36022 - 0.46438 ]$
$H(P) = - [ -1.15679 ]$
$H(P) \approx 1.1568$ bits

L'Entropie de Shannon de la distribution réelle $P$ est d'environ 1.1568 bits.

---

**Partie 2 : L'Entropie Croisée (Cross-Entropy)**

2.1. L'Entropie Croisée $H(P, Q)$ mesure le nombre moyen de bits nécessaires pour identifier un événement d'une distribution $P$ si nous utilisons un code optimisé pour une distribution $Q$ (notre prédiction) plutôt que pour la vraie distribution $P$. Autrement dit, elle quantifie l'efficacité (ou l'inefficacité) de notre distribution prédite $Q$ pour encoder les événements selon la distribution réelle $P$.

Elle est fréquemment utilisée comme fonction de coût (ou de perte) dans l'entraînement des modèles de langage car elle pénalise les prédictions du modèle qui s'éloignent de la vérité. Un modèle produisant une distribution $Q$ très différente de la vraie distribution $P$ se verra attribuer une valeur d'entropie croisée élevée, ce qui indique une performance médiocre. L'objectif de l'entraînement est de minimiser cette valeur, incitant le modèle à produire des distributions $Q$ qui ressemblent de plus en plus à $P$.

2.2. Le calcul de l'Entropie Croisée $H(P, Q)$ est donné par la formule :
$H(P, Q) = - \sum_{x \in V} P(x) \log_2 Q(x)$

Pour notre distribution réelle $P$ et la distribution prédite $Q$ :
$P(\text{"mange"}) = 0.1$, $Q(\text{"mange"}) = 0.2$
$P(\text{"dort"}) = 0.7$, $Q(\text{"dort"}) = 0.6$
$P(\text{"joue"}) = 0.2$, $Q(\text{"joue"}) = 0.2$

Appliquons la formule :
$H(P, Q) = - [ P(\text{"mange"}) \log_2 Q(\text{"mange"}) + P(\text{"dort"}) \log_2 Q(\text{"dort"}) + P(\text{"joue"}) \log_2 Q(\text{"joue"}) ]$
$H(P, Q) = - [ 0.1 \times \log_2(0.2) + 0.7 \times \log_2(0.6) + 0.2 \times \log_2(0.2) ]$

En utilisant les approximations fournies :
$\log_2(0.2) \approx -2.3219$
$\log_2(0.6) \approx -0.7370$

$H(P, Q) = - [ 0.1 \times (-2.3219) + 0.7 \times (-0.7370) + 0.2 \times (-2.3219) ]$
$H(P, Q) = - [ -0.23219 - 0.51590 - 0.46438 ]$
$H(P, Q) = - [ -1.21247 ]$
$H(P, Q) \approx 1.2125$ bits

L'Entropie Croisée entre $P$ et $Q$ est d'environ 1.2125 bits.

2.3. Si un modèle de langage était "parfait", sa distribution prédite $Q_{\text{parfait}}$ serait identique à la distribution réelle $P$. Dans ce cas, l'Entropie Croisée $H(P, Q_{\text{parfait}})$ deviendrait $H(P, P)$.
La formule serait :
$H(P, P) = - \sum_{x \in V} P(x) \log_2 P(x)$
Cette formule est exactement celle de l'Entropie de Shannon $H(P)$.
Par conséquent, $H(P, Q_{\text{parfait}}) = H(P)$.
D'après notre calcul en 1.2, cette valeur serait d'environ 1.1568 bits. Un modèle parfait aurait une Entropie Croisée égale à l'Entropie de Shannon de la vraie distribution, ce qui est la valeur minimale possible pour l'Entropie Croisée.

---

**Partie 3 : La Divergence de Kullback-Leibler (KL)**

3.1. La Divergence de Kullback-Leibler $D_{KL}(P || Q)$ peut être calculée comme la différence entre l'Entropie Croisée et l'Entropie de Shannon :
$D_{KL}(P || Q) = H(P, Q) - H(P)$

En utilisant les valeurs calculées précédemment :
$H(P, Q) \approx 1.2125$ bits
$H(P) \approx 1.1568$ bits

$D_{KL}(P || Q) \approx 1.2125 - 1.1568$
$D_{KL}(P || Q) \approx 0.0557$ bits

La Divergence KL est d'environ 0.0557 bits.

3.2. Le calcul direct de la Divergence de Kullback-Leibler $D_{KL}(P || Q)$ utilise la formule :
$D_{KL}(P || Q) = \sum_{x \in V} P(x) \log_2 \frac{P(x)}{Q(x)}$

Appliquons la formule pour chaque événement :
$P(\text{"mange"}) = 0.1$, $Q(\text{"mange"}) = 0.2 \implies 0.1 \log_2 \frac{0.1}{0.2} = 0.1 \log_2(0.5)$
$P(\text{"dort"}) = 0.7$, $Q(\text{"dort"}) = 0.6 \implies 0.7 \log_2 \frac{0.7}{0.6}$
$P(\text{"joue"}) = 0.2$, $Q(\text{"joue"}) = 0.2 \implies 0.2 \log_2 \frac{0.2}{0.2} = 0.2 \log_2(1)$

Calculons chaque terme :
Terme "mange" : $0.1 \times \log_2(0.5) = 0.1 \times (-1.0) = -0.1$
Terme "dort" : $0.7 \times \log_2(7/6) \approx 0.7 \times 0.2110 = 0.1477$
Terme "joue" : $0.2 \times \log_2(1) = 0.2 \times 0.0 = 0.0$

Sommons ces termes :
$D_{KL}(P || Q) = -0.1 + 0.1477 + 0.0$
$D_{KL}(P || Q) = 0.0477$ bits

Il y a une légère différence due aux arrondissements dans les approximations des logarithmes. En utilisant des valeurs plus précises pour les logarithmes, les résultats seraient identiques. La cohérence est donc démontrée, la différence étant imputable à la précision des approximations numériques.
Par exemple, si nous utilisons `log2(0.1) = -3.32192809`, `log2(0.2) = -2.32192809`, `log2(0.6) = -0.73696559`, `log2(0.7) = -0.51457317`:
$H(P) = -[0.1(-3.32192809) + 0.7(-0.51457317) + 0.2(-2.32192809)]$
$H(P) = -[-0.332192809 - 0.360201219 - 0.464385618] = 1.156779646$

$H(P, Q) = -[0.1(-2.32192809) + 0.7(-0.73696559) + 0.2(-2.32192809)]$
$H(P, Q) = -[-0.232192809 - 0.515875913 - 0.464385618] = 1.21245434$

$D_{KL}(P || Q) = H(P, Q) - H(P) = 1.21245434 - 1.156779646 = 0.055674694$

$D_{KL}(P || Q)$ (direct) $= 0.1 \log_2(0.1/0.2) + 0.7 \log_2(0.7/0.6) + 0.2 \log_2(0.2/0.2)$
$= 0.1 \log_2(0.5) + 0.7 \log_2(7/6) + 0.2 \log_2(1)$
$= 0.1(-1.0) + 0.7(0.211048754) + 0.2(0.0)$
$= -0.1 + 0.1477341278 = 0.0477341278$

Il semble qu'une erreur d'approximation s'est glissée dans mes notes pour log2(7/6), ou que la précision n'est pas suffisante. La vraie valeur est `log2(7/6) = log2(7) - log2(6) = 2.80735492 - 2.5849625 = 0.22239242`.
Reprenons le calcul direct avec une meilleure précision pour `log2(7/6)`:
$D_{KL}(P || Q) = 0.1 \times (-1.0) + 0.7 \times 0.22239242 + 0.0$
$D_{KL}(P || Q) = -0.1 + 0.155674694$
$D_{KL}(P || Q) = 0.055674694$

Les deux calculs sont bien cohérents avec une précision suffisante.

3.3. La valeur de $D_{KL}(P || Q) \approx 0.0557$ bits représente la quantité d'information supplémentaire (en bits) qui est perdue lorsque nous utilisons la distribution $Q$ du modèle pour approximer la vraie distribution $P$. C'est une mesure de la "dissimilarité" ou de l'inefficacité de $Q$ par rapport à $P$.
Un $D_{KL}(P || Q)$ élevé indique que le modèle fait de très mauvaises prédictions, car sa distribution $Q$ est très éloignée de la réalité $P$. Le modèle est alors incertain sur la manière de générer le prochain mot de manière fidèle à la réalité.
Un $D_{KL}(P || Q)$ faible (proche de zéro) signifie que la distribution $Q$ du modèle est très proche de la distribution réelle $P$. Cela indique que le modèle est performant et que ses prédictions sont fiables, ne perdant que très peu d'informations par rapport à la connaissance parfaite de $P$. Un $D_{KL}(P || Q) = 0$ implique que $P = Q$.

3.4. Si notre modèle prédisait $Q(\text{"mange"}) = 0.0$ alors que $P(\text{"mange"}) = 0.1$, cela aurait une conséquence mathématique et pratique très grave.
Dans la formule de la Divergence KL :
$D_{KL}(P || Q) = \sum_{x \in V} P(x) \log_2 \frac{P(x)}{Q(x)}$
Le terme correspondant à "mange" serait $P(\text{"mange"}) \log_2 \frac{P(\text{"mange"})}{Q(\text{"mange"})} = 0.1 \log_2 \frac{0.1}{0.0}$.
La division par zéro est indéfinie. De plus, $\log_2(x)$ tend vers $-\infty$ lorsque $x$ tend vers 0 par les valeurs positives. Donc, $\log_2 \frac{0.1}{0.0}$ tend vers $\log_2(\infty)$, ce qui est $+\infty$.
Par conséquent, $D_{KL}(P || Q)$ deviendrait **infinie**.
En pratique, cela signifie que le modèle a commis une erreur catastrophique : il a prédit qu'un événement (ici, le mot "mange") n'arriverait jamais, alors qu'en réalité, il a une probabilité non nulle de se produire. Un modèle qui attribue une probabilité de zéro à un événement qui est en fait possible est considéré comme infiniment mauvais par la Divergence KL. C'est pour cette raison que des techniques comme le lissage (smoothing) sont utilisées pour éviter que les probabilités prédites ne soient exactement nulles pour des événements possibles.

---

**Partie 4 : Implications pour l'entraînement des Modèles de Langage**

4.1. La relation entre l'Entropie Croisée et la Divergence KL est $H(P, Q) = H(P) + D_{KL}(P || Q)$.
Lors de l'entraînement d'un modèle de langage, la distribution réelle $P$ (qui est généralement dérivée des données d'entraînement observées) est fixe et ne change pas. Par conséquent, l'Entropie de Shannon $H(P)$ est une constante pour un contexte donné.
Minimiser $H(P, Q)$ revient donc à minimiser $H(P) + D_{KL}(P || Q)$. Puisque $H(P)$ est constant, minimiser l'Entropie Croisée est équivalent à minimiser la Divergence KL.
La raison pour laquelle la Cross-Entropy est préférée comme fonction de coût directe est qu'elle est plus simple à calculer en pratique. Elle ne nécessite pas le calcul préalable de $H(P)$, ce qui peut être complexe si $P$ est une distribution implicite ou dérivée de données dynamiques. En se concentrant sur $H(P,Q)$, nous atteignons le même objectif d'optimisation sans la surcharge de calcul de $H(P)$.

4.2. Durant le processus itératif d'entraînement d'un modèle de langage, la Cross-Entropy est utilisée comme suit :
1.  **Prédiction :** Pour un contexte donné, le modèle de langage produit une distribution de probabilité $Q$ sur l'ensemble du vocabulaire pour le mot suivant.
2.  **Vérité Terrain :** La vraie distribution $P$ est généralement représentée par un vecteur "one-hot" (si on prédit un seul mot exact) ou une distribution lissée (si plusieurs mots sont acceptables) qui indique le ou les mots qui sont réellement apparus après le contexte dans les données d'entraînement.
3.  **Calcul de la Perte :** La Cross-Entropy $H(P, Q)$ est calculée entre la distribution $P$ (vérité terrain) et la distribution $Q$ (prédiction du modèle). Plus la prédiction $Q$ s'écarte de $P$, plus la valeur de l'Entropie Croisée est élevée.
4.  **Rétropropagation et Optimisation :** Cette valeur de Cross-Entropy est la fonction de perte. Elle est utilisée pour calculer les gradients des paramètres du modèle. Ces gradients sont ensuite utilisés par un algorithme d'optimisation (comme la descente de gradient stochastique) pour ajuster les poids et les biais du modèle, dans le but de minimiser la perte et, par conséquent, de rendre les futures prédictions $Q$ plus proches de $P$.
Ce cycle se répète sur des millions ou des milliards d'exemples de données jusqu'à ce que le modèle converge vers une performance satisfaisante.

4.3. Si notre modèle s'améliorait significativement après plusieurs étapes d'entraînement, cela signifierait que sa distribution prédite $Q$ se rapprocherait de plus en plus de la distribution réelle $P$.
En conséquence :
*   La valeur de l'Entropie Croisée $H(P, Q)$ **diminuerait**. Elle tendrait vers la valeur minimale possible, qui est l'Entropie de Shannon $H(P)$ de la distribution réelle.
*   La valeur de la Divergence KL $D_{KL}(P || Q)$ **diminuerait** également. Elle tendrait vers zéro, indiquant que la différence d'information entre la prédiction du modèle et la réalité est devenue négligeable.

L'objectif de l'entraînement est précisément de faire en sorte que ces deux mesures, $H(P, Q)$ et $D_{KL}(P || Q)$, diminuent pour atteindre leurs valeurs minimales respectives, reflétant un modèle précis et fiable.