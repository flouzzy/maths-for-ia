# Exercice 5 : Bilinéarité et Continuité Séparée
$\bigstar\bigstar\bigstar\star\star$
**Énoncé :**
Soient $E, F$ des espaces de Banach, et $G$ un espace vectoriel normé.
Soit $B : E \times F \to G$ une application bilinéaire.
On suppose que $B$ est séparément continue :
- Pour tout $x_0 \in E$, l'application $y \mapsto B(x_0, y)$ est continue sur $F$.
- Pour tout $y_0 \in F$, l'application $x \mapsto B(x, y_0)$ est continue sur $E$.
Montrer que $B$ est globalement continue (continue sur $E \times F$).

**Correction :**
1. Soit la boule unité fermée de $E$, notée $B_E = \{x \in E : \|x\|_E \le 1\}$.
   Considérons la famille d'opérateurs linéaires $(T_x)_{x \in B_E}$ de $F$ dans $G$ définie par $T_x(y) = B(x, y)$.
   Par hypothèse de continuité séparée, chaque $T_x$ est un opérateur linéaire continu sur $F$.
2. Vérifions la condition de bornitude ponctuelle :
   Soit $y \in F$ fixé. On s'intéresse à la famille d'images $(T_x(y))_{x \in B_E} = (B(x, y))_{x \in B_E}$.
   Considérons l'application $S_y : E \to G$ définie par $S_y(x) = B(x, y)$.
   Par hypothèse, $S_y$ est linéaire et continue sur $E$.
   Donc pour tout $x \in B_E$, $\|S_y(x)\|_G \le \|S_y\|_{\mathcal{L}(E,G)} \|x\|_E \le \|S_y\|$.
   Ceci montre que l'ensemble $\{T_x(y) : x \in B_E\}$ est borné (par $\|S_y\|$).
3. Application de Banach-Steinhaus :
   $F$ est un espace de Banach. La famille $(T_x)_{x \in B_E}$ est ponctuellement bornée.
   D'après le théorème de Banach-Steinhaus, cette famille est uniformément bornée :
   $\exists M > 0, \forall x \in B_E, \|T_x\|_{\mathcal{L}(F,G)} \le M$.
4. Conclusion sur la continuité globale :
   Pour tout $x \in E$ et $y \in F$ non nuls, $\frac{x}{\|x\|} \in B_E$.
   Donc $\|T_{x/\|x\|}(y)\| \le M \|y\|$.
   Par linéarité, $\|B(x, y)\| = \|T_x(y)\| = \|x\| \left\| T_{x/\|x\|}(y) \right\| \le M \|x\|_E \|y\|_F$.
   Cette majoration prouve que l'application bilinéaire $B$ est globalement continue.