# Exercice 7 : Unicité sur une sous-classe (Théorème $\pi-\lambda$) (★★★★☆)

**Énoncé :**
Montrer que la mesure produit $\mu_1 \otimes \mu_2$ est définie de manière unique sur $\mathcal{F}_1 \otimes \mathcal{F}_2$ à partir de ses valeurs sur les rectangles $A \times B$ dans le cas où les mesures $\mu_1$ et $\mu_2$ sont finies. (On redétaillera la preuve en s'assurant de bien justifier chaque axiome du $\lambda$-système).

**Correction :**
Soit $\pi_1$ et $\pi_2$ deux mesures finies sur $\mathcal{F} = \mathcal{F}_1 \otimes \mathcal{F}_2$ qui coïncident sur la famille des rectangles $\mathcal{R} = \{A_1 \times A_2 \mid A_1 \in \mathcal{F}_1, A_2 \in \mathcal{F}_2\}$.
Posons $\mathcal{L} = \{E \in \mathcal{F} \mid \pi_1(E) = \pi_2(E)\}$.
Montrons que $\mathcal{L}$ est un $\lambda$-système (système de Dynkin).
1. **L'espace total :** $X = X_1 \times X_2$ est un rectangle (car $X_1 \in \mathcal{F}_1, X_2 \in \mathcal{F}_2$). Donc $X \in \mathcal{R} \subset \mathcal{L}$.
2. **Stabilité par complémentation :** Soit $E \in \mathcal{L}$.
   $\pi_1(E^c) = \pi_1(X) - \pi_1(E)$ (licite car les mesures sont finies, aucune forme $\infty - \infty$).
   Comme $\pi_1(X) = \pi_2(X)$ et $\pi_1(E) = \pi_2(E)$, alors $\pi_1(E^c) = \pi_2(X) - \pi_2(E) = \pi_2(E^c)$.
   Donc $E^c \in \mathcal{L}$.
3. **Stabilité par union dénombrable disjointe :** Soit $(E_n)_{n \geq 1}$ une suite d'ensembles de $\mathcal{L}$ deux à deux disjoints.
   Soit $E = \bigcup_{n \geq 1} E_n$.
   Par $\sigma$-additivité des mesures $\pi_1$ et $\pi_2$, on a :
   $\pi_1(E) = \sum_{n=1}^\infty \pi_1(E_n) = \sum_{n=1}^\infty \pi_2(E_n) = \pi_2(E)$ (car $E_n \in \mathcal{L}$).
   Donc $E \in \mathcal{L}$.

$\mathcal{L}$ est bien un $\lambda$-système. De plus, il contient $\mathcal{R}$.
Or $\mathcal{R}$ est un $\pi$-système (stable par intersection finie).
Le théorème de Dynkin énonce que si un $\lambda$-système contient un $\pi$-système, alors il contient la tribu engendrée par ce $\pi$-système.
Donc $\sigma(\mathcal{R}) \subset \mathcal{L}$.
Mais $\sigma(\mathcal{R}) = \mathcal{F}_1 \otimes \mathcal{F}_2$.
Conclusion : pour tout $E \in \mathcal{F}_1 \otimes \mathcal{F}_2$, $\pi_1(E) = \pi_2(E)$, les deux mesures sont bien identiques sur toute la tribu produit.
