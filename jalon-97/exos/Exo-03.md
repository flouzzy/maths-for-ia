# Exercice 3 : Somme de deux opérateurs continus
$\bigstar$\bigstar\star\star\star$

**Énoncé :**
Soient $S, T \in \mathcal{L}(E,F)$ deux opérateurs continus. Montrer que $S+T$ est continu et que $\|S+T\| \le \|S\| + \|T\|$.

**Correction Détaillée :**
1. Par inégalité triangulaire, pour tout $x \in E$, $\|(S+T)(x)\| = \|S(x) + T(x)\| \le \|S(x)\| + \|T(x)\|$.
2. Par définition de la norme d'opérateur, $\|S(x)\| \le \|S\| \|x\|$ et $\|T(x)\| \le \|T\| \|x\|$.
3. Donc $\|(S+T)(x)\| \le (\|S\| + \|T\|)\|x\|$.
4. L'opérateur est donc borné, avec $\|S+T\| \le \|S\| + \|T\|$.
