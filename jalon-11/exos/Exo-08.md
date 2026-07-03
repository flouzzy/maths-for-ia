---
uuid: "exo-11-08"
title: "Exercice 8: Bidulalité et annulateur d'annulateur"
---
# Exercice 8: Bidulalité et annulateur d'annulateur (Difficulté $\star \star \star \star \star$)

## Énoncé
Soit $E$ un espace vectoriel de dimension finie. Soit $F$ un sous-espace vectoriel de $E$. En utilisant l'isomorphisme canonique $\Psi : E \to E^{**}$, démontrer formellement la propriété d'involution orthogonale : $(F^\perp)^\circ = F$, où l'orthogonalité est prise dans le sens des espaces duaux.

## Correction détaillée

1. **Définition rigoureuse des espaces d'annulateurs :**
   Rappelons les définitions :
   - $F^\perp = \{ \phi \in E^* \mid \forall x \in F, \phi(x) = 0 \}$ (Annulateur dans $E^*$ du sous-espace $F \subset E$).
   - Pour un sous-espace $G \subset E^*$, $G^\circ = \{ x \in E \mid \forall \phi \in G, \Psi(x)(\phi) = 0 \} = \{ x \in E \mid \forall \phi \in G, \phi(x) = 0 \}$.
   Le but est de montrer $(F^\perp)^\circ = F$.

2. **Démonstration de l'inclusion directe $F \subseteq (F^\perp)^\circ$ :**
   Soit $x \in F$.
   Pour prouver que $x \in (F^\perp)^\circ$, il faut vérifier que pour toute forme $\phi \in F^\perp$, l'évaluation donne $\phi(x) = 0$.
   Or, si $\phi \in F^\perp$, par définition même, la forme $\phi$ annule tous les vecteurs de $F$. Comme $x \in F$, on a bien $\phi(x) = 0$.
   Ceci prouve que l'action est réciproque. Donc $x \in (F^\perp)^\circ$.
   L'inclusion $F \subseteq (F^\perp)^\circ$ est établie.

3. **Démonstration de l'égalité par le théorème des dimensions :**
   Appliquons les théorèmes de dimensions des orthogonaux en dimension finie.
   Nous savons que $\dim(F^\perp) = \dim(E) - \dim(F)$.
   De manière strictement analogue pour le sous-espace $G = F^\perp \subseteq E^*$, on a pour l'annulateur dans le primal :
   $\dim(G^\circ) = \dim(E^*) - \dim(G)$.
   En remplaçant :
   $\dim((F^\perp)^\circ) = \dim(E) - \dim(F^\perp)$
   $\dim((F^\perp)^\circ) = \dim(E) - (\dim(E) - \dim(F))$
   $\dim((F^\perp)^\circ) = \dim(F)$.

4. **Conclusion :**
   Nous avons une inclusion vectorielle $F \subseteq (F^\perp)^\circ$ entre deux sous-espaces de même dimension finie.
   Cette condition suffit à garantir l'égalité stricte des ensembles.
   $(F^\perp)^\circ = F$.
