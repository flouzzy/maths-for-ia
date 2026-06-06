# Exercice 8 : L'inégalité de McDiarmid (Différences bornées)
**Énoncé :** Montrer comment la fonction $f(x_1, \dots, x_n) = \frac{1}{n} \sum_{i=1}^n x_i$ avec $x_i \in [a, b]$ satisfait la condition des différences bornées de McDiarmid.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Évaluer la variation maximale de $f$ si l'on modifie une seule coordonnée.
* *Résolution pas-à-pas :*
Soit le vecteur $x = (x_1, \dots, x_i, \dots, x_n)$ et un vecteur $x'$ différant uniquement par la $i$-ème coordonnée $x' = (x_1, \dots, x'_i, \dots, x_n)$, avec $x_j \in [a, b]$ pour tout $j$.
Calculons la différence des valeurs de la fonction :
$$|f(x_1, \dots, x_i, \dots, x_n) - f(x_1, \dots, x'_i, \dots, x_n)| = \left| \frac{1}{n} \sum_{j=1}^n x_j - \frac{1}{n} \sum_{j=1}^n x'_j \right|$$
Puisque tous les termes $x_j$ pour $j \neq i$ s'annulent :
$$= \left| \frac{1}{n} (x_i - x'_i) \right| = \frac{1}{n} |x_i - x'_i|$$
Comme $x_i \in [a, b]$ et $x'_i \in [a, b]$, la distance maximale entre deux points de cet intervalle est $b - a$.
Donc :
$$|f(x_1, \dots, x_n) - f(x_1, \dots, x'_i, \dots, x_n)| \le \frac{b - a}{n}$$
La fonction satisfait donc la condition des différences bornées avec les constantes $c_i = \frac{b - a}{n}$ pour tout $i=1, \dots, n$.
L'inégalité de McDiarmid donne alors la borne de concentration :
$$P(f - \mathbb{E}[f] \ge t) \le \exp\left( - \frac{2 t^2}{\sum_{i=1}^n c_i^2} \right) = \exp\left( - \frac{2 t^2}{\sum_{i=1}^n \frac{(b-a)^2}{n^2}} \right) = \exp\left( - \frac{2 t^2}{n \frac{(b-a)^2}{n^2}} \right) = \exp\left( - \frac{2 n t^2}{(b-a)^2} \right)$$
Ce qui correspond exactement à l'inégalité de Hoeffding. $\blacksquare$
