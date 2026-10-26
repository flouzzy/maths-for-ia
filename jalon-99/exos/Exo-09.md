# Exercice 9
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Démontrer que dans un espace vectoriel topologique réel localement convexe $E$, le dual topologique $E^*$ sépare les points de $E$.
Plus précisément, si $x, y \in E$ avec $x \ne y$, montrer qu'il existe une forme linéaire continue $f \in E^*$ telle que $f(x) \ne f(y)$.

**Correction :**
1. **Traduction vectorielle :**
   La question est équivalente à prouver que pour tout vecteur non nul $v = x - y \in E \setminus \{0\}$, il existe une forme linéaire continue $f$ telle que $f(v) \ne 0$.
2. **Utilisation de la topologie localement convexe :**
   Puisque l'espace topologique $E$ est localement convexe et séparé (ce qui est toujours supposé dans la définition usuelle d'un evc), il existe un voisinage de l'origine (vecteur nul) qui est un ensemble convexe. Plus précisément, comme $E$ est séparé et que $v \ne 0$, il existe un voisinage de l'origine qui ne contient pas $v$.
   Dans un espace localement convexe, la base de voisinages de l'origine est formée d'ensembles convexes, équilibrés et absorbants.
   Il existe donc un tel voisinage $V$ de l'origine, qui est convexe et ouvert, tel que $v \notin V$.
3. **Application de Hahn-Banach Géométrique :**
   Posons $A = V$ et $B = \{v\}$.
   - $A$ est un voisinage de $0$, ouvert (ou qu'on peut prendre comme l'intérieur d'un voisinage, qui restera convexe) et convexe par définition de la topologie locale.
   - $B$ est un singleton, donc convexe.
   - $A$ et $B$ sont disjoints car $v \notin V$.
   La première forme géométrique de Hahn-Banach s'applique : il existe un hyperplan séparateur.
   Il existe $f \in E^*$ et $\alpha \in \mathbb{R}$ tels que :
   $\forall u \in V, \, f(u) < \alpha \quad \text{et} \quad f(v) \ge \alpha$
4. **Conclusion :**
   Puisque $V$ est un voisinage de l'origine, $0 \in V$. L'inégalité sur $V$ évaluée en $0$ donne $f(0) < \alpha$, c'est-à-dire $0 < \alpha$.
   La seconde inégalité donne $f(v) \ge \alpha > 0$.
   Ainsi, nous avons trouvé une forme linéaire continue $f$ telle que $f(v) \ne 0$, et par conséquent $f(x) - f(y) \ne 0 \implies f(x) \ne f(y)$. Le dual sépare bien les points, propriété fondamentale de l'analyse fonctionnelle (qui prouve que l'espace dual n'est jamais trivial si l'espace primal est localement convexe et séparé).
