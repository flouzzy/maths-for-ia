# Exercice 2 : Convergence presque sûre vers une constante \quad $\bigstar\bigstar\star\star\star$

## Énoncé
Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires i.i.d. de loi uniforme sur $[0, a]$ avec $a>0$. Soit $M_n = \max(X_1, \dots, X_n)$.
Montrer que $M_n$ converge presque sûrement vers $a$ lorsque $n \to \infty$.

## Correction Détaillée
### Étape 1 : Propriété de monotonie
On remarque que $M_n$ est une suite croissante de variables aléatoires, puisque $M_{n+1} = \max(M_n, X_{n+1}) \ge M_n$. De plus, $M_n \le a$ pour tout $n$. Ainsi, pour tout $\omega \in \Omega$, la suite réelle $(M_n(\omega))$ est croissante et majorée. Elle converge donc vers une limite $M(\omega) \le a$.

### Étape 2 : Évaluation des probabilités d'écart
Soit $\epsilon > 0$ tel que $\epsilon < a$. Calculons la probabilité que $M_n$ s'écarte de $a$ par plus de $\epsilon$.
$$ \mathbb{P}(M_n \le a - \epsilon) = \mathbb{P}(X_1 \le a - \epsilon, \dots, X_n \le a - \epsilon) $$
Par indépendance des $X_i$, cette probabilité est le produit des probabilités :
$$ \mathbb{P}(M_n \le a - \epsilon) = (\mathbb{P}(X_1 \le a - \epsilon))^n = \left( \frac{a - \epsilon}{a} \right)^n $$

### Étape 3 : Application de Borel-Cantelli
Soit l'événement $A_n = \{ M_n \le a - \epsilon \}$.
La série $\sum_{n=1}^\infty \mathbb{P}(A_n) = \sum_{n=1}^\infty \left( 1 - \frac{\epsilon}{a} \right)^n$ est une série géométrique de raison $q = 1 - \frac{\epsilon}{a} \in ]0, 1[$.
Donc, $\sum_{n=1}^\infty \mathbb{P}(A_n) < +\infty$.
Par le lemme de Borel-Cantelli, $\mathbb{P}(\limsup A_n) = 0$. Cela signifie que presque sûrement, à partir d'un certain rang, $M_n > a - \epsilon$.
Puisque cela est vrai pour tout $\epsilon > 0$ (en considérant une suite $\epsilon_k = 1/k \to 0$), on conclut que $M_n \xrightarrow{p.s.} a$. $\blacksquare$
