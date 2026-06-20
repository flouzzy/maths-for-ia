Absolument. En tant que Professeur de Mathématiques à l'ENS, je vous propose l'exercice suivant, conçu pour tester la maîtrise la plus fine de la quantification et de la négation.

---

# Exercice 9 : La Propriété de "Médiation Indépendante"

**Niveau de difficulté :** $\star \star \star \star \star$

## Énoncé

Soit $E$ un ensemble non vide et $R$ une relation binaire sur $E$, c'est-à-dire $R \subseteq E \times E$.

On définit la propriété $\mathcal{P}(E, R)$ comme suit :
$$ \mathcal{P}(E, R) \quad \equiv \quad \forall x \in E, \exists y \in E, \forall z \in E, \left( (x R z \land z \neq x) \implies \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) $$

1.  Écrire la négation de la propriété $\mathcal{P}(E, R)$, notée $\neg \mathcal{P}(E, R)$, en déplaçant tous les symboles de négation ($\neg$) le plus à l'intérieur possible de l'expression logique, jusqu'aux prédicats atomiques.

2.  Donner un exemple concret d'ensemble $E$ et de relation $R$ pour lesquels la propriété $\mathcal{P}(E, R)$ est **vraie**. Justifier rigoureusement votre choix.

3.  Donner un exemple concret d'ensemble $E$ et de relation $R$ pour lesquels la propriété $\mathcal{P}(E, R)$ est **fausse** (c'est-à-dire $\neg \mathcal{P}(E, R)$ est vraie). Justifier rigoureusement votre choix.

---

## Correction Ultra-Détaillée

### 1. Négation de la propriété $\mathcal{P}(E, R)$

La propriété $\mathcal{P}(E, R)$ est donnée par :
$$ \mathcal{P}(E, R) \quad \equiv \quad \forall x \in E, \exists y \in E, \forall z \in E, \left( (x R z \land z \neq x) \implies \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) $$

Nous allons appliquer les règles de négation pas à pas, en déplaçant le symbole de négation vers l'intérieur.

**Étape 1 : Négation du premier quantificateur universel.**
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \neg \left( \forall x \in E, \exists y \in E, \forall z \in E, \left( (x R z \land z \neq x) \implies \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) \right) $$
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \neg \left( \exists y \in E, \forall z \in E, \left( (x R z \land z \neq x) \implies \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) \right) $$

**Étape 2 : Négation du quantificateur existentiel.**
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \forall y \in E, \neg \left( \forall z \in E, \left( (x R z \land z \neq x) \implies \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) \right) $$

**Étape 3 : Négation du quantificateur universel.**
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \forall y \in E, \exists z \in E, \neg \left( (x R z \land z \neq x) \implies \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) $$

**Étape 4 : Négation d'une implication.**
Rappel : $\neg (A \implies B) \equiv A \land \neg B$.
Ici, $A \equiv (x R z \land z \neq x)$ et $B \equiv \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z)$.
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \forall y \in E, \exists z \in E, \left( (x R z \land z \neq x) \land \neg \left( \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) \right) $$

**Étape 5 : Négation du quantificateur existentiel.**
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \forall y \in E, \exists z \in E, \left( (x R z \land z \neq x) \land \forall w \in E, \neg \left( (y R w \land w R z \land w \neq y \land w \neq z) \right) \right) $$

**Étape 6 : Négation d'une conjonction.**
Rappel : $\neg (A \land B \land C \land D) \equiv \neg A \lor \neg B \lor \neg C \lor \neg D$.
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \forall y \in E, \exists z \in E, \left( (x R z \land z \neq x) \land \forall w \in E, \left( \neg (y R w) \lor \neg (w R z) \lor \neg (w \neq y) \lor \neg (w \neq z) \right) \right) $$
En utilisant la notation standard pour la négation des prédicats atomiques :
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \forall y \in E, \exists z \in E, \left( (x R z \land z \neq x) \land \forall w \in E, \left( (y \not R w) \lor (w \not R z) \lor (w = y) \lor (w = z) \right) \right) $$

Pour une meilleure lisibilité, on peut réécrire la dernière partie comme une implication :
Rappel : $(A \lor B \lor C \lor D) \equiv \neg ( \neg A \land \neg B \land \neg C \land \neg D)$.
Donc $\left( (y \not R w) \lor (w \not R z) \lor (w = y) \lor (w = z) \right)$ est équivalent à $\neg \left( (y R w) \land (w R z) \land (w \neq y) \land (w \neq z) \right)$.
Ceci signifie que si $(y R w \land w R z)$ est vrai, alors nécessairement $(w=y \lor w=z)$.

Ainsi, la négation finale est :
$$ \neg \mathcal{P}(E, R) \quad \equiv \quad \exists x \in E, \forall y \in E, \exists z \in E, \left( (x R z \land z \neq x) \land \forall w \in E, \left( (y R w \land w R z) \implies (w = y \lor w = z) \right) \right) $$

### 2. Exemple où $\mathcal{P}(E, R)$ est vraie

