---
title: "Exercice 3 : Distance SNCF (ou du centre spatial)"
---

### Exercice 3 : Distance SNCF (ou du centre spatial) \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $X = \mathbb{R}^2$ et $O$ l'origine $(0,0)$. Soit $\|\cdot\|$ la norme euclidienne standard. On définit la fonction $d$ par :
- $d(A, B) = \|A - B\|$ si $A, B$ et $O$ sont alignés.
- $d(A, B) = \|A\| + \|B\|$ si $A, B$ et $O$ ne sont pas alignés.

Démontrer que $d$ est une distance. Pourquoi l'appelle-t-on souvent la distance de la SNCF ?

**Correction Détaillée :**
Vérifions les trois axiomes d'une distance :

1. **Séparation :** Si $d(A, B) = 0$.
   - Si $A, B, O$ alignés, $\|A - B\| = 0 \implies A = B$.
   - Si non alignés, $\|A\| + \|B\| = 0 \implies \|A\| = 0$ et $\|B\| = 0 \implies A = O$ et $B = O$. Or si $A=O$ et $B=O$, ils sont alignés (avec $O$), contradiction. Donc $A=B$ est l'unique cas d'annulation.
2. **Symétrie :** Claire, par symétrie de la norme et de l'addition.
3. **Inégalité triangulaire :** $d(A, C) \le d(A, B) + d(B, C)$.
   - Cas 1 : $A, B, C$ sur une même droite passant par $O$. Alors $d$ coïncide avec la distance euclidienne, qui vérifie l'inégalité triangulaire.
   - Cas 2 : $A, C, O$ alignés, mais $B$ n'appartient pas à cette droite. Alors $d(A, C) = \|A - C\| \le \|A\| + \|C\|$ (par inégalité triangulaire de la norme).
     De plus, $d(A, B) = \|A\| + \|B\|$ et $d(B, C) = \|B\| + \|C\|$.
     La somme donne $\|A\| + 2\|B\| + \|C\|$, qui est clairement supérieur ou égal à $\|A\| + \|C\|$. L'inégalité est vérifiée.
   - Cas 3 : $A, C, O$ non alignés. $d(A, C) = \|A\| + \|C\|$. Les paires $(A, B)$ et $(B, C)$ ne peuvent pas toutes deux être alignées avec $O$ (sinon $A$ et $C$ le seraient aussi). Au moins l'une donne la somme des normes, ce qui garantit que $d(A,B)+d(B,C) \ge \|A\| + \|C\|$.

Cette métrique est appelée distance de la SNCF (centralisée sur Paris) car pour aller d'une ville A à une ville B, si elles ne sont pas sur la même ligne passant par la capitale, on est obligé de transiter par l'origine.
