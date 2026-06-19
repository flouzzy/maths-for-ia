En tant que Professeur de Mathématiques à l'ENS, je vous propose l'exercice suivant pour le Jalon 3. Il vise à consolider votre maîtrise de la quantification, de l'ordre des quantificateurs et de la négation, des concepts fondamentaux en analyse et en logique.

---

# Exercice 3 (Jalon 3 : Quantification, ordre des quantificateurs, négation)

**Niveau de difficulté :** $\star \star \rule{0.5cm}{0.4pt}\rule{0.5cm}{0.4pt}\rule{0.5cm}{0.4pt}$ (2/5 étoiles)

Soit $A$ un sous-ensemble non vide de l'ensemble des nombres réels $\mathbb{R}$.
Nous définissons la propriété $\mathcal{P}(A)$ comme suit :
$$ \mathcal{P}(A) : \quad \forall x \in A, \exists y \in A, \left( y \neq x \land \left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right) $$
Cette propriété peut être interprétée comme : "Pour tout élément $x$ de $A$, il existe un autre élément $y$ de $A$ tel que l'intervalle ouvert strictement entre $x$ et $y$ ne contient aucun élément de $A$."

**Question 1.** (a) Écrire la négation de la propriété $\mathcal{P}(A)$, notée $\neg \mathcal{P}(A)$, sous une forme logique rigoureuse et simplifiée (sans double négation).

**Question 2.** (b) Donner un exemple d'un ensemble $A \subseteq \mathbb{R}$ non vide qui satisfait la propriété $\mathcal{P}(A)$. Justifier votre réponse de manière rigoureuse.

**Question 3.** (c) Donner un exemple d'un ensemble $A \subseteq \mathbb{R}$ non vide qui satisfait la propriété $\neg \mathcal{P}(A)$. Justifier votre réponse de manière rigoureuse.

---

# Correction de l'Exercice 3

## Question 1. (a) Négation de la propriété $\mathcal{P}(A)$

La propriété $\mathcal{P}(A)$ est donnée par :
$$ \mathcal{P}(A) : \quad \forall x \in A, \exists y \in A, \left( y \neq x \land \left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right) $$

Nous allons construire la négation étape par étape en appliquant les règles de négation des quantificateurs et des opérateurs logiques.

1.  **Négation du quantificateur universel initial ($\forall x \in A$) :**
    La négation de $\forall x \in A, Q(x)$ est $\exists x \in A, \neg Q(x)$.
    Donc, $\neg \mathcal{P}(A) \equiv \exists x \in A, \neg \left( \exists y \in A, \left( y \neq x \land \left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right) \right)$.

2.  **Négation du quantificateur existentiel suivant ($\exists y \in A$) :**
    La négation de $\exists y \in A, R(y)$ est $\forall y \in A, \neg R(y)$.
    Donc, $\neg \mathcal{P}(A) \equiv \exists x \in A, \forall y \in A, \neg \left( y \neq x \land \left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right)$.

3.  **Négation de la conjonction logique ($\land$) :**
    La négation de $(P \land Q)$ est $(\neg P \lor \neg Q)$ (loi de De Morgan).
    Ici, $P$ est $(y \neq x)$ et $Q$ est $\left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right)$.
    Donc, $\neg \mathcal{P}(A) \equiv \exists x \in A, \forall y \in A, \left( \neg (y \neq x) \lor \neg \left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right)$.
    Simplifions $\neg (y \neq x)$ en $(y = x)$.
    $\neg \mathcal{P}(A) \equiv \exists x \in A, \forall y \in A, \left( y = x \lor \neg \left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right)$.

