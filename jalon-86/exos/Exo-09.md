## Mesurabilité du supremum d'une suite de V.A.R. \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X_n)_{n \in \mathbb{N}}$ une suite dénombrable de variables aléatoires réelles définies sur le même espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$.
On définit la fonction $Y : \Omega \to \overline{\mathbb{R}}$ par $Y(\omega) = \sup_{n \in \mathbb{N}} X_n(\omega)$.
Démontrer que $Y$ est une variable aléatoire mesurable (à valeurs dans la droite achevée $\overline{\mathbb{R}}$).

**Correction Explicative :**
1. Il s'agit d'un résultat fondamental d'analyse fonctionnelle qui garantit que les opérations limites préservent la mesurabilité, ce qui est crucial pour définir des concepts tels que la convergence presque sûre. L'espace d'arrivée est ici la droite achevée $\overline{\mathbb{R}} = \mathbb{R} \cup \{-\infty, +\infty\}$, munie de sa tribu borélienne engendrée par les intervalles de la forme $[-\infty, a[$.
2. Pour démontrer que la fonction $Y$ est mesurable, nous devons prouver que pour tout réel $a$, l'ensemble image réciproque $A_a = \{ \omega \in \Omega \mid Y(\omega) \leq a \}$ appartient à la tribu $\mathcal{F}$. L'utilisation de l'inégalité large est pertinente ici pour manipuler le supremum.
3. Rédigeons l'équivalence logique fondamentale liant le supremum à une borne supérieure. Le supremum d'un ensemble de valeurs réelles $(X_n(\omega))_{n \in \mathbb{N}}$ est inférieur ou égal à un nombre $a$ si et seulement si *toutes* les valeurs individuelles sont inférieures ou égales à $a$.
   En termes mathématiques rigoureux :
   $$\sup_{n \in \mathbb{N}} X_n(\omega) \leq a \iff \forall n \in \mathbb{N}, \quad X_n(\omega) \leq a$$
4. Cette équivalence logique nous permet de traduire la condition sur la variable limite $Y$ en une intersection infinie dénombrable de conditions portant sur les variables individuelles $X_n$.
   En termes ensemblistes, l'événement $A_a$ peut s'écrire comme l'intersection des événements individuels :
   $$A_a = \{ \omega \in \Omega \mid Y(\omega) \leq a \} = \bigcap_{n \in \mathbb{N}} \{ \omega \in \Omega \mid X_n(\omega) \leq a \}$$
5. Vérifions l'appartenance à la tribu $\mathcal{F}$ pas-à-pas :
   - Par hypothèse, pour chaque indice $n \in \mathbb{N}$, la fonction $X_n$ est une variable aléatoire réelle.
   - Par conséquent, la définition de la mesurabilité implique que pour tout réel $a$, l'ensemble de sous-niveau $E_{n,a} = \{ \omega \in \Omega \mid X_n(\omega) \leq a \}$ appartient à la tribu $\mathcal{F}$.
   - L'ensemble $A_a$ est l'intersection dénombrable de ces ensembles $E_{n,a}$ pour $n \in \mathbb{N}$.
   - Par définition axiomatique, une tribu (ou $\sigma$-algèbre) est stable par complémentation et par union dénombrable. Par les lois de De Morgan, il en découle qu'elle est nécessairement stable par intersection dénombrable.
   - Puisque chaque $E_{n,a} \in \mathcal{F}$, leur intersection dénombrable l'est également : $A_a = \bigcap_{n \in \mathbb{N}} E_{n,a} \in \mathcal{F}$.
6. Conclusion : Pour tout réel $a$, $\{ Y \leq a \} \in \mathcal{F}$. Ceci démontre de manière exhaustive et rigoureuse que le supremum d'une suite de variables aléatoires est une variable aléatoire mesurable (à valeurs dans $\overline{\mathbb{R}}$). Un raisonnement analogue s'applique pour l'infimum (en considérant $\{ \inf X_n \geq a \}$), ainsi que pour les limites supérieure ($\limsup$) et inférieure ($\liminf$).
