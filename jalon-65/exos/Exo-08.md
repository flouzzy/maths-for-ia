## Définition alternative de la mesurabilité \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X, \mathcal{F})$ un espace mesurable. Soit $f : X \to \mathbb{R}$.
Montrez que $f$ est mesurable si et seulement si, pour tout nombre rationnel $q \in \mathbb{Q}$, l'ensemble $f^{-1}(]q, +\infty[) \in \mathcal{F}$.

### Correction Détaillée

1. **Sens ($\implies$) :**
   Si $f$ est mesurable, alors pour tout borélien $B$, $f^{-1}(B) \in \mathcal{F}$. Or, pour tout rationnel $q \in \mathbb{Q}$, l'intervalle $]q, +\infty[$ est un borélien. Donc trivialement $f^{-1}(]q, +\infty[) \in \mathcal{F}$.

2. **Sens ($\impliedby$) :**
   Supposons que pour tout rationnel $q \in \mathbb{Q}$, $f^{-1}(]q, +\infty[) \in \mathcal{F}$.
   Nous devons montrer que pour tout réel $a \in \mathbb{R}$, $f^{-1}(]a, +\infty[) \in \mathcal{F}$, car ces intervalles engendrent la tribu borélienne.

   Soit $a \in \mathbb{R}$ un nombre irrationnel.
   La densité de $\mathbb{Q}$ dans $\mathbb{R}$ implique qu'il existe une suite décroissante de nombres rationnels $(q_n)_{n \in \mathbb{N}}$ qui converge vers $a$ (c'est-à-dire que $q_n > a$ et $q_n \to a$).
   Plus précisément, on peut approcher l'intervalle strict $]a, +\infty[$ par une union dénombrable d'intervalles stricts aux bornes rationnelles.
   Pour tout $x > a$, il existe un rationnel $q_n$ tel que $a < q_n < x$. Par conséquent :
   $$ ]a, +\infty[ = \bigcup_{n \in \mathbb{N}} ]q_n, +\infty[ $$

   Appliquons l'image réciproque, qui commute avec l'union :
   $$ f^{-1}(]a, +\infty[) = f^{-1}\left(\bigcup_{n \in \mathbb{N}} ]q_n, +\infty[\right) = \bigcup_{n \in \mathbb{N}} f^{-1}(]q_n, +\infty[) $$

   Par hypothèse, chaque ensemble $f^{-1}(]q_n, +\infty[)$ appartient à $\mathcal{F}$.
   La tribu $\mathcal{F}$ étant stable par union dénombrable, leur réunion appartient également à $\mathcal{F}$.
   Ainsi $f^{-1}(]a, +\infty[) \in \mathcal{F}$ pour tout réel $a$, ce qui engendre bien la tribu de Borel.
   $f$ est donc mesurable.
