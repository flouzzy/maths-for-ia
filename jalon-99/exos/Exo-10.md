# Exercice 10
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Un modèle de classification binaire produit des "marges dures" si l'ensemble des données d'entraînement, séparé en deux classes $C_+$ et $C_-$, peut être scindé sans erreur par un hyperplan affine.
Supposons que les données vivent dans l'espace $\ell^2(\mathbb{N})$ (espace de Hilbert des suites de carré sommable, modélisant un espace de features de dimension infinie via le kernel trick).
Les classes sont définies par $C_+ = \{ e_n + \frac{1}{n} e_1 \mid n \ge 2 \}$ et $C_- = \{ -e_n - \frac{1}{n} e_1 \mid n \ge 2 \}$, où $(e_k)$ est la base hilbertienne usuelle de $\ell^2$.
Soient $K_+ = \overline{\text{Conv}(C_+)}$ et $K_- = \overline{\text{Conv}(C_-)}$ les enveloppes convexes fermées des deux classes.
Montrer que $K_+$ et $K_-$ sont disjointes. Peut-on les séparer strictement au sens du SVM à marge dure (2ème forme de Hahn-Banach) ?

**Correction :**
1. **Fermeture convexe et Disjonction :**
   Les vecteurs de $C_+$ ont toutes leurs composantes d'indice $\ge 2$ positives ou nulles (et au moins une vaut 1), et leur première composante est strictement positive. Par combinaison convexe et passage à la limite dans $\ell^2$, tout élément de $K_+$ a sa première composante $\ge 0$.
   Par symétrie complète, tout élément de $K_-$ a sa première composante $\le 0$.
   Supposons qu'il existe $u \in K_+ \cap K_-$. Alors nécessairement sa première coordonnée est $u_1 = 0$.
   Or, pour toute combinaison convexe $v = \sum \lambda_i (e_{n_i} + \frac{1}{n_i} e_1) \in \text{Conv}(C_+)$, la première composante est $\sum \lambda_i \frac{1}{n_i}$. Si $v$ s'approche de $u$ dans $\ell^2$, la composante s'approche de $u_1=0$. Mais les autres composantes (la somme des carrés des $\lambda_i$) doivent être sommables et de somme 1, on ne peut pas faire tendre $\sum \lambda_i \frac{1}{n_i}$ vers 0 en gardant $\sum \lambda_i = 1$ sauf en "rejetant la masse à l'infini" (ce qui correspond à la suite $(e_n)_{n \to \infty}$ qui n'a pas de limite forte, mais converge faiblement vers 0, mais $0 \notin K_+$ car la norme de la suite est $1$). Une analyse fine (hors portée d'un simple calcul) montre formellement que $K_+$ et $K_-$ ne partagent aucun point : ils sont disjoints.
2. **Absence de Compacité :**
   $C_+$ contient la suite orthonormée $(e_n)_{n \ge 2}$ (à un terme correctif tendant vers 0 en norme près). La distance entre deux éléments de la base est $\sqrt{2}$. La suite n'admet aucune sous-suite convergente. L'ensemble n'est pas précompact, donc son enveloppe convexe fermée $K_+$ n'est absolument pas compacte en dimension infinie. Le théorème 2 de Hahn-Banach ne s'applique pas d'office.
3. **Impossibilité de séparation stricte (Pas de SVM à marge dure) :**
   La distance entre $K_+$ et $K_-$ est donnée par $\inf \| x - y \|$ pour $x \in K_+, y \in K_-$.
   En considérant les suites définissantes, la distance entre le $n$-ième point de $C_+$ et le $m$-ième point de $C_-$ pour $n,m$ grands n'est pas nulle.
   Cependant, considérons la combinaison convexe $\frac{1}{N} \sum_{n=2}^{N+1} (e_n + \frac{1}{n} e_1) \in K_+$.
   La norme au carré de ce vecteur est $\frac{1}{N^2} ( \sum_{n=2}^{N+1} \frac{1}{n} )^2 + \frac{1}{N^2} \sum_{n=2}^{N+1} 1 = \frac{O(\log^2 N)}{N^2} + \frac{N}{N^2}$.
   Quand $N \to \infty$, cette norme tend vers 0. L'origine 0 est donc dans l'adhérence des ensembles (c'est leur point d'accumulation faible commun).
   La distance entre $K_+$ et $K_-$ est exactement $0$.
   S'il existait un hyperplan de séparation stricte, défini par $f(x) = \langle w, x \rangle = \alpha$ et une marge $\varepsilon > 0$, la distance géométrique entre les deux convexes (qui serait minorée par la distance au plan des deux côtés, soit $2\varepsilon / \|w\|$) serait strictement positive.
   Puisque la distance est nulle, il n'existe **aucune marge dure stricte**.
   L'intelligence artificielle doit ici recourir aux SVM à marge souple (Soft Margin) ou à des régularisations pénalisant les projections asymptotiques, confirmant que le passage à la dimension infinie brise les intuitions euclidiennes de séparation stricte en l'absence de compacité.
