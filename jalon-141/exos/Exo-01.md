# Exercice 1 : Convergence de la mesure empirique
**Énoncé :** Démontrer, sans ellipse, que pour tout ensemble mesurable $A$ fixé, la probabilité empirique $P_n(A) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}_{Z_i \in A}$ converge presque sûrement vers $P(A)$.
**Correction Détaillée :**
* *Analyse de l'énoncé :* La classe de fonction $\mathcal{F}$ est le singleton $\{ \mathbb{I}_A \}$.
* *Résolution pas-à-pas :*
Soit $Z_1, Z_2, \dots, Z_n$ des variables aléatoires indépendantes et identiquement distribuées selon la probabilité $P$. Posons $X_i = \mathbb{I}_{Z_i \in A}$.
Par définition de l'espérance de la fonction indicatrice :
$$\mathbb{E}[X_i] = \mathbb{E}[\mathbb{I}_{Z_i \in A}] = 1 \cdot P(Z_i \in A) + 0 \cdot P(Z_i \notin A) = P(A)$$
Puisque les $Z_i$ sont i.i.d., les $X_i$ sont également des variables aléatoires i.i.d. bornées (à valeurs dans $\{0, 1\}$). L'espérance $\mathbb{E}[X_i]$ est finie.
En appliquant la loi forte des grands nombres de Kolmogorov :
$$P_n(A) = \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{n \to \infty} \mathbb{E}[X_1] = P(A) \quad \text{presque sûrement.}$$
La convergence de l'erreur empirique vers l'erreur vraie pour un concept unique est donc établie. $\blacksquare$
