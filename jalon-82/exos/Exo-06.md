# Exercice 6 : Convergence de distributions singulières (Peigne de Dirac)
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit pour tout entier $N \ge 1$ la distribution $D_N = \sum_{k=-N}^{N} \delta_{k}$.
Montrez que la suite de distributions $(D_N)_{N \ge 1}$ converge dans $\mathcal{D}'(\mathbb{R})$ et déterminez sa limite formelle (que l'on notera "Peigne de Dirac" Ш).

**Correction Détaillée :**
1. **Action de la somme finie :**
   Soit $\varphi \in \mathcal{D}(\mathbb{R})$ une fonction test quelconque.
   L'action de la distribution $D_N$ sur $\varphi$ est par linéarité :
   $$ \langle D_N, \varphi \rangle = \left\langle \sum_{k=-N}^{N} \delta_{k}, \varphi \right\rangle = \sum_{k=-N}^{N} \langle \delta_{k}, \varphi \rangle = \sum_{k=-N}^{N} \varphi(k) $$

2. **Analyse de la limite :**
   Nous devons étudier la limite de la suite numérique $S_N = \sum_{k=-N}^{N} \varphi(k)$ lorsque $N \to +\infty$.
   Par définition, une fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ a un support compact.
   Cela signifie qu'il existe un réel $R > 0$ tel que pour tout $x$ vérifiant $|x| > R$, on a $\varphi(x) = 0$.
   En particulier, il existe un entier $M = \lceil R \rceil$ tel que pour tout entier $k$ avec $|k| > M$, $\varphi(k) = 0$.

3. **Stationnarité de la suite :**
   Par conséquent, dès que $N \ge M$, tous les termes additionnels dans la somme pour $|k| > M$ sont nuls :
   Pour $N \ge M$, $S_N = \sum_{k=-N}^{N} \varphi(k) = \sum_{k=-M}^{M} \varphi(k) + \sum_{M < |k| \le N} 0 = \sum_{k=-M}^{M} \varphi(k)$.
   La suite $(S_N)$ est donc constante (stationnaire) à partir du rang $M$.

4. **Conclusion :**
   La limite existe nécessairement et vaut cette constante :
   $$ \lim_{N \to +\infty} \langle D_N, \varphi \rangle = \sum_{k=-\infty}^{+\infty} \varphi(k) $$
   La somme infinie est en fait une somme finie puisque seuls les termes où $k$ est dans le support de $\varphi$ sont non nuls.
   Nous avons ainsi démontré que la suite converge vers une distribution, le Peigne de Dirac Ш, dont l'action est formellement définie par :
   $$ \langle Ш, \varphi \rangle = \sum_{k \in \mathbb{Z}} \varphi(k) $$