4.  **Négation du quantificateur universel suivant ($\forall z \in \mathbb{R}$) :**
    La négation de $\forall z \in \mathbb{R}, S(z)$ est $\exists z \in \mathbb{R}, \neg S(z)$.
    Donc, $\neg \mathcal{P}(A) \equiv \exists x \in A, \forall y \in A, \left( y = x \lor \left( \exists z \in \mathbb{R}, \neg \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right)$.

5.  **Négation de l'implication logique ($\implies$) :**
    La négation de $(P \implies Q)$ est $(P \land \neg Q)$.
    Ici, $P$ est $(\min(x,y) < z < \max(x,y))$ et $Q$ est $(z \notin A)$.
    Donc, $\neg \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right)$ est équivalent à :
    $(\min(x,y) < z < \max(x,y)) \land \neg (z \notin A)$.
    Simplifions $\neg (z \notin A)$ en $(z \in A)$.
    Ainsi, l'expression devient : $(\min(x,y) < z < \max(x,y)) \land (z \in A)$.

6.  **Recomposition de la négation complète :**
    En substituant toutes les formes simplifiées, nous obtenons la négation finale de $\mathcal{P}(A)$ :
    $$ \neg \mathcal{P}(A) : \quad \exists x \in A, \forall y \in A, \left( y = x \lor \left( \exists z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \land z \in A \right) \right) \right) $$
    En mots : "Il existe un élément $x$ dans $A$ tel que pour tout élément $y$ dans $A$, soit $y$ est égal à $x$, soit l'intervalle ouvert strictement entre $x$ et $y$ contient au moins un élément de $A$."

## Question 2. (b) Exemple d'un ensemble $A$ satisfaisant $\mathcal{P}(A)$

Nous cherchons un ensemble $A \subseteq \mathbb{R}$ non vide tel que :
$\forall x \in A, \exists y \in A, \left( y \neq x \land \left( \forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin A \right) \right) \right)$.

Considérons l'ensemble des nombres entiers relatifs $A = \mathbb{Z}$.
L'ensemble $\mathbb{Z}$ est un sous-ensemble non vide de $\mathbb{R}$.

**Justification :**
Soit $x$ un élément arbitraire de $A = \mathbb{Z}$. (Typage : $x \in \mathbb{Z}$).
Nous devons trouver un élément $y \in A$ tel que $y \neq x$ et l'intervalle ouvert $(\min(x,y), \max(x,y))$ ne contienne aucun élément de $\mathbb{Z}$.

Choisissons $y = x+1$. (Typage : Puisque $x \in \mathbb{Z}$ et $1 \in \mathbb{Z}$, leur somme $y=x+1$ est également un entier, donc $y \in \mathbb{Z}$).
Vérifions les deux conditions de la conjonction :

1.  **$y \neq x$ :**
    Puisque $y = x+1$, nous avons $y - x = 1 \neq 0$, d'où $y \neq x$. Cette condition est rigoureusement satisfaite.

2.  **$\forall z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \implies z \notin \mathbb{Z} \right)$ :**
    Puisque $y = x+1$, nous avons $x < y$.
    Donc, $\min(x,y) = x$ et $\max(x,y) = x+1$.
    L'intervalle ouvert $(\min(x,y), \max(x,y))$ est donc $(x, x+1)$.
    La condition devient : $\forall z \in \mathbb{R}, \left( (x < z < x+1) \implies z \notin \mathbb{Z} \right)$.

    Soit $z$ un nombre réel arbitraire tel que $x < z < x+1$. (Typage : $z \in \mathbb{R}$).
    Nous devons montrer que $z \notin \mathbb{Z}$.
    Par définition des nombres entiers, il n'existe aucun entier strictement compris entre deux entiers consécutifs. Puisque $x$ est un entier, $x+1$ est l'entier le plus petit strictement supérieur à $x$. Par conséquent, tout nombre réel $z$ qui satisfait $x < z < x+1$ ne peut pas être un entier.
    Ainsi, $z \notin \mathbb{Z}$ est une proposition vraie.

Puisque nous avons trouvé un tel $y$ (à savoir $x+1$) pour un $x$ arbitraire dans $\mathbb{Z}$, la propriété $\mathcal{P}(\mathbb{Z})$ est satisfaite.
Donc, $A = \mathbb{Z}$ est un exemple d'ensemble qui satisfait la propriété $\mathcal{P}(A)$.

## Question 3. (c) Exemple d'un ensemble $A$ satisfaisant $\neg \mathcal{P}(A)$

