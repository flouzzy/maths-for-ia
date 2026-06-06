---
uuid: "jalon-140-exo-01"
title: "Exercice 1 - Jalon 140"
---
# Exercice 1 : Détermination du Classifieur de Bayes Optimal pour des Distributions Uniformes
**Difficulté:** ★

## Énoncé
Considérons un problème de classification binaire où la variable de classe Y peut prendre les valeurs 0 ou 1. Nous disposons d'une unique variable explicative continue X.
Les probabilités a priori des classes sont données par :
P(Y=0) = 0.6
P(Y=1) = 0.4

Les fonctions de densité de probabilité conditionnelles p(x|Y) sont définies comme suit :
Pour la classe Y=0 : p(x|Y=0) est une distribution uniforme sur l'intervalle [0, 1].
C'est-à-dire, p(x|Y=0) = 1 si x ∈ [0, 1], et p(x|Y=0) = 0 sinon.

Pour la classe Y=1 : p(x|Y=1) est une distribution uniforme sur l'intervalle [0.5, 1.5].
C'est-à-dire, p(x|Y=1) = 1 si x ∈ [0.5, 1.5], et p(x|Y=1) = 0 sinon.

Déterminez la règle de décision du classifieur de Bayes optimal pour ce problème. La règle de décision doit spécifier à quelle classe (0 ou 1) une observation x est assignée pour chaque valeur possible de x.

## Correction Pas-à-Pas
Le classifieur de Bayes optimal minimise le taux d'erreur de classification. Il assigne une observation x à la classe k qui maximise la probabilité a posteriori P(Y=k|X=x).
Selon le théorème de Bayes, la probabilité a posteriori est donnée par :
P(Y=k|X=x) = [p(x|Y=k) * P(Y=k)] / p(x)

Pour un problème de classification binaire entre la classe 0 et la classe 1, le classifieur de Bayes compare P(Y=0|X=x) et P(Y=1|X=x).
Puisque le terme p(x) est le même pour toutes les classes et est strictement positif pour les valeurs de x où au moins une densité conditionnelle est non nulle, la règle de décision équivalente est d'assigner x à la classe k qui maximise le produit p(x|Y=k) * P(Y=k).

Calculons ces produits pour chaque classe :
Pour la classe Y=0, le produit est :
p(x|Y=0) * P(Y=0)

Pour la classe Y=1, le produit est :
p(x|Y=1) * P(Y=1)

Nous devons analyser ces produits sur les différentes régions de l'espace des caractéristiques X.
Les supports des distributions sont [0, 1] pour Y=0 et [0.5, 1.5] pour Y=1.
Nous allons considérer les intervalles pertinents sur l'axe des réels, formés par l'union et l'intersection de ces supports.

**Cas 1 : x < 0**
Dans cet intervalle :
p(x|Y=0) = 0 (car x n'est pas dans [0, 1])
p(x|Y=1) = 0 (car x n'est pas dans [0.5, 1.5])
Calcul des produits :
p(x|Y=0) * P(Y=0) = 0 * 0.6 = 0
p(x|Y=1) * P(Y=1) = 0 * 0.4 = 0
Pour ces valeurs de x, aucune des classes n'est supportée par les distributions données. Le classifieur ne peut pas prendre de décision basée sur ces modèles. Nous supposons que les observations x se situeront dans l'union des supports, c'est-à-dire dans [0, 1.5].

**Cas 2 : x ∈ [0, 0.5)**
Dans cet intervalle :
p(x|Y=0) = 1 (car x est dans [0, 1])
p(x|Y=1) = 0 (car x n'est pas dans [0.5, 1.5])
Calcul des produits :
p(x|Y=0) * P(Y=0) = 1 * 0.6 = 0.6
p(x|Y=1) * P(Y=1) = 0 * 0.4 = 0
Comparaison des produits : 0.6 > 0
Conclusion : Pour x ∈ [0, 0.5), le classifieur de Bayes assigne x à la classe Y=0.

**Cas 3 : x ∈ [0.5, 1]**
Dans cet intervalle :
p(x|Y=0) = 1 (car x est dans [0, 1])
p(x|Y=1) = 1 (car x est dans [0.5, 1.5])
Calcul des produits :
p(x|Y=0) * P(Y=0) = 1 * 0.6 = 0.6
p(x|Y=1) * P(Y=1) = 1 * 0.4 = 0.4
Comparaison des produits : 0.6 > 0.4
Conclusion : Pour x ∈ [0.5, 1], le classifieur de Bayes assigne x à la classe Y=0.

**Cas 4 : x ∈ (1, 1.5]**
Dans cet intervalle :
p(x|Y=0) = 0 (car x n'est pas dans [0, 1])
p(x|Y=1) = 1 (car x est dans [0.5, 1.5])
Calcul des produits :
p(x|Y=0) * P(Y=0) = 0 * 0.6 = 0
p(x|Y=1) * P(Y=1) = 1 * 0.4 = 0.4
Comparaison des produits : 0.4 > 0
Conclusion : Pour x ∈ (1, 1.5], le classifieur de Bayes assigne x à la classe Y=1.

**Cas 5 : x > 1.5**
Dans cet intervalle :
p(x|Y=0) = 0 (car x n'est pas dans [0, 1])
p(x|Y=1) = 0 (car x n'est pas dans [0.5, 1.5])
Calcul des produits :
p(x|Y=0) * P(Y=0) = 0 * 0.6 = 0
p(x|Y=1) * P(Y=1) = 0 * 0.4 = 0
Comme pour le Cas 1, ces valeurs de x ne sont pas couvertes par les distributions.

**Synthèse de la règle de décision :**
En combinant les conclusions des différents cas, la règle de décision du classifieur de Bayes optimal est la suivante :
Si x ∈ [0, 1], alors le classifieur assigne x à la classe Y=0.
Si x ∈ (1, 1.5], alors le classifieur assigne x à la classe Y=1.

Pour les valeurs de x en dehors de l'intervalle [0, 1.5], le modèle ne fournit pas d'information pour la classification, car la densité de probabilité est nulle pour les deux classes. Dans un contexte pratique, de telles observations seraient considérées comme hors du domaine d'application du modèle ou nécessiteraient une gestion spécifique.
