# Exercice 8 : Produit de convolution de polynômes trigonométriques $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f(t) = \cos(2t) + \sin(3t)$ et $g(t) = \sin(2t)$.
Calculer la convolution $(f * g)(t) = \frac{1}{2\pi} \int_0^{2\pi} f(u)g(t-u) du$ en utilisant les coefficients de Fourier complexes.

**Correction Détaillée :**
1. **Coefficients :**
Pour $f$ : $f(t) = \frac{e^{i2t} + e^{-i2t}}{2} + \frac{e^{i3t} - e^{-i3t}}{2i}$.
Les coefficients non nuls sont $c_2(f) = 1/2$, $c_{-2}(f) = 1/2$, $c_3(f) = 1/(2i)$, $c_{-3}(f) = -1/(2i)$.
Pour $g$ : $g(t) = \frac{e^{i2t} - e^{-i2t}}{2i}$.
Les coefficients non nuls sont $c_2(g) = 1/(2i)$, $c_{-2}(g) = -1/(2i)$.

2. **Théorème de Convolution :**
On sait que $c_n(f * g) = c_n(f) \cdot c_n(g)$.
Pour tout $n \notin \{-2, 2\}$, soit $c_n(f)=0$, soit $c_n(g)=0$.
Calculons pour $n=2$ et $n=-2$ :
$c_2(f * g) = c_2(f) \cdot c_2(g) = \frac{1}{2} \cdot \frac{1}{2i} = \frac{1}{4i} = -\frac{i}{4}$.
$c_{-2}(f * g) = c_{-2}(f) \cdot c_{-2}(g) = \frac{1}{2} \cdot \frac{-1}{2i} = -\frac{1}{4i} = \frac{i}{4}$.

3. **Reconstruction :**
La série est finie :
$$ (f * g)(t) = c_{-2} e^{-i2t} + c_2 e^{i2t} = \frac{i}{4} e^{-i2t} - \frac{i}{4} e^{i2t} = -\frac{i}{4} (e^{i2t} - e^{-i2t}) = -\frac{i}{4} \cdot 2i \sin(2t) = \frac{1}{2} \sin(2t) $$
