# Exercice 10 : Théorème de compacité et coloriage de graphes infinis (Niveau ENS)

## Énoncé
Soit $G = (V, E)$ un graphe non orienté, où l'ensemble des sommets $V$ est infini (dénombrable ou non) et $E \subseteq \{\{u, v\} \mid u, v \in V, u \neq v\}$ est l'ensemble des arêtes.
Soit $k \ge 1$ un entier naturel. On rappelle qu'un **$k$-coloriage** propre de $G$ est une application $f : V \to \{1, \dots, k\}$ telle que pour toute arête $\{u, v\} \in E$ :
$$f(u) \neq f(v)$$

On suppose que le graphe $G$ vérifie la propriété locale suivante :
> **Tout sous-graphe fini de $G$ est $k$-colorable.**

Le but de cet exercice est de démontrer, à l'aide du **théorème de compacité de la logique propositionnelle**, le **théorème de De Bruijn-Erdős** :
> **Le graphe infini $G$ est lui-même $k$-colorable.**

1. Modéliser le problème en définissant un ensemble de variables propositionnelles approprié.
2. Écrire les formules logiques modélisant les trois contraintes suivantes :
   - Contrainte 1 : Tout sommet possède au moins une couleur.
   - Contrainte 2 : Tout sommet possède au plus une couleur.
   - Contrainte 3 : Deux sommets adjacents n'ont pas la même couleur.
   On notera $\Sigma$ l'ensemble de toutes ces clauses.
3. Soit $\Sigma_0$ un sous-ensemble fini de $\Sigma$. Démontrer que $\Sigma_0$ est satisfaisable.
4. Conclure par le théorème de compacité de la logique propositionnelle.

---

## Correction Détaillée

### Question 1 : Choix des variables propositionnelles
Pour chaque sommet $i \in V$ et chaque couleur $c \in \{1, \dots, k\}$, nous définissons la variable propositionnelle $x_{i, c}$ dont la sémantique est :
$$x_{i, c} \equiv \text{« Le sommet } i \text{ est coloré avec la couleur } c \text{ »}$$
L'ensemble de nos variables propositionnelles est donc :
$$\mathcal{P} = \{x_{i, c} \mid i \in V, c \in \{1, \dots, k\}\}$$

---

### Question 2 : Modélisation des contraintes logiques

1. **Chaque sommet a au moins une couleur :**
   Pour tout sommet $i \in V$, la formule traduisant cette condition est une clause disjonctive sur toutes les couleurs disponibles :
   $$\Phi_i = \bigvee_{c=1}^k x_{i, c}$$
   Désignons par $\Sigma_1 = \{\Phi_i \mid i \in V\}$ l'ensemble de ces clauses.

2. **Chaque sommet a au plus une couleur :**
   Pour tout sommet $i \in V$ et pour chaque paire de couleurs distinctes $c_1 \neq c_2$, le sommet ne peut pas porter les deux couleurs simultanément, ce qui s'écrit $\neg(x_{i, c_1} \land x_{i, c_2}) \equiv \neg x_{i, c_1} \lor \neg x_{i, c_2}$.
   Désignons par $\Sigma_2$ l'ensemble de toutes ces clauses d'exclusion :
   $$\Sigma_2 = \{\neg x_{i, c_1} \lor \neg x_{i, c_2} \mid i \in V, \quad 1 \le c_1 < c_2 \le k\}$$

3. **Les sommets adjacents ont des couleurs différentes :**
   Pour chaque arête $\{i, j\} \in E$ et chaque couleur $c \in \{1, \dots, k\}$, les sommets $i$ et $j$ ne peuvent pas être colorés tous deux en $c$, ce qui s'écrit $\neg(x_{i, c} \land x_{j, c}) \equiv \neg x_{i, c} \lor \neg x_{j, c}$.
   Désignons par $\Sigma_3$ l'ensemble de ces clauses de conflit :
   $$\Sigma_3 = \{\neg x_{i, c} \lor \neg x_{j, c} \mid \{i, j\} \in E, \quad c \in \{1, \dots, k\}\}$$

L'ensemble total de nos formules est $\Sigma = \Sigma_1 \cup \Sigma_2 \cup \Sigma_3$.
Une valuation $v$ satisfaisant $\Sigma$ correspond bijectivement à un $k$-coloriage propre de $G$.

---

