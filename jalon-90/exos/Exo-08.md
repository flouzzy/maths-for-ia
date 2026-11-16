# Exercice 8 : Cas où la convergence en probabilité vers une constante implique la convergence dans $L^p$

Niveau : $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $(X_n)$ une suite de variables aléatoires vérifiant :
1. $X_n \xrightarrow{\mathbb{P}} c$ (où $c$ est une constante réelle).
2. Il existe une constante $M > 0$ telle que pour tout $n$, $|X_n| \le M$ presque sûrement. (On dit que la suite est uniformément bornée).
Montrer que pour tout $p \ge 1$, $X_n \xrightarrow{L^p} c$.

## Correction

Soit $p \ge 1$ et soit $\varepsilon > 0$. On veut montrer que $\lim_{n \to \infty} \mathbb{E}[|X_n - c|^p] = 0$.
Séparons l'espérance selon que $|X_n - c|$ est grand ou petit, en utilisant l'événement $A_n = \{|X_n - c| \le \varepsilon\}$ et son complémentaire $A_n^c = \{|X_n - c| > \varepsilon\}$.
On utilise la linéarité de l'espérance en l'écrivant comme l'intégrale (l'espérance) sur les indicatrices :
$$\mathbb{E}[|X_n - c|^p] = \mathbb{E}[|X_n - c|^p \mathbb{1}_{A_n}] + \mathbb{E}[|X_n - c|^p \mathbb{1}_{A_n^c}]$$
Majorons chaque terme :
- Sur l'événement $A_n$, on a par définition $|X_n - c| \le \varepsilon$, donc $|X_n - c|^p \le \varepsilon^p$. Ainsi :
$$\mathbb{E}[|X_n - c|^p \mathbb{1}_{A_n}] \le \varepsilon^p \mathbb{E}[\mathbb{1}_{A_n}] \le \varepsilon^p \cdot 1 = \varepsilon^p$$
- Sur l'événement $A_n^c$, on utilise la borne uniforme. Presque sûrement, $|X_n| \le M$. De plus, $|c| \le M$ (sinon $X_n$ ne pourrait pas converger en probabilité vers $c$).
Ainsi, par l'inégalité triangulaire, presque sûrement, $|X_n - c| \le |X_n| + |c| \le 2M$.
Donc $|X_n - c|^p \le (2M)^p$.
On majore alors le second terme :
$$\mathbb{E}[|X_n - c|^p \mathbb{1}_{A_n^c}] \le (2M)^p \mathbb{E}[\mathbb{1}_{A_n^c}] = (2M)^p \mathbb{P}(|X_n - c| > \varepsilon)$$
En combinant les deux majorations, on obtient pour tout $n$ :
$$\mathbb{E}[|X_n - c|^p] \le \varepsilon^p + (2M)^p \mathbb{P}(|X_n - c| > \varepsilon)$$
Maintenant, prenons la limite quand $n \to +\infty$. Comme $X_n \xrightarrow{\mathbb{P}} c$, on sait que $\lim_{n \to \infty} \mathbb{P}(|X_n - c| > \varepsilon) = 0$.
Donc :
$$\limsup_{n \to \infty} \mathbb{E}[|X_n - c|^p] \le \varepsilon^p + 0 = \varepsilon^p$$
Cette inégalité est vraie pour tout $\varepsilon > 0$. En faisant tendre $\varepsilon \to 0$, on obtient :
$$\limsup_{n \to \infty} \mathbb{E}[|X_n - c|^p] \le 0$$
Puisque l'espérance est toujours positive, on conclut que $\lim_{n \to \infty} \mathbb{E}[|X_n - c|^p] = 0$.
La suite converge donc vers $c$ dans $L^p$. C'est un cas particulier du théorème de convergence dominée généralisé (uniforme intégrabilité).
