# Exercice 5 : Variables symétriques et loi forte \quad $\bigstar\bigstar\bigstar\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables I.I.D. de loi symétrique par rapport à 0, et possédant un moment d'ordre 1. Soit $\bar{X}_n$ leur moyenne empirique.
1. Que vaut l'espérance $\mathbb{E}[X_1]$ ?
2. Déterminer la limite presque sûre de $\bar{X}_n$.
3. On pose $Z_n = \cos(\bar{X}_n) + \sin(\bar{X}_n)$. Vers quoi converge $Z_n$ presque sûrement ?

**Correction :**
1. La variable $X_1$ admet une espérance par hypothèse, et sa loi est symétrique par rapport à 0 (c'est-à-dire que $X_1$ et $-X_1$ ont même loi). Donc $\mathbb{E}[X_1] = \mathbb{E}[-X_1] = -\mathbb{E}[X_1]$, ce qui implique $2\mathbb{E}[X_1] = 0$, soit $\mathbb{E}[X_1] = 0$.
2. La suite $(X_n)$ est I.I.D. et admet une espérance finie $\mu = 0$. Par le théorème de Kolmogorov (loi forte des grands nombres), la moyenne empirique $\bar{X}_n$ converge presque sûrement vers l'espérance. Donc $\bar{X}_n \xrightarrow{p.s.} 0$.
3. La fonction $h(x) = \cos(x) + \sin(x)$ est continue sur $\mathbb{R}$. Par composition avec une limite presque sûre, puisque $\bar{X}_n \xrightarrow{p.s.} 0$, on en déduit que $h(\bar{X}_n) \xrightarrow{p.s.} h(0)$. Or $h(0) = \cos(0) + \sin(0) = 1 + 0 = 1$. Ainsi, $Z_n \xrightarrow{p.s.} 1$.
