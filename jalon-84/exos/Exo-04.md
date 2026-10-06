# Exercice 04 : Analyse spectrale et Fourier

**Niveau :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
On considère un signal discret de longueur $N=1024$ et de fréquence d'échantillonnage $f_s = 16000$ Hz. On souhaite appliquer une fenêtre de Hann de longueur $L=512$.
1. Quelle est la résolution fréquentielle du spectrogramme généré ?
2. Calculez l'énergie de la fenêtre de Hann discrète définie par $w[n] = 0.5(1 - \cos(2\pi n / (L-1)))$ pour $n=0, \dots, L-1$.

**Correction Détaillée :**
1. La résolution fréquentielle d'une transformée de Fourier sur $L$ points est donnée par $\Delta f = \frac{f_s}{L}$.
   Ici, $\Delta f = \frac{16000}{512} = 31.25$ Hz.
2. L'énergie de la fenêtre discrète est la somme des carrés de ses éléments :
   $$ E = \sum_{n=0}^{L-1} |w[n]|^2 = \sum_{n=0}^{L-1} 0.25 (1 - \cos(2\pi n / (L-1)))^2 $$
   En développant le carré : $(1 - \cos(x))^2 = 1 - 2\cos(x) + \cos^2(x)$.
   On sait que $\cos^2(x) = 0.5(1 + \cos(2x))$.
   Ainsi, en sommant sur une ou plusieurs périodes entières (pour un $L$ grand, l'approximation intégrale est excellente) :
   $$ E \approx L \times 0.25 \times (1 - 0 + 0.5) = L \times 0.25 \times 1.5 = \frac{3L}{8} $$
   Ici $L=512$, donc $E \approx \frac{3 \times 512}{8} = 192$.
   L'énergie est donc approchée par 192.
