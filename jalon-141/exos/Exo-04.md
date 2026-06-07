# Exercice 4 : Classe de Glivenko-Cantelli unitaire
**Énoncé :** Soit $\mathcal{H} = \{h_0\}$ une classe de fonctions contenant une unique fonction mesurable $h_0: \mathcal{Z} \to \{0, 1\}$. Montrer que $\mathcal{H}$ est une classe de Glivenko-Cantelli universelle.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit revenir à la définition de base d'une classe de Glivenko-Cantelli, en considérant le cas le plus simple possible : un ensemble contenant un seul élément.
* *Résolution pas-à-pas :*
  1. Par définition, nous devons montrer que pour toute distribution $\mathcal{P}$ :
     $$\lim_{n \to \infty} \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| = 0 \quad \text{presque sûrement.}$$
  2. Puisque la classe ne contient que la fonction $h_0$, le supremum sur $\mathcal{H}$ se réduit à l'évaluation en $h_0$ :
     $$\sup_{h \in \mathcal{H}} |R_n(h) - R(h)| = |R_n(h_0) - R(h_0)|$$
  3. Rappelons les définitions pour $h_0$ :
     - $R(h_0) = \mathbb{E}_{Z \sim \mathcal{P}}[h_0(Z)]$
     - $R_n(h_0) = \frac{1}{n} \sum_{i=1}^n h_0(Z_i)$
  4. Les variables aléatoires $Y_i = h_0(Z_i)$ sont indépendantes, identiquement distribuées, et possèdent une espérance finie $\mathbb{E}[Y_1] = R(h_0)$ (car elles sont bornées entre 0 et 1).
  5. Par conséquent, on peut appliquer la Loi Forte des Grands Nombres de Kolmogorov à la suite $(Y_i)_{i \ge 1}$.
  6. La Loi Forte affirme que la moyenne empirique converge vers l'espérance mathématique presque sûrement :
     $$\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n Y_i = \mathbb{E}[Y_1] \quad \text{p.s.}$$
  7. En remplaçant par nos notations :
     $$\lim_{n \to \infty} R_n(h_0) = R(h_0) \quad \text{p.s.}$$
  8. Ce qui équivaut exactement à :
     $$\lim_{n \to \infty} |R_n(h_0) - R(h_0)| = 0 \quad \text{p.s.}$$
  9. La condition de Glivenko-Cantelli est donc satisfaite pour toute distribution $\mathcal{P}$. $\mathcal{H}$ est bien une classe de Glivenko-Cantelli universelle.
