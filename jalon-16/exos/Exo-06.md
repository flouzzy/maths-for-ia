# Exercice 06 : La série harmonique alternée et positive

## Énoncé
Soit $u_n = \sqrt{n+1} - \sqrt{n}$. Étudier la convergence de la série $\sum_{n \ge 1} u_n$.

## Correction Détaillée
1. **Positivité :**
   Pour tout $n \ge 1$, $n+1 > n$, la fonction racine est croissante donc $\sqrt{n+1} > \sqrt{n}$. $u_n > 0$.

2. **Méthode 1 : Simplification par la quantité conjuguée (pour trouver l'équivalent) :**
   $$u_n = \frac{(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n})}{\sqrt{n+1} + \sqrt{n}}$$
   $$u_n = \frac{(n+1) - n}{\sqrt{n} (\sqrt{1+1/n} + 1)} = \frac{1}{\sqrt{n} (\sqrt{1+1/n} + 1)}$$

3. **Équivalent à l'infini :**
   Lorsque $n \to \infty$, $1/n \to 0$, d'où le terme au dénominateur tend vers $1 + 1 = 2$.
   $$u_n \sim_{+\infty} \frac{1}{2\sqrt{n}}$$
   La série $\sum \frac{1}{\sqrt{n}}$ est une série de Riemann divergente ($\alpha = 1/2 \le 1$). Donc par équivalence pour les termes positifs, la série $\sum u_n$ diverge.

4. **Méthode 2 : Par les sommes partielles (Télescopage) :**
   $S_N = \sum_{n=1}^N (\sqrt{n+1} - \sqrt{n})$
   $$S_N = (\sqrt{2} - \sqrt{1}) + (\sqrt{3} - \sqrt{2}) + \dots + (\sqrt{N+1} - \sqrt{N})$$
   Tous les termes s'annulent sauf le premier et le dernier.
   $$S_N = \sqrt{N+1} - 1$$
   Lorsque $N \to \infty$, $\lim S_N = +\infty$. La série diverge vers l'infini.
