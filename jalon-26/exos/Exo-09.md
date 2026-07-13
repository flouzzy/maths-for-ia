---
uuid: "jalon-26-exo-09"
title: "Séries de Fourier géométriques"
difficulty: 3
---

# Exercice 9 : Séries de Fourier géométriques (Difficulté ★★★☆☆)

Soit $E = C([-\pi, \pi], \mathbb{R})$ muni du produit scalaire $\langle f, g \rangle = \frac{1}{\pi} \int_{-\pi}^\pi f(t)g(t)dt$.
1. Montrer que la famille de fonctions $\mathcal{B} = (\frac{1}{\sqrt{2}}, \cos(t), \sin(t), \cos(2t), \sin(2t), \ldots, \cos(nt), \sin(nt))$ est orthonormée.
2. Soit $f \in E$. Exprimer la projection orthogonale de $f$ sur le sous-espace engendré par $\mathcal{B}$ en fonction des coefficients de Fourier $a_k$ et $b_k$.
3. Écrire l'inégalité de Bessel dans ce contexte.

## Démonstration Rigoureuse à Blanc

1. Posons $e_0(t) = \frac{1}{\sqrt{2}}$, $c_k(t) = \cos(kt)$, $s_k(t) = \sin(kt)$ pour $k \ge 1$.
   - $\|e_0\|^2 = \frac{1}{\pi} \int_{-\pi}^\pi \frac{1}{2} dt = \frac{1}{2\pi} [t]_{-\pi}^\pi = \frac{2\pi}{2\pi} = 1$.
   - $\|c_k\|^2 = \frac{1}{\pi} \int_{-\pi}^\pi \cos^2(kt) dt = \frac{1}{\pi} \int_{-\pi}^\pi \frac{1 + \cos(2kt)}{2} dt = \frac{1}{2\pi} [t + \frac{\sin(2kt)}{2k}]_{-\pi}^\pi = 1$.
   - De même $\|s_k\|^2 = 1$. Tous les vecteurs sont normés.
   - Orthogonalité : $\langle e_0, c_k \rangle = \frac{1}{\pi \sqrt{2}} \int_{-\pi}^\pi \cos(kt) dt = 0$.
   - $\langle c_k, s_m \rangle = \frac{1}{\pi} \int_{-\pi}^\pi \cos(kt)\sin(mt) dt = 0$ (fonction impaire sur un intervalle symétrique).
   - $\langle c_k, c_m \rangle$ avec $k \neq m$ :
     $$ = \frac{1}{\pi} \int_{-\pi}^\pi \frac{1}{2}(\cos((k+m)t) + \cos((k-m)t)) dt = 0 $$.
   - L'orthogonalité est prouvée, la famille est orthonormée.

2. Soit $F_n = \text{Vect}(\mathcal{B}_n)$. Puisque $\mathcal{B}_n$ est orthonormée, la projection $S_n(f)$ s'écrit :
   $$ S_n(f) = \langle f, e_0 \rangle e_0 + \sum_{k=1}^n (\langle f, c_k \rangle c_k + \langle f, s_k \rangle s_k) $$
   - Or $\langle f, e_0 \rangle = \frac{1}{\pi} \int f(t)\frac{1}{\sqrt{2}} dt = \frac{a_0}{\sqrt{2}}$. Donc $\langle f, e_0 \rangle e_0 = \frac{a_0}{2}$.
   - $\langle f, c_k \rangle = \frac{1}{\pi} \int f(t)\cos(kt) dt = a_k$.
   - $\langle f, s_k \rangle = \frac{1}{\pi} \int f(t)\sin(kt) dt = b_k$.
   - Finalement :
     $$ S_n(f)(t) = \frac{a_0}{2} + \sum_{k=1}^n (a_k \cos(kt) + b_k \sin(kt)) $$
   C'est la somme partielle de la série de Fourier.

3. D'après le théorème de projection, le projeté a une norme inférieure ou égale à celle de $f$ :
   $$ \|S_n(f)\|^2 \le \|f\|^2 $$
   Or par le théorème de Pythagore sur la base orthonormée :
   $$ \|S_n(f)\|^2 = |\langle f, e_0 \rangle|^2 + \sum_{k=1}^n (\langle f, c_k \rangle^2 + \langle f, s_k \rangle^2) $$
   $$ = \frac{a_0^2}{2} + \sum_{k=1}^n (a_k^2 + b_k^2) $$
   L'inégalité de Bessel s'écrit donc :
   $$ \frac{a_0^2}{2} + \sum_{k=1}^n (a_k^2 + b_k^2) \le \frac{1}{\pi} \int_{-\pi}^\pi f(t)^2 dt $$
   $\blacksquare$
