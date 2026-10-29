$\bigstar\bigstar\bigstar\bigstar\bigstar$
**Énoncé :** Adhérence faible d'un convexe.
Soit $E$ un espace de Banach et $C$ un sous-ensemble convexe de $E$. Démontrer que l'adhérence forte de $C$ coïncide avec son adhérence faible.

**Correction Détaillée :**
Notons $\overline{C}$ l'adhérence forte de $C$, et $\overline{C}^w$ son adhérence faible.
Toute forme linéaire continue l'étant aussi pour la topologie forte, un voisinage faible est a fortiori un voisinage fort. Par conséquent, la topologie faible est moins fine que la topologie forte. Il s'ensuit que tout ensemble faiblement fermé est fortement fermé.
En appliquant cela à $\overline{C}^w$ qui est faiblement fermé et contient $C$, on obtient que $\overline{C}^w$ est fortement fermé et contient $C$. Comme $\overline{C}$ est le plus petit fermé fort contenant $C$, on a $\overline{C} \subset \overline{C}^w$.
Montrons l'inclusion réciproque. Raisonnons par l'absurde en supposant qu'il existe $x_0 \in \overline{C}^w$ tel que $x_0 \notin \overline{C}$.
Puisque $C$ est convexe, son adhérence forte $\overline{C}$ est également convexe et fortement fermée.
Par le théorème de séparation stricte de Hahn-Banach (forme géométrique, Jalon 99), comme $x_0 \notin \overline{C}$ et $\{x_0\}$ est compact, il existe une forme linéaire continue $L \in E^*$ et des réels $\alpha, \epsilon > 0$ tels que :
$L(x_0) \le \alpha - \epsilon < \alpha \le L(y)$ pour tout $y \in \overline{C}$.
Considérons le demi-espace ouvert $V = \{x \in E \mid L(x) < \alpha\}$.
$V$ est un voisinage faible de $x_0$ par définition des voisinages faibles.
Cependant, pour tout $y \in C$, $L(y) \ge \alpha$, donc $y \notin V$. Ainsi $V \cap C = \emptyset$.
Ceci contredit le fait que $x_0$ appartient à l'adhérence faible de $C$ (tout voisinage faible de $x_0$ devrait intersecter $C$).
On conclut que l'hypothèse $x_0 \notin \overline{C}$ est fausse. D'où $\overline{C}^w \subset \overline{C}$.
Par double inclusion, les deux adhérences coïncident.
