---
uuid: "jalon-1"
title: "Logique formelle, connecteurs, tables de vérité et calcul des propositions"
year: 1
trimester: 1
tags:
  - math/fondations
  - ia/logique-symbolique
prev: "None"
next: "[[Jalon 2 (Méthodes de raisonnement).md]]"
---
# Jalon 1 : Logique formelle, connecteurs, tables de vérité et calcul des propositions

## 1. Présentation du concept clé

La logique formelle est la science des structures de raisonnement valides. Pour aborder ce concept de manière géométrique et intuitive, libérée du formalisme brut, imaginons un labyrinthe géant représentant l'ensemble des possibles. Ce labyrinthe est composé d'une multitude d'aiguillages et de portes commandés à distance. Chaque porte ne peut être que dans deux états stables : ouverte (valeur de vérité Vrai, notée $1$) ou fermée (valeur de vérité Faux, notée $0$).

La métaphore fondamentale de la logique propositionnelle réside dans la notion de flot ou de flux d'information à travers un réseau d'aiguillages. Considérons un fluide circulant dans ce réseau. Si nous plaçons deux vannes à la suite sur une même canalisation, le fluide ne passera que si la première vanne ET la seconde vanne sont ouvertes. C'est l'essence du connecteur de conjonction ($\land$). Si nous plaçons ces deux vannes en parallèle sur deux embranchements distincts reliant les mêmes points, il suffit que la première vanne OU la seconde vanne soit ouverte pour que le fluide traverse. C'est l'essence du connecteur de disjonction ($\lor$).

Pourquoi a-t-on ressenti le besoin d'inventer un tel formalisme ? Le langage naturel (le français, l'anglais, etc.) est parsemé d'ambiguïtés sémantiques. Le mot "ou", par exemple, exprime tantôt une disjonction exclusive ("fromage ou dessert", mais pas les deux), tantôt une disjonction inclusive ("recherche programmeur maîtrisant le C++ ou le Python", de préférence les deux). De plus, l'esprit humain est sujet aux biais cognitifs et aux sophismes. La création d'une langue artificielle universelle, libre de toute ambiguïté contextuelle, a permis de détacher la forme d'un raisonnement de son contenu. C'est le projet leibnizien de la *characteristica universalis* et du *calculus ratiocinator* : transformer toute dispute philosophique ou scientifique en un simple calcul mathématique. "Calculons !" disait Leibniz. Gottlob Frege, à la fin du XIXe siècle, a concrétisé ce rêve avec son *Idéographie* (*Begriffsschrift*), jetant les bases de la logique mathématique moderne.

Dans cette optique, les variables propositionnelles agissent comme des interrupteurs élémentaires, et les formules logiques sont des montages complexes d'interrupteurs. Construire une table de vérité revient à dresser la carte complète des tensions de notre circuit pour toutes les configurations possibles des interrupteurs d'entrée. Si un circuit produit une tension de sortie positive (Vrai) quelle que soit la position des interrupteurs d'entrée, nous avons affaire à une tautologie : une vérité structurelle inébranlable, indépendante du monde réel. À l'inverse, si la sortie est toujours nulle, c'est une contradiction.

Cette dissociation fondamentale entre la syntaxe (la forme de la formule) et la sémantique (sa signification ou sa valeur de vérité dans un monde donné) est la clé de voûte de la logique. Elle montre comment des règles de manipulation purement symboliques peuvent refléter fidèlement des réalités sémantiques. En manipulant des symboles selon des règles strictes, sans même savoir ce qu'ils représentent, on préserve la vérité. C'est cette nature purement mécanique qui permettra plus tard aux ordinateurs de manipuler des concepts abstraits et de raisonner de manière autonome.

---

## 2. Formalisation & Rigueur Académique

Pour structurer rigoureusement le calcul des propositions (ou logique propositionnelle classique), nous devons définir précisément sa syntaxe (l'ensemble des formules bien formées) et sa sémantique (l'évaluation de ces formules).

### A. Syntaxe du calcul des propositions

Soit $\mathcal{P}$ un ensemble dénombrable de symboles appelés **variables propositionnelles** (ou atomes), généralement notés $p, q, r, \dots$ ou $p_1, p_2, \dots$

On définit l'alphabet de notre langage par la réunion de $\mathcal{P}$, des connecteurs logiques $\{\neg, \lor, \land, \Rightarrow, \Leftrightarrow\}$ et des symboles de ponctuation $\{$ ( , ) $\}$.

