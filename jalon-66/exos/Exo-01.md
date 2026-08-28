# Exercice 1 : Calcul d'intégrale de fonction simple \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit $X = \{1, 2, 3, 4, 5\}$ muni de la mesure de comptage $\mu$. Soit $s(x) = x^2$ si $x$ est pair, et $s(x) = x$ si $x$ est impair. Calculer $\int_X s \, d\mu$.

**Correction :**
La fonction $s$ prend les valeurs : $s(1)=1, s(2)=4, s(3)=3, s(4)=16, s(5)=5$.

Écrivons $s$ sous forme canonique :
$s = 1 \cdot \mathbf{1}_{\{1\}} + 3 \cdot \mathbf{1}_{\{3\}} + 4 \cdot \mathbf{1}_{\{2\}} + 5 \cdot \mathbf{1}_{\{5\}} + 16 \cdot \mathbf{1}_{\{4\}}$.

L'intégrale est :
$\int_X s \, d\mu = 1 \cdot \mu(\{1\}) + 3 \cdot \mu(\{3\}) + 4 \cdot \mu(\{2\}) + 5 \cdot \mu(\{5\}) + 16 \cdot \mu(\{4\})$.

Puisque $\mu$ est la mesure de comptage, chaque singleton a une mesure de 1.
$\int_X s \, d\mu = 1\cdot 1 + 3\cdot 1 + 4\cdot 1 + 5\cdot 1 + 16\cdot 1 = 29$.
