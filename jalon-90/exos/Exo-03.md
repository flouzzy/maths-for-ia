# Exercice 03

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Lemme de Borel-Cantelli

Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires. On suppose que pour tout $\epsilon > 0$, la série $\sum_{n=1}^\infty \mathbb{P}(|X_n| > \epsilon)$ est convergente.
Démontrez que $X_n$ converge presque sûrement vers $0$.

**Correction exhaustive :**
Fixons $\epsilon > 0$. Considérons la suite d'événements $A_n^\epsilon = \{|X_n| > \epsilon\}$.
Par hypothèse, la série $\sum_{n=1}^\infty \mathbb{P}(A_n^\epsilon) < \infty$.
D'après le premier lemme de Borel-Cantelli, la probabilité que l'événement $A_n^\epsilon$ se réalise une infinité de fois est nulle :
$$ \mathbb{P}(\limsup_{n \to \infty} A_n^\epsilon) = 0 $$
L'événement $\limsup A_n^\epsilon$ s'écrit $\bigcap_{N=1}^\infty \bigcup_{n \ge N} A_n^\epsilon$.
Prenons une suite de réels strictement positifs décroissant vers zéro, par exemple $\epsilon_k = \frac{1}{k}$ pour $k \in \mathbb{N}^*$.
Soit $E_k = \limsup_{n \to \infty} A_n^{\epsilon_k}$. Nous avons montré que $\mathbb{P}(E_k) = 0$.
Par sous-additivité de la mesure de probabilité, l'union dénombrable de ces événements de probabilité nulle est également de probabilité nulle :
$$ \mathbb{P}\left(\bigcup_{k=1}^\infty E_k\right) \le \sum_{k=1}^\infty \mathbb{P}(E_k) = 0 $$
Considérons l'événement complémentaire de cette union, notons-le $\Omega^* = \left(\bigcup_{k=1}^\infty E_k\right)^c = \bigcap_{k=1}^\infty E_k^c$. Sa probabilité vaut 1.
Pour tout $\omega \in \Omega^*$, et pour tout $k \ge 1$, $\omega \in E_k^c$, ce qui signifie qu'il n'appartient pas à $\limsup A_n^{\epsilon_k}$.
Donc pour tout $k \ge 1$, l'événement $\{|X_n(\omega)| > \frac{1}{k}\}$ ne se réalise qu'un nombre fini de fois.
Autrement dit, il existe un entier $N(\omega, k)$ tel que pour tout $n \ge N(\omega, k)$, $|X_n(\omega)| \le \frac{1}{k}$.
Ceci est exactement la définition de la convergence $\lim_{n \to \infty} X_n(\omega) = 0$.
Puisque ce résultat est vrai pour tout $\omega \in \Omega^*$, et que $\mathbb{P}(\Omega^*) = 1$, nous avons prouvé que $X_n \xrightarrow{p.s.} 0$.