Soit $E = \{1, 2, 3\}$.
Soit $R$ la relation binaire sur $E$ définie par $R = \{(i,j) \in E \times E \mid i \neq j\}$.
Autrement dit, $R = \{(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)\}$. C'est la relation de "différence" ou un graphe complet sans boucles.

Nous devons montrer que :
$$ \forall x \in E, \exists y \in E, \forall z \in E, \left( (x R z \land z \neq x) \implies \exists w \in E, (y R w \land w R z \land w \neq y \land w \neq z) \right) $$

Prenons un $x \in E$ arbitraire. Sans perte de généralité, choisissons $x=1$.
Nous devons trouver un $y \in E$. Choisissons $y=2$.

Maintenant, nous devons vérifier la condition pour tout $z \in E$.
La prémisse de l'implication est $(x R z \land z \neq x)$.
Puisque $x=1$, cette prémisse devient $(1 R z \land z \neq 1)$.
Les éléments $z \in E$ qui satisfont cette prémisse sont $z=2$ et $z=3$ (car $1 R 2$ et $1 R 3$ sont vrais, et $2 \neq 1$, $3 \neq 1$).

**Cas 1 : $z=2$.**
La prémisse $(1 R 2 \land 2 \neq 1)$ est vraie.
Nous devons montrer qu'il existe un $w \in E$ tel que $(y R w \land w R z \land w \neq y \land w \neq z)$.
Avec $y=2$ et $z=2$, la condition devient :
$\exists w \in E, (2 R w \land w R 2 \land w \neq 2 \land w \neq 2)$.
Ceci se simplifie en : $\exists w \in E, (2 R w \land w R 2 \land w \neq 2)$.

Cherchons un tel $w$.
*   Si $w=1$:
    *   $2 R 1$ est vraie (car $2 \neq 1$).
    *   $1 R 2$ est vraie (car $1 \neq 2$).
    *   $w \neq 2$ est vraie (car $1 \neq 2$).
    Donc, $w=1$ satisfait toutes les conditions.
*   Si $w=3$:
    *   $2 R 3$ est vraie (car $2 \neq 3$).
    *   $3 R 2$ est vraie (car $3 \neq 2$).
    *   $w \neq 2$ est vraie (car $3 \neq 2$).
    Donc, $w=3$ satisfait toutes les conditions.
Nous avons trouvé un $w$ (par exemple $w=1$). La condition est donc satisfaite pour $z=2$.

**Cas 2 : $z=3$.**
La prémisse $(1 R 3 \land 3 \neq 1)$ est vraie.
Nous devons montrer qu'il existe un $w \in E$ tel que $(y R w \land w R z \land w \neq y \land w \neq z)$.
Avec $y=2$ et $z=3$, la condition devient :
$\exists w \in E, (2 R w \land w R 3 \land w \neq 2 \land w \neq 3)$.

Cherchons un tel $w$.
*   Si $w=1$:
    *   $2 R 1$ est vraie (car $2 \neq 1$).
    *   $1 R 3$ est vraie (car $1 \neq 3$).
    *   $w \neq 2$ est vraie (car $1 \neq 2$).
    *   $w \neq 3$ est vraie (car $1 \neq 3$).
    Donc, $w=1$ satisfait toutes les conditions.
*   Si $w=2$: $w \neq 2$ est fausse. $w=2$ ne convient pas.
*   Si $w=3$: $w \neq 3$ est fausse. $w=3$ ne convient pas.
Nous avons trouvé un $w$ (à savoir $w=1$). La condition est donc satisfaite pour $z=3$.

Puisque nous avons montré que pour $x=1$, le choix $y=2$ fonctionne pour tous les $z$ pertinents, la propriété est vraie pour $x=1$.

Nous devons également vérifier de manière explicite les autres cas pour $x$ :
*   Si $x=2$, nous pouvons choisir $y=3$.
    *   Pour $z=1$: $2 R 1 \land 1 \neq 2$. On cherche $w$ tel que $3 R w \land w R 1 \land w \neq 3 \land w \neq 1$. $w=2$ convient (car $3 R 2$, $2 R 1$, $2 \neq 3$, $2 \neq 1$).
    *   Pour $z=3$: $2 R 3 \land 3 \neq 2$. On cherche $w$ tel que $3 R w \land w R 3 \land w \neq 3$. $w=1$ ou $w=2$ conviennent.
*   Si $x=3$, nous pouvons choisir $y=1$.
    *   Pour $z=1$: $3 R 1 \land 1 \neq 3$. On cherche $w$ tel que $1 R w \land w R 1 \land w \neq 1$. $w=2$ ou $w=3$ conviennent.
    *   Pour $z=2$: $3 R 2 \land 2 \neq 3$. On cherche $w$ tel que $1 R w \land w R 2 \land w \neq 1 \land w \neq 2$. $w=3$ convient (car $1 R 3$, $3 R 2$, $3 \neq 1$, $3 \neq 2$).

Dans tous les cas, pour chaque $x \in E$, nous avons pu trouver un $y \in E$ qui satisfait la condition pour tous les $z$ pertinents.
Donc, la propriété $\mathcal{P}(E, R)$ est vraie pour cet exemple.

