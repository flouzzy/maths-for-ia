# Exercice 03 : Indépendance deux à deux n'est pas indépendance mutuelle
Difficulté : $\bigstar\bigstar\star\star\star$

**Énoncé :**
On lance deux pièces de monnaie équilibrées de manière indépendante. $\Omega = \{PP, PF, FP, FF\}$.
Soit $A$ : « la première pièce fait Pile ».
Soit $B$ : « la deuxième pièce fait Pile ».
Soit $C$ : « les deux pièces donnent le même résultat ».
Montrer que $A, B, C$ sont indépendants deux à deux, mais pas mutuellement indépendants.

**Correction :**
1. **Évaluation des probabilités simples :**
$A = \{PP, PF\}$, $\mathbb{P}(A) = \frac{2}{4} = \frac{1}{2}$.
$B = \{PP, FP\}$, $\mathbb{P}(B) = \frac{2}{4} = \frac{1}{2}$.
$C = \{PP, FF\}$, $\mathbb{P}(C) = \frac{2}{4} = \frac{1}{2}$.

2. **Indépendance deux à deux :**
- $A \cap B = \{PP\}$, $\mathbb{P}(A \cap B) = \frac{1}{4}$. Et $\mathbb{P}(A)\mathbb{P}(B) = \frac{1}{4}$. ($A$ et $B$ indépendants).
- $A \cap C = \{PP\}$, $\mathbb{P}(A \cap C) = \frac{1}{4}$. Et $\mathbb{P}(A)\mathbb{P}(C) = \frac{1}{4}$. ($A$ et $C$ indépendants).
- $B \cap C = \{PP\}$, $\mathbb{P}(B \cap C) = \frac{1}{4}$. Et $\mathbb{P}(B)\mathbb{P}(C) = \frac{1}{4}$. ($B$ et $C$ indépendants).
La famille est bien indépendante deux à deux.

3. **Indépendance mutuelle :**
$A \cap B \cap C = \{PP\}$, $\mathbb{P}(A \cap B \cap C) = \frac{1}{4}$.
Cependant, $\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}$.
Comme $\frac{1}{4} \neq \frac{1}{8}$, les trois événements ne sont pas mutuellement indépendants. Connaître $A$ et $B$ détermine entièrement $C$.
