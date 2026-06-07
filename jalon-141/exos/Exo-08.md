# Exercice 8 : Convergence d'une classe finie
**Énoncé :** Soit $\mathcal{H}$ une classe finie de fonctions contenant $M$ fonctions : $\mathcal{H} = \{h_1, \dots, h_M\}$. Prouver sans utiliser le théorème de Vapnik-Chervonenkis que $\mathcal{H}$ est une classe de Glivenko-Cantelli universelle.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On a une classe finie. On peut combiner la borne de Hoeffding et l'union bound pour prouver la convergence uniforme presque sûre.
* *Résolution pas-à-pas :*
  1. Fixons un $\epsilon > 0$. On s'intéresse à la probabilité de déviation uniforme :
     $$ \mathbb{P}\left(\sup_{h \in \mathcal{H}} |R_n(h) - R(h)| \ge \epsilon\right) = \mathbb{P}\left(\max_{j \in \{1, \dots, M\}} |R_n(h_j) - R(h_j)| \ge \epsilon\right) $$
  2. Par l'inégalité de l'union (Boole) :
     $$ \mathbb{P}\left(\max_{j} |R_n(h_j) - R(h_j)| \ge \epsilon\right) \le \sum_{j=1}^M \mathbb{P}(|R_n(h_j) - R(h_j)| \ge \epsilon) $$
  3. Par l'inégalité de Hoeffding, pour une fonction $h_j$ donnée à valeurs dans $\{0, 1\}$ :
     $$ \mathbb{P}(|R_n(h_j) - R(h_j)| \ge \epsilon) \le 2 \exp(-2 n \epsilon^2) $$
  4. En substituant dans la somme :
     $$ \mathbb{P}\left(\sup_{h \in \mathcal{H}} |R_n(h) - R(h)| \ge \epsilon\right) \le \sum_{j=1}^M 2 \exp(-2 n \epsilon^2) = 2 M \exp(-2 n \epsilon^2) $$
  5. Appelons cet événement de déviation $A_n(\epsilon)$. Étudions la série :
     $$ \sum_{n=1}^\infty \mathbb{P}(A_n(\epsilon)) \le \sum_{n=1}^\infty 2 M (e^{-2\epsilon^2})^n $$
  6. C'est une série géométrique de raison $q = e^{-2\epsilon^2}$. Puisque $\epsilon > 0$, $0 < q < 1$.
  7. La série géométrique converge donc.
  8. D'après le lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n(\epsilon)) = 0$. Donc presque sûrement, il existe un rang à partir duquel $\sup_h |R_n(h) - R(h)| < \epsilon$.
  9. En prenant une suite $\epsilon_k = 1/k$ (dénombrable), on conclut que la limite du sup est 0 presque sûrement, quelle que soit la distribution $\mathcal{P}$.
