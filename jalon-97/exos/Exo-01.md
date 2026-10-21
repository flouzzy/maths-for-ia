# Exercice 1 : Continuité de l'opérateur identité
$\bigstar\star\star\star\star$

**Énoncé :**
Soit $E$ un espace de Banach. Montrer que l'opérateur identité $I: E \to E$ est continu et calculer sa norme.

**Correction Détaillée :**
1. Soit $x \in E$. Par définition de l'opérateur identité, $I(x) = x$.
2. Ainsi, $\|I(x)\|_E = \|x\|_E$.
3. On en déduit directement que $\forall x \in E, \|I(x)\|_E \le 1 \cdot \|x\|_E$.
4. L'opérateur $I$ est donc borné (et continu). Sa norme est $\|I\| = \sup_{\|x\|=1} \|I(x)\| = \sup_{\|x\|=1} \|x\| = 1$.
