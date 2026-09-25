# Exercice 10 : Équation différentielle résolue par Fourier \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Trouver une solution $2\pi$-périodique de l'équation différentielle $y'' + 2y = |\sin(t)|$ en utilisant les séries de Fourier.

**Correction Détaillée :**

1. \textbf{Analyse du second membre :}
   Soit $f(t) = |\sin(t)|$. C'est une fonction paire, $2\pi$-périodique (et même $\pi$-périodique).
   Calculons sa série de Fourier. Les $b_n$ sont nuls.
   La période utile est $\pi$. Pour utiliser la formulation usuelle $2\pi$, on note que la fondamentale est $2t$.
   $$ a_0 = \frac{1}{\pi} \int_0^\pi \sin(t) dt = \frac{2}{\pi} $$
   Pour $n \ge 1$ : $a_n = \frac{2}{\pi} \int_0^\pi \sin(t) \cos(nt) dt$.
   On utilise $\sin(t)\cos(nt) = \frac{1}{2}(\sin((n+1)t) - \sin((n-1)t))$.
   Si $n$ est impair ($n=2p+1$), l'intégrale est nulle par symétrie.
   Si $n$ est pair ($n=2p$), on trouve :
   $$ a_{2p} = -\frac{4}{\pi(4p^2 - 1)} $$
   Le second membre s'écrit donc : $f(t) = \frac{2}{\pi} - \frac{4}{\pi} \sum_{p=1}^\infty \frac{\cos(2pt)}{4p^2 - 1}$.

2. \textbf{Recherche de la solution sous forme de série :}
   Supposons que $y(t) = \alpha_0 + \sum_{n=1}^\infty \alpha_n \cos(nt)$. (La parité dicte de ne chercher que des cosinus).
   D'après le théorème de dérivation (Exercice 9), $y''(t) = -\sum_{n=1}^\infty n^2 \alpha_n \cos(nt)$.
   L'équation donne :
   $$ \left( 2\alpha_0 + \sum_{n=1}^\infty (2 - n^2)\alpha_n \cos(nt) \right) = \frac{2}{\pi} - \frac{4}{\pi} \sum_{p=1}^\infty \frac{\cos(2pt)}{4p^2 - 1} $$

3. \textbf{Identification des coefficients (Unicité) :}
   Pour le terme constant : $2\alpha_0 = \frac{2}{\pi} \implies \alpha_0 = \frac{1}{\pi}$.
   Pour les harmoniques impairs ($n=2p+1$) : le second membre n'en a pas, donc $(2 - (2p+1)^2)\alpha_{2p+1} = 0 \implies \alpha_{2p+1} = 0$.
   Pour les harmoniques pairs ($n=2p$) :
   $$ (2 - 4p^2)\alpha_{2p} = -\frac{4}{\pi(4p^2 - 1)} \implies \alpha_{2p} = \frac{4}{\pi(4p^2 - 1)(4p^2 - 2)} $$

4. \textbf{Conclusion :}
   La solution formelle est :
   $$ y(t) = \frac{1}{\pi} + \frac{2}{\pi} \sum_{p=1}^\infty \frac{\cos(2pt)}{(4p^2 - 1)(2p^2 - 1)} $$
   La décroissance très rapide des coefficients (en $1/p^4$) garantit la convergence uniforme de la série et de ses dérivées, ce qui valide pleinement la solution.
