# Exercice 9 : Dualité Fourier et bases hilbertiennes
$\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(e_n)_{n \in \mathbb{N}}$ une base hilbertienne de l'espace de Hilbert complexe $L^2(\mathbb{R})$.
1. Rappeler ce que signifie le fait que $(e_n)$ soit une base hilbertienne.
2. Définissons la suite de fonctions $E_n = \frac{1}{\sqrt{2\pi}} \widetilde{\mathcal{F}}(e_n)$. Montrer que $(E_n)_{n \in \mathbb{N}}$ forme également une base hilbertienne de $L^2(\mathbb{R})$.
3. Exprimer les coefficients de Fourier généralisés d'une fonction $f \in L^2(\mathbb{R})$ dans la base $(E_n)$ en fonction des coefficients spectraux $\hat{f}$.

---
**Correction :**
**Question 1 : Définition d'une base hilbertienne**
La suite $(e_n)_{n \in \mathbb{N}}$ est une base hilbertienne de $L^2(\mathbb{R})$ si :
- Elle est orthonormée : $\langle e_n, e_m \rangle_{L^2} = \delta_{n,m}$.
- Elle est totale : l'espace engendré par des combinaisons linéaires finies de $e_n$ est dense dans $L^2(\mathbb{R})$. De façon équivalente, pour tout $f \in L^2$, $f = \sum_{n=0}^{+\infty} \langle f, e_n \rangle e_n$, avec convergence dans $L^2$.

**Question 2 : Image par Fourier normalisée**
Soit l'opérateur $\mathcal{U} = \frac{1}{\sqrt{2\pi}} \widetilde{\mathcal{F}}$. Le théorème de Plancherel stipule que $\|\widetilde{\mathcal{F}}(f)\|_2 = \sqrt{2\pi}\|f\|_2$, donc $\|\mathcal{U}(f)\|_2 = \|f\|_2$.
L'opérateur $\mathcal{U}$ est donc une isométrie surjective de $L^2(\mathbb{R})$ sur lui-même (un isomorphisme unitaire).
On sait qu'un opérateur unitaire préserve le produit scalaire :
$$ \langle \mathcal{U}(e_n), \mathcal{U}(e_m) \rangle_{L^2} = \langle e_n, e_m \rangle_{L^2} = \delta_{n,m} $$
Donc $E_n = \mathcal{U}(e_n)$ forme une famille orthonormée.
Pour montrer qu'elle est totale, considérons $g \in L^2(\mathbb{R})$ telle que $\langle g, E_n \rangle_{L^2} = 0$ pour tout $n$.
$$ 0 = \langle g, \mathcal{U}(e_n) \rangle = \langle \mathcal{U}^{-1}(g), e_n \rangle $$
Puisque $(e_n)$ est totale, cela implique $\mathcal{U}^{-1}(g) = 0$, et comme $\mathcal{U}^{-1}$ est inversible, $g = 0$.
Ainsi, l'orthogonal de $\text{Vect}(E_n)$ est réduit à $\{0\}$, ce qui signifie que $(E_n)$ est totale et constitue donc une base hilbertienne.

**Question 3 : Coefficients de Fourier dans la base $(E_n)$**
Pour tout $f \in L^2(\mathbb{R})$, on peut l'écrire dans la base $(E_n)$ :
$$ f = \sum_{n=0}^{+\infty} c_n E_n \quad \text{avec} \quad c_n = \langle f, E_n \rangle_{L^2} $$
Calculons $c_n$ :
$$ c_n = \langle f, E_n \rangle_{L^2} = \langle f, \mathcal{U}(e_n) \rangle_{L^2} = \int_{-\infty}^{+\infty} f(\xi) \overline{\mathcal{U}(e_n)(\xi)} d\xi $$
Par définition de $\mathcal{U}$, $\mathcal{U}(e_n)(\xi) = \frac{1}{\sqrt{2\pi}} \hat{e}_n(\xi)$. Or, l'opérateur unitaire a pour adjoint son inverse $\mathcal{U}^* = \mathcal{U}^{-1}$, qui correspond à la transformée de Fourier inverse.
$$ c_n = \langle \mathcal{U}^{-1}(f), e_n \rangle_{L^2} = \langle \frac{1}{\sqrt{2\pi}} \mathcal{F}^{-1}(f), e_n \rangle_{L^2} $$
Mais il est souvent plus direct d'utiliser la relation de Parseval :
$$ \langle g, h \rangle_{L^2} = \langle \mathcal{U}(g), \mathcal{U}(h) \rangle_{L^2} $$
Soit $g$ tel que $\mathcal{U}(g) = f$. Alors $g = \mathcal{U}^{-1}(f)$.
$$ c_n = \langle \mathcal{U}(g), \mathcal{U}(e_n) \rangle_{L^2} = \langle g, e_n \rangle_{L^2} = \langle \mathcal{U}^{-1}(f), e_n \rangle_{L^2} $$
Ce qui démontre que l'analyse d'un signal dans la base fréquentielle image de Fourier équivaut à décomposer la transformée inverse de ce signal dans la base d'origine.
