# Exercice 2

**Difficulté :** $\bigstar\star\star\star\star$

## Indépendance et divergence

Soit $(E_n)_{n \in \mathbb{N}}$ une suite d'événements mutuellement indépendants dans un espace de probabilité. On suppose que $\mathbb{P}(E_n) = \frac{1}{n+1}$ pour $n \ge 0$.
Quelle est la probabilité que les événements $E_n$ se réalisent infiniment souvent ?

**Correction détaillée :**
1. La probabilité de l'événement $E_n$ est $\mathbb{P}(E_n) = \frac{1}{n+1}$.
2. On étudie la nature de la série $\sum_{n=0}^{\infty} \mathbb{P}(E_n) = \sum_{n=0}^{\infty} \frac{1}{n+1} = \sum_{k=1}^{\infty} \frac{1}{k}$.
3. Il s'agit de la série harmonique. Or, on sait que la série harmonique diverge vers $+\infty$.
4. De plus, l'énoncé stipule que les événements $E_n$ sont mutuellement indépendants.
5. Ces deux conditions (divergence de la série des probabilités et indépendance mutuelle) sont exactement les hypothèses du second lemme de Borel-Cantelli.
6. En appliquant ce lemme, on déduit directement que $\mathbb{P}(\limsup_{n \to \infty} E_n) = 1$.
7. Donc, presque sûrement, une infinité de $E_n$ se réalisent.
