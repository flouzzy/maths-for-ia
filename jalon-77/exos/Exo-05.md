## Exercice 5 : Invariance par translation et continuité en moyenne \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Pour $f \in L^p(\mathbb{R})$ ($1 \le p < \infty$) et $h \in \mathbb{R}$, on définit la fonction translatée $\tau_h f(x) = f(x - h)$.
Démontrer que l'application $h \mapsto \tau_h f$ est continue de $\mathbb{R}$ dans $L^p(\mathbb{R})$.
C'est-à-dire : $\lim_{h \to 0} \| \tau_h f - f \|_p = 0$. On utilisera la densité de $C_c(\mathbb{R})$.

**Correction :**
Fixons $\epsilon > 0$.
Puisque $C_c(\mathbb{R})$ est dense dans $L^p(\mathbb{R})$, il existe $g \in C_c(\mathbb{R})$ telle que $\| f - g \|_p < \frac{\epsilon}{3}$.
Par l'inégalité triangulaire dans $L^p$, on a :
$\| \tau_h f - f \|_p \le \| \tau_h f - \tau_h g \|_p + \| \tau_h g - g \|_p + \| g - f \|_p$.

1. Par invariance de la mesure de Lebesgue par translation, $\| \tau_h f - \tau_h g \|_p = \| f - g \|_p < \frac{\epsilon}{3}$.
2. Le terme de droite $\| g - f \|_p$ est strictement inférieur à $\frac{\epsilon}{3}$.
Il reste à borner $\| \tau_h g - g \|_p$.

La fonction $g$ est continue à support compact. Elle est donc uniformément continue sur $\mathbb{R}$ (Théorème de Heine).
Soit $K$ un compact contenant le support de $g$. Si $|h| \le 1$, le support de $\tau_h g - g$ est inclus dans un compact fixe $K' = K + [-1, 1]$.
Par continuité uniforme, $\lim_{h \to 0} \sup_{x \in \mathbb{R}} |g(x-h) - g(x)| = 0$.
Ainsi, pour $h$ suffisamment petit, $|g(x-h) - g(x)| < \eta$, où $\eta = \frac{\epsilon}{3 \mu(K')^{1/p}}$.
Alors,
$\| \tau_h g - g \|_p = \left( \int_{K'} |g(x-h) - g(x)|^p dx \right)^{1/p} \le \left( \eta^p \mu(K') \right)^{1/p} = \eta \mu(K')^{1/p} = \frac{\epsilon}{3}$.

En additionnant les trois termes, pour $h$ suffisamment petit,
$\| \tau_h f - f \|_p < \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon$.
La continuité en moyenne d'ordre $p$ est ainsi démontrée.
