---
title: "Exercice 9"
---
## Exercice 9 : Série d'intégrales de Lebesgue $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(q_n)_{n \ge 1}$ une énumération des rationnels de $]0,1[$.
On définit $f(x) = \sum_{n=1}^\infty \frac{1}{2^n \sqrt{|x-q_n|}}$.
Montrer que $f$ est intégrable sur $[0,1]$ (et donc $f(x) < \infty$ p.p.).

**Correction Détaillée :**
1. Posons $u_n(x) = \frac{1}{2^n \sqrt{|x-q_n|}} \mathbf{1}_{[0,1]}(x)$.
2. Chaque $u_n$ est mesurable et positive.
3. Par le corollaire du TCM (sommation terme à terme de fonctions positives) :
   $$\int_{[0,1]} f(x) dx = \sum_{n=1}^\infty \int_0^1 \frac{1}{2^n \sqrt{|x-q_n|}} dx$$
4. Calculons l'intégrale $\int_0^1 \frac{1}{\sqrt{|x-q|}} dx$ pour $q \in ]0,1[$.
   $$ \int_0^1 \frac{dx}{\sqrt{|x-q|}} = \int_0^q \frac{dx}{\sqrt{q-x}} + \int_q^1 \frac{dx}{\sqrt{x-q}} $$
   $$ = [-2\sqrt{q-x}]_0^q + [2\sqrt{x-q}]_q^1 = 2\sqrt{q} + 2\sqrt{1-q} $$
5. Comme $q \in ]0,1[$, on a $\sqrt{q} \le 1$ et $\sqrt{1-q} \le 1$. Donc l'intégrale est $\le 4$.
6. On obtient : $\int_{[0,1]} f(x) dx \le \sum_{n=1}^\infty \frac{4}{2^n} = 4 \sum_{n=1}^\infty \frac{1}{2^n} = 4 \times 1 = 4$.
7. Comme l'intégrale de $f$ est finie, $f$ est finie presque partout sur $[0,1]$.