L'ensemble $\mathcal{F}$ des **formules bien formées** (FBF) est défini de manière inductive comme le plus petit ensemble de mots sur cet alphabet satisfaisant aux règles suivantes :
1. **Règle de base :** Si $p \in \mathcal{P}$, alors $p \in \mathcal{F}$ (les variables propositionnelles sont des formules atomiques).
2. **Règle d'induction unaire :** Si $A \in \mathcal{F}$, alors $(\neg A) \in \mathcal{F}$.
3. **Règle d'induction binaire :** Si $A \in \mathcal{F}$ et $B \in \mathcal{F}$, alors $(A \land B) \in \mathcal{F}$, $(A \lor B) \in \mathcal{F}$, $(A \Rightarrow B) \in \mathcal{F}$ et $(A \Leftrightarrow B) \in \mathcal{F}$.

*Remarque sur l'écriture :* Pour alléger la lecture, on omet souvent les parenthèses extérieures et on établit des règles de priorité des connecteurs (le connecteur $\neg$ est plus prioritaire que $\land$ et $\lor$, qui sont plus prioritaires que $\Rightarrow$ et $\Leftrightarrow$).

Le **Théorème de lecture unique** (ou d'auto-analyse) garantit que pour toute formule bien formée non atomique $F$, il existe un unique connecteur principal et d'uniques sous-formules directes permettant de la construire. Cela permet de définir des propriétés sur les formules par induction structurelle et des fonctions par récurrence sur la complexité des formules.

### B. Sémantique et Évaluation

La sémantique de la logique propositionnelle repose sur le principe de bivalence (les formules sont soit vraies, soit fausses) et de compositionnalité (la valeur de vérité d'une formule complexe dépend uniquement de celle de ses sous-formules).

On appelle **valuation** (ou interprétation) une application $v : \mathcal{P} \to \{0, 1\}$. L'ensemble des valuations est noté $\mathcal{V} = \{0, 1\}^\mathcal{P}$.

Toute valuation $v$ s'étend de manière unique en une application $\bar{v} : \mathcal{F} \to \{0, 1\}$ (que l'on notera également $v$ par abus de langage) définie par récurrence structurelle :
- Pour tout $p \in \mathcal{P}$, $\bar{v}(p) = v(p)$.
- $\bar{v}((\neg A)) = 1 - \bar{v}(A)$.
- $\bar{v}((A \land B)) = \min(\bar{v}(A), \bar{v}(B))$.
- $\bar{v}((A \lor B)) = \max(\bar{v}(A), \bar{v}(B))$.
- $\bar{v}((A \Rightarrow B)) = \max(1 - \bar{v}(A), \bar{v}(B))$.
- $\bar{v}((A \Leftrightarrow B)) = 1 - |\bar{v}(A) - \bar{v}(B)|$.

Une formule $A$ est dite **satisfaisable** s'il existe une valuation $v$ telle que $v(A) = 1$. Dans ce cas, $v$ est appelée un **modèle** de $A$ (noté $v \models A$). Un ensemble de formules $\Sigma$ est satisfaisable s'il existe une valuation qui est modèle de toutes les formules de $\Sigma$.

Une formule $A$ est une **tautologie** (ou est universellement valide) si pour toute valuation $v$, $v(A) = 1$. On note alors $\models A$.
Une formule $A$ est une **contradiction** (ou est antilogie) si pour toute valuation $v$, $v(A) = 0$.

Soit $\Sigma \subseteq \mathcal{F}$ un ensemble de formules et $A \in \mathcal{F}$ une formule. On dit que $A$ est une **conséquence sémantique** de $\Sigma$, notée $\Sigma \models A$, si pour toute valuation $v$, si $v(B) = 1$ pour tout $B \in \Sigma$, alors $v(A) = 1$.

### C. Systèmes Formels de Déduction (Syntaxe)

Parallèlement à la sémantique, on définit des systèmes de preuve purement syntaxiques (comme les systèmes de Hilbert, la déduction naturelle ou le calcul des séquents). Une preuve formelle d'une formule $A$ sous les hypothèses $\Sigma$ est une suite finie de formules se terminant par $A$, où chaque formule est soit un axiome du système, soit une formule de $\Sigma$, soit obtenue à partir de formules précédentes par une règle d'inférence (comme le *Modus Ponens* : de $X$ et $X \Rightarrow Y$, on déduit $Y$). On note alors $\Sigma \vdash A$.

Les propriétés fondamentales reliant sémantique et syntaxe sont :
- **Théorème de Correction (Soundness) :** Si $\Sigma \vdash A$, alors $\Sigma \models A$. (Tout ce qui est démontrable est vrai).
- **Théorème de Complétude (Completeness) :** Si $\Sigma \models A$, alors $\Sigma \vdash A$. (Tout ce qui est vrai est démontrable).

---

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

Nous présentons ici trois démonstrations fondamentales du calcul des propositions, rédigées avec une rigueur absolue et sans aucune ellipse mathématique.

### Démonstration 1 : Loi de De Morgan $\neg(A \lor B) \Leftrightarrow (\neg A \land \neg B)$

Soit $v$ une valuation quelconque. Nous voulons démontrer que pour toutes formules $A$ et $B$, $v(\neg(A \lor B)) = v(\neg A \land \neg B)$. Nous allons procéder par étude exhaustive des cas (valeurs de vérité de $A$ et $B$).

1. **Cas 1 : $v(A) = 1$ et $v(B) = 1$**
   - Évaluons le membre gauche :
     $$v(A \lor B) = \max(v(A), v(B)) = \max(1, 1) = 1$$
     $$v(\neg(A \lor B)) = 1 - v(A \lor B) = 1 - 1 = 0$$
   - Évaluons le membre droit :
     $$v(\neg A) = 1 - v(A) = 1 - 1 = 0$$
     $$v(\neg B) = 1 - v(B) = 1 - 1 = 0$$
     $$v(\neg A \land \neg B) = \min(v(\neg A), v(\neg B)) = \min(0, 0) = 0$$
   - Les deux valeurs coïncident : $0 = 0$.

2. **Cas 2 : $v(A) = 1$ et $v(B) = 0$**
   - Évaluons le membre gauche :
     $$v(A \lor B) = \max(v(A), v(B)) = \max(1, 0) = 1$$
     $$v(\neg(A \lor B)) = 1 - v(A \lor B) = 1 - 1 = 0$$
   - Évaluons le membre droit :
     $$v(\neg A) = 1 - v(A) = 1 - 1 = 0$$
     $$v(\neg B) = 1 - v(B) = 1 - 0 = 1$$
     $$v(\neg A \land \neg B) = \min(v(\neg A), v(\neg B)) = \min(0, 1) = 0$$
   - Les deux valeurs coïncident : $0 = 0$.

3. **Cas 3 : $v(A) = 0$ et $v(B) = 1$**
   - Évaluons le membre gauche :
     $$v(A \lor B) = \max(v(A), v(B)) = \max(0, 1) = 1$$
     $$v(\neg(A \lor B)) = 1 - v(A \lor B) = 1 - 1 = 0$$
   - Évaluons le membre droit :
     $$v(\neg A) = 1 - v(A) = 1 - 0 = 1$$
     $$v(\neg B) = 1 - v(B) = 1 - 1 = 0$$
     $$v(\neg A \land \neg B) = \min(v(\neg A), v(\neg B)) = \min(1, 0) = 0$$
   - Les deux valeurs coïncident : $0 = 0$.

4. **Cas 4 : $v(A) = 0$ et $v(B) = 0$**
   - Évaluons le membre gauche :
     $$v(A \lor B) = \max(v(A), v(B)) = \max(0, 0) = 0$$
     $$v(\neg(A \lor B)) = 1 - v(A \lor B) = 1 - 0 = 1$$
   - Évaluons le membre droit :
     $$v(\neg A) = 1 - v(A) = 1 - 0 = 1$$
     $$v(\neg B) = 1 - v(B) = 1 - 0 = 1$$
     $$v(\neg A \land \neg B) = \min(v(\neg A), v(\neg B)) = \min(1, 1) = 1$$
   - Les deux valeurs coïncident : $1 = 1$.

Dans tous les cas possibles, $v(\neg(A \lor B)) = v(\neg A \land \neg B)$. La formule $\neg(A \lor B) \Leftrightarrow (\neg A \land \neg B)$ est donc une tautologie.

---

### Démonstration 2 : Distributivité de la disjonction par rapport à la conjonction : $A \lor (B \land C) \Leftrightarrow (A \lor B) \land (A \lor C)$

Soit $v$ une valuation. Posons $x = v(A)$, $y = v(B)$ et $z = v(C)$, où $x, y, z \in \{0, 1\}$.
Nous devons prouver l'égalité algébrique suivante dans l'algèbre de Boole $\{0, 1\}$ :
$$\max(x, \min(y, z)) = \min(\max(x, y), \max(x, z))$$

Analysons les cas possibles selon la valeur de $x$ :

1. **Cas 1 : $x = 1$**
   - Évaluons le membre de gauche (MG) :
     $$\text{MG} = \max(1, \min(y, z))$$
     Puisque pour tout $t \in \{0, 1\}$, $\max(1, t) = 1$, nous avons :
     $$\text{MG} = 1$$
   - Évaluons le membre de droite (MD) :
     $$\max(1, y) = 1 \quad \text{et} \quad \max(1, z) = 1$$
     D'où :
     $$\text{MD} = \min(1, 1) = 1$$
   - Ainsi, $\text{MG} = \text{MD}$.

2. **Cas 2 : $x = 0$**
   - Évaluons le membre de gauche (MG) :
     $$\text{MG} = \max(0, \min(y, z))$$
     Puisque pour tout $t \in \{0, 1\}$, $\max(0, t) = t$, nous avons :
     $$\text{MG} = \min(y, z)$$
   - Évaluons le membre de droite (MD) :
     $$\max(0, y) = y \quad \text{et} \quad \max(0, z) = z$$
     D'où :
     $$\text{MD} = \min(y, z)$$
   - Ainsi, $\text{MG} = \text{MD}$.

Dans tous les cas, l'équivalence est vérifiée, ce qui valide la distributivité de $\lor$ sur $\land$.

---

### Démonstration 3 : Théorème de compacité de la logique propositionnelle

> **Théorème :**
> Soit $\Sigma \subseteq \mathcal{F}$ un ensemble infini de formules. Si tout sous-ensemble fini $\Sigma_0 \subseteq \Sigma$ est satisfaisable, alors $\Sigma$ lui-même est satisfaisable.

**Démonstration par le théorème de Tychonoff :**

Soit $\mathcal{P}$ l'ensemble des variables propositionnelles apparaissant dans $\Sigma$. L'ensemble des valuations de $\mathcal{P}$ est l'ensemble $\mathcal{V} = \{0, 1\}^\mathcal{P}$.
Nous pouvons munir l'ensemble discret $\{0, 1\}$ de la topologie discrète (qui est compacte car l'espace est fini).
Par le **Théorème de Tychonoff**, l'espace produit $\mathcal{V} = \{0, 1\}^\mathcal{P}$ muni de la topologie produit est compact (espace de Cantor).

