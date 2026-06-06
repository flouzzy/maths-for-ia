# Exercice 10 : L'erreur d'approximation et d'estimation (ENS)
**Énoncé :** Soit un espace d'hypothèses complet $\mathcal{H}$ et le minimiseur du risque théorique $h^* = \arg\min_{h \in \mathcal{H}} R(h)$. Soit une sous-classe $\mathcal{H}_d \subset \mathcal{H}$ de dimension VC $d$. On pose $\hat{h}_n = \arg\min_{h \in \mathcal{H}_d} \hat{R}_n(h)$ (le minimiseur du risque empirique) et $\tilde{h} = \arg\min_{h \in \mathcal{H}_d} R(h)$ (le meilleur dans la classe).
Décomposer rigoureusement l'excès de risque $R(\hat{h}_n) - R(h^*)$.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Effectuer la décomposition Biais-Variance algorithmique.
* *Résolution pas-à-pas :*
L'excès de risque est la différence entre la performance du modèle entraîné et la performance idéale atteignable dans $\mathcal{H}$.
Ajoutons et soustrayons le risque du meilleur modèle de la sous-classe $\tilde{h}$ :
$$R(\hat{h}_n) - R(h^*) = \underbrace{(R(\hat{h}_n) - R(\tilde{h}))}_{\text{Erreur d'estimation}} + \underbrace{(R(\tilde{h}) - R(h^*))}_{\text{Erreur d'approximation}}$$
1. L'**Erreur d'approximation** ne dépend pas des données d'entraînement. Elle mesure l'incapacité de la classe restreinte $\mathcal{H}_d$ à contenir la fonction optimale $h^*$. Elle décroît si on augmente la capacité $d$ de la classe.
2. L'**Erreur d'estimation** dépend des données. Nous pouvons la borner par l'uniforme convergence.
On remarque que $R(\hat{h}_n) - R(\tilde{h}) = R(\hat{h}_n) - \hat{R}_n(\hat{h}_n) + \hat{R}_n(\hat{h}_n) - \hat{R}_n(\tilde{h}) + \hat{R}_n(\tilde{h}) - R(\tilde{h})$.
Puisque $\hat{h}_n$ minimise $\hat{R}_n$ sur $\mathcal{H}_d$, $\hat{R}_n(\hat{h}_n) - \hat{R}_n(\tilde{h}) \le 0$.
Donc :
$$R(\hat{h}_n) - R(\tilde{h}) \le (R(\hat{h}_n) - \hat{R}_n(\hat{h}_n)) + (\hat{R}_n(\tilde{h}) - R(\tilde{h}))$$
Chaque terme est majoré par le supremum de l'écart absolu sur toute la classe :
$$R(\hat{h}_n) - R(\tilde{h}) \le 2 \sup_{h \in \mathcal{H}_d} |R(h) - \hat{R}_n(h)|$$
D'après le théorème de Vapnik-Chervonenkis, avec probabilité $1-\delta$, ce supremum est borné par un terme en $O\left(\sqrt{\frac{d \log(n/d) + \log(1/\delta)}{n}}\right)$.
L'erreur d'estimation augmente avec $d$ et diminue avec $n$. Le compromis fondamental (bias-variance tradeoff) requiert de choisir un $d$ optimal pour minimiser la somme totale. $\blacksquare$
