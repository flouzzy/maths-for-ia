## Exercice 10 : Construction d'un paradoxe géométrique (Vitali restreint)
$\bigstar\bigstar\bigstar\bigstar\bigstar$

### Énoncé

Pourquoi exige-t-on que la tribu $\mathcal{F}$ ne soit pas toujours égale à l'ensemble des parties $\mathcal{P}(\Omega)$ lorsque l'univers $\Omega$ est continu (comme $[0, 1]$) ?
Le paradoxe de Vitali montre qu'il est impossible de définir une mesure de probabilité sur $\mathcal{P}([0, 1])$ qui soit simultanément :
- $\sigma$-additive.
- Invariante par translation (la probabilité d'un intervalle ne dépend que de sa longueur).
- Normalisée ($\mathbb{P}([0, 1]) = 1$).

On construit une relation d'équivalence sur $[0, 1[$ : $x \sim y \iff x - y \in \mathbb{Q}$. On choisit un représentant unique par classe pour former un ensemble $V$.
Justifier pourquoi, si l'on suppose par l'absurde que $\mathbb{P}(V)$ existe, le fait de sommer les translations rationnelles de $V$ aboutit à une contradiction insoluble avec les axiomes de Kolmogorov, rendant $V$ "non-mesurable".


### Correction Détaillée

Cet exercice illustre l'impérieuse nécessité de la notion de "tribu" $\mathcal{F}$ dans la définition axiomatique de Kolmogorov, empêchant de mesurer des ensembles "pathologiques".

**Étape 1 : Construction des translations dénombrables**
L'ensemble $V$ contient un et un seul représentant de chaque classe de l'équivalence $x \sim y \iff x-y \in \mathbb{Q}$.
L'ensemble des rationnels dans $[-1, 1]$ est dénombrable. Énumérons-les : $\{q_1, q_2, q_3, \dots\}$.
Pour chaque rationnel $q_n$, on définit le translaté : $V_n = \{v + q_n \pmod 1 \mid v \in V\}$. (Le modulo 1 assure qu'on reste dans $[0, 1[$).

**Étape 2 : Disjonction et Couverture**
1. **Les $V_n$ sont disjoints deux à deux.** Supposons par l'absurde que $x \in V_n \cap V_m$ (avec $n \neq m$). Alors $x = v_1 + q_n = v_2 + q_m$ (modulo 1). Ainsi $v_1 - v_2 = q_m - q_n \in \mathbb{Q}$. Par définition de la relation d'équivalence, $v_1 \sim v_2$. Mais $V$ ne contient qu'un seul représentant par classe, donc $v_1 = v_2$. Il s'ensuit que $q_n = q_m$, contradiction.
2. **L'union des $V_n$ couvre l'espace.** Tout réel $x \in [0, 1[$ appartient à une classe d'équivalence, donc il diffère d'un certain élément de $V$ par un rationnel $q_n$. Donc $x \in V_n$.
Ainsi, $\bigcup_{n=1}^\infty V_n = [0, 1[$.

**Étape 3 : La contradiction via les axiomes de Kolmogorov**
Supposons que $V$ soit un événement mesurable et possède une probabilité $p = \mathbb{P}(V)$.
Puisque la mesure de Lebesgue est invariante par translation, chaque $V_n$ a la même probabilité : $\mathbb{P}(V_n) = \mathbb{P}(V) = p$.

D'après le troisième axiome de Kolmogorov ($\sigma$-additivité sur des ensembles disjoints), la probabilité de l'union infinie est la somme des probabilités :
$\mathbb{P}\left(\bigcup_{n=1}^\infty V_n\right) = \sum_{n=1}^\infty \mathbb{P}(V_n)$.

Or, l'union des $V_n$ est exactement l'univers $[0, 1[$. D'après le deuxième axiome de Kolmogorov, sa probabilité est de $1$ :
$1 = \sum_{n=1}^\infty p = p + p + p + \dots$

Il y a maintenant deux cas, tous les deux absurdes :
- Cas 1 : Si $p = 0$, alors la somme infinie vaut $0$, ce qui contredit $1 = 0$.
- Cas 2 : Si $p > 0$, alors la série somme d'une infinité de termes constants strictement positifs diverge vers l'infini, ce qui contredit $1 = +\infty$.

**Conclusion :**
L'hypothèse initiale "l'ensemble $V$ possède une probabilité mesurable" est obligatoirement fausse. Il existe des ensembles dans $\mathcal{P}([0, 1])$ auxquels on ne peut pas attribuer de probabilité respectant les axiomes. D'où la nécessité de restreindre l'application $\mathbb{P}$ à une tribu mathématiquement sage (comme la tribu borélienne).
