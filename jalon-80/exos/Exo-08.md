\subsection*{Exercice 8 : Déphasage et convolution \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Soient $f, g \in L^1(\mathbb{R})$.
On considère les fonctions modulées $f_1(t) = e^{i\omega_0 t} f(t)$ et la fonction translatée $g_a(t) = g(t-a)$.
Exprimer la transformée de Fourier de $f_1 * g_a$ en fonction de $\hat{f}$ et $\hat{g}$.

---
**Correction :**

Rappelons les propriétés de base :
1) Translation temporelle : $\mathcal{F}(g(t-a))(\xi) = e^{-ia\xi} \hat{g}(\xi)$. Donc $\widehat{g_a}(\xi) = e^{-ia\xi} \hat{g}(\xi)$.
2) Modulation (translation fréquentielle) :
$\mathcal{F}(e^{i\omega_0 t} f(t))(\xi) = \int f(t) e^{i\omega_0 t} e^{-i\xi t} dt = \int f(t) e^{-i(\xi - \omega_0) t} dt = \hat{f}(\xi - \omega_0)$.
Donc $\widehat{f_1}(\xi) = \hat{f}(\xi - \omega_0)$.

D'après le théorème de convolution, la transformée de $f_1 * g_a$ est le produit des transformées :
$\mathcal{F}(f_1 * g_a)(\xi) = \widehat{f_1}(\xi) \cdot \widehat{g_a}(\xi)$.
En remplaçant par les expressions trouvées :
$\mathcal{F}(f_1 * g_a)(\xi) = \hat{f}(\xi - \omega_0) \cdot \left( e^{-ia\xi} \hat{g}(\xi) \right)$.
Soit :
$$ \mathcal{F}(f_1 * g_a)(\xi) = e^{-ia\xi} \hat{f}(\xi - \omega_0) \hat{g}(\xi) $$
Cette opération illustre l'impact croisé des modulations (qui décalent le spectre de $f$) et des translations (qui ajoutent une phase linéaire au spectre de $g$) dans les filtres appliqués aux signaux.
