\subsection*{Exercice 10 : Convergence L^p et intégrabilité uniforme \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Soit $X_n \xrightarrow{\mathbb{P}} X$. Montrer que $X_n \xrightarrow{L^p} X$ si et seulement si la suite $(|X_n|^p)$ est uniformément intégrable.
Définition: Une famille $(Y_n)$ est uniformément intégrable si $\lim_{K \to \infty} \sup_n \mathbb{E}[|Y_n| \mathbf{1}_{|Y_n| > K}] = 0$.

**Correction :**
Ce résultat, connu sous le nom de théorème de convergence de Vitali, généralise le théorème de convergence dominée de Lebesgue.
($\Rightarrow$) Supposons que $X_n \xrightarrow{L^p} X$. Posons $Z_n = |X_n|^p$. On a $\lim_n \mathbb{E}[|X_n - X|^p] = 0$. L'inégalité de Minkowski montre que $\mathbb{E}[Z_n] \to \mathbb{E}[|X|^p]$. La convergence dans $L^p$ pour $L^1$ des $|X_n|^p$ implique leur intégrabilité uniforme selon un résultat fondamental d'analyse.
($\Leftarrow$) Supposons $X_n \xrightarrow{\mathbb{P}} X$ et que $|X_n|^p$ est uniformément intégrable.
Pour $R > 0$, considérons la fonction de troncature $T_R(x) = \max(-R, \min(x, R))$. La fonction est bornée et continue.
On a $|X_n - X|^p \le 2^{p-1}(|X_n|^p + |X|^p)$. L'intégrabilité uniforme de la somme de séquences uniformément intégrables garantit que $|X_n - X|^p$ est uniformément intégrable.
On décompose l'espérance:
$\mathbb{E}[|X_n - X|^p] = \mathbb{E}[|X_n - X|^p \mathbf{1}_{|X_n - X| \le \delta}] + \mathbb{E}[|X_n - X|^p \mathbf{1}_{|X_n - X| > \delta, |X_n - X| \le M}] + \mathbb{E}[|X_n - X|^p \mathbf{1}_{|X_n - X| > M}]$.
- Le premier terme est majoré par $\delta^p$.
- Le deuxième terme est majoré par $M^p \mathbb{P}(|X_n - X| > \delta)$, qui tend vers 0 par convergence en probabilité.
- Le troisième terme est contrôlé indépendamment de $n$ et de $\delta$ en choisissant $M$ grand, grâce à l'intégrabilité uniforme, il peut être rendu $<\varepsilon$.
On a donc $\limsup \mathbb{E}[|X_n - X|^p] \le \delta^p + \varepsilon$. En faisant tendre $\delta \to 0$ puis $\varepsilon \to 0$, on obtient bien la convergence $L^p$.
