# Exercice 7 : Limite d'une somme de variables bornées par Borel-Cantelli

$\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires indépendantes telles que pour tout $n$, $\mathbb{P}(X_n = 1) = p$ et $\mathbb{P}(X_n = -1) = 1-p$, avec $p \in ]0, 1[$.
Soit $S_n = \sum_{i=1}^n X_i$.

Montrer en utilisant la LFGN que si $p > 1/2$, alors $S_n \xrightarrow{p.s.} +\infty$.

**Correction détaillée :**

1. Les variables $X_n$ sont I.I.D.
   Calculons leur espérance :
   $$ \mathbb{E}[X_1] = 1 \cdot p + (-1) \cdot (1-p) = p - 1 + p = 2p - 1 $$
2. Puisque $X_n \in \{-1, 1\}$, $\mathbb{E}[|X_1|] = 1 < +\infty$.
   La loi forte des grands nombres s'applique à la suite $(X_n)$, donc :
   $$ \frac{S_n}{n} = \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{p.s.} \mathbb{E}[X_1] = 2p - 1 $$
3. Par hypothèse, $p > 1/2$, ce qui implique que $2p - 1 > 0$. Notons $\mu = 2p - 1 > 0$.
   La convergence presque sûre $\frac{S_n}{n} \xrightarrow{p.s.} \mu$ signifie que, pour presque tout $\omega \in \Omega$, il existe un rang $N(\omega)$ tel que pour tout $n \geq N(\omega)$, $\frac{S_n(\omega)}{n} \geq \frac{\mu}{2}$.
   Par conséquent, pour $n \geq N(\omega)$ :
   $$ S_n(\omega) \geq n \frac{\mu}{2} $$
   Puisque $\mu/2 > 0$, la limite du terme de droite est $+\infty$ lorsque $n \to +\infty$.
   Par minoration, on en déduit que pour presque tout $\omega$, $\lim_{n \to +\infty} S_n(\omega) = +\infty$.
   Ce qui démontre que $S_n \xrightarrow{p.s.} +\infty$.
   (Interprétation : dans une marche aléatoire où la probabilité d'aller à droite est strictement supérieure à celle d'aller à gauche, la particule part inéluctablement vers $+\infty$).
