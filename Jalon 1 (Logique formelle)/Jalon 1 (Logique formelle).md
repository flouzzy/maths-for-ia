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
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous êtes un détective face à un tableau de bord composé de leviers qui peuvent être soit "Haut" (Vrai), soit "Bas" (Faux). La logique formelle, c'est le manuel d'instruction qui vous dit exactement quel voyant s'allume en fonction de la position des leviers. Si je vous dis : "Le voyant s'allume SI le levier A est haut ET le levier B est bas", vous venez de pratiquer la logique. C'est le code source universel de la pensée : avant même de savoir *ce que* l'on dit, on définit *comment* les briques de vérité s'emboîtent.
- **Le "Pourquoi on a inventé ça" :** Les mathématiciens voulaient éliminer le flou du langage humain. Les mots comme "ou" peuvent être ambigus (est-ce "fromage ou dessert" ou bien "l'un, l'autre, ou les deux" ?). En créant une langue artificielle pure, ils ont pu construire des raisonnements infaillibles que même une machine peut exécuter sans jamais se tromper.
- **Visualisation :** On peut imaginer des circuits électriques. Un connecteur "ET" est comme deux interrupteurs placés l'un après l'autre : le courant ne passe que si les deux sont fermés. Un connecteur "OU" est comme deux interrupteurs en parallèle : il suffit qu'un seul soit fermé pour que la lumière brille.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $\mathcal{P}$ un ensemble de symboles appelés **variables propositionnelles**. On définit l'ensemble $\mathcal{F}$ des **formules du calcul des propositions** par induction :
1. Toute variable $p \in \mathcal{P}$ est une formule.
2. Si $A$ est une formule, alors $(\neg A)$ (négation) est une formule.
3. Si $A$ et $B$ sont des formules, alors $(A \land B)$ (conjonction), $(A \lor B)$ (disjonction), $(A \Rightarrow B)$ (implication) et $(A \Leftrightarrow B)$ (équivalence) sont des formules.

On appelle **interprétation** (ou distribution de valeurs de vérité) une application $v : \mathcal{P} \to \{0, 1\}$, où $0$ représente le Faux et $1$ le Vrai. Cette application s'étend de manière unique à $\mathcal{F}$ selon les règles de calcul (tables de vérité).

### B. Théorèmes, Propositions & Lemmes
> **Théorème de la Complétude (Simplifié) :**
> Une formule $A$ est une **tautologie** (notée $\vDash A$) si et seulement si elle est démontrable dans le système formel du calcul des propositions (notée $\vdash A$).
> $$v(A) = 1 \text{ pour toute interprétation } v \iff \vdash A$$

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Loi de De Morgan $\neg(A \land B) \iff (\neg A \lor \neg B)$
Nous allons démontrer cette équivalence par la méthode des tables de vérité, en examinant toutes les interprétations possibles des variables $A$ et $B$.

1. **Initialisation / Cadre :** Soient $A$ et $B$ deux variables propositionnelles. Le nombre d'interprétations possibles est $2^2 = 4$. Nous allons construire le tableau de vérité colonne par colonne.

2. **Étape 1 : Construction des briques de base**
   Calculons $A \land B$ :
   - Si $v(A)=1, v(B)=1 \implies v(A \land B)=1$
   - Si $v(A)=1, v(B)=0 \implies v(A \land B)=0$
   - Si $v(A)=0, v(B)=1 \implies v(A \land B)=0$
   - Si $v(A)=0, v(B)=0 \implies v(A \land B)=0$

3. **Étape 2 : Calcul de la partie gauche $\neg(A \land B)$**
   Inversons les valeurs de la colonne précédente :
   - Interp 1 : $\neg(1) = 0$
   - Interp 2 : $\neg(0) = 1$
   - Interp 3 : $\neg(0) = 1$
   - Interp 4 : $\neg(0) = 1$
   Valeurs de $\neg(A \land B)$ : $\{0, 1, 1, 1\}$

4. **Étape 3 : Calcul de la partie droite $(\neg A \lor \neg B)$**
   Calculons d'abord $\neg A$ et $\neg B$, puis leur disjonction :
   - Interp 1 : $\neg 1 = 0, \neg 1 = 0 \implies 0 \lor 0 = 0$
   - Interp 2 : $\neg 1 = 0, \neg 0 = 1 \implies 0 \lor 1 = 1$
   - Interp 3 : $\neg 0 = 1, \neg 1 = 0 \implies 1 \lor 0 = 1$
   - Interp 4 : $\neg 0 = 1, \neg 0 = 1 \implies 1 \lor 1 = 1$
   Valeurs de $(\neg A \lor \neg B)$ : $\{0, 1, 1, 1\}$

