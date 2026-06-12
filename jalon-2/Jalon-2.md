---
uuid: "jalon-2"
title: "Méthodes de raisonnement (implication, contraposée, l'absurde, analyse-synthèse)"
year: 1
trimester: 1
tags:
  - math/fondations
  - ia/logique-algorithmique
prev: "[[Jalon 1 (Logique formelle).md]]"
next: "[[Jalon-3.md]]"
---
# Jalon 2 : Méthodes de raisonnement (implication, contraposée, l'absurde, analyse-synthèse)

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Pensez à un avocat dans un tribunal. Pour prouver que son client est innocent, il peut utiliser plusieurs tactiques. L'**implication** est un chemin direct : "S'il était au cinéma, il ne pouvait pas être sur les lieux du crime". L'**absurde**, c'est montrer que l'hypothèse inverse est ridicule : "Supposons qu'il soit coupable... mais alors il aurait dû être à deux endroits en même temps, ce qui est impossible ! Donc il est innocent". La **contraposée**, c'est retourner la veste : au lieu de dire "S'il pleut, le sol est mouillé", on dit "Si le sol est sec, c'est qu'il ne pleut pas".
- **Le "Pourquoi on a inventé ça" :** Les mathématiques ne sont pas juste des calculs, c'est l'art de la certitude. Sans méthodes de raisonnement claires, on pourrait croire des choses fausses. Ces outils sont les "plans de construction" qui garantissent que l'édifice mathématique ne s'écroulera jamais.
- **Visualisation :** Imaginez un labyrinthe. L'**analyse-synthèse** consiste d'abord à partir de la sortie pour voir par où on a pu passer (analyse), puis à vérifier qu'en partant de l'entrée on arrive bien à la sortie en suivant ce chemin (synthèse).

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soient $P$ et $Q$ deux propositions.
1. **L'Implication ($P \Rightarrow Q$) :** Proposition qui n'est fausse que lorsque $P$ est vraie et $Q$ est fausse.
2. **La Contraposée :** La proposition $(\neg Q \Rightarrow \neg P)$ est logiquement équivalente à $(P \Rightarrow Q)$.
3. **La Réciproque :** La proposition $(Q \Rightarrow P)$. Attention, elle n'est pas équivalente à l'implication initiale.
4. **Le Raisonnement par l'Absurde :** Pour démontrer $P$, on suppose $\neg P$ et on cherche à obtenir une contradiction ($R \land \neg R$).
5. **Analyse-Synthèse :** Méthode de résolution d'équation ou de recherche d'objet. L'analyse détermine les conditions nécessaires (candidats possibles), la synthèse vérifie lesquelles de ces conditions sont suffisantes.

