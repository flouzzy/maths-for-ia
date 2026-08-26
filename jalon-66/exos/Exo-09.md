### Intégrale sur des espaces produits (Introduction) \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Considérons l'espace $X = \{1, 2\}$ et la tribu $\mathcal{P}(X)$, muni de la mesure $\mu(\{1\}) = \alpha$, $\mu(\{2\}) = \beta$.
Calculer explicitement l'intégrale d'une fonction quelconque $f: X \to \mathbb{R}_+$ définie par $f(1) = u$, $f(2) = v$.

**Correction Détaillée :**
**Étape 1 : Forme simple.**
Dans ce cas discret fini, TOUTE fonction est une fonction simple.
En effet, on peut écrire $f = u \mathbf{1}_{\{1\}} + v \mathbf{1}_{\{2\}}$.

**Étape 2 : Calcul direct.**
Par définition de l'intégrale d'une fonction simple :
$$\int_X f d\mu = u \cdot \mu(\{1\}) + v \cdot \mu(\{2\}) = u\alpha + v\beta$$

**Conclusion :**
Sur un espace fini, l'intégrale de Lebesgue se réduit à une somme pondérée (ou produit scalaire de dimension finie). C'est le socle de l'espérance mathématique des variables aléatoires discrètes finies.