5. **Conclusion :** Les colonnes des étapes 3 et 4 sont identiques pour toutes les interprétations. L'équivalence $\neg(A \land B) \Leftrightarrow (\neg A \lor \neg B)$ est donc une tautologie. Elle est rigoureusement démontrée.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe
**Énoncé :** Démontrer que l'implication $(A \Rightarrow B)$ est équivalente à $(\neg A \lor B)$.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Nous devons comparer les valeurs de vérité de l'opérateur "Implication" avec la formule combinée utilisant "Négation" et "Disjonction".
* *Résolution pas-à-pas :*
   1. Table de $A \Rightarrow B$ : $\{1, 0, 1, 1\}$ (définition standard : faux seulement si le vrai implique le faux).
   2. Calcul de $\neg A$ :
      - $v(A)=1 \implies v(\neg A)=0$
      - $v(A)=0 \implies v(\neg A)=1$
   3. Calcul de $\neg A \lor B$ :
      - Interp 1 ($A=1, B=1$) : $0 \lor 1 = 1$
      - Interp 2 ($A=1, B=0$) : $0 \lor 0 = 0$
      - Interp 3 ($A=0, B=1$) : $1 \lor 1 = 1$
      - Interp 4 ($A=0, B=0$) : $1 \lor 0 = 1$
   4. Conclusion : Les résultats $\{1, 0, 1, 1\}$ coïncident parfaitement. L'équivalence est établie.

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT)
**Énoncé :** Soit la formule $F = ((A \Rightarrow B) \land (B \Rightarrow C)) \Rightarrow (A \Rightarrow C)$. Montrer que $F$ est une tautologie sans utiliser de table de vérité, en utilisant uniquement les propriétés algébriques de la logique.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Il s'agit de la loi du syllogisme hypothétique (transitivité de l'implication).
* *Résolution pas-à-pas :*
   1. Traduisons les implications internes : $F = ((\neg A \lor B) \land (\neg B \lor C)) \Rightarrow (\neg A \lor C)$.
   2. Traduisons l'implication principale : $F = \neg [(\neg A \lor B) \land (\neg B \lor C)] \lor (\neg A \lor C)$.
   3. Appliquons De Morgan sur le crochet : $F = [\neg(\neg A \lor B) \lor \neg(\neg B \lor C)] \lor (\neg A \lor C)$.
   4. Appliquons à nouveau De Morgan à l'intérieur : $F = [(A \land \neg B) \lor (B \land \neg C)] \lor (\neg A \lor C)$.
   5. Par associativité et commutativité de $\lor$ : $F = (A \land \neg B) \lor \neg A \lor (B \land \neg C) \lor C$.
   6. Distribuons $\neg A$ sur $(A \land \neg B)$ : $(\neg A \lor A) \land (\neg A \lor \neg B)$. Or $(\neg A \lor A) = 1$, donc il reste $(\neg A \lor \neg B)$.
   7. Distribuons $C$ sur $(B \land \neg C)$ : $(C \lor B) \land (C \lor \neg C)$. Or $(C \lor \neg C) = 1$, donc il reste $(C \lor B)$.
   8. Réassemblons : $F = (\neg A \lor \neg B) \lor (C \lor B)$.
   9. Par associativité : $F = \neg A \lor (\neg B \lor B) \lor C$.
   10. Or $(\neg B \lor B) = 1$, donc $F = \neg A \lor 1 \lor C$.
   11. Par propriété de l'élément absorbant du Vrai ($1 \lor X = 1$) : $F = 1$.
   12. La formule est identiquement égale à Vrai, c'est donc une tautologie.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Le calcul des propositions est l'ancêtre direct des circuits logiques (portes logiques) et des moteurs d'inférence en IA symbolique.
- **Exemple Concret :** Dans les **systèmes experts** ou les **solveurs SAT** (utilisés pour vérifier la sécurité de codes logiciels complexes ou optimiser la planification logistique), l'algorithme doit décider si une énorme conjonction de contraintes logiques est "satisfaisable". C'est précisément l'application massive des tables de vérité et de l'algèbre de Boole pour résoudre des problèmes où le nombre de combinaisons dépasse l'entendement humain.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** Aucun (Jalon initial)
- **Concepts Futurs dépendants :** [[Jalon 2 (Méthodes de raisonnement)]], [[Jalon 3 (Quantification)]]
