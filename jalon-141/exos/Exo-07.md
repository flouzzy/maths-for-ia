# Exercice 7 : Lemme de Sauer-Shelah (Définition)
**Énoncé :** Énoncer le lemme de Sauer-Shelah et calculer la borne pour un espace de dimension $d=3$ avec $n=10$ échantillons.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Calcul numérique explicite de la formule de borne polynomiale.
* *Résolution pas-à-pas :*
Le lemme de Sauer-Shelah stipule que pour une classe $\mathcal{F}$ de dimension de Vapnik-Chervonenkis $d$ finie, pour tout $n$, la fonction de croissance vérifie :
$$S_{\mathcal{F}}(n) \le \sum_{i=0}^d \binom{n}{i}$$
Et pour $n \ge d$, on a la borne supérieure relâchée :
$$S_{\mathcal{F}}(n) \le \left( \frac{en}{d} \right)^d$$
Pour $d = 3$ et $n = 10$, on calcule la valeur exacte de la somme :
$$\sum_{i=0}^3 \binom{10}{i} = \binom{10}{0} + \binom{10}{1} + \binom{10}{2} + \binom{10}{3}$$
$$= 1 + 10 + \frac{10 \times 9}{2} + \frac{10 \times 9 \times 8}{3 \times 2 \times 1}$$
$$= 1 + 10 + 45 + \frac{720}{6}$$
$$= 56 + 120 = 176$$
Le nombre maximal de sous-ensembles réalisables par la classe sur $10$ points est $176$, ce qui est massivement inférieur à $2^{10} = 1024$. La classe est donc très restreinte, prouvant que la généralisation est possible. $\blacksquare$
