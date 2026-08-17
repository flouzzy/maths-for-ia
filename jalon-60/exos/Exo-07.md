## Exercice 7 : Théorème d'approximation et réseaux ReLU profonds \quad $\bigstar\bigstar\bigstar\bigstar\star$

Démontrer qu'un réseau composé uniquement de couches affines et de la fonction d'activation identité ne peut pas être un approximateur universel, quelle que soit sa profondeur.

**Correction :**
Soit un réseau avec $L$ couches, où la $k$-ème couche calcule $x^{(k)} = W^{(k)} x^{(k-1)} + b^{(k)}$.
Par récurrence immédiate, on a $x^{(1)} = W^{(1)} x^{(0)} + b^{(1)}$ (une fonction affine de l'entrée $x^{(0)}$).
Supposons que $x^{(k-1)} = A x^{(0)} + c$ pour des matrices $A$ et vecteurs $c$.
Alors $x^{(k)} = W^{(k)} (A x^{(0)} + c) + b^{(k)} = (W^{(k)} A) x^{(0)} + (W^{(k)} c + b^{(k)})$.
La composition de fonctions affines est une fonction affine.
Ainsi, le réseau complet calcule une fonction $f(x) = W x + B$.
L'ensemble de ces fonctions n'est que l'ensemble des applications affines, qui est de dimension finie et donc fermé et non dense dans $\mathcal{C}(I_n)$. Sans la non-linéarité (comme la ReLU ou la sigmoïde), la profondeur est inutile.
