# Exercice 8 : Suite de variables aléatoires de Bernoulli

$\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X_n)$ une suite de variables aléatoires indépendantes suivant la loi de Bernoulli de paramètre $p_n$.
Montrer que $X_n \xrightarrow{p.s.} 0$ si et seulement si $\sum_{n=1}^\infty p_n < +\infty$.

**Correction :**
Rappelons que $X_n \in \{0, 1\}$.
La convergence vers 0 de la suite $X_n$ signifie que pour tout $\epsilon > 0$, il n'y a qu'un nombre fini de $X_n$ tels que $|X_n| \ge \epsilon$.
En choisissant $\epsilon = 1/2$, la condition $|X_n| \ge 1/2$ est équivalente à $X_n = 1$.
Donc $X_n \xrightarrow{p.s.} 0$ si et seulement si l'événement $\{X_n = 1\}$ ne se produit qu'un nombre fini de fois presque sûrement, c'est-à-dire $\mathbb{P}(\limsup \{X_n = 1\}) = 0$.
Soit $A_n = \{X_n = 1\}$. On a $\mathbb{P}(A_n) = p_n$.
- Sens direct ($\impliedby$) : Si $\sum p_n < +\infty$, le premier lemme de Borel-Cantelli s'applique immédiatement et assure que $\mathbb{P}(\limsup A_n) = 0$. Donc $X_n \xrightarrow{p.s.} 0$.
- Sens réciproque ($\implies$) : Supposons que $\sum p_n = +\infty$. Comme les $X_n$ sont indépendantes, les événements $A_n$ le sont aussi. Le second lemme de Borel-Cantelli affirme que $\mathbb{P}(\limsup A_n) = 1$. Ainsi, $X_n = 1$ une infinité de fois avec probabilité 1. La suite $(X_n)$ ne peut donc pas converger vers 0. Par contraposée, si $X_n \xrightarrow{p.s.} 0$, alors on a nécessairement $\sum p_n < +\infty$.
L'équivalence est ainsi rigoureusement démontrée.
