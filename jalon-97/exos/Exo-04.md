# Exercice 4 : Composition d'opérateurs continus
$\bigstar$\bigstar\star\star\star$

**Énoncé :**
Soient $T \in \mathcal{L}(E,F)$ et $S \in \mathcal{L}(F,G)$. Montrer que $S \circ T \in \mathcal{L}(E,G)$ et que $\|S \circ T\| \le \|S\| \|T\|$.

**Correction Détaillée :**
1. Pour tout $x \in E$, $(S \circ T)(x) = S(T(x))$.
2. Puisque $S$ est continu, $\|S(T(x))\|_G \le \|S\| \|T(x)\|_F$.
3. Puisque $T$ est continu, $\|T(x)\|_F \le \|T\| \|x\|_E$.
4. En combinant, $\|(S \circ T)(x)\|_G \le \|S\| \|T\| \|x\|_E$. Donc $S \circ T$ est continu et sa norme est majorée par $\|S\| \|T\|$.
