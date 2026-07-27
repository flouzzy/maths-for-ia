with open("jalon-26/exos/Exo-03.md", "r") as f:
    text = f.read()

# Replace empty proof stubs with actual detailed proofs
if "## Démonstration Rigoureuse à Blanc\n\n1." in text:
    # Just in case we already started
    pass
else:
    new_text = r"""---
uuid: "jalon-26-exo-03"
title: "Orthogonalité dans les polynômes"
difficulty: 3
---

# Exercice 3 : Orthogonalité dans les polynômes (Difficulté ★★★☆☆)

Soit $E = \mathbb{R}_2[X]$ l'espace des polynômes de degré inférieur ou égal à 2. On définit pour $P, Q \in E$ :
$\langle P, Q \rangle = P(0)Q(0) + P(1)Q(1) + P(2)Q(2)$.

1. Prouver de manière exhaustive que cette forme est un produit scalaire. Vous justifierez minutieusement le fait que si $P(0)^2+P(1)^2+P(2)^2=0$ alors $P$ est le polynôme nul.
2. La famille $(1, X, X^2)$ est-elle orthogonale pour ce produit scalaire ?
3. Déterminer une base orthonormée de $E$ en appliquant méticuleusement l'algorithme de Gram-Schmidt à la base canonique $(1, X, X^2)$.

## Démonstration Rigoureuse à Blanc

1. Vérifions les axiomes du produit scalaire pour la forme définie sur $E = \mathbb{R}_2[X]$.
   - **Symétrie** : Soient $P, Q \in E$.
     $$ \langle P, Q \rangle = P(0)Q(0) + P(1)Q(1) + P(2)Q(2) = Q(0)P(0) + Q(1)P(1) + Q(2)P(2) = \langle Q, P \rangle $$
   - **Bilinéarité** : Soient $P, Q, R \in E$ et $\lambda \in \mathbb{R}$.
     $$ \langle \lambda P + Q, R \rangle = (\lambda P(0) + Q(0))R(0) + (\lambda P(1) + Q(1))R(1) + (\lambda P(2) + Q(2))R(2) $$
     En développant et en regroupant :
     $$ = \lambda (P(0)R(0) + P(1)R(1) + P(2)R(2)) + (Q(0)R(0) + Q(1)R(1) + Q(2)R(2)) = \lambda \langle P, R \rangle + \langle Q, R \rangle $$
     Par symétrie, l'application est bilinéaire.
   - **Positivité** : Pour $P \in E$,
     $$ \langle P, P \rangle = P(0)^2 + P(1)^2 + P(2)^2 $$
     Ceci est une somme de carrés de nombres réels, elle est donc toujours positive ou nulle.
   - **Caractère défini** : Supposons que $\langle P, P \rangle = 0$.
     Cela implique $P(0)^2 + P(1)^2 + P(2)^2 = 0$. Une somme de termes positifs est nulle si et seulement si chaque terme est nul. Donc :
     $$ P(0) = 0, \quad P(1) = 0, \quad P(2) = 0 $$
     Le polynôme $P$ admet donc au moins trois racines distinctes : 0, 1 et 2. Or, $P \in \mathbb{R}_2[X]$, ce qui signifie que le degré de $P$ est inférieur ou égal à 2. Un polynôme non nul de degré $n$ admet au plus $n$ racines. Puisque $P$ a plus de racines que son degré maximal, $P$ est nécessairement le polynôme nul. Donc $P = 0_E$.
     L'application est un produit scalaire.

2. Vérifions l'orthogonalité de la base canonique $(e_0, e_1, e_2) = (1, X, X^2)$.
   Calculons $\langle e_0, e_1 \rangle = \langle 1, X \rangle$ :
   $$ \langle 1, X \rangle = 1(0) + 1(1) + 1(2) = 0 + 1 + 2 = 3 $$
   Puisque $\langle e_0, e_1 \rangle \neq 0$, la famille n'est pas orthogonale. (Il est inutile de calculer les autres produits scalaires pour conclure).

3. Appliquons le procédé d'orthonormalisation de Gram-Schmidt à la base canonique $(e_0, e_1, e_2) = (1, X, X^2)$ pour obtenir une base orthonormée $(u_0, u_1, u_2)$.
   - **Étape 1 : Construction de $u_0$.**
     Posons $v_0 = e_0 = 1$. Calculons sa norme :
     $$ \|v_0\|^2 = \langle 1, 1 \rangle = 1^2 + 1^2 + 1^2 = 3 \implies \|v_0\| = \sqrt{3} $$
     Donc $u_0 = \frac{v_0}{\|v_0\|} = \frac{1}{\sqrt{3}}$.

   - **Étape 2 : Construction de $u_1$.**
     Posons $v_1 = e_1 - \langle e_1, u_0 \rangle u_0$.
     Calculons d'abord $\langle e_1, u_0 \rangle = \langle X, \frac{1}{\sqrt{3}} \rangle$ :
     $$ \langle X, \frac{1}{\sqrt{3}} \rangle = 0 \cdot \frac{1}{\sqrt{3}} + 1 \cdot \frac{1}{\sqrt{3}} + 2 \cdot \frac{1}{\sqrt{3}} = \frac{3}{\sqrt{3}} = \sqrt{3} $$
     Donc $v_1 = X - \sqrt{3} \cdot \frac{1}{\sqrt{3}} = X - 1$.
     Calculons la norme de $v_1$ :
     $$ \|v_1\|^2 = \langle X-1, X-1 \rangle = (-1)^2 + 0^2 + 1^2 = 1 + 0 + 1 = 2 \implies \|v_1\| = \sqrt{2} $$
     Donc $u_1 = \frac{v_1}{\|v_1\|} = \frac{X - 1}{\sqrt{2}}$.

   - **Étape 3 : Construction de $u_2$.**
     Posons $v_2 = e_2 - \langle e_2, u_0 \rangle u_0 - \langle e_2, u_1 \rangle u_1$.
     Calculons $\langle e_2, u_0 \rangle = \langle X^2, \frac{1}{\sqrt{3}} \rangle$ :
     $$ \langle X^2, \frac{1}{\sqrt{3}} \rangle = 0 \cdot \frac{1}{\sqrt{3}} + 1 \cdot \frac{1}{\sqrt{3}} + 4 \cdot \frac{1}{\sqrt{3}} = \frac{5}{\sqrt{3}} $$
     Le premier terme retranché est $\frac{5}{\sqrt{3}} \frac{1}{\sqrt{3}} = \frac{5}{3}$.
     Calculons $\langle e_2, u_1 \rangle = \langle X^2, \frac{X-1}{\sqrt{2}} \rangle$ :
     $$ \langle X^2, \frac{X-1}{\sqrt{2}} \rangle = 0 \cdot \frac{-1}{\sqrt{2}} + 1 \cdot 0 + 4 \cdot \frac{1}{\sqrt{2}} = \frac{4}{\sqrt{2}} = 2\sqrt{2} $$
     Le second terme retranché est $2\sqrt{2} \frac{X-1}{\sqrt{2}} = 2(X-1) = 2X - 2$.
     Donc $v_2 = X^2 - \frac{5}{3} - (2X - 2) = X^2 - 2X + \frac{1}{3}$.
     Calculons la norme de $v_2$ :
     Pour $X=0$: $v_2(0) = \frac{1}{3}$. Pour $X=1$: $v_2(1) = 1 - 2 + \frac{1}{3} = -\frac{2}{3}$. Pour $X=2$: $v_2(2) = 4 - 4 + \frac{1}{3} = \frac{1}{3}$.
     $$ \|v_2\|^2 = \left(\frac{1}{3}\right)^2 + \left(-\frac{2}{3}\right)^2 + \left(\frac{1}{3}\right)^2 = \frac{1}{9} + \frac{4}{9} + \frac{1}{9} = \frac{6}{9} = \frac{2}{3} $$
     Donc $\|v_2\| = \sqrt{\frac{2}{3}}$.
     Ainsi, $u_2 = \frac{v_2}{\|v_2\|} = \sqrt{\frac{3}{2}} (X^2 - 2X + \frac{1}{3})$.

   La base orthonormée finale est : $\left( \frac{1}{\sqrt{3}}, \frac{X - 1}{\sqrt{2}}, \sqrt{\frac{3}{2}} \left( X^2 - 2X + \frac{1}{3} \right) \right)$.
   $\blacksquare$
"""
    with open("jalon-26/exos/Exo-03.md", "w", encoding='utf-8') as f:
        f.write(new_text)