### Question 3 : Satisfaisabilité de tout sous-ensemble fini $\Sigma_0$
Soit $\Sigma_0 \subseteq \Sigma$ un sous-ensemble fini de clauses.
- Puisque $\Sigma_0$ est fini, il ne contient qu'un nombre fini de clauses.
- Chaque clause de $\Sigma_0$ ne fait intervenir qu'un nombre fini de sommets de $V$.
- Désignons par $V_0 \subseteq V$ l'ensemble des sommets apparaissant dans les clauses de $\Sigma_0$. Puisque $\Sigma_0$ est fini et que chaque clause contient au plus $k$ sommets (les clauses de $\Sigma_1$ ont $1$ sommet, $\Sigma_2$ ont $1$ sommet, et $\Sigma_3$ ont $2$ sommets), $V_0$ est un **ensemble fini**.
- Soit $G_0 = (V_0, E_0)$ le sous-graphe fini de $G$ induit par le sous-ensemble de sommets $V_0$, où $E_0 = \{\{i, j\} \in E \mid i, j \in V_0\}$.

Par hypothèse de l'énoncé, le sous-graphe fini $G_0$ est $k$-colorable. Il existe donc une fonction de coloriage propre $f_0 : V_0 \to \{1, \dots, k\}$ sur ce sous-graphe.
Définissons une valuation $v_0$ pour les variables propositionnelles apparaissant dans $\Sigma_0$ par :
$$v_0(x_{i, c}) = 1 \iff i \in V_0 \text{ et } f_0(i) = c$$

Vérifions que $v_0$ satisfait toutes les clauses de $\Sigma_0$ :
- Si une clause $C \in \Sigma_0$ provient de $\Sigma_1$, elle est de la forme $\bigvee_{c=1}^k x_{i, c}$ pour un certain $i \in V_0$. Comme $f_0(i) \in \{1, \dots, k\}$, il existe un unique $c^*$ tel que $f_0(i) = c^*$. Alors $v_0(x_{i, c^*}) = 1$, la clause est donc satisfaite.
- Si $C \in \Sigma_0$ provient de $\Sigma_2$, elle est de la forme $\neg x_{i, c_1} \lor \neg x_{i, c_2}$ pour $c_1 < c_2$. Comme $f_0(i)$ ne peut pas être égal à la fois à $c_1$ et $c_2$, au moins l'une des variables $x_{i, c_1}$ ou $x_{i, c_2}$ est évaluée à $0$ par $v_0$. La disjonction des négations est donc évaluée à $1$. La clause est satisfaite.
- Si $C \in \Sigma_0$ provient de $\Sigma_3$, elle est de la forme $\neg x_{i, c} \lor \neg x_{j, c}$ avec $\{i, j\} \in E_0$. Puisque $f_0$ est un coloriage propre de $G_0$, $f_0(i) \neq f_0(j)$. Donc $i$ et $j$ ne peuvent pas avoir tous deux la couleur $c$. L'une des variables $x_{i, c}$ ou $x_{j, c}$ vaut nécessairement $0$, ce qui satisfait la clause.

Puisque toutes les clauses de $\Sigma_0$ sont satisfaites par $v_0$, le sous-ensemble fini $\Sigma_0$ est **satisfaisable**.

---

### Question 4 : Conclusion par compacité
Nous venons de démontrer que pour tout sous-ensemble fini $\Sigma_0 \subseteq \Sigma$, $\Sigma_0$ est satisfaisable.
Par le **théorème de compacité de la logique propositionnelle**, l'ensemble infini complet $\Sigma$ est satisfaisable.

Il existe donc une valuation globale $v^* : \mathcal{P} \to \{0, 1\}$ telle que pour toute clause $C \in \Sigma$, $v^*(C) = 1$.
Définissons l'application de coloriage global $f^* : V \to \{1, \dots, k\}$ par :
$$f^*(i) = c \iff v^*(x_{i, c}) = 1$$

Vérifions que $f^*$ est bien définie et est un coloriage propre :
- Les clauses de $\Sigma_1$ garantissent que pour chaque $i \in V$, il existe au moins un $c$ tel que $v^*(x_{i, c}) = 1$.
- Les clauses de $\Sigma_2$ garantissent que pour chaque $i \in V$, il existe au plus un $c$ tel que $v^*(x_{i, c}) = 1$.
- Donc, $f^*$ est une application bien définie de $V$ dans $\{1, \dots, k\}$.
- Les clauses de $\Sigma_3$ garantissent que si $\{i, j\} \in E$, alors pour tout $c$, $v^*(x_{i, c}) = 0$ ou $v^*(x_{j, c}) = 0$. Donc $f^*(i) \neq f^*(j)$. Le coloriage est propre.

Le graphe infini $G$ est donc $k$-colorable. $\blacksquare$