### B. Théorèmes, Propositions & Lemmes
> **Principe du Tiers Exclu :**
> Pour toute proposition $P$, soit $P$ est vraie, soit $\neg P$ est vraie. Il n'y a pas de troisième possibilité.
> $$\vDash P \lor \neg P$$

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Irrationalité de $\sqrt{2}$ (Raisonnement par l'absurde)
Nous voulons démontrer que $\sqrt{2} \notin \mathbb{Q}$.

1. **Initialisation / Cadre :** Raisonnons par l'absurde. Supposons que $\sqrt{2} \in \mathbb{Q}$.
   Alors il existe deux entiers naturels $p$ et $q$ (avec $q \neq 0$) tels que $\sqrt{2} = \frac{p}{q}$.
   Supposons de plus que la fraction $\frac{p}{q}$ est irréductible (ce qui est toujours possible en simplifiant au maximum).

2. **Étape 1 : Élévation au carré et manipulation**
   $\sqrt{2} = \frac{p}{q} \implies 2 = \frac{p^2}{q^2}$
   $\implies p^2 = 2q^2$
   On en déduit que $p^2$ est pair. Or, le carré d'un nombre impair est impair, donc $p$ est nécessairement pair.
   Il existe donc un entier $k$ tel que $p = 2k$.

3. **Étape 2 : Substitution et nouvelle déduction**
   Remplaçons $p$ par $2k$ dans l'égalité $p^2 = 2q^2$ :
   $(2k)^2 = 2q^2 \implies 4k^2 = 2q^2$
   $\implies 2k^2 = q^2$
   On en déduit que $q^2$ est pair, et donc $q$ est pair.

4. **Étape 3 : Mise en évidence de la contradiction**
   Nous avons montré que $p$ est pair et $q$ est pair.
   Cela signifie que la fraction $\frac{p}{q}$ est simplifiable par $2$.
   Or, nous avions supposé au départ que $\frac{p}{q}$ était irréductible.
   Nous obtenons une contradiction : (Fraction irréductible) $\land$ (Fraction réductible par 2).

5. **Conclusion :** L'hypothèse de départ ($\sqrt{2} \in \mathbb{Q}$) est donc fausse. Par conséquent, $\sqrt{2}$ est irrationnel.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Contraposée)
**Énoncé :** Soit $n \in \mathbb{N}$. Démontrer que si $n^2$ est impair, alors $n$ est impair.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Utilisons le raisonnement par contraposée. La proposition est $(n^2 \text{ impair} \Rightarrow n \text{ impair})$. Sa contraposée est $(n \text{ pair} \Rightarrow n^2 \text{ pair})$.
* *Résolution pas-à-pas :*
   1. Supposons que $n$ est pair.
   2. Alors il existe $k \in \mathbb{N}$ tel que $n = 2k$.
   3. Calculons $n^2$ : $n^2 = (2k)^2 = 4k^2$.
   4. On peut écrire $n^2 = 2(2k^2)$.
   5. Posons $K = 2k^2$. Comme $k \in \mathbb{N}$, alors $K \in \mathbb{N}$.
   6. On a $n^2 = 2K$, donc $n^2$ est pair.
   7. La contraposée est démontrée. Par équivalence, la proposition initiale est vraie.

### Exercice 2 : Niveau Avancé (Analyse-Synthèse)
**Énoncé :** Déterminer toutes les fonctions $f : \mathbb{R} \to \mathbb{R}$ telles que pour tous $x, y \in \mathbb{R}$, $f(x+y) = f(x) + f(y)$ et $f$ est continue. (Équation fonctionnelle de Cauchy).
**Correction Détaillée :**
* *Analyse de l'énoncé :* Nous cherchons un ensemble de fonctions. Nous allons restreindre les candidats.
* *Résolution pas-à-pas (ANALYSE) :*
   1. Si $f$ existe, alors $f(0+0) = f(0)+f(0) \implies f(0) = 0$.
   2. Par récurrence immédiate (que nous détaillons) : $f(n \cdot x) = n \cdot f(x)$ pour $n \in \mathbb{N}$.
      - Pour $n=1$, $f(x)=f(x)$ (vrai).
      - Supposons $f(kx) = kf(x)$. Alors $f((k+1)x) = f(kx+x) = f(kx)+f(x) = kf(x)+f(x) = (k+1)f(x)$.
   3. Pour $x=1$, on a $f(n) = n \cdot f(1)$. Posons $a = f(1)$. Alors $f(n) = an$.
   4. On montre de même pour $q \in \mathbb{Q}$ que $f(q) = aq$.
      - $f(1) = f(q \cdot \frac{1}{q}) = q \cdot f(\frac{1}{q}) \implies f(\frac{1}{q}) = \frac{1}{q} a$.
      - $f(\frac{p}{q}) = p \cdot f(\frac{1}{q}) = \frac{p}{q} a$.
   5. Par continuité, comme $\mathbb{Q}$ est dense dans $\mathbb{R}$, pour tout $x \in \mathbb{R}$, il existe une suite de rationnels $q_n \to x$.
   6. $f(x) = f(\lim q_n) = \lim f(q_n) = \lim (aq_n) = a \lim q_n = ax$.
   7. Les candidats sont les fonctions linéaires $f(x) = ax$.
* *Résolution pas-à-pas (SYNTHÈSE) :*
   1. Soit $f(x) = ax$ avec $a \in \mathbb{R}$.
   2. $f(x+y) = a(x+y) = ax + ay = f(x) + f(y)$. La condition est vérifiée.
   3. $f$ est une fonction polynomiale de degré 1, elle est donc continue.
* *Conclusion :* Les solutions sont exactement les fonctions de la forme $f(x) = ax$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Le raisonnement par l'absurde et la contraposée sont au cœur des algorithmes de **vérification formelle** (Formal Verification) qui garantissent qu'une IA critique (voiture autonome, diagnostic médical) ne prendra jamais de décision catastrophique.
- **Exemple Concret :** Dans l'**apprentissage par renforcement**, pour prouver qu'un agent finira par atteindre son objectif, on utilise souvent des raisonnements par l'absurde : "Supposons que l'agent reste bloqué indéfiniment... alors une certaine énergie (fonction de Lyapunov) devrait décroître à l'infini, ce qui est impossible car elle est bornée. Donc il ne peut pas rester bloqué."

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 1 (Logique formelle)]]
- **Concepts Futurs dépendants :** [[Jalon 3 (Quantification)]], [[Jalon 4 (Théorie des ensembles)]]
