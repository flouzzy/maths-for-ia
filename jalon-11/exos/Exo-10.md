# Exercice 10: Somme directe et annulateur
## Énoncé
Soit $E$ un espace vectoriel de dimension finie, et $F, G$ deux sous-espaces vectoriels de $E$.
Montrer que $E = F \oplus G$ si et seulement si $E^* = F^\circ \oplus G^\circ$.


## Correction détaillée
**Preuve du sens direct :**
Supposons $E = F \oplus G$. Tout vecteur $x \in E$ se décompose de manière unique en $x = x_F + x_G$ avec $x_F \in F$ et $x_G \in G$.
1. **Intersection nulle :** Soit $\varphi \in F^\circ \cap G^\circ$.
   Alors $\forall f \in F, \varphi(f) = 0$ et $\forall g \in G, \varphi(g) = 0$.
   Pour tout $x \in E$, $\varphi(x) = \varphi(x_F + x_G) = \varphi(x_F) + \varphi(x_G) = 0 + 0 = 0$.
   Donc $\varphi = 0_{E^*}$. Ainsi $F^\circ \cap G^\circ = \{0_{E^*}\}$.
2. **Somme de l'espace :** Par les propriétés des annulateurs, $\dim(F^\circ) = \dim(E) - \dim(F)$ et $\dim(G^\circ) = \dim(E) - \dim(G)$.
   Puisque $E = F \oplus G$, on a $\dim(E) = \dim(F) + \dim(G)$.
   Calculons la dimension de la somme $F^\circ + G^\circ$ :
   $\dim(F^\circ + G^\circ) = \dim(F^\circ) + \dim(G^\circ) - \dim(F^\circ \cap G^\circ)$
   $= (\dim E - \dim F) + (\dim E - \dim G) - 0$
   $= 2\dim E - (\dim F + \dim G) = 2\dim E - \dim E = \dim E$.
   Le sous-espace $F^\circ + G^\circ$ a la même dimension que $E^*$, donc $F^\circ \oplus G^\circ = E^*$.

**Preuve du sens indirect :**
Supposons $E^* = F^\circ \oplus G^\circ$.
Par un argument sur les dimensions, on a $\dim(E^*) = \dim(F^\circ) + \dim(G^\circ)$.
Soit $n = \dim(E) = \dim(E^*)$. On a :
$n = (n - \dim F) + (n - \dim G) \implies \dim F + \dim G = n$.
Il suffit maintenant de montrer que $F \cap G = \{0\}$.
Soit $x \in F \cap G$. Pour toute forme $\varphi \in E^*$, on peut l'écrire $\varphi = \varphi_F + \varphi_G$ avec $\varphi_F \in F^\circ$ et $\varphi_G \in G^\circ$.
Évaluons $\varphi$ sur $x$ :
$\varphi(x) = (\varphi_F + \varphi_G)(x) = \varphi_F(x) + \varphi_G(x)$.
Comme $x \in F$ et $\varphi_F \in F^\circ$, $\varphi_F(x) = 0$.
Comme $x \in G$ et $\varphi_G \in G^\circ$, $\varphi_G(x) = 0$.
Donc $\forall \varphi \in E^*, \varphi(x) = 0$.
Ceci implique que l'évaluation $\text{ev}_x$ est nulle, et par l'isomorphisme du bidual, $x = 0_E$.
Ainsi $F \cap G = \{0\}$, et la somme des dimensions donne $\dim E$, ce qui prouve $E = F \oplus G$.
