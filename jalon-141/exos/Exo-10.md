# Exercice 10 : Non-apprenabilité d'une classe de VC-dimension infinie
**Énoncé :** Soit $\mathcal{X} = \mathbb{R}$. Soit $\mathcal{H}$ la classe des fonctions caractéristiques de tous les sous-ensembles finis de $\mathbb{R}$. Montrer que la dimension VC de $\mathcal{H}$ est infinie, puis construire explicitement une distribution de probabilité sur $\mathbb{R}$ pour laquelle $\mathcal{H}$ n'est pas une classe de Glivenko-Cantelli.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On démontre que le théorème de VC est une condition nécessaire. On doit d'abord prouver VCdim = $\infty$, puis trouver une "mauvaise" distribution continue.
* *Résolution pas-à-pas :*
  1. **Étape 1 : Dimension VC de $\mathcal{H}$**
     - Soit $n \in \mathbb{N}^*$ quelconque. Prenons n'importe quel ensemble $S = \{x_1, \dots, x_n\}$ de $n$ points distincts dans $\mathbb{R}$.
     - Pour tout sous-ensemble $A \subseteq S$, l'ensemble $A$ est lui-même un sous-ensemble fini de $\mathbb{R}$.
     - Donc la fonction caractéristique $h_A(x) = \mathbb{I}_{x \in A}$ appartient à la classe $\mathcal{H}$.
     - Cette fonction attribue 1 à tous les points de $A$ et 0 aux autres points de $S$.
     - On a donc réalisé tous les étiquetages possibles. $S$ est éclaté.
     - Comme c'est vrai pour tout $n$, $\text{VCdim}(\mathcal{H}) = \infty$.
  2. **Étape 2 : Construction de la distribution**
     - Soit $\mathcal{P}$ une loi continue sur $\mathbb{R}$, par exemple la loi uniforme sur $[0, 1]$.
     - Propriété d'une loi continue : la probabilité de tout ensemble fini de points est nulle.
     - Pour toute fonction $h \in \mathcal{H}$, $h$ est l'indicatrice d'un ensemble fini $E_h$.
     - Donc, le risque réel (espérance) est : $R(h) = \mathbb{P}(Z \in E_h) = 0$.
     - Et ceci est vrai pour toutes les fonctions de la classe : $\sup_{h \in \mathcal{H}} R(h) = 0$.
  3. **Étape 3 : Calcul du risque empirique**
     - Soit un échantillon aléatoire $Z_1, \dots, Z_n$ tiré selon la loi uniforme.
     - Considérons l'ensemble $E_{emp} = \{Z_1, \dots, Z_n\}$. C'est un ensemble fini.
     - Donc la fonction $h_{emp}(x) = \mathbb{I}_{x \in E_{emp}}$ appartient à la classe $\mathcal{H}$.
     - Évaluons le risque empirique de $h_{emp}$ :
       $$ R_n(h_{emp}) = \frac{1}{n} \sum_{i=1}^n h_{emp}(Z_i) = \frac{1}{n} \sum_{i=1}^n 1 = 1 $$
     - Or $h_{emp} \in \mathcal{H}$, donc le supremum du risque empirique sur la classe est au moins égal à 1 :
       $$ \sup_{h \in \mathcal{H}} R_n(h) \ge 1 $$
     - Comme le risque maximum est 1, on a $\sup_{h \in \mathcal{H}} R_n(h) = 1$.
  4. **Conclusion sur la non-convergence**
     - La déviation uniforme s'écrit :
       $$ \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| $$
     - En choisissant $h = h_{emp}$, on obtient $|R_n(h_{emp}) - R(h_{emp})| = |1 - 0| = 1$.
     - Donc $\sup_{h \in \mathcal{H}} |R_n(h) - R(h)| = 1$ pour tout $n$.
     - La limite quand $n \to \infty$ de la déviation maximale ne tend pas vers 0, elle vaut constamment 1.
     - Ainsi, $\mathcal{H}$ n'est pas une classe de Glivenko-Cantelli pour la loi uniforme continue.