Pour chaque formule $A \in \Sigma$, définissons l'ensemble $M(A) = \{v \in \mathcal{V} \mid v(A) = 1\}$, c'est-à-dire l'ensemble des modèles de $A$.
Puisque la syntaxe d'une formule $A$ ne fait intervenir qu'un nombre fini de variables propositionnelles, la valeur de vérité de $A$ ne dépend que d'une projection finie de $\mathcal{V}$. Un sous-ensemble défini par un nombre fini de coordonnées dans une topologie produit de topologies discrètes est fermé (et même ouvert). Donc, $M(A)$ est un fermé de l'espace compact $\mathcal{V}$.

L'hypothèse selon laquelle tout sous-ensemble fini $\Sigma_0 \subseteq \Sigma$ est satisfaisable se traduit sémantiquement par :
$$\bigcap_{A \in \Sigma_0} M(A) \neq \emptyset$$

Considérons la famille de fermés de l'espace compact $\mathcal{V}$ définie par $\mathcal{C} = \{ M(A) \mid A \in \Sigma \}$.
D'après le résultat ci-dessus, cette famille possède la **propriété de l'intersection finie** (toute intersection d'un nombre fini de membres de la famille est non vide).

Par caractérisation de la compacité, une famille de fermés d'un espace compact ayant la propriété de l'intersection finie a une intersection totale non vide :
$$\bigcap_{A \in \Sigma} M(A) \neq \emptyset$$

Il existe donc une valuation $v^* \in \bigcap_{A \in \Sigma} M(A)$. Cette valuation $v^*$ est modèle de toutes les formules de $\Sigma$. Par conséquent, $\Sigma$ est satisfaisable. $\blacksquare$

---

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Preuve de la Loi de Peirce

**Énoncé :** Démontrer algébriquement, puis à l'aide de l'évaluation sémantique, que la formule $((A \Rightarrow B) \Rightarrow A) \Rightarrow A$ (Loi de Peirce) est une tautologie.

**Correction pas-à-pas :**

1. **Méthode sémantique :**
   Soit $v$ une valuation. Posons $a = v(A)$ et $b = v(B)$. Nous voulons évaluer $v(((A \Rightarrow B) \Rightarrow A) \Rightarrow A)$.
   Rappelons que $v(X \Rightarrow Y) = 1$ ssi $v(X) \le v(Y)$, ce qui s'écrit algébriquement $v(X \Rightarrow Y) = \max(1 - v(X), v(Y))$.
   
   - **Cas 1 : $a = 1$.**
     Le membre final de notre implication principale est la formule $A$. Or sa valeur est $a = 1$.
     Une implication de la forme $X \Rightarrow Y$ prend la valeur $1$ si la conséquence $Y$ vaut $1$, car $\max(1-v(X), 1) = 1$.
     Puisque la conséquence de notre implication principale est $A$ et que $v(A) = 1$, la formule entière prend la valeur $1$.
     
   - **Cas 2 : $a = 0$.**
     - Évaluons d'abord l'implication la plus interne :
       $$v(A \Rightarrow B) = \max(1 - a, b) = \max(1 - 0, b) = \max(1, b) = 1$$
     - Évaluons le membre gauche de l'implication principale :
       $$v((A \Rightarrow B) \Rightarrow A) = \max(1 - v(A \Rightarrow B), a) = \max(1 - 1, 0) = \max(0, 0) = 0$$
     - Évaluons enfin l'implication principale :
       $$v(((A \Rightarrow B) \Rightarrow A) \Rightarrow A) = \max(1 - v((A \Rightarrow B) \Rightarrow A), a) = \max(1 - 0, 0) = \max(1, 0) = 1$$

   Dans les deux cas possibles, la valeur de vérité de la formule est $1$. C'est donc une tautologie.

2. **Méthode algébrique (Simplification propositionnelle) :**
   Utilisons l'équivalence $X \Rightarrow Y \equiv \neg X \lor Y$.
   - Étape 1 : Réécriture de l'implication interne :
     $$(A \Rightarrow B) \Rightarrow A \equiv \neg(\neg A \lor B) \lor A$$
   - Étape 2 : Application de la loi de De Morgan sur la négation externe :
     $$\neg(\neg A \lor B) \lor A \equiv (\neg\neg A \land \neg B) \lor A \equiv (A \land \neg B) \lor A$$
   - Étape 3 : Par absorption dans l'algèbre de Boole, $(A \land \neg B) \lor A \equiv A$.
     *Justification pas-à-pas de l'absorption :*
     $$(A \land \neg B) \lor A \equiv (A \land \neg B) \lor (A \land 1) \equiv A \land (\neg B \lor 1) \equiv A \land 1 \equiv A$$
   - Étape 4 : Substituons ce résultat dans la formule complète :
     $$((A \Rightarrow B) \Rightarrow A) \Rightarrow A \equiv A \Rightarrow A$$
   - Étape 5 : Simplifions $A \Rightarrow A$ :
     $$A \Rightarrow A \equiv \neg A \lor A \equiv 1$$
   La formule est bien équivalente à la constante Vrai, c'est une tautologie.

---

### Exercice 2 : Complétude fonctionnelle du connecteur de Sheffer (NAND)

**Énoncé :** On définit le connecteur binaire $\mid$ (appelé barre de Sheffer ou NAND) par la table de vérité suivante : $v(A \mid B) = 1 - \min(v(A), v(B))$.
Démontrer que le singleton $\{\mid\}$ est un système complet de connecteurs (c'est-à-dire que n'importe quelle formule propositionnelle peut s'écrire uniquement à l'aide de ce connecteur).

**Correction pas-à-pas :**

1. **Rappel théorique :**
   On sait que le couple de connecteurs $\{\neg, \land\}$ est fonctionnellement complet. Pour montrer que $\{\mid\}$ est complet, il suffit d'exprimer les opérations de négation ($\neg$) et de conjonction ($\land$) en utilisant exclusivement le connecteur $\mid$.

2. **Expression de la négation $\neg A$ :**
   Montrons que $\neg A$ est équivalent à $A \mid A$.
   Soit $v$ une valuation quelconque.
   $$v(A \mid A) = 1 - \min(v(A), v(A)) = 1 - v(A)$$
   Or, $v(\neg A) = 1 - v(A)$.
   Les deux évaluations coïncident. Nous avons donc :
   $$\neg A \equiv A \mid A$$

3. **Expression de la conjonction $A \land B$ :**
   Montrons que $A \land B$ est équivalent à $(A \mid B) \mid (A \mid B)$.
   Soit $v$ une valuation.
   Posons $X = A \mid B$. Par la définition de la négation établie au point précédent :
   $$v(X \mid X) = 1 - v(X)$$
   Remplaçons $v(X)$ par sa définition :
   $$v(X) = 1 - \min(v(A), v(B)) = v(\neg(A \land B))$$
   D'où :
   $$v(X \mid X) = 1 - (1 - \min(v(A), v(B))) = \min(v(A), v(B)) = v(A \land B)$$
   Ainsi, les formules coïncident. Nous avons établi :
   $$A \land B \equiv (A \mid B) \mid (A \mid B)$$

4. **Conclusion :**
   Puisque nous pouvons traduire la négation ($\neg$) et la conjonction ($\land$) uniquement à l'aide de la barre de Sheffer, et que le système $\{\neg, \land\}$ est complet, le singleton $\{\mid\}$ est à son tour un système complet de connecteurs.

---

## 5. Ancrage & Application en Intelligence Artificielle

La logique propositionnelle, bien que formulée au XIXe siècle, est au cœur des révolutions technologiques de l'Intelligence Artificielle contemporaine, qu'elle soit symbolique ou hybride.

### Le SAT-Solving : Le moteur de l'IA symbolique

Le problème de la décidabilité de la satisfaisabilité d'une formule propositionnelle (problème **SAT**) est le premier problème à avoir été prouvé **NP-complet** par Stephen Cook (1971) et Leonid Levin. Malgré cette complexité théorique redoutable en pire des cas, les chercheurs en IA ont développé des moteurs de résolution de contraintes logiques d'une efficacité spectaculaire (les **SAT-Solvers**), capables de traiter des formules comportant des millions de variables et de clauses.

Le cœur de ces moteurs repose sur l'algorithme historique **DPLL** (Davis-Putnam-Logemann-Loveland) et sa version moderne **CDCL** (Conflict-Driven Clause Learning). L'algorithme opère sur des formules écrites sous Forme Normale Conjonctive (CNF) – c'est-à-dire des conjonctions de clauses, où chaque clause est une disjonction de littéraux (variables ou négation de variables).
Le principe du CDCL est le suivant :
1. **Assignation de variables (décisions) :** On choisit une variable et on lui affecte arbitrairement une valeur ($0$ ou $1$).
2. **Propagation unitaire (Boolean Constraint Propagation - BCP) :** Si une clause ne contient plus qu'un littéral non assigné, cette variable doit être forcée à la valeur qui rend le littéral vrai.
3. **Analyse de conflit et Apprentissage :** Si une contradiction (conflit) émerge (une clause devenant entièrement fausse), le solveur n'effectue pas un simple retour en arrière classique (*backtracking*). Il analyse le graphe des implications qui a mené au conflit, extrait une clause dite de conflit (la cause minimale de l'erreur) et l'ajoute à sa base de connaissances pour ne plus jamais reproduire la même suite d'erreurs.
4. **Retour arrière non-chronologique (*backjumping*) :** Le solveur remonte directement au niveau de décision qui a provoqué le conflit.

Ces moteurs sont utilisés en IA pour :
- **La vérification formelle de modèles :** S'assurer que le code d'un pilote automatique ou d'un système critique (médical, aérospatial) ne peut jamais se retrouver dans un état instable ou interdit (modélisé par une contradiction logique).
- **La planification automatisée :** Trouver une séquence d'actions permettant à un robot d'atteindre un but sous des contraintes logiques strictes (l'approche SATPlan).
- **La vérification formelle des Réseaux de Neurones :** Des outils récents encodent le comportement local de neurones avec des fonctions d'activation linéaires par morceaux (ReLU) sous forme de contraintes logiques pour prouver qu'un réseau profond ne subira pas de failles de type "exemples contradictoires" ou "exemples antagonistes" (*adversarial examples*).

---

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** Aucun (Jalon initial)
- **Concepts Futurs dépendants :** [[Jalon 2 (Méthodes de raisonnement)]], [[Jalon 3 (Quantification)]], [[Jalon 12 (Livrable IA)]], [[Jalon 133 (Modele PAC)]]
