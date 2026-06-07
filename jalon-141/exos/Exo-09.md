# Exercice 9 : Propriété de stabilité par passage au complémentaire
**Énoncé :** Soit $\mathcal{H}$ une classe de Glivenko-Cantelli universelle. Soit $\bar{\mathcal{H}} = \{1 - h \mid h \in \mathcal{H}\}$ la classe des fonctions complémentaires. Montrer que $\bar{\mathcal{H}}$ est aussi une classe de Glivenko-Cantelli universelle.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit analyser la déviation empirique pour une fonction complémentaire $\bar{h} = 1 - h$.
* *Résolution pas-à-pas :*
  1. Pour toute fonction $\bar{h} \in \bar{\mathcal{H}}$, il existe une fonction $h \in \mathcal{H}$ telle que $\bar{h}(x) = 1 - h(x)$.
  2. Évaluons le risque réel de $\bar{h}$ :
     $$ R(\bar{h}) = \mathbb{E}[\bar{h}(Z)] = \mathbb{E}[1 - h(Z)] = 1 - \mathbb{E}[h(Z)] = 1 - R(h) $$
  3. Évaluons le risque empirique de $\bar{h}$ :
     $$ R_n(\bar{h}) = \frac{1}{n} \sum_{i=1}^n \bar{h}(Z_i) = \frac{1}{n} \sum_{i=1}^n (1 - h(Z_i)) = 1 - \frac{1}{n} \sum_{i=1}^n h(Z_i) = 1 - R_n(h) $$
  4. Calculons l'écart entre risque empirique et réel pour $\bar{h}$ :
     $$ R_n(\bar{h}) - R(\bar{h}) = (1 - R_n(h)) - (1 - R(h)) = - (R_n(h) - R(h)) $$
  5. En prenant la valeur absolue :
     $$ |R_n(\bar{h}) - R(\bar{h})| = |-(R_n(h) - R(h))| = |R_n(h) - R(h)| $$
  6. Considérons maintenant le supremum sur l'ensemble de la classe $\bar{\mathcal{H}}$ :
     $$ \sup_{\bar{h} \in \bar{\mathcal{H}}} |R_n(\bar{h}) - R(\bar{h})| = \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| $$
  7. Or, puisque $\mathcal{H}$ est une classe de Glivenko-Cantelli universelle, on sait que pour toute distribution $\mathcal{P}$ :
     $$ \lim_{n \to \infty} \sup_{h \in \mathcal{H}} |R_n(h) - R(h)| = 0 \quad \text{p.s.} $$
  8. Par subsitution directe (égalité stricte à la ligne 6) :
     $$ \lim_{n \to \infty} \sup_{\bar{h} \in \bar{\mathcal{H}}} |R_n(\bar{h}) - R(\bar{h})| = 0 \quad \text{p.s.} $$
  9. La classe $\bar{\mathcal{H}}$ est donc bien une classe de Glivenko-Cantelli universelle.