Nous cherchons un ensemble $A \subseteq \mathbb{R}$ non vide tel que :
$\exists x \in A, \forall y \in A, \left( y = x \lor \left( \exists z \in \mathbb{R}, \left( (\min(x,y) < z < \max(x,y)) \land z \in A \right) \right) \right)$.

Considérons l'ensemble $A = [0,1]$ (l'intervalle fermé des nombres réels de 0 à 1).
L'ensemble $[0,1]$ est un sous-ensemble non vide de $\mathbb{R}$.

**Justification :**
Nous devons trouver un $x \in A$ tel que la condition universelle sur $y$ soit vérifiée.
Choisissons $x=0$. (Typage : $x=0 \in [0,1]$).

Nous devons montrer que pour ce $x=0$, la proposition suivante est vraie :
$\forall y \in [0,1], \left( y = 0 \lor \left( \exists z \in \mathbb{R}, \left( (\min(0,y) < z < \max(0,y)) \land z \in [0,1] \right) \right) \right)$.

Soit $y$ un élément arbitraire de $A = [0,1]$. (Typage : $y \in [0,1]$).
Nous allons analyser deux cas pour $y$ :

**Cas 1 : $y=0$.**
Dans ce cas, la première disjonction $(y=0)$ est vraie. Par conséquent, l'énoncé complet de la disjonction est vrai pour ce $y$.

**Cas 2 : $y \neq 0$.**
Puisque $y \in [0,1]$ et $y \neq 0$, cela implique que $0 < y \le 1$.
Dans ce cas, la première disjonction $(y=0)$ est fausse. Nous devons donc montrer que la seconde disjonction est vraie :
$\exists z \in \mathbb{R}, \left( (\min(0,y) < z < \max(0,y)) \land z \in [0,1] \right)$.

Puisque $0 < y$, nous avons $\min(0,y) = 0$ et $\max(0,y) = y$.
La condition devient : $\exists z \in \mathbb{R}, \left( (0 < z < y) \land z \in [0,1] \right)$.

Nous devons trouver un tel $z$. Choisissons $z = \frac{y}{2}$. (Typage : $z \in \mathbb{R}$).
Vérifions les deux conditions de la conjonction pour ce choix de $z$ :

1.  **$0 < z < y$ :**
    Puisque $y > 0$, en multipliant par $\frac{1}{2}$ (qui est positif), les inégalités sont préservées :
    $0 \cdot \frac{1}{2} < y \cdot \frac{1}{2}$, ce qui donne $0 < \frac{y}{2}$.
    De plus, puisque $y > 0$, nous avons $\frac{1}{2} < 1$, donc $\frac{y}{2} < y$.
    Ainsi, $0 < z < y$ est satisfaite.

2.  **$z \in [0,1]$ :**
    Nous savons que $z = \frac{y}{2}$.
    Puisque $y \in (0,1]$, nous avons $0 < y \le 1$.
    En multipliant par $\frac{1}{2}$ : $0 \cdot \frac{1}{2} < y \cdot \frac{1}{2} \le 1 \cdot \frac{1}{2}$.
    Ceci nous donne $0 < \frac{y}{2} \le \frac{1}{2}$.
    Puisque $0 < \frac{y}{2} \le \frac{1}{2}$, et que $\frac{1}{2} \le 1$, nous déduisons par transitivité que $0 \le \frac{y}{2} \le 1$, ce qui implique formellement que $\frac{y}{2} \in [0,1]$.
    Ainsi, $z \in [0,1]$ est satisfaite.

Puisque nous avons trouvé un tel $z$ (à savoir $y/2$) pour tout $y \neq 0$, et que la propriété est vraie pour $y=0$, la condition pour $x=0$ est entièrement vérifiée.
Par conséquent, il existe un $x \in [0,1]$ (en l'occurrence $x=0$) tel que la propriété $\neg \mathcal{P}(A)$ est satisfaite.
Donc, $A = [0,1]$ est un exemple d'ensemble qui satisfait la propriété $\neg \mathcal{P}(A)$.

---