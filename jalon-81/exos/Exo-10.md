## Dualité Fourier et translations dans $L^2$

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$


Soit l'opérateur de translation $\tau_a$ défini par $(\tau_a f)(x) = f(x-a)$ et l'opérateur de modulation $M_a$ défini par $(M_a f)(x) = e^{iax} f(x)$.
1. Montrer que $\mathcal{F}(\tau_a f) = M_{-a}(\mathcal{F}f)$ et $\mathcal{F}(M_a f) = \tau_a(\mathcal{F}f)$ sur l'espace dense $\mathcal{S}(\mathbb{R})$.
2. On définit l'opérateur $U_a = \tau_a M_a$. Cet opérateur est-il unitaire sur $L^2(\mathbb{R})$ ?
3. Calculer la norme $L^2$ de $U_a f$ pour tout $f \in L^2(\mathbb{R})$.

### Correction :

1. Commençons par la translation. Soit $f \in \mathcal{S}(\mathbb{R})$.
$$ \mathcal{F}(\tau_a f)(\xi) = \int_{\mathbb{R}} f(x-a) e^{-i\xi x} dx $$
On effectue le changement de variable $y = x-a \implies dx = dy$.
$$ \mathcal{F}(\tau_a f)(\xi) = \int_{\mathbb{R}} f(y) e^{-i\xi (y+a)} dy = e^{-i\xi a} \int_{\mathbb{R}} f(y) e^{-i\xi y} dy = e^{-i\xi a} \hat{f}(\xi) $$
Or, $M_{-a}(\hat{f})(\xi) = e^{-i a \xi} \hat{f}(\xi)$. L'égalité est démontrée.
Pour la modulation :
$$ \mathcal{F}(M_a f)(\xi) = \int_{\mathbb{R}} (e^{iax} f(x)) e^{-i\xi x} dx = \int_{\mathbb{R}} f(x) e^{-i(\xi-a)x} dx = \hat{f}(\xi-a) = (\tau_a \hat{f})(\xi) $$
L'égalité est démontrée.

2. Un opérateur linéaire $T : L^2 \to L^2$ est unitaire s'il est surjectif et préserve la norme, i.e., $\|Tf\|_{L^2} = \|f\|_{L^2}$.
Étudions $U_a f(x) = \tau_a (e^{iax} f(x))$.
$U_a f(x) = e^{ia(x-a)} f(x-a)$.
Calculons la norme :
$$ \|U_a f\|_{L^2}^2 = \int_{\mathbb{R}} |e^{ia(x-a)} f(x-a)|^2 dx $$
Puisque $|e^{ia(x-a)}| = 1$ (c'est une phase pure), on a :
$$ \|U_a f\|_{L^2}^2 = \int_{\mathbb{R}} |f(x-a)|^2 dx $$
Par le changement de variable (isométrie de la mesure de Lebesgue par translation) $y = x-a$, on obtient :
$$ \int_{\mathbb{R}} |f(y)|^2 dy = \|f\|_{L^2}^2 $$
L'opérateur $U_a$ est donc une isométrie.
Pour montrer qu'il est surjectif, cherchons son inverse. L'inverse de la translation par $a$ est la translation par $-a$, et l'inverse de $M_a$ est $M_{-a}$.
L'opérateur inverse existe et est trivialement isométrique, ce qui prouve que $U_a$ est unitaire.

3. D'après la question précédente, pour toute fonction $f \in L^2(\mathbb{R})$, on a rigoureusement :
$$ \|U_a f\|_{L^2} = \|f\|_{L^2} $$
L'énergie est strictement conservée sous les opérations de translation temporelle et de modulation de phase (décalage de fréquence).
