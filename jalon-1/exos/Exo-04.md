# Exercice 4 : Preuve en déduction naturelle de la loi de Peirce

## Énoncé
La **déduction naturelle** est un système formel syntaxique introduit par Gerhard Gentzen. Dans sa version classique, il dispose notamment des règles suivantes (où $\Gamma$ est un ensemble de formules servant d'hypothèses) :
- **Règle d'Implication-Introduction ($\Rightarrow$-I) :** Si $\Gamma, A \vdash B$, alors $\Gamma \vdash A \Rightarrow B$.
- **Règle d'Implication-Élimination ou Modus Ponens ($\Rightarrow$-E) :** Si $\Gamma \vdash A \Rightarrow B$ et $\Gamma \vdash A$, alors $\Gamma \vdash B$.
- **Règle de l'Absurde Classique ou Élimination de la Double Négation ($\neg\neg$-E) :** Si $\Gamma, \neg A \vdash \bot$ (où $\bot$ représente une contradiction), alors $\Gamma \vdash A$.
- **Règle de Négation-Introduction ($\neg$-I) :** Si $\Gamma, A \vdash \bot$, alors $\Gamma \vdash \neg A$.
- **Règle de Négation-Élimination ($\neg$-E) :** Si $\Gamma \vdash \neg A$ et $\Gamma \vdash A$, alors $\Gamma \vdash \bot$.

Démontrer la **loi de Peirce** $\vdash ((A \Rightarrow B) \Rightarrow A) \Rightarrow A$ dans ce système formel en détaillant chaque étape de déduction.

---

## Correction Détaillée

Pour démontrer la formule $((A \Rightarrow B) \Rightarrow A) \Rightarrow A$, nous allons chercher à appliquer la règle d'introduction de l'implication ($\Rightarrow$-I) à l'étape finale.
Il nous suffit donc de prouver le séquent suivant sous hypothèse :
$$(A \Rightarrow B) \Rightarrow A \vdash A$$

Pour démontrer $A$ sous cette hypothèse, nous allons procéder par l'absurde classique. Nous rajoutons donc l'hypothèse $\neg A$ et cherchons à déduire la contradiction $\bot$. Notre but intermédiaire est de prouver :
$$(A \Rightarrow B) \Rightarrow A, \quad \neg A \vdash \bot$$

Voici la construction pas-à-pas de la démonstration :

### Étape 1 : Hypothèses de départ
Nous disposons dans notre contexte de deux hypothèses :
- $(1)$ : $(A \Rightarrow B) \Rightarrow A$
- $(2)$ : $\neg A$

### Étape 2 : Construction de la sous-preuve de $A \Rightarrow B$
Pour exploiter l'hypothèse $(1)$ par élimination de l'implication, il serait utile de disposer de la formule $A \Rightarrow B$. Montrons que sous les hypothèses $(1)$ et $(2)$, nous pouvons déduire $A \Rightarrow B$.
Pour cela, introduisons une hypothèse temporaire supplémentaire pour construire l'implication :
- $(3)$ : $A$ (hypothèse pour l'introduction de $\Rightarrow$)

Maintenant, nous avons dans le contexte local les formules $A$ (hypothèse 3) et $\neg A$ (hypothèse 2).
1. Appliquons la règle de négation-élimination ($\neg$-E) sur $A$ et $\neg A$ :
   $$\text{De } \Gamma, A \vdash A \text{ et } \Gamma, A \vdash \neg A \implies \Gamma, A \vdash \bot$$
   Nous obtenons une contradiction $\bot$.
2. Sous la contradiction $\bot$, nous pouvons déduire n'importe quelle proposition (règle du *Principe d'explosion* ou *ex falso sequitur quodlibet*). Appliquons cette règle pour déduire $B$ :
   $$\text{Puisque } (A \Rightarrow B) \Rightarrow A, \neg A, A \vdash \bot \implies (A \Rightarrow B) \Rightarrow A, \neg A, A \vdash B$$
3. Déchargeons maintenant l'hypothèse temporaire $A$ (3) par la règle d'introduction de l'implication ($\Rightarrow$-I) :
   $$\text{Puisque } (A \Rightarrow B) \Rightarrow A, \neg A, A \vdash B \implies (A \Rightarrow B) \Rightarrow A, \neg A \vdash A \Rightarrow B$$
Nous avons réussi à démontrer la formule $A \Rightarrow B$ sous les hypothèses de base.

### Étape 3 : Application du Modus Ponens et Obtention de la Contradiction
Reprenons notre contexte global avec les hypothèses $(1)$ $(A \Rightarrow B) \Rightarrow A$ et $(2)$ $\neg A$.
1. Nous venons de prouver que ce contexte permet de déduire $A \Rightarrow B$.
2. Appliquons la règle d'élimination de l'implication ($\Rightarrow$-E, ou Modus Ponens) entre l'hypothèse $(1)$ et la formule $A \Rightarrow B$ :
   $$\text{De } \Gamma \vdash (A \Rightarrow B) \Rightarrow A \quad \text{et} \quad \Gamma \vdash A \Rightarrow B \implies \Gamma \vdash A$$
   Nous avons donc déduit $A$.
3. Nous disposons désormais à la fois de $A$ et de l'hypothèse de base $\neg A$ (2). Appliquons la règle de négation-élimination ($\neg$-E) :
   $$\text{De } \Gamma \vdash A \quad \text{et} \quad \Gamma \vdash \neg A \implies \Gamma \vdash \bot$$
   Nous obtenons la contradiction souhaitée.

### Étape 4 : Déchargement des hypothèses
1. Appliquons la règle de l'absurde classique ($\neg\neg$-E) pour décharger l'hypothèse $\neg A$ (2) :
   $$\text{Puisque } (A \Rightarrow B) \Rightarrow A, \neg A \vdash \bot \implies (A \Rightarrow B) \Rightarrow A \vdash A$$
2. Appliquons enfin la règle d'introduction de l'implication ($\Rightarrow$-I) pour décharger la dernière hypothèse $(A \Rightarrow B) \Rightarrow A$ (1) :
   $$\text{Puisque } (A \Rightarrow B) \Rightarrow A \vdash A \implies \vdash ((A \Rightarrow B) \Rightarrow A) \Rightarrow A$$

La loi de Peirce est démontrée de manière purement syntaxique dans le système classique de déduction naturelle.

---

### Représentation sous forme d'Arbre de Preuve
Voici l'arbre syntaxique complet résumant la démonstration :

$$\frac{
  \frac{
    \displaystyle [(A \Rightarrow B) \Rightarrow A]^1 \qquad
    \frac{
      \frac{\displaystyle [\neg A]^2 \quad [A]^3}{\bot}\small\text{($\neg$-E)}
      }{
        \displaystyle B
      }\small\text{($\bot$-E)}
    }{
      \displaystyle A \Rightarrow B
    }\small\text{($\Rightarrow$-I décharge 3)}
  }{
    \displaystyle A
  }\small\text{($\Rightarrow$-E)} \qquad [\neg A]^2
}{
  \frac{
    \displaystyle \bot
  }{
    \displaystyle A
  }\small\text{($\neg\neg$-E décharge 2)}
}\small\text{($\neg$-E)}$$
$$\overline{\displaystyle ((A \Rightarrow B) \Rightarrow A) \Rightarrow A}\small\text{($\Rightarrow$-I décharge 1)}$$
