## Exercice 10 : Sous-espaces fermés et somme directe \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $H$ un espace de Hilbert et $M$ un sous-espace vectoriel de $H$. Montrer que $M$ est fermé si et seulement si $H = M \oplus M^\perp$.

**Correction Détaillée :**
1. **Condition suffisante (Si $H = M \oplus M^\perp$) :**
   Si $H = M \oplus M^\perp$, alors tout élément $x \in H$ s'écrit de manière unique $x = m + n$ avec $m \in M$ et $n \in M^\perp$.
   Considérons le projecteur $P_M: H \to H$ défini par $P_M(x) = m$. $P_M$ est linéaire et continu (car $\|x\|^2 = \|m\|^2 + \|n\|^2 \ge \|m\|^2 = \|P_M(x)\|^2$).
   Le noyau de $I - P_M$ est l'ensemble des $x$ tels que $x - m = 0$, donc $x \in M$.
   $M = \ker(I - P_M)$. Puisque $I - P_M$ est continue, son noyau est un fermé. Donc $M$ est fermé.
2. **Condition nécessaire (Si $M$ est fermé) :**
   Puisque $M$ est un sous-espace vectoriel fermé et convexe d'un espace de Hilbert, le théorème de projection orthogonale s'applique.
   Pour tout $x \in H$, il existe un unique $p \in M$ minimisant la distance. La caractérisation de cette projection est que $(x-p) \in M^\perp$.
   On peut donc écrire $x = p + (x-p)$, avec $p \in M$ et $(x-p) \in M^\perp$. Donc $H = M + M^\perp$.
   De plus, si $y \in M \cap M^\perp$, alors $\langle y, y \rangle = 0 \implies y=0$. La somme est donc directe : $H = M \oplus M^\perp$.
3. **Conclusion :** L'équivalence est démontrée rigoureusement.
