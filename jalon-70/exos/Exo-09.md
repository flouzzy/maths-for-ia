# Exercice 9 : La Diagonale et la Non $\sigma$-finitude (★★★★★)

**Énoncé :**
Soit $X = [0,1]$. On munit $X$ de la tribu borélienne $\mathcal{B}([0,1])$.
Soit $\lambda$ la mesure de Lebesgue sur $X$, et $\mu$ la mesure de comptage sur $X$.
Considérons l'espace produit $(X \times X, \mathcal{B}([0,1]) \otimes \mathcal{B}([0,1]))$ muni des mesures $m_1 = \lambda \otimes \mu$ et $m_2 = \mu \otimes \lambda$.
Soit $\Delta = \{(x,x) \mid x \in [0,1]\}$ la diagonale.
1. Montrer que $\Delta$ est mesurable pour la tribu produit.
2. Montrer que l'intégrale par sections itérées dépend de l'ordre d'intégration pour l'ensemble $\Delta$.
3. Expliquer rigoureusement pourquoi ce phénomène se produit, et conclure sur la notion de mesure produit dans ce cas.

**Correction :**
1. L'application $f(x,y) = x - y$ est continue de $X \times X \to \mathbb{R}$. Or $\Delta = f^{-1}(\{0\})$. L'image réciproque d'un fermé par une fonction continue étant fermée, $\Delta$ est un fermé. Tout fermé appartenant à la tribu borélienne, et la tribu borélienne produit sur $\mathbb{R}^2$ coïncidant avec $\mathcal{B}(\mathbb{R}) \otimes \mathcal{B}(\mathbb{R})$, $\Delta$ est bien mesurable dans la tribu produit.
2. Calculons par sections $x$ fixées (intégration selon $y$, puis $x$) :
   $\Delta_{x} = \{y \in X \mid (x,y) \in \Delta\} = \{x\}$.
   La mesure de la section selon la seconde mesure (mesure de comptage $\mu$) est $\mu(\Delta_x) = \mu(\{x\}) = 1$.
   On intègre ensuite selon $x$ (mesure de Lebesgue $\lambda$) : $\int_X 1 \, d\lambda(x) = \lambda([0,1]) = 1$.
   Calculons par sections $y$ fixées (intégration selon $x$, puis $y$) :
   $\Delta^y = \{x \in X \mid (x,y) \in \Delta\} = \{y\}$.
   La mesure de la section selon la première mesure (mesure de Lebesgue $\lambda$) est $\lambda(\Delta^y) = \lambda(\{y\}) = 0$.
   On intègre ensuite selon $y$ (mesure de comptage $\mu$) : $\int_X 0 \, d\mu(y) = 0$.
   Les résultats diffèrent de manière patente ($1 \neq 0$).
3. Le théorème d'existence et unicité de la mesure produit postule que les deux espaces mesurés initiaux doivent être **$\sigma$-finis**. Or, l'espace $(X, \mathcal{B}([0,1]), \mu)$ muni de la mesure de comptage n'est pas $\sigma$-fini (il est indénombrable, donc on ne peut l'écrire comme l'union dénombrable d'ensembles finis).
   Ainsi, il n'existe pas de mesure produit **unique**. L'ordre de l'intégration ne caractérise plus une valeur univoque pour $\Delta$. Le "produit" des mesures n'est pas bien posé globalement sur toute la tribu en dehors des hypothèses de $\sigma$-finitude.
