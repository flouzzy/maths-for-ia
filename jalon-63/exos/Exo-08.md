---
uuid: "exo-jalon-63-08"
title: "Exercice 8 : Absolue continuité discrète"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Absolue continuité discrète

## Énoncé

Soit $(X, \mathcal{A})$ un espace mesurable muni de deux mesures finies $\mu$ et $\nu$. On dit que $\nu$ est absolument continue par rapport à $\mu$ (noté $\nu \ll \mu$) si pour tout $A \in \mathcal{A}$, $\mu(A) = 0 \implies \nu(A) = 0$. Montrer que l'assertion suivante est équivalente : Pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour tout $A \in \mathcal{A}$, $\mu(A) < \delta \implies \nu(A) < \epsilon$.

## Correction Détaillée

Montrons l'équivalence par double implication.

**Sens réciproque ($\impliedby$) :**
Supposons que la condition en $\epsilon, \delta$ soit vraie. Soit $A \in \mathcal{A}$ tel que $\mu(A) = 0$.
Soit $\epsilon > 0$. Il existe $\delta > 0$ tel que $\mu(A) < \delta \implies \nu(A) < \epsilon$.
Puisque $\mu(A) = 0 < \delta$, on a inévitablement $\nu(A) < \epsilon$.
Cette inégalité étant vraie pour tout $\epsilon > 0$, on en déduit formellement que $\nu(A) = 0$. Donc $\nu \ll \mu$.

**Sens direct ($\implies$) : Raisonnement par l'absurde.**
Supposons $\nu \ll \mu$ mais que la condition en $\epsilon, \delta$ est fausse.
Il existe alors un $\epsilon_0 > 0$ tel que pour tout $\delta > 0$, on peut trouver un ensemble $A \in \mathcal{A}$ vérifiant $\mu(A) < \delta$ mais $\nu(A) \geq \epsilon_0$.
Choisissons successivement $\delta = \frac{1}{2^n}$ pour $n \in \mathbb{N}^*$.
Il existe une suite d'ensembles $(A_n)$ telle que $\mu(A_n) < \frac{1}{2^n}$ et $\nu(A_n) \geq \epsilon_0$.
Définissons $B_N = \bigcup_{n=N}^{\infty} A_n$ et l'événement $\limsup A_n = B = \bigcap_{N=1}^{\infty} B_N$.

Par sous-additivité, $\mu(B_N) \leq \sum_{n=N}^{\infty} \mu(A_n) < \sum_{n=N}^{\infty} \frac{1}{2^n} = \frac{1}{2^{N-1}}$.
Puisque $B$ est l'intersection décroissante des $B_N$ et que $\mu$ est finie, la continuité décroissante donne :
$\mu(B) = \lim_{N \to \infty} \mu(B_N) \leq \lim_{N \to \infty} \frac{1}{2^{N-1}} = 0$.
Donc $\mu(B) = 0$. Par l'hypothèse d'absolue continuité $\nu \ll \mu$, cela force $\nu(B) = 0$.

Cependant, évaluons $\nu$ sur $B$. On a $A_n \subset B_n$, donc $\nu(B_n) \geq \nu(A_n) \geq \epsilon_0$.
Par continuité décroissante appliquée à la mesure finie $\nu$ :
$\nu(B) = \lim_{N \to \infty} \nu(B_N) \geq \epsilon_0 > 0$.
Nous obtenons la contradiction flagrante $\nu(B) = 0$ et $\nu(B) \geq \epsilon_0 > 0$.
L'hypothèse initiale est donc inévitablement vraie. $\blacksquare$
