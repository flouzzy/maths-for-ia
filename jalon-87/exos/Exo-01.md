# Exercice 1 : Calcul direct d'espérance discrète

**Difficulté :** $\bigstar\star\star\star\star$

On considère une variable aléatoire $X$ dont la loi de probabilité discrète est donnée par $\mathbb{P}(X = -1) = 0.2$, $\mathbb{P}(X = 0) = 0.5$ et $\mathbb{P}(X = 2) = 0.3$.
1. Calculer l'espérance mathématique de $X$, $\mathbb{E}[X]$.
2. Calculer l'espérance de $X^2$, $\mathbb{E}[X^2]$.
3. En déduire la variance de $X$, $\mathrm{Var}(X)$.

### Correction détaillée

1. L'espérance pour une loi discrète est la somme pondérée des valeurs :
   $$ \mathbb{E}[X] = \sum_{x \in \{-1, 0, 2\}} x \mathbb{P}(X = x) $$
   $$ \mathbb{E}[X] = (-1) \times 0.2 + 0 \times 0.5 + 2 \times 0.3 $$
   $$ \mathbb{E}[X] = -0.2 + 0 + 0.6 = 0.4 $$

2. Pour calculer $\mathbb{E}[X^2]$, on utilise le théorème de transfert :
   $$ \mathbb{E}[X^2] = \sum_{x \in \{-1, 0, 2\}} x^2 \mathbb{P}(X = x) $$
   $$ \mathbb{E}[X^2] = (-1)^2 \times 0.2 + 0^2 \times 0.5 + 2^2 \times 0.3 $$
   $$ \mathbb{E}[X^2] = 1 \times 0.2 + 0 + 4 \times 0.3 = 0.2 + 1.2 = 1.4 $$

3. D'après la formule de Koenig-Huygens, on a :
   $$ \mathrm{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 $$
   $$ \mathrm{Var}(X) = 1.4 - (0.4)^2 = 1.4 - 0.16 = 1.24 $$
