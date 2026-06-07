# Exercice 7 : Théorème de Borel-Cantelli
**Énoncé :** Soit $(A_n)_{n \ge 1}$ une suite d'événements dans un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$. Démontrer le premier lemme de Borel-Cantelli : si $\sum_{n=1}^\infty \mathbb{P}(A_n) < \infty$, alors $\mathbb{P}(\limsup_{n \to \infty} A_n) = 0$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit prouver que si la somme des probabilités est finie, alors la probabilité qu'une infinité d'événements se réalisent est nulle.
* *Résolution pas-à-pas :*
  1. On définit la limite supérieure des événements $A_n$ par :
     $$ \limsup_{n \to \infty} A_n = \bigcap_{N=1}^\infty \bigcup_{n=N}^\infty A_n $$
     C'est l'événement défini par "pour tout $N$, il existe un $n \ge N$ tel que $A_n$ se réalise".
  2. Par la continuité décroissante de la mesure de probabilité (puisque la suite $B_N = \bigcup_{n=N}^\infty A_n$ est décroissante par inclusion) :
     $$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = \lim_{N \to \infty} \mathbb{P}\left(\bigcup_{n=N}^\infty A_n\right) $$
  3. Par la propriété de sous-additivité (inégalité de Boole) :
     $$ \mathbb{P}\left(\bigcup_{n=N}^\infty A_n\right) \le \sum_{n=N}^\infty \mathbb{P}(A_n) $$
  4. L'hypothèse de départ est que la série complète converge, soit $\sum_{n=1}^\infty \mathbb{P}(A_n) = S < \infty$.
  5. La somme $\sum_{n=N}^\infty \mathbb{P}(A_n)$ correspond au reste d'ordre $N-1$ de cette série convergente.
  6. Un résultat fondamental d'analyse affirme que le reste d'une série convergente tend vers zéro lorsque l'ordre tend vers l'infini :
     $$ \lim_{N \to \infty} \sum_{n=N}^\infty \mathbb{P}(A_n) = 0 $$
  7. En utilisant le fait que les probabilités sont positives ou nulles :
     $$ 0 \le \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) \le \lim_{N \to \infty} \sum_{n=N}^\infty \mathbb{P}(A_n) = 0 $$
  8. On obtient bien :
     $$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 0 $$