### 3. Exemple où $\mathcal{P}(E, R)$ est fausse (c'est-à-dire $\neg \mathcal{P}(E, R)$ est vraie)

Nous devons montrer que :
$$ \exists x \in E, \forall y \in E, \exists z \in E, \left( (x R z \land z \neq x) \land \forall w \in E, \left( (y R w \land w R z) \implies (w = y \lor w = z) \right) \right) $$

Soit $E = \{a, b, c\}$.
Soit $R$ la relation binaire sur $E$ définie par $R = \{(a,b), (b,c)\}$. C'est une chaîne linéaire.

Nous devons trouver un $x \in E$. Choisissons $x = a$.

Maintenant, nous devons montrer que pour tout $y \in E$, il existe un $z \in E$ tel que la condition entre parenthèses est vraie.
La condition est : $(x R z \land z \neq x) \land \forall w \in E, \left( (y R w \land w R z) \implies (w = y \lor w = z) \right)$.
Avec $x=a$, la première partie de la conjonction est $(a R z \land z \neq a)$.
Le seul $z \in E$ qui satisfait $(a R z \land z \neq a)$ est $z=b$. (Car $a R b$ est vrai et $b \neq a$. Pour $z=a$ ou $z=c$, la prémisse est fausse).
Donc, nous fixons $z=b$.

Nous devons maintenant montrer que pour tout $y \in E$, la condition est vraie avec $x=a$ et $z=b$.
La condition devient : $(a R b \land b \neq a) \land \forall w \in E, \left( (y R w \land w R b) \implies (w = y \lor w = b) \right)$.
La première partie $(a R b \land b \neq a)$ est vraie.
Nous devons donc montrer que pour tout $y \in E$, la deuxième partie est vraie :
$$ \forall w \in E, \left( (y R w \land w R b) \implies (w = y \lor w = b) \right) $$

Nous allons vérifier cette condition pour chaque $y \in E$.

**Cas 1 : $y=a$.**
Nous devons montrer : $\forall w \in E, \left( (a R w \land w R b) \implies (w = a \lor w = b) \right)$.
*   Prenons $w=a$:
    *   $(a R a \land a R b)$ est fausse (car $a R a$ est fausse). L'implication est vraie.
*   Prenons $w=b$:
    *   $(a R b \land b R b)$ est fausse (car $b R b$ est fausse). L'implication est vraie.
*   Prenons $w=c$:
    *   $(a R c \land c R b)$ est fausse (car $a R c$ est fausse et $c R b$ est fausse). L'implication est vraie.
Puisque l'implication est vraie pour tous les $w \in E$, la condition est satisfaite pour $y=a$.

**Cas 2 : $y=b$.**
Nous devons montrer : $\forall w \in E, \left( (b R w \land w R b) \implies (w = b \lor w = b) \right)$.
Ceci se simplifie en : $\forall w \in E, \left( (b R w \land w R b) \implies (w = b) \right)$.
*   Prenons $w=a$:
    *   $(b R a \land a R b)$ est fausse (car $b R a$ est fausse). L'implication est vraie.
*   Prenons $w=b$:
    *   $(b R b \land b R b)$ est fausse (car $b R b$ est fausse). L'implication est vraie.
*   Prenons $w=c$:
    *   $(b R c \land c R b)$ est fausse (car $c R b$ est fausse). L'implication est vraie.
Puisque l'implication est vraie pour tous les $w \in E$, la condition est satisfaite pour $y=b$.

**Cas 3 : $y=c$.**
Nous devons montrer : $\forall w \in E, \left( (c R w \land w R b) \implies (w = c \lor w = b) \right)$.
*   Prenons $w=a$:
    *   $(c R a \land a R b)$ est fausse (car $c R a$ est fausse). L'implication est vraie.
*   Prenons $w=b$:
    *   $(c R b \land b R b)$ est fausse (car $c R b$ est fausse et $b R b$ est fausse). L'implication est vraie.
*   Prenons $w=c$:
    *   $(c R c \land c R b)$ est fausse (car $c R c$ est fausse et $c R b$ est fausse). L'implication est vraie.
Puisque l'implication est vraie pour tous les $w \in E$, la condition est satisfaite pour $y=c$.

Nous avons trouvé un $x=a$ tel que pour tout $y \in E$, il existe un $z=b$ (qui satisfait $x R z \land z \neq x$) tel que pour tout $w \in E$, si $y R w \land w R z$, alors $w=y$ ou $w=z$.
En d'autres termes, pour la relation $R = \{(a,b), (b,c)\}$, il n'y a jamais de "chemin de médiation" de longueur 2 entre $y$ et $z=b$ qui utilise un $w$ distinct de $y$ et $z$. Les seuls chemins possibles sont directs ($y R b$) ou impliquent $y$ ou $b$ comme point intermédiaire. Par exemple, pour $y=a$ et $z=b$, il n'y a pas de $w$ tel que $a R w \land w R b$. Le seul chemin est $a R b$ directement.

Donc, la propriété $\neg \mathcal{P}(E, R)$ est vraie pour cet exemple.

---