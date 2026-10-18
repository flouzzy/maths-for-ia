# Exercice 9 : Démonstration du Lemme de Borel-Cantelli (partie directe) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Le premier lemme de Borel-Cantelli a été un outil clé dans la preuve de la LFGN sous hypothèse de moment d'ordre 4.
Soit $(A_n)_{n \geq 1}$ une suite d'événements dans un espace probabilisé $(\Omega, \mathcal{A}, P)$. On pose $\limsup A_n = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k$ (l'événement "une infinité de $A_n$ se réalisent").
1. Si $\sum_{n=1}^\infty \mathbb{P}(A_n) < \infty$, montrer que $\mathbb{P}(\limsup A_n) = 0$.

**Correction :**
1. Posons $B_n = \bigcup_{k=n}^\infty A_k$. La suite d'événements $(B_n)$ est décroissante pour l'inclusion ($B_{n+1} \subset B_n$). L'événement $\limsup A_n$ est l'intersection décroissante des $B_n$.
Par le théorème de continuité décroissante de la probabilité, on a :
$$\mathbb{P}(\limsup A_n) = \mathbb{P}\left(\bigcap_{n=1}^\infty B_n\right) = \lim_{n \to \infty} \mathbb{P}(B_n)$$
Or, par sous-additivité de la mesure de probabilité (union bound), on a pour tout $n$ :
$$\mathbb{P}(B_n) = \mathbb{P}\left(\bigcup_{k=n}^\infty A_k\right) \leq \sum_{k=n}^\infty \mathbb{P}(A_k)$$
Comme par hypothèse la série $\sum \mathbb{P}(A_k)$ est convergente, le reste d'ordre $n$ de la série, qui est $\sum_{k=n}^\infty \mathbb{P}(A_k)$, tend vers 0 lorsque $n \to \infty$.
On a donc $0 \leq \lim_{n \to \infty} \mathbb{P}(B_n) \leq 0$, d'où $\mathbb{P}(\limsup A_n) = 0$.
